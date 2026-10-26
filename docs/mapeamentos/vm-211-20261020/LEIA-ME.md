# Inspeção real dos módulos na VM

Sessão: vm-211-20261020

Uma tela é aberta, inspecionada e salva antes da próxima. Sem gravação de dados de negócio.

| Módulo | Rotas previstas | Inspecionadas | Outras situações |
|---|---:|---:|---:|
| [Acesso](acesso.md) | 42 | 23 | 19 |
| [Refeitório](refeitorio.md) | 21 | 4 | 17 |
| [Portaria](portaria.md) | 13 | 0 | 13 |
| [Estacionamento](estacionamento.md) | 20 | 2 | 18 |
| [Escola](escola.md) | 26 | 2 | 24 |
| [Administração](administracao.md) | 3 | 1 | 2 |

## Material para reutilizar

- [Catálogo de telas e cobertura](catalogo-telas.json).
- [Rotas, janelas e botões candidatos para código](rotas-para-codigo.json).
- [Painel de Módulos](../../../reports/inspecao-telas/vm-211-20261020/painel-corrigido.md).

Cada mapa registra a captura real e a referência estática separadamente. Valores de dados são omitidos.
Nomes Delphi não são automation_id. Handles e IDs de sessão não são seletores permanentes.

As rotas indisponíveis ou não acionadas permanecem identificadas no catálogo; não são aprovações.

Totais desta sessão:

```json
{
  "rotas_previstas": 125,
  "situacoes": {
    "PENDENTE": 90,
    "INSPECIONADA": 32,
    "NAO_ACIONADA": 1,
    "DIALOGO_OBSERVADO": 1,
    "INDISPONIVEL_NO_MENU": 1
  },
  "variacoes_abas": 50,
  "inclusoes_canceladas": 9,
  "mapas_markdown": 110
}
```
