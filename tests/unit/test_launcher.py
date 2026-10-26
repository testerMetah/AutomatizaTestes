from unittest.mock import MagicMock, patch

import pytest
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.timings import TimeoutError as UiTimeoutError

from automatiza.config import Settings
from automatiza.desktop import DesktopApp


@pytest.fixture(autouse=True)
def desktop_simulado_disponivel():
    # Estes testes simulam o aplicativo. A recusa de desktop real é testada em test_ambiente.
    with patch('automatiza.desktop.require_interactive_desktop', return_value={'disponivel': True}):
        yield


@pytest.mark.parametrize("error", [ElementNotFoundError(), UiTimeoutError()])
def test_modulo_ausente_orienta_abrir_acesso(error):
    with patch("automatiza.desktop.Application") as application:
        application.return_value.connect.side_effect = error
        desktop = DesktopApp(Settings(app_title_re="^Módulo de Acesso"))
        with pytest.raises(RuntimeError, match="abra o Acesso"):
            desktop.connect()
        application.return_value.start.assert_not_called()


def test_modulo_abre_pelo_painel_com_pasta_correta(tmp_path):
    executable = tmp_path / "Acessus.Modulo.exe"
    executable.touch()
    settings = Settings(app_title_re="^Módulo de Acesso", launcher_path=str(executable),
                        launcher_title_re="^Painel", launcher_menu_path="Modulos->Acesso",
                        app_work_dir=str(tmp_path))
    application = MagicMock()
    application.connect.side_effect = [ElementNotFoundError(), None]
    launcher = MagicMock()
    launcher.connect.side_effect = ElementNotFoundError()
    with patch("automatiza.desktop.Application", side_effect=[application, launcher]):
        desktop = DesktopApp(settings).start()
    launcher.start.assert_called_once_with(f'"{executable}"', work_dir=str(tmp_path))
    launcher.window.return_value.menu_select.assert_called_once_with("Modulos->Acesso")
    assert application.connect.call_args_list[-1].kwargs == {
        "title_re": "^Módulo de Acesso", "timeout": 20
    }
    assert desktop.window is application.window.return_value


def test_abertura_reutiliza_modulo_sem_abrir_segunda_instancia():
    with patch("automatiza.desktop.Application") as application:
        desktop = DesktopApp(Settings(app_title_re="^Módulo de Acesso")).start()
    application.assert_called_once()
    application.return_value.start.assert_not_called()
    assert desktop.window is application.return_value.window.return_value
