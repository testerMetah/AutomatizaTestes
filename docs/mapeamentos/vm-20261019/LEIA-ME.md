# Inspeção real dos módulos na VM

Sessão: vm-20261019

Uma tela é aberta, inspecionada e salva antes da próxima. Sem gravação de dados de negócio.

| Módulo | Rotas previstas | Inspecionadas | Outras situações |
|---|---:|---:|---:|
| [Acesso](acesso.md) | 42 | 21 | 21 |
| [Refeitório](refeitorio.md) | 21 | 20 | 1 |
| [Portaria](portaria.md) | 13 | 12 | 1 |
| [Estacionamento](estacionamento.md) | 20 | 19 | 1 |
| [Escola](escola.md) | 26 | 26 | 0 |
| [Administração](administracao.md) | 3 | 2 | 1 |

## Material para reutilizar

- [Catálogo de telas e cobertura](catalogo-telas.json).
- [Rotas, janelas e botões candidatos para código](rotas-para-codigo.json).
- [Painel de Módulos](../../../reports/inspecao-telas/vm-20261019/painel-corrigido.md).

Cada mapa registra a captura real e a referência estática separadamente. Valores de dados são omitidos.
Nomes Delphi não são automation_id. Handles e IDs de sessão não são seletores permanentes.

As rotas indisponíveis ou não acionadas permanecem identificadas no catálogo; não são aprovações.

Totais desta sessão:

```json
{
  "rotas_previstas": 125,
  "situacoes": {
    "INSPECIONADA": 100,
    "FALHA_INSPECAO": 1,
    "PENDENTE": 20,
    "NAO_ACIONADA": 3,
    "INDISPONIVEL_NO_MENU": 1
  },
  "variacoes_abas": 133,
  "inclusoes_canceladas": 34,
  "mapas_markdown": 285
}
```
