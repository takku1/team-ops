"""Keyword trigger proxy: rank skill descriptions by IDF-weighted word overlap with eval prompts (skill names stripped).

Usage: python scripts/trigger_proxy.py plugins evals. A cheap regression check for description edits; real routing is measured by run_scenarios.py.
"""
import json, math, re, sys
from pathlib import Path
plugins, evals = Path(sys.argv[1]), Path(sys.argv[2])
STOP = set('a an the and or of to for in on with is are be by as at it its this that from not use when your you any into can do does we our their them they what which who how was were has have had but if then than so no only all each one per via vs'.split())
def words(t):
    out = set()
    for w in re.findall(r'[a-z][a-z0-9]+', t.lower()):
        if w in STOP or len(w) < 3: continue
        out.add(w[:6])  # crude stemming
    return out
desc = {}
for p in plugins.glob('*/skills/*/SKILL.md'):
    m = re.search(r'^description: (.*)$', p.read_text(encoding='utf-8'), re.M)
    desc[p.parent.name] = words(m.group(1))
df = {}
for ws in desc.values():
    for w in ws: df[w] = df.get(w, 0) + 1
idf = {w: math.log(len(desc) / c) + 0.1 for w, c in df.items()}
top1 = top3 = n = 0; misses = []
for d in sorted(evals.iterdir()):
    if not (d / 'prompt.md').exists(): continue
    target = json.loads((d / 'case.json').read_text())['skills']
    text = (d / 'prompt.md').read_text(encoding='utf-8').split('---', 2)[-1]
    for s in desc: text = re.sub(re.escape(s), ' ', text, flags=re.I)
    pw = words(text)
    ranked = sorted(desc, key=lambda s: -sum(idf[w] for w in desc[s] & pw))
    n += 1; best = min(ranked.index(t) for t in target)
    top1 += best == 0; top3 += best < 3
    if best >= 3: misses.append(f'{d.name}->{target} got {ranked[:3]}')
print(f'top1 {top1}/{n}  top3 {top3}/{n}')
for m in misses: print('  miss', m)
