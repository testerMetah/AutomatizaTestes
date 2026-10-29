# Acesso: TFrmCadSetores

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Setores....

- DFM: `Acesso/UFrmCadSetores.dfm`
- PAS: `Acesso/UFrmCadSetores.pas`
- Handler de abertura: `acCadSetoresExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadSetores | TFrmCadSetores | outro | Cadastro de Setores | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| TSSituacao | TTabSheet | contêiner | Situação (Ctrl+D) | — | — | — | — |
| HoverSpeedButton1 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 0 | — | — | — |
| cmbSituacao | TComboBox | seleção | — | 1 | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| pnlCadastro | TPanel | contêiner | — | 1 | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Label3 | TLabel | rótulo | Situação: | — | — | — | — |
| Label4 | TLabel | rótulo | Nome: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | Text=EdNome |
| cmbStatus | TComboBox | seleção | — | 1 | — | — | Text=Ativo, ItemIndex=0 |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| CdsSetores | TClientDataSet | outro | — | — | — | — | — |
| CdsSetoresId | TIntegerField | outro | — | — | — | — | — |
| CdsSetoresNome | TStringField | outro | — | — | — | — | — |
| CdsSetoresSituacao | TIntegerField | outro | — | — | — | — | — |
| DsSetores | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 76 | `FSetoresController.Excluir`, `FFiltrosController.VerificarSetorUpdate` |
| `ActExibirTudoExecute` | 105 | `FSetoresController.GetSetoresTodos` |
| `ActIncluirExecute` | 127 | — |
| `ActIrExecute` | 133 | `FSetoresController.GetSetor`, `FSetoresController.GetSetoresPorDescricao` |
| `FormCreate` | 218 | `TSetoresController.Create`, `FSetoresController.SetConexao`, `TFiltrosController.Create`, `FFiltrosController.SetConexao` |
| `GravaCampos` | 238 | `FSetoresController.Inserir`, `FSetoresController.Atualizar` |
| `ValidarCampos` | 279 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 83: `Excluir o registro?`
- Linha 89: `Problemas com a exclus�o no Banco de Dados!`
- Linha 94: `Problemas com a exclus�o no Banco de Dados!`
- Linha 100: `Problemas com a exclus�o no Banco de Dados!`
- Linha 284: `O Nome do setor deve ser informado.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
