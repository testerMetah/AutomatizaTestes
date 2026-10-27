"""Executa uma varredura variada, serial e somente de leitura."""
import html
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime

from automatiza import caminhos
from automatiza.organizacao import atualizar, finalizar, indice, iniciar
from automatiza.pausa import gravar, ler


ETAPAS = (
    ("ambiente-auditorias", ("ambiente", "--perfil", "auditorias")),
    ("ambiente-sequencias", ("ambiente", "--perfil", "sequencias")),
    ("unitarios", ("testes-unitarios",)),
    ("sequencia-leitura", ("sequencias", "--arquivo", "tests/sequencias/checagem_leitura.yaml")),
    ("robot-smoke", ("robot", "--tag", "smoke")),
    ("sequencia-seed-4242", ("sequencias", "--seed", "4242", "--passos", "12", "--massa", "5")),
    ("sequencia-seed-20261027", ("sequencias", "--seed", "20261027", "--passos", "12", "--massa", "5")),
    ("auditorias-todos-extremo", ("auditorias", "--modulo", "todos", "--perfil", "auditorias", "--extremo")),
)


def plano():
    return [{"nome": nome, "comando": ["automatiza", *args], "estado": "PENDENTE"}
            for nome, args in ETAPAS]


def _relatorio(pasta, etapas):
    linhas = ["<!doctype html><html lang='pt-BR'><meta charset='utf-8'>",
             "<title>Varredura ampla</title><h1>Varredura ampla</h1>",
             "<p>Etapas em sequência; todas de leitura. Abra o log de cada etapa para ações e erros.</p>",
             "<table border='1' cellpadding='6'><tr><th>Etapa</th><th>Estado</th><th>Início</th><th>Fim</th><th>Log</th><th>Rodadas geradas</th></tr>"]
    for etapa in etapas:
        nome = html.escape(etapa["nome"])
        log = f"etapas/{nome}.log"
        rodadas = "<br>".join(
            f"<a href='../{html.escape(ident)}/RELATORIO.html'>{html.escape(ident)}</a>"
            for ident in etapa.get("rodadas", [])) or "—"
        linhas.append("<tr><td>" + nome + "<br><code>" + html.escape(" ".join(etapa["comando"]))
                     + "</code></td><td>" + html.escape(etapa["estado"])
                     + "</td><td>" + html.escape(etapa.get("inicio") or "—")
                     + "</td><td>" + html.escape(etapa.get("fim") or "—")
                     + f"</td><td><a href='{log}'>Abrir log</a></td><td>{rodadas}</td></tr>")
    linhas.append("</table></html>")
    (pasta / "RELATORIO.html").write_text("\n".join(linhas), encoding="utf-8")


def _salvar(pasta, etapas):
    gravar(pasta / "resumo.json", {"etapas": etapas, "atualizado_em": datetime.now().astimezone().isoformat()})
    _relatorio(pasta, etapas)
    indice()


def _validar_destinos():
    from automatiza.database import SqlServer
    from automatiza.perfis_teste import carregar, configuracao

    for nome in ("auditorias", "sequencias"):
        perfil = carregar(nome)
        if not perfil.get("confirmado_como_teste"):
            raise RuntimeError(f"Perfil {nome} não confirmado como teste")
        efetivo = SqlServer(configuracao(nome)).assert_database()
        if efetivo.casefold() != perfil["banco"].casefold():
            raise RuntimeError(f"Banco divergente no perfil {nome}: {efetivo}")


def executar():
    ident = os.environ.get("AUTOMATIZA_VARREDURA_ID")
    if ident:
        if not re.fullmatch(r"\d{8}-\d{6}-varredura-ampla", ident):
            raise ValueError("ID da varredura inválido")
        pasta = caminhos.rodadas() / ident
        pasta.mkdir(parents=True, exist_ok=False)
    else:
        pasta = caminhos.nova_rodada("varredura", "ampla")
    iniciar(pasta, "varredura", "ampla", comando_cli_equivalente="automatiza.varredura_ampla",
            observacoes="Leitura; etapas serializadas; cancelamento interrompe as próximas etapas.")
    (pasta / "etapas").mkdir()
    etapas = plano()
    _salvar(pasta, etapas)
    try:
        _validar_destinos()
        for etapa, (_, args) in zip(etapas, ETAPAS):
            etapa["estado"] = "RODANDO"
            etapa["inicio"] = datetime.now().astimezone().isoformat(timespec="seconds")
            _salvar(pasta, etapas)
            anteriores = {p.name for p in caminhos.rodadas().iterdir() if p.is_dir()}
            log = pasta / "etapas" / (etapa["nome"] + ".log")
            controle = pasta / "controle" / etapa["nome"]
            controle.mkdir(parents=True)
            ambiente = os.environ.copy()
            ambiente["AUTOMATIZA_PAUSA_DIR"] = str(controle)
            inicio = time.monotonic()
            with log.open("w", encoding="utf-8") as out:
                out.write("Comando: " + " ".join(etapa["comando"]) + "\n")
                out.write("Início: " + etapa["inicio"] + "\n\n")
                out.flush()
                proc = subprocess.Popen([sys.executable, "-u", "-m", "automatiza.nova_cli", *args],
                                        cwd=caminhos.raiz(), env=ambiente,
                                        stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT)
                etapa["pid"] = proc.pid
                _salvar(pasta, etapas)
                codigo = proc.wait()
                out.write(f"\nFim: {datetime.now().astimezone().isoformat(timespec='seconds')}\nCódigo: {codigo}\n")
            etapa["codigo"] = codigo
            etapa["fim"] = datetime.now().astimezone().isoformat(timespec="seconds")
            etapa["duracao_s"] = round(time.monotonic() - inicio, 2)
            etapa["rodadas"] = sorted(p.name for p in caminhos.rodadas().iterdir()
                                       if p.is_dir() and p.name not in anteriores)
            cancelado = ler(controle / "controle.json").get("estado") == "CANCELANDO"
            etapa["estado"] = "CANCELADO" if cancelado else ("CONCLUIDO" if codigo == 0 else "FALHOU")
            _salvar(pasta, etapas)
            if cancelado:
                break
        status = "CANCELADO" if any(e["estado"] == "CANCELADO" for e in etapas) else (
            "FALHOU" if any(e["estado"] == "FALHOU" for e in etapas) else "CONCLUIDO")
        finalizar(pasta, status, {e["estado"]: sum(x["estado"] == e["estado"] for x in etapas)
                                   for e in etapas})
        return 2 if status == "CANCELADO" else (1 if status == "FALHOU" else 0)
    except BaseException as exc:
        (pasta / "ERRO.txt").write_text(f"{type(exc).__name__}: {exc}\n", encoding="utf-8")
        finalizar(pasta, "FALHOU", {"falha_preparacao": 1})
        raise


if __name__ == "__main__":
    raise SystemExit(executar())
