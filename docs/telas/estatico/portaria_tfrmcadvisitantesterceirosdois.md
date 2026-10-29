# Portaria: TFrmCadVisitantesTerceirosDois

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastro > Visitantes e Terceiros....

- DFM: `Acesso/UFrmCadVisitantesTerceirosDois.dfm`
- PAS: `Acesso/UFrmCadVisitantesTerceirosDois.pas`
- Handler de abertura: `acCadVisitantesTerceirosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadVisitantesTerceirosDois | TFrmCadVisitantesTerceirosDois | outro | Cadastro de Visitantes e Terceiros | — | — | — | Visible=True |
| Pagina | TPageControl | contêiner | — | 0 | — | — | — |
| Grid | TTabSheet | contêiner | Grid | — | — | — | — |
| DGridVisitantes | TDrawGrid | grade | — | 0 | — | — | — |
| pnlCimaPadrao | TPanel | contêiner | — | 1 | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | 0 | — | — | — |
| TabSheet2 | TTabSheet | contêiner | Nome (Ctrl+B) | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | 0 | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | 2 | — | — | — |
| btnexcluir | THoverSpeedButton | ação | Excluir (Ctrl+Del) | 0 | — | — | — |
| btnInserir | THoverSpeedButton | ação | Incluir (Ctrl+I) | 1 | — | — | — |
| btnAlterar | THoverSpeedButton | ação | Alterar (Ctrl+E) | 2 | — | — | — |
| btnEncerrarVisitas | THoverSpeedButton | ação | Encerrar Visitas Selecionadas | 3 | — | — | — |
| Cadastro | TTabSheet | contêiner | Cadastro | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | 0 | — | — | — |
| btnOk | THoverSpeedButton | ação | Salvar (Ctrl+S) | 0 | — | — | — |
| btnCancelar | THoverSpeedButton | ação | Cancelar (Ctrl+D) | 1 | — | — | — |
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
| Campos | TTabSheet | contêiner | Campos | — | — | — | — |
| Panel4 | TPanel | contêiner | — | 0 | — | — | — |
| BitBtn2 | TBitBtn | outro | OK (F2) | 0 | — | — | — |
| BitBtn3 | TBitBtn | outro | Cancelar (F3) | 1 | — | — | — |
| BitBtn4 | TBitBtn | outro | Ajuda (F1) | 2 | — | — | — |
| BitBtn5 | TBitBtn | outro | Todos | 3 | — | — | — |
| CdsVisitantes | TClientDataSet | outro | — | — | — | — | — |
| CdsVisitantesid | TIntegerField | outro | — | — | — | — | — |
| CdsVisitantesNome | TStringField | outro | — | — | — | — | — |
| CdsVisitantesStatus | TIntegerField | outro | — | — | — | — | — |
| CdsVisitantesCpf | TStringField | outro | — | — | — | — | — |
| CdsVisitantesEstrangeiro | TBooleanField | outro | — | — | — | — | — |
| CdsVisitantesTipoPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsVisitantesEmpresaAcesso | TIntegerField | outro | — | — | — | — | — |
| DsVisitantes | TDataSource | outro | — | — | — | — | — |
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
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActIncluir | TAction | ação | Incluir (Ctrl+I) | — | — | — | — |
| ActAlterar | TAction | ação | Alterar (Ctrl+E) | — | — | — | — |
| ActExcluir | TAction | ação | Excluir (Ctrl+Del) | — | — | — | — |
| ActFechar | TAction | ação | Fechar | — | — | — | — |
| ActIr | TAction | ação | Buscar | — | — | — | — |
| ActExibirTudo | TAction | ação | Exibir tudo (Ctrl+T) | — | — | — | — |
| ActLocalizarCodigo | TAction | ação | Localizar por Código(Ctrl+A) | — | — | — | — |
| ActLocalizarNome | TAction | ação | Localizar por Nome(Ctrl+B) | — | — | — | — |
| ActSalvar | TAction | ação | Salvar (Ctrl+S) | — | — | — | — |
| ActCancelar | TAction | ação | Cancelar (Ctrl+D) | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActCadastrarEmpresa | TAction | ação | Cadastrar empresa (Ctrl+N) | — | — | — | — |
| ActHistoricoVisitas | TAction | ação | Histórico de visitas (Ctrl+H) | — | — | — | — |
| ActProcurar | TAction | ação | Procurar (Ctrl+F) | — | — | — | — |
| ActCamera | TAction | ação | Câmera (Ctrl+C) | — | — | — | — |
| ActSalvarFoto | TAction | ação | Salvar (Ctrl+Alt+S) | — | — | — | — |
| ActLimparFoto | TAction | ação | Limpar (Alt+Del) | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 713 | `TEstadoVisitaController.Create`, `FEstadoVisitaController.SetConexao`, `TConfigEtiquetaController.Create`, `FConfigEtiquetaController.AcbrEtiqueta`, `TPreCadastroController.Create`, `FVisitantesTerceirosController.SetConexao`, `TFaixaAcessoColetoresController.Create`, `FFaixaAcessoColetoresController.SetConexao` |
| `ActExibirTudoExecute` | 1265 | — |
| `ActIrExecute` | 1271 | — |
| `ActIncluirExecute` | 1290 | — |
| `ActExcluirExecute` | 1315 | `TVisitantesTerceirosHistoricosController.Create`, `FVisitantesTerceirosHistoricosController.SetConexao`, `FVisitantesTerceirosController.Excluir`, `FVisitantesTerceirosHistoricosController.ExcluirVisitante`, `FVisitantesTerceirosHistoricosController.Free` |
| `ActSalvarExecute` | 1401 | `FVisitantesTerceirosController.GetPessoa` |
| `ActCancelarExecute` | 1450 | — |
| `ValidarCampos` | 1560 | `FCrachasController.VerificaCPFVinculado` |
| `GravaCampos` | 1650 | `FVisitantesTerceirosController.Inserir`, `FVisitantesTerceirosController.Atualizar` |
| `GravaFoto` | 1756 | `TFaceControlIdController.Create`, `FFaceControlIdController.SetConexao`, `FFaceControlIdController.GetFacePorPessoa`, `FFaceControlIdController.Excluir`, `FFaceControlIdController.Inserir` |
| `ActSalvarFotoExecute` | 2002 | `FVisitantesTerceirosController.GetPessoa` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 327: `Não foi possível comunicar o encerramento ao equipamento.`
- Linha 1128: `Selecione pelo menos um visitante/terceiro para encerrar visitas.`
- Linha 1133: `Deseja encerrar as visitas em aberto dos %d selecionados?`
- Linha 1164: `Falha na comunicação com alguns equipamentos. Deseja continuar mesmo assim?`
- Linha 1193: `%d visitas foram encerradas com sucesso.`
- Linha 1196: `Nenhuma visita foi encerrada.`
- Linha 1333: `Selecione um visitante/terceiro para excluir.`
- Linha 1344: `Registro inválido selecionado.`
- Linha 1351: `Este visitante possui visitas em aberto. `
- Linha 1361: `Excluir o registro: %s?`
- Linha 1387: `Registro excluído com sucesso!`
- Linha 1390: `Problemas com a exclusão no Banco de Dados!`
- Linha 1413: `A foto não está salva. Deseja salvar?`
- Linha 1444: `Problemas com a gravação no Banco de Dados!`
- Linha 1571: `O nome deve ser preenchido`
- Linha 1583: `O CPF deve ser preenchido.`
- Linha 1590: `O CPF deve ter 11 dígitos.`
- Linha 1597: `CPF Inválido.`
- Linha 1629: `A empresa deve ser preenchida para Terceiros.`
- Linha 1700: `Erro ao gravar: `
- Linha 1782: `Foto removida com sucesso`
- Linha 1784: `Erro ao remover foto`
- Linha 1830: `Foto atualizada com sucesso`
- Linha 1832: `Erro ao atualizar foto`
- Linha 1835: `Erro ao atualizar foto`
- Linha 1848: `Foto salva com sucesso`
- Linha 1850: `Erro ao salvar foto`
- Linha 1907: `Selecione um visitante/terceiro válido.`
- Linha 2014: `Problemas com a gravação no Banco de Dados!`
- Linha 2020: `Problemas com a gravação no Banco de Dados!`
- Linha 2046: `Este visitante/terceiro não está cadastrado. Deseja salvar?`
- Linha 2076: `Selecione um visitante/terceiro válido.`
- Linha 2115: `CPF Inválido.`
- Linha 2121: `O CPF tem 11 números.`
- Linha 2154: `Empresa de Acesso não cadastrada`
- Linha 2169: `Data Inválida!`
- Linha 2179: `Hora Inválida!`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
