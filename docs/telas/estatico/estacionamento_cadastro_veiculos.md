# Estacionamento: TFrmEstacionamentoViewsCadastroVeiculos

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Veículos.

- DFM: `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Veiculos.dfm`
- PAS: `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Veiculos.pas`
- Handler de abertura: `actCadVeiculosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEstacionamentoViewsCadastroVeiculos | TFrmEstacionamentoViewsCadastroVeiculos | outro | Cadastro de Veículos | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | Motorista (Ctrl+B) | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| tbsVeiculos | TTabSheet | contêiner | Veículo (Ctrl+D) | — | — | — | — |
| edVeiculo | TEdit | campo de texto/data | — | 0 | — | — | — |
| Panel1 | TPanel | contêiner | Acesso | 1 | — | — | — |
| Shape1 | TShape | outro | — | — | — | — | — |
| SpeedButton1 | TSpeedButton | ação | — | — | — | — | — |
| TabSheet3 | TTabSheet | contêiner | Placa (Ctrl+F) | — | — | — | — |
| edtPlaca | TEdit | campo de texto/data | — | 0 | — | — | — |
| Panel2 | TPanel | contêiner | Acesso | 1 | — | — | — |
| Shape3 | TShape | outro | — | — | — | — | — |
| SpeedButton2 | TSpeedButton | ação | — | — | — | — | — |
| TabSheet4 | TTabSheet | contêiner | Tipo Veículo (Ctrl+G) | — | — | — | — |
| Panel3 | TPanel | contêiner | Acesso | 0 | — | — | — |
| Shape4 | TShape | outro | — | — | — | — | — |
| SpeedButton3 | TSpeedButton | ação | — | — | — | — | — |
| cmbTipoVei | TComboBox | seleção | — | 1 | — | — | — |
| TabSheet5 | TTabSheet | contêiner | Estacionamento (Ctrl+F) | — | — | — | — |
| edtEstacionamento | TEdit | campo de texto/data | — | 0 | — | — | — |
| Panel5 | TPanel | contêiner | Acesso | 1 | — | — | — |
| Shape5 | TShape | outro | — | — | — | — | — |
| SpeedButton4 | TSpeedButton | ação | — | — | — | — | — |
| TabSheet6 | TTabSheet | contêiner | Status (Ctrl+H) | — | — | — | — |
| Panel6 | TPanel | contêiner | Acesso | 0 | — | — | — |
| Shape6 | TShape | outro | — | — | — | — | — |
| SpeedButton5 | TSpeedButton | ação | — | — | — | — | — |
| cmbStatus | TComboBox | seleção | — | 1 | — | — | — |
| TabSheet7 | TTabSheet | contêiner | Tag (Ctrl+W) | — | — | — | — |
| edtTag | TEdit | campo de texto/data | — | 0 | — | — | — |
| Panel7 | TPanel | contêiner | Acesso | 1 | — | — | — |
| Shape7 | TShape | outro | — | — | — | — | — |
| SpeedButton6 | TSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| LblObservacoes | TLabel | rótulo | Observações: | — | — | — | — |
| LblCadTag | TLabel | rótulo | Tag: | — | — | — | — |
| MetaEquipLocalizar1 | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblTag | TLabel | rótulo | lblTag | — | — | — | — |
| lblEstacionamento | TLabel | rótulo | lblEstacionamento | — | — | — | — |
| MetaEquipLocalizar2 | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LblCadEstacionamento | TLabel | rótulo | Estacionamento: | — | — | — | — |
| LblTipoVeiculo | TLabel | rótulo | Tipo de Veículo: | — | — | — | — |
| LblPlaca | TLabel | rótulo | Placa: | — | — | — | — |
| LblNomeVeiculo | TLabel | rótulo | Nome do Veículo: | — | — | — | — |
| LblSituacao | TLabel | rótulo | Situação: | — | — | — | — |
| LblUsoVeiculo | TLabel | rótulo | Uso do Veículo: | — | — | — | — |
| LblTipoVaga | TLabel | rótulo | Tipo de Vaga: | — | — | — | — |
| lblPessoaPreCad | TLabel | rótulo | Motorista: | — | — | — | — |
| MetaEquipLocalizar3 | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblPessoa | TLabel | rótulo | lblPessoa | — | — | — | — |
| LblTipoMotorista | TLabel | rótulo | Tipo de Motorista: | — | — | — | — |
| ImgNomeVeiculo | TImage | outro | — | — | — | — | — |
| ImgPlaca | TImage | outro | — | — | — | — | — |
| ImgTipoVeiculo | TImage | outro | — | — | — | — | — |
| ImgEstacionamento | TImage | outro | — | — | — | — | — |
| ImgTag | TImage | outro | — | — | — | — | — |
| ImgMotorista | TImage | outro | — | — | — | — | — |
| ImgTipoMotorista | TImage | outro | — | — | — | — | — |
| ImgObservacoes | TImage | outro | — | — | — | — | — |
| ImgSituacao | TImage | outro | — | — | — | — | — |
| ImgTipoVaga | TImage | outro | — | — | — | — | — |
| ImgUsoVeiculo | TImage | outro | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| EdObservacao | TMemo | outro | — | 1 | — | — | — |
| edTag | TEdit | campo de texto/data | — | 2 | — | — | — |
| EdEstacionamento | TEdit | campo de texto/data | — | 3 | — | — | — |
| cmbTipoVeiculo | TComboBox | seleção | — | 4 | — | — | Text=Automóvel, ItemIndex=0 |
| EdNomeVeiculo | TEdit | campo de texto/data | — | 5 | — | 200 | — |
| CmbStatusVeiculos | TComboBox | seleção | — | 6 | — | — | Text=Ativo, ItemIndex=0 |
| cmbVeiculoUso | TComboBox | seleção | — | 7 | — | — | Text=Próprio, ItemIndex=0 |
| cmbBoxReserva | TComboBox | seleção | — | 8 | — | — | Text=Não Preferencial      , ItemIndex=0 |
| EdPessoa | TEdit | campo de texto/data | — | 9 | — | — | — |
| EdPlaca | TEdit | campo de texto/data | — | 10 | — | — | — |
| cmbPessoaPreCad | TComboBox | seleção | — | 11 | — | — | Text=Pré-Cadastro, ItemIndex=1 |
| btnCadTags | THoverSpeedButton | ação | Cadastrar Tags (Ctrl+N) | 12 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActTSMotorista | TAction | ação | Motorista (Ctrl+B) | — | — | — | — |
| ActTSVeiculo | TAction | ação | Veículo (Ctrl+D) | — | — | — | — |
| ActTSPlaca | TAction | ação | Placa (Ctrl+F) | — | — | — | — |
| ActTSTipoVeiculo | TAction | ação | Tipo Veículo (Ctrl+G) | — | — | — | — |
| ActTSEstacionamento | TAction | ação | Estacionamento (Ctrl+F) | — | — | — | — |
| ActTSStatus | TAction | ação | Status (Ctrl+H) | — | — | — | — |
| ActTSTag | TAction | ação | Tag (Ctrl+W) | — | — | — | — |
| ActCadastrarTags | TAction | ação | Cadastrar Tags (Ctrl+N) | — | — | — | — |
| DsVeiculos | TDataSource | outro | — | — | — | — | — |
| CdsVeiculos | TClientDataSet | outro | — | — | — | — | — |
| CdsVeiculosId | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosPlaca | TStringField | outro | — | — | AAA\-AAAA;0;_ | — | — |
| CdsVeiculosIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosIdTipoVeiculo | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosIdEstacionamento | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosObservacao | TMemoField | outro | — | — | — | — | — |
| CdsVeiculosTipoBoxReserva | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosNomePessoa | TStringField | outro | — | — | — | — | — |
| CdsVeiculosTipoVeiculoNome | TStringField | outro | — | — | — | — | — |
| CdsVeiculosNomeEstacionamento | TStringField | outro | — | — | — | — | — |
| CdsVeiculosNome | TStringField | outro | — | — | — | — | — |
| CdsVeiculosStatus | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosIdPreCadastro | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosTag | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 256 | `FCrachasController.VerificaTagExclui`, `FVeiculosController.Excluir` |
| `ActExibirTudoExecute` | 282 | `FVeiculosController.GetTodos` |
| `ActIncluirExecute` | 321 | — |
| `ActIrExecute` | 328 | `FVeiculosController.GetPorNome` |
| `ActSalvarExecute` | 362 | `FCrachasController.VerificaTagExistente` |
| `FormCreate` | 794 | `TVeiculosController.Create`, `FVeiculosController.SetConexao`, `TCrachaController.Create`, `FCrachasController.SetConexao` |
| `GravaCampos` | 813 | `FVeiculosController.Inserir`, `FVeiculosController.Atualizar`, `FCrachasController.VerificaTagExistenteEAtualiza` |
| `ValidarCampos` | 914 | — |
| `ValidarPlaca` | 949 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 262: `Excluir o registro?`
- Linha 269: `Problemas com a exclusão no Banco de Dados!`
- Linha 274: `Erro ao verificar e excluir Tag vinculada ao Veículo. Entre em contato com o suporte!`
- Linha 921: `O Nome do veículo deve ser informado.`
- Linha 928: `A placa do veículo deve ser informada.`
- Linha 936: `A placa do veículo deve ser informada.`
- Linha 943: `Placa inválida!`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
