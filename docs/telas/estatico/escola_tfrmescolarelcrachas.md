# Escola: TFrmEscolaRelCrachas

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Relatórios > Relatório de Crachás.

- DFM: `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Crachas.dfm`
- PAS: `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Crachas.pas`
- Handler de abertura: `actRelatorioCrachasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaRelCrachas | TFrmEscolaRelCrachas | outro | Relatório de Crachás | — | — | — | — |
| PgRelatorio | TPageControl | contêiner | — | — | — | — | — |
| TabDefinições | TTabSheet | contêiner | — | — | — | — | — |
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
| GbTipoUso | TGroupBox | contêiner |            Tipo de uso | 2 | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| cmbTipoUso | TComboBox | seleção | — | 0 | — | — | Text=Todos, ItemIndex=0 |
| GbTipoCracha | TGroupBox | contêiner |            Tipo de crachá | 3 | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| ChkFixo | TCheckBox | seleção | Fixo | 0 | — | — | — |
| ChkProvisorio | TCheckBox | seleção | Provisório | 1 | — | — | — |
| ChkMestre | TCheckBox | seleção | Mestre | 2 | — | — | — |
| GbPeriodo | TGroupBox | contêiner |            Período de registro | 4 | — | — | — |
| LblAte | TLabel | rótulo | Até | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| MEdDataInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdDataFim | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdHoraFim | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| MEdHoraInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| gbVinculo | TGroupBox | contêiner |            Vínculo | 5 | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| cmbVinculo | TComboBox | seleção | — | 0 | — | — | Text=Apenas Não Vinculados, ItemIndex=2 |
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

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActRelatorioExecute` | 54 | — |
| `FormCreate` | 158 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 69: `Data de Inicio inválida.`
- Linha 76: `Data de Término inválida.`
- Linha 83: `Horario de Inicio inválido.`
- Linha 90: `Horario de Término inválido.`
- Linha 97: `Tipo de Uso inválido.`
- Linha 103: `Opção de Vínculo inválido.`
- Linha 109: `Opção de Ordenação inválida.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
