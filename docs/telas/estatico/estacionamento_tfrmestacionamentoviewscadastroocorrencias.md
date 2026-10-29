# Estacionamento: TFrmEstacionamentoViewsCadastroOcorrencias

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Ocorrências.

- DFM: `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Ocorrencias.dfm`
- PAS: `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Ocorrencias.pas`
- Handler de abertura: `actCadOcorrenciasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEstacionamentoViewsCadastroOcorrencias | TFrmEstacionamentoViewsCadastroOcorrencias | outro | Cadastro de Ocorrências | — | — | — | — |
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
| PnlOcorrencia | TPanel | contêiner | — | 1 | — | — | — |
| ImgNomeOcorrencia | TImage | outro | — | — | — | — | — |
| LblOcorrencia | TLabel | rótulo | Nome da Ocorrência: | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DsOcorrencias | TDataSource | outro | — | — | — | — | — |
| CdsOcorrencias | TClientDataSet | outro | — | — | — | — | — |
| CdsOcorrenciasId | TIntegerField | outro | — | — | — | — | — |
| CdsOcorrenciasNome | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 83 | `FOcorrenciasController.Excluir` |
| `ActExibirTudoExecute` | 100 | `FOcorrenciasController.GetOcorrenciasTodos` |
| `ActIncluirExecute` | 118 | — |
| `ActIrExecute` | 124 | `FOcorrenciasController.GetOcorrenciasPorNome` |
| `FormCreate` | 174 | `TOcorrenciasController.Create`, `FOcorrenciasController.SetConexao` |
| `GravaCampos` | 188 | `FOcorrenciasController.Inserir`, `FOcorrenciasController.Atualizar` |
| `ValidarCampos` | 219 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 88: `Excluir o registro?`
- Linha 93: `Problemas com a exclus�o no Banco de Dados!`
- Linha 224: `O Descri��o da ocorr�ncia deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
