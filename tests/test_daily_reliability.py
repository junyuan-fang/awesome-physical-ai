"""Offline regression checks for network failures and post-apply recovery."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import sources
import recheck_open


class DiscoveryTests(unittest.TestCase):
    def test_unreachable_arxiv_is_not_an_empty_success(self):
        with patch.object(sources, 'http_get', return_value=None):
            with self.assertRaisesRegex(RuntimeError, 'coverage was not completed'):
                sources.arxiv_search('cat:cs.RO')

    def test_failure_after_first_page_does_not_accept_partial_coverage(self):
        page = '<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/abs/2610.00001</id></entry></feed>'
        with patch.object(sources, 'http_get', side_effect=[page, None]), patch.object(sources.time, 'sleep'):
            with self.assertRaises(RuntimeError):
                sources.arxiv_search('cat:cs.RO', max_results=2, page=1)

    def test_successful_empty_feed_is_valid(self):
        with patch.object(sources, 'http_get', return_value='<feed xmlns="http://www.w3.org/2005/Atom"/>'):
            self.assertEqual(sources.arxiv_search('cat:cs.RO'), [])

    def test_repo_timeout_preserves_prior_open_status(self):
        paper = {'open': {'repo': 'https://github.com/example/project', 'code': 'substantive'}}
        with patch.object(sources, 'probe_repo', side_effect=subprocess.TimeoutExpired('git show', 60)):
            result, probe = recheck_open.recheck(paper)
        self.assertEqual(probe['code'], 'unknown')
        self.assertEqual(result['open']['code'], 'substantive')


@unittest.skipUnless(shutil.which('bash'), 'requires bash')
class RecoveryTests(unittest.TestCase):
    def run_pipeline(self, state):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'scripts').mkdir()
            shutil.copy(Path(__file__).resolve().parents[1] / 'scripts/run_daily.sh', root / 'scripts/run_daily.sh')
            fake = root / 'fake-python'
            fake.write_text('#!/bin/sh\nprintf "%s\\n" "$*" >> "$CALL_LOG"\n'
                            'if [ "$1" = scripts/daily_state.py ]; then exit "$APPLIED_STATE"; fi\n')
            fake.chmod(0o755)
            log = root / 'calls'
            result = subprocess.run(['bash', 'scripts/run_daily.sh', 'apply', '2026-11-01'], cwd=root,
                                    env={**os.environ, 'PYTHON': str(fake), 'CALL_LOG': str(log), 'APPLIED_STATE': str(state)},
                                    capture_output=True, text=True)
            return result.returncode, log.read_text()

    def test_resume_renders_without_reapplying_or_network_recheck(self):
        code, calls = self.run_pipeline(10)
        self.assertEqual(code, 0)
        self.assertNotIn('apply_reviews.py', calls)
        self.assertNotIn('recheck_open.py', calls)
        self.assertIn('generate_readme.py', calls)
        self.assertIn('validate.py', calls)

    def test_fresh_run_applies_once(self):
        code, calls = self.run_pipeline(0)
        self.assertEqual(code, 0)
        self.assertEqual(calls.count('apply_reviews.py'), 1)

    def test_state_error_stops_before_mutation(self):
        code, calls = self.run_pipeline(1)
        self.assertEqual(code, 1)
        self.assertNotIn('apply_reviews.py', calls)
        self.assertNotIn('generate_readme.py', calls)


if __name__ == '__main__':
    unittest.main()
