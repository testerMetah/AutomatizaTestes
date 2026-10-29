# Refeitorio: TFrmRelRefeicoesTotal

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Relatórios > Refeições Total.

- DFM: `Acesso/UFrmRelRefeicoesTotal.dfm`
- PAS: `Acesso/UFrmRelRefeicoesTotal.pas`
- Handler de abertura: `Action1Execute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmRelRefeicoesTotal | TFrmRelRefeicoesTotal | outro | Relatório Total de Refeições | — | — | — | — |
| PgRelatorio | TPageControl | contêiner | — | — | — | — | — |
| TabDefinições | TTabSheet | contêiner | — | — | — | — | — |
| Panel1 | TPanel | contêiner | — | 2 | — | — | — |
| RgbSelecao | TRadioGroup | seleção | — | — | — | — | — |
| PgSelecao | TPageControl | contêiner | — | — | — | — | — |
| Filtros | TTabSheet | contêiner | — | — | — | — | — |
| PnGrupoAcesso | TPanel | contêiner | — | — | — | — | — |
| AdicionaFiltro | TSpeedButton | ação | — | — | — | — | — |
| RemoveFiltro | TSpeedButton | ação | — | — | — | — | — |
| RemoveTudoFiltros | TSpeedButton | ação | — | — | — | — | — |
| AdicionaTudoFiltros | TSpeedButton | ação | — | — | — | — | — |
| DBGridFiltro | TDBGrid | grade | — | — | — | — | — |
| DBGridFiltro2 | TDBGrid | grade | — | — | — | — | — |
| Setor | TTabSheet | contêiner | — | — | — | — | — |
| PnSetor | TPanel | contêiner | — | — | — | — | — |
| AdicionaSetor | TSpeedButton | ação | — | — | — | — | — |
| RemoveSetor | TSpeedButton | ação | — | — | — | — | — |
| DBGridSetor | TDBGrid | grade | — | — | — | — | — |
| DBGridSetor2 | TDBGrid | grade | — | — | — | — | — |
| Pessoa | TTabSheet | contêiner | — | — | — | — | — |
| PnPessoa | TPanel | contêiner | — | — | — | — | — |
| AdicionaPessoa | TSpeedButton | ação | — | — | — | — | — |
| AdicionaTudoPessoa | TSpeedButton | ação | — | — | — | — | — |
| DBGridPessoa | TDBGrid | grade | — | — | — | — | — |
| DBGridPessoa2 | TDBGrid | grade | — | — | — | — | — |
| Geral | TTabSheet | contêiner | — | — | — | — | — |
| lblTodosGeral | TLabel | rótulo | — | — | — | — | — |
| Unidade | TTabSheet | contêiner | — | — | — | — | — |
| AdiconaUnidade | TSpeedButton | ação | — | — | — | — | — |
| RemoveUnidade | TSpeedButton | ação | — | — | — | — | — |
| RemoveTudoUnidade | TSpeedButton | ação | — | — | — | — | — |
| DBGridUnidade | TDBGrid | grade | — | — | — | — | — |
| DBGridUnidade2 | TDBGrid | grade | — | — | — | — | — |
| PreCadastro | TTabSheet | contêiner | — | — | — | — | — |
| DBGridPreCadastro | TDBGrid | grade | — | — | — | — | — |
| DBGridPreCadastro2 | TDBGrid | grade | — | — | — | — | — |
| EmpresaAcesso | TTabSheet | contêiner | — | — | — | — | — |
| RemoveEmpresaAcesso | TSpeedButton | ação | — | — | — | — | — |
| AdicionaEmpresaAcesso | TSpeedButton | ação | — | — | — | — | — |
| DBGridEmpresaAcesso | TDBGrid | grade | — | — | — | — | — |
| DBGridEmpresaAcesso2 | TDBGrid | grade | — | — | — | — | — |
| Panel2 | TPanel | contêiner | — | — | — | — | — |
| SBGrids | TSearchBox | outro | — | — | — | — | — |
| pnlOrdenacao | TPanel | contêiner | — | 3 | — | — | — |
| lbOrdenar | TLabel | rótulo | — | — | — | — | — |
| lbOrdem | TLabel | rótulo | — | — | — | — | — |
| cmbOrdenar | TComboBox | seleção | — | — | — | — | — |
| cmbOrdem | TComboBox | seleção | — | — | — | — | — |
| GbPeriodo | TGroupBox | contêiner |            Período | 0 | — | — | — |
| Até | TLabel | rótulo | Até | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| MEdDataInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdDataFim | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdHoraFim | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| MEdHoraInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| GbCardapio | TGroupBox | contêiner |            Cardápio | 1 | — | — | — |
| LblCardapio | TLabel | rótulo | LblCardapio | — | — | — | — |
| BtnIrCardapios | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| EdCardapio | TEdit | campo de texto/data | — | 0 | — | — | — |
| GbColetor | TGroupBox | contêiner |            Coletor | 4 | — | — | — |
| BtnIrColetor | TMetaEquipLocalizar | outro | — | — | — | — | — |
| ImgColetor | TImage | outro | — | — | — | — | — |
| lbColetor | TListBox | seleção | — | 0 | — | — | — |
| btnExcluiFiltro | THoverSpeedButton | ação | Excluir | 1 | — | — | — |
| Selecao | TTabSheet | contêiner | — | — | — | — | — |
| Label1 | TLabel | rótulo | — | — | — | — | — |
| PnBotao | TPanel | contêiner | — | — | — | — | — |
| BtnImpressao | THoverSpeedButton | ação | — | — | — | — | — |
| frxPDFExport1 | TfrxPDFExport | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| CdsFiltro | TClientDataSet | outro | — | — | — | — | — |
| CdsSetores | TClientDataSet | outro | — | — | — | — | — |
| CdsPessoas | TClientDataSet | outro | — | — | — | — | — |
| DsFiltro | TDataSource | outro | — | — | — | — | — |
| DsSetores | TDataSource | outro | — | — | — | — | — |
| DsPessoas | TDataSource | outro | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| frxRelUnidade | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelPessoas | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelMarcacoesOnline | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelAcessoVisitantesTerceiros | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelAvaliacaoRefeicao | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelCracha | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelCreditos | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelEmpresas | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelHistoricoAcessoRapido | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelPresenca | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| Cabecalho | TfrxHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelPreCadastro | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelRefeicoesTotal | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| GroupHeader1 | TfrxGroupHeader | outro | — | — | — | — | — |
| fxRelatorioSelecao | TfrxMemoView | outro | — | — | — | — | — |
| frxRelResCon | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelReservasRefeicoes | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| GroupHeader1 | TfrxGroupHeader | outro | — | — | — | — | — |
| frxRelSetor | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelMonitoramentoColaboradorVinculadoEstacionamento | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelOcorrenciasVeiculos | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelVeiculosAcessos | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelVisitantesTerceiros | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelDigitaisFaces | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| CdsPreCadastro | TClientDataSet | outro | — | — | — | — | — |
| IntegerField1 | TIntegerField | outro | — | — | — | — | — |
| StringField1 | TStringField | outro | — | — | — | — | — |
| DsPreCadastro | TDataSource | outro | — | — | — | — | — |
| frxRelatorio | TfrxReport | outro | — | — | — | — | — |
| Data | TfrxDataPage | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Shape1 | TfrxShapeView | outro | — | — | — | — | — |
| Shape3 | TfrxShapeView | outro | — | — | — | — | — |
| NomeEmpresa | TfrxMemoView | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo6 | TfrxMemoView | outro | — | — | — | — | — |
| MemoNomeRelatorio | TfrxMemoView | outro | — | — | — | — | — |
| Memo3 | TfrxMemoView | outro | — | — | — | — | — |
| Memo4 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| Picture1 | TfrxPictureView | outro | — | — | — | — | — |
| Memo1 | TfrxMemoView | outro | — | — | — | — | — |
| Memo2 | TfrxMemoView | outro | — | — | — | — | — |
| Memo14 | TfrxMemoView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Line6 | TfrxLineView | outro | — | — | — | — | — |
| Line7 | TfrxLineView | outro | — | — | — | — | — |
| Line8 | TfrxLineView | outro | — | — | — | — | — |
| Line11 | TfrxLineView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line15 | TfrxLineView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| Line13 | TfrxLineView | outro | — | — | — | — | — |
| Memo22 | TfrxMemoView | outro | — | — | — | — | — |
| Memo23 | TfrxMemoView | outro | — | — | — | — | — |
| Memo25 | TfrxMemoView | outro | — | — | — | — | — |
| Memo27 | TfrxMemoView | outro | — | — | — | — | — |
| Memo28 | TfrxMemoView | outro | — | — | — | — | — |
| GroupHeader2 | TfrxGroupHeader | outro | — | — | — | — | — |
| Shape7 | TfrxShapeView | outro | — | — | — | — | — |
| fxRelatorioNome | TfrxMemoView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Shape6 | TfrxShapeView | outro | — | — | — | — | — |
| Memo15 | TfrxMemoView | outro | — | — | — | — | — |
| Memo16 | TfrxMemoView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line17 | TfrxLineView | outro | — | — | — | — | — |
| Line18 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| fxRelatorioDataHora | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| MasterData1 | TfrxMasterData | outro | — | — | — | — | — |
| Shape9 | TfrxShapeView | outro | — | — | — | — | — |
| Memo24 | TfrxMemoView | outro | — | — | — | — | — |
| Line10 | TfrxLineView | outro | — | — | — | — | — |
| Memo26 | TfrxMemoView | outro | — | — | — | — | — |
| Header1 | TfrxHeader | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| Shape8 | TfrxShapeView | outro | — | — | — | — | — |
| GroupHeader1 | TfrxGroupHeader | outro | — | — | — | — | — |
| Shape10 | TfrxShapeView | outro | — | — | — | — | — |
| fxRelatorioSelecao | TfrxMemoView | outro | — | — | — | — | — |
| Header2 | TfrxHeader | outro | — | — | — | — | — |
| GroupFooter1 | TfrxGroupFooter | outro | — | — | — | — | — |
| GroupFooter2 | TfrxGroupFooter | outro | — | — | — | — | — |
| fxTotalizador | TfrxMemoView | outro | — | — | — | — | — |
| shpRodape2 | TfrxShapeView | outro | — | — | — | — | — |
| fxRelatorio | TfrxDBDataset | outro | — | — | — | — | — |
| CdsRelatorio | TClientDataSet | outro | — | — | — | — | — |
| CdsRelatorioId | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioDataHora | TDateTimeField | outro | — | — | — | — | — |
| CdsRelatorioTipoRefeicao | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioNome | TStringField | outro | — | — | — | — | — |
| CdsRelatorioColetor | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioDescColetor | TStringField | outro | — | — | — | — | — |
| CdsRelatorioorigem | TStringField | outro | — | — | — | — | — |
| CdsRelatorioIdRefeitorio | TIntegerField | outro | — | — | — | — | — |
| CdsRelatoriodescrefeitorio | TStringField | outro | — | — | — | — | — |
| CdsRelatorioIdCardapio | TIntegerField | outro | — | — | — | — | — |
| CdsRelatoriodescCardapio | TStringField | outro | — | — | — | — | — |
| CdsRelatorioValorRefeicao | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioTipoValorRefeicao | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioUtilizaCreditosRefeitorio | TBooleanField | outro | — | — | — | — | — |
| CdsRelatorioQuantidade | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioCountCardapio | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioNomeCardapioCount | TStringField | outro | — | — | — | — | — |
| CdsRelatorioIdSetor | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioSetor | TStringField | outro | — | — | — | — | — |
| CdsRelatorioIdEmpresa | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioEmpresa | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActRelatorioExecute` | 151 | — |
| `FormCreate` | 204 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 191: `Selecione um item para excluí-lo.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
