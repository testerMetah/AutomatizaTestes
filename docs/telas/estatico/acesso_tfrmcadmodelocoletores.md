# Acesso: TFrmCadModeloColetores

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Coletores > Modelos de Coletores....

- DFM: `Acesso/uFrmCadModeloColetores.dfm`
- PAS: `Acesso/uFrmCadModeloColetores.pas`
- Handler de abertura: `acCadModeloColetoresExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadModeloColetores | TFrmCadModeloColetores | outro | Cadastro de Modelo de Coletores | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | Visible=False, Enabled=False |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| Label7 | TLabel | rótulo | Sinal Decimal: | — | — | — | Visible=False |
| pnlFundoCadastro | TPanel | contêiner | — | 4 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| gbxLayoutArquivo | TGroupBox | contêiner | Layout nos Arquivos  | 3 | — | — | Visible=False |
| PnlGridLayout | TPanel | contêiner | — | 0 | — | — | — |
| pcLayoutArquivo | TPageControl | contêiner | — | 0 | — | — | — |
| tabCabecalho | TTabSheet | contêiner | Cabeçalho | — | — | — | — |
| DbgLayoutCab | TDBGrid | grade | — | 0 | — | — | Visible=True |
| tabDetalhe | TTabSheet | contêiner | Detalhes | — | — | — | — |
| DbgLayoutDet | TDBGrid | grade | — | 0 | — | — | Visible=True |
| tabRodape | TTabSheet | contêiner | Rodapé | — | — | — | — |
| DbgLayoutRod | TDBGrid | grade | — | 0 | — | — | Visible=True |
| PanelGridLayoutBotao | TPanel | contêiner | — | 1 | — | — | — |
| Label3 | TLabel | rótulo | Campo | — | — | — | — |
| Label4 | TLabel | rótulo | Tipo | — | — | — | — |
| Label5 | TLabel | rótulo | Tamanho | — | — | — | — |
| BtnLayoutNovo | TSpeedButton | ação | — | — | — | — | — |
| Label6 | TLabel | rótulo | Formato | — | — | — | — |
| BtnLayoutExcluir | TSpeedButton | ação | — | — | — | — | — |
| EdCampo | TEdit | campo de texto/data | — | 0 | — | — | Text=EDCAMPO |
| CbxTipo | TComboBox | seleção | — | 1 | — | — | — |
| BtnOkLayout | TBitBtn | outro | OK | 4 | — | — | — |
| BtnCancelaLayout | TBitBtn | outro | Cancelar | 5 | — | — | — |
| EdTamanho | TSpinEdit | campo de texto/data | — | 2 | — | — | — |
| EdFormato | TEdit | campo de texto/data | — | 3 | — | — | Text=EDTIPO |
| PnlGridLayoutLado | TPanel | contêiner | — | 2 | — | — | — |
| pnlSetas | TPanel | contêiner | — | 0 | — | — | — |
| BtnSetaParaCima | THoverSpeedButton | ação |  | 0 | — | — | — |
| BtnSetaParaBaixo | THoverSpeedButton | ação |  | 1 | — | — | — |
| Panel1 | TPanel | contêiner | — | 3 | — | — | — |
| cbxSinalDecimal | TComboBox | seleção | — | 0 | — | — | Visible=False |
| rgFormatoCampos | TRadioGroup | seleção | Formato dos Campos | 1 | — | — | Visible=False |
| EdCaracterSeparador | TEdit | campo de texto/data | — | 2 | — | — | Text=EdMarca, Visible=False |
| PnlCampos | TPanel | contêiner | — | 5 | — | — | — |
| lblNome | TLabel | rótulo | Nome: | — | — | — | — |
| lblMarca | TLabel | rótulo | Marca: | — | — | — | — |
| mlMarca | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblNomeMarca | TLabel | rótulo | lblNomeMarca | — | — | — | — |
| imgNome | TImage | outro | — | — | — | — | — |
| imgMarca | TImage | outro | — | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | Text=EDNOME |
| EdMarca | TEdit | campo de texto/data | — | 1 | — | — | Text=EdMarca |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActCancelar | TAction | ação | — | — | — | — | — |
| acLayoutOK | TAction | ação | OK | — | — | — | — |
| acLayoutCancelar | TAction | ação | Cancelar | — | — | — | — |
| acLayoutNovo | TAction | ação | — | — | — | — | — |
| acLayoutAlterar | TAction | ação | — | — | — | — | — |
| acLayoutExcluir | TAction | ação | — | — | — | — | — |
| acSetaParaCima | TAction | ação | — | — | — | — | — |
| acSetaParaBaixo | TAction | ação | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| CdsLayout | TClientDataSet | outro | — | — | — | — | — |
| CdsLayoutId | TIntegerField | outro | — | — | — | — | — |
| CdsLayoutlayout | TIntegerField | outro | — | — | — | — | — |
| CdsLayoutordem | TIntegerField | outro | — | — | — | — | — |
| CdsLayoutcampo | TStringField | outro | — | — | — | — | — |
| CdsLayouttipo | TIntegerField | outro | — | — | — | — | — |
| CdsLayouttamanho | TIntegerField | outro | — | — | — | — | — |
| CdsLayoutidmodelo | TIntegerField | outro | — | — | — | — | — |
| CdsLayoutformato | TStringField | outro | — | — | — | — | — |
| CdsLayoutTipoNome | TStringField | outro | — | — | — | — | — |
| DsLayout | TDataSource | outro | — | — | — | — | — |
| CdsModeloColetores | TClientDataSet | outro | — | — | — | — | — |
| CdsModeloColetoresId | TIntegerField | outro | — | — | — | — | — |
| CdsModeloColetoresNome | TStringField | outro | — | — | — | — | — |
| CdsModeloColetoresIdMarca | TStringField | outro | — | — | — | — | — |
| CdsModeloColetoresSinalDecimal | TIntegerField | outro | — | — | — | — | — |
| CdsModeloColetoresFormatoCampos | TIntegerField | outro | — | — | — | — | — |
| CdsModeloColetoresCaracSepara | TStringField | outro | — | — | — | — | — |
| CdsModeloColetoresNomeSinalDecimal | TStringField | outro | — | — | — | — | — |
| CdsModeloColetoresNomeFormatoCampos | TStringField | outro | — | — | — | — | — |
| DsModeloColetores | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `acLayoutCancelarExecute` | 156 | — |
| `acLayoutExcluirExecute` | 163 | — |
| `ActCancelarExecute` | 255 | — |
| `ActExcluirExecute` | 262 | `FModeloColetoresController.Excluir` |
| `ActExibirTudoExecute` | 277 | `FModeloColetoresController.GetModeloColetoresTodos` |
| `ActIncluirExecute` | 298 | — |
| `ActIrExecute` | 334 | `FModeloColetoresController.GetModeloColetor`, `FModeloColetoresController.GetModeloColetoresPorDescricao` |
| `ActSalvarExecute` | 371 | — |
| `FormCreate` | 522 | `TModeloColetoresController.Create`, `FModeloColetoresController.SetConexao`, `TModeloColLayoutController.Create`, `FModeloColLayoutController.SetConexao` |
| `GravaCampos` | 556 | `FModeloColetoresController.Inserir`, `FModeloColetoresController.Atualizar` |
| `GravaCamposLayout` | 586 | `FModeloColLayoutController.Inserir`, `FModeloColLayoutController.Atualizar`, `FModeloColLayoutController.Excluir` |
| `ValidarCampos` | 726 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 171: `Tem deseja excluir o item `
- Linha 266: `Excluir o registro?`
- Linha 271: `Problemas com a exclusão no Banco de Dados!`
- Linha 490: `Marca de Coletor inexistente`
- Linha 731: `O Nome do Modelo de coletores é obrigatório.`
- Linha 739: `A Marca do Modelo de coletores é obrigatório.`
- Linha 747: `Para este tipo de Formato de Campo é obrigatório informar o Caracter.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
