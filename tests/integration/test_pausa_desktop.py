"""Teste real da tecla global; rode somente em sessão Windows desbloqueada."""
import ctypes
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

import pytest

from automatiza.pausa import gravar, ler, ponto


@pytest.mark.desktop
def test_pause_break_para_laco_falso(monkeypatch, tmp_path):
    if os.name != "nt":
        pytest.skip("Windows necessário")
    monkeypatch.setenv("AUTOMATIZA_PAUSA_DIR", str(tmp_path))
    gravar(tmp_path / "meta.json", {"nome": "Integração da pausa", "perfil": "teste",
                                   "banco": "sem banco", "pid": os.getpid(),
                                   "inicio_monotonico": time.monotonic()})
    gravar(tmp_path / "controle.json", {"estado": "RODANDO", "instante": time.time()})
    log = (tmp_path / "sentinela-erro.log").open("w", encoding="utf-8")
    proc = subprocess.Popen([sys.executable, "-m", "automatiza.sentinela.runtime", str(tmp_path)],
                            stdout=log, stderr=subprocess.STDOUT)
    log.close()
    try:
        limite = time.monotonic() + 10
        while not (tmp_path / "sentinela.json").exists() and time.monotonic() < limite:
            time.sleep(0.03)
        if ler(tmp_path / "sentinela.json").get("atalho") != "Pause":
            pytest.skip("Pause/Break não disponível nesta sessão")
        parado = threading.Event()
        worker = threading.Thread(target=lambda: (ponto(), parado.set()), daemon=True)
        # INPUT para SendInput no Python 32 bits.
        class KEYBDINPUT(ctypes.Structure):
            _fields_ = [("wVk", ctypes.c_ushort), ("wScan", ctypes.c_ushort),
                        ("dwFlags", ctypes.c_ulong), ("time", ctypes.c_ulong),
                        ("dwExtraInfo", ctypes.c_void_p)]
        class MOUSEINPUT(ctypes.Structure):
            _fields_ = [("dx", ctypes.c_long), ("dy", ctypes.c_long), ("mouseData", ctypes.c_ulong),
                        ("dwFlags", ctypes.c_ulong), ("time", ctypes.c_ulong),
                        ("dwExtraInfo", ctypes.c_void_p)]
        class UNION(ctypes.Union):
            _fields_ = [("ki", KEYBDINPUT), ("mi", MOUSEINPUT)]
        class INPUT(ctypes.Structure):
            _fields_ = [("type", ctypes.c_ulong), ("data", UNION)]
        inicio = time.monotonic()
        for flag in (0, 2):
            data = INPUT(1, UNION(ki=KEYBDINPUT(0x13, 0, flag, 0, None)))
            assert ctypes.windll.user32.SendInput(1, ctypes.byref(data), ctypes.sizeof(data)) == 1
        while ler(tmp_path / "controle.json").get("estado") != "PAUSADO" and time.monotonic() - inicio < 2:
            time.sleep(0.01)
        assert ler(tmp_path / "controle.json").get("estado") == "PAUSADO"
        worker.start()
        assert not parado.wait(0.15)
        assert (time.monotonic() - inicio) < 1.5
        gravar(tmp_path / "pedido.json", {"acao": "continuar", "origem": "teste", "instante": time.time_ns()})
        assert parado.wait(2)
    finally:
        gravar(tmp_path / "final.json", {"estado": "CONCLUIDO", "resumo": "Teste", "pasta": str(tmp_path)})
        proc.terminate()
        proc.wait(timeout=5)


@pytest.mark.desktop
def test_congelamento_segura_processo_principal(tmp_path):
    if os.name != "nt":
        pytest.skip("Windows necessário")
    contador = tmp_path / "contador.txt"
    script = ("import pathlib,time,sys\n"
              "p=pathlib.Path(sys.argv[1]); n=0\n"
              "while True:\n n+=1; p.write_text(str(n)); time.sleep(.02)\n")
    worker = subprocess.Popen([sys.executable, "-c", script, str(contador)])
    gravar(tmp_path / "meta.json", {"nome": "Congelamento", "perfil": "teste",
                                      "banco": "sem banco", "pid": worker.pid,
                                      "inicio_monotonico": time.monotonic()})
    gravar(tmp_path / "controle.json", {"estado": "RODANDO", "instante": time.time()})
    log = (tmp_path / "sentinela-erro.log").open("w", encoding="utf-8")
    sentinela = subprocess.Popen([sys.executable, "-m", "automatiza.sentinela.runtime", str(tmp_path)],
                                stdout=log, stderr=subprocess.STDOUT)
    log.close()
    try:
        limite = time.monotonic() + 5
        while not (tmp_path / "sentinela.json").exists() and time.monotonic() < limite:
            time.sleep(.03)
        assert ler(tmp_path / "sentinela.json").get("estado") == "ATIVA"
        gravar(tmp_path / "pedido.json", {"acao": "pausar", "origem": "teste", "instante": time.time_ns()})
        limite = time.monotonic() + 3
        while time.monotonic() < limite:
            events = (tmp_path / "eventos.jsonl")
            if events.exists() and "Pausado à força" in events.read_text(encoding="utf-8"):
                break
            time.sleep(.03)
        assert "Pausado à força" in (tmp_path / "eventos.jsonl").read_text(encoding="utf-8")
        antes = contador.read_text()
        time.sleep(.2)
        assert contador.read_text() == antes
        gravar(tmp_path / "pedido.json", {"acao": "continuar", "origem": "teste", "instante": time.time_ns()})
        limite = time.monotonic() + 2
        while contador.read_text() == antes and time.monotonic() < limite:
            time.sleep(.03)
        assert contador.read_text() != antes
    finally:
        gravar(tmp_path / "pedido.json", {"acao": "continuar", "origem": "teste", "instante": time.time_ns()})
        time.sleep(.1)
        worker.terminate()
        worker.wait(timeout=5)
        sentinela.terminate()
        sentinela.wait(timeout=5)
