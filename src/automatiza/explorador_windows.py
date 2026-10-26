"""Adaptador Windows para explorar formulários Delphi do Acessus."""

from __future__ import annotations

import re
import time
from datetime import datetime
from pathlib import Path

from pywinauto import Application, Desktop
from pywinauto.application import process_module

from automatiza.ambiente import require_interactive_desktop
from automatiza.rh import _fill_without_logging


MODULES = {
    "acesso": ("Acessus.exe", "TFrmPrincipal"),
    "refeitorio": ("Acessus.Refeitorio.exe", "TFrmRefeitorioViewsPrincipal"),
    "portaria": ("Acessus.Portaria.exe", "TFrmPortariaViewsPrincipal"),
    "estacionamento": ("Acessus.Estacionamento.exe", "TFrmEstacionamentoViewsPrincipal"),
    "escola": ("Acessus.Escola.exe", "TFrmEscolaViewsPrincipal"),
    "administracao": ("Acessus.Administracao.exe", "TFrmAdministracaoViewsPrincipal"),
}
SAFE_BUTTONS = {"cancelar", "fechar", "voltar", "anterior", "próximo", "proximo", "ajuda"}
MUTATING_WORDS = ("salvar", "gravar", "confirmar", "excluir", "apagar", "importar",
                  "exportar", "enviar", "processar", "gerar", "executar", "imprimir")
PASSWORD_WORDS = ("senha", "password", "token", "segredo", "secret")


def _caption(text: str) -> str:
    return text.replace("&", "").strip().casefold()


def _matches(rule, control) -> bool:
    if "classe" in rule and rule["classe"] != control["classe"]:
        return False
    if "id_controle" in rule and rule["id_controle"] != control["id_controle"]:
        return False
    if "legenda_regex" in rule and not re.search(rule["legenda_regex"], control["legenda"], re.I):
        return False
    if "rotulo_regex" in rule and not re.search(rule["rotulo_regex"], control["rotulo"], re.I):
        return False
    return True


