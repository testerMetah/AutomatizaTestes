# Escola: TFrmEscolaCadResponsaveis

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Responsáveis....

- DFM: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Responsaveis.dfm`
- PAS: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Responsaveis.pas`
- Handler de abertura: `actResponsaveisExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaCadResponsaveis | TFrmEscolaCadResponsaveis | outro | Cadastro de Responsáveis | — | — | — | — |
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
| pgResponsaveis | TPageControl | contêiner | — | 1 | — | — | — |
| TabGerais | TTabSheet | contêiner | Dados Gerais | — | — | — | — |
| Nome | TLabel | rótulo | Nome: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Nascimento: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| Image6 | TImage | outro | — | — | — | — | — |
| Label2 | TLabel | rótulo | Email: | — | — | — | — |
| Label4 | TLabel | rótulo | Sexo: | — | — | — | — |
| Label5 | TLabel | rótulo | Cpf: | — | — | — | — |
| Label3 | TLabel | rótulo | Situação: | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| imgFalse | TImage | outro | — | — | — | — | Visible=False |
| imgTrue | TImage | outro | — | — | — | — | Visible=False |
| edtNome | TEdit | campo de texto/data | — | 1 | — | — | — |
| mskNascimento | TMaskEdit | campo de texto/data | — | 3 | !99/99/0000;1;  | 10 | Text=  /  /     |
| edtEmail | TEdit | campo de texto/data | — | 2 | — | — | — |
| cmbSexo | TComboBox | seleção | — | 4 | — | — | — |
| edtCpf | TEdit | campo de texto/data | — | 5 | — | — | — |
| cmbSituacao | TComboBox | seleção | — | 0 | — | — | Text=Ativo, ItemIndex=0 |
| gbxCrachas | TGroupBox | contêiner | Crachás | 6 | — | — | — |
| Label6 | TLabel | rótulo | Crachá Fixo: | — | — | — | — |
| Label7 | TLabel | rótulo | Crachá Provisório: | — | — | — | — |
| lblFixo | TLabel | rótulo | Cadastrar Crachá Fixo... | — | — | — | — |
| lblProvisorio | TLabel | rótulo | Cadastrar Crachá Provisório... | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Image7 | TImage | outro | — | — | — | — | — |
| gbxDigitaisFaces | TGroupBox | contêiner | Digitais/Faces | 7 | — | — | — |
| lblFace | TLabel | rótulo | lblFace | — | — | — | — |
| lblDigital | TLabel | rótulo | lblDigital | — | — | — | — |
| imgFaceCheck | TImage | outro | — | — | — | — | — |
| imgDigitalCheck | TImage | outro | — | — | — | — | — |
| btnFace | THoverSpeedButton | ação | Cadastrar Face | 0 | — | — | — |
| btnDigital | THoverSpeedButton | ação | Cadastrar Digital | 1 | — | — | — |
| TabAlunos | TTabSheet | contêiner | Alunos | — | — | — | — |
| dbgAlunos | TDBGrid | grade | — | 0 | — | — | — |
| Panel1 | TPanel | contêiner | — | 1 | — | — | — |
| Image13 | TImage | outro | — | — | — | — | — |
| Label11 | TLabel | rótulo | Aluno: | — | — | — | — |
| mlAlunos | TMetaEquipLocalizar | outro | — | — | — | — | — |
| btnNovoAluno | THoverSpeedButton | ação | Cadastrar novo Aluno | 0 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| cdsResponsaveis | TClientDataSet | outro | — | — | — | — | — |
| cdsResponsaveisid | TIntegerField | outro | — | — | — | — | — |
| cdsResponsaveisnome | TStringField | outro | — | — | — | — | — |
| cdsResponsaveissituacao | TStringField | outro | — | — | — | — | — |
| dsResponsaveis | TDataSource | outro | — | — | — | — | — |
| cdsAlunos | TClientDataSet | outro | — | — | — | — | — |
| dsAlunos | TDataSource | outro | — | — | — | — | — |
| EscolaIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `GravaCampos` | 122 | `TResponsaveisController.Create`, `ResponsaveisController.SetConexao`, `ResponsaveisController.Inserir`, `ResponsaveisController.Atualizar` |
| `ValidarCampos` | 366 | `TResponsaveisController.Create`, `ResponsaveisController.SetConexao`, `ResponsaveisController.ExisteResponsavelCpf` |
| `ActExcluirExecute` | 631 | `TResponsaveisController.Create`, `FResponsaveisController.SetConexao`, `FResponsaveisController.Excluir` |
| `ActExibirTudoExecute` | 681 | `TResponsaveisController.Create`, `ResponsaveisController.SetConexao`, `ResponsaveisController.GetResponsaveisTodos` |
| `ActIncluirExecute` | 712 | — |
| `ActSalvarExecute` | 719 | — |
| `FormCreate` | 773 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 380: `É necessário informar o Nome.`
- Linha 388: `É necessário informar a Data de Nascimento.`
- Linha 395: `Data de Nascimento inválida.`
- Linha 404: `É necessário informar o Sexo do(a) responsável.`
- Linha 413: `É necessário informar o CPF.`
- Linha 421: `CPF Inválido.`
- Linha 433: `CPF já existe.`
- Linha 642: `Excluir o registro?`
- Linha 660: `Problemas com a exclusão no Banco de Dados!`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
