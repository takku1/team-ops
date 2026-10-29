"""Validate both plugins: metadata, supporting links, evidence IDs, and eval coverage.

Requires PyYAML. This does not execute or grade behavioral eval scenarios.
"""
import json
from pathlib import Path
import re
import sys
import yaml
from package_resources import synchronize

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ['team-ops', 'team-ops-delivery']
# Descriptions load into every session; keep them short enough to stay cheap.
MAX_DESCRIPTION = 260
RETIRED = {'eng-policy-lead', 'org-team-topology', 'org-ownership-raci', 'org-capacity-plan',
           'plan-delivery-cadence', 'plan-estimate-forecast', 'plan-late-recovery',
           'plan-decision-record', 'measure-delivery-health', 'ai-workflow-efficiency',
           'secure-threat-model', 'secure-supply-chain'}

def main():
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    def frontmatter(p):
        text = p.read_text(encoding='utf-8')
        match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        check(bool(match), f'{p}: missing frontmatter')
        try:
            meta = yaml.safe_load(match.group(1)) if match else {}
        except yaml.YAMLError as exc:
            check(False, f'{p}: invalid YAML: {exc}')
            meta = {}
        check(isinstance(meta, dict), f'{p}: frontmatter must be a mapping')
        return (meta if isinstance(meta, dict) else {}), text

    def links(p, text):
        check(text.count('```') % 2 == 0, f'{p}: unmatched fence')
        check(not any(ord(c) < 32 and c not in '\r\n\t' for c in text), f'{p}: control character')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            check((p.parent/target.split('#')[0]).exists(), f'{p}: broken local link {target}')

    register = (ROOT/'docs/current/research-evidence.md').read_text(encoding='utf-8')
    check(not synchronize(check=True), 'packaged references drifted; run python scripts/package_resources.py')
    ids = set(re.findall(r'\b[RP]\d{2}\b', register))
    skills = {plugin: {} for plugin in PLUGINS}
    agents = {}
    always_on = 0
    body_words = 0
    support_words = 0
    versions = set()
    for plugin in PLUGINS:
        base = ROOT/'plugins'/plugin
        manifest = json.loads((base/'.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        check(manifest['name'] == plugin, f'{plugin}: manifest name mismatch')
        check(bool(re.fullmatch(r'\d+\.\d+\.\d+', manifest.get('version', ''))),
              f'{plugin}: invalid package version')
        versions.add(manifest.get('version'))
        for p in sorted((base/'skills').glob('*/SKILL.md')):
            meta, text = frontmatter(p)
            name = meta.get('name')
            description = meta.get('description')
            check(name == p.parent.name, f'{p}: name does not match directory')
            check(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name or '')), f'{p}: invalid name')
            check(isinstance(description, str) and 0 < len(description) <= MAX_DESCRIPTION,
                  f'{p}: description missing or over {MAX_DESCRIPTION} chars')
            check(all(name not in s for s in skills.values()), f'{p}: duplicate skill name')
            skills[plugin][name] = p
            always_on += len(description or '')
            body_words += len(text.split('---', 2)[-1].split())
            refs = set(re.findall(r'\b(?:R\d{2}|P0\d)\b', text))
            check(bool(refs), f'{p}: no research/practice evidence IDs')
            check(refs <= ids, f'{p}: unknown evidence IDs {refs - ids}')
            check('research-evidence.md' in text, f'{p}: no evidence register link')
            links(p, text)
        for p in sorted((base/'skills').glob('*/references/*.md')):
            text = p.read_text(encoding='utf-8')
            support_words += len(text.split())
            links(p, text)
        for p in sorted((base/'references').glob('*.md')):
            links(p, p.read_text(encoding='utf-8'))
        # Installed bundles must work without the suite checkout or its sibling plugin.
        for p in base.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
                if target.startswith(('https://', 'http://', '#', 'mailto:')):
                    continue
                resolved = (p.parent/target.split('#')[0]).resolve()
                check(resolved.is_relative_to(base.resolve()), f'{p}: link escapes installed package: {target}')
        for p in sorted((base/'agents').glob('*.md')) if (base/'agents').exists() else []:
            meta, text = frontmatter(p)
            check(meta.get('name') == p.stem, f'{p}: name does not match file')
            description = meta.get('description')
            check(isinstance(description, str) and 0 < len(description) <= MAX_DESCRIPTION,
                  f'{p}: description missing or over {MAX_DESCRIPTION} chars')
            always_on += len(description or '')
            links(p, text)
            check('Skill' in str(meta.get('tools')), f'{p}: cannot load its playbooks')
            check(bool(re.findall(r'team-ops:([a-z0-9-]+)', text)), f'{p}: names no playbook skill')
            check('STATUS: done | blocked | needs-decision' in text, f'{p}: missing handoff report shape')
            agents[p.stem] = p

    every = [p for s in skills.values() for p in s.values()] + list(agents.values())
    for p in every:
        text = p.read_text(encoding='utf-8')
        stale = {r for r in RETIRED if re.search(rf'\b{r}\b', text)}
        check(not stale, f'{p}: references retired skills {stale}')
        for plugin in PLUGINS:
            for ref in re.findall(rf'`{plugin}:([a-z0-9-]+)`', text):
                check(ref in skills[plugin] or (plugin == 'team-ops' and ref in agents),
                      f'{p}: unknown reference {plugin}:{ref}')
        for role in re.findall(r'agents/([a-z0-9-]+)\.md', text):
            check(role in agents, f'{p}: unknown agent file {role}')

    all_skills = {n for s in skills.values() for n in s}
    coverage = set()
    cases = 0
    for d in sorted((ROOT/'evals').iterdir()):
        if not d.is_dir() or not (d/'prompt.md').exists():
            continue
        cases += 1
        meta = json.loads((d/'case.json').read_text(encoding='utf-8'))
        check(set(meta['skills']) <= all_skills, f'{d}: unknown skill target')
        coverage.update(meta['skills'])
        fm, prompt = frontmatter(d/'prompt.md')
        check(isinstance(fm.get('max_turns'), int) and fm['max_turns'] > 0, f'{d}: bad turn budget')
        check(bool(fm.get('allowed_tools')), f'{d}: missing tool scope')
        grade, rubric = frontmatter(d/'graders/criteria.md')
        check(grade.get('type') == 'llm' and grade.get('weight', 0) > 0, f'{d}: bad grader')
        check(len(prompt) > 100 and len(rubric) > 100, f'{d}: empty case')
    check(coverage == all_skills, f'Uncovered skills: {all_skills - coverage}')
    check(len(versions) == 1, 'companion plugins must share a release version')

    for name in ('README.md', 'docs/STATUS.md', 'evals/PROTOCOL.md'):
        p = ROOT/name
        links(p, p.read_text(encoding='utf-8'))

    market = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    for entry in market['plugins']:
        manifest = json.loads((ROOT/entry['source']/'.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        check(manifest['version'] == entry['version'], f'{entry["name"]}: version mismatch')
    report = {'kind': 'static-package-validation',
              'skills': {plugin: len(s) for plugin, s in skills.items()}, 'agents': len(agents),
              'always_on_description_chars': always_on, 'eval_cases': cases,
              'skill_body_words': body_words, 'on_demand_reference_words': support_words,
              'skills_with_scenarios': len(coverage), 'errors': errors,
              'behavioral_evals_executed': False}
    print(json.dumps(report, indent=2))
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
