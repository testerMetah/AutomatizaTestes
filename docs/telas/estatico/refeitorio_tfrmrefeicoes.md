# Refeitorio: TFrmRefeicoes

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Refeitório > Incluir Refeições....

- DFM: `Acesso/UFrmCadRefeicoes.dfm`
- PAS: `Acesso/UFrmCadRefeicoes.pas`
- Handler de abertura: `acRefRefeicoesExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmRefeicoes | TFrmRefeicoes | outro | Incluir Refeições Manual | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TbsPeriodo | TTabSheet | contêiner | Período (Ctrl+A) | — | — | — | — |
| Label4 | TLabel | rótulo | De | — | — | — | — |
| Label5 | TLabel | rótulo | Até | — | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| DtTermino | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| TmTermino | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| HoverSpeedButton5 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 4 | — | — | — |
| tbsTipoRefeicao | TTabSheet | contêiner | Tipo de Refeição (Ctrl+B) | — | — | — | — |
| Label9 | TLabel | rótulo | Tipo de Refeição | — | — | — | — |
| CmbLocTipoRefeicao | TComboBox | seleção | — | 0 | — | — | Text=Ambas, ItemIndex=2 |
| HoverSpeedButton4 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| TbsPessoa | TTabSheet | contêiner | Pessoa (Ctrl+G) | — | — | — | — |
| mlFiltroPessoa | TMetaEquipLocalizar | outro | F5 | — | — | — | — |
| lblPessoaFiltro | TLabel | rótulo | lblPessoa | — | — | — | — |
| Label11 | TLabel | rótulo | Pessoa | — | — | — | — |
| EdPessoaFiltro | TEdit | campo de texto/data | — | 0 | — | — | Text=EdPessoa |
| HoverSpeedButton3 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| TabSheet2 | TTabSheet | contêiner | Inativo | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| TbsRefeitorio | TTabSheet | contêiner | Refeitório (Ctrl+H) | — | — | — | — |
| mlRefeitorio | TMetaEquipLocalizar | outro | F5 | — | — | — | — |
| lblRefeitorioFiltro | TLabel | rótulo | lblRefeitorio | — | — | — | — |
| Label12 | TLabel | rótulo | Refeitório | — | — | — | — |
| EdRefeitorio | TEdit | campo de texto/data | — | 0 | — | — | Text=EdRefeitorio |
| HoverSpeedButton2 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| TbsCardapio | TTabSheet | contêiner | Cardápio (Ctrl+J) | — | — | — | — |
| Label13 | TLabel | rótulo | Cardápio | — | — | — | — |
| mlCardapio | TMetaEquipLocalizar | outro | F5 | — | — | — | — |
| lblCardapioFiltro | TLabel | rótulo | lblRefeitorio | — | — | — | — |
| EdCardapio | TEdit | campo de texto/data | — | 0 | — | — | Text=EdCardapio |
| HoverSpeedButton1 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| pnlBuscar | TPanel | contêiner | Acesso | 1 | — | — | Visible=False, Enabled=False |
| Shape3 | TShape | outro | — | — | — | — | — |
| btnBuscar | TSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| Label1 | TLabel | rótulo | Tipo da Refeição: | — | — | — | Visible=False, Enabled=False |
| Label2 | TLabel | rótulo | Data/Hora: | — | — | — | — |
| Label3 | TLabel | rótulo | Coletor: | — | — | — | — |
| mlColetor | TMetaEquipLocalizar | outro | F5 | — | — | — | — |
| lblColetor | TLabel | rótulo | lblColetor | — | — | — | — |
| Label7 | TLabel | rótulo | Refeitório: | — | — | — | — |
| lblRefeitorio | TLabel | rótulo | lblRefeitorio | — | — | — | — |
| Label8 | TLabel | rótulo | Cardápio: | — | — | — | — |
| lblCardapio | TLabel | rótulo | lblCardapio | — | — | — | — |
| lblTipoSelecao | TLabel | rótulo | Tipo de Seleção: | — | — | — | — |
| Label6 | TLabel | rótulo | Valor da Refeição: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| Image6 | TImage | outro | — | — | — | — | Visible=False, Enabled=False |
| Image7 | TImage | outro | — | — | — | — | — |
| mlEscCardapio | TMetaEquipLocalizar | outro | F6 | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | Enabled=False |
| pnlFundoCadastro | TPanel | contêiner | — | 4 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| dtRefeicao | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| tmRefeicao | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| cmbTipoRefeicao | TComboBox | seleção | — | 3 | — | — | Text=Reserva, ItemIndex=0, Visible=False, Enabled=False |
| EdColetor | TEdit | campo de texto/data | — | 2 | — | — | — |
| CmbTipoSelecao | TComboBox | seleção | — | 5 | — | — | Text=Geral, ItemIndex=0 |
| PgcTipoSelecoes | TPageControl | contêiner | — | 6 | — | — | — |
| TabFiltros | TTabSheet | contêiner | TabFiltros | — | — | — | — |
| Filtro | TLabel | rótulo | Filtro | — | — | — | — |
| mlFiltro | TMetaEquipLocalizar | outro | F7 | — | — | — | — |
| lblNomeFiltro | TLabel | rótulo | lblNomeFiltro | — | — | — | — |
| EdFiltro | TEdit | campo de texto/data | — | 0 | — | — | Text=EdFiltro |
| TabPessoas | TTabSheet | contêiner | TabPessoas | — | — | — | — |
| Label10 | TLabel | rótulo | Lista de Pessoas | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | F7 | — | — | — | — |
| LstPessoas | TListBox | seleção | — | 0 | — | — | — |
| BtnRemoverSelecaoPessoas | THoverSpeedButton | ação | F10 | 1 | — | — | — |
| TabSetores | TTabSheet | contêiner | TabSetores | — | — | — | — |
| Label14 | TLabel | rótulo | Lista de Setores | — | — | — | — |
| mlSetor | TMetaEquipLocalizar | outro | F7 | — | — | — | — |
| LstSetores | TListBox | seleção | — | 0 | — | — | — |
| BtnRemoverSelecaoSetores | THoverSpeedButton | ação | F10 | 1 | — | — | — |
| TabPreCadastro | TTabSheet | contêiner | TabPreCadastro | — | — | — | — |
| Label15 | TLabel | rótulo | Lista de Pré-Cadastro | — | — | — | — |
| mlPreCadastro | TMetaEquipLocalizar | outro | F7 | — | — | — | — |
| LstPreCadastro | TListBox | seleção | — | 0 | — | — | — |
| BtnRemoverSelecaoPreCadastros | THoverSpeedButton | ação | F10 | 1 | — | — | — |
| cmbTipoValorRefeicao | TComboBox | seleção | — | 7 | — | — | — |
| EdValorRefeicao | TEdit | campo de texto/data | — | 8 | — | — | — |
| edtCardapio | TEdit | campo de texto/data | — | 9 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExibirTudo | TAction | ação | — | — | — | — | — |
| ActLocalizarCodigo | TAction | ação | — | — | — | — | — |
| ActLocalizarNome | TAction | ação | — | — | — | — | — |
| ActCancelar | TAction | ação | — | — | — | — | — |
| ActRelatorio | TAction | ação | Relatório (F6) | — | — | — | — |
| ActPeriodo | TAction | ação | ActPeriodo | — | — | — | — |
| ActTipoRefeicao | TAction | ação | ActTipoRefeicao | — | — | — | — |
| ActPessoa | TAction | ação | ActPessoa | — | — | — | — |
| ActRefeitorio | TAction | ação | ActRefeitorio | — | — | — | — |
| ActCardapio | TAction | ação | ActCardapio | — | — | — | — |
| ActTSPeriodo | TAction | ação | Período (Ctrl+A) | — | — | — | — |
| ActTSTipoRefeicao | TAction | ação | Tipo de Refeição (Ctrl+B) | — | — | — | — |
| ActTSPessoa | TAction | ação | Pessoa (Ctrl+G) | — | — | — | — |
| ActTSRefeitorio | TAction | ação | Refeitório (Ctrl+H) | — | — | — | — |
| ActTSCardapio | TAction | ação | Cardápio (Ctrl+J) | — | — | — | — |
| ActBuscarFiltros | TAction | ação | Buscar (F5) | — | — | — | — |
| ActBuscarCardapio | TAction | ação | Buscar Cardápio (F6) | — | — | — | — |
| ActBuscarSelecao | TAction | ação | Buscar Seleção (F7) | — | — | — | — |
| ActRemoverSelecao | TAction | ação | F10 | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsRefeicoes | TDataSource | outro | — | — | — | — | — |
| CdsRefeicoes | TClientDataSet | outro | — | — | — | — | — |
| CdsRefeicoesId | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesDataHora | TDateTimeField | outro | — | — | — | — | — |
| CdsRefeicoesTipoRefeicao | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesNome | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesColetor | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesDescColetor | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesorigem | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesIdRefeitorio | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesdescrefeitorio | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesIdCardapio | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesdescCardapio | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesValorRefeicao | TFloatField | outro | — | — | — | — | — |
| CdsRefeicoesTipoValorRefeicao | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesUtilizaCreditosRefeitorio | TBooleanField | outro | — | — | — | — | — |
| frxRefeicoes | TfrxReport | outro | — | — | — | — | — |
| Data | TfrxDataPage | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Shape1 | TfrxShapeView | outro | — | — | — | — | — |
| MemoEmpresa | TfrxMemoView | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo6 | TfrxMemoView | outro | — | — | — | — | — |
| Memo7 | TfrxMemoView | outro | — | — | — | — | — |
| MemoNomeRelatorio | TfrxMemoView | outro | — | — | — | — | — |
| Memo11 | TfrxMemoView | outro | — | — | — | — | — |
| Memo3 | TfrxMemoView | outro | — | — | — | — | — |
| Memo4 | TfrxMemoView | outro | — | — | — | — | — |
| Memo8 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| Memo1 | TfrxMemoView | outro | — | — | — | — | — |
| Memo2 | TfrxMemoView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Memo22 | TfrxMemoView | outro | — | — | — | — | — |
| GroupHeader1 | TfrxGroupHeader | outro | — | — | — | — | — |
| MemoQuebra | TfrxMemoView | outro | — | — | — | — | — |
| fxRefeicoesTipoRefeicao | TfrxMemoView | outro | — | — | — | — | — |
| MasterData1 | TfrxMasterData | outro | — | — | — | — | — |
| fxRefeicoesDataHora | TfrxMemoView | outro | — | — | — | — | — |
| fxRefeicoesDescColetor | TfrxMemoView | outro | — | — | — | — | — |
| fxRefeicoesColetor | TfrxMemoView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| Memo23 | TfrxMemoView | outro | — | — | — | — | — |
| GroupFooter1 | TfrxGroupFooter | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| SysMemo1 | TfrxSysMemoView | outro | — | — | — | — | — |
| Memo15 | TfrxMemoView | outro | — | — | — | — | — |
| SysMemo4 | TfrxSysMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| GroupHeader3 | TfrxGroupHeader | outro | — | — | — | — | — |
| Memo10 | TfrxMemoView | outro | — | — | — | — | — |
| fxRefeicoesdescrefeitorio | TfrxMemoView | outro | — | — | — | — | — |
| GroupFooter2 | TfrxGroupFooter | outro | — | — | — | — | — |
| Memo9 | TfrxMemoView | outro | — | — | — | — | — |
| SysMemo2 | TfrxSysMemoView | outro | — | — | — | — | — |
| Memo14 | TfrxMemoView | outro | — | — | — | — | — |
| SysMemo6 | TfrxSysMemoView | outro | — | — | — | — | — |
| GroupHeader2 | TfrxGroupHeader | outro | — | — | — | — | — |
| Memo16 | TfrxMemoView | outro | — | — | — | — | — |
| fxRefeicoesdescCardapio | TfrxMemoView | outro | — | — | — | — | — |
| GroupFooter3 | TfrxGroupFooter | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| SysMemo3 | TfrxSysMemoView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| SysMemo5 | TfrxSysMemoView | outro | — | — | — | — | — |
| fxRefeicoes | TfrxDBDataset | outro | — | — | — | — | — |
| CdsRefeicoesRelatorio | TClientDataSet | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioId | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioDataHora | TDateTimeField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioTipoRefeicao | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioNome | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioColetor | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioDescColetor | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioIdRefeitorio | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesRelatoriodescrefeitorio | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioIdCardapio | TIntegerField | outro | — | — | — | — | — |
| CdsRefeicoesRelatoriodescCardapio | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioorigem | TStringField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioValorRefeicao | TFloatField | outro | — | — | — | — | — |
| CdsRefeicoesRelatorioTipoValorRefeicao | TIntegerField | outro | — | — | — | — | — |
| frxPDFExport1 | TfrxPDFExport | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 315 | `FRefeicoesController.Excluir`, `TCreditosController.Create` |
| `ActExibirTudoExecute` | 366 | — |
| `ActIncluirExecute` | 372 | — |
| `ActIrExecute` | 387 | — |
| `ActRelatorioExecute` | 415 | — |
| `ActSalvarExecute` | 460 | — |
| `FormCreate` | 859 | `TRefeicoesController.Create`, `FRefeicoesController.SetConexao` |
| `GravaCampos` | 1179 | `FRefeicoesController.Inserir`, `TCreditosController.Create`, `TFiltrosController.Create`, `TPessoasController.Create`, `TPreCadastroController.Create`, `lFiltroController.SetConexao`, `lPessoasController.SetConexao`, `lPreCadastroController.SetConexao` |
| `ValidarCampos` | 1485 | — |
| `ValidarFiltros` | 1554 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 249: `Não é possível alterar uma marcação que já foi importada do coletor.`
- Linha 326: `Não é possível excluir uma marcação que já foi importada do coletor.`
- Linha 329: `Excluir o registro?`
- Linha 360: `Problemas com a exclusão no Banco de Dados!`
- Linha 689: `Data Inválida!`
- Linha 712: `Cardápio não cadastrado`
- Linha 742: `Coletor não cadastrado.`
- Linha 768: `Filtro não cadastrado`
- Linha 801: `Pessoa não cadastrada.`
- Linha 826: `Refeitório não cadastrado`
- Linha 842: `Valor inválido.`
- Linha 1480: `Hora Inválida!`
- Linha 1491: `A data da refeição deve ser informada.`
- Linha 1498: `A hora da refeição deve ser informada.`
- Linha 1505: `O coletor deve ser informado.`
- Linha 1512: `O cardápio deve ser informado.`
- Linha 1526: `O Filtro deve ser informado.`
- Linha 1534: `Selecione alguma pessoa na lista.`
- Linha 1542: `Selecione algum setor na lista.`
- Linha 1549: `Nenhum refeitório vinculado, vincule pelo cadastro de coletores.`
- Linha 1558: `Data de Início deve ser informada.`
- Linha 1565: `A hora de Início deve ser informada.`
- Linha 1572: `Data de Término deve ser informada.`
- Linha 1579: `A hora de Término deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
