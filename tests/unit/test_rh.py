from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from automatiza.config import Settings
from automatiza.rh import RhApp, _fill_without_logging, login_controls


def test_logger_fechado_do_pythonw_nao_interrompe_acoes():
    import io
    import logging
    from automatiza.rh import repair_closed_action_logs
    from pywinauto.actionlogger import ActionLogger
    logger = logging.getLogger('pywinauto')
    original = logger.handlers[:]
    stream = io.StringIO()
    stream.close()
    logger.handlers = [logging.StreamHandler(stream)]
    try:
        repair_closed_action_logs()
        ActionLogger().log('acao sem credenciais')
        assert all(isinstance(h, logging.NullHandler) for h in logger.handlers)
    finally:
        logger.handlers = original


def test_logger_valido_e_preservado():
    import io
    import logging
    from automatiza.rh import repair_closed_action_logs
    logger = logging.getLogger('pywinauto')
    original = logger.handlers[:]
    handler = logging.StreamHandler(io.StringIO())
    logger.handlers = [handler]
    try:
        repair_closed_action_logs()
        assert logger.handlers == [handler]
    finally:
        logger.handlers = original


def field(*, password=False, enabled=True, readonly=False):
    control = MagicMock()
    control.is_visible.return_value = True
    control.is_enabled.return_value = enabled
    control.has_style.side_effect = lambda style: {0x0020: password, 0x0800: readonly}[style]
    return control


def dialog_with_fields(fields):
    dialog = MagicMock()
    button = MagicMock()
    button.window_text.return_value = "&OK"
    dialog.descendants.side_effect = lambda **kw: fields if kw["class_name"] == "TEdit" else [button]
    return dialog, button


def test_login_ignora_campos_ad_desabilitados_e_exige_senha_mascarada():
    user, password = field(), field(password=True)
    dialog, button = dialog_with_fields([field(enabled=False), field(readonly=True), user, password])
    assert login_controls(dialog) == (user, password, button)


def test_login_ambiguo_nao_preenche_nem_confirma():
    fields = [field(), field(), field(password=True)]
    dialog, button = dialog_with_fields(fields)
    app = RhApp(Settings(rh_user="usuario", rh_password="segredo"), desktop=MagicMock())
    with pytest.raises(RuntimeError, match="campo de login"):
        app._authenticate(dialog)
    for control in fields:
        control.set_edit_text.assert_not_called()
    button.click.assert_not_called()


def test_preenchimento_nao_envia_credencial_ao_logger_e_restaura_logger():
    control = MagicMock()
    original = control.actions
    control.set_edit_text.side_effect = lambda text: control.actions.log(text)
    _fill_without_logging(control, "segredo-teste")
    original.log.assert_not_called()
    assert control.actions is original


def test_frequencia_aberta_e_minimizada_e_reutilizada():
    app = RhApp(Settings(), desktop=MagicMock())
    frequency = MagicMock()
    frequency.is_minimized.return_value = True
    app._frequency = MagicMock(return_value=[frequency])
    with patch("automatiza.rh.subprocess.Popen") as launch:
        assert app.start().window is frequency
    launch.assert_not_called()
    frequency.restore.assert_called_once()


def test_cenario_sem_autenticacao_nao_preenche_login_pendente():
    app = RhApp(Settings(rh_user='usuario', rh_password='segredo'), desktop=MagicMock())
    app._frequency = MagicMock(return_value=[])
    app._logins = MagicMock(return_value=[MagicMock()])
    app._panels = MagicMock(return_value=[])
    app._notices = MagicMock(return_value=[])
    app._authenticate = MagicMock()
    with pytest.raises(RuntimeError, match='Entre manualmente'):
        app.start(authenticate=False)
    app._authenticate.assert_not_called()


def test_frequencia_exclui_tapplication_com_titulo_igual():
    app = RhApp(Settings(), desktop=MagicMock())
    app._windows = MagicMock(return_value=[])
    assert app._frequency() == []
    assert app._windows.call_args.kwargs['class_name'] == 'TFrm_RHPA0010'


def test_painel_transitorio_na_abertura_nao_pula_login():
    app = RhApp(Settings(), desktop=MagicMock(), clock=MagicMock(return_value=0))
    panel, login = MagicMock(), MagicMock()
    app._logins = MagicMock(side_effect=[[], [login]])
    app._notices = MagicMock(return_value=[])
    app._panels = MagicMock(return_value=[panel])
    assert app._startup_windows() == []
    assert app._startup_windows() == [login]


def test_login_abre_frequencia_somente_depois_de_confirmar_sucesso():
    user, password = field(), field(password=True)
    dialog, button = dialog_with_fields([user, password])
    panel, frequency = MagicMock(), MagicMock()
    app = RhApp(Settings(rh_user="usuario", rh_password="segredo"), desktop=MagicMock())
    app._frequency = MagicMock(return_value=[frequency])
    app._frequency.side_effect = lambda: [] if not button.click.called else [frequency]
    app._logins = MagicMock(side_effect=[[dialog], []])
    app._panels = MagicMock(side_effect=[[], [panel]])
    with patch("automatiza.rh.subprocess.Popen") as launch:
        assert app.start().window is frequency
    user.set_edit_text.assert_called_once_with("usuario")
    password.set_edit_text.assert_called_once_with("segredo")
    button.click.assert_called_once()
    panel.menu_select.assert_called_once_with("Módulos->Frequência")
    launch.assert_not_called()


