# Acesso: TFImportadorExportadorMetadados

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ferramentas > Importador Metadados....

- DFM: `Acesso/UImportadorExportadorMetadados.dfm`
- PAS: `Acesso/UImportadorExportadorMetadados.pas`
- Handler de abertura: `acFerImportadorMetadadosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FImportadorExportadorMetadados | TFImportadorExportadorMetadados | outro | Importador Metadados | — | — | — | Visible=True |
| Label14 | TLabel | rótulo | Label14 | — | — | — | — |
| Image10 | TImage | outro | — | — | — | — | — |
| PgcDados | TPageControl | contêiner | — | 0 | — | — | — |
| TbsImportacao | TTabSheet | contêiner | Importação | — | — | — | — |
| GbConfigBanco | TGroupBox | contêiner |           Informações do Banco de Dados | 0 | — | — | — |
| Image14 | TImage | outro | — | — | — | — | — |
| pnlCamposConfig | TPanel | contêiner | — | 0 | — | — | — |
| Panel6 | TPanel | contêiner | — | 0 | — | — | — |
| Label4 | TLabel | rótulo | Selecione B.D.: | — | — | — | — |
| Image12 | TImage | outro | — | — | — | — | — |
| dblcbxSelecioneBD | TDBLookupComboBox | seleção | — | 0 | — | — | — |
| pnlTipoBD | TPanel | contêiner | — | 1 | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Label9 | TLabel | rótulo | Tipo do B.D.: | — | — | — | — |
| CmbTipoBD | TComboBox | seleção | — | 0 | — | — | — |
| pnlNomeServidor | TPanel | contêiner | — | 2 | — | — | — |
| lblNomeDoServidor | TLabel | rótulo | Nome do Servidor: | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| EdNomeServidor | TEdit | campo de texto/data | — | 0 | — | — | — |
| EdPorta | TEdit | campo de texto/data | — | 1 | — | — | — |
| pnlNomeBD | TPanel | contêiner | — | 3 | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Label5 | TLabel | rótulo | Nome do B.D.: | — | — | — | — |
| EdNomeBanco | TEdit | campo de texto/data | — | 0 | — | — | — |
| pnlUsuario | TPanel | contêiner | — | 4 | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| lblUsuario | TLabel | rótulo | Usuário: | — | — | — | — |
| EdUsuario | TEdit | campo de texto/data | — | 0 | — | — | — |
| pnlSenha | TPanel | contêiner | — | 5 | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Label7 | TLabel | rótulo | Senha: | — | — | — | — |
| EdSenha | TEdit | campo de texto/data | — | 0 | — | — | — |
| Panel1 | TPanel | contêiner | — | 1 | — | — | — |
| btnSalvarConfig | THoverSpeedButton | ação | Salvar Configuração (Ctrl+S) | 0 | — | — | — |
| btnExcluirConfig | THoverSpeedButton | ação | Excluir Configuração (Ctrl+Del) | 1 | — | — | — |
| GBFiltros | TGroupBox | contêiner |           Filtros | 1 | — | — | — |
| Label10 | TLabel | rótulo | Data do Cadastro: | — | — | — | — |
| Label11 | TLabel | rótulo |  | — | — | — | — |
| Label12 | TLabel | rótulo | Empresas: | — | — | — | — |
| Label13 | TLabel | rótulo | Selecione várias empresas usando vírgulas. | — | — | — | Visible=False |
| Image6 | TImage | outro | — | — | — | — | — |
| Image7 | TImage | outro | — | — | — | — | — |
| Image13 | TImage | outro | — | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| Image15 | TImage | outro | — | — | — | — | — |
| Label15 | TLabel | rótulo | Data de Admissão: | — | — | — | — |
| Label16 | TLabel | rótulo | Importar Pré-Cadastros: | — | — | — | — |
| Label18 | TLabel | rótulo | Unidades: | — | — | — | — |
| Image16 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Selecione várias unidades usando vírgulas. | — | — | — | Visible=False |
| EdEmpresas | TEdit | campo de texto/data | — | 0 | — | — | — |
| EdUnidades | TEdit | campo de texto/data | — | 5 | — | — | — |
| MskAdmissao | TMaskEdit | campo de texto/data | — | 1 | !99/99/9999;1;  | 10 | Text=  /  /     |
| ChkPreCadastro | TCheckBox | seleção | — | 2 | — | — | — |
| EdDataCadastro | TMaskEdit | campo de texto/data | — | 3 | !99/99/9999;1;  | 10 | Text=  /  /     |
| pnlImportar | TPanel | contêiner | — | 4 | — | — | Visible=False |
| Label6 | TLabel | rótulo | Importar Foto: | — | — | — | — |
| Label17 | TLabel | rótulo | Importar Digitais: | — | — | — | — |
| Image17 | TImage | outro | — | — | — | — | — |
| Label19 | TLabel | rótulo | Contratos alterados a partir: | — | — | — | — |
| Image8 | TImage | outro | — | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| ChkImportarFoto | TCheckBox | seleção | — | 2 | — | — | — |
| ChkImportarDigitais | TCheckBox | seleção | — | 1 | — | — | — |
| MskContratoAlteradoApatir | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| pnlFundoPadrao | TPanel | contêiner | — | 6 | — | — | — |
| btnImportar | THoverSpeedButton | ação | Importar (Ctrl+I) | 0 | — | — | — |
| TbsSQLOracle | TTabSheet | contêiner | SQL ORACLE | — | — | — | — |
| Memo1 | TMemo | outro | — | 0 | — | — | — |
| DBGrid1 | TDBGrid | grade | — | 1 | — | — | — |
| Button1 | TButton | ação | EXECUTAR | 2 | — | — | — |
| FDQuery1 | TFDQuery | outro | — | — | — | — | — |
| DataSource1 | TDataSource | outro | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| memSelecioneDB | TFDMemTable | outro | — | — | — | — | — |
| memSelecioneDBID | TIntegerField | outro | — | — | — | — | — |
| memSelecioneDBNOME | TStringField | outro | — | — | — | — | — |
| dsSelecioneDB | TDataSource | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActSalvarConfiguracao | TAction | ação | Salvar Configuração (Ctrl+S) | — | — | — | — |
| ActImportar | TAction | ação | Importar (Ctrl+I) | — | — | — | — |
| ActExcluirConfiguracao | TAction | ação | Excluir Configuração (Ctrl+Del) | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirConfiguracaoExecute` | 653 | `FConexaoClienteController.Excluir` |
| `ActSalvarConfiguracaoExecute` | 756 | `FConexaoClienteController.ExisteBD`, `FConexaoClienteController.Inserir`, `FConexaoClienteController.Atualizar` |
| `btnSalvarConfigClick` | 921 | `FConexaoClienteController.ExisteBD`, `FConexaoClienteController.Inserir`, `FConexaoClienteController.Atualizar` |
| `FormCreate` | 1145 | `TConexaoController.Create`, `FConexaoClienteController.SetConexao` |
| `SalvarLogErro` | 2288 | — |
| `SalvarDiagnosticoAmbiente` | 2391 | — |
| `BtnSalvarClick` | 2574 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 484: `Diretório deve ser preenchido.`
- Linha 491: `Diretório inexistente.`
- Linha 498: `Data de Início deve ser informada.`
- Linha 505: `A hora de Início deve ser informada.`
- Linha 512: `Data de Término deve ser informada.`
- Linha 519: `A hora de Término deve ser informada.`
- Linha 526: `Selecione um Layout.`
- Linha 648: `Exportação concluída.`
- Linha 706: `Não foi possivel estabelecer conexão. Erro: `
- Linha 726: `Importação concluída.`
- Linha 829: `Não foi possivel estabelecer conexão. Erro: `
- Linha 848: `Importação concluída.`
- Linha 1130: `Data Inválida!`
- Linha 1479: `Importação concluída.`
- Linha 1488: `Deseja importar?`
- Linha 1511: `Importação concluída.`
- Linha 1730: `Data Inválida!`
- Linha 2206: `Hora Inválida!`
- Linha 2592: `Log salvo com sucesso em:`
- Linha 2612: `Texto copiado para a área de transferência!`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
