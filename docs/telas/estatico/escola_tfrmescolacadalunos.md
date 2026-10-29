# Escola: TFrmEscolaCadAlunos

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Alunos....

- DFM: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Alunos.dfm`
- PAS: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Alunos.pas`
- Handler de abertura: `actAlunosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaCadAlunos | TFrmEscolaCadAlunos | outro | Cadastro de Alunos | — | — | — | — |
| Shape3 | TShape | outro | — | — | — | — | — |
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
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| pgAluno | TPageControl | contêiner | — | 1 | — | — | — |
| TabGerais | TTabSheet | contêiner | Dados Gerais | — | — | — | — |
| Nome | TLabel | rótulo | Nome: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Nascimento: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| Image6 | TImage | outro | — | — | — | — | — |
| Label2 | TLabel | rótulo | Email: | — | — | — | — |
| Label3 | TLabel | rótulo | Situação: | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| Label4 | TLabel | rótulo | Sexo: | — | — | — | — |
| Label5 | TLabel | rótulo | CPF: | — | — | — | — |
| imgFalse | TImage | outro | — | — | — | — | Visible=False |
| imgTrue | TImage | outro | — | — | — | — | Visible=False |
| edtNome | TEdit | campo de texto/data | — | 1 | — | — | — |
| mskNascimento | TMaskEdit | campo de texto/data | — | 3 | !99/99/0000;1;  | 10 | Text=  /  /     |
| edtEmail | TEdit | campo de texto/data | — | 2 | — | — | — |
| cmbSituacao | TComboBox | seleção | — | 0 | — | — | Text=Ativo, ItemIndex=0 |
| cmbSexo | TComboBox | seleção | — | 4 | — | — | — |
| gbxCrachasAlunos | TGroupBox | contêiner | Crachás | 6 | — | — | — |
| Label12 | TLabel | rótulo | Crachá Fixo: | — | — | — | — |
| Label13 | TLabel | rótulo | Crachá Provisório: | — | — | — | — |
| lblFixo | TLabel | rótulo | Cadastrar Crachá Fixo... | — | — | — | — |
| lblProvisorio | TLabel | rótulo | Cadastrar Crachá Provisório... | — | — | — | — |
| Image14 | TImage | outro | — | — | — | — | — |
| Image15 | TImage | outro | — | — | — | — | — |
| gbxDigitaisFaces | TGroupBox | contêiner | Digitais/Faces | 7 | — | — | — |
| lblFace | TLabel | rótulo | lblFace | — | — | — | — |
| lblDigital | TLabel | rótulo | lblDigital | — | — | — | — |
| imgFaceCheck | TImage | outro | — | — | — | — | — |
| imgDigitalCheck | TImage | outro | — | — | — | — | — |
| btnFace | THoverSpeedButton | ação | Cadastrar Face | 0 | — | — | — |
| btnDigital | THoverSpeedButton | ação | Cadastrar Digital | 1 | — | — | — |
| edtCpf | TEdit | campo de texto/data | — | 5 | — | — | — |
| TabAluno | TTabSheet | contêiner | Dados do Aluno | — | — | — | — |
| Image7 | TImage | outro | — | — | — | — | — |
| Label6 | TLabel | rótulo | Data de Matrícula: | — | — | — | — |
| Image8 | TImage | outro | — | — | — | — | — |
| Label7 | TLabel | rótulo | Série/Ano: | — | — | — | — |
| Image10 | TImage | outro | — | — | — | — | — |
| Label8 | TLabel | rótulo | Nível de Ensino: | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| Label9 | TLabel | rótulo | Matrícula: | — | — | — | — |
| Image12 | TImage | outro | — | — | — | — | — |
| Label10 | TLabel | rótulo | Observações: | — | — | — | — |
| Image16 | TImage | outro | — | — | — | — | — |
| Label14 | TLabel | rótulo | Turma: | — | — | — | — |
| mlTurma | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblTurma | TLabel | rótulo | lblTurma | — | — | — | — |
| mskDataMatricula | TMaskEdit | campo de texto/data | — | 1 | !99/99/0000;1;  | 10 | Text=  /  /     |
| cmbSerie | TComboBox | seleção | — | 3 | — | — | — |
| cmbEnsino | TComboBox | seleção | — | 2 | — | — | — |
| edtMatricula | TEdit | campo de texto/data | — | 0 | — | 9 | — |
| memObservacoes | TMemo | outro | — | 5 | — | — | — |
| edtTurma | TEdit | campo de texto/data | — | 4 | — | — | — |
| TabResponsavel | TTabSheet | contêiner | Responsáveis | — | — | — | — |
| dbgResponsaveis | TDBGrid | grade | — | 0 | — | — | — |
| Panel1 | TPanel | contêiner | — | 1 | — | — | — |
| Image13 | TImage | outro | — | — | — | — | — |
| Label11 | TLabel | rótulo | Responsáveis: | — | — | — | — |
| mlResponsaveis | TMetaEquipLocalizar | outro | — | — | — | — | — |
| btnNovoResponsavel | THoverSpeedButton | ação | Cadastrar novo Responsavel | 0 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActExcluirResponsavel | TAction | ação | Excluir | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| cdsAlunos | TClientDataSet | outro | — | — | — | — | — |
| cdsAlunosid | TIntegerField | outro | — | — | — | — | — |
| cdsAlunosnome | TStringField | outro | — | — | — | — | — |
| cdsAlunossituacao | TStringField | outro | — | — | — | — | — |
| cdsResponsaveis | TClientDataSet | outro | — | — | — | — | — |
| dsResponsaveis | TDataSource | outro | — | — | — | — | — |
| dsAlunos | TDataSource | outro | — | — | — | — | — |
| PopupMenu1 | TPopupMenu | outro | — | — | — | — | — |
| Action11 | TMenuItem | outro | — | — | — | — | — |
| EscolaIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `GravaCampos` | 151 | `TAlunosController.Create`, `AlunosController.SetConexao`, `AlunosController.Inserir`, `AlunosController.Atualizar` |
| `ValidarCampos` | 389 | `TAlunosController.Create`, `AlunosController.SetConexao`, `AlunosController.ExisteAlunoCpf`, `AlunosController.ExisteAlunoMatricula` |
| `FormCreate` | 746 | — |
| `ActExcluirExecute` | 793 | `TAlunosController.Create`, `FAlunosController.SetConexao`, `FAlunosController.Excluir` |
| `ActExibirTudoExecute` | 843 | `TAlunosController.Create`, `AlunosController.SetConexao`, `AlunosController.GetAlunosTodos` |
| `ActIncluirExecute` | 874 | — |
| `ActSalvarExecute` | 881 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 403: `É necessário informar o Nome.`
- Linha 411: `É necessário informar a Data de Nascimento.`
- Linha 418: `Data de Nascimento inválida.`
- Linha 426: `É necessário informar o Sexo do(a) aluno(a).`
- Linha 436: `CPF Inválido.`
- Linha 448: `CPF já existe.`
- Linha 467: `Matrícula já existe.`
- Linha 475: `É necessário informar a Matrícula do(a) aluno(a).`
- Linha 804: `Excluir o registro?`
- Linha 822: `Problemas com a exclusão no Banco de Dados!`
- Linha 984: `Turma não encontrada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
