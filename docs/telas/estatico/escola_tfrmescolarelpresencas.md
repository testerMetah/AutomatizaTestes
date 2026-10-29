# Escola: TFrmEscolaRelPresencas

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Relatórios > Relatório de Presenças.

- DFM: `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Presencas.dfm`
- PAS: `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Presencas.pas`
- Handler de abertura: `actRelatorioPresencasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaRelPresencas | TFrmEscolaRelPresencas | outro | Relatório de Presenças | — | — | — | — |
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
| pnlOrdenacao | TPanel | contêiner | — | — | — | — | — |
| lbOrdenar | TLabel | rótulo | — | — | — | — | — |
| lbOrdem | TLabel | rótulo | — | — | — | — | — |
| cmbOrdenar | TComboBox | seleção | — | — | — | — | — |
| cmbOrdem | TComboBox | seleção | — | — | — | — | — |
| GbPeriodo | TGroupBox | contêiner |            Período | 2 | — | — | — |
| Até | TLabel | rótulo | Até | — | — | — | — |
| ImgPeriodo | TImage | outro | — | — | — | — | — |
| MEdDataInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdDataFim | TMaskEdit | campo de texto/data | — | 1 | !99/99/9999;1;  | 10 | Text=  /  /     |
| GbPessoas | TGroupBox | contêiner |            Presença | 3 | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| CmbPresenca | TComboBox | seleção | — | 0 | — | — | Text=Todos, ItemIndex=0 |
| GbAfastamentos | TGroupBox | contêiner |            Afastamentos | 4 | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| ChkAfastamentos | TCheckBox | seleção | Exibir afastamentos | 0 | — | — | Checked=True |
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

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActRelatorioExecute` | 48 | — |
| `FormCreate` | 110 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 57: `Data de Inicio inválida.`
- Linha 64: `Data de Término inválida.`
- Linha 71: `Data de Término não pode ser menor que a Data de Inicio.`
- Linha 78: `Tipo de presença inválida.`
- Linha 84: `Opção de Ordenação inválida.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
