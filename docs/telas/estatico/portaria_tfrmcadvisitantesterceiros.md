# Portaria: TFrmCadVisitantesTerceiros

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastro > Visitantes e Terceiros....

- DFM: `Acesso/UFrmCadVisitantesTerceiros.dfm`
- PAS: `Acesso/UFrmCadVisitantesTerceiros.pas`
- Handler de abertura: `acCadVisitantesTerceirosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadVisitantesTerceiros | TFrmCadVisitantesTerceiros | outro | Cadastros de Visitantes e Terceiros | — | — | — | — |
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
| pnForm | TPanel | contêiner | — | 1 | — | — | — |
| Label5 | TLabel | rótulo | Nome: | — | — | — | — |
| Label6 | TLabel | rótulo | CPF: | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Label7 | TLabel | rótulo | Empresa: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Label8 | TLabel | rótulo | Situação: | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Label9 | TLabel | rótulo | Tipo: | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| lblEmpresa | TLabel | rótulo | lblEmpresa | — | — | — | — |
| MetaEmpresa | TMetaEquipLocalizar | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Telefone: | — | — | — | — |
| Image6 | TImage | outro | — | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | Text=EdNome |
| cmbSituacao | TComboBox | seleção | — | 1 | — | — | Text=Ativo, ItemIndex=0 |
| MskCPF | TEdit | campo de texto/data | — | 2 | — | 14 | — |
| CmbTipo | TComboBox | seleção | — | 3 | — | — | Text=Visitante, ItemIndex=0 |
| EdEmpresa | TEdit | campo de texto/data | — | 4 | — | 5 | — |
| GroupBox1 | TGroupBox | contêiner | Fotografia | 5 | — | — | — |
| imgFoto | TImage | outro | — | — | — | — | — |
| btnSalvarFoto | THoverSpeedButton | ação | Salvar (Ctrl+Alt+S) | 0 | — | — | — |
| BtnLimpar | THoverSpeedButton | ação | Limpar (Alt+Del) | 1 | — | — | — |
| btnSelectImage | THoverSpeedButton | ação | Procurar (Ctrl+F) | 2 | — | — | — |
| btnCamera | THoverSpeedButton | ação | Câmera (Ctrl+C) | 3 | — | — | — |
| EdTelefone | TEdit | campo de texto/data | — | 6 | — | 14 | — |
| btnCadEmpresa | THoverSpeedButton | ação | Cadastrar empresa (Ctrl+N) | 7 | — | — | — |
| BtnHistorico | THoverSpeedButton | ação | Histórico de visitas (Ctrl+H) | 8 | — | — | — |
| ChkEstrangeiro | TCheckBox | seleção | Estrangeiro | 9 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActCancelar | TAction | ação | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActCadastrarEmpresa | TAction | ação | Cadastrar empresa (Ctrl+N) | — | — | — | — |
| ActHistoricoVisitas | TAction | ação | Histórico de visitas (Ctrl+H) | — | — | — | — |
| ActProcurar | TAction | ação | Procurar (Ctrl+F) | — | — | — | — |
| ActCamera | TAction | ação | Câmera (Ctrl+C) | — | — | — | — |
| ActSalvarFoto | TAction | ação | Salvar (Ctrl+Alt+S) | — | — | — | — |
| ActLimparFoto | TAction | ação | Limpar (Alt+Del) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsVisitantes | TDataSource | outro | — | — | — | — | — |
| CdsVisitantes | TClientDataSet | outro | — | — | — | — | — |
| CdsVisitantesid | TIntegerField | outro | — | — | — | — | — |
| CdsVisitantesTipoPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsVisitantesNome | TStringField | outro | — | — | — | — | — |
| CdsVisitantesCpf | TStringField | outro | — | — | — | — | — |
| CdsVisitantesEstrangeiro | TBooleanField | outro | — | — | — | — | — |
| CdsVisitantesEmpresaAcesso | TIntegerField | outro | — | — | — | — | — |
| CdsVisitantesStatus | TIntegerField | outro | — | — | — | — | — |
| CdsHistorico | TClientDataSet | outro | — | — | — | — | — |
| CdsHistoricoid | TIntegerField | outro | — | — | — | — | — |
| CdsHistoricoidVisitantesTerceiros | TIntegerField | outro | — | — | — | — | — |
| CdsHistoricoExcluido | TStringField | outro | — | — | — | — | — |
| CdsHistoricoAcao | TStringField | outro | — | — | — | — | — |
| CdsHistoricoObservacao | TStringField | outro | — | — | — | — | — |
| CdsHistoricoNrCracha | TStringField | outro | — | — | — | — | — |
| CdsHistoricoDataHoraInicio | TDateTimeField | outro | — | — | — | — | — |
| CdsHistoricoDataHoraTermino | TDateTimeField | outro | — | — | — | — | — |
| CdsHistoricoCardapios | TStringField | outro | — | — | — | — | — |
| CdsHistoricoColetores | TStringField | outro | — | — | — | — | — |
| dsHistorico | TDataSource | outro | — | — | — | — | — |
| OpenDialog1 | TOpenDialog | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 283 | `TVisitantesTerceirosHistoricosController.Create`, `FVisitantesTerceirosHistoricosController.SetConexao`, `FVisitantesTerceirosController.Excluir`, `FVisitantesTerceirosHistoricosController.ExcluirVisitante`, `FVisitantesTerceirosHistoricosController.Free` |
| `ActExibirTudoExecute` | 315 | `FVisitantesTerceirosController.GetTodosVisitantesTerceiros` |
| `ActIncluirExecute` | 357 | — |
| `ActIrExecute` | 365 | `FVisitantesTerceirosController.GetPessoasPorNome` |
| `ActSalvarExecute` | 458 | `FVisitantesTerceirosController.GetPessoa` |
| `ActSalvarFotoExecute` | 489 | `FVisitantesTerceirosController.GetPessoa` |
| `FormCreate` | 738 | `TConfigEtiquetaController.Create`, `FConfigEtiquetaController.AcbrEtiqueta`, `TPreCadastroController.Create`, `FVisitantesTerceirosController.SetConexao`, `TFaixaAcessoColetoresController.Create`, `FFaixaAcessoColetoresController.SetConexao`, `TCrachaController.Create`, `FCrachasController.SetConexao` |
| `GravaCampos` | 774 | `FVisitantesTerceirosController.Inserir`, `FVisitantesTerceirosController.Atualizar` |
| `GravaFoto` | 817 | `TFaceControlIdController.Create`, `FFaceControlIdController.SetConexao`, `FFaceControlIdController.GetFacePorPessoa`, `FFaceControlIdController.Excluir`, `FFaceControlIdController.Inserir` |
| `ValidarCampos` | 1076 | `FCrachasController.VerificaCPFVinculado` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 296: `Excluir o registro?`
- Linha 305: `Problemas com a exclusão no Banco de Dados!`
- Linha 468: `A foto não está salva. Deseja salvar?`
- Linha 477: `Problemas com a gravação no Banco de Dados!`
- Linha 501: `Problemas com a gravação no Banco de Dados!`
- Linha 507: `Problemas com a gravação no Banco de Dados!`
- Linha 527: `Este visitante/terceiro não está cadastrado. Deseja salvar?`
- Linha 678: `Data Inválida!`
- Linha 711: `Empresa de Acesso não cadastrado`
- Linha 840: `Foto salva com sucesso`
- Linha 842: `Erro ao cadastrar foto`
- Linha 891: `Foto atualizada com sucesso`
- Linha 893: `Erro ao atualizar foto[0]`
- Linha 896: `Erro ao atualizar foto[1]`
- Linha 908: `Foto salva com sucesso`
- Linha 910: `Erro ao salvar foto`
- Linha 963: `CPF Inválido.`
- Linha 969: `O CPF tem 11 números.`
- Linha 1071: `Hora Inválida!`
- Linha 1087: `O nome deve ser preenchido`
- Linha 1105: `CPF Inválido.`
- Linha 1112: `O CPF deve ser preenchido.`
- Linha 1149: `A empresa deve ser preenchida.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
