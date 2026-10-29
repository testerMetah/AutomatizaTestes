# Acesso: TFrmRegCrachas

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Acesso > Crachás > Registro de Crachás....

- DFM: `Acesso/UFrmRegCrachas.dfm`
- PAS: `Acesso/UFrmRegCrachas.pas`
- Handler de abertura: `acAceRegistroCrachasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmRegCrachas | TFrmRegCrachas | outro | Registro de Crachás | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | Nome da Pessoa(Ctrl+B) | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| TabSheet3 | TTabSheet | contêiner | Código da Pessoa (Ctrl+C) | — | — | — | — |
| EdCodPessoa | TEdit | campo de texto/data | — | 0 | — | — | — |
| HoverSpeedButton1 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| TipoCracha | TTabSheet | contêiner | Tipo do Crachá (Ctrl+F) | — | — | — | — |
| CmxTipoCracha | TComboBox | seleção | — | 0 | — | — | — |
| HoverSpeedButton2 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| TabSheet1 | TTabSheet | contêiner | Código do Crachá (Ctrl+G) | — | — | — | — |
| EdCodCracha | TEdit | campo de texto/data | — | 0 | — | — | — |
| HoverSpeedButton3 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | 5 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| PgTipoUso | TPageControl | contêiner | — | 4 | — | — | — |
| Pessoas | TTabSheet | contêiner | Pessoas | — | — | — | — |
| lblPessoa | TLabel | rótulo | Selecione uma pessoa... | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Pessoa: | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| EdPessoa | TEdit | campo de texto/data | — | 0 | — | — | Text=EdPessoa |
| PreCadastro | TTabSheet | contêiner | Pré-Cadastros | — | — | — | — |
| mlPreCadastro | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LblPreCadastro | TLabel | rótulo | Selecione um pré-cadastro... | — | — | — | — |
| Label2 | TLabel | rótulo | Pré-Cadastro: | — | — | — | — |
| Image7 | TImage | outro | — | — | — | — | — |
| EdPreCadastro | TEdit | campo de texto/data | — | 0 | — | — | Text=EdPessoa |
| Veiculos | TTabSheet | contêiner | Veículos | — | — | — | — |
| Image8 | TImage | outro | — | — | — | — | — |
| Label3 | TLabel | rótulo | Veículo: | — | — | — | — |
| LblVeiculo | TLabel | rótulo | Selecione um veículo... | — | — | — | — |
| mlVeiculo | TMetaEquipLocalizar | outro | — | — | — | — | — |
| edVeiculo | TEdit | campo de texto/data | — | 0 | — | — | Text=EdPessoa |
| Alunos | TTabSheet | contêiner | Alunos | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Label4 | TLabel | rótulo | Aluno: | — | — | — | — |
| mlAluno | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblAluno | TLabel | rótulo | Selecione um aluno... | — | — | — | — |
| edtAluno | TEdit | campo de texto/data | — | 0 | — | — | Text=edtAluno |
| Responsaveis | TTabSheet | contêiner | Responsaveis | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| Label5 | TLabel | rótulo | Responsável: | — | — | — | — |
| lblResponsavel | TLabel | rótulo | Selecione um responsável... | — | — | — | — |
| mlResponsavel | TMetaEquipLocalizar | outro | — | — | — | — | — |
| edtResponsavel | TEdit | campo de texto/data | — | 0 | — | — | Text=edtResponsavel |
| Funcionarios | TTabSheet | contêiner | Funcionários | — | — | — | — |
| MlFuncionario | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblFuncionario | TLabel | rótulo | Selecione um funcionário... | — | — | — | — |
| Label7 | TLabel | rótulo | Funcionário: | — | — | — | — |
| Image10 | TImage | outro | — | — | — | — | — |
| edtFuncionario | TEdit | campo de texto/data | — | 0 | — | — | Text=edtFuncionario |
| pnlCodigo | TPanel | contêiner | — | 1 | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| lblCodigo | TLabel | rótulo | Código do Crachá: | — | — | — | — |
| lblInfoTag | TLabel | rótulo | Informe o código WG sem virgula | — | — | — | Visible=False |
| EdCracha | TEdit | campo de texto/data | — | 0 | — | — | — |
| pnlDataHoraRegistro | TPanel | contêiner | — | 2 | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Label8 | TLabel | rótulo | Data/Hora do Registro: | — | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;_ | 10 | Text=  /  /    , Enabled=False |
| tmInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;_ | 5 | Text=  :  , Enabled=False |
| pnlTipoCracha | TPanel | contêiner | — | 3 | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Label11 | TLabel | rótulo | Tipo do Crachá: | — | — | — | — |
| CmbTipoCracha | TComboBox | seleção | — | 0 | — | — | Text=Fixo, ItemIndex=0 |
| pnlUso | TPanel | contêiner | — | 0 | — | — | — |
| Image6 | TImage | outro | — | — | — | — | — |
| Label12 | TLabel | rótulo | Uso: | — | — | — | — |
| CmbTipoUso | TComboBox | seleção | — | 0 | — | — | Text=Pessoas, ItemIndex=0 |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| DsCrachas | TDataSource | outro | — | — | — | — | — |
| CdsCrachas | TClientDataSet | outro | — | — | — | — | — |
| CdsCrachasId | TIntegerField | outro | — | — | — | — | — |
| CdsCrachasCracha | TStringField | outro | — | — | — | — | — |
| CdsCrachasdatahoraregistro | TDateTimeField | outro | — | — | — | — | — |
| CdsCrachastipocracha | TIntegerField | outro | — | — | — | — | — |
| CdsCrachaspessoa | TIntegerField | outro | — | — | — | — | — |
| CdsCrachasnomepessoa | TStringField | outro | — | — | — | — | — |
| CdsCrachasveiculo | TIntegerField | outro | — | — | — | — | — |
| CdsCrachasnomeveiculo | TStringField | outro | — | — | — | — | — |
| CdsCrachastipodepessoa | TStringField | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActTSCodCracha | TAction | ação | Código do Crachá (Ctrl+G) | — | — | — | — |
| ActTSCodPessoa | TAction | ação | Código da Pessoa (Ctrl+C) | — | — | — | — |
| ActTSTipoCracha | TAction | ação | Tipo do Crachá (Ctrl+F) | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActIr | TAction | ação | — | — | — | — | — |
| ActLocalizarCodigo | TAction | ação | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 195 | `FCrachasController.Excluir` |
| `ActExibirTudoExecute` | 212 | `FCrachasController.GetCrachaTodos`, `FCrachasController.GetCrachasEscola` |
| `ActIncluirExecute` | 311 | — |
| `ActIrExecute` | 321 | `FCrachasController.GetCrachasPorVeiculo`, `FCrachasController.GetCrachasPorPessoa`, `FCrachasController.GetCrachasPorVeiculoNome`, `FCrachasController.GetCrachasPorPessoaNome`, `FCrachasController.GetCrachasPorTipoCracha`, `FCrachasController.GetCrachaPorCodigo` |
| `ActSalvarExecute` | 473 | `FCrachasController.VerificarPessoaIns`, `FCrachasController.RemovePessoaVinculadaCracha`, `FCrachasController.VerificarPessoaAtt` |
| `FormCreate` | 1228 | `TCrachaController.Create`, `FCrachasController.SetConexao` |
| `GravaCampos` | 1310 | `FCrachasController.Inserir`, `FCrachasController.Atualizar` |
| `ValidarCampos` | 1506 | `FCrachasController.GetExisteCrachaPorCodigo` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 199: `Excluir o registro?`
- Linha 204: `Problemas com a exclusão no Banco de Dados!`
- Linha 1001: `Data Inválida!`
- Linha 1012: `Data Inválida!`
- Linha 1055: `Pessoa não cadastrada`
- Linha 1085: `Pessoa não cadastrada`
- Linha 1116: `Aluno não cadastrada`
- Linha 1145: `Funcionário não cadastrado`
- Linha 1178: `Aluno não cadastrado`
- Linha 1208: `Pessoa não cadastrada`
- Linha 1474: `Veículo não cadastrada`
- Linha 1490: `Hora Inválida!`
- Linha 1501: `Hora Inválida!`
- Linha 1513: `O código do crachá deve ser informado.`
- Linha 1520: `Data de Início deve ser informada.`
- Linha 1528: `A hora de Início deve ser informada.`
- Linha 1536: `O Tipo do Crachá deve ser informado.`
- Linha 1548: `Já existe uma TAG cadastrada com este código: [ `
- Linha 1551: `Já existe um crachá cadastrado com este código: [ `

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
