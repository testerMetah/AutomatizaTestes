"""Abertura e autenticação local do RH Metadados.

Classes e tipos extraídos dos recursos instalados RHLogin.bpl e RHID.exe.
O preenchimento só ocorre na classe TFrm_Login do RHID.exe da pasta configurada.
O fluxo completo ainda precisa de validação na instalação real.
"""

import os
import logging
import subprocess
import time
from pathlib import Path

from pywinauto import Desktop
from pywinauto.application import process_module
from automatiza.ambiente import require_interactive_desktop

SCREENS = {
    "ocorrencias": ("Programações->Registro de Ocorrências...", "TFrm_RHPA5020"),
    "ferias": ("Programações->Férias Cedidas...", "TFrm_RHPA5130"),
    "reservas": ("Programações->Reserva ou Consumo...", "TFrm_RHPA5210"),
    "pessoas": ("Cadastramento->Pessoas e Contratos...", "TFrm_RHPA4300"),
}

class _NoCredentialLog:
    def log(self, *args, **kwargs):
        pass


def _fill_without_logging(control, value):
    # EditWrapper.set_edit_text registra o texto quando o log da biblioteca está ativo.
    # Trocar somente o logger deste controle evita registrar usuário ou senha.
    previous = control.actions
    control.actions = _NoCredentialLog()
    try:
        control.set_edit_text(value)
    finally:
        control.actions = previous


def _unique(items, label):
    if len(items) != 1:
        raise RuntimeError(f"Esperado um único {label}; encontrados {len(items)}. Nenhuma tentativa adicional de login foi feita.")
    return items[0]


def repair_closed_action_logs():
    """O pythonw pode herdar handlers ligados à captura já fechada do pytest."""
    logger = logging.getLogger('pywinauto')
    for handler in list(logger.handlers):
        if isinstance(handler, logging.StreamHandler):
            stream = handler.stream
            if stream is None or getattr(stream, 'closed', False):
                logger.removeHandler(handler)
    if not logger.handlers:
        logger.addHandler(logging.NullHandler())


def login_controls(dialog):
    """Usa classes e estilo de senha; nunca usa coordenadas ou índices de sessão."""
    fields = [field for field in dialog.descendants(class_name="TEdit")
              if field.is_visible() and field.is_enabled() and not field.has_style(0x0800)]  # ES_READONLY
    password = _unique([field for field in fields if field.has_style(0x0020)], "campo de senha")
    user = _unique([field for field in fields if not field.has_style(0x0020)], "campo de login")
    submit = _unique([button for button in dialog.descendants(class_name="TBitBtn")
                      if button.is_visible() and button.is_enabled()
                      and button.window_text().replace("&", "").strip().casefold() == "ok"], "botão OK")
    return user, password, submit


