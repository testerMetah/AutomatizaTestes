# Administracao: TFrmAuditoriaHistoricoAdministracao

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Consultas > .

- DFM: `Acesso/UFrmAuditoriaHistoricoAdministracao.dfm`
- PAS: `Acesso/UFrmAuditoriaHistoricoAdministracao.pas`
- Handler de abertura: `actConsultasHistoricosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmAuditoriaHistoricoAdministracao | TFrmAuditoriaHistoricoAdministracao | outro | Consulta de Usuários | — | — | — | Visible=True |
| MetaEquipLocalizar1 | TMetaEquipLocalizar | outro | — | — | — | — | — |
| PnlFundo | TPanel | contêiner | — | 0 | — | — | — |
| BtnContarRegistros | THoverSpeedButton | ação | Contar Registros (F5) | 0 | — | — | — |
| BtnConsultar | THoverSpeedButton | ação | Consultar (F6) | 1 | — | — | — |
| HoverSpeedButton1 | THoverSpeedButton | ação | Relatório (F7) | 2 | — | — | — |
| Panel3 | TPanel | contêiner | — | 1 | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | 0 | — | — | — |
| TbsPeriodo | TTabSheet | contêiner | Período (Ctrl+A) | — | — | — | — |
| LblDe | TLabel | rótulo | De | — | — | — | — |
| LblAte | TLabel | rótulo | Até | — | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| DtTermino | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| TmTermino | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| TbsUsuario | TTabSheet | contêiner | Usuário (Ctrl+B) | — | — | — | — |
| Label1 | TLabel | rótulo | Usuário | — | — | — | — |
| mlUsuario | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblUsuario | TLabel | rótulo | lblUsuario | — | — | — | — |
| EdUsuario | TEdit | campo de texto/data | — | 0 | — | — | Text=EdUsuario |
| BtnLimparFiltros | THoverSpeedButton | ação | Limpar Filtros (Ctrl+X) | 1 | — | — | — |
| Pgc_Auditoria | TPageControl | contêiner | — | 2 | — | — | — |
| Tbs_Usuarios | TTabSheet | contêiner | Usuários | — | — | — | — |
| Grid_Usuarios | TDBGrid | grade | — | 0 | — | — | Visible=True |
| Tbs_Acessus_Sync_Agendamentos | TTabSheet | contêiner | Agendamentos Acessus Sync | — | — | — | — |
| Grid_Agendamentos | TDBGrid | grade | — | 0 | — | — | Visible=True |
| Tbs_Acessus_Sync_Tarefas | TTabSheet | contêiner | Tarefas Acessus Sync | — | — | — | — |
| Grid_Tarefas | TDBGrid | grade | — | 0 | — | — | Visible=True |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActFechar | TAction | ação | Fechar (Alt+F4) | — | — | — | — |
| ActLimparFiltros | TAction | ação | Limpar Filtros (Ctrl+X) | — | — | — | — |
| ActLocalizarPessoa | TAction | ação | ActLocalizarPessoa | — | — | — | — |
| ActConsultar | TAction | ação | Consultar (F6) | — | — | — | — |
| ActPeriodo | TAction | ação | ActPeriodo | — | — | — | — |
| ActContarRegistros | TAction | ação | Contar Registros (F5) | — | — | — | — |
| ActBuscarFiltros | TAction | ação | F4 | — | — | — | — |
| ActUsuarios | TAction | ação | ActUsuarios | — | — | — | — |
| Cds_Usuarios | TClientDataSet | outro | — | — | — | — | — |
| Cds_Usuariosid | TIntegerField | outro | — | — | — | — | — |
| Cds_Usuariosid_usuario | TIntegerField | outro | — | — | — | — | — |
| Cds_Usuariosid_empresa | TIntegerField | outro | — | — | — | — | — |
| Cds_Usuariosid_usuario_alterou | TIntegerField | outro | — | — | — | — | — |
| Cds_Usuariosid_empresa_alterou | TIntegerField | outro | — | — | — | — | — |
| Cds_Usuariosnome | TStringField | outro | — | — | — | — | — |
| Cds_Usuariossenha | TStringField | outro | — | — | — | — | — |
| Cds_Usuariospermissoes | TStringField | outro | — | — | — | — | — |
| Cds_Usuariosadministrador | TStringField | outro | — | — | — | — | — |
| Cds_Usuariostipo_operacao | TStringField | outro | — | — | — | — | — |
| Cds_Usuariosobservacao | TStringField | outro | — | — | — | — | — |
| Cds_Usuariosip_maquina | TStringField | outro | — | — | — | — | — |
| Cds_Usuariosnome_maquina | TStringField | outro | — | — | — | — | — |
| Cds_Usuariosstatus | TIntegerField | outro | — | — | — | — | — |
| Cds_Usuariospermissoes_adicionadas | TStringField | outro | — | — | — | — | — |
| Cds_Usuariospermissoes_removidas | TStringField | outro | — | — | — | — | — |
| Cds_Usuariostipo_operacao_desc | TStringField | outro | — | — | — | — | — |
| Cds_Usuariosdata_hora_operacao | TDateTimeField | outro | — | — | — | — | — |
| Dts_Usuarios | TDataSource | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentos | TClientDataSet | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosid | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosid_acessusyn_agendamentos | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosid_tarefa | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosid_usuario | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosid_empresa | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosdescricao | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosdiasemanas | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosperiodicamente | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosstatus | TBooleanField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentostipo_operacao | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosobservacao | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosip_maquina | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosnome_maquina | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentosdata_hora | TDateTimeField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentostipo_operacao_desc | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Agendamentoshorarios | TStringField | outro | — | — | — | — | — |
| Dts_Acessus_Agendamento | TDataSource | outro | — | — | — | — | — |
| Cds_Acessus_Tarefas | TClientDataSet | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasid | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasid_acessussync_tarefas | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasid_usuario | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasid_empresa | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasdescricao | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefastipo | TIntegerField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasstatus | TBooleanField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefastipo_operacao | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasobservacao | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasip_maquina | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefastipo_operacao_desc | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasnome_maquina | TStringField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasdata_hora | TDateTimeField | outro | — | — | — | — | — |
| Cds_Acessus_Tarefasopcoes | TStringField | outro | — | — | — | — | — |
| Dts_Acessus_Tarefas | TDataSource | outro | — | — | — | — | — |
| frxRelUsuarios | TfrxReport | outro | — | — | — | — | — |
| Data | TfrxDataPage | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Shape1 | TfrxShapeView | outro | — | — | — | — | — |
| Shape3 | TfrxShapeView | outro | — | — | — | — | — |
| NomeEmpresa | TfrxMemoView | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo6 | TfrxMemoView | outro | — | — | — | — | — |
| MemoNomeRelatorio | TfrxMemoView | outro | — | — | — | — | — |
| Memo3 | TfrxMemoView | outro | — | — | — | — | — |
| Memo4 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| Picture1 | TfrxPictureView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| Memo23 | TfrxMemoView | outro | — | — | — | — | — |
| Memo25 | TfrxMemoView | outro | — | — | — | — | — |
| Memo24 | TfrxMemoView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line17 | TfrxLineView | outro | — | — | — | — | — |
| Line18 | TfrxLineView | outro | — | — | — | — | — |
| Memo27 | TfrxMemoView | outro | — | — | — | — | — |
| Memo30 | TfrxMemoView | outro | — | — | — | — | — |
| Memo37 | TfrxMemoView | outro | — | — | — | — | — |
| Line1 | TfrxLineView | outro | — | — | — | — | — |
| Memo16 | TfrxMemoView | outro | — | — | — | — | — |
| Line4 | TfrxLineView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Line7 | TfrxLineView | outro | — | — | — | — | — |
| Memo22 | TfrxMemoView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line23 | TfrxLineView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_operacao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_final | TfrxMemoView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Line25 | TfrxLineView | outro | — | — | — | — | — |
| Line5 | TfrxLineView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| Line6 | TfrxLineView | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| Memo26 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| frxDBUsuarios | TfrxDBDataset | outro | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| frxDBAgendamentos | TfrxDBDataset | outro | — | — | — | — | — |
| frxRelAgendamentos | TfrxReport | outro | — | — | — | — | — |
| Data | TfrxDataPage | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Shape1 | TfrxShapeView | outro | — | — | — | — | — |
| Shape3 | TfrxShapeView | outro | — | — | — | — | — |
| NomeEmpresa | TfrxMemoView | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo6 | TfrxMemoView | outro | — | — | — | — | — |
| MemoNomeRelatorio | TfrxMemoView | outro | — | — | — | — | — |
| Memo3 | TfrxMemoView | outro | — | — | — | — | — |
| Memo4 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| Picture1 | TfrxPictureView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| Memo23 | TfrxMemoView | outro | — | — | — | — | — |
| Memo25 | TfrxMemoView | outro | — | — | — | — | — |
| Memo24 | TfrxMemoView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line17 | TfrxLineView | outro | — | — | — | — | — |
| Line18 | TfrxLineView | outro | — | — | — | — | — |
| Memo27 | TfrxMemoView | outro | — | — | — | — | — |
| Memo30 | TfrxMemoView | outro | — | — | — | — | — |
| Memo37 | TfrxMemoView | outro | — | — | — | — | — |
| Line1 | TfrxLineView | outro | — | — | — | — | — |
| Memo16 | TfrxMemoView | outro | — | — | — | — | — |
| Line4 | TfrxLineView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Line7 | TfrxLineView | outro | — | — | — | — | — |
| Memo22 | TfrxMemoView | outro | — | — | — | — | — |
| Line13 | TfrxLineView | outro | — | — | — | — | — |
| Memo28 | TfrxMemoView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line23 | TfrxLineView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_operacao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_final | TfrxMemoView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Line25 | TfrxLineView | outro | — | — | — | — | — |
| Line5 | TfrxLineView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| Line6 | TfrxLineView | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| Memo26 | TfrxMemoView | outro | — | — | — | — | — |
| Line19 | TfrxLineView | outro | — | — | — | — | — |
| Memo29 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| frxRelTarefas | TfrxReport | outro | — | — | — | — | — |
| Data | TfrxDataPage | outro | — | — | — | — | — |
| Page1 | TfrxReportPage | outro | — | — | — | — | — |
| PageHeader1 | TfrxPageHeader | outro | — | — | — | — | — |
| Shape1 | TfrxShapeView | outro | — | — | — | — | — |
| Shape3 | TfrxShapeView | outro | — | — | — | — | — |
| NomeEmpresa | TfrxMemoView | outro | — | — | — | — | — |
| Memo5 | TfrxMemoView | outro | — | — | — | — | — |
| Memo6 | TfrxMemoView | outro | — | — | — | — | — |
| MemoNomeRelatorio | TfrxMemoView | outro | — | — | — | — | — |
| Memo3 | TfrxMemoView | outro | — | — | — | — | — |
| Memo4 | TfrxMemoView | outro | — | — | — | — | — |
| Memo12 | TfrxMemoView | outro | — | — | — | — | — |
| Picture1 | TfrxPictureView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| Memo23 | TfrxMemoView | outro | — | — | — | — | — |
| Memo25 | TfrxMemoView | outro | — | — | — | — | — |
| Memo24 | TfrxMemoView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line17 | TfrxLineView | outro | — | — | — | — | — |
| Line18 | TfrxLineView | outro | — | — | — | — | — |
| Memo27 | TfrxMemoView | outro | — | — | — | — | — |
| Memo30 | TfrxMemoView | outro | — | — | — | — | — |
| Memo37 | TfrxMemoView | outro | — | — | — | — | — |
| Memo16 | TfrxMemoView | outro | — | — | — | — | — |
| Line4 | TfrxLineView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Line7 | TfrxLineView | outro | — | — | — | — | — |
| Line13 | TfrxLineView | outro | — | — | — | — | — |
| Memo28 | TfrxMemoView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line23 | TfrxLineView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_operacao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_final | TfrxMemoView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Line5 | TfrxLineView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| Line6 | TfrxLineView | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| Line19 | TfrxLineView | outro | — | — | — | — | — |
| Memo29 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| frxDBTarefas | TfrxDBDataset | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActConsultarExecute` | 422 | — |
| `FormCreate` | 574 | `TUsuariosController.Create`, `FUsuariosController.SetConexao`, `TAcessusAgendamentosController.Create`, `FAcessusAgendamentoController.SetConexao`, `TAcessusTarefasController.Create`, `FAcessusTarefasController.SetConexao` |
| `ValidarFiltros` | 697 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 437: `Possui `
- Linha 440: `Possui `
- Linha 442: `Possui `
- Linha 529: `Data Inválida!`
- Linha 552: `Usuário não cadastrado`
- Linha 692: `Hora Inválida!`
- Linha 701: `Data de Início deve ser informada.`
- Linha 708: `A hora de Início deve ser informada.`
- Linha 715: `Data de Término deve ser informada.`
- Linha 722: `A hora de Término deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
