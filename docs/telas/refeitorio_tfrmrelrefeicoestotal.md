# Refeitório > Relatórios > Refeições Total

> Inventário estático de `Acesso/UFrmRelRefeicoesTotal.dfm` e `Acesso/UFrmRelRefeicoesTotal.pas` no commit `28074dd`. Esta ficha combina inventário estático com notas de leitura manual das procedures; ainda requer conferência de controllers, DAOs e do build instalado.

- Form: `TFrmRelRefeicoesTotal`
- Abertura: `Action1Execute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FrmRelRefeicoesTotal` | `TFrmRelRefeicoesTotal` (herdado) | Relatório Total de Refeições | — | `—` | — | — | — |
| `PgRelatorio` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `TabDefinições` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Panel1` | `TPanel` (herdado) | — | 2 | `—` | — | — | — |
| `RgbSelecao` | `TRadioGroup` (herdado) | — | — | `—` | — | — | — |
| `PgSelecao` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `Filtros` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `PnGrupoAcesso` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `AdicionaFiltro` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `RemoveFiltro` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `RemoveTudoFiltros` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `AdicionaTudoFiltros` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `DBGridFiltro` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `DBGridFiltro2` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `Setor` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `PnSetor` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `AdicionaSetor` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `RemoveSetor` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `DBGridSetor` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `DBGridSetor2` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `Pessoa` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `PnPessoa` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `AdicionaPessoa` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `AdicionaTudoPessoa` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `DBGridPessoa` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `DBGridPessoa2` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `Geral` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `lblTodosGeral` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `Unidade` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `AdiconaUnidade` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `RemoveUnidade` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `RemoveTudoUnidade` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `DBGridUnidade` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `DBGridUnidade2` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `PreCadastro` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `DBGridPreCadastro` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `DBGridPreCadastro2` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `EmpresaAcesso` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `RemoveEmpresaAcesso` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `AdicionaEmpresaAcesso` | `TSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `DBGridEmpresaAcesso` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `DBGridEmpresaAcesso2` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `Panel2` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `SBGrids` | `TSearchBox` (herdado) | — | — | `—` | — | — | — |
| `pnlOrdenacao` | `TPanel` (herdado) | — | 3 | `—` | — | — | — |
| `lbOrdenar` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `lbOrdem` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `cmbOrdenar` | `TComboBox` (herdado) | — | — | `—` | — | — | — |
| `cmbOrdem` | `TComboBox` (herdado) | — | — | `—` | — | — | — |
| `GbPeriodo` | `TGroupBox` |            Período | 0 | `—` | — | — | — |
| `Até` | `TLabel` | Até | — | `—` | — | — | — |
| `MEdDataInicio` | `TMaskEdit` | — | 0 | `!99/99/9999;1; ` | 10 | Text=  /  /     | — |
| `MEdDataFim` | `TMaskEdit` | — | 2 | `!99/99/9999;1; ` | 10 | Text=  /  /     | — |
| `MEdHoraFim` | `TMaskEdit` | — | 3 | `!99:99;1; ` | 5 | Text=  :   | — |
| `MEdHoraInicio` | `TMaskEdit` | — | 1 | `!99:99;1; ` | 5 | Text=  :   | — |
| `GbCardapio` | `TGroupBox` |            Cardápio | 1 | `—` | — | — | — |
| `LblCardapio` | `TLabel` | LblCardapio | — | `—` | — | — | — |
| `BtnIrCardapios` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `EdCardapio` | `TEdit` | — | 0 | `—` | — | — | — |
| `GbColetor` | `TGroupBox` |            Coletor | 4 | `—` | — | — | — |
| `BtnIrColetor` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `lbColetor` | `TListBox` | — | 0 | `—` | — | — | — |
| `btnExcluiFiltro` | `THoverSpeedButton` | Excluir | 1 | `—` | — | — | OnClick=btnExcluiFiltroClick |
| `Selecao` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Label1` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `PnBotao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `BtnImpressao` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `frxPDFExport1` | `TfrxPDFExport` (herdado) | — | — | `—` | — | — | — |
| `ActionList1` | `TActionList` (herdado) | — | — | `—` | — | — | — |
| `frxRelUnidade` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelPessoas` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelMarcacoesOnline` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelAcessoVisitantesTerceiros` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelAvaliacaoRefeicao` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelCracha` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelCreditos` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelEmpresas` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelHistoricoAcessoRapido` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelPresenca` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `Cabecalho` | `TfrxHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelPreCadastro` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelRefeicoesTotal` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `GroupHeader1` | `TfrxGroupHeader` (herdado) | — | — | `—` | — | — | — |
| `fxRelatorioSelecao` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelResCon` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelReservasRefeicoes` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `GroupHeader1` | `TfrxGroupHeader` (herdado) | — | — | `—` | — | — | — |
| `frxRelSetor` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelMonitoramentoColaboradorVinculadoEstacionamento` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelOcorrenciasVeiculos` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelVeiculosAcessos` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelVisitantesTerceiros` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelDigitaisFaces` | `TfrxReport` (herdado) | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` (herdado) | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` (herdado) | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` (herdado) | — | — | `—` | — | — | — |
| `frxRelatorio` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `NomeEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo1` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo2` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo14` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo19` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line6` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line7` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line8` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line11` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line15` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line13` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo22` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo23` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo25` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo27` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo28` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `GroupHeader2` | `TfrxGroupHeader` | — | — | `—` | — | — | — |
| `Shape7` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `fxRelatorioNome` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MasterData2` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Shape6` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Memo15` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo16` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo17` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo18` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line16` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line17` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line18` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `fxRelatorioDataHora` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MasterData1` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Shape9` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Memo24` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line10` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo26` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Header1` | `TfrxHeader` | — | — | `—` | — | — | — |
| `Memo20` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Shape8` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `GroupHeader1` | `TfrxGroupHeader` | — | — | `—` | — | — | — |
| `Shape10` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `fxRelatorioSelecao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Header2` | `TfrxHeader` | — | — | `—` | — | — | — |
| `GroupFooter1` | `TfrxGroupFooter` | — | — | `—` | — | — | — |
| `GroupFooter2` | `TfrxGroupFooter` | — | — | `—` | — | — | — |
| `fxTotalizador` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `shpRodape2` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `fxRelatorio` | `TfrxDBDataset` | — | — | `—` | — | — | — |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 191: `Selecione um item para excluí-lo.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActRelatorioExecute`
- `btnExcluiFiltroClick`

## Fluxo e regras identificados

O fluxo herdado de seleção, consulta, geração e fechamento está em [base_relatorio_padrao.md](base_relatorio_padrao.md). Salvar, Excluir e Cancelar de cadastro não se aplicam a este formulário.

- `ActRelatorioExecute` valida data/hora inicial e final, mostra mensagem e aborta se falhar. Usa `GetIdsColetor` para múltiplos coletores, `StrToIntDef(EdCardapio.Text, 0)` para cardápio, seleção, ordenação e ordem. Chama `ReceberDadosRelRefeicoesTotal` e a geração herdada.
- `btnExcluiFiltroClick` mostra `Selecione um item para excluí-lo.` se `lbColetor` não está focado; caso contrário remove o item selecionado.

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
