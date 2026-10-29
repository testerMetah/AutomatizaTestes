# Estacionamento: TFrmAuditoriaHistoricoEstacionamento

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Consultas > .

- DFM: `Acesso/UFrmAuditoriaHistoricoEstacionamento.dfm`
- PAS: `Acesso/UFrmAuditoriaHistoricoEstacionamento.pas`
- Handler de abertura: `actConsultasHistoricosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmAuditoriaHistoricoEstacionamento | TFrmAuditoriaHistoricoEstacionamento | outro | Auditorias/Históricos | — | — | — | Visible=True |
| MetaEquipLocalizar1 | TMetaEquipLocalizar | outro | — | — | — | — | — |
| PnlFundo | TPanel | contêiner | — | 0 | — | — | — |
| BtnContarRegistros | THoverSpeedButton | ação | Contar Registros (F5) | 0 | — | — | — |
| BtnConsultar | THoverSpeedButton | ação | Consultar (F6) | 1 | — | — | — |
| HoverSpeedButton1 | THoverSpeedButton | ação | Relatório (F7) | 2 | — | — | — |
| Pgc_Auditoria | TPageControl | contêiner | — | 1 | — | — | — |
| Tbs_FilaComandos | TTabSheet | contêiner | Fila/Comandos | — | — | — | — |
| Grid_FilaComandos | TDBGrid | grade | — | 0 | — | — | Visible=True |
| Tbs_RegrasAcesso | TTabSheet | contêiner | Regras Acesso | — | — | — | — |
| Grid_RegrasAcesso | TDBGrid | grade | — | 0 | — | — | Visible=True |
| Tbs_Veiculos | TTabSheet | contêiner | Veículos | — | — | — | — |
| Grid_Veiculos | TDBGrid | grade | — | 0 | — | — | Visible=True |
| Panel3 | TPanel | contêiner | — | 2 | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | 0 | — | — | — |
| TbsPeriodo | TTabSheet | contêiner | Período (Ctrl+A) | — | — | — | — |
| LblDe | TLabel | rótulo | De | — | — | — | — |
| LblAte | TLabel | rótulo | Até | — | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| DtTermino | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| TmTermino | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| TbsColetorFuncao | TTabSheet | contêiner | Coletor (Ctrl+B) | — | — | — | — |
| lblCampoColetor | TLabel | rótulo | Coletor | — | — | — | — |
| mlColetor | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblColetor | TLabel | rótulo | lblColetor | — | — | — | — |
| EdColetor | TEdit | campo de texto/data | — | 0 | — | — | — |
| TbsPessoa | TTabSheet | contêiner | Pessoa (Ctrl+H) | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblPessoa | TLabel | rótulo | lblPessoa | — | — | — | — |
| LblCampoPessoa | TLabel | rótulo | Pessoa | — | — | — | — |
| EdPessoa | TEdit | campo de texto/data | — | 0 | — | — | Text=EdPessoa |
| TbsPreCadastro | TTabSheet | contêiner | Pré-Cadastro (Ctrl+I) | — | — | — | — |
| mlPreCadastro | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| Lbl_PreCadastro | TLabel | rótulo | Lbl_PreCadastro | — | — | — | — |
| Label2 | TLabel | rótulo | Pré-Cadastro | — | — | — | — |
| Edt_PreCadastro | TEdit | campo de texto/data | — | 0 | — | — | Text=Edt_PreCadastro |
| TbsUsuario | TTabSheet | contêiner | Usuário (Ctrl+J) | — | — | — | — |
| Label1 | TLabel | rótulo | Usuário | — | — | — | — |
| mlUsuario | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblUsuario | TLabel | rótulo | lblUsuario | — | — | — | — |
| EdUsuario | TEdit | campo de texto/data | — | 0 | — | — | Text=EdUsuario |
| TbsVeiculos | TTabSheet | contêiner | Veículo (Ctrl+O) | — | — | — | — |
| Label4 | TLabel | rótulo | Veículo | — | — | — | — |
| mlVeiculo | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| Lbl_Veiculo | TLabel | rótulo | Lbl_Veiculo | — | — | — | — |
| EdVeiculo | TEdit | campo de texto/data | — | 0 | — | — | Text=EdVeiculo |
| BtnLimparFiltros | THoverSpeedButton | ação | Limpar Filtros (Ctrl+X) | 1 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActFechar | TAction | ação | Fechar (Alt+F4) | — | — | — | — |
| ActLimparFiltros | TAction | ação | Limpar Filtros (Ctrl+X) | — | — | — | — |
| ActLocalizarPessoa | TAction | ação | ActLocalizarPessoa | — | — | — | — |
| ActConsultar | TAction | ação | Consultar (F6) | — | — | — | — |
| ActPeriodo | TAction | ação | ActPeriodo | — | — | — | — |
| ActPessoa | TAction | ação | ActPessoa | — | — | — | — |
| ActContarRegistros | TAction | ação | Contar Registros (F5) | — | — | — | — |
| ActBuscarFiltros | TAction | ação | F4 | — | — | — | — |
| ActPreCadastro | TAction | ação | ActPreCadastro | — | — | — | — |
| ActUsuarios | TAction | ação | ActUsuarios | — | — | — | — |
| ActVeiculo | TAction | ação | ActVeiculo | — | — | — | — |
| ActColetorFuncao | TAction | ação | ActColetorFuncao | — | — | — | — |
| Dts_RegrasAcesso | TDataSource | outro | — | — | — | — | — |
| Dts_FilaComandos | TDataSource | outro | — | — | — | — | — |
| Cds_Veiculos | TClientDataSet | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField1 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField2 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField3 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosStringField1 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField4 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField5 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField6 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosStringField2 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField7 | TIntegerField | outro | — | — | — | — | — |
| Cds_Veiculostipo_operacao_desc | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField8 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosStringField3 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField9 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField10 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosIntegerField11 | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculosStringField4 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosStringField5 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosStringField6 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosStringField7 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosStringField8 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosStringField9 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosStringField10 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosStringField11 | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosDateTimeField1 | TDateTimeField | outro | — | — | — | — | — |
| Cds_VeiculosnomePessoa | TStringField | outro | — | — | — | — | — |
| Cds_VeiculosidPessoa | TIntegerField | outro | — | — | — | — | — |
| Cds_VeiculostipoPessoa | TStringField | outro | — | — | — | — | — |
| Dts_Veiculos | TDataSource | outro | — | — | — | — | — |
| Cds_RegrasAcesso | TClientDataSet | outro | — | — | — | — | — |
| StringField16 | TStringField | outro | — | — | — | — | — |
| StringField21 | TStringField | outro | — | — | — | — | — |
| DateTimeField4 | TDateTimeField | outro | — | — | — | — | — |
| IntegerField11 | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoid_filtro | TIntegerField | outro | — | — | — | — | — |
| StringField18 | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessotipo_regra | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessotipo_operacao_desc | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessocoletores | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessosetores_antes | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessopessoas_antes | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessoprecadastros_antes | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessoprecadastros_removidos | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessoprecadastros_adicionados | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessopessoas_removidas | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessopessoas_adicionadas | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessosetores_removidos | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessosetores_adicionados | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_setores | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_setores_antes | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_setores_removidos | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_setores_adicionados | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_pessoas | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_pessoas_antes | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_pessoas_removidas | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_pessoas_adicionadas | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_precadastros | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_precadastros_antes | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_precadastros_removidos | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtd_precadastros_adicionados | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessotipo_selecao | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessosetores | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessopessoas | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessoseparar_regra_dia | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessobloquear_sabados | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessoqtde_acesso | TIntegerField | outro | — | — | — | — | — |
| StringField22 | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessoconsidera_pre_cadastro | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessodias_semana | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessotipo_acesso | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessosituacao | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessopre_cadastros | TStringField | outro | — | — | — | — | — |
| Cds_RegrasAcessoid_regra_acesso | TIntegerField | outro | — | — | — | — | — |
| Cds_RegrasAcessodata_hora_inicio | TDateTimeField | outro | — | — | — | — | — |
| Cds_RegrasAcessodata_hora_termino | TDateTimeField | outro | — | — | — | — | — |
| Cds_RegrasAcessobloquear_domingos | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandos | TClientDataSet | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField1 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField2 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosDateTimeField1 | TDateTimeField | outro | — | — | — | — | — |
| Cds_FilaComandosDateTimeField2 | TDateTimeField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField3 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField1 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField2 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField3 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandostipo_operacao_desc | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField4 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField5 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField4 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField5 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField6 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField6 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField7 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField8 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField9 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField7 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField10 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField11 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField8 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField9 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField12 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField13 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField14 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosDateTimeField3 | TDateTimeField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField15 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandosIntegerField10 | TIntegerField | outro | — | — | — | — | — |
| Cds_FilaComandosStringField16 | TStringField | outro | — | — | — | — | — |
| Cds_FilaComandospessoa | TStringField | outro | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| frxRelVeiculos | TfrxReport | outro | — | — | — | — | — |
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
| Memo1 | TfrxMemoView | outro | — | — | — | — | — |
| Memo14 | TfrxMemoView | outro | — | — | — | — | — |
| Line6 | TfrxLineView | outro | — | — | — | — | — |
| Line7 | TfrxLineView | outro | — | — | — | — | — |
| Line11 | TfrxLineView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| Line13 | TfrxLineView | outro | — | — | — | — | — |
| Memo23 | TfrxMemoView | outro | — | — | — | — | — |
| Memo25 | TfrxMemoView | outro | — | — | — | — | — |
| Line8 | TfrxLineView | outro | — | — | — | — | — |
| Line18 | TfrxLineView | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| Memo15 | TfrxMemoView | outro | — | — | — | — | — |
| Memo16 | TfrxMemoView | outro | — | — | — | — | — |
| Line21 | TfrxLineView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| Memo22 | TfrxMemoView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Line20 | TfrxLineView | outro | — | — | — | — | — |
| Line22 | TfrxLineView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line17 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line9 | TfrxLineView | outro | — | — | — | — | — |
| Line23 | TfrxLineView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_operacao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_inicial | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_final | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1id_usuario | TfrxMemoView | outro | — | — | — | — | — |
| Line24 | TfrxLineView | outro | — | — | — | — | — |
| Memo24 | TfrxMemoView | outro | — | — | — | — | — |
| Line19 | TfrxLineView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Memo26 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| frxDBVeiculos | TfrxDBDataset | outro | — | — | — | — | — |
| frxRelFilaComandos | TfrxReport | outro | — | — | — | — | — |
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
| Memo1 | TfrxMemoView | outro | — | — | — | — | — |
| Memo14 | TfrxMemoView | outro | — | — | — | — | — |
| Line6 | TfrxLineView | outro | — | — | — | — | — |
| Line7 | TfrxLineView | outro | — | — | — | — | — |
| Line11 | TfrxLineView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line15 | TfrxLineView | outro | — | — | — | — | — |
| Memo21 | TfrxMemoView | outro | — | — | — | — | — |
| Line13 | TfrxLineView | outro | — | — | — | — | — |
| Memo23 | TfrxMemoView | outro | — | — | — | — | — |
| Memo25 | TfrxMemoView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Line8 | TfrxLineView | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| Memo15 | TfrxMemoView | outro | — | — | — | — | — |
| Line20 | TfrxLineView | outro | — | — | — | — | — |
| Memo16 | TfrxMemoView | outro | — | — | — | — | — |
| Line21 | TfrxLineView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| Memo22 | TfrxMemoView | outro | — | — | — | — | — |
| Line22 | TfrxLineView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Shape6 | TfrxShapeView | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line17 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line9 | TfrxLineView | outro | — | — | — | — | — |
| Line23 | TfrxLineView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_operacao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_inicial | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_final | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao1 | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1id_usuario | TfrxMemoView | outro | — | — | — | — | — |
| Line24 | TfrxLineView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Memo24 | TfrxMemoView | outro | — | — | — | — | — |
| Line25 | TfrxLineView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| Child1 | TfrxChild | outro | — | — | — | — | — |
| Shape4 | TfrxShapeView | outro | — | — | — | — | — |
| Memo26 | TfrxMemoView | outro | — | — | — | — | — |
| Line26 | TfrxLineView | outro | — | — | — | — | — |
| Memo30 | TfrxMemoView | outro | — | — | — | — | — |
| Child2 | TfrxChild | outro | — | — | — | — | — |
| Memo27 | TfrxMemoView | outro | — | — | — | — | — |
| Memo31 | TfrxMemoView | outro | — | — | — | — | — |
| Line27 | TfrxLineView | outro | — | — | — | — | — |
| frxDBFilaComandos | TfrxDBDataset | outro | — | — | — | — | — |
| frxRelRegrasAcesso | TfrxReport | outro | — | — | — | — | — |
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
| Memo26 | TfrxMemoView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line17 | TfrxLineView | outro | — | — | — | — | — |
| Line18 | TfrxLineView | outro | — | — | — | — | — |
| Memo27 | TfrxMemoView | outro | — | — | — | — | — |
| Memo30 | TfrxMemoView | outro | — | — | — | — | — |
| Memo37 | TfrxMemoView | outro | — | — | — | — | — |
| Line21 | TfrxLineView | outro | — | — | — | — | — |
| Line33 | TfrxLineView | outro | — | — | — | — | — |
| Memo46 | TfrxMemoView | outro | — | — | — | — | — |
| Line35 | TfrxLineView | outro | — | — | — | — | — |
| Memo48 | TfrxMemoView | outro | — | — | — | — | — |
| Line38 | TfrxLineView | outro | — | — | — | — | — |
| Memo49 | TfrxMemoView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line23 | TfrxLineView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_operacao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_final | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao1 | TfrxMemoView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Line25 | TfrxLineView | outro | — | — | — | — | — |
| Line34 | TfrxLineView | outro | — | — | — | — | — |
| Line36 | TfrxLineView | outro | — | — | — | — | — |
| Memo47 | TfrxMemoView | outro | — | — | — | — | — |
| Line37 | TfrxLineView | outro | — | — | — | — | — |
| Memo50 | TfrxMemoView | outro | — | — | — | — | — |
| Memo51 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| ChildPessoas | TfrxChild | outro | — | — | — | — | — |
| Memo28 | TfrxMemoView | outro | — | — | — | — | — |
| Line19 | TfrxLineView | outro | — | — | — | — | — |
| Line20 | TfrxLineView | outro | — | — | — | — | — |
| Memo29 | TfrxMemoView | outro | — | — | — | — | — |
| Memo31 | TfrxMemoView | outro | — | — | — | — | — |
| Line24 | TfrxLineView | outro | — | — | — | — | — |
| Memo32 | TfrxMemoView | outro | — | — | — | — | — |
| ChildPessoasCabecalho | TfrxChild | outro | — | — | — | — | — |
| Memo33 | TfrxMemoView | outro | — | — | — | — | — |
| Line27 | TfrxLineView | outro | — | — | — | — | — |
| Memo34 | TfrxMemoView | outro | — | — | — | — | — |
| Line28 | TfrxLineView | outro | — | — | — | — | — |
| Memo35 | TfrxMemoView | outro | — | — | — | — | — |
| Line29 | TfrxLineView | outro | — | — | — | — | — |
| Memo36 | TfrxMemoView | outro | — | — | — | — | — |
| ChildPreCadastroCabecalho | TfrxChild | outro | — | — | — | — | — |
| Memo38 | TfrxMemoView | outro | — | — | — | — | — |
| Line15 | TfrxLineView | outro | — | — | — | — | — |
| Memo39 | TfrxMemoView | outro | — | — | — | — | — |
| Line22 | TfrxLineView | outro | — | — | — | — | — |
| Memo40 | TfrxMemoView | outro | — | — | — | — | — |
| Line26 | TfrxLineView | outro | — | — | — | — | — |
| Memo41 | TfrxMemoView | outro | — | — | — | — | — |
| ChildPreCadastro | TfrxChild | outro | — | — | — | — | — |
| Memo42 | TfrxMemoView | outro | — | — | — | — | — |
| Line30 | TfrxLineView | outro | — | — | — | — | — |
| Line31 | TfrxLineView | outro | — | — | — | — | — |
| Memo43 | TfrxMemoView | outro | — | — | — | — | — |
| Memo44 | TfrxMemoView | outro | — | — | — | — | — |
| Line32 | TfrxLineView | outro | — | — | — | — | — |
| Memo45 | TfrxMemoView | outro | — | — | — | — | — |
| Child_SetoresCabecalho | TfrxChild | outro | — | — | — | — | — |
| Memo54 | TfrxMemoView | outro | — | — | — | — | — |
| Line39 | TfrxLineView | outro | — | — | — | — | — |
| Memo55 | TfrxMemoView | outro | — | — | — | — | — |
| Line40 | TfrxLineView | outro | — | — | — | — | — |
| Memo56 | TfrxMemoView | outro | — | — | — | — | — |
| Line41 | TfrxLineView | outro | — | — | — | — | — |
| Memo57 | TfrxMemoView | outro | — | — | — | — | — |
| Child_Setores | TfrxChild | outro | — | — | — | — | — |
| Memo58 | TfrxMemoView | outro | — | — | — | — | — |
| Line42 | TfrxLineView | outro | — | — | — | — | — |
| Line43 | TfrxLineView | outro | — | — | — | — | — |
| Memo59 | TfrxMemoView | outro | — | — | — | — | — |
| Memo60 | TfrxMemoView | outro | — | — | — | — | — |
| Line44 | TfrxLineView | outro | — | — | — | — | — |
| Memo61 | TfrxMemoView | outro | — | — | — | — | — |
| frxDBRegrasAcesso | TfrxDBDataset | outro | — | — | — | — | — |
| frxRelRegrasAcessoSintetico | TfrxReport | outro | — | — | — | — | — |
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
| Memo26 | TfrxMemoView | outro | — | — | — | — | — |
| Line14 | TfrxLineView | outro | — | — | — | — | — |
| Line17 | TfrxLineView | outro | — | — | — | — | — |
| Line18 | TfrxLineView | outro | — | — | — | — | — |
| Memo27 | TfrxMemoView | outro | — | — | — | — | — |
| Memo30 | TfrxMemoView | outro | — | — | — | — | — |
| Memo37 | TfrxMemoView | outro | — | — | — | — | — |
| Line21 | TfrxLineView | outro | — | — | — | — | — |
| Line33 | TfrxLineView | outro | — | — | — | — | — |
| Memo46 | TfrxMemoView | outro | — | — | — | — | — |
| Line35 | TfrxLineView | outro | — | — | — | — | — |
| Memo48 | TfrxMemoView | outro | — | — | — | — | — |
| Line38 | TfrxLineView | outro | — | — | — | — | — |
| Memo49 | TfrxMemoView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line23 | TfrxLineView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_operacao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_final | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1tipo_selecao1 | TfrxMemoView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Line25 | TfrxLineView | outro | — | — | — | — | — |
| Line34 | TfrxLineView | outro | — | — | — | — | — |
| Line36 | TfrxLineView | outro | — | — | — | — | — |
| Memo47 | TfrxMemoView | outro | — | — | — | — | — |
| Line37 | TfrxLineView | outro | — | — | — | — | — |
| Memo50 | TfrxMemoView | outro | — | — | — | — | — |
| Memo51 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| ChildPessoasCabecalho | TfrxChild | outro | — | — | — | — | — |
| Memo33 | TfrxMemoView | outro | — | — | — | — | — |
| Line27 | TfrxLineView | outro | — | — | — | — | — |
| Memo34 | TfrxMemoView | outro | — | — | — | — | — |
| Line28 | TfrxLineView | outro | — | — | — | — | — |
| Memo35 | TfrxMemoView | outro | — | — | — | — | — |
| Line29 | TfrxLineView | outro | — | — | — | — | — |
| Memo36 | TfrxMemoView | outro | — | — | — | — | — |
| ChildPreCadastroCabecalho | TfrxChild | outro | — | — | — | — | — |
| Memo38 | TfrxMemoView | outro | — | — | — | — | — |
| Line15 | TfrxLineView | outro | — | — | — | — | — |
| Memo39 | TfrxMemoView | outro | — | — | — | — | — |
| Line22 | TfrxLineView | outro | — | — | — | — | — |
| Memo40 | TfrxMemoView | outro | — | — | — | — | — |
| Line26 | TfrxLineView | outro | — | — | — | — | — |
| Memo41 | TfrxMemoView | outro | — | — | — | — | — |
| Child_SetoresCabecalho | TfrxChild | outro | — | — | — | — | — |
| Memo54 | TfrxMemoView | outro | — | — | — | — | — |
| Line39 | TfrxLineView | outro | — | — | — | — | — |
| Memo55 | TfrxMemoView | outro | — | — | — | — | — |
| Line40 | TfrxLineView | outro | — | — | — | — | — |
| Memo56 | TfrxMemoView | outro | — | — | — | — | — |
| Line41 | TfrxLineView | outro | — | — | — | — | — |
| Memo57 | TfrxMemoView | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `MontarRelatorioRegras` | 667 | — |
| `ActConsultarExecute` | 696 | — |
| `FormCreate` | 1100 | `THistoricoFilaComandosController.Create`, `FHistoricoFilaComandosController.SetConexao`, `TRegrasAcessoController.Create`, `FHistoricoRegraAcessosController.SetConexao`, `TVeiculosController.Create`, `FHistoricoVeiculosController.SetConexao` |
| `ValidarFiltros` | 1214 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 721: `Aba não configurada`
- Linha 743: `Possui `
- Linha 745: `Página não encontrada.`
- Linha 939: `Data Inválida!`
- Linha 962: `Coletor não cadastrado`
- Linha 991: `Pessoa não cadastrada`
- Linha 1020: `Veículo não cadastrado`
- Linha 1049: `Pessoa não cadastrada`
- Linha 1078: `Usuário não cadastrado`
- Linha 1209: `Hora Inválida!`
- Linha 1218: `Data de Início deve ser informada.`
- Linha 1225: `A hora de Início deve ser informada.`
- Linha 1232: `Data de Término deve ser informada.`
- Linha 1239: `A hora de Término deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
