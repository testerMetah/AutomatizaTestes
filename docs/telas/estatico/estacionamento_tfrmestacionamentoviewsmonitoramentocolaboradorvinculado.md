# Estacionamento: TFrmEstacionamentoViewsMonitoramentoColaboradorVinculado

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Relatórios > Colaborador Vinculado Estacionamento.

- DFM: `Estacionamento/Views/Relatorio/Acessus.Estacionamento.Views.Relatorio.ColaboradorVinculado.dfm`
- PAS: `Estacionamento/Views/Relatorio/Acessus.Estacionamento.Views.Relatorio.ColaboradorVinculado.pas`
- Handler de abertura: `actRelColaboradorVinculadoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEstacionamentoViewsMonitoramentoColaboradorVinculado | TFrmEstacionamentoViewsMonitoramentoColaboradorVinculado | outro | Colaborador Vinculado ao Estacionamento | — | — | — | — |
| PgRelatorio | TPageControl | contêiner | — | — | — | — | — |
| TabDefinições | TTabSheet | contêiner | — | — | — | — | — |
| Panel1 | TPanel | contêiner | — | 2 | — | — | Enabled=False |
| PgSelecao | TPageControl | contêiner | — | — | — | — | — |
| Filtros | TTabSheet | contêiner | — | — | — | — | — |
| PnGrupoAcesso | TPanel | contêiner | — | — | — | — | — |
| Setor | TTabSheet | contêiner | — | — | — | — | — |
| PnSetor | TPanel | contêiner | — | — | — | — | — |
| Pessoa | TTabSheet | contêiner | — | — | — | — | — |
| PnPessoa | TPanel | contêiner | — | — | — | — | — |
| Geral | TTabSheet | contêiner | — | — | — | — | — |
| lblTodosGeral | TLabel | rótulo | — | — | — | — | — |
| Panel2 | TPanel | contêiner | — | — | — | — | — |
| SBGrids | TSearchBox | outro | — | — | — | — | — |
| pnlOrdenacao | TPanel | contêiner | — | — | — | — | — |
| lbOrdenar | TLabel | rótulo | — | — | — | — | — |
| lbOrdem | TLabel | rótulo | — | — | — | — | — |
| cmbOrdenar | TComboBox | seleção | — | — | — | — | — |
| cmbOrdem | TComboBox | seleção | — | — | — | — | — |
| GbCardapio | TGroupBox | contêiner |            Estacionamento | 0 | — | — | — |
| LblEstacionamento | TLabel | rótulo | LblEstacionamento | — | — | — | — |
| BtnIrVeiculo | TMetaEquipLocalizar | outro | — | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| EdEstacionamento | TEdit | campo de texto/data | — | 0 | — | — | — |
| Selecao | TTabSheet | contêiner | — | — | — | — | — |
| Label1 | TLabel | rótulo | — | — | — | — | — |
| PnBotao | TPanel | contêiner | — | — | — | — | — |
| BtnImpressao | THoverSpeedButton | ação | — | — | — | — | — |
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
| CdsRelatorio | TClientDataSet | outro | — | — | — | — | — |
| CdsRelatorioIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioNomePessoa | TStringField | outro | — | — | — | — | — |
| CdsRelatorioIdEstacionamento | TIntegerField | outro | — | — | — | — | — |
| CdsRelatorioNomeEstacionamento | TStringField | outro | — | — | — | — | — |
| fxRelatorio | TfrxDBDataset | outro | — | — | — | — | — |
| frxRelatorio | TfrxReport | outro | — | — | — | — | — |
| Data | TfrxDataPage | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| MasterData1 | TfrxMasterData | outro | — | — | — | — | — |
| fxRelatorioNome | TfrxMemoView | outro | — | — | — | — | — |
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
| Memo1 | TfrxMemoView | outro | — | — | — | — | — |
| Line11 | TfrxLineView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line15 | TfrxLineView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| GroupHeader1 | TfrxGroupHeader | outro | — | — | — | — | — |
| Shape2 | TfrxShapeView | outro | — | — | — | — | — |
| Memo23 | TfrxMemoView | outro | — | — | — | — | — |
| Memo7 | TfrxMemoView | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActRelatorioExecute` | 106 | — |
| `FormCreate` | 128 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Nenhum literal simples encontrado.

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
