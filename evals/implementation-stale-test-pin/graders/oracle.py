"""Pass when the suite passes, the pin asserts the new mapping, production is unchanged, and STATUS is updated."""
import re, shutil, subprocess, sys, tempfile
from pathlib import Path
work, fixtures = Path(sys.argv[1]), Path(__file__).parents[1] / 'fixtures'
test = (work / 'test_keymap.py').read_text(encoding='utf-8')
gap = re.search(r'def test_keymap_gap\(self\):(.*?)(?=\n    def |\nif __name__|\Z)', test, re.S)
pinned = bool(gap) and re.search(r'assertEqual\(\s*lookup\(0x4B\)\s*,\s*0x49\s*\)', gap.group(1)) is not None
others_kept = 'assertIsNone(lookup(0x99))' in test and 'assertEqual(lookup(0x4D), 0x4D)' in test
production = (work / 'keymap.py').read_text(encoding='utf-8') == (fixtures / 'keymap.py').read_text(encoding='utf-8')
status = (work / 'STATUS.md').read_text(encoding='utf-8')
open_section = status.split('## Open problems', 1)[-1].split('\n## ', 1)[0]
status_ok = 'test_keymap_gap' not in open_section
with tempfile.TemporaryDirectory() as tmp:
    shutil.copy2(work / 'keymap.py', tmp); shutil.copy2(work / 'test_keymap.py', tmp)
    suite = subprocess.run([sys.executable, '-m', 'unittest', '-q'], cwd=tmp, capture_output=True, text=True)
print(f'pinned={pinned} others_kept={others_kept} production_unchanged={production} status_updated={status_ok} suite_exit={suite.returncode}')
sys.exit(0 if pinned and others_kept and production and status_ok and suite.returncode == 0 else 1)
