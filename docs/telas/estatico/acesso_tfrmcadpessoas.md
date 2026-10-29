# Acesso: TFrmCadPessoas

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Pessoas....

- DFM: `Acesso/UFrmCadPessoas.dfm`
- PAS: `Acesso/UFrmCadPessoas.pas`
- Handler de abertura: `acCadPessoasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadPessoas | TFrmCadPessoas | outro | Cadastro de Pessoas | — | — | — | — |
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
| BtnImportarPessoas | THoverSpeedButton | ação | Importar Pessoas (Ctrl + F5) | 3 | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
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
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActAtualiza | TAction | ação | Importar Pessoas (Ctrl + F5) | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActPesquisaCep | TAction | ação | Pesquisar Rua (F5) | — | — | — | — |
| ActLimparEndereco | TAction | ação | Limpar Endereço (F6) | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsPessoas | TDataSource | outro | — | — | — | — | — |
| CdsPessoas | TClientDataSet | outro | — | — | — | — | — |
| CdsPessoasId | TIntegerField | outro | — | — | — | — | — |
| CdsPessoasNome | TStringField | outro | — | — | — | — | — |
| CdsPessoasSituacao | TIntegerField | outro | — | — | — | — | — |
| CdsPessoasAfastado | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 208 | `FAceAutorizaController.ExistePessoaAutorizada`, `FAceAutorizaController.ExcluirPessoaAutorizada`, `FPessoasController.Excluir`, `FFiltrosController.VerificarPessoaUpdate` |
| `ActExibirTudoExecute` | 265 | `FPessoasController.GetPessoasTodosComAfastamento` |
| `ActIncluirExecute` | 294 | — |
| `ActIrExecute` | 301 | `FPessoasController.GetPessoa`, `FPessoasController.GetPessoasPorNome` |
| `ActSalvarExecute` | 405 | — |
| `FormCreate` | 728 | `TPessoasController.Create`, `FPessoasController.SetConexao`, `TUnidadesController.Create`, `FUnidadesController.SetConexao`, `TFiltrosController.Create`, `FFiltrosController.SetConexao`, `TAceAutorizaController.Create`, `FAceAutorizaController.SetConexao` |
| `GravaCampos` | 781 | `TCrachaController.Create`, `FCrachaController.SetConexao`, `FUnidadesController.GetUnidadePorId`, `FPessoasController.Inserir`, `FPessoasController.Atualizar`, `FCrachaController.GetCrachasPorPessoa` |
| `ValidarCampos` | 992 | `FCrachasController.VerificaCPFVinculado`, `FPessoasController.VerificarCPFCadastrado`, `FPessoasController.GetExisteIdExp` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 214: `Excluir o registro?`
- Linha 220: `A pessoa selecionada está vinculada à Autorização de Acessos.`
- Linha 240: `Problemas com a exclusão no Banco de Dados!`
- Linha 245: `Problemas com a exclusão no Banco de Dados!`
- Linha 260: `Problemas com a exclusão no Banco de Dados!`
- Linha 356: `Preencha o CEP para localizar o endereço.`
- Linha 594: `Digite apenas números.`
- Linha 608: `CEP errado ou fora do padrão.`
- Linha 640: `Setor não cadastrado.`
- Linha 670: `Unidade não cadastrada.`
- Linha 961: `CPF Inválido.`
- Linha 968: `O CPF tem 11 números.`
- Linha 986: `Data inválida.`
- Linha 1004: `O nome deve ser preenchido.`
- Linha 1012: `O CPF deve ser preenchido.`
- Linha 1020: `CPF inválido`
- Linha 1082: `O código de Importação/Exportação "`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