class WindowsExplorerBackend:
    def __init__(self, config: dict, installation: Path = Path("C:/acesso")):
        self.config = config
        self.installation = Path(installation)
        self.main = None
        self.screen = None
        self.process_id = None
        self.module = None
        self.skipped = []
        self._event_logger = None

    def set_event_logger(self, callback):
        self._event_logger = callback

    def _emit(self, status, action, detail=""):
        if self._event_logger:
            self._event_logger(status, action, detail)

    def _click_menu(self, window, route):
        if not window.is_visible() or not window.is_enabled():
            raise RuntimeError("Janela bloqueada antes da navegação.")
        last_error = None
        for attempt in range(3):
            try:
                window.set_focus()
                panel = Desktop(backend="uia").window(handle=window.handle)
                for caption in route:
                    item = panel.child_window(title=caption, control_type="MenuItem", visible_only=True)
                    item.wait("visible enabled", timeout=5)
                    action = {"id": f"menu:{caption}", "tipo": "menu", "controle": caption}
                    self._emit("ANTES", action)
                    item.click_input()
                    self._emit("DEPOIS", action)
                    time.sleep(0.15)
                return
            except Exception as exc:
                last_error = exc
                self._emit("REPETIR_MENU", {"id": "menu:repetir", "tipo": "menu", "controle": route},
                           f"tentativa {attempt + 1}: {type(exc).__name__}")
                window.type_keys("{ESC}{ESC}")
                time.sleep(0.4)
        raise RuntimeError(f"Menu indisponível após três tentativas: {type(last_error).__name__}")

    def _screen_visible(self):
        try:
            return self.screen is not None and self.screen.is_visible()
        except Exception:
            return False

    def _main_window(self, module: str):
        executable, class_name = MODULES[module]
        candidates = []
        for window in Desktop(backend="win32").windows():
            if window.class_name() != class_name or not window.is_visible():
                continue
            try:
                path = Path(process_module(window.process_id()))
            except (OSError, RuntimeError):
                continue
            if path.name.casefold() == executable.casefold() and path.parent.resolve() == self.installation.resolve():
                candidates.append(window)
        if len(candidates) > 1:
            raise RuntimeError(f"Mais de uma janela principal de {module} encontrada.")
        return candidates[0] if candidates else None

    def _panel(self):
        candidates = [w for w in Desktop(backend="win32").windows()
                      if w.class_name() == "TFrmModuloViewsPrincipal" and w.is_visible()]
        if len(candidates) > 1:
            raise RuntimeError("Mais de um Painel de Módulos encontrado.")
        if candidates:
            return candidates[0]
        executable = self.installation / "Acessus.Modulo.exe"
        if not executable.is_file():
            raise FileNotFoundError(executable)
        Application(backend="win32").start(f'"{executable}"', work_dir=str(self.installation))
        deadline = time.monotonic() + 25
        while time.monotonic() < deadline:
            candidates = [w for w in Desktop(backend="win32").windows()
                          if w.class_name() == "TFrmModuloViewsPrincipal" and w.is_visible()]
            if len(candidates) == 1:
                return candidates[0]
            time.sleep(0.25)
        raise RuntimeError("Painel não autenticado ou indisponível; login manual necessário.")

    def _ensure_module(self, module: str):
        window = self._main_window(module)
        if window:
            return window
        panel = self._panel()
        label = module.capitalize() if module != "refeitorio" else "Refeitório"
        if module == "administracao":
            label = "Administração"
        self._click_menu(panel, ["Modulos", label])
        deadline = time.monotonic() + 25
        while time.monotonic() < deadline:
            window = self._main_window(module)
            if window:
                return window
            time.sleep(0.25)
        raise RuntimeError(f"Módulo {module} não abriu; verificar sessão e login.")

    def _forms(self):
        if not self.main:
            return []
        process = self.main.process_id()
        windows = list(Desktop(backend="win32").windows(process=process))
        windows += self.main.descendants()
        unique = {w.handle: w for w in windows
                  if w.handle != self.main.handle and w.is_visible()
                  and (w.class_name().startswith(("TFrm", "TF")) or w.class_name() == "#32770")}
        return list(unique.values())

    def open(self, route: dict):
        require_interactive_desktop()
        self.module = route["modulo"]
        self.main = self._ensure_module(self.module)
        self.process_id = self.main.process_id()
        before = {w.handle for w in self._forms()}
        self._click_menu(self.main, route["menu"])
        deadline = time.monotonic() + 12
        while time.monotonic() < deadline:
            new = [w for w in self._forms() if w.handle not in before and w.is_enabled()]
            if new:
                self.screen = max(new, key=lambda w: w.rectangle().width() * w.rectangle().height())
                if self.config.get("exploracao", {}).get("entrar_em_cadastro", False):
                    self._enter_edit()
                return
            time.sleep(0.2)
        raise RuntimeError("Rota não abriu formulário novo; pode ser uma ação imediata ou menu alterado.")

    def _enter_edit(self):
        candidates = [c for c in self._controls()
                      if "button" in c.class_name().casefold()
                      and re.match(r"^(incluir|novo|adicionar)\b", _caption(c.window_text()))]
        if len(candidates) != 1:
            self._emit("SEM_EDICAO", {"id": "cadastro:entrada", "tipo": "inventario", "controle": self.screen.class_name()},
                       f"{len(candidates)} botões de inclusão")
            return
        button = candidates[0]
        action = {"id": "cadastro:incluir", "tipo": "clicar", "controle": button.window_text()}
        before = {w.handle for w in self._forms()}
        self._emit("ANTES", action)
        button.click_input()
        self._emit("DEPOIS", action)
        time.sleep(0.25)
        new = [w for w in self._forms() if w.handle not in before and w.is_enabled()]
        if new:
            self.screen = max(new, key=lambda w: w.rectangle().width() * w.rectangle().height())
        if not any(re.match(r"^(salvar|gravar)\b", _caption(c.window_text()))
                   for c in self._controls() if "button" in c.class_name().casefold()):
            raise RuntimeError("Clique em Incluir não disponibilizou botão de gravação.")
        self._emit("ESTADO_EDICAO", action, self.screen.class_name())

    def _controls(self):
        if not self._screen_visible():
            raise RuntimeError("Formulário não está aberto.")
        return [c for c in self.screen.descendants() if c.is_visible() and c.is_enabled()]

    def _descriptor(self, index, control):
        label = ""
        class_name = control.class_name().casefold()
        is_field = any(word in class_name for word in
                       ("edit", "memo", "combobox", "listbox", "password",
                        "grid", "treeview", "datetimepicker"))
        if "edit" in class_name or "memo" in class_name:
            rect = control.rectangle()
            candidates = []
            for other in self.screen.descendants():
                if other.handle == control.handle or not other.is_visible() or not other.window_text():
                    continue
                if not any(word in other.class_name().casefold() for word in ("label", "static")):
                    continue
                position = other.rectangle()
                vertical = abs((position.top + position.bottom) - (rect.top + rect.bottom))
                if position.right <= rect.left + 20 and vertical < 50:
                    candidates.append((rect.left - position.right + vertical, other.window_text()))
            if candidates:
                label = min(candidates)[1][:120]
        location = control.rectangle()
        origin = self.screen.rectangle()
        return {"indice": index, "classe": control.class_name(), "id_controle": control.control_id(),
                "legenda": "" if is_field else control.window_text()[:120], "rotulo": label,
                "posicao": [location.left - origin.left, location.top - origin.top]}

    def _values_for(self, descriptor, config):
        label = (descriptor["legenda"] + " " + descriptor["rotulo"]).casefold()
        if any(word in label for word in PASSWORD_WORDS):
            return []
        for rule in config.get("regras_campos", []):
            if _matches(rule, descriptor):
                return rule["valores"]
        class_name = descriptor["classe"].casefold()
        if "date" in class_name or "data" in label:
            return config["valores"].get("data", [])
        if "time" in class_name or "hora" in label:
            return config["valores"].get("hora", [])
        if any(word in class_name + label for word in ("spin", "numero", "número", "quantidade")):
            return config["valores"].get("numero", [])
        return config["valores"].get("texto", [])

    def _button_allowed(self, descriptor, config):
        label = _caption(descriptor["legenda"])
        policy = config["politica"]
        if any(word in label for word in PASSWORD_WORDS):
            return False
        if not policy.get("permitir_gravacao", False):
            return label in SAFE_BUTTONS
        allowed = [_caption(x) for x in policy.get("botoes_autorizados", [])]
        if any(word in label for word in MUTATING_WORDS):
            return "*" in allowed or label in allowed
        return label in SAFE_BUTTONS or "*" in allowed or label in allowed

    def _tab(self, title):
        tabs = Desktop(backend="uia").window(handle=self.screen.handle).descendants(control_type="TabItem")
        matching = [tab for tab in tabs if tab.is_visible() and tab.is_enabled()
                    and tab.window_text() == title]
        if len(matching) != 1:
            raise RuntimeError(f"Aba {title!r} não encontrada de forma única.")
        action = {"id": f"aba:{title}", "tipo": "aba", "controle": title}
        self._emit("ANTES", action)
        matching[0].click_input()
        self._emit("DEPOIS", action)
        time.sleep(0.15)

    def discover(self, config: dict, *, _tab_title=None, _tab_index=None):
        actions = []
        if _tab_title is None:
            self.skipped = []
            try:
                tabs = Desktop(backend="uia").window(handle=self.screen.handle).descendants(control_type="TabItem")
                titles = [tab.window_text() for tab in tabs
                          if tab.is_visible() and tab.is_enabled() and tab.window_text()]
            except Exception as exc:
                titles = []
                self.skipped.append({"motivo": "abas UIA indisponíveis", "erro": type(exc).__name__})
            if titles:
                for tab_index, title in enumerate(dict.fromkeys(titles)):
                    self._tab(title)
                    actions.extend(self.discover(config, _tab_title=title, _tab_index=tab_index))
                return actions
        for index, control in enumerate(self._controls()):
            item = self._descriptor(index, control)
            class_name = item["classe"].casefold()
            if any(word in class_name for word in ("password", "grid", "treeview")):
                self.skipped.append({"controle": item, "motivo": "tipo não preenchível"})
                continue
            if ("edit" in class_name or "memo" in class_name) and not control.has_style(0x20):
                values = self._values_for(item, config)
                if not values:
                    self.skipped.append({"controle": item, "motivo": "campo sensível ou sem valor configurado"})
                for value_index, value in enumerate(values):
                    actions.append({"id": f"preencher:{index}:{value_index}", "tipo": "preencher",
                                    "controle": item, "valor": value})
            elif "combobox" in class_name:
                values = config["valores"].get("combo", [])
                if not values and config.get("exploracao", {}).get("combo_auto", False):
                    try:
                        values = [value for value in control.item_texts() if value.strip()]
                        values = values[:config["exploracao"].get("max_opcoes_combo", 5)]
                    except Exception as exc:
                        self.skipped.append({"controle": item, "motivo": "opções do combo indisponíveis",
                                             "erro": type(exc).__name__})
                        values = []
                if not values:
                    self.skipped.append({"controle": item, "motivo": "opções de combo não configuradas"})
                for value_index, value in enumerate(values):
                    actions.append({"id": f"selecionar:{index}:{value_index}", "tipo": "selecionar",
                                    "controle": item, "valor": value})
            elif "datetimepicker" in class_name:
                is_time = "hora" in item["rotulo"].casefold() or "time" in item["rotulo"].casefold()
                mode = "hora" if is_time else "data"
                for value_index, value in enumerate(config["valores"].get(mode, [])):
                    actions.append({"id": f"{mode}:{index}:{value_index}", "tipo": mode,
                                    "controle": item, "valor": value})
            elif "listbox" in class_name:
                values = config["valores"].get("lista", [])
                if not values:
                    self.skipped.append({"controle": item, "motivo": "seleções de lista não configuradas"})
                for value_index, value in enumerate(values):
                    actions.append({"id": f"lista:{index}:{value_index}", "tipo": "lista",
                                    "controle": item, "valor": value})
            elif "checkbox" in class_name or "radiobutton" in class_name:
                actions.append({"id": f"alternar:{index}", "tipo": "alternar", "controle": item})
            elif "button" in class_name or "bitbtn" in class_name or "speedbutton" in class_name:
                if self._button_allowed(item, config):
                    actions.append({"id": f"clicar:{index}", "tipo": "clicar", "controle": item})
                else:
                    self.skipped.append({"controle": item, "motivo": "botão não autorizado pela política"})
        if _tab_title is not None:
            for action in actions:
                action["id"] = f"aba{_tab_index}:" + action["id"]
                action["aba"] = _tab_title
        return actions

    def perform(self, action: dict):
        descriptor = action["controle"]
        kind = action["tipo"]
        if "aba" in action:
            self._tab(action["aba"])
        candidates = []
        for index, candidate in enumerate(self._controls()):
            if candidate.class_name() != descriptor["classe"]:
                continue
            current = self._descriptor(index, candidate)
            if descriptor["legenda"] and current["legenda"] != descriptor["legenda"]:
                continue
            if descriptor["rotulo"] and current["rotulo"] != descriptor["rotulo"]:
                continue
            distance = (abs(current["posicao"][0] - descriptor["posicao"][0])
                        + abs(current["posicao"][1] - descriptor["posicao"][1]))
            candidates.append((distance, candidate))
        candidates.sort(key=lambda item: item[0])
        if not candidates or candidates[0][0] > 80 or (
                len(candidates) > 1 and candidates[0][0] == candidates[1][0]):
            raise RuntimeError("Controle não encontrado de forma única na posição esperada.")
        control = candidates[0][1]
        previous = None
        if kind == "alternar":
            try:
                previous = control.get_check_state()
            except (AttributeError, RuntimeError):
                pass
        if kind == "preencher":
            if control.has_style(0x20):
                raise RuntimeError("Campo de senha não é preenchido pelo explorador.")
            _fill_without_logging(control, action["valor"])
        elif kind == "selecionar":
            control.select(action["valor"])
        elif kind == "data":
            value = datetime.strptime(action["valor"], "%d/%m/%Y")
            control.set_time(year=value.year, month=value.month, day=value.day)
        elif kind == "hora":
            value = datetime.strptime(action["valor"], "%H:%M")
            control.set_time(hour=value.hour, minute=value.minute)
        elif kind == "lista":
            control.select(action["valor"])
        elif kind in ("alternar", "clicar"):
            control.click_input()
        else:
            raise ValueError(f"Ação inválida: {kind}")
        time.sleep(0.15)
        dialogs = [w for w in Desktop(backend="win32").windows(process=self.process_id)
                   if w.class_name() == "#32770" and w.is_visible()]
        if dialogs:
            messages = [" ".join(c.window_text() for c in w.descendants()
                                 if c.class_name() == "Static" and c.window_text())[:300]
                        for w in dialogs]
            validation = {"status": "FALHOU", "motivo": "Diálogo bloqueador após a ação",
                          "mensagens": messages}
        else:
            validation = self._validate_control(action, control, previous)
        return {"janelas_visiveis": [w.window_text() for w in dialogs[:8]],
                "formulario_visivel": self._screen_visible(), "validacao": validation}

    def _validate_control(self, action, control, previous):
        kind = action["tipo"]
        expected = action.get("valor")
        try:
            if kind == "preencher":
                actual = control.window_text()
                return {"status": "APROVADO" if actual == expected else "FALHOU",
                        "esperado": expected, "observado": actual}
            if kind in ("selecionar", "lista"):
                actual = control.selected_text()
                return {"status": "APROVADO" if actual == expected else "FALHOU",
                        "esperado": expected, "observado": actual}
            if kind == "alternar":
                actual = control.get_check_state()
                if "radiobutton" in control.class_name().casefold():
                    expected = 1
                elif previous is not None:
                    expected = 0 if previous else 1
                else:
                    return {"status": "NAO_VERIFICADO", "motivo": "Estado inicial indisponível."}
                return {"status": "APROVADO" if actual == expected else "FALHOU",
                        "esperado": expected, "observado": actual}
            if kind in ("data", "hora"):
                actual = control.get_time()
                if kind == "data":
                    observed = f"{actual.day:02d}/{actual.month:02d}/{actual.year:04d}"
                else:
                    observed = f"{actual.hour:02d}:{actual.minute:02d}"
                return {"status": "APROVADO" if observed == expected else "FALHOU",
                        "esperado": expected, "observado": observed}
            return {"status": "NAO_VERIFICADO",
                    "motivo": "Clique sem resultado de negócio genérico verificável."}
        except (AttributeError, RuntimeError, ValueError) as exc:
            return {"status": "NAO_VERIFICADO",
                    "motivo": f"Leitura do controle indisponível: {type(exc).__name__}"}

    def _dismiss_dialogs(self):
        if self.process_id is None:
            return
        dialogs = [w for w in Desktop(backend="win32").windows(process=self.process_id)
                   if w.class_name() == "#32770" and w.is_visible()]
        for dialog in dialogs:
            message = " ".join(c.window_text() for c in dialog.descendants()
                               if c.class_name() == "Static" and c.window_text())[:300]
            buttons = [c for c in dialog.descendants() if c.class_name() == "Button"
                       and c.is_visible() and c.is_enabled()]
            choice = next((c for title in ("não", "nao", "descartar", "cancelar", "ok")
                           for c in buttons if _caption(c.window_text()) == title), None)
            if choice is None:
                raise RuntimeError(f"Diálogo bloqueador sem resposta segura: {dialog.window_text()}")
            action = {"id": "recuperacao:dialogo", "tipo": "clicar", "controle": choice.window_text()}
            self._emit("DIALOGO_BLOQUEADOR", action, message)
            self._emit("ANTES", action)
            choice.click_input()
            self._emit("DEPOIS", action)
            time.sleep(0.2)

    def reset(self):
        self._dismiss_dialogs()
        if self.screen is None:
            return
        if self._screen_visible():
            buttons = [c for c in self.screen.descendants() if c.is_visible() and c.is_enabled()
                       and re.match(r"^(cancelar|fechar)\b", _caption(c.window_text()))
                       and any(x in c.class_name().casefold() for x in ("button", "btn"))]
            cancel = [c for c in buttons if _caption(c.window_text()).startswith("cancelar")]
            if len(cancel) == 1:
                buttons = cancel
            if len(buttons) == 1:
                action = {"id": "recuperacao:cancelar", "tipo": "clicar", "controle": buttons[0].window_text()}
                self._emit("ANTES", action)
                buttons[0].click_input()
                self._emit("DEPOIS", action)
                time.sleep(0.2)
            if self._screen_visible():
                action = {"id": "recuperacao:fechar", "tipo": "fechar", "controle": self.screen.class_name()}
                self._emit("ANTES", action)
                self.screen.close()
                self._emit("DEPOIS", action)
                time.sleep(0.2)
        self._dismiss_dialogs()
        if self._screen_visible():
            raise RuntimeError("Formulário permaneceu aberto; recuperação manual necessária.")
        self.screen = None

    def capture(self, path: Path):
        if not self.config["politica"].get("capturar_erros", False):
            raise RuntimeError("Captura de tela desativada para evitar dados pessoais.")
        path.parent.mkdir(parents=True, exist_ok=True)
        self.screen.capture_as_image().save(str(path))
