from unittest.mock import MagicMock, patch
import pytest
from automatiza.ambiente import require_interactive_desktop
from automatiza.config import Settings
from automatiza.rh import RhApp


def test_desktop_indisponivel_impede_tela_antes_de_qualquer_lancamento():
    with patch('automatiza.rh.Desktop'), patch('automatiza.rh.require_interactive_desktop', side_effect=RuntimeError('desktop isolado')):
        app = RhApp(Settings())
        with patch.object(app, '_frequency') as frequency, patch('automatiza.rh.subprocess.Popen') as launch:
            with pytest.raises(RuntimeError, match='desktop isolado'):
                app.start()
            frequency.assert_not_called()
            launch.assert_not_called()


def test_checagem_nao_afirma_disponibilidade_em_desktop_diferente():
    with patch('automatiza.ambiente.desktop_context', return_value={'disponivel': False}):
        with pytest.raises(RuntimeError, match='Nenhum aplicativo'):
            require_interactive_desktop()


def test_desktop_confirmado_e_aceito_sem_trocar_contexto():
    context = {'disponivel': True, 'desktop_processo': 'Default', 'desktop_entrada': 'Default'}
    with patch('automatiza.ambiente.desktop_context', return_value=context):
        assert require_interactive_desktop() == context


def test_acessus_nao_tenta_conectar_ou_iniciar_em_desktop_indisponivel():
    from automatiza.desktop import DesktopApp
    with patch('automatiza.desktop.Application') as application, patch('automatiza.desktop.require_interactive_desktop', side_effect=RuntimeError('desktop isolado')):
        app = DesktopApp(Settings(app_title_re='Teste'))
        for action in (app.connect, app.start):
            with pytest.raises(RuntimeError, match='desktop isolado'):
                action()
        application.return_value.connect.assert_not_called()
        application.return_value.start.assert_not_called()
