"""Ciclo de vida de uma rodada da CLI."""
import json
import os
import sys
from collections import Counter
from pathlib import Path

from automatiza import caminhos
from automatiza.log import mascarar
from automatiza.organizacao import iniciar, finalizar


def _linhas(path):
    if not path.exists():
        return 0
    with path.open("rb") as stream:
        return sum(bloco.count(b"\n") for bloco in iter(lambda: stream.read(1024 * 1024), b""))


class _Duplo:
    def __init__(self, stream, arquivo):
        self.stream, self.arquivo = stream, arquivo
        self.encoding = getattr(stream, "encoding", "utf-8")

    def write(self, mensagem):
        limpa = mascarar(str(mensagem))
        self.stream.write(limpa)
        self.arquivo.write(limpa)
        self.arquivo.flush()
        return len(mensagem)

    def flush(self):
        self.stream.flush()
        self.arquivo.flush()

    def isatty(self):
        return self.stream.isatty()


class Rodada:
    def __init__(self, comando, alvo, perfil, banco, servidor=None, opcoes=None, executavel=None):
        caminhos.preparar()
        self.pasta = caminhos.nova_rodada(comando, alvo)
        self.anterior = {k: os.environ.get(k) for k in ("AUTOMATIZA_RODADA_DIR", "AUTOMATIZA_EXECUCAO_ID")}
        os.environ["AUTOMATIZA_RODADA_DIR"] = str(self.pasta)
        os.environ["AUTOMATIZA_EXECUCAO_ID"] = self.pasta.name
        self.log = caminhos.logs_permanentes() / "passo-a-passo-detalhado.jsonl"
        self.linha_inicial = _linhas(self.log) + 1
        iniciar(self.pasta, comando, alvo, perfil=perfil, banco_efetivo=banco, servidor=servidor,
                opcoes=opcoes or {}, caminho_executavel=executavel,
                comando_cli_equivalente="automatiza " + comando)
        self.arquivo = (self.pasta / "saida-console.txt").open("a", encoding="utf-8")
        self.stdout, self.stderr = sys.stdout, sys.stderr

    def __enter__(self):
        sys.stdout = _Duplo(self.stdout, self.arquivo)
        sys.stderr = _Duplo(self.stderr, self.arquivo)
        return self

    def __exit__(self, kind, erro, tb):
        sys.stdout, sys.stderr = self.stdout, self.stderr
        self.arquivo.close()
        for nome, valor in self.anterior.items():
            if valor is None:
                os.environ.pop(nome, None)
            else:
                os.environ[nome] = valor

    def concluir(self, estado, pausas=None):
        totais = Counter()
        for path in self.pasta.rglob("tentativas.jsonl"):
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    record = json.loads(line)
                    totais[record.get("status") or record.get("estado") or "DESCONHECIDO"] += 1
                except ValueError:
                    continue
        final = _linhas(self.log)
        trecho = {"arquivo": "logs-permanentes/passo-a-passo-detalhado.jsonl",
                  "linha_inicial": self.linha_inicial, "linha_final": final}
        from automatiza.organizacao import carregar
        links = carregar(self.pasta)["links_relativos"]
        links["log_permanente_trecho"] = trecho
        finalizar(self.pasta, estado, dict(totais), links_relativos=links, pausas=pausas or {"quantidade": 0, "tempo_total_s": 0})
