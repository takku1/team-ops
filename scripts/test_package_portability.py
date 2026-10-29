"""Round-trip each plugin alone into an isolated host-like cache, then use it."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unittest
import uuid
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CHECK_PYTHON = str(Path(sys.base_prefix) / 'python.exe') if os.name == 'nt' else sys.executable


class PackagePortabilityTests(unittest.TestCase):
    def setUp(self):
        self.base = ROOT / ('_package_test_' + uuid.uuid4().hex)
        self.base.mkdir()
        self.addCleanup(self.cleanup)

    def cleanup(self):
        target = self.base.resolve()
        if target.parent != ROOT.resolve() or not target.name.startswith('_package_test_'):
            raise ValueError('cleanup outside workspace')
        shutil.rmtree(target)

    def cached_package(self, plugin):
        source = ROOT / 'plugins' / plugin
        archive = self.base / (plugin + '.zip')
        with zipfile.ZipFile(archive, 'w') as output:
            for path in source.rglob('*'):
                if path.is_file() and '__pycache__' not in path.parts:
                    output.write(path, path.relative_to(source))
        cached = self.base / 'cache' / plugin / 'package'
        with zipfile.ZipFile(archive) as incoming:
            incoming.extractall(cached)
        return cached

    def test_each_cached_plugin_has_only_resolvable_internal_links(self):
        for plugin in ('team-ops', 'team-ops-delivery'):
            with self.subTest(plugin=plugin):
                cached = self.cached_package(plugin)
                manifest = json.loads((cached / '.claude-plugin/plugin.json').read_text())
                self.assertEqual(manifest['name'], plugin)
                for path in cached.rglob('*.md'):
                    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                        if target.startswith(('https://', 'http://', '#', 'mailto:')):
                            continue
                        resolved = (path.parent / target.split('#')[0]).resolve()
                        self.assertTrue(resolved.is_relative_to(cached.resolve()), (path, target))
                        self.assertTrue(resolved.exists(), (path, target))

    def test_helper_runs_from_cached_core_without_checkout_imports(self):
        cached = self.cached_package('team-ops')
        work = self.base / 'fixture'
        work.mkdir()
        (work / 'input.txt').write_text('fixture', encoding='utf-8')
        (work / 'check.py').write_text("assert open('input.txt').read() == 'fixture'\n", encoding='utf-8')
        runner = cached / 'skills/team-lead/scripts/check_runner.py'
        command = [CHECK_PYTHON, str(runner), '--cwd', str(work), '--state-dir',
                   str(self.base / 'state'), '--input', '.', '--identity', 'fixture-python',
                   '--reuse', '--', CHECK_PYTHON, '-B', 'check.py']
        values = []
        for _ in range(2):
            result = subprocess.run(command, cwd=self.base, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            values.append(json.loads(result.stdout))
        self.assertEqual(values[0]['execution_id'], values[1]['execution_id'])
        self.assertTrue(values[1]['reused'])


if __name__ == '__main__':
    unittest.main()
