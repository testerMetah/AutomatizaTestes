"""Protocolo local de pausa entre a CLI, os testes e a sentinela."""
import json
import os
import tempfile
import time
from pathlib import Path

from automatiza.config import ROOT

ESTADOS = {"PREPARANDO", "RODANDO", "PAUSADO", "CANCELANDO", "CONCLUIDO", "FALHOU", "CANCELADO"}
ATALHOS_PERMITIDOS = {"Pause", "Ctrl+Shift+F9", "Ctrl+Shift+P"}


class TesteCancelado(BaseException):
    """Cancelamento pedido pelo usuário num ponto seguro."""
    __test__ = False


def configuracao():
    path = ROOT / "config/notificacoes.json"
    cfg = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(cfg.get("avisos"), bool) or not isinstance(cfg.get("congelamento"), bool):
        raise ValueError("Configuração de avisos inválida.")
    for key in ("inicio_segundos", "fim_segundos"):
        if not 1 <= float(cfg[key]) <= 60:
            raise ValueError(f"Duração inválida: {key}.")
    if not cfg.get("atalhos") or any(x not in ATALHOS_PERMITIDOS for x in cfg["atalhos"]):
        raise ValueError("Atalho inválido; use Pause, Ctrl+Shift+F9 ou Ctrl+Shift+P.")
    return cfg


def gravar(path, value):
    """Substituição atômica para não expor JSON pela metade."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False)
            stream.flush()
            os.fsync(stream.fileno())
        for tentativa in range(30):
            try:
                os.replace(tmp, path)
                break
            except PermissionError:
                if tentativa == 29:
                    raise
                time.sleep(0.005)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def ler(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def pasta():
    value = os.environ.get("AUTOMATIZA_PAUSA_DIR")
    return Path(value) if value else None


def comando(acao, origem="painel"):
    base = pasta()
    if base is None:
        raise RuntimeError("Nenhum teste pausável nesta execução.")
    if acao not in {"pausar", "continuar", "cancelar"}:
        raise ValueError("Comando de pausa inválido.")
    gravar(base / "pedido.json", {"acao": acao, "origem": origem, "instante": time.time_ns()})


def ponto(contexto=None):
    """Bloqueia antes da próxima ação. Não interrompe uma ação já começada."""
    base = pasta()
    if base is None:
        return
    visto = None
    while True:
        pedido = ler(base / "controle.json")
        estado = pedido.get("estado", "RODANDO")
        if estado in {"CANCELANDO", "CANCELADO"}:
            gravar(base / "confirmacao.json", {"estado": "CANCELADO", "instante": time.time(), "contexto": contexto or {}})
            raise TesteCancelado("Cancelado pelo usuário")
        if estado != "PAUSADO":
            if visto == "PAUSADO":
                if os.name == "nt" and pedido.get("janela_anterior"):
                    import ctypes
                    hwnd = int(pedido["janela_anterior"])
                    if not ctypes.windll.user32.IsWindow(hwnd):
                        raise RuntimeError("estado alterado durante a pausa: janela original fechada")
                    ctypes.windll.user32.SetForegroundWindow(hwnd)
                gravar(base / "confirmacao.json", {"estado": "RODANDO", "instante": time.time(), "contexto": contexto or {}})
            return
        heartbeat = ler(base / "heartbeat.json").get("instante", 0)
        if time.time() - heartbeat > 2:
            return  # Falha da sentinela: o teste segue sem pausa.
        if visto != "PAUSADO":
            gravar(base / "confirmacao.json", {"estado": "PAUSADO", "instante": time.time(), "contexto": contexto or {}})
            visto = "PAUSADO"
        time.sleep(0.03)


def esperar(condicao, timeout, intervalo=0.1):
    """Espera por condição sem consumir o timeout enquanto há pausa."""
    from pywinauto.timings import TimeoutError as WaitTimeoutError
    relogio = RelogioAtivo()
    while relogio.decorrido() < timeout:
        base = pasta()
        relogio.sincronizar(bool(base and ler(base / "controle.json").get("estado") == "PAUSADO"))
        ponto()
        relogio.sincronizar(False)
        if condicao():
            return True
        time.sleep(min(intervalo, max(0, timeout - relogio.decorrido())))
    raise WaitTimeoutError("Condição não apareceu antes do limite de espera.")


class RelogioAtivo:
    """Tempo decorrido que ignora períodos em pausa."""

    def __init__(self):
        self.inicio = time.monotonic()
        self.pausa_inicio = None
        self.pausado = 0.0

    def decorrido(self):
        agora = time.monotonic()
        pausa = self.pausado + ((agora - self.pausa_inicio) if self.pausa_inicio else 0)
        return agora - self.inicio - pausa

    def sincronizar(self, esta_pausado):
        agora = time.monotonic()
        if esta_pausado and self.pausa_inicio is None:
            self.pausa_inicio = agora
        elif not esta_pausado and self.pausa_inicio is not None:
            self.pausado += agora - self.pausa_inicio
            self.pausa_inicio = None


def tecla_reservada(value, atalhos=None):
    """Recusa o gesto completo; não tenta interpretar texto digitado comum."""
    at = atalhos or configuracao()["atalhos"]
    norm = str(value).upper().replace(" ", "")
    formas = {"Pause": {"{PAUSE}", "{BREAK}"},
              "Ctrl+Shift+F9": {"^+{F9}", "+^{F9}"},
              "Ctrl+Shift+P": {"^+P", "+^P"}}
    return any(norm in formas[name] for name in at)