def test_falha_no_preenchimento_nao_repete_nem_expoe_senha():
    user, password = field(), field(password=True)
    dialog, button = dialog_with_fields([user, password])
    password.set_edit_text.side_effect = RuntimeError("conteudo segredo")
    app = RhApp(Settings(rh_user="usuario", rh_password="segredo"), desktop=MagicMock())
    with pytest.raises(RuntimeError) as failure:
        app._authenticate(dialog)
    assert "segredo" not in str(failure.value)
    assert password.set_edit_text.call_count == 1
    button.click.assert_not_called()


def test_filtro_de_processo_nao_aceita_rhid_de_outra_pasta(tmp_path):
    desktop = MagicMock()
    good, bad = MagicMock(), MagicMock()
    good.process_id.return_value = 1
    bad.process_id.return_value = 2
    desktop.windows.return_value = [good, bad]
    app = RhApp(Settings(rh_work_dir=str(tmp_path)), desktop=desktop)
    with patch("automatiza.rh.process_module", side_effect=[str(tmp_path / "RHID.exe"), str(tmp_path / "outra" / "RHID.exe")]):
        assert app._windows("RHID.exe", class_name="TFrm_Login") == [good]


def test_rh_senha_nao_aparece_em_settings():
    assert "segredo" not in repr(Settings(rh_password="segredo"))


def test_aviso_autorizado_e_confirmado_uma_vez_e_registrado():
    app = RhApp(Settings(rh_continue_invalid_config="yes"), desktop=MagicMock())
    notice, button = dialog_with_fields([])
    button.window_text.return_value = "&Continuar"
    app._notices = MagicMock(return_value=[notice])
    assert app._panel_after_notice() == []
    assert app._panel_after_notice() == []
    button.click.assert_called_once()
    assert len(app.warnings) == 1


def test_aviso_sem_autorizacao_nao_e_confirmado():
    app = RhApp(Settings(), desktop=MagicMock())
    notice, button = dialog_with_fields([])
    app._notices = MagicMock(return_value=[notice])
    with pytest.raises(RuntimeError, match="Configurações Inválidas"):
        app._panel_after_notice()
    button.click.assert_not_called()


def test_rota_usa_menu_e_classe_sem_indices_de_sessao():
    desktop = MagicMock()
    app = RhApp(Settings(), desktop=desktop)
    app.window = MagicMock()
    screen = app.open_screen("ocorrencias")
    app.window.menu_select.assert_called_once_with("Programações->Registro de Ocorrências...")
    desktop.window.return_value.child_window.assert_called_once_with(class_name="TFrm_RHPA5020")
    screen.wait.assert_called_once_with("visible enabled", timeout=20)


@pytest.mark.parametrize('name,keys', [('ocorrencias', '%po'), ('ferias', '%pf'), ('reservas', '%pu')])
def test_menu_ilegivel_usa_mnemonico_e_exige_tela_resultante(name, keys):
    app = RhApp(Settings(), desktop=MagicMock())
    app.window = MagicMock()
    failure = OSError('leitura parcial')
    failure.winerror = 299
    app.window.menu_select.side_effect = failure
    screen = app.open_screen(name)
    app.window.type_keys.assert_called_once_with(keys)
    screen.wait.assert_called_once_with('visible enabled', timeout=20)


def test_frequencia_com_erro_nao_abre_ou_confirma_dialogos():
    app = RhApp(Settings(), desktop=MagicMock())
    dialog = MagicMock()
    app._windows = MagicMock(return_value=[dialog])
    with patch('automatiza.rh.subprocess.Popen') as launch:
        with pytest.raises(RuntimeError, match='bloqueado por uma mensagem'):
            app.start(authenticate=False)
    launch.assert_not_called()
    dialog.click.assert_not_called()


def test_frequencia_transitoria_nao_e_considerada_pronta():
    clock = MagicMock(side_effect=[0, 0.5, 1.1])
    app = RhApp(Settings(), desktop=MagicMock(), clock=clock)
    app._check_frequency_messages = MagicMock(return_value=False)
    window = MagicMock()
    app._frequency = MagicMock(return_value=[window])
    assert app._frequency_ready() == []
    assert app._frequency_ready() == []
    assert app._frequency_ready() == [window]


def test_aviso_informativo_de_entrada_com_ok_pode_continuar():
    app = RhApp(Settings(), desktop=MagicMock())
    dialog, button = MagicMock(), MagicMock()
    dialog.window_text.return_value = 'Information'
    dialog.descendants.return_value = [button]
    button.class_name.return_value = 'TButton'
    button.window_text.return_value = '&OK'
    app._windows = MagicMock(return_value=[dialog])
    assert app._check_frequency_messages() is True
    button.click_input.assert_called_once()
    assert app.warnings


def test_confirmacao_com_sim_nao_e_tratada_como_aviso_de_entrada():
    app = RhApp(Settings(), desktop=MagicMock())
    dialog, button = MagicMock(), MagicMock()
    dialog.window_text.return_value = 'Information'
    dialog.descendants.return_value = [button]
    button.class_name.return_value = 'TButton'
    button.window_text.return_value = 'Sim'
    app._windows = MagicMock(return_value=[dialog])
    with pytest.raises(RuntimeError, match='bloqueado'):
        app._check_frequency_messages()
    button.click_input.assert_not_called()
