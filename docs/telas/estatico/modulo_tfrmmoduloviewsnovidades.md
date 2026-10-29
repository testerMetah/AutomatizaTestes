# Modulo: TFrmModuloViewsNovidades

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ajuda > Novidades.

- DFM: `Modulo/Views/Acessus.Modulo.Views.Novidades.dfm`
- PAS: `Modulo/Views/Acessus.Modulo.Views.Novidades.pas`
- Handler de abertura: `actNovidadesVersoesExecuteExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmModuloViewsNovidades | TFrmModuloViewsNovidades | outro | Novidades | — | — | — | — |
| pnlBottom | TPanel | contêiner | — | 0 | — | — | — |
| BtnFechar | THoverSpeedButton | ação | Fechar (Ctrl+F4) | 0 | — | — | — |
| WBNovidades | TWebBrowser | outro | — | 1 | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActFechar | TAction | ação | Fechar (Ctrl+F4) | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 95 | `TSistemaVersaoController.Create`, `NotasReleaseController.SetConexao`, `NotasReleaseController.GetNotasRelease`, `NotasReleaseController.Free` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Nenhum literal simples encontrado.

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
