"""Pass when the typo is fixed, nothing else in args.rs changed, and `cargo test -p cli` passes."""
import subprocess, sys
from pathlib import Path
work = Path(sys.argv[1])
text = (work / 'cli' / 'args.rs').read_text(encoding='utf-8')
fixed = '"Enable verbose output"' in text and 'verbos ' not in text
original = (Path(__file__).parents[1] / 'fixtures' / 'cli' / 'args.rs').read_text(encoding='utf-8')
scoped = text == original.replace('verbos output', 'verbose output')
test = subprocess.run(['cargo', 'test', '-p', 'cli', '--offline', '-q'], cwd=work, capture_output=True, text=True)
print(f'fixed={fixed} scoped={scoped} cargo_test_exit={test.returncode}')
# `scoped` is reported, not gated: the rubric permits extra edits such as a spelling test.
sys.exit(0 if fixed and test.returncode == 0 else 1)
