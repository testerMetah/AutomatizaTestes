# Estacionamento: TFrmEstacionamentoViewsMonitoramentoGraficoOcupacaoVagas

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Monitoramento > Gráfico do Estacionamento.

- DFM: `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.GraficoOcupacaoVagas.dfm`
- PAS: `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.GraficoOcupacaoVagas.pas`
- Handler de abertura: `actMonGraficoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEstacionamentoViewsMonitoramentoGraficoOcupacaoVagas | TFrmEstacionamentoViewsMonitoramentoGraficoOcupacaoVagas | outro | Monitoramento \| Grafico de Ocupação de Vagas | — | — | — | Visible=True |
| WebBrowser | TWebBrowser | outro | — | 0 | — | — | — |
| CdsEstacionamento | TClientDataSet | outro | — | — | — | — | — |
| CdsEstacionamentoId | TIntegerField | outro | — | — | — | — | — |
| CdsEstacionamentoNome | TStringField | outro | — | — | — | — | — |
| CdsEstacionamentoQuantidade | TIntegerField | outro | — | — | — | — | — |
| CdsEstacionamentoUsada | TIntegerField | outro | — | — | — | — | — |
| DataSource1 | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 73 | `TEstacionamentoController.Create`, `FEstacionamentoController.SetConexao` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Nenhum literal simples encontrado.

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
