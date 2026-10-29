# Refeitório > Relatórios > Reservas de Refeições...

> Inventário estático de `Acesso/UFrmRelReservasRefeicoes.dfm` e `Acesso/UFrmRelReservasRefeicoes.pas` no commit `28074dd`. Esta ficha combina inventário estático com notas de leitura manual das procedures; ainda requer conferência de controllers, DAOs e do build instalado.

- Form: `TFrmRelReservasRefeicoes`
- Abertura: `acRefReservasRefeicoesExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FrmRelReservasRefeicoes` | `TFrmRelReservasRefeicoes` (herdado) | Relatório de Reservas de Refeições | — | `—` | — | — | — |
| `PgRelatorio` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `TabDefinições` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Panel1` | `TPanel` (herdado) | — | 3 | `—` | — | — | — |
| `PgSelecao` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `Filtros` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `PnGrupoAcesso` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `Setor` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `PnSetor` | `TPanel` (herdado) | — | — | `—` | — | — | — |
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
| `GbPeriodo` | `TGroupBox` |            Data De Início | 0 | `—` | — | — | — |
| `lblAte` | `TLabel` | Até | — | `—` | — | — | — |
| `MEdDataIni` | `TMaskEdit` | — | 0 | `!99/99/9999;1; ` | 10 | Text=  /  /     | — |
| `MEdDataFim` | `TMaskEdit` | — | 1 | `!99/99/9999;1; ` | 10 | Text=  /  /     | — |
| `GbSituacao` | `TGroupBox` |            Situação | 1 | `—` | — | — | — |
| `cbSituacao` | `TComboBox` | — | 0 | `—` | — | Text=Todos, ItemIndex=0 | — |
| `GbCardapio` | `TGroupBox` |            Cardápio | 2 | `—` | — | — | — |
| `mlCardapio` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `lblCardapio` | `TLabel` | lblCardapio | — | `—` | — | — | — |
| `EdCardapio` | `TEdit` | — | 0 | `—` | — | Visible=False | — |
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

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Nenhuma chamada com literal direto detectada.

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActRelatorioExecute`

## Fluxo e regras identificados

O fluxo herdado de seleção, consulta, geração e fechamento está em [base_relatorio_padrao.md](base_relatorio_padrao.md). Salvar, Excluir e Cancelar de cadastro não se aplicam a este formulário.

- `ActRelatorioExecute` valida `MEdDataIni` e `MEdDataFim` com horas fixas `00:00` e `23:59`, mostra a mensagem e aborta se falhar. Passa cardápio (`EdCardapio`), situação (`cbSituacao`), ordenação e ordem a `ReceberDadosRelReservasRefeicoes`; depois chama a geração herdada.
- `FormCreate` preenche as duas datas com o dia atual. O período do relatório é inclusivo até 23:59 do fim informado no form.

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
