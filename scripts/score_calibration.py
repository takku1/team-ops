"""Score human calibration grades against each AI judge: python scripts/score_calibration.py evals/calibration/round-1"""
import csv
import json
import sys
from pathlib import Path

VERDICTS = ('pass', 'partial', 'fail')


def main():
    root = Path(sys.argv[1])
    key = json.loads((root / '.key.json').read_text(encoding='utf-8'))
    with (root / 'grades.csv').open(encoding='utf-8') as f:
        grades = {row['item'].zfill(2): row for row in csv.DictReader(f) if row['verdict'].strip()}
    if not grades:
        sys.exit('no grades filled in yet')
    for judge in ('opus', 'codex'):
        rows = [(g['verdict'].strip().lower(), key[i][judge]) for i, g in grades.items() if g['verdict'].strip().lower() in VERDICTS]
        dis = [(h, j) for (i, g), (h, j) in zip(grades.items(), rows) if key[i]['disagreement']]
        print(f'{judge:6} agrees with you on {sum(h == j for h, j in rows)}/{len(rows)} '
              f'(on judge disagreements: {sum(h == j for h, j in dis)}/{len(dis)}); '
              f'more lenient than you on {sum(VERDICTS.index(j) < VERDICTS.index(h) for h, j in rows)}')
    severe = [i for i, g in grades.items() if g.get('severe', '').strip().lower() in ('y', 'yes', 'true')]
    print('items you marked severe:', severe or 'none')


if __name__ == '__main__':
    main()
