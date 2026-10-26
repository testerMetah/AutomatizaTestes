"""Seletores da instalação Delphi observada; remapear por build quando necessário."""
MODULOS = {
    "acesso": ("Acessus.exe", "Acesso"),
    "refeitorio": ("Acessus.Refeitorio.exe", "Refeit"),
    "portaria": ("Acessus.Portaria.exe", "Portaria"),
    "estacionamento": ("Acessus.Estacionamento.exe", "Estacionamento"),
    "escola": ("Acessus.Escola.exe", "Escola"),
    "administracao": ("Acessus.Administracao.exe", "Administra"),
}
PAINEL = "Acessus.Modulo.exe"
CLASSE_PAINEL = "TFrmModuloViewsPrincipal"
CLASSE_LOGIN = "TFrmModuloViewsLogin"
CLASSE_JANELA_PRINCIPAL = "Principal"
CLASSE_AUDITORIA = "AuditoriaHistorico"
MENU_MODULOS = "Modulos"
MENU_CONSULTAS = "Consultas"
MENU_AUDITORIAS = "Auditorias/Hist"
BOTAO_LOGIN = "Login (Enter)"
