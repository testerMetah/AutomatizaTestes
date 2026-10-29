# Escola: TFrmEscolaCadFuncionario

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Funcionários....

- DFM: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Funcionarios.dfm`
- PAS: `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Funcionarios.pas`
- Handler de abertura: `actFuncionariosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEscolaCadFuncionario | TFrmEscolaCadFuncionario | outro | Cadastro de Funcionários | — | — | — | — |
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
| PgcCadastro | TPageControl | contêiner | — | 1 | — | — | — |
| tbsDadosGerais | TTabSheet | contêiner | Dados Gerais | — | — | — | — |
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| Label2 | TLabel | rótulo | Situação: | — | — | — | — |
| Label8 | TLabel | rótulo | Email: | — | — | — | — |
| Label7 | TLabel | rótulo | Fone: | — | — | — | — |
| Label5 | TLabel | rótulo | Nascimento: | — | — | — | — |
| Label3 | TLabel | rótulo | CPF: | — | — | — | — |
| Label9 | TLabel | rótulo | Setor: | — | — | — | — |
| Label6 | TLabel | rótulo | Sexo: | — | — | — | — |
| lblSetor | TLabel | rótulo | Selecione um setor... | — | — | — | — |
| Label19 | TLabel | rótulo | — | — | — | — | — |
| Label20 | TLabel | rótulo | Código de Exportação / Matrícula: | — | — | — | — |
| LblUnidade | TLabel | rótulo | Selecione uma unidade... | — | — | — | — |
| Label22 | TLabel | rótulo | Unidade: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Image6 | TImage | outro | — | — | — | — | — |
| Image7 | TImage | outro | — | — | — | — | — |
| Image8 | TImage | outro | — | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| Image10 | TImage | outro | — | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| Image12 | TImage | outro | — | — | — | — | — |
| mlUnidade | TMetaEquipLocalizar | outro | — | — | — | — | — |
| mlSetor | TMetaEquipLocalizar | outro | — | — | — | — | — |
| Image19 | TImage | outro | — | — | — | — | — |
| Label14 | TLabel | rótulo | Responsável: | — | — | — | — |
| lblResponsavel | TLabel | rótulo | Selecione um Responsavel... | — | — | — | — |
| mlResponsavel | TMetaEquipLocalizar | outro | — | — | — | — | — |
| cmbStatus | TComboBox | seleção | — | 1 | — | — | Text=Ativo, ItemIndex=0 |
| MskNascimento | TMaskEdit | campo de texto/data | — | 3 | !99/99/9999;1;  | 10 | Text=  /  /     |
| CmbGenero | TComboBox | seleção | — | 4 | — | — | — |
| EdFone | TEdit | campo de texto/data | — | 5 | — | 12 | — |
| EdEmail | TEdit | campo de texto/data | — | 6 | — | — | — |
| EdSetor | TEdit | campo de texto/data | — | 7 | — | — | — |
| GbCrachas | TGroupBox | contêiner | Crachás | 10 | — | — | — |
| Label17 | TLabel | rótulo | Crachá Fixo: | — | — | — | — |
| lblCrachaFixo | TLabel | rótulo | Cadastrar crachá fixo | — | — | — | — |
| Label18 | TLabel | rótulo | Crachá Provisório: | — | — | — | — |
| lblCrachaProvisorio | TLabel | rótulo | Cadastrar crachá provisório | — | — | — | — |
| Image13 | TImage | outro | — | — | — | — | — |
| Image14 | TImage | outro | — | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Label4 | TLabel | rótulo | Crachá Mestre: | — | — | — | — |
| lblCrachaMestre | TLabel | rótulo | Cadastrar crachá mestre | — | — | — | — |
| EdCodExportacao | TEdit | campo de texto/data | — | 9 | — | 12 | — |
| EdUnidade | TEdit | campo de texto/data | — | 8 | — | — | — |
| cbxGestor | TCheckBox | seleção | Gestor: | 2 | — | — | — |
| GroupBox1 | TGroupBox | contêiner | Acesso para o Aplicativo | 11 | — | — | — |
| Label21 | TLabel | rótulo | Usuário: | — | — | — | — |
| Label23 | TLabel | rótulo | Senha: | — | — | — | — |
| Image15 | TImage | outro | — | — | — | — | — |
| Image16 | TImage | outro | — | — | — | — | — |
| EdUsuario | TEdit | campo de texto/data | — | 0 | — | 50 | — |
| EdSenha | TEdit | campo de texto/data | — | 1 | — | 15 | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | — |
| MskCpf | TEdit | campo de texto/data | — | 12 | — | 11 | — |
| edResponsavel | TEdit | campo de texto/data | — | 13 | — | — | — |
| TbsDadosCadastrais | TTabSheet | contêiner | Dados Cadastrais | — | — | — | — |
| Image17 | TImage | outro | — | — | — | — | — |
| Image18 | TImage | outro | — | — | — | — | — |
| Label24 | TLabel | rótulo | Endereço: | — | — | — | — |
| Label25 | TLabel | rótulo | CEP: | — | — | — | — |
| Label26 | TLabel | rótulo | Número: | — | — | — | — |
| Label10 | TLabel | rótulo | Bairro: | — | — | — | — |
| Label11 | TLabel | rótulo | Cidade: | — | — | — | — |
| Label12 | TLabel | rótulo | Complemento: | — | — | — | — |
| Label13 | TLabel | rótulo | UF: | — | — | — | — |
| edpri_cep | TEdit | campo de texto/data | — | 0 | — | 19 | — |
| edpri_endereco | TEdit | campo de texto/data | — | 1 | — | 60 | — |
| Edt_NumeroEnder | TEdit | campo de texto/data | — | 2 | — | 19 | — |
| edpri_bairro | TEdit | campo de texto/data | — | 3 | — | 60 | — |
| edpri_complemento | TEdit | campo de texto/data | — | 4 | — | — | — |
| edtCidade | TEdit | campo de texto/data | — | 5 | — | — | — |
| cmbUfs | TComboBox | seleção | — | 6 | — | — | — |
| BtnLimparEndereco | THoverSpeedButton | ação | Limpar Endereço (F6) | 7 | — | — | — |
| BtnPesquisarEndereco | THoverSpeedButton | ação | Pesquisar Rua (F5) | 8 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActPesquisaCep | TAction | ação | Pesquisar Rua (F5) | — | — | — | — |
| ActLimparEndereco | TAction | ação | Limpar Endereço (F6) | — | — | — | — |
| ActTSNome | TAction | ação | Action1 | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| CdsPessoas | TClientDataSet | outro | — | — | — | — | — |
| CdsPessoasId | TIntegerField | outro | — | — | — | — | — |
| CdsPessoasNome | TStringField | outro | — | — | — | — | — |
| CdsPessoasSituacao | TIntegerField | outro | — | — | — | — | — |
| CdsPessoasAfastado | TStringField | outro | — | — | — | — | — |
| DsPessoas | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 189 | `FAceAutorizaController.ExistePessoaAutorizada`, `FAceAutorizaController.ExcluirPessoaAutorizada`, `FPessoasController.Excluir`, `FFiltrosController.VerificarPessoaUpdate` |
| `ActExibirTudoExecute` | 246 | `FPessoasController.GetPessoasTodosComAfastamento` |
| `ActIncluirExecute` | 275 | — |
| `ActIrExecute` | 282 | `FPessoasController.GetPessoa`, `FPessoasController.GetPessoasPorNome` |
| `ActSalvarExecute` | 386 | — |
| `FormCreate` | 743 | `TPessoasController.Create`, `FPessoasController.SetConexao`, `TUnidadesController.Create`, `FUnidadesController.SetConexao`, `TFiltrosController.Create`, `FFiltrosController.SetConexao`, `TAceAutorizaController.Create`, `FAceAutorizaController.SetConexao` |
| `GravaCampos` | 789 | `TCrachaController.Create`, `FCrachaController.SetConexao`, `FUnidadesController.GetUnidadePorId`, `FPessoasController.Inserir`, `FPessoasController.Atualizar`, `FCrachaController.GetCrachasPorPessoa` |
| `ValidarCampos` | 1002 | `TResponsaveisController.Create`, `FResponsaveisController.SetConexao`, `FCrachasController.VerificaCPFVinculado`, `FPessoasController.VerificarCPFCadastrado`, `FPessoasController.GetExisteIdExp`, `FResponsaveisController.GetResponsavelPorId` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 195: `Excluir o registro?`
- Linha 201: `A pessoa selecionada está vinculada à Autorização de Acessos.`
- Linha 221: `Problemas com a exclusão no Banco de Dados!`
- Linha 226: `Problemas com a exclusão no Banco de Dados!`
- Linha 241: `Problemas com a exclusão no Banco de Dados!`
- Linha 337: `Preencha o CEP para localizar o endereço.`
- Linha 580: `Digite apenas números.`
- Linha 594: `CEP errado ou fora do padrão.`
- Linha 626: `Responsável não cadastrado.`
- Linha 655: `Setor não cadastrado.`
- Linha 685: `Unidade não cadastrada.`
- Linha 971: `CPF Inválido.`
- Linha 978: `O CPF tem 11 números.`
- Linha 996: `Data inválida.`
- Linha 1019: `O nome deve ser preenchido.`
- Linha 1027: `O CPF deve ser preenchido.`
- Linha 1035: `CPF inválido`
- Linha 1078: `CPF já está em uso.`
- Linha 1097: `O código de Importação/Exportação "`
- Linha 1109: `Para criar um vínculo de um Funcionário com um Responsável, os CPFs devem ser iguais.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
