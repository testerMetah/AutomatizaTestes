import time
from pathlib import Path

from automatiza.sequencias.relatorio import mask
from automatiza.pausa import ponto, tecla_reservada


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

    def attach(self, *, process_id, class_name):
        from pywinauto import Desktop
        windows = Desktop(backend="win32").windows(process=process_id, class_name=class_name)
        if not windows: raise UiBlocked(f"Janela {class_name} não encontrada")
        self.window = windows[0]
        self._event("abrir", None, None, "PASSOU", 0)
        return self.window

    def _meta(self, control):
        if control is None:
            return {}
        ei = control.element_info
        # O texto de TEdit pode conter senha; o log guarda o tipo sem ler o valor como rótulo.
        label = "<campo>" if control.class_name() == "TEdit" else control.window_text()
        return {"tipo": getattr(ei, "control_type", ""), "nome": label,
                "auto_id": getattr(ei, "automation_id", ""), "classe": control.class_name(),
                "found_index": None}

    def _event(self, action, control, value, result, elapsed, before=None, error=None, screenshot=None, dialogs=None,
               meta_override=None, tela_override=None):
        meta = meta_override if meta_override is not None else self._meta(control)
        tela = tela_override if tela_override is not None else {"titulo": self.window.window_text() if self.window else "",
                                                                    "classe": self.window.class_name() if self.window else "", "menu": self.menu_path}
        return self.report.emit("INTERACAO", tela=tela,
                                controle=meta, acao=action, valor=mask(value, meta.get("nome", "")),
                                valor_anterior=mask(before, meta.get("nome", "")), resultado=result,
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

    def interact(self, action, selector=None, value=None, important=False, sensitive=False):
        if action == "teclar" and tecla_reservada(value):
            raise UiBlocked("Este atalho está reservado para pausar o teste.")
        ponto({"acao": action, "seletor": str(selector) if selector else "janela principal"})
        if self.window is None:
            self.connect()
        if selector is None and action not in {"teclar", "fechar", "abrir"}:
            raise UiBlocked(f"Seletor ausente para {action}")
        if selector:
            from pywinauto import Desktop
            control = Desktop(backend="win32").window(**selector).wrapper_object()
        else:
            control = self.window
        before = control.window_text() if action in {"digitar", "selecionar"} else None
        meta_before = self._meta(control)
        tela_before = {"titulo": self.window.window_text(), "classe": self.window.class_name(), "menu": self.menu_path}
        start = time.perf_counter()
        try:
            if action == "clique":
                control.click_input(coords=tuple(value)) if isinstance(value, (list, tuple)) else control.click_input()
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
            self._event(action, control, "****" if sensitive else value, "FALHOU", time.perf_counter()-start,
                        "****" if sensitive else before, type(exc).__name__, shot,
                        meta_override=meta_before, tela_override=tela_before)
            raise
        shot = self.screenshot("passo") if important else None
        self._event(action, control, "****" if sensitive else value, "PASSOU", time.perf_counter()-start,
                    "****" if sensitive else before, screenshot=shot,
                    meta_override=meta_before, tela_override=tela_before)
        return before

    def read(self, selector):
        if self.window is None: self.connect()
        from pywinauto import Desktop
        return Desktop(backend="win32").window(**selector).wrapper_object().window_text()

    def inventory(self):
        if self.window is None: self.connect()
        items = []
        for control in self.window.descendants():
            try:
                items.append(self._meta(control))
            except (OSError, RuntimeError):
                # Controles MDI podem desaparecer enquanto a arvore e percorrida.
                continue
        self.report.emit("MAPA_TELA", tela={"titulo": self.window.window_text(), "classe": self.window.class_name(), "menu": self.menu_path},
                         controles=items, resultado="PASSOU")
        return items

    def open_menu(self, route):
        from pywinauto import Desktop
        if self.window is None: self.connect()
        self.window.set_focus()
        panel = Desktop(backend="uia").window(handle=self.window.handle)
        for caption in route:
            ponto({"acao": "abrir menu", "item": caption})
            spec = panel.child_window(title=caption, control_type="MenuItem", visible_only=True)
            spec.wait("visible enabled", timeout=10)
            item = spec.wrapper_object()
            meta = {"tipo": "MenuItem", "nome": caption, "auto_id": getattr(item.element_info, "automation_id", ""),
                    "classe": item.class_name(), "found_index": None}
            tela = {"titulo": self.window.window_text(), "classe": self.window.class_name(),
                    "menu": self.menu_path}
            start = time.perf_counter()
            item.click_input()
            parts = self.menu_path.split(" → ") if self.menu_path else []
            self.menu_path = " → ".join(parts + [caption])
            self._event("clique", None, caption, "PASSOU", time.perf_counter()-start,
                        meta_override=meta, tela_override=tela)
