"""Single-host, opt-in deterministic check reuse. See references/coordination.md."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def fingerprint(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def identity_details(cwd: Path, inputs: list[str], command: list[str], tag: str) -> dict:
    """Hash declared inputs, including names/modes and untracked directory entries."""
    entries = {}
    for value in inputs:
        path = cwd / value
        if not path.is_absolute():
            path = path.absolute()
        # Reject symlink components, not just a symlink at the leaf.
        if any(p.is_symlink() for p in (path, *path.parents)):
            raise ValueError(f'symlink input is unsupported: {value}')
        path = path.resolve(strict=True)
        if not path.is_relative_to(cwd):
            raise ValueError(f'input outside workspace: {value}')
        paths = [path, *sorted(path.rglob('*'))] if path.is_dir() else [path]
        for item in paths:
            if item.is_symlink():
                raise ValueError(f'symlink input is unsupported: {item}')
            relative = item.relative_to(cwd).as_posix()
            mode = item.stat().st_mode
            if item.is_file():
                entries[relative] = [mode, digest_file(item)]
            elif item.is_dir():
                entries[relative] = [mode, 'directory']
            else:
                raise ValueError(f'non-file input is unsupported: {item}')
    # Store only category fingerprints, never environment values or per-secret hashes.
    return {
        'workspace': fingerprint(str(cwd)), 'inputs': fingerprint(entries),
        'input_scope': fingerprint(sorted(set(inputs))), 'command': fingerprint(command),
        'executable': digest_file(Path(command[0])), 'toolchain': fingerprint(tag),
        'environment': fingerprint(sorted(os.environ.items())), 'platform': fingerprint(sys.platform),
    }


def identity(cwd: Path, inputs: list[str], command: list[str], tag: str) -> str:
    return fingerprint({'schema': 2, 'components': identity_details(cwd, inputs, command, tag)})


@contextmanager
def lane_lock(path: Path, timeout: float):
    """OS-owned local lock. Never steal a lock based on timestamps."""
    with path.open('a+b') as stream:
        stream.seek(0, os.SEEK_END)
        if stream.tell() == 0:
            stream.write(b'0')
            stream.flush()
        deadline = time.monotonic() + timeout
        while True:
            try:
                stream.seek(0)
                if os.name == 'nt':
                    import msvcrt
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except (BlockingIOError, OSError):
                if time.monotonic() >= deadline:
                    raise TimeoutError('check lane is busy; retry after its owner completes')
                time.sleep(0.05)
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def read_reusable(path: Path, key: str) -> dict | None:
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
        if (value.get('input_id') == key and value.get('exit_code') == 0
                and value.get('stable') is True
                and all(Path(value[k]).is_file() for k in ('stdout_log', 'stderr_log'))):
            return value
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        pass
    return None


def cache_decision(state: Path, key: str, components: dict) -> tuple[dict | None, dict]:
    cached = state / f'{key}.json'
    reusable = read_reusable(cached, key)
    if reusable:
        return reusable, {'outcome': 'hit', 'reasons': ['matching_successful_execution']}
    try:
        prior = json.loads((cached if cached.exists() else state / 'latest.json').read_text(encoding='utf-8'))
        if not isinstance(prior, dict):
            raise ValueError('record is not an object')
    except FileNotFoundError:
        return None, {'outcome': 'miss', 'reasons': ['no_prior_execution']}
    except (OSError, ValueError):
        return None, {'outcome': 'miss', 'reasons': ['record_unreadable_or_invalid']}
    old = prior.get('identity_components')
    reasons = ([f'{name}_changed' for name, value in components.items() if old.get(name) != value]
               if isinstance(old, dict) else ['identity_details_unavailable'])
    if prior.get('exit_code') != 0:
        reasons.append('prior_execution_failed')
    if prior.get('stable') is not True:
        reasons.append('prior_inputs_unstable')
    if not all(isinstance(prior.get(k), str) and Path(prior[k]).is_file()
               for k in ('stdout_log', 'stderr_log')):
        reasons.append('prior_logs_missing')
    return None, {'outcome': 'miss', 'reasons': reasons or ['no_matching_success_record'],
                  'compared_execution': prior.get('execution_id')}


def write_json(path: Path, value: dict):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    os.replace(temporary, path)


def run(args: argparse.Namespace) -> tuple[dict, int]:
    cwd = Path(args.cwd).resolve(strict=True)
    if not cwd.is_dir():
        raise ValueError('cwd must be a directory')
    state = Path(args.state_dir).resolve()
    if state.is_relative_to(cwd):
        raise ValueError('state-dir must be outside the checked workspace')
    command = args.command[1:] if args.command[:1] == ['--'] else args.command
    if not command:
        raise ValueError('a command after -- is required')
    # Resolve relative executables against the command cwd, not the caller cwd.
    if '/' in command[0] or '\\' in command[0]:
        executable = str((cwd / command[0]).resolve(strict=True))
    else:
        # Explicit search avoids Windows' implicit caller-directory lookup.
        suffixes = ['.exe', '.com'] if os.name == 'nt' and not Path(command[0]).suffix else ['']
        executable = next((str(candidate) for entry in os.get_exec_path()
                           for suffix in suffixes
                           if (candidate := (cwd / entry / (command[0] + suffix)).absolute()).is_file()
                           and os.access(candidate, os.X_OK)), None)
    if not executable:
        raise ValueError(f'executable not found: {command[0]}')
    if os.name == 'nt' and Path(executable).suffix.lower() in ('.bat', '.cmd'):
        raise ValueError('use a real executable; batch wrappers require an explicit shell command')
    command = [str(Path(executable).resolve()), *command[1:]]
    state.mkdir(parents=True, exist_ok=True)
    # A single lane avoids contention between different commands sharing outputs.
    with lane_lock(state / 'lane.lock', args.lock_timeout):
        components = identity_details(cwd, args.input, command, args.identity)
        key = fingerprint({'schema': 2, 'components': components})
        cached = state / f'{key}.json'
        previous, decision = cache_decision(state, key, components)
        if getattr(args, 'explain', False):
            return {'schema': 2, 'inspection_only': True, 'input_id': key,
                    'would_reuse': previous is not None, 'cache': decision}, 0
        if args.reuse:
            if previous:
                return {**previous, 'reused': True, 'cache': decision}, 0
        else:
            decision = {'outcome': 'fresh', 'reasons': ['fresh_execution_requested'],
                        'reuse_eligibility': decision}
        # Invalidate before launch: launch/logging failures must not leave old green.
        cached.unlink(missing_ok=True)
        # Preserve a tombstone if launch/log creation fails; explanations cannot cite older green.
        write_json(state / 'latest.json', {'schema': 2, 'input_id': key,
                   'identity_components': components, 'exit_code': None, 'stable': False,
                   'state': 'execution_started', 'cache': decision})
        execution = uuid.uuid4().hex
        stdout = state / f'{execution}.stdout.log'
        stderr = state / f'{execution}.stderr.log'
        started = time.time()
        with stdout.open('wb') as out, stderr.open('wb') as err:
            completed = subprocess.run(command, cwd=cwd, stdout=out, stderr=err,
                                       check=False, stdin=subprocess.DEVNULL)
        try:
            stable = identity(cwd, args.input, command, args.identity) == key
        except (OSError, ValueError):
            stable = False
        result = {
            'schema': 2, 'execution_id': execution, 'input_id': key,
            'identity_components': components, 'cache': decision,
            'command': command, 'cwd': str(cwd), 'exit_code': completed.returncode,
            'stable': stable, 'reused': False, 'started_unix': started,
            'elapsed_seconds': round(time.time() - started, 3),
            'stdout_log': str(stdout), 'stderr_log': str(stderr),
        }
        write_json(state / f'{execution}.result.json', result)
        write_json(state / 'latest.json', result)
        # A subsequent fresh failure must invalidate an earlier green record.
        if stable and completed.returncode == 0:
            write_json(cached, result)
        else:
            cached.unlink(missing_ok=True)
        return result, (0 if completed.returncode == 0 and stable else 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cwd', required=True)
    parser.add_argument('--state-dir', required=True)
    parser.add_argument('--input', action='append', required=True,
                        help='Complete file or directory input; repeat as needed')
    parser.add_argument('--identity', required=True,
                        help='Toolchain/dependency identity not captured by input files')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--reuse', action='store_true', help='Assert deterministic, complete inputs')
    mode.add_argument('--fresh', action='store_true', help='Always execute (default)')
    mode.add_argument('--explain', action='store_true', help='Explain reuse eligibility without executing')
    parser.add_argument('--lock-timeout', type=float, default=60)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not math.isfinite(args.lock_timeout) or args.lock_timeout < 0:
        parser.error('lock-timeout must be finite and nonnegative')
    try:
        result, code = run(args)
        print(json.dumps(result))
        return code
    except (OSError, ValueError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
