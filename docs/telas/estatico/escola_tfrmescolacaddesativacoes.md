# Escola: TFrmEscolaCadDesativacoes

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Desativações|Ativações....

- DFM: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Desativacoes.dfm`
- PAS: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Desativacoes.pas`
- Handler de abertura: `actDesativacoesExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaCadDesativacoes | TFrmEscolaCadDesativacoes | outro | Desativações \| Ativações | — | — | — | Visible=True |
| ImgBotao | TImage | outro | — | — | — | — | — |
| Panel1 | TPanel | contêiner | — | 0 | — | — | — |
| PnGrupoAcesso | TPanel | contêiner | — | 0 | — | — | — |
| AdicionaFiltro | TSpeedButton | ação | — | — | — | — | — |
| RemoveFiltro | TSpeedButton | ação | — | — | — | — | — |
| Label1 | TLabel | rótulo | Ativos | — | — | — | — |
| Label2 | TLabel | rótulo | Inativos | — | — | — | — |
| GridItens | TDBGrid | grade | — | 0 | — | — | Visible=True |
| GridItens2 | TDBGrid | grade | — | 1 | — | — | Visible=True |
| pnlFundoTopPadrao | TPanel | contêiner | — | 1 | — | — | — |
| edBusca | TEdit | campo de texto/data | — | 0 | — | — | — |
| edBusca2 | TEdit | campo de texto/data | — | 1 | — | — | — |
| pnlFundoBotPadrao | TPanel | contêiner | — | 2 | — | — | — |
| BtnFechar | THoverSpeedButton | ação | Fechar (Ctrl+F4) | 0 | — | — | — |
| Panel2 | TPanel | contêiner | — | 1 | — | — | — |
| cmbSelecao | TComboBox | seleção | — | 0 | — | — | Text=Alunos, ItemIndex=0 |
| CdsConsulta | TClientDataSet | outro | — | — | — | — | — |
| CdsConsultaSELECAO | TBooleanField | outro | — | — | — | — | — |
| CdsConsultaID | TIntegerField | outro | — | — | — | — | — |
| CdsConsultaNOME | TStringField | outro | — | — | — | — | — |
| CdsConsulta2 | TClientDataSet | outro | — | — | — | — | — |
| CdsConsulta2SELECAO | TBooleanField | outro | — | — | — | — | — |
| CdsConsulta2ID | TIntegerField | outro | — | — | — | — | — |
| CdsConsulta2NOME | TStringField | outro | — | — | — | — | — |
| GridIcons | TImageList | outro | — | — | — | — | — |
| DsConsulta | TDataSource | outro | — | — | — | — | — |
| DsConsulta2 | TDataSource | outro | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActFechar | TAction | ação | Fechar (Ctrl+F4) | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 108 | `TPessoasController.Create`, `FPessoasController.SetConexao`, `TAlunosController.Create`, `FAlunosController.SetConexao`, `TResponsaveisController.Create`, `FResponsaveisController.SetConexao` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 535: `Erro ao inativar pessoa: `
- Linha 556: `Erro ao ativar pessoa: `
- Linha 590: `Erro ao inativar aluno: `
- Linha 619: `Erro ao ativar aluno: `
- Linha 661: `Erro ao inativar respons�vel: `
- Linha 703: `Erro ao ativar respons�vel: `

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
