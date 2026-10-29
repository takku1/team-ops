"""Re-grade a scenario run's records with an independent judge from another model family (Codex CLI).

Rebuilds the same blind judge prompt from stored transcripts, writes verdicts beside the originals
(`rejudge/<arm>/<case>.r<n>.json`), and reports agreement with the primary judge. Calls are billed.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import shutil
import subprocess

import run_scenarios as rs

VERDICTS = ('pass', 'partial', 'fail')


def judge_prompt(run: Path, record: dict, work_root: Path | None) -> str:
    case_dir = rs.EVALS / record['case']
    _, prompt = rs.frontmatter(case_dir / 'prompt.md')
    _, rubric = rs.frontmatter(case_dir / 'graders' / 'criteria.md')
    name = f"{record['case']}.r{record['repeat']}"
    stdout = (run / 'transcripts' / record['arm'] / f'{name}.jsonl').read_text(encoding='utf-8')
    events, final, _ = rs.parse_stream(stdout)
    work = work_root / record['arm'] / name if work_root else None
    files = rs.changed_files(case_dir, work) if work and work.exists() else []
    return rs.JUDGE.format(prompt=prompt, rubric=rubric,
                           trace='\n'.join(f'{n}: {i}' for n, i in events[:60]) or '(none)',
                           files='\n'.join(files)[:9000] or '(none)',
                           oracle=json.dumps(record['oracle']) if record.get('oracle') else '(none for this scenario)',
                           answer=(final.get('result') or '')[:12000])


def codex(prompt: str, cwd: Path, timeout: int) -> dict:
    try:
        # npm installs codex as a .cmd shim, which CreateProcess will not find by bare name.
        out = subprocess.run([shutil.which('codex') or 'codex', 'exec', '--skip-git-repo-check', '--sandbox', 'read-only', '-'],
                             input=prompt, cwd=cwd, capture_output=True, text=True,
                             encoding='utf-8', errors='replace', timeout=timeout)
    except subprocess.TimeoutExpired:
        return {'verdict': 'ungraded', 'reason': 'timeout'}
    found = re.findall(r'\{[^{}]*"verdict"[^{}]*\}', out.stdout)
    try:
        verdict = json.loads(found[-1])
        if verdict.get('verdict') in VERDICTS:
            return verdict
    except (IndexError, json.JSONDecodeError):
        pass
    return {'verdict': 'ungraded', 'reason': (out.stdout + out.stderr)[-400:]}


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    pe = sum((sum(a == v for a, _ in pairs) / n) * (sum(b == v for _, b in pairs) / n) for v in VERDICTS)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run', type=Path, required=True, help='scenario run directory')
    p.add_argument('--work', type=Path, help='workspace root used for that run (for changed files)')
    p.add_argument('--jobs', type=int, default=2)
    p.add_argument('--timeout', type=int, default=300)
    opts = p.parse_args()
    run = opts.run.resolve()
    records = [json.loads(f.read_text(encoding='utf-8')) for f in sorted((run / 'records').rglob('*.json'))]

    def one(record):
        out = run / 'rejudge' / record['arm'] / f"{record['case']}.r{record['repeat']}.json"
        if out.exists():
            return json.loads(out.read_text(encoding='utf-8'))
        verdict = codex(judge_prompt(run, record, opts.work), run, opts.timeout)
        if verdict['verdict'] != 'ungraded':
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(verdict, indent=2), encoding='utf-8')
        print(f"{record['arm']:9} {record['case']:44} primary={record['judge']['verdict']:8} second={verdict['verdict']}", flush=True)
        return verdict

    with ThreadPoolExecutor(opts.jobs) as pool:
        seconds = list(pool.map(one, records))
    pairs = [(r['judge']['verdict'], s['verdict']) for r, s in zip(records, seconds)
             if r['judge']['verdict'] in VERDICTS and s['verdict'] in VERDICTS]
    if pairs:
        print(f'graded {len(pairs)}/{len(records)}; exact agreement {sum(a == b for a, b in pairs) / len(pairs):.2f}; '
              f'Cohen kappa {kappa(pairs):.2f}')


if __name__ == '__main__':
    main()
