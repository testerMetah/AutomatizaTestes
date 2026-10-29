# Escola: TFrmEscolaCadTurmas

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Turmas....

- DFM: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Turmas.dfm`
- PAS: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Turmas.pas`
- Handler de abertura: `actTurmasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaCadTurmas | TFrmEscolaCadTurmas | outro | Cadastro de Turmas | — | — | — | — |
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
| Label2 | TLabel | rótulo | Situação: | — | — | — | — |
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| Label3 | TLabel | rótulo | Turno: | — | — | — | — |
| mlTurno | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblTurno | TLabel | rótulo | lblTurno | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| cmbSituacao | TComboBox | seleção | — | 1 | — | — | — |
| edtNome | TEdit | campo de texto/data | — | 2 | — | — | — |
| edtTurno | TEdit | campo de texto/data | — | 3 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| cdsTurmas | TClientDataSet | outro | — | — | — | — | — |
| cdsTurmasid | TIntegerField | outro | — | — | — | — | — |
| cdsTurmasnome | TStringField | outro | — | — | — | — | — |
| cdsTurmassituacao | TStringField | outro | — | — | — | — | — |
| dsTurmas | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `GravaCampos` | 58 | `TTurmasController.Create`, `TurmasController.SetConexao`, `TurmasController.Inserir`, `TurmasController.Atualizar` |
| `ActExcluirExecute` | 109 | `TTurmasController.Create`, `FTurmasController.SetConexao`, `FTurmasController.Excluir` |
| `ActExibirTudoExecute` | 142 | `TTurmasController.Create`, `TurmasController.SetConexao`, `TurmasController.GetTurmasTodos` |
| `ValidarCampos` | 204 | — |
| `FormCreate` | 271 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 120: `Excluir o registro?`
- Linha 130: `Problemas com a exclusão no Banco de Dados!`
- Linha 208: `Nome é obrigatório.`
- Linha 217: `Situação inválida.`
- Linha 226: `Turno é obrigatório.`
- Linha 257: `Turno não encontrado.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
