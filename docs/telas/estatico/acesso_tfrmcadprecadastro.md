# Acesso: TFrmCadPreCadastro

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Pré-Cadastros > Pré-Cadastros.

- DFM: `Acesso/UFrmCadPreCadastro.dfm`
- PAS: `Acesso/UFrmCadPreCadastro.pas`
- Handler de abertura: `acCadPrePessoasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadPreCadastro | TFrmCadPreCadastro | outro | Pré-Cadastros | — | — | — | — |
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
| lblEmpresa | TLabel | rótulo | Selecione uma empresa... | — | — | — | — |
| MetaEmpresa | TMetaEquipLocalizar | outro | — | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| Label3 | TLabel | rótulo | CPF: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| Label2 | TLabel | rótulo | Situação: | — | — | — | — |
| Label5 | TLabel | rótulo | Empresa: | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Label6 | TLabel | rótulo | Tipo: | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | 6 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 2 | — | — | — |
| cmbSituacao | TComboBox | seleção | — | 1 | — | — | Text=Ativo, ItemIndex=0 |
| EdCpf | TEdit | campo de texto/data | — | 3 | — | 14 | — |
| GbCrachas | TGroupBox | contêiner | Crachás | 5 | — | — | — |
| lblCrachaFixo | TLabel | rótulo | Cadastrar crachá fixo | — | — | — | — |
| lblCrachaProvisorio | TLabel | rótulo | Cadastrar crachá provisório | — | — | — | — |
| Image13 | TImage | outro | — | — | — | — | — |
| Image14 | TImage | outro | — | — | — | — | — |
| Label17 | TLabel | rótulo | Crachá Fixo: | — | — | — | — |
| Label18 | TLabel | rótulo | Crachá Provisório: | — | — | — | — |
| EdEmpresa | TEdit | campo de texto/data | — | 4 | — | 5 | — |
| CmbTipoPessoa | TComboBox | seleção | — | 0 | — | — | — |
| BtnCadastrarEmpresa | THoverSpeedButton | ação | Cadastrar Empresa (Ctrl+N) | 7 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActCadastrarEmpresa | TAction | ação | Cadastrar Empresa (Ctrl+N) | — | — | — | — |
| DsPreCadastro | TDataSource | outro | — | — | — | — | — |
| CdsPreCadastro | TClientDataSet | outro | — | — | — | — | — |
| CdsPreCadastroid | TIntegerField | outro | — | — | — | — | — |
| CdsPreCadastroNome | TStringField | outro | — | — | — | — | — |
| CdsPreCadastroTipoPessoa | TStringField | outro | — | — | — | — | — |
| CdsPreCadastroStatus | TIntegerField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 166 | `FPreCadastroController.Excluir`, `FFiltrosController.VerificarPreCadastroUpdate` |
| `ActExibirTudoExecute` | 196 | `FPreCadastroController.GetTodosPreCadastros` |
| `ActIncluirExecute` | 240 | — |
| `ActIrExecute` | 254 | `FPreCadastroController.GetPessoasPorNome` |
| `ActSalvarExecute` | 276 | — |
| `FormCreate` | 418 | `TPreCadastroController.Create`, `FPreCadastroController.SetConexao`, `TFiltrosController.Create`, `FFiltrosController.SetConexao`, `TCrachaController.Create`, `FCrachasController.SetConexao` |
| `GravaCampos` | 451 | `TCrachaController.Create`, `FCrachaController.SetConexao`, `FPreCadastroController.Inserir`, `FPreCadastroController.Atualizar`, `FCrachaController.GetCrachasPorPreCadastro` |
| `ValidarCampos` | 682 | `FCrachasController.VerificaCPFVinculado`, `FPreCadastroController.VerificarCPFCadastrado` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 173: `Excluir o registro?`
- Linha 179: `Problemas com a exclusão no Banco de Dados!`
- Linha 184: `Problemas com a exclusão no Banco de Dados!`
- Linha 191: `Problemas com a exclusão no Banco de Dados!`
- Linha 363: `Data Inválida!`
- Linha 393: `Empresa de Acesso não cadastrado`
- Linha 677: `Hora Inválida!`
- Linha 693: `O nome deve ser preenchido`
- Linha 700: `O CPF deve ser preenchido.`
- Linha 707: `CPF inválido`
- Linha 763: `É necessário selecionar um tipo de pessoa.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