class RhApp:
    def __init__(self, settings, *, desktop=None, clock=time.monotonic, sleep=time.sleep):
        repair_closed_action_logs()
        self.settings = settings
        self._check_desktop = desktop is None
        self.desktop = desktop if desktop is not None else Desktop(backend="win32")
        self.clock, self.sleep = clock, sleep
        self.window = None
        self.warnings = []
        self._acknowledged = set()
        self._path_cache = {}

    def _windows(self, executable, **criteria):
        expected = os.path.normcase(str(Path(self.settings.rh_work_dir) / executable))
        result = []
        for window in self.desktop.windows(visible_only=False, **criteria):
            pid = window.process_id()
            try:
                if pid not in self._path_cache:
                    self._path_cache[pid] = os.path.normcase(process_module(pid))
            except (OSError, RuntimeError):
                continue
            if self._path_cache[pid] == expected:
                result.append(window)
        return result

    def _logins(self):
        return [w for w in self._windows("RHID.exe", class_name="TFrm_Login") if w.is_visible()]

    def _panels(self):
        panels = [w for w in self._windows("RHID.exe", class_name="TFrm_RHID0010") if w.is_enabled()]
        visible = [w for w in panels if w.is_visible()]
        return visible or panels

    def _frequency(self):
        # TApplication tem o mesmo título, mas não é a janela navegável.
        return [w for w in self._windows("RHPA.exe", class_name="TFrm_RHPA0010",
                                        title_re=r"^Frequência(?:\s.*)?$") if w.is_enabled()]

    def _check_frequency_messages(self):
        # O usuário autorizou confirmar avisos de entrada com OK. Isso não
        # autoriza confirmação de exclusão, gravação ou troca de origem.
        dialogs = [w for w in self._windows("RHPA.exe", class_name="TMessageForm")
                   if w.is_visible()]
        if dialogs:
            if len(dialogs) == 1:
                dialog = dialogs[0]
                buttons = [b for b in dialog.descendants()
                           if b.class_name() in {'TButton', 'TBitBtn'}
                           and b.is_visible() and b.is_enabled()]
                if (dialog.window_text().strip().casefold() in {'information', 'informação', 'informacao'}
                        and len(buttons) == 1
                        and buttons[0].window_text().replace('&', '').strip().casefold() == 'ok'):
                    self._restore(dialog)
                    buttons[0].click_input()
                    self.warnings.append('Aviso informativo de entrada do Frequência confirmado com OK conforme autorização do usuário.')
                    return True
            raise RuntimeError("O módulo Frequência está bloqueado por uma mensagem do RH. "
                               "Confira a tela e ErroLog.Txt antes de repetir; "
                               "nenhum diálogo foi confirmado automaticamente.")

    def _frequency_ready(self):
        if self._check_frequency_messages():
            self._frequency_since = None
            return []
        windows = self._frequency()
        if not windows:
            self._frequency_since = None
            return []
        identity = windows[0].handle
        if getattr(self, '_frequency_handle', None) != identity or getattr(self, '_frequency_since', None) is None:
            self._frequency_handle = identity
            self._frequency_since = self.clock()
            return []
        return windows if self.clock() - self._frequency_since >= 1 else []

    def _startup_windows(self):
        """Evita confundir painel ainda não bloqueado com autenticação concluída."""
        dialogs = self._logins() or self._notices()
        if dialogs:
            self._startup_panel_since = None
            return dialogs
        panels = self._panels()
        if not panels:
            self._startup_panel_since = None
            return []
        since = getattr(self, '_startup_panel_since', None)
        if since is None:
            self._startup_panel_since = self.clock()
            return []
        return panels if self.clock() - since >= 0.8 else []

    def _notices(self):
        return [w for w in self._windows("RHID.exe", class_name="TFrm_ConfiguracoesInvalidas") if w.is_visible()]

    def _panel_after_notice(self):
        notices = self._notices()
        if notices:
            notice = _unique(notices, "aviso de Configurações Inválidas")
            if self.settings.rh_continue_invalid_config != "yes":
                raise RuntimeError("O RH exibiu Configurações Inválidas. RH_CONTINUE_INVALID_CONFIG=yes permite continuar nesse aviso específico.")
            if notice.handle not in self._acknowledged:
                self._restore(notice)
                button = _unique([b for b in notice.descendants(class_name="TBitBtn")
                                  if b.is_visible() and b.is_enabled()
                                  and b.window_text().replace("&", "").strip().casefold() in {"continuar", "ok"}],
                                 "botão Continuar/OK do aviso")
                button.click()
                self._acknowledged.add(notice.handle)
                self.warnings.append("RH exibiu Configurações Inválidas; aviso confirmado conforme configuração local.")
            return []
        return [] if self._logins() else self._panels()

    def _wait(self, probe, label):
        deadline = self.clock() + self.settings.ui_timeout
        while True:
            values = probe()
            if values:
                return _unique(values, label)
            if self.clock() >= deadline:
                raise RuntimeError(f"Tempo limite aguardando {label}. Confira avisos ou mensagens abertas no RH.")
            self.sleep(0.2)

    def _restore(self, window):
        if window.is_minimized() or not window.is_visible():
            window.restore()
        if not window.is_visible():
            raise RuntimeError("O RH está oculto na bandeja. Restaure sua janela para continuar.")
        window.set_focus()
        return window

    def _authenticate(self, dialog):
        if not self.settings.rh_user or not self.settings.rh_password:
            raise RuntimeError("Configure RH_USER e RH_PASSWORD no .env local.")
        self._restore(dialog)
        user, password, submit = login_controls(dialog)
        stage = 'preencher_usuario'
        try:
            _fill_without_logging(user, self.settings.rh_user)
            stage = 'validar_saida_usuario'
            # Tab dispara a validação de edt_Operador (OnExit) observada no recurso Delphi.
            user.type_keys("{TAB}")
            stage = 'conferir_campos'
            if not dialog.is_visible() or not password.is_enabled() or not submit.is_enabled():
                raise RuntimeError("Os controles mudaram durante a identificação.")
            stage = 'preencher_senha'
            _fill_without_logging(password, self.settings.rh_password)
            stage = 'confirmar_login'
            submit.click()
        except Exception as exc:
            # Não incluir detalhes de exceções de preenchimento, que podem carregar o texto.
            code = getattr(exc, 'winerror', None)
            diagnostic = f" Etapa={stage}; tipo={type(exc).__name__}" + (f"; codigo={code}" if isinstance(code, int) else '')
            raise RuntimeError("Não foi possível concluir o login do RH. Verifique a tela; não haverá repetição automática." + diagnostic) from None
        # Sumir a caixa não basta: exigir painel habilitado e ausência de login visível.
        return self._wait(self._panel_after_notice, "painel autenticado do RH")

    def start(self, *, authenticate=True):
        if self._check_desktop:
            require_interactive_desktop()
        self._check_frequency_messages()
        frequency = self._frequency()
        if frequency:
            self.window = self._restore(self._wait(self._frequency_ready, "Módulo de Frequência disponível"))
            return self
        logins = self._logins()
        panels = self._panels()
        notices = self._notices()
        if not logins and not panels and not notices:
            path = Path(self.settings.rh_path)
            if not path.is_file() or not Path(self.settings.rh_work_dir).is_dir():
                raise ValueError("Configure RH_PATH e RH_WORK_DIR com caminhos existentes.")
            subprocess.Popen([str(path)], cwd=self.settings.rh_work_dir,
                             stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            first = self._wait(self._startup_windows, "login ou painel do RH")
            logins = [first] if first.class_name() == "TFrm_Login" else []
            panels = [] if logins else [first]
        if logins and not authenticate:
            raise RuntimeError('Entre manualmente no RH e confira o alias ativo antes de executar o cenário.')
        panel = (self._authenticate(_unique(logins, "login do RH")) if logins else
                 self._wait(self._panel_after_notice, "painel autenticado do RH"))
        self._restore(panel)
        panel.menu_select(self.settings.rh_frequency_menu)
        self.window = self._restore(self._wait(self._frequency_ready, "Módulo de Frequência disponível"))
        return self

    def open_screen(self, name):
        """Rotas de ocorrências, férias e reservas validadas em RHFagundes."""
        if name not in SCREENS:
            raise ValueError("Tela desconhecida. Use ocorrencias, ferias, reservas ou pessoas.")
        if self.window is None:
            raise RuntimeError("Abra/conecte ao Módulo de Frequência antes de navegar.")
        self._check_frequency_messages()
        menu, class_name = SCREENS[name]
        self._restore(self.window)
        try:
            self.window.menu_select(menu)
        except OSError as exc:
            if getattr(exc, 'winerror', None) != 299:
                raise
            # O menu desta instalação falha em ReadProcessMemory. Os mnemônicos
            # &Programações, Registro de &Ocorrências e &Férias Cedidas
            # vêm do recurso instalado; exigir a classe resultante abaixo.
            self.window.type_keys({'ocorrencias': '%po', 'ferias': '%pf', 'reservas': '%pu',
                                   'pessoas': '%cp'}[name])
        screen = self.desktop.window(handle=self.window.handle).child_window(class_name=class_name)
        screen.wait("visible enabled", timeout=self.settings.ui_timeout)
        return screen
