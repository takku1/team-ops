"""Exercise actual check execution, reuse, concurrency, and invalidation."""
import json
import argparse
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import shutil
import time
import uuid
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'plugins/team-ops/skills/team-lead/scripts/check_runner.py'
CHECK_PYTHON = str(Path(sys.base_prefix) / 'python.exe') if os.name == 'nt' else sys.executable


class CheckRunnerTests(unittest.TestCase):
    def setUp(self):
        # tempfile's private Windows ACLs are incompatible with some managed hosts.
        self.base = ROOT / ('_runner_test_' + uuid.uuid4().hex)
        self.base.mkdir()
        self.addCleanup(self.cleanup_workspace)
        self.work = self.base / 'work'
        self.work.mkdir()
        self.state = self.base / 'state'
        self.source = self.work / 'input.txt'
        self.source.write_text('first', encoding='utf-8')
        self.script = self.work / 'check.py'
        self.script.write_text("print('observed check')\n", encoding='utf-8')

    def cleanup_workspace(self):
        target = self.base.resolve()
        if target.parent != ROOT.resolve() or not target.name.startswith('_runner_test_'):
            raise ValueError('test cleanup escaped its workspace')
        shutil.rmtree(target)

    def command(self, *flags, code=None):
        return [sys.executable, str(RUNNER), '--cwd', str(self.work),
                '--state-dir', str(self.state), '--input', 'input.txt',
                '--input', 'check.py', '--identity', 'test-python-v1', *flags,
                '--', CHECK_PYTHON, *(['-c', code] if code else ['check.py'])]

    def invoke(self, *flags, code=None, env=None):
        result = subprocess.run(self.command(*flags, code=code), capture_output=True,
                                text=True, env=env)
        return result, json.loads(result.stdout or result.stderr)

    def test_reuse_is_opt_in_and_logs_are_retained(self):
        first, a = self.invoke('--reuse')
        second, b = self.invoke('--reuse')
        fresh, c = self.invoke('--fresh')
        self.assertEqual([first.returncode, second.returncode, fresh.returncode], [0, 0, 0])
        self.assertTrue(b['reused'])
        self.assertEqual(a['execution_id'], b['execution_id'])
        self.assertNotEqual(a['execution_id'], c['execution_id'])
        self.assertIn('observed check', Path(a['stdout_log']).read_text())

    def test_secret_shaped_output_is_redacted(self):
        key = 'AKIA' + 'ABCDEFGHIJKLMNOP'
        code = (f"import sys; print('aws {key}'); print('api_key = hunter2-value');"
                "print('-----BEGIN RSA PRIVATE KEY-----\\nabc\\n-----END RSA PRIVATE KEY-----');"
                "print('Bearer ' + 'x' * 24, file=sys.stderr); print('plain output')")
        result, data = self.invoke(code=code)
        self.assertEqual(result.returncode, 0, result.stderr)
        logs = Path(data['stdout_log']).read_text() + Path(data['stderr_log']).read_text()
        for secret in (key, 'hunter2-value', 'abc\n', 'x' * 24):
            self.assertNotIn(secret, logs)
        self.assertIn('api_key = [REDACTED]', logs)
        self.assertIn('plain output', logs)
        self.assertEqual(data['redactions'], 4)

    def status(self):
        out = subprocess.run([sys.executable, str(RUNNER), '--state-dir', str(self.state), '--status'],
                             capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        return json.loads(out.stdout)

    def test_status_shows_running_owner_then_finished(self):
        proc = subprocess.Popen(self.command('--owner', 'task-7', code='import time; time.sleep(4)'),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.addCleanup(proc.kill)
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline and not (self.state / 'jobs').exists():
            time.sleep(0.05)
        running = {}
        while time.monotonic() < deadline:
            running = self.status()
            if running['busy']:
                break
            time.sleep(0.1)
        self.assertTrue(running['busy'])
        self.assertEqual(running['running'][0]['owner'], 'task-7')
        proc.communicate(timeout=30)
        done = self.status()
        self.assertFalse(done['busy'])
        self.assertEqual((done['recent'][0]['state'], done['recent'][0]['exit_code']), ('finished', 0))

    def test_dead_job_is_reported_orphaned_not_busy(self):
        dead = subprocess.Popen([sys.executable, '-c', 'pass'])
        dead.wait()
        (self.state / 'jobs').mkdir(parents=True)
        (self.state / 'jobs' / 'x.json').write_text(json.dumps(
            {'job_id': 'x', 'pid': dead.pid, 'owner': 'gone', 'state': 'running', 'updated_unix': 0}))
        status = self.status()
        self.assertFalse(status['busy'])
        self.assertEqual([j['owner'] for j in status['orphaned']], ['gone'])

    def test_changed_inputs_invalidate_green(self):
        _, a = self.invoke('--reuse')
        self.source.write_text('second', encoding='utf-8')
        result, b = self.invoke('--reuse')
        self.assertEqual(result.returncode, 0)
        self.assertNotEqual(a['input_id'], b['input_id'])
        self.assertFalse(b['reused'])
        self.assertIn('inputs_changed', b['cache']['reasons'])

    def test_environment_change_invalidates_without_exposing_values(self):
        _, a = self.invoke('--reuse')
        env = dict(os.environ, TEAM_OPS_TEST_VALUE='private-value-357')
        result, b = self.invoke('--reuse', env=env)
        self.assertNotEqual(a['input_id'], b['input_id'])
        self.assertIn('environment_changed', b['cache']['reasons'])
        self.assertNotIn('private-value-357', result.stdout)
        self.assertNotIn('private-value-357', ''.join(p.read_text() for p in self.state.glob('*.json')))

    def test_failure_is_not_reused(self):
        code = "import sys; print('failed'); sys.exit(7)"
        first, a = self.invoke('--reuse', code=code)
        second, b = self.invoke('--reuse', code=code)
        self.assertNotEqual(first.returncode, 0)
        self.assertNotEqual(second.returncode, 0)
        self.assertEqual(a['exit_code'], 7)
        self.assertNotEqual(a['execution_id'], b['execution_id'])
        self.assertIn('prior_execution_failed', b['cache']['reasons'])

    def test_fresh_failure_invalidates_previous_green(self):
        # Deliberately external-state dependent to test invalidation; never a valid reuse use case.
        flag = self.base / 'fail'
        code = f"import pathlib,sys; sys.exit(9 if pathlib.Path({str(flag)!r}).exists() else 0)"
        _, a = self.invoke('--reuse', code=code)
        flag.touch()
        failed, b = self.invoke('--fresh', code=code)
        repeated, c = self.invoke('--reuse', code=code)
        self.assertEqual(a['exit_code'], 0)
        self.assertEqual(b['exit_code'], 9)
        self.assertNotEqual(repeated.returncode, 0)
        self.assertNotEqual(b['execution_id'], c['execution_id'])

    def test_mutation_during_execution_makes_success_stale(self):
        code = "from pathlib import Path; Path('input.txt').write_text('mutated')"
        result, value = self.invoke('--reuse', code=code)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(value['exit_code'], 0)
        self.assertFalse(value['stable'])

    def test_concurrent_reusable_requests_execute_once(self):
        counter = self.base / 'executions.txt'
        code = (f"import time; from pathlib import Path; p=Path({str(counter)!r}); "
                "p.write_text(p.read_text()+'x' if p.exists() else 'x'); time.sleep(0.4)")
        processes = [subprocess.Popen(self.command('--reuse', code=code),
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                     for _ in range(2)]
        output = [p.communicate(timeout=15) for p in processes]
        self.assertEqual([p.returncode for p in processes], [0, 0])
        values = [json.loads(out) for out, _ in output]
        self.assertEqual(counter.read_text(), 'x')
        self.assertEqual(values[0]['execution_id'], values[1]['execution_id'])
        self.assertEqual(sum(v['reused'] for v in values), 1)

    def test_lane_wait_is_bounded(self):
        marker = self.base / 'started'
        code = f"import time; from pathlib import Path; Path({str(marker)!r}).touch(); time.sleep(1)"
        process = subprocess.Popen(self.command(code=code), stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        import time
        deadline = time.monotonic() + 10
        while not marker.exists() and time.monotonic() < deadline:
            time.sleep(0.02)
        try:
            result, value = self.invoke('--lock-timeout', '0')
            self.assertEqual(result.returncode, 2)
            self.assertIn('busy', value['error'])
        finally:
            process.communicate(timeout=10)

    def test_missing_input_and_nested_state_rejected(self):
        self.source.unlink()
        result, _ = self.invoke()
        self.assertEqual(result.returncode, 2)
        self.source.touch()
        self.state = self.work / 'state'
        result, value = self.invoke()
        self.assertEqual(result.returncode, 2)
        self.assertIn('outside', value['error'])

    def test_directory_identity_includes_untracked_files(self):
        self.script.write_text("print('ok')", encoding='utf-8')
        command = self.command('--reuse')
        index = command.index('input.txt')
        command[index] = '.'
        first = subprocess.run(command, capture_output=True, text=True)
        (self.work / 'new-untracked').write_text('new', encoding='utf-8')
        second = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual([first.returncode, second.returncode], [0, 0])
        self.assertNotEqual(json.loads(first.stdout)['input_id'], json.loads(second.stdout)['input_id'])

    def test_corrupt_ledger_and_missing_log_trigger_execution(self):
        _, a = self.invoke('--reuse')
        ledger = self.state / (a['input_id'] + '.json')
        ledger.write_text('broken', encoding='utf-8')
        _, b = self.invoke('--reuse')
        Path(b['stdout_log']).unlink()
        _, c = self.invoke('--reuse')
        self.assertEqual(len({a['execution_id'], b['execution_id'], c['execution_id']}), 3)

    def test_launch_failure_invalidates_prior_green(self):
        _, previous = self.invoke('--reuse')
        spec = importlib.util.spec_from_file_location('check_runner_under_test', RUNNER)
        runner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runner)
        args = argparse.Namespace(cwd=str(self.work), state_dir=str(self.state),
                                  input=['input.txt', 'check.py'], identity='test-python-v1',
                                  command=[CHECK_PYTHON, 'check.py'], reuse=False, lock_timeout=1)
        with patch.object(runner.subprocess, 'run', side_effect=OSError('launch failed')):
            with self.assertRaisesRegex(OSError, 'launch failed'):
                runner.run(args)
        self.assertFalse((self.state / (previous['input_id'] + '.json')).exists())
        _, explanation = self.invoke('--explain')
        self.assertIn('prior_execution_incomplete', explanation['cache']['reasons'])
        self.assertNotIn('prior_execution_failed', explanation['cache']['reasons'])

    def test_relative_path_entry_resolves_from_workspace(self):
        command = self.command()
        tools = self.work / 'local-tools'
        tools.mkdir()
        executable = tools / ('probe.exe' if os.name == 'nt' else 'probe')
        # Pin the OS binary: PATH may list a dependent copy first (e.g. Git's MSYS whoami needs msys-2.0.dll).
        source = (Path(os.environ['SystemRoot'], 'System32', 'whoami.exe') if os.name == 'nt'
                  else shutil.which('echo'))
        shutil.copy2(source, executable)
        command = command[:command.index('--') + 1] + [executable.name]
        env = dict(os.environ, PATH='local-tools')
        result = subprocess.run(command, capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(Path(json.loads(result.stdout)['command'][0]).resolve(),
                         executable.resolve())

    def test_nonfinite_lock_timeout_is_rejected(self):
        for value in ('nan', 'inf', '-inf'):
            with self.subTest(value=value):
                result = subprocess.run(self.command('--lock-timeout=' + value),
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 2)
                self.assertIn('finite', result.stderr)

    def test_explain_does_not_execute_or_replace_results(self):
        _, first = self.invoke('--reuse')
        count = len(list(self.state.glob('*.result.json')))
        result, hit = self.invoke('--explain')
        self.assertEqual(result.returncode, 0)
        self.assertTrue(hit['inspection_only'])
        self.assertTrue(hit['would_reuse'])
        self.source.write_text('changed', encoding='utf-8')
        _, miss = self.invoke('--explain')
        self.assertFalse(miss['would_reuse'])
        self.assertIn('inputs_changed', miss['cache']['reasons'])
        self.assertEqual(len(list(self.state.glob('*.result.json'))), count)
        self.assertTrue(Path(first['stdout_log']).exists())

    def test_toolchain_and_command_changes_are_distinguished(self):
        self.invoke('--reuse')
        _, changed = self.invoke('--explain', '--identity', 'new-toolchain')
        self.assertIn('toolchain_changed', changed['cache']['reasons'])
        self.assertNotIn('inputs_changed', changed['cache']['reasons'])
        _, changed = self.invoke('--explain', code="print('different command')")
        self.assertIn('command_changed', changed['cache']['reasons'])

    def test_fresh_execution_explains_bypass(self):
        self.invoke('--reuse')
        _, fresh = self.invoke('--fresh')
        self.assertEqual(fresh['cache']['reasons'], ['fresh_execution_requested'])
        self.assertEqual(fresh['cache']['reuse_eligibility']['outcome'], 'hit')

    def test_missing_log_explains_reexecution(self):
        _, first = self.invoke('--reuse')
        Path(first['stdout_log']).unlink()
        _, value = self.invoke('--reuse')
        self.assertIn('prior_logs_missing', value['cache']['reasons'])


if __name__ == '__main__':
    unittest.main()
