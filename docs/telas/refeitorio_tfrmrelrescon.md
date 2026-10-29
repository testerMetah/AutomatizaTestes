# Refeitório > Relatórios > Reservas e Consumos...

> Inventário estático de `Acesso/UFrmRelResCon.dfm` e `Acesso/UFrmRelResCon.pas` no commit `28074dd`. Esta ficha combina inventário estático com notas de leitura manual das procedures; ainda requer conferência de controllers, DAOs e do build instalado.

- Form: `TFrmRelResCon`
- Abertura: `acRelReservasConsumosExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FrmRelResCon` | `TFrmRelResCon` (herdado) | Relatório de Reservas e Consumos | — | `—` | — | — | — |
| `PgRelatorio` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `TabDefinições` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Panel1` | `TPanel` (herdado) | — | 3 | `—` | — | — | — |
| `RgbSelecao` | `TRadioGroup` (herdado) | — | — | `—` | — | — | — |
| `PgSelecao` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `Filtros` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `PnGrupoAcesso` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `Setor` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `PnSetor` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `DBGridSetor` | `TDBGrid` (herdado) | — | — | `—` | — | — | — |
| `Pessoa` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `PnPessoa` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `Geral` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `lblTodosGeral` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `Panel2` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `SBGrids` | `TSearchBox` (herdado) | — | — | `—` | — | — | — |
| `pnlOrdenacao` | `TPanel` (herdado) | — | 4 | `—` | — | — | — |
| `lbOrdenar` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `lbOrdem` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `cmbOrdenar` | `TComboBox` (herdado) | — | — | `—` | — | — | — |
| `cmbOrdem` | `TComboBox` (herdado) | — | — | `—` | — | — | — |
| `GbPeriodo` | `TGroupBox` |            Período | 0 | `—` | — | — | — |
| `lblAte` | `TLabel` | Até | — | `—` | — | — | — |
| `MEdDataInicio` | `TMaskEdit` | — | 0 | `!99/99/9999;1; ` | 10 | Text=  /  /     | — |
| `MEdDataFim` | `TMaskEdit` | — | 1 | `!99/99/9999;1; ` | 10 | Text=  /  /     | — |
| `MEdHoraFim` | `TMaskEdit` | — | 2 | `!99:99;1; ` | 5 | Text=  :   | — |
| `MEdHoraInicio` | `TMaskEdit` | — | 3 | `!99:99;1; ` | 5 | Text=  :   | — |
| `GbCardapio` | `TGroupBox` |            Cardápio | 1 | `—` | — | — | — |
| `LblCardapio` | `TLabel` | LblCardapio | — | `—` | — | — | — |
| `BtnIrCardapios` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `EdCardapio` | `TEdit` | — | 0 | `—` | — | — | — |
| `ChkInconsistencias` | `TCheckBox` | Apenas Inconsistências | 2 | `—` | — | — | — |
| `GbColetor` | `TGroupBox` |            Coletor | 5 | `—` | — | — | — |
| `BtnIrColetor` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `lbColetor` | `TListBox` | — | 0 | `—` | — | — | — |
| `btnExcluiFiltro` | `THoverSpeedButton` | Excluir | 1 | `—` | — | — | OnClick=btnExcluiFiltroClick |
| `Selecao` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Label1` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `PnBotao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `BtnImpressao` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `frxPDFExport1` | `TfrxPDFExport` (herdado) | — | — | `—` | — | — | — |
| `ActionList1` | `TActionList` (herdado) | — | — | `—` | — | — | — |
| `CdsRelatorioTipoRefeicao` | `TWideStringField` | — | — | `—` | — | — | — |
| `CdsRelatorioCardapio` | `TWideStringField` | — | — | `—` | — | — | — |
| `fxRelatorio` | `TfrxDBDataset` | — | — | `—` | — | — | — |
| `frxRelatorio` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `MasterData1` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Shape4` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `fxRelatorioNomePessoa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioCardapio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioIdTipoRefeicao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioDataHora` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioColetor` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioValorRefeicao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line1` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line2` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line4` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line3` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line5` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line13` | `TfrxLineView` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `MemoEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo9` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo20` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo1` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo2` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo14` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo19` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line6` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line7` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line8` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line9` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line10` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line11` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line15` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Footer1` | `TfrxFooter` | — | — | `—` | — | — | — |
| `Shape2` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Memo15` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioCountReservaComConsumo` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo17` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo18` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioCountReservaSemConsumo` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioCountConsumoSemReserva` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioValorTotalReservaSemConsumo` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioValorTotalConsumoSemReserva` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `fxRelatorioValorTotalReservaComConsumo` | `TfrxMemoView` | — | — | `—` | — | — | — |
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

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 182: `Selecione um item para excluí-lo.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActFecharExecute`
- `ActRelatorioExecute`
- `btnExcluiFiltroClick`

## Fluxo e regras identificados

O fluxo herdado de seleção, consulta, geração e fechamento está em [base_relatorio_padrao.md](base_relatorio_padrao.md). Salvar, Excluir e Cancelar de cadastro não se aplicam a este formulário.

- `ActRelatorioExecute` valida data/hora inicial e final com `ValidaCamposDataHoraIniFim`; em erro mostra a mensagem retornada e aborta. Depois usa múltiplos coletores de `GetIdsColetor`, código de `EdCardapio`, `ChkInconsistencias`, ordenação e ordem. Chama `ReceberDadosRelResCon` e a geração herdada.
- `btnExcluiFiltroClick` mostra `Selecione um item para excluí-lo.` quando `lbColetor` não está focado; caso contrário remove o item selecionado.

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
