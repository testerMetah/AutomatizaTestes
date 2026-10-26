"""Fixture para dados sintéticos; limpeza sempre executada e banco validado."""
from contextlib import contextmanager
from datetime import datetime
from uuid import uuid4

from automatiza.perfis_teste import validar_escrita


@contextmanager
def dados_sinteticos(settings, criar, limpar):
    """Recebe callbacks da entidade; nenhuma tabela/SQL é presumida aqui.

    `criar(prefixo)` prepara dados e devolve identificadores. `limpar(ids)`
    elimina apenas os dados dessa fixture. Ambos são específicos da entidade.
    """
    validar_escrita(settings)
    prefixo = f"AUTOTEST_{datetime.now():%Y%m%d%H%M%S}_{uuid4().hex[:6]}_"
    identificadores = criar(prefixo)
    try:
        yield identificadores
    finally:
        validar_escrita(settings)
        limpar(identificadores)
