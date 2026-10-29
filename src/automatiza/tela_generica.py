"""Tela MDI descrita por YAML. Seletores só podem agir após validação na UI."""

from __future__ import annotations

from pathlib import Path
import yaml


class FalhaTeste(RuntimeError):
    """Automação ou ambiente indisponível."""


class FalhaSistema(AssertionError):
    """Comportamento observado diverge do esperado."""


class TelaGenerica:
    def __init__(self, nome: str, pasta_mapas: Path | None = None):
        pasta = pasta_mapas or Path(__file__).parent / "mapas"
        caminho = pasta / f"{nome}.yaml"
        if not caminho.is_file():
            raise FalhaTeste(f"Mapa ausente: {caminho}")
        self.mapa = yaml.safe_load(caminho.read_text(encoding="utf-8"))
        self.nome = nome
        self.janela = None

    def _desktop(self, backend=None):
        from pywinauto import Desktop
        return Desktop(backend=backend or self.mapa.get("backend", "win32"))

    def _principal(self, auto_start=False):
        classe = self.mapa.get("principal_class", "TFrmPrincipal")
        janelas = self._desktop().windows(class_name=classe, visible_only=True)
        if not janelas:
            if auto_start:
                from automatiza.abertura_modulo import abrir_modulo
                return abrir_modulo(classe)
            raise FalhaTeste(f"{classe} ausente; abra o módulo e autentique-se.")
        return janelas[0]

    def _esperar_form(self, timeout=15):
        principal = self._principal()
        from pywinauto.timings import wait_until_passes

        def localizar():
            for janela in principal.descendants():
                if janela.class_name() == self.mapa["form_class"] and janela.is_visible():
                    # Delphi pode recriar o handle logo após criar a filha MDI.
                    janela.set_focus()
                    return janela
            raise FalhaTeste(f"Aguardando {self.mapa['form_class']}")

        try:
            self.janela = wait_until_passes(timeout, 0.2, localizar)
            return self.janela
        except Exception as exc:
            raise FalhaTeste(f"Timeout aguardando {self.mapa['form_class']}: {type(exc).__name__}: {exc}") from exc

    def abrir(self):
        if not self.mapa.get("validado_na_ui"):
            raise FalhaTeste(f"Mapa {self.nome} ainda não validado na UI; execução bloqueada.")
        from automatiza.menus import click_uia_menu
        principal = self._principal(auto_start=True)
        for janela in principal.descendants():
            if janela.class_name() == self.mapa["form_class"] and janela.is_visible():
                return self._esperar_form()
        click_uia_menu(principal, self.mapa["menu"])
        return self._esperar_form()

    def _controle(self, nome):
        # MDI VCL pode recriar o HWND durante a ativação; não reutilizar handle antigo.
        self._esperar_form()
        spec = self.mapa["controles"].get(nome)
        if spec is None:
            raise FalhaTeste(f"Controle lógico inexistente: {self.nome}.{nome}")
        if not self.mapa.get("validado_na_ui"):
            raise FalhaTeste(f"Mapa {self.nome} ainda não validado na UI")
        validados = self.mapa.get("controles_validados")
        if validados is not None and nome not in validados:
            raise FalhaTeste(f"Controle {self.nome}.{nome} ainda não validado na UI")
        backend = spec.get("backend", self.mapa.get("backend", "win32"))
        janela = self._desktop(backend).window(handle=self.janela.handle)
        filtro = {k: spec[k] for k in ("class_name", "auto_id", "title") if spec.get(k) is not None}
        if not filtro:
            raise FalhaTeste(f"Controle {nome} sem seletor")
        try:
            candidatos = janela.wrapper_object().descendants(**filtro)
            indice = spec.get("found_index")
            if indice is None and len(candidatos) != 1:
                raise FalhaTeste(f"Seletor ambíguo: {nome}, {len(candidatos)} controles; valide found_index na UI")
            if indice is not None and not 0 <= indice < len(candidatos):
                raise FalhaTeste(f"found_index={indice} fora da faixa em {nome}; {len(candidatos)} controles")
            alvo = candidatos[indice if indice is not None else 0]
            if not alvo.is_visible() or not alvo.is_enabled():
                raise FalhaTeste(f"Controle {nome} invisível ou desabilitado")
            return alvo
        except Exception as exc:
            raise FalhaTeste(f"Controle {self.nome}.{nome} não encontrado: {exc}") from exc

    def _popups(self):
        principal = self._principal()
        return [w for w in self._desktop().windows(process=principal.process_id())
                if w.class_name() in {"#32770", "TMessageForm"} and w.is_visible()]

    def _sem_popup(self):
        popups = self._popups()
        if popups:
            raise FalhaTeste(f"Popup inesperado antes da ação: {self.ler_mensagem()}")

    def preencher(self, campo, valor):
        self._sem_popup()
        self._controle(campo).set_edit_text(str(valor))

    def clicar(self, botao):
        self._sem_popup()
        self._controle(botao).click_input()

    def teclar(self, teclas):
        self._sem_popup()
        if self.janela is None:
            self._esperar_form()
        self.janela.type_keys(str(teclas), set_foreground=True)

    def ler_mensagem(self):
        return [" | ".join([w.window_text()] + [x.window_text() for x in w.descendants()
                                              if x.window_text() and x.class_name() not in {"Button", "THoverSpeedButton"}])
                for w in self._popups()]

    def fechar_popup(self):
        for popup in self._popups():
            botoes = [x for x in popup.descendants() if x.class_name() in {"Button", "THoverSpeedButton"}
                      and (x.window_text().strip().upper() in {"OK", "FECHAR", "CANCELAR", "&OK"})]
            if len(botoes) != 1:
                raise FalhaTeste(f"Popup sem botão de fechamento inequívoco: {self.ler_mensagem()}")
            botoes[0].click_input()

    def ler_grid(self, nome="grid"):
        return self._controle(nome).texts()

    def fechar(self):
        principal = self._principal()
        for janela in principal.descendants():
            if janela.class_name() == self.mapa["form_class"] and janela.is_visible():
                janela.close()
                break
