"""Refresh manifests from ACTIVE skills; never read or write skillwren-src.

Usage: python scripts/refresh-skillwren-builds.py --tool-root Z:/SkillWren
The toolchain performs static validation/packaging, not behavioral enforcement.
"""
import argparse
import json
from pathlib import Path
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tool-root', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    tool_src = args.tool_root.resolve()/'src'
    if not (tool_src/'skillwren').is_dir():
        parser.error('tool-root must contain src/skillwren')
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(tool_src))
    from skillwren.compiler import _compile
    from skillwren.validator import validate_file
    # These are literal, single-file builds. Avoid temporary directories, which
    # can receive inaccessible ACLs in a managed Windows workspace. Validate all
    # candidates before replacing any manifest; archive files are never inputs.
    built = []
    for active in sorted((root/'skills').glob('*/manifest.json')):
        entry = active.parent/'SKILL.md'
        content, manifest = _compile(entry)
        if content != entry.read_bytes() or manifest['contexts']:
            raise RuntimeError(f'Only unchanged literal builds are supported: {entry}')
        errors, warnings = validate_file(entry)
        if errors:
            raise RuntimeError(f'{entry}: {errors}')
        manifest['warnings'] = [dict(line=d.line, rule=d.rule, message=d.msg) for d in warnings]
        built.append((active, json.dumps(manifest, indent=2) + '\n'))
    for destination, content in built:
        staged = destination.with_suffix('.next.json')
        staged.write_text(content, encoding='utf-8')
        staged.replace(destination)
    print(f'Refreshed {len(built)} active manifests; archival sources untouched.')

if __name__ == '__main__':
    main()
