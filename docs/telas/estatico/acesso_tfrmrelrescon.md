# Acesso: TFrmRelResCon

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Relatórios > Reservas e Consumos....

- DFM: `Acesso/UFrmRelResCon.dfm`
- PAS: `Acesso/UFrmRelResCon.pas`
- Handler de abertura: `acRelReservasConsumosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmRelResCon | TFrmRelResCon | outro | Relatório de Reservas e Consumos | — | — | — | — |
| PgRelatorio | TPageControl | contêiner | — | — | — | — | — |
| TabDefinições | TTabSheet | contêiner | — | — | — | — | — |
| ImgInconsistencias | TImage | outro | — | — | — | — | — |
| Panel1 | TPanel | contêiner | — | 3 | — | — | — |
| RgbSelecao | TRadioGroup | seleção | — | — | — | — | — |
| PgSelecao | TPageControl | contêiner | — | — | — | — | — |
| Filtros | TTabSheet | contêiner | — | — | — | — | — |
| PnGrupoAcesso | TPanel | contêiner | — | — | — | — | — |
| Setor | TTabSheet | contêiner | — | — | — | — | — |
| PnSetor | TPanel | contêiner | — | — | — | — | — |
| DBGridSetor | TDBGrid | grade | — | — | — | — | — |
| Pessoa | TTabSheet | contêiner | — | — | — | — | — |
| PnPessoa | TPanel | contêiner | — | — | — | — | — |
| Geral | TTabSheet | contêiner | — | — | — | — | — |
| lblTodosGeral | TLabel | rótulo | — | — | — | — | — |
| Panel2 | TPanel | contêiner | — | — | — | — | — |
| SBGrids | TSearchBox | outro | — | — | — | — | — |
| pnlOrdenacao | TPanel | contêiner | — | 4 | — | — | — |
| lbOrdenar | TLabel | rótulo | — | — | — | — | — |
| lbOrdem | TLabel | rótulo | — | — | — | — | — |
| cmbOrdenar | TComboBox | seleção | — | — | — | — | — |
| cmbOrdem | TComboBox | seleção | — | — | — | — | — |
| GbPeriodo | TGroupBox | contêiner |            Período | 0 | — | — | — |
| lblAte | TLabel | rótulo | Até | — | — | — | — |
| ImgPeriodo | TImage | outro | — | — | — | — | — |
| MEdDataInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdDataFim | TMaskEdit | campo de texto/data | — | 1 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdHoraFim | TMaskEdit | campo de texto/data | — | 2 | !99:99;1;  | 5 | Text=  :   |
| MEdHoraInicio | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| GbCardapio | TGroupBox | contêiner |            Cardápio | 1 | — | — | — |
| ImgCardapio | TImage | outro | — | — | — | — | — |
| LblCardapio | TLabel | rótulo | LblCardapio | — | — | — | — |
| BtnIrCardapios | TMetaEquipLocalizar | outro | — | — | — | — | — |
| EdCardapio | TEdit | campo de texto/data | — | 0 | — | — | — |
| ChkInconsistencias | TCheckBox | seleção | Apenas Inconsistências | 2 | — | — | — |
| GbColetor | TGroupBox | contêiner |            Coletor | 5 | — | — | — |
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
| CdsRelatorio | TClientDataSet | outro | — | — | — | — | — |
| CdsRelatorioIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioIdTipoRefeicao | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioIdCardapio | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioTipoRefeicao | TWideStringField | outro | — | — | — | — | — |
| CdsRelatorioValorRefeicao | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioNomePessoa | TStringField | outro | — | — | — | — | — |
| CdsRelatorioCardapio | TWideStringField | outro | — | — | — | — | — |
| CdsRelatorioDataHora | TDateTimeField | outro | — | — | — | — | — |
| CdsRelatorioColetor | TStringField | outro | — | — | — | — | — |
| CdsRelatorioCountReservaComConsumo | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioCountConsumoComReserva | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioCountReservaSemConsumo | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioCountConsumoSemReserva | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioValorReservaComConsumo | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioValorConsumoComReserva | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioValorReservaSemConsumo | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioValorConsumoSemConsumo | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioValorTotalReservaComConsumo | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioValorTotalConsumoComReserva | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioValorTotalReservaSemConsumo | TFloatField | outro | — | — | — | — | — |
| CdsRelatorioValorTotalConsumoSemReserva | TFloatField | outro | — | — | — | — | — |
| fxRelatorio | TfrxDBDataset | outro | — | — | — | — | — |
| frxRelatorio | TfrxReport | outro | — | — | — | — | — |
| Data | TfrxDataPage | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| MasterData1 | TfrxMasterData | outro | — | — | — | — | — |
| Shape4 | TfrxShapeView | outro | — | — | — | — | — |
| fxRelatorioNomePessoa | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioCardapio | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioIdTipoRefeicao | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioDataHora | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioColetor | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioValorRefeicao | TfrxMemoView | outro | — | — | — | — | — |
| Line1 | TfrxLineView | outro | — | — | — | — | — |
| Line2 | TfrxLineView | outro | — | — | — | — | — |
| Line4 | TfrxLineView | outro | — | — | — | — | — |
| Line3 | TfrxLineView | outro | — | — | — | — | — |
| Line5 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line13 | TfrxLineView | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Shape1 | TfrxShapeView | outro | — | — | — | — | — |
| Shape3 | TfrxShapeView | outro | — | — | — | — | — |
| MemoEmpresa | TfrxMemoView | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo6 | TfrxMemoView | outro | — | — | — | — | — |
| MemoNomeRelatorio | TfrxMemoView | outro | — | — | — | — | — |
| Memo3 | TfrxMemoView | outro | — | — | — | — | — |
| Memo4 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| Picture1 | TfrxPictureView | outro | — | — | — | — | — |
| Memo9 | TfrxMemoView | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| Memo1 | TfrxMemoView | outro | — | — | — | — | — |
| Memo2 | TfrxMemoView | outro | — | — | — | — | — |
| Memo14 | TfrxMemoView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Line6 | TfrxLineView | outro | — | — | — | — | — |
| Line7 | TfrxLineView | outro | — | — | — | — | — |
| Line8 | TfrxLineView | outro | — | — | — | — | — |
| Line9 | TfrxLineView | outro | — | — | — | — | — |
| Line10 | TfrxLineView | outro | — | — | — | — | — |
| Line11 | TfrxLineView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line15 | TfrxLineView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| Footer1 | TfrxFooter | outro | — | — | — | — | — |
| Shape2 | TfrxShapeView | outro | — | — | — | — | — |
| Memo15 | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioCountReservaComConsumo | TfrxMemoView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioCountReservaSemConsumo | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioCountConsumoSemReserva | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioValorTotalReservaSemConsumo | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioValorTotalConsumoSemReserva | TfrxMemoView | outro | — | — | — | — | — |
| fxRelatorioValorTotalReservaComConsumo | TfrxMemoView | outro | — | — | — | — | — |
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

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActRelatorioExecute` | 150 | — |
| `FormCreate` | 194 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 182: `Selecione um item para excluí-lo.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
