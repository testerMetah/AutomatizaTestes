"""Dois diários centrais, persistentes e sincronizados para testes de auditoria."""

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


class DiarioAuditorias:
    """Acrescenta cada ação ao log legível e ao JSONL detalhado.

    Os arquivos ficam na raiz de ``resultados`` e nunca são abertos em modo de
    substituição. O identificador da execução e a sequência ligam todos os
    eventos, mesmo quando várias rodadas usam os mesmos arquivos.
    """

    def __init__(self, pasta_resultados, contexto):
        self.pasta = Path(pasta_resultados)
        self.contexto = dict(contexto)
        self.execucao_id = f"{datetime.now():%Y%m%d-%H%M%S}-{uuid4().hex[:8]}"
        self.sequencia = 0
        self.inicio_monotonico = time.perf_counter()
        self.tentativa_atual = None
        self._inicio_tentativa = None
        self.contagem_status = {}
        self._passos = None
        self._detalhado = None

    def __enter__(self):
        self.pasta.mkdir(parents=True, exist_ok=True)
        self._passos = (self.pasta / "passo-a-passo.log").open(
            "a", encoding="utf-8", buffering=1)
        try:
            self._detalhado = (self.pasta / "passo-a-passo-detalhado.jsonl").open(
                "a", encoding="utf-8", buffering=1)
        except BaseException:
            self._passos.close()
            raise
        return self

    def __exit__(self, exc_type, exc, traceback):
        try:
            self._json({
                "tipo": "fim_execucao",
                "situacao": "FALHOU" if exc_type else "CONCLUIDA",
                "erro": f"{exc_type.__name__}: {exc}" if exc_type else None,
                "resultados": self.contagem_status,
            })
        finally:
            self._detalhado.close()
            self._passos.close()

    def _base(self):
        agora = datetime.now().astimezone()
        self.sequencia += 1
        return {
            "versao_formato": 1,
            "execucao_id": self.execucao_id,
            "evento_id": f"{self.execucao_id}-{self.sequencia:07d}",
            "sequencia_execucao": self.sequencia,
            "data_hora_local": agora.isoformat(timespec="milliseconds"),
            "data_hora_utc": agora.astimezone(timezone.utc).isoformat(timespec="milliseconds"),
            "decorrido_ms": round((time.perf_counter() - self.inicio_monotonico) * 1000, 3),
            "contexto_execucao": self.contexto,
        }, agora

    def _json(self, campos):
        base, _ = self._base()
        base.update(campos)
        self._detalhado.write(json.dumps(base, ensure_ascii=False, default=str) + "\n")
        self._detalhado.flush()
        os.fsync(self._detalhado.fileno())
        return base

    def acao(self, modulo, historico, filtro, descricao, *, detalhes=None):
        base, agora = self._base()
        linha = (f"[{agora:%d/%m/%Y - %H:%M:%S}] "
                 f"Tela: Auditorias/Históricos | Módulo: {modulo} | "
                 f"Histórico: {historico} | Filtro: {filtro} | {descricao}")
        base.update({
            "tipo": "acao", "tela": "Auditorias/Históricos",
            "modulo": modulo, "historico": historico, "filtro": filtro,
            "descricao": descricao, "linha_passo_a_passo": linha,
            "tentativa": dict(self.tentativa_atual) if self.tentativa_atual else None,
            "detalhes": detalhes or {},
        })
        self._passos.write(linha + "\n")
        self._passos.flush()
        os.fsync(self._passos.fileno())
        self._detalhado.write(json.dumps(base, ensure_ascii=False, default=str) + "\n")
        self._detalhado.flush()
        os.fsync(self._detalhado.fileno())
        return base

    def iniciar_tentativa(self, registro):
        registro["execucao_id"] = self.execucao_id
        registro["tentativa_id"] = f"{self.execucao_id}-T{uuid4().hex[:10]}"
        self.tentativa_atual = registro
        self._inicio_tentativa = time.perf_counter()

    def finalizar_tentativa(self, registro):
        registro["fim"] = datetime.now().astimezone().isoformat(timespec="milliseconds")
        registro["duracao_ms"] = round((time.perf_counter() - self._inicio_tentativa) * 1000, 3)
        status = registro.get("status", "SEM_STATUS")
        self.contagem_status[status] = self.contagem_status.get(status, 0) + 1
        self._json({"tipo": "tentativa_finalizada", "tentativa_id": registro["tentativa_id"],
                    "registro_completo": dict(registro)})
        self.tentativa_atual = None
        self._inicio_tentativa = None
