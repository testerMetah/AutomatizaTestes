import time
from pathlib import Path

from automatiza.sequencias.relatorio import mask


class UiBlocked(RuntimeError):
    pass


class Gateway:
    """Envolve cada gesto; seletores devem vir de mapa validado no build atual."""

    def __init__(self, report, exe=r"C:\acesso\Acessus.exe"):
        self.report, self.exe = report, exe
        self.window = None
        self.menu_path = ""

    def connect(self):
        from pywinauto import Desktop
        windows = Desktop(backend="win32").windows(class_name="TFrmPrincipal")
        if not windows:
            raise UiBlocked("Janela TFrmPrincipal não encontrada; abrir Acessus e mapear o build atual")
        self.window = windows[0]
        self._event("abrir", None, None, "PASSOU", 0)
        return self.window

    def _meta(self, control):
        if control is None:
            return {}
        ei = control.element_info
        return {"tipo": getattr(ei, "control_type", ""), "nome": control.window_text(),
                "auto_id": getattr(ei, "automation_id", ""), "classe": control.class_name(),
                "found_index": None}

    def _event(self, action, control, value, result, elapsed, before=None, error=None, screenshot=None, dialogs=None):
        title = self.window.window_text() if self.window else ""
        cls = self.window.class_name() if self.window else ""
        return self.report.emit("INTERACAO", tela={"titulo": title, "classe": cls, "menu": self.menu_path},
                                controle=self._meta(control), acao=action, valor=mask(value, self._meta(control).get("nome", "")),
                                valor_anterior=mask(before, self._meta(control).get("nome", "")), resultado=result,
                                erro=str(error) if error else None, avisos=dialogs or [], duracao_ms=round(elapsed * 1000, 2), screenshot=screenshot)

    def screenshot(self, label):
        if self.window is None:
            return None
        folder = self.report.folder / "capturas"
        folder.mkdir(exist_ok=True)
        path = folder / f"{len(self.report.events)+1:05d}-{label}.png"
        try:
            self.window.capture_as_image().save(path)
            return str(path.relative_to(self.report.folder))
        except Exception as exc:
            self.report.emit("AVISO", regra="captura", motivo=f"Captura indisponível: {type(exc).__name__}")
            return None

    def interact(self, action, selector=None, value=None, important=False):
        if self.window is None:
            self.connect()
        if selector is None and action not in {"teclar", "fechar", "abrir"}:
            raise UiBlocked(f"Seletor ausente para {action}")
        control = self.window.child_window(**selector).wrapper_object() if selector else self.window
        before = control.window_text() if action in {"digitar", "selecionar"} else None
        start = time.perf_counter()
        try:
            if action == "clique": control.click_input()
            elif action == "duplo_clique": control.double_click_input()
            elif action == "digitar": control.set_edit_text(str(value))
            elif action == "selecionar": control.select(value)
            elif action == "marcar": control.check() if value else control.uncheck()
            elif action == "teclar": control.type_keys(str(value), set_foreground=True)
            elif action == "rolar": control.scroll(wheel_dist=int(value))
            elif action == "fechar": control.close()
            else: raise ValueError(f"Ação de interface desconhecida: {action}")
        except Exception as exc:
            shot = self.screenshot("falha")
            self._event(action, control, value, "FALHOU", time.perf_counter()-start, before, type(exc).__name__, shot)
            raise
        shot = self.screenshot("passo") if important else None
        self._event(action, control, value, "PASSOU", time.perf_counter()-start, before, screenshot=shot)
        return before

    def read(self, selector):
        if self.window is None: self.connect()
        return self.window.child_window(**selector).wrapper_object().window_text()

    def inventory(self):
        if self.window is None: self.connect()
        items = [self._meta(control) for control in self.window.descendants()]
        self.report.emit("MAPA_TELA", tela={"titulo": self.window.window_text(), "classe": self.window.class_name(), "menu": self.menu_path},
                         controles=items, resultado="PASSOU")
        return items
