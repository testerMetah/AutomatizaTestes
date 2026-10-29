"""Abre um módulo Acessus via painel, usando apenas credenciais locais do .env."""

from pathlib import Path

from dotenv import dotenv_values
from pywinauto import Application, Desktop
from pywinauto.timings import wait_until_passes


MODULOS = {
    "TFrmPrincipal": "Acesso",
    "TFrmRefeitorioViewsPrincipal": "Refeitório",
    "TFrmEstacionamentoViewsPrincipal": "Estacionamento",
    "TFrmPortariaViewsPrincipal": "Portaria",
    "TFrmEscolaViewsPrincipal": "Escola",
    "TFrmAdministracaoViewsPrincipal": "Administração",
}


def _janela(classe):
    janelas = Desktop(backend="win32").windows(class_name=classe, visible_only=True)
    return janelas[0] if janelas else None


def abrir_modulo(classe_principal, timeout=30):
    modulo = MODULOS.get(classe_principal)
    if not modulo:
        raise RuntimeError(f"Abertura automática sem rota para {classe_principal}")
    existente = _janela(classe_principal)
    if existente:
        return existente

    painel = _janela("TFrmModuloViewsPrincipal")
    login = _janela("TFrmModuloViewsLogin")
    if not painel and not login:
        exe = Path(r"C:\acesso\Acessus.Modulo.exe")
        if not exe.exists():
            raise RuntimeError(f"Painel não encontrado: {exe}")
        Application(backend="win32").start(f'"{exe}"', work_dir=str(exe.parent))
        wait_until_passes(timeout, 0.3, lambda: _janela("TFrmModuloViewsLogin") or _janela("TFrmModuloViewsPrincipal") or (_ for _ in ()).throw(RuntimeError("Aguardando painel")))
        painel = _janela("TFrmModuloViewsPrincipal")
        login = _janela("TFrmModuloViewsLogin")

    if login:
        env = dotenv_values(Path(__file__).parents[2] / ".env")
        usuario, senha = env.get("TESTE_USUARIO"), env.get("TESTE_SENHA")
        if not usuario or not senha:
            raise RuntimeError("Configure TESTE_USUARIO e TESTE_SENHA no .env local")
        campos = sorted([c for c in login.descendants() if c.class_name() == "TEdit" and c.is_visible()],
                        key=lambda c: c.rectangle().top)
        botoes = [c for c in login.descendants() if c.window_text().startswith("Login (")]
        if len(campos) != 2 or len(botoes) != 1:
            raise RuntimeError("Tela de login mudou; remapear antes de continuar")
        campos[0].set_edit_text(usuario)
        campos[1].set_edit_text(senha)
        botoes[0].click_input()
        def autenticado():
            if _janela("TFrmModuloViewsLogin"):
                raise RuntimeError("Aguardando autenticação")
            return _janela("TFrmModuloViewsPrincipal") or (_ for _ in ()).throw(RuntimeError("Aguardando painel"))
        painel = wait_until_passes(timeout, 0.3, autenticado)

    if not painel:
        painel = _janela("TFrmModuloViewsPrincipal")
    if not painel:
        raise RuntimeError("Painel de módulos não está disponível")
    from automatiza.menus import click_uia_menu
    click_uia_menu(painel, ["Modulos", modulo])
    def encontrado():
        janela = _janela(classe_principal)
        if not janela:
            raise RuntimeError(f"Aguardando módulo {modulo}")
        return janela
    return wait_until_passes(timeout, 0.3, encontrado)
