# Escola: TFrmEscolaRelMarcacoesOnline

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Relatórios > Relatório de Marcações Online.

- DFM: `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.MarcacoesOnline.dfm`
- PAS: `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.MarcacoesOnline.pas`
- Handler de abertura: `actRelatorioMarcacoesOnlineExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaRelMarcacoesOnline | TFrmEscolaRelMarcacoesOnline | outro | Relatório de Marcações Online | — | — | — | — |
| PgRelatorio | TPageControl | contêiner | — | — | — | — | — |
| TabDefinições | TTabSheet | contêiner | — | — | — | — | — |
| Crachá | TLabel | rótulo | Crachá | — | — | — | — |
| Label2 | TLabel | rótulo | Função | — | — | — | — |
| Situação | TLabel | rótulo | Situação | — | — | — | — |
| Coleta | TLabel | rótulo | Coleta | — | — | — | — |
| Sentido | TLabel | rótulo | Sentido | — | — | — | — |
| Panel1 | TPanel | contêiner | — | — | — | — | — |
| PgSelecao | TPageControl | contêiner | — | — | — | — | — |
| Geral | TTabSheet | contêiner | — | — | — | — | — |
| lblTodosGeral | TLabel | rótulo | — | — | — | — | — |
| Aluno | TTabSheet | contêiner | — | — | — | — | — |
| PnAluno | TPanel | contêiner | — | — | — | — | — |
| Responsavel | TTabSheet | contêiner | — | — | — | — | — |
| Panel3 | TPanel | contêiner | — | — | — | — | — |
| Pessoa | TTabSheet | contêiner | — | — | — | — | — |
| PnPessoa | TPanel | contêiner | — | — | — | — | — |
| Turma | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| Turno | TTabSheet | contêiner | — | — | — | — | — |
| Panel5 | TPanel | contêiner | — | — | — | — | — |
| Panel2 | TPanel | contêiner | — | — | — | — | — |
| SBGrids | TSearchBox | outro | — | — | — | — | — |
| RgbSelecao | TRadioGroup | seleção | — | — | — | — | — |
| pnlOrdenacao | TPanel | contêiner | — | — | — | — | — |
| lbOrdenar | TLabel | rótulo | — | — | — | — | — |
| lbOrdem | TLabel | rótulo | — | — | — | — | — |
| cmbOrdenar | TComboBox | seleção | — | — | — | — | — |
| cmbOrdem | TComboBox | seleção | — | — | — | — | — |
| EdFuncao | TEdit | campo de texto/data | — | 2 | — | — | — |
| EdCracha | TEdit | campo de texto/data | — | 3 | — | — | — |
| CmbSituacao | TComboBox | seleção | — | 4 | — | — | Text=Todos, ItemIndex=2 |
| CmbColeta | TComboBox | seleção | — | 5 | — | — | Text=Todos, ItemIndex=2 |
| CmbSentido | TComboBox | seleção | — | 6 | — | — | Text=Todos, ItemIndex=2 |
| GbPeriodo | TGroupBox | contêiner |            Período | 7 | — | — | — |
| Até | TLabel | rótulo | Até | — | — | — | — |
| ImgPeriodo | TImage | outro | — | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| MEdDataInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdDataFim | TMaskEdit | campo de texto/data | — | 1 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdHoraFim | TMaskEdit | campo de texto/data | — | 2 | !99:99;1;  | 5 | Text=  :   |
| MEdHoraInicio | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| ChkSepararDia | TCheckBox | seleção | Repetir diariamente | 4 | — | — | — |
| GbColetor | TGroupBox | contêiner |            Coletor | 8 | — | — | — |
| BtnIrColetor | TMetaEquipLocalizar | outro | — | — | — | — | — |
| ImgColetor | TImage | outro | — | — | — | — | — |
| lbColetor | TListBox | seleção | — | 0 | — | — | — |
| btnExcluiFiltro | THoverSpeedButton | ação | Excluir | 1 | — | — | — |
| Selecao | TTabSheet | contêiner | — | — | — | — | — |
| Label1 | TLabel | rótulo | — | — | — | — | — |
| PnBotao | TPanel | contêiner | — | — | — | — | — |
| BtnImpressao | THoverSpeedButton | ação | — | — | — | — | — |
| frxRelPresenca | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| Cabecalho | TfrxHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelInconsistencias | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| Cabecalho | TfrxHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelAlunos | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| Cabecalho | TfrxHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelPessoas | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| Cabecalho | TfrxHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelResponsaveis | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| Cabecalho | TfrxHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelCracha | TfrxReport | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelMarcacoesOnline | TfrxReport | outro | — | — | — | — | — |
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
| `ActRelatorioExecute` | 93 | — |
| `FormCreate` | 208 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 109: `O período informado excede o limite de 3650 dias (10 anos).`
- Linha 115: `Data de Inicio é inválida.`
- Linha 122: `Data de Término é inválida.`
- Linha 129: `Horário de Inicio é inválido.`
- Linha 136: `Horário de Término é inválido.`
- Linha 143: `Situação inválida.`
- Linha 149: `Tipo de Coleta inválida.`
- Linha 155: `Sentido inválido.`
- Linha 161: `Opção de Ordenação inválida.`
- Linha 193: `Selecione um item para excluí-lo.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
