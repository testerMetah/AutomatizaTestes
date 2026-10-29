# Refeitório > Relatórios > Marcações OnLine...

> Inventário estático de `Acesso/UFrmRelMarcacoesOnline.dfm` e `Acesso/UFrmRelMarcacoesOnline.pas` no commit `28074dd`. Esta ficha combina inventário estático com notas de leitura manual das procedures; ainda requer conferência de controllers, DAOs e do build instalado.

- Form: `TFrmRelMarcacoesOnline`
- Abertura: `acRelMarcacoesOnlineExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FrmRelMarcacoesOnline` | `TFrmRelMarcacoesOnline` (herdado) | Relatório de Marcações Online | — | `—` | — | — | — |
| `PgRelatorio` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `TabDefinições` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Crachá` | `TLabel` | Crachá | — | `—` | — | — | — |
| `Situação` | `TLabel` | Situação | — | `—` | — | — | — |
| `Coleta` | `TLabel` | Coleta | — | `—` | — | — | — |
| `Sentido` | `TLabel` | Sentido | — | `—` | — | — | — |
| `Label2` | `TLabel` | Função | — | `—` | — | — | — |
| `Panel1` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `RgbSelecao` | `TRadioGroup` (herdado) | — | — | `—` | — | — | — |
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
| `pnlOrdenacao` | `TPanel` (herdado) | — | 7 | `—` | — | — | — |
| `lbOrdenar` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `lbOrdem` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `cmbOrdenar` | `TComboBox` (herdado) | — | — | `—` | — | — | — |
| `cmbOrdem` | `TComboBox` (herdado) | — | — | `—` | — | — | — |
| `GbPeriodo` | `TGroupBox` |            Período | 1 | `—` | — | — | — |
| `Até` | `TLabel` | Até | — | `—` | — | — | — |
| `MEdDataInicio` | `TMaskEdit` | — | 0 | `!99/99/9999;1; ` | 10 | Text=  /  /     | — |
| `MEdDataFim` | `TMaskEdit` | — | 1 | `!99/99/9999;1; ` | 10 | Text=  /  /     | — |
| `MEdHoraFim` | `TMaskEdit` | — | 2 | `!99:99;1; ` | 5 | Text=  :   | — |
| `MEdHoraInicio` | `TMaskEdit` | — | 3 | `!99:99;1; ` | 5 | Text=  :   | — |
| `ChkSepararDia` | `TCheckBox` | Repetir diariamente | 4 | `—` | — | — | — |
| `EdCracha` | `TEdit` | — | 2 | `—` | — | — | — |
| `CmbSituacao` | `TComboBox` | — | 3 | `—` | — | Text=Todos, ItemIndex=2 | — |
| `CmbColeta` | `TComboBox` | — | 4 | `—` | — | Text=Todos, ItemIndex=2 | — |
| `CmbSentido` | `TComboBox` | — | 5 | `—` | — | Text=Todos, ItemIndex=2 | — |
| `EdFuncao` | `TEdit` | — | 6 | `—` | — | — | — |
| `GbColetor` | `TGroupBox` |            Coletor | 8 | `—` | — | — | — |
| `BtnIrColetor` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `lbColetor` | `TListBox` | — | 0 | `—` | — | — | — |
| `btnExcluiFiltro` | `THoverSpeedButton` | Excluir | 1 | `—` | — | — | OnClick=btnExcluiFiltroClick |
| `Selecao` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Label1` | `TLabel` (herdado) | — | — | `—` | — | — | — |
| `PnBotao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `BtnImpressao` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
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

- Linha 147: `O período informado excede o limite de 3650 dias (10 anos).`
- Linha 216: `Selecione um item para excluí-lo.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActRelatorioExecute`
- `btnExcluiFiltroClick`

## Fluxo e regras identificados

O fluxo herdado de seleção, consulta, geração e fechamento está em [base_relatorio_padrao.md](base_relatorio_padrao.md). Salvar, Excluir e Cancelar de cadastro não se aplicam a este formulário.

- `ActRelatorioExecute` rejeita período com `DaysBetween > 3650` e mostra `O período informado excede o limite de 3650 dias (10 anos).`. **Dúvida:** chama `StrToDateTime` antes da validação que retornaria mensagem amigável; data malformada pode provocar exceção primeiro.
- Após validar o período, usa `ChkSepararDia`, múltiplos coletores (`GetIdsColetor`), coleta, situação, crachá, sentido, função, pré-cadastro (`True`), ordenação e ordem. Chama `ReceberDadosRelMarcacoesOnline` e a geração herdada.

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
