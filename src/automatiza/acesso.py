"""Rotas iniciais observadas no Acessus 2.10.0.

Menus e títulos foram confirmados visualmente. A resolução pelo pywinauto
precisa ser validada ao executar os primeiros testes reais.
"""

SCREENS = {
    "pessoas": ("Cadastros->Pessoas...", "Cadastro de Pessoas"),
    "acesso_por_pessoa": ("Consultas->Acesso por Pessoa...", "Acesso por Pessoa"),
    "reservas_consumos": ("Relatórios->Reservas e Consumos...", "Relatório de Reservas e Consumos"),
}


class Acesso:
    def __init__(self, desktop):
        self.desktop = desktop

    def open_screen(self, name: str):
        if name not in SCREENS:
            raise ValueError(f"Tela desconhecida: {name}. Disponíveis: {', '.join(SCREENS)}")
        if self.desktop.settings.app_backend != "win32":
            raise ValueError("As rotas por menu usam APP_BACKEND=win32.")
        if self.desktop.window is None:
            raise RuntimeError("Conecte ao Módulo de Acesso antes de abrir uma tela.")
        menu, title = SCREENS[name]
        from automatiza.menus import click_uia_menu
        window = self.desktop.window.wrapper_object()
        click_uia_menu(window, menu.split('->'))
        screen = self.desktop.window.child_window(title=title)
        screen.wait("visible enabled", timeout=self.desktop.settings.ui_timeout)
        return screen
