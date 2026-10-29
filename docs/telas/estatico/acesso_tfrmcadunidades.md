# Acesso: TFrmCadUnidades

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Unidades....

- DFM: `Acesso/UFrmCadUnidades.dfm`
- PAS: `Acesso/UFrmCadUnidades.pas`
- Handler de abertura: `acCadUnidadesExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadUnidades | TFrmCadUnidades | outro | Cadastro de Unidades | — | — | — | — |
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
| Label2 | TLabel | rótulo | Situação: | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Label6 | TLabel | rótulo | Código: | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 1 | — | — | — |
| cmbStatus | TComboBox | seleção | — | 2 | — | — | Text=Ativo, ItemIndex=0 |
| EdCodigo | TEdit | campo de texto/data | — | 3 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DsUnidades | TDataSource | outro | — | — | — | — | — |
| CdsUnidades | TClientDataSet | outro | — | — | — | — | — |
| CdsUnidadesId | TIntegerField | outro | — | — | — | — | — |
| CdsUnidadesNome | TStringField | outro | — | — | — | — | — |
| CdsUnidadesStatus | TIntegerField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 75 | `TUnidadesController.Create`, `FUnidadesController.SetConexao`, `TFiltrosController.Create`, `FFiltrosController.SetConexao` |
| `GravaCampos` | 92 | `FUnidadesController.Inserir`, `FUnidadesController.Atualizar` |
| `ActExcluirExecute` | 140 | `FUnidadesController.Excluir`, `FFiltrosController.VerificarUnidadeUpdate` |
| `ActExibirTudoExecute` | 169 | `FUnidadesController.GetUnidadesTodos` |
| `ActIncluirExecute` | 191 | — |
| `ActIrExecute` | 197 | `FUnidadesController.GetUnidade`, `FUnidadesController.GetUnidadesPorDescricao` |
| `ValidarCampos` | 259 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 147: `Excluir o registro?`
- Linha 153: `Problemas com a exclus�o no Banco de Dados!`
- Linha 158: `Problemas com a exclus�o no Banco de Dados!`
- Linha 164: `Problemas com a exclus�o no Banco de Dados!`
- Linha 264: `O Nome da unidade deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
