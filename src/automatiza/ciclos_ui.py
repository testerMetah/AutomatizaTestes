"""CRUD de férias e ocorrências em dias no RH instalado, sem handles persistidos."""
import time
from dataclasses import replace
from datetime import datetime

from automatiza.ciclos import Blocked


class RhLifecycleUI:
    def __init__(self, settings, config):
        from automatiza.execucao import WindowsActions
        self.config = config
        self.actions = WindowsActions(replace(settings, rh_continue_invalid_config="yes"))
        self.app = self.actions.app
        self.app.start()
        if self.actions.origin_alias() != config["origem"]:
            raise Blocked("Alias ativo do RH não corresponde à origem do manifesto.")

    def dialogs(self):
        from pywinauto import Desktop
        return [w for w in Desktop(backend="win32").windows(process=self.root.process_id())
                if w.is_visible() and w.class_name() in {"TMessageForm", "TFrm_Erro"}]

    def field(self, cls, offset, *, enabled=True):
        # Coordenada horizontal relativa ao formulário maximizado, não à tela/handle.
        fields = [c for c in self.form.descendants() if c.is_visible() and (not enabled or c.is_enabled())
                  and c.class_name() == cls and
                  abs(c.rectangle().left - self.form.rectangle().left - offset) <= 1]
        if len(fields) != 1:
            raise Blocked(f"Layout RH mudou: {cls}, posição relativa {offset}, encontrados {len(fields)}.")
        return fields[0]

    def type(self, control, text):
        from pywinauto import keyboard
        control.click_input()
        control.set_keyboard_focus()
        if not control.has_keyboard_focus():
            raise Blocked("Campo não recebeu foco de teclado.")
        # A primeira edição pode ativar o dataset Delphi e deslocar o foco.
        keyboard.send_keys("{HOME}+{END}{DELETE}", pause=.08)
        time.sleep(.2)
        control.set_keyboard_focus()
        if not control.has_keyboard_focus():
            raise Blocked("RH deslocou o foco durante a entrada em edição.")
        keyboard.send_keys(text + "{TAB}", pause=.08)
        time.sleep(.3)

    def apply(self, case, action, end, screenshot, *, expected_before):
        import win32gui
        from pywinauto import Desktop, keyboard, mouse
        self.root = self.app.window.wrapper_object() if hasattr(self.app.window, "wrapper_object") else self.app.window
        if self.dialogs():
            raise Blocked("Diálogo pendente no RH; nenhuma operação iniciada.")
        self.root.maximize()
        screen = "ferias" if case["tipo"] == "ferias" else "ocorrencias"
        self.app.open_screen(screen)
        # Seleciona explicitamente a unidade pelo seletor nativo.
        self.root.set_focus()
        win32gui.PostMessage(self.root.handle, 0x111, 28, 0)
        dialog = Desktop(backend="win32").window(class_name="TFrm_UniEmpNovo",
                                               process=self.root.process_id())
        dialog.wait("visible enabled", timeout=8)
        boxes = [c for c in dialog.descendants(class_name="TListBox") if c.is_visible()]
        if len(boxes) != 1:
            raise Blocked("Seletor de unidade não identificado.")
        values = [s for s in boxes[0].item_texts() if s.startswith(self.config["unidade"] + " -")]
        if len(values) != 1:
            raise Blocked("Unidade não encontrada de forma única.")
        boxes[0].select(values[0])
        boxes[0].type_keys("{ENTER}")
        time.sleep(.5)
        cls = "TFrm_RHPA5130" if screen == "ferias" else "TFrm_RHPA5020"
        forms = [c for c in self.root.descendants() if c.class_name() == cls and c.is_visible()]
        if len(forms) != 1:
            raise Blocked("Formulário não identificado de forma única.")
        self.form = forms[0]
        self.form.maximize()
        if abs(self.form.rectangle().width() - 1286) > 3:
            raise Blocked("Resolução/layout diferente do mapa validado de 1280 pixels.")
        contract = self.field("TEdit", 67 if screen == "ferias" else 68)
        self.type(contract, str(self.config["contrato"]))
        time.sleep(.7)
        if contract.window_text() != str(self.config["contrato"]):
            raise Blocked("Contrato não confirmado na tela.")
        start_date = datetime.fromisoformat(case["inicio"])
        start = start_date.strftime("%d/%m/%Y")
        hourly = screen == "ocorrencias" and start_date.time() != datetime.min.time()
        start_offset = 26 if screen == "ferias" else 522
        grid_class = "TDBMetaGrid" if screen == "ferias" else "TDBGrid"
        grids = [c for c in self.form.descendants() if c.class_name() == grid_class and c.is_visible()]
        if len(grids) != 1:
            raise Blocked("Grade de registros não identificada.")
        grids[0].click_input()
        grids[0].set_keyboard_focus()
        if action == "criar":
            # Código e início formam a chave. Definir os dois antes de disparar
            # OnExit evita criar uma linha com a data da seleção anterior.
            start_control = self.field("TMaskEdit", start_offset)
            start_control.set_edit_text(start)
            if screen == "ocorrencias":
                code = self.field("TEdit", 19)
                code.set_edit_text(case["ocorrencia"])
            start_control.set_keyboard_focus()
            keyboard.send_keys("{TAB}")
            time.sleep(.5)
            current_start = self.field("TMaskEdit", start_offset, enabled=False)
            if current_start.window_text() != start and current_start.is_enabled():
                # Ao sair do código, algumas versões carregam a primeira linha
                # dele e substituem a data; escrever o início uma segunda vez.
                self.type(current_start, datetime.fromisoformat(case["inicio"]).strftime("%d%m%Y"))
            if self.field("TMaskEdit", start_offset, enabled=False).window_text() != start:
                raise Blocked("Chave nova não corresponde ao início esperado.")
            if hourly:
                # Nesta tela a chave da faixa de horas só é completada ao sair
                # da hora inicial. Antes disso ainda aparece o término da
                # primeira linha do mesmo código, apesar da nova data visível.
                self.type(self.field("TMaskEdit", 626), start_date.strftime("%H%M"))
                if self.field("TMaskEdit", 626, enabled=False).window_text() != start_date.strftime("%H:%M"):
                    raise Blocked("Hora inicial nova não corresponde ao plano.")
            if (screen == "ocorrencias" and
                    any(ch.isdigit() for ch in self.field("TDBEdit", 734).window_text())):
                raise Blocked("Chave nova não abriu campos vazios; criação não prosseguida.")
        else:
            # Os campos inferiores são edição da linha, não filtros de pesquisa.
            target = (start, case["ocorrencia"] if screen == "ocorrencias" else "")
            if screen == "ferias":
                # TDBMetaGrid não responde a Down; usar linhas visíveis e rolagem.
                seen = set()
                found = False
                rect = grids[0].rectangle()
                count = min(40, max(1, (rect.height() - 48) // 18))
                for _ in range(25):
                    new = False
                    for row in range(count):
                        mouse.click(coords=(rect.left + 70, rect.top + 27 + row * 18))
                        time.sleep(.05)
                        key = (self.field("TMaskEdit", start_offset).window_text(), "")
                        if key == target:
                            found = True
                            break
                        if key not in seen:
                            seen.add(key)
                            new = True
                    if found:
                        break
                    if not new:
                        raise Blocked("Registro esperado não localizado na grade de férias.")
                    mouse.scroll(coords=(rect.right - 25, rect.top + 150), wheel_dist=-6)
                    time.sleep(.3)
                if not found:
                    raise Blocked("Limite de navegação da grade de férias excedido.")
            else:
                keyboard.send_keys("^{HOME}")
                time.sleep(.3)
                seen = set()
                for _ in range(500):
                    key = (self.field("TMaskEdit", start_offset).window_text(),
                           self.field("TEdit", 19).window_text())
                    if key == target:
                        break
                    if key in seen:
                        raise Blocked("Registro esperado não localizado na grade.")
                    seen.add(key)
                    keyboard.send_keys("{DOWN}")
                    time.sleep(.1)
                else:
                    raise Blocked("Limite de navegação da grade excedido.")
            displayed_end = self.field("TDBEdit", 202 if screen == "ferias" else 734).window_text()
            if displayed_end != datetime.fromisoformat(expected_before).strftime("%d/%m/%Y"):
                raise Blocked("Linha selecionada não corresponde ao término conferido na origem.")
            if hourly and self.field("TDBEdit", 833).window_text() != datetime.fromisoformat(expected_before).strftime("%H:%M"):
                raise Blocked("Linha selecionada não corresponde à hora final da origem.")
        start_field = self.field("TMaskEdit", start_offset, enabled=False)
        if self.dialogs() or start_field.window_text() != start:
            raise Blocked("Data de início não confirmada.")
        if screen == "ocorrencias" and self.field("TEdit", 19, enabled=False).window_text() != case["ocorrencia"]:
            raise Blocked("Código de ocorrência não confirmado.")
        if hourly and self.field("TMaskEdit", 626, enabled=False).window_text() != start_date.strftime("%H:%M"):
            raise Blocked("Hora inicial não confirmada.")
        if action == "excluir":
            # Excluir somente após selecionar a chave conferida pelo backend.
            self.form.capture_as_image().save(str(screenshot))
            win32gui.PostMessage(self.root.handle, 0x111, 11, 0)
            time.sleep(.7)
            modals = self.dialogs()
            if len(modals) != 1 or modals[0].class_name() != "TMessageForm":
                raise Blocked("Confirmação de exclusão esperada não apareceu.")
            modals[0].capture_as_image().save(str(screenshot.with_name(screenshot.stem + "-confirmacao.png")))
            buttons = [c for c in modals[0].descendants() if c.class_name() == "TButton"
                       and c.window_text().replace("&", "").casefold() == "sim"]
            if len(buttons) != 1:
                raise Blocked("Botão de confirmação de exclusão não encontrado.")
            buttons[0].click_input()
        else:
            date = datetime.fromisoformat(end)
            end_offset = 202 if screen == "ferias" else 734
            self.type(self.field("TDBEdit", end_offset), date.strftime("%d%m%Y"))
            if hourly:
                self.type(self.field("TDBEdit", 833), date.strftime("%H%M"))
            for _ in range(30):
                displayed_end = self.field("TDBEdit", end_offset).window_text().strip()
                displayed_time = self.field("TDBEdit", 833).window_text().strip() if hourly else None
                if (displayed_end == date.strftime("%d/%m/%Y") and
                        (not hourly or displayed_time == date.strftime("%H:%M"))) or self.dialogs():
                    break
                time.sleep(.1)
            self.form.capture_as_image().save(str(screenshot))
            if displayed_end != date.strftime("%d/%m/%Y"):
                raise Blocked(f"Término preenchido não corresponde ao plano: {displayed_end!r}.")
            if hourly and displayed_time != date.strftime("%H:%M"):
                raise Blocked(f"Hora final preenchida não corresponde ao plano: {displayed_time!r}.")
        win32gui.PostMessage(self.root.handle, 0x111, 9, 0)
        time.sleep(.8)
        if self.dialogs():
            raise Blocked("RH apresentou validação ao salvar; captura preservada.")
        win32gui.PostMessage(self.form.handle, 0x10, 0, 0)
        time.sleep(1)
        if self.dialogs():
            raise Blocked("RH não concluiu o fechamento; operação requer reconciliação.")
