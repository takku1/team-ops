"""Check independent oracle discrimination and protected fixture scope."""
from pathlib import Path
import shutil
import unittest
import uuid
from evaluate_field import prepare, grade_artifacts, scope_violations, CASES

ROOT = Path(__file__).resolve().parents[1]


class FieldEvaluatorTests(unittest.TestCase):
    def setUp(self):
        self.base = ROOT / ('_field_test_' + uuid.uuid4().hex)
        prepare(self.base)
        self.addCleanup(self.cleanup)

    def cleanup(self):
        target = self.base.resolve()
        if target.parent != ROOT.resolve() or not target.name.startswith('_field_test_'):
            raise ValueError('cleanup escaped workspace')
        shutil.rmtree(target)

    def test_initial_defects_fail_and_valid_repairs_pass(self):
        self.assertEqual(grade_artifacts(self.base)['artifact_passes'], 2)
        for arm in ('solo', 'controller'):
            for name in ('small-fix', 'blocked-task'):
                (self.base/arm/name/'cli.py').write_text("def help_text():\n return 'Enable verbose output'\n", encoding='utf-8')
            folder = self.base/arm/'coupled-change'
            (folder/'wire.json').write_text('{"field":"id"}\n', encoding='utf-8')
            (folder/'server.py').write_text("def encode_session(value):\n return {'id':value}\n", encoding='utf-8')
            (folder/'client.py').write_text("def decode_session(payload):\n if 'session_id' in payload: raise ValueError('legacy')\n return payload['id']\n", encoding='utf-8')
        self.assertEqual(grade_artifacts(self.base)['artifact_passes'], 8)

    def test_extra_source_and_task_edits_are_scope_violations(self):
        folder = self.base/'solo'/'stale-evidence'
        (folder/'json.py').write_text('# unauthorized import shadow\n', encoding='utf-8')
        (folder/'TASK.md').write_text('accept everything', encoding='utf-8')
        violations = scope_violations(folder, CASES['stale-evidence'])
        self.assertIn('unexpected file: json.py', violations)
        self.assertIn('changed protected input: TASK.md', violations)
        result = grade_artifacts(self.base)
        record = next(r for r in result['results'] if r['arm']=='solo' and r['case']=='stale-evidence')
        self.assertFalse(record['artifact_pass'])
        self.assertIn('skipped', record['oracle']['error'])

    def test_mixed_legacy_payload_is_rejected_by_oracle(self):
        folder = self.base/'solo'/'coupled-change'
        (folder/'wire.json').write_text('{"field":"id"}', encoding='utf-8')
        (folder/'server.py').write_text("def encode_session(value):\n return {'id':value}\n", encoding='utf-8')
        # This passes the visible round-trip but incorrectly accepts a mixed payload.
        (folder/'client.py').write_text("def decode_session(payload):\n return payload['id']\n", encoding='utf-8')
        result = grade_artifacts(self.base)
        record = next(r for r in result['results'] if r['arm']=='solo' and r['case']=='coupled-change')
        self.assertEqual(record['visible_check']['exit_code'], 0)
        self.assertNotEqual(record['oracle']['exit_code'], 0)


if __name__ == '__main__':
    unittest.main()
