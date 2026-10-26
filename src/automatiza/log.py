"""Mensagens de execução sem credenciais."""
import json
import os
import re
from datetime import datetime


_CREDENCIAL = re.compile(r"(?i)\b(password|pwd|senha|token|secret)\s*[:=]\s*([^\s;,}]+)")
_CONEXAO = re.compile(r"(?i)(?:driver|server|database|uid|pwd)\s*=.*?(?:;|$)")


def mascarar(valor):
    if isinstance(valor, dict):
        return {k: ("[oculto]" if re.search(r"(?i)senha|password|pwd|token|secret|connection_string|usuario_windows", k)
                    else mascarar(v)) for k, v in valor.items()}
    if isinstance(valor, list):
        return [mascarar(x) for x in valor]
    if not isinstance(valor, str):
        return valor
    for chave in ("TESTE_SENHA", "SQL_PASSWORD", "RH_PASSWORD"):
        segredo = os.environ.get(chave)
        if segredo:
            valor = valor.replace(segredo, "[oculto]")
    valor = _CREDENCIAL.sub(lambda m: m.group(1) + "=[oculto]", valor)
    return _CONEXAO.sub("[conexão ocultada]", valor)


def linha(nivel, componente, execucao_id, mensagem):
    instante = datetime.now().astimezone().isoformat(timespec="milliseconds")
    return f"{instante} {nivel.upper()} {componente} {execucao_id or '-'} {mascarar(str(mensagem))}"


def json_seguro(valor):
    return json.dumps(mascarar(valor), ensure_ascii=False, indent=2, default=str)
