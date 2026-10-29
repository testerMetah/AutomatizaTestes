# Escola: TFrmEscolaCadTurnos

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Turnos....

- DFM: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Turnos.dfm`
- PAS: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Turnos.pas`
- Handler de abertura: `actTurnosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaCadTurnos | TFrmEscolaCadTurnos | outro | Cadastro de Turnos | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| Label2 | TLabel | rótulo | Situação: | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| edtNome | TEdit | campo de texto/data | — | 1 | — | — | — |
| cmbSituacao | TComboBox | seleção | — | 2 | — | — | Text=Ativo, ItemIndex=0 |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| cdsTurnos | TClientDataSet | outro | — | — | — | — | — |
| cdsTurnosid | TIntegerField | outro | — | — | — | — | — |
| cdsTurnosnome | TStringField | outro | — | — | — | — | — |
| cdsTurnossituacao | TStringField | outro | — | — | — | — | — |
| dsTurnos | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 50 | — |
| `GravaCampos` | 68 | `TTurnosController.Create`, `TurnosController.SetConexao`, `TurnosController.Inserir`, `TurnosController.Atualizar` |
| `ValidarCampos` | 157 | — |
| `ActExcluirExecute` | 182 | `TTurnosController.Create`, `FTurnosController.SetConexao`, `FTurnosController.Excluir` |
| `ActExibirTudoExecute` | 215 | `TTurnosController.Create`, `TurnosController.SetConexao`, `TurnosController.GetTurnosTodos` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 161: `Nome é obrigatório.`
- Linha 170: `Situação inválida.`
- Linha 193: `Excluir o registro?`
- Linha 203: `Problemas com a exclusão no Banco de Dados!`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
