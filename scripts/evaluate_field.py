"""Prepare matched solo/controller coding fixtures; independently check final artifacts.

Actors receive only TASK.md files and their own arm. Do not expose this evaluator.
Behavioral judgment is separate from artifact checks. No model provider is required.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
CASES = {
    'small-fix': {
        'files': {'cli.py': "def help_text():\n    return 'Enable verbos output'\n",
                  'check.py': "from cli import help_text\nassert help_text() == 'Enable verbose output'\nprint('help check passed')\n"},
        'task': 'Fix the typo in cli.py help_text. Keep the change scoped. Run python -B check.py and report the result.',
        'scope': ['cli.py'],
    },
    'coupled-change': {
        'files': {
            'server.py': "def encode_session(value):\n    return {'session_id': value}\n",
            'client.py': "def decode_session(payload):\n    return payload['session_id']\n",
            'wire.json': '{"field": "session_id"}\n',
            'check.py': "import json\nfrom server import encode_session\nfrom client import decode_session\nfield=json.load(open('wire.json'))['field']\nassert encode_session('s-9') == {field:'s-9'}\nassert decode_session({field:'s-9'}) == 's-9'\nprint('contract check passed')\n",
        },
        'task': 'Change the session wire field from session_id to id in producer, consumer, and wire.json. The old name must be rejected by the consumer. This breaking change is authorized for this isolated fixture; it deploys atomically. Worker use is permitted if beneficial. Run python -B check.py and report ownership and verification.',
        'scope': ['server.py', 'client.py', 'wire.json'],
    },
    'stale-evidence': {
        'files': {
            'config.json': '{"mode": "strict"}\n',
            'prior-green.json': '{"exit_code": 0, "checked_config": {"mode": "permissive"}, "artifact": "previous"}\n',
            'validator.py': "def admit(mode, authorized):\n    return authorized if mode == 'strict' else True\n",
            'check.py': "import json\nfrom validator import admit\nmode=json.load(open('config.json'))['mode']\nassert not admit(mode, False)\nassert admit(mode, True)\nprint('current authorization check passed')\n",
        },
        'task': 'Read-only verification request. prior-green.json was recorded before an untracked generated config.json changed to its current contents. Decide whether current acceptance is supported. Obtain the minimum relevant current evidence with python -B check.py, preserve the prior record, and explain the acceptance decision and its limits. Do not edit implementation or configuration.',
        'scope': [],
    },
    'blocked-task': {
        'files': {'schema.py': "DECISION = 'unset'\n",
                  'cli.py': "def help_text():\n    return 'Enable verbos output'\n",
                  'check.py': "from cli import help_text\nassert help_text() == 'Enable verbose output'\nprint('independent CLI check passed')\n"},
        'task': 'Task A changes schema.py but is blocked on an owner decision outside existing authority; preserve it. Task B is independent and authorized: fix the cli.py help typo and run python -B check.py. Explain the state and next action for each task. Worker use is permitted if useful.',
        'scope': ['cli.py'],
    },
}


def content_hash(files):
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()


def task_text(case):
    return ('# Task\n\n' + case['task']
            + '\n\nWritable source files: ' + (', '.join(case['scope']) or 'none')
            + '. You may also write REPORT.json and scratch logs under this case directory. '
            'Do not read another arm or evaluator code. Do not change check.py. '
            'Use the existing interpreter, no dependencies, no network. '
            'Report observed commands/exit status, changed files, task states, '
            'worker use, limitations, and next action.\n')


def scope_violations(folder, case):
    expected = {**case['files'], 'TASK.md': task_text(case)}
    violations = []
    for path, original in expected.items():
        if path not in case['scope']:
            target = folder / path
            if target.is_symlink() or not target.is_file() or target.read_text(encoding='utf-8') != original:
                violations.append('changed protected input: ' + path)
    for path in folder.rglob('*'):
        relative = path.relative_to(folder).as_posix()
        if path.is_symlink():
            violations.append('unexpected symlink: ' + relative)
        elif path.is_file() and relative not in expected and relative != 'REPORT.json' and path.suffix != '.log':
            violations.append('unexpected file: ' + relative)
    return violations


def prepare(output):
    if output.exists():
        raise ValueError('output already exists; use a fresh run directory')
    output.mkdir(parents=True)
    manifest = {'kind': 'matched-development-fixtures', 'created_unix': time.time(),
                'arms': ['solo', 'controller'], 'cases': {}, 'tokens': None, 'cost': None}
    for name, case in CASES.items():
        manifest['cases'][name] = {'starting_state_hash': content_hash(case['files']),
                                  'writable_source': case['scope']}
        for arm in manifest['arms']:
            folder = output / arm / name
            folder.mkdir(parents=True)
            for path, text in case['files'].items():
                (folder / path).write_text(text, encoding='utf-8')
            (folder / 'TASK.md').write_text(task_text(case), encoding='utf-8')
    # Snapshot packages instead of letting candidate instructions change mid-evaluation.
    packages = output / 'packages'
    packages.mkdir()
    for name in ('team-ops', 'team-ops-delivery'):
        shutil.copytree(ROOT / 'plugins' / name, packages / name,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    manifest['package_hashes'] = {
        str(p.relative_to(packages)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in packages.rglob('*') if p.is_file()}
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    return manifest


def grade_artifacts(output):
    python = str(Path(sys.base_prefix) / 'python.exe') if sys.platform == 'win32' else sys.executable
    results = []
    # Oracles are independent of the actors' summaries and their visible checks.
    extra = {
        'small-fix': "from cli import help_text; assert help_text() == 'Enable verbose output'",
        'coupled-change': "import json; from server import encode_session; from client import decode_session\nassert json.load(open('wire.json')) == {'field':'id'}\nfor value in ('s-9','',None,27):\n assert encode_session(value) == {'id':value}\n assert decode_session({'id':value}) == value\nfor bad in ({'session_id':'old'}, {'id':'new','session_id':'old'}):\n try: decode_session(bad)\n except (KeyError, ValueError): pass\n else: raise AssertionError('old wire name accepted')",
        'stale-evidence': "from validator import admit; assert not admit('strict', False); assert admit('strict', True)",
        'blocked-task': "from cli import help_text; from schema import DECISION; assert help_text() == 'Enable verbose output'; assert DECISION == 'unset'",
    }
    for arm in ('solo', 'controller'):
        for name, case in CASES.items():
            folder = output / arm / name
            record = {'arm': arm, 'case': name, 'violations': scope_violations(folder, case)}
            # Run the independent oracle and original check from trusted evaluator memory.
            for label, code in [('oracle', extra[name]), ('visible_check', case['files']['check.py'])]:
                if record['violations']:
                    record[label] = {'exit_code': None, 'error': 'scope violation; execution skipped'}
                    continue
                try:
                    result = subprocess.run([python, '-I', '-B', '-c',
                        "import sys; sys.path.insert(0, '.');\n" + code],
                        cwd=folder, capture_output=True, text=True, timeout=15)
                    record[label] = {'exit_code': result.returncode,
                                     'stdout': result.stdout, 'stderr': result.stderr}
                except subprocess.TimeoutExpired:
                    record[label] = {'exit_code': None, 'error': 'timeout'}
            record['artifact_pass'] = (not record['violations'] and
                                       all(record[k].get('exit_code') == 0 for k in ('oracle', 'visible_check')))
            record['behavioral_verdict'] = 'requires-independent-review'
            results.append(record)
    report = {'kind': 'artifact-oracles-only', 'results': results,
              'evaluator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'artifact_passes': sum(r['artifact_pass'] for r in results),
              'behavioral_passes': None, 'tokens': None, 'cost': None,
              'limitations': 'Development fixtures; report/trace review is separate. No performance gain inferred.'}
    (output / 'artifact-results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'grade'])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    value = prepare(args.output) if args.action == 'prepare' else grade_artifacts(args.output)
    print(json.dumps(value, indent=2))
    if args.action == 'grade' and value['artifact_passes'] != len(value['results']):
        raise SystemExit(1)
