# Estacionamento: TFrmEstacionamentoViewsMonitoramentoSituacaoVeiculo

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Monitoramento > Veículos no Estacionamento.

- DFM: `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.Situacao.dfm`
- PAS: `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.Situacao.pas`
- Handler de abertura: `actMonVeiculosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEstacionamentoViewsMonitoramentoSituacaoVeiculo | TFrmEstacionamentoViewsMonitoramentoSituacaoVeiculo | outro | Monitoramento \| Veículo no Estacionamento | — | — | — | Visible=True |
| btnAtualizar | TButton | ação | ATUALIZAR | 0 | — | — | — |
| DBCtrlGrid1 | TDBCtrlGrid | grade | — | 1 | — | — | — |
| DBText1 | TDBText | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Placa | — | — | — | — |
| DBText2 | TDBText | outro | — | — | — | — | — |
| Label2 | TLabel | rótulo | Nome | — | — | — | — |
| ImgYesParking | TImage | outro | — | — | — | — | Visible=False |
| imgNoParking | TImage | outro | — | — | — | — | — |
| Panel1 | TPanel | contêiner | — | 0 | — | — | — |
| Panel2 | TPanel | contêiner | — | 1 | — | — | — |
| Panel3 | TPanel | contêiner | — | 2 | — | — | — |
| Panel4 | TPanel | contêiner | — | 3 | — | — | — |
| CdsSituacaoVeiculo | TClientDataSet | outro | — | — | — | — | — |
| CdsSituacaoVeiculoId | TIntegerField | outro | — | — | — | — | — |
| CdsSituacaoVeiculoPlaca | TStringField | outro | — | — | AAA\-AAAA;0;_ | — | — |
| CdsSituacaoVeiculoIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsSituacaoVeiculoNomePessoa | TStringField | outro | — | — | — | — | — |
| CdsSituacaoVeiculoSituacao | TIntegerField | outro | — | — | — | — | — |
| dsSituacaoVeiculo | TDataSource | outro | — | — | — | — | — |
| Timer1 | TTimer | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 121 | `TVeiculosController.Create`, `FVeiculosController.SetConexao` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Nenhum literal simples encontrado.

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
