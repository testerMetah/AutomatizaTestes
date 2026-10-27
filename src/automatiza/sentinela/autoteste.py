"""Autoteste manual do atalho e dos avisos na VM interativa."""
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from automatiza.pausa import TesteCancelado, gravar, ler, ponto


def executar(ns):
    anterior = os.environ.get("AUTOMATIZA_PAUSA_DIR")
    base = Path(anterior) if anterior else Path(tempfile.mkdtemp(prefix="automatiza-pausa-teste-"))
    base.mkdir(parents=True, exist_ok=True)
    os.environ["AUTOMATIZA_PAUSA_DIR"] = str(base)
    gravar(base / "meta.json", {"nome": "Autoteste da sentinela", "perfil": "local",
                                "banco": "sem banco", "pid": os.getpid(),
                                "inicio_monotonico": time.monotonic()})
    gravar(base / "controle.json", {"estado": "RODANDO", "instante": time.time()})
    exe = Path(sys.executable).with_name("pythonw.exe")
    erro = (base / "sentinela-erro.log").open("w", encoding="utf-8")
    proc = subprocess.Popen([str(exe if exe.exists() else sys.executable), "-m",
                             "automatiza.sentinela.runtime", str(base)],
                            stdout=erro, stderr=subprocess.STDOUT,
                            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    erro.close()
    final = "CONCLUIDO"
    try:
        limite = time.monotonic() + 10
        while not (base / "sentinela.json").exists() and time.monotonic() < limite and proc.poll() is None:
            time.sleep(0.03)
        info = ler(base / "sentinela.json")
        print(f"Atalho registrado: {info.get('atalho') or 'nenhum'}; estado: {info.get('estado', 'falhou')}", flush=True)
        if ns.comando == "aviso-teste":
            estado = {"inicio": "CONCLUIDO", "fim": "CONCLUIDO", "cancelado": "CANCELADO"}[ns.tipo]
            if ns.tipo == "inicio":
                time.sleep(1)
            gravar(base / "final.json", {"estado": estado, "resumo": "Exemplo de aviso", "pasta": str(base)})
            time.sleep(2)
            return 0
        print("Aperte o atalho. A detecção aparece aqui. Ctrl+C encerra o autoteste.", flush=True)
        lidos = 0
        while proc.poll() is None:
            try:
                ponto({"acao": "laço falso de autoteste"})
            except TesteCancelado:
                final = "CANCELADO"
                break
            if (base / "eventos.jsonl").exists():
                linhas = (base / "eventos.jsonl").read_text(encoding="utf-8").splitlines()
                for linha in linhas[lidos:]:
                    import json
                    evt = json.loads(linha)
                    print(f"{time.strftime('%H:%M:%S', time.localtime(evt['data_hora']))} {evt['tipo']} {evt.get('latencia_ms', '')} ms", flush=True)
                lidos = len(linhas)
            time.sleep(0.03)
        return 2 if final == "CANCELADO" else 0
    except KeyboardInterrupt:
        return 0
    finally:
        gravar(base / "final.json", {"estado": final, "resumo": "Autoteste encerrado", "pasta": str(base)})
        if anterior is None:
            os.environ.pop("AUTOMATIZA_PAUSA_DIR", None)
        else:
            os.environ["AUTOMATIZA_PAUSA_DIR"] = anterior
