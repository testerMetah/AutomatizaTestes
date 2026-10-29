# Acesso: TFrmRelPreCadastro

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Relatórios > Operacional > Pré-cadastro....

- DFM: `Acesso/UFrmRelPreCadastro.dfm`
- PAS: `Acesso/UFrmRelPreCadastro.pas`
- Handler de abertura: `acRelOperacionalPreCadastroExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmRelPreCadastro | TFrmRelPreCadastro | outro | Relatório de Pré-cadastros | — | — | — | — |
| PgRelatorio | TPageControl | contêiner | — | — | — | — | — |
| TabDefinições | TTabSheet | contêiner | — | — | — | — | — |
| Panel1 | TPanel | contêiner | — | 2 | — | — | — |
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
| pnlOrdenacao | TPanel | contêiner | — | 3 | — | — | — |
| lbOrdenar | TLabel | rótulo | — | — | — | — | — |
| lbOrdem | TLabel | rótulo | — | — | — | — | — |
| cmbOrdenar | TComboBox | seleção | — | — | — | — | — |
| cmbOrdem | TComboBox | seleção | — | — | — | — | — |
| GbCracha | TGroupBox | contêiner |            Crachá | 0 | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| EdCracha | TEdit | campo de texto/data | — | 0 | — | 14 | — |
| GbStatus | TGroupBox | contêiner |            Status | 1 | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| CmbStatus | TComboBox | seleção | — | 0 | — | — | Text=Todos, ItemIndex=0 |
| Selecao | TTabSheet | contêiner | — | — | — | — | — |
| Label1 | TLabel | rótulo | — | — | — | — | — |
| PnBotao | TPanel | contêiner | — | — | — | — | — |
| BtnImpressao | THoverSpeedButton | ação | — | — | — | — | — |
| frxPDFExport1 | TfrxPDFExport | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
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

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActRelatorioExecute` | 83 | — |
| `FormCreate` | 108 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Nenhum literal simples encontrado.

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
