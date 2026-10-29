# Refeitorio: TFrmCadRefeitorios

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Refeitório > Cadastro....

- DFM: `Acesso/uFrmCadRefeitorio.dfm`
- PAS: `Acesso/uFrmCadRefeitorio.pas`
- Handler de abertura: `acRefCadastroExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadRefeitorios | TFrmCadRefeitorios | outro | Cadastro de Refeitórios | — | — | — | — |
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
| btnImportar | THoverSpeedButton | ação | Importar Refeitórios (Ctrl+F5) | 3 | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| lblColetores | TLabel | rótulo | Coletores de Acesso: | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| pnlCampos | TPanel | contêiner | — | 1 | — | — | — |
| Label4 | TLabel | rótulo | Situação: | — | — | — | — |
| imgNome | TImage | outro | — | — | — | — | — |
| Label3 | TLabel | rótulo | Nome: | — | — | — | — |
| imgSituacao | TImage | outro | — | — | — | — | — |
| imgCreditos | TImage | outro | — | — | — | — | Visible=False |
| lblSentidoAcesso | TLabel | rótulo | Sentido de Acesso: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| cmbStatus | TComboBox | seleção | — | 1 | — | — | Text=Ativo, ItemIndex=0 |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | — |
| ChUtilizaControleCreditos | TCheckBox | seleção | Utilizar Controle de Créditos | 3 | — | — | Visible=False |
| cmbSentidoAcesso | TComboBox | seleção | — | 2 | — | — | Text=Entrada, ItemIndex=0 |
| pnlGrid | TPanel | contêiner | — | 2 | — | — | — |
| GridItens | TDBGrid | grade | — | 0 | — | — | Visible=True |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActImportar | TAction | ação | Importar Refeitórios (Ctrl+F5) | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsRefeitorios | TDataSource | outro | — | — | — | — | — |
| CdsRefeitorios | TClientDataSet | outro | — | — | — | — | — |
| CdsRefeitoriosId | TIntegerField | outro | — | — | — | — | — |
| CdsRefeitoriosNome | TStringField | outro | — | — | — | — | — |
| CdsRefeitoriosSentidoAcesso | TStringField | outro | — | — | — | — | — |
| CdsRefeitoriosSituacao | TIntegerField | outro | — | — | — | — | — |
| CdsConsulta | TClientDataSet | outro | — | — | — | — | — |
| CdsConsultaSELECIONADO | TIntegerField | outro | — | — | — | — | — |
| CdsConsultaID | TStringField | outro | — | — | — | — | — |
| CdsConsultaNOME | TStringField | outro | — | — | — | — | — |
| dsConsulta | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 122 | `FCardRefController.ExcluirPorRefeitorio`, `FRefeitoriosController.Excluir` |
| `ActExibirTudoExecute` | 149 | `FRefeitoriosController.GetRefeitoriosTodos` |
| `ActIncluirExecute` | 260 | — |
| `ActIrExecute` | 266 | `FRefeitoriosController.GetRefeitorio`, `FRefeitoriosController.GetRefeitoriosPorDescricao` |
| `FormCreate` | 455 | `TColetoresController.Create`, `FColetoresController.SetConexao`, `TRefeitoriosController.Create`, `FRefeitoriosController.SetConexao`, `TCardapiosRefeitoriosController.Create`, `FCardRefController.SetConexao` |
| `GravaCampos` | 481 | `FRefeitoriosController.Inserir`, `FRefeitoriosController.Atualizar` |
| `ValidarCampos` | 621 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 108: `Usuário MASTER não pode salvar registros.`
- Linha 129: `Excluir o registro?`
- Linha 227: `Erro ao gravar informações no Banco de Dados: `
- Linha 229: `Importação realizada com sucesso`
- Linha 626: `O Nome do refeitório deve ser informado.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
