# Administracao: TFrmAdministracaoViewsCadUsuarios

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Usuários.

- DFM: `Administracao/Views/Acessus.Administracao.Views.CadUsuarios.dfm`
- PAS: `Administracao/Views/Acessus.Administracao.Views.CadUsuarios.pas`
- Handler de abertura: `actUsuariosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmAdministracaoViewsCadUsuarios | TFrmAdministracaoViewsCadUsuarios | outro | Cadastro de Usuários | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | Visible=False, Enabled=False |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| pgcModulos | TPageControl | contêiner | — | 1 | — | — | — |
| tstModulo | TTabSheet | contêiner | Modulos | — | — | — | — |
| sbxModulo | TScrollBox | outro | — | 0 | — | — | — |
| tstAcesso | TTabSheet | contêiner | Acesso | — | — | — | — |
| sbxAcesso | TScrollBox | outro | — | 0 | — | — | — |
| tstPortaria | TTabSheet | contêiner | Portaria | — | — | — | — |
| sbxPortaria | TScrollBox | outro | — | 0 | — | — | — |
| tstRefeitorio | TTabSheet | contêiner | Refeitório | — | — | — | — |
| sbxRefeitorio | TScrollBox | outro | — | 0 | — | — | — |
| tstEstacionamento | TTabSheet | contêiner | Estacionamento | — | — | — | — |
| sbxEstacionamento | TScrollBox | outro | — | 0 | — | — | — |
| tstEscola | TTabSheet | contêiner | Escola | — | — | — | — |
| sbxEscola | TScrollBox | outro | — | 0 | — | — | — |
| tstAdministracao | TTabSheet | contêiner | Administração | — | — | — | — |
| sbxAdministracao | TScrollBox | outro | — | 0 | — | — | — |
| pnlCadastro | TPanel | contêiner | — | 2 | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Usuário: | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Label2 | TLabel | rótulo | Situação: | — | — | — | — |
| Label4 | TLabel | rótulo | Nova Senha: | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Label5 | TLabel | rótulo | Confirmar Senha: | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| versenha | TSpeedButton | ação | — | — | — | — | — |
| cmbStatus | TComboBox | seleção | — | 3 | — | — | Text=Ativo, ItemIndex=0 |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | — |
| edSenha | TEdit | campo de texto/data | — | 1 | — | 20 | — |
| edSenhac | TEdit | campo de texto/data | — | 2 | — | 20 | — |
| cbManterSenha | TCheckBox | seleção | Manter senha atual | 4 | — | — | — |
| cbAdministrador | TCheckBox | seleção | Usuário Administrador | 5 | — | — | Visible=False, Enabled=False |
| pnlVinculaColetores | TPanel | contêiner | — | 3 | — | — | — |
| mlColetores | TMetaEquipLocalizar | outro | — | — | — | — | — |
| Label3 | TLabel | rótulo | Vincular Coletores: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| lsColetores | TListBox | seleção | — | 0 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| pnlEmpresa | TPanel | contêiner | — | 1 | — | — | Visible=False, Enabled=False |
| lblEmpresaTittle | TLabel | rótulo | Empresa: | — | — | — | — |
| mlEmpresa | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblEmpresa | TLabel | rótulo | Selecione uma Empresa... | — | — | — | — |
| EdEmpresa | TEdit | campo de texto/data | — | 0 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | — |
| ActExibirTudo | TAction | ação | Exibir tudo (Ctrl + T) | — | — | — | — |
| ActCancelar | TAction | ação | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| CdsCadUsuarios | TClientDataSet | outro | — | — | — | — | — |
| CdsCadUsuariosId | TIntegerField | outro | — | — | — | — | — |
| CdsCadUsuariosNome | TStringField | outro | — | — | — | — | — |
| CdsCadUsuariosSenha | TStringField | outro | — | — | — | — | — |
| CdsCadUsuariosIdEmpresa | TIntegerField | outro | — | — | — | — | — |
| CdsCadUsuariosSituacao | TIntegerField | outro | — | — | — | — | — |
| CdsCadUsuariosEmpresa | TStringField | outro | — | — | — | — | — |
| CdsCadUsuariospermissoes | TStringField | outro | — | — | — | — | — |
| CdsCadUsuariosprimeirologin | TBooleanField | outro | — | — | — | — | — |
| DsCadUsuarios | TDataSource | outro | — | — | — | — | — |
| CdsEmpresa | TClientDataSet | outro | — | — | — | — | — |
| CdsEmpresaCODIGO | TIntegerField | outro | — | — | — | — | — |
| CdsEmpresaNOME | TStringField | outro | — | — | — | — | — |
| DsEmpresa | TDataSource | outro | — | — | — | — | — |
| DSServerMetaDataProvider1 | TDSServerMetaDataProvider | outro | — | — | — | — | — |
| DSServerMetaDataProvider2 | TDSServerMetaDataProvider | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 293 | `TUsuariosController.Create`, `FUsuariosController.SetConexao`, `TParametrosSistemaController.Create`, `FParametrosSistemaController.SetConexao`, `TModulosPermissoesController.Create`, `FModulosPermissoesController.SetConexao`, `TEmpresasController.Create`, `FEmpresasController.SetConexao` |
| `GravaCampos` | 422 | `FParametrosSistemaController.AlteraSenhaPrimeiroLogin`, `FUsuariosController.Inserir`, `FUsuariosController.UpdateUser`, `FModulosPermissoesController.GetPermissoesPorUsuario`, `FUsuariosController.InserirHistorico` |
| `ActCancelarExecute` | 1054 | — |
| `ActExcluirExecute` | 1063 | `FUsuariosController.Excluir`, `FModulosPermissoesController.ExcluirPorUsuario` |
| `ActExibirTudoExecute` | 1091 | `FUsuariosController.GetUsuariosTodos` |
| `ActIncluirExecute` | 1133 | — |
| `ActIrExecute` | 1240 | `FUsuariosController.GetUsuariosPorDescricao` |
| `ActSalvarExecute` | 1276 | `FUsuariosController.VerificarAdministrador`, `FUsuariosController.VerificarUsuarioExistente`, `FOpcoesSenhaController.ValidarSenha`, `FOpcoesSenhaController.ObterOpcoesSenha` |
| `GravaPermissoesMenu` | 1477 | `FModulosPermissoesController.Get`, `FModulosPermissoesController.Inserir`, `FModulosPermissoesController.Atualizar` |
| `ValidarCampos` | 1976 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 1028: `Você não tem permissão para alterar o usuário administrador!`
- Linha 1067: `Excluir o registro?`
- Linha 1224: `Empresa não cadastrado.`
- Linha 1852: `CheckBox clicado: `
- Linha 1981: `O Nome do usuário é obrigatório.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
