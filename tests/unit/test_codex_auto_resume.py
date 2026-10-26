"""Decisões locais; nenhum teste chama o servidor ou renova cota."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('auto_resume', Path(__file__).resolve().parents[2] / 'scripts/codex_auto_resume.py')
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class AutoResumeTests(unittest.TestCase):
    def test_only_official_usage_error(self):
        self.assertTrue(mod.is_usage_limit({'codexErrorInfo': 'usageLimitExceeded'}))
        self.assertFalse(mod.is_usage_limit({'codexErrorInfo': 'contextWindowExceeded'}))
        self.assertFalse(mod.is_usage_limit({'message': 'token limit'}))

    def test_waits_for_both_windows(self):
        limits = {'rateLimits': {'primary': {'usedPercent': 100, 'resetsAt': 200},
                                'secondary': {'usedPercent': 100, 'resetsAt': 500}}}
        self.assertEqual(mod.quota_wait(limits, 100), 430)

    def test_unknown_quota_never_means_available(self):
        self.assertIsNone(mod.quota_wait({}, 100))
        self.assertIsNone(mod.quota_wait({'rateLimits': {}}, 100))

    def test_spend_block_waits(self):
        self.assertEqual(mod.quota_wait({'rateLimits': {'primary': {'usedPercent': 1},
                        'spendControlReached': True}}, 100), 900)

    def test_codex_bucket_selected(self):
        self.assertEqual(mod.quota_wait({'rateLimitsByLimitId': {'codex': {
            'primary': {'usedPercent': 1}}}, 'rateLimits': {
            'primary': {'usedPercent': 100, 'resetsAt': 500}}}, 100), 0)

    def test_atomic_state_and_ambiguous_result(self):
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / 'config.json'
            mod.atomic_json(config, {'enabled': True})
            supervisor = mod.Supervisor(config)
            self.assertEqual(supervisor._result({'items': []}), 'precisa_usuario')
            self.assertEqual(supervisor._result({'items': [{'type': 'agentMessage',
                'text': '{"status":"concluido","resumo":"feito"}'}]}), 'concluido')
            self.assertEqual(list(Path(folder).glob('*.tmp-*')), [])

    def test_disabled_never_connects(self):
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / 'config.json'
            mod.atomic_json(config, {'enabled': False})
            with patch.object(mod, 'LocalRpc') as rpc:
                self.assertFalse(mod.Supervisor(config).tick())
                rpc.assert_not_called()

    def test_terminal_state_never_connects(self):
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / 'config.json'
            mod.atomic_json(config, {'enabled': True})
            mod.atomic_json(Path(folder) / 'state.json', {'status': 'concluido'})
            with patch.object(mod, 'LocalRpc') as rpc:
                self.assertFalse(mod.Supervisor(config).tick())
                rpc.assert_not_called()

    def test_future_quota_check_never_connects(self):
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / 'config.json'
            mod.atomic_json(config, {'enabled': True})
            mod.atomic_json(Path(folder) / 'state.json', {'next_check_at': 1000})
            with patch.object(mod.time, 'time', return_value=100), patch.object(mod, 'LocalRpc') as rpc:
                self.assertTrue(mod.Supervisor(config).tick())
                rpc.assert_not_called()

    def test_active_and_user_interruption_never_start_turn(self):
        for runtime, status, expected in [('active', 'inProgress', True),
                                          ('idle', 'interrupted', False),
                                          ('idle', 'failed', False)]:
            with self.subTest(status=status), tempfile.TemporaryDirectory() as folder:
                config = Path(folder) / 'config.json'
                mod.atomic_json(config, {'enabled': True, 'codex_path': 'unused',
                    'thread_id': 'original', 'workspace': folder})
                mod.atomic_json(Path(folder) / 'state.json', {'owned_turn': 'original-turn'})
                with patch.object(mod, 'LocalRpc') as factory:
                    rpc = factory.return_value
                    rpc.call.side_effect = [
                        {'thread': {'cwd': folder, 'status': {'type': runtime}}},
                        {'data': [{'id': 'original-turn', 'status': status,
                                   'error': {'codexErrorInfo': 'other'}}]}]
                    self.assertEqual(mod.Supervisor(config).tick(), expected)
                    self.assertEqual([c.args[0] for c in rpc.call.call_args_list],
                                     ['thread/read', 'thread/turns/list'])


if __name__ == '__main__':
    unittest.main()
