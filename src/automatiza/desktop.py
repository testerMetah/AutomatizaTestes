from pathlib import Path

from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.timings import TimeoutError as UiTimeoutError

from automatiza.config import Settings
from automatiza.ambiente import require_interactive_desktop


class DesktopApp:
    def __init__(self, settings: Settings):
        if settings.app_backend not in {"win32", "uia"}:
            raise ValueError("APP_BACKEND deve ser win32 ou uia.")
        if not settings.app_title_re:
            raise ValueError("Configure APP_TITLE_RE no .env.")
        self.settings = settings
        self.app = Application(backend=settings.app_backend)
        self.window = None

    def connect(self):
        """Conecta à aplicação já aberta, sem abrir uma segunda instância."""
        require_interactive_desktop()
        try:
            self.app.connect(title_re=self.settings.app_title_re,
                             timeout=self.settings.ui_timeout)
        except (ElementNotFoundError, UiTimeoutError) as exc:
            raise RuntimeError(
                f"Janela da aplicação não encontrada em {self.settings.ui_timeout}s "
                f"(APP_TITLE_RE={self.settings.app_title_re!r}). "
                "Este teste conecta ao módulo já aberto. No Painel de Módulos, "
                "abra o Acesso e aguarde sua janela principal antes de tentar novamente. "
                "Se a janela já estiver aberta, confira APP_TITLE_RE no .env."
            ) from exc
        return self._main_window()

    def start(self):
        require_interactive_desktop()
        # Reutiliza o módulo se já estiver aberto; evita dispará-lo novamente pelo painel.
        try:
            self.app.connect(title_re=self.settings.app_title_re, timeout=1)
        except (ElementNotFoundError, UiTimeoutError):
            pass
        else:
            return self._main_window()
        if self.settings.launcher_path:
            return self._start_via_launcher()
        path = Path(self.settings.app_path)
        if not path.is_file():
            raise ValueError("Configure APP_PATH com o caminho de um executável existente.")
        if path.name.casefold() == 'acessus.exe':
            panel_path = path.with_name('Acessus.Modulo.exe')
            if not panel_path.is_file():
                raise ValueError('O Acessus exige abertura pelo painel Acessus.Modulo.exe, não encontrado na pasta do módulo.')
            return self._start_via_launcher(
                path=panel_path, title_re=r'^Sistema Acessus.*Painel de Módulos.*$',
                menu_path='Modulos->Acesso')
        self.app.start(f'"{path}"', work_dir=self.settings.app_work_dir or str(path.parent))
        return self._main_window()

    def _start_via_launcher(self, *, path=None, title_re=None, menu_path=None):
        # O painel e o módulo são processos distintos.
        path = Path(path or self.settings.launcher_path)
        title_re = title_re or self.settings.launcher_title_re
        menu_path = menu_path or self.settings.launcher_menu_path
        if not path.is_file():
            raise ValueError("LAUNCHER_PATH precisa apontar para um executável existente.")
        if not title_re or not menu_path:
            raise ValueError("Configure LAUNCHER_TITLE_RE e LAUNCHER_MENU_PATH.")
        if self.settings.app_backend != "win32":
            raise ValueError("A abertura pelo menu do painel usa APP_BACKEND=win32.")
        launcher = Application(backend="win32")
        try:
            launcher.connect(title_re=title_re, timeout=1)
        except (ElementNotFoundError, UiTimeoutError):
            launcher.start(f'"{path}"',
                           work_dir=self.settings.app_work_dir or str(path.parent))
        panel = launcher.window(title_re=title_re)
        try:
            panel.wait("visible enabled", timeout=self.settings.ui_timeout)
        except UiTimeoutError as exc:
            raise RuntimeError(
                "O painel não ficou disponível. Verifique se há uma tela de login ou "
                "configuração de banco pendente. A automação não preenche essas telas."
            ) from exc
        if panel.class_name() == 'TFrmModuloViewsPrincipal':
            from automatiza.menus import click_uia_menu
            click_uia_menu(panel.wrapper_object(), menu_path.split('->'))
        else:
            panel.menu_select(menu_path)
        # Conecta à janela do módulo em seu próprio processo.
        return self.connect()

    def _main_window(self):
        self.window = self.app.window(title_re=self.settings.app_title_re)
        self.window.wait("visible enabled", timeout=self.settings.ui_timeout)
        return self

    def control(self, **selector):
        if self.window is None:
            raise RuntimeError("Conecte ou abra a aplicação primeiro.")
        control = self.window.child_window(**selector)
        control.wait("visible enabled", timeout=self.settings.ui_timeout)
        return control

    def click(self, **selector):
        self.control(**selector).click_input()

    def fill(self, text: str, **selector):
        self.control(**selector).set_edit_text(text)

    def screenshot(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.window.capture_as_image().save(str(path))
