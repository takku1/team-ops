"""Rerun the pristine fixture tests against the resulting parser."""
import shutil, subprocess, sys, tempfile
from pathlib import Path
work, fixtures = Path(sys.argv[1]), Path(__file__).parents[1] / 'fixtures'
with tempfile.TemporaryDirectory() as tmp:
    shutil.copy2(work / 'parser.py', tmp)
    shutil.copy2(fixtures / 'test_parser.py', tmp)
    r = subprocess.run([sys.executable, '-m', 'unittest', '-q'], cwd=tmp, capture_output=True, text=True)
print(r.stdout + r.stderr)
sys.exit(r.returncode)
