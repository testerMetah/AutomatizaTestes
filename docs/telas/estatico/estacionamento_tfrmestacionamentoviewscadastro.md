# Estacionamento: TFrmEstacionamentoViewsCadastro

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Estacionamento.

- DFM: `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.dfm`
- PAS: `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.pas`
- Handler de abertura: `actCadEstacionamentoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEstacionamentoViewsCadastro | TFrmEstacionamentoViewsCadastro | outro | Cadastro de Estacionamento | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| PnlComponentes | TPanel | contêiner | — | 1 | — | — | — |
| ImgNomeEstacionamento | TImage | outro | — | — | — | — | — |
| ImgQuantidadeVagas | TImage | outro | — | — | — | — | — |
| LblNomeEstacionamento | TLabel | rótulo | Nome do Estacionamento: | — | — | — | — |
| LblQuantidadeVagas | TLabel | rótulo | Quantidade de Vagas: | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | 100 | — |
| EdQuantidade | TSpinEdit | campo de texto/data | — | 1 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DsEstacionamento | TDataSource | outro | — | — | — | — | — |
| CdsEstacionamento | TClientDataSet | outro | — | — | — | — | — |
| CdsEstacionamentoId | TIntegerField | outro | — | — | — | — | — |
| CdsEstacionamentoNome | TStringField | outro | — | — | — | — | — |
| CdsEstacionamentoQuantidade | TIntegerField | outro | — | — | — | — | — |
| CdsEstacionamentoUsado | TIntegerField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 87 | `FEstacionamentoController.Excluir` |
| `ActExibirTudoExecute` | 104 | `FEstacionamentoController.GetEstacionamentoTodos` |
| `ActIncluirExecute` | 123 | — |
| `ActIrExecute` | 129 | `FEstacionamentoController.GetEstacionamentoPorNome` |
| `FormCreate` | 179 | `TEstacionamentoController.Create`, `FEstacionamentoController.SetConexao` |
| `GravaCampos` | 194 | `FEstacionamentoController.Inserir`, `FEstacionamentoController.Atualizar` |
| `ValidarCampos` | 231 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 92: `Excluir o registro?`
- Linha 97: `Problemas com a exclus�o no Banco de Dados!`
- Linha 236: `O Descri��o do estacionamento deve ser informada.`
- Linha 243: `A Quantidade deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
