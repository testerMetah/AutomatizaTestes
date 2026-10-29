# Acesso: TFrmMensagemColetores

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Coletores > Mensagens dos Coletores....

- DFM: `Acesso/uFrmCadMensagemColetores.dfm`
- PAS: `Acesso/uFrmCadMensagemColetores.pas`
- Handler de abertura: `acCadMensagemColetoresExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmMensagemColetores | TFrmMensagemColetores | outro | Mensagem dos Coletores | — | — | — | — |
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
| GbPeriodo | TGroupBox | contêiner |            Mensagem | 1 | — | — | — |
| ImgMensagem | TImage | outro | — | — | — | — | — |
| EdMensagem | TEdit | campo de texto/data | — | 0 | — | — | Text=EdMensagem |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DsMensagemColetores | TDataSource | outro | — | — | — | — | — |
| CdsMensagemColetores | TClientDataSet | outro | — | — | — | — | — |
| CdsMensagemColetoresID | TIntegerField | outro | — | — | — | — | — |
| CdsMensagemColetoresMensagem | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 61 | `FMensagemColetoresController.Excluir` |
| `FormCreate` | 84 | `TMensagemColetoresController.Create`, `FMensagemColetoresController.SetConexao` |
| `ValidarCampos` | 109 | — |
| `GravaCampos` | 131 | `FMensagemColetoresController.Inserir`, `FMensagemColetoresController.Atualizar` |
| `ActExibirTudoExecute` | 158 | `FMensagemColetoresController.GetMensagemTodos` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 65: `Excluir o registro?`
- Linha 70: `Problemas com a exclus�o no Banco de Dados!`
- Linha 114: `O conte�do da mensagem n�o pode estar vazio.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
