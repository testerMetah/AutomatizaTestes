# Refeitório > Consultas > Auditorias/Históricos...

> Inventário estático de `Acesso/UFrmAuditoriaHistoricoRefeitorio.dfm` e `Acesso/UFrmAuditoriaHistoricoRefeitorio.pas` no commit `28074dd`. Esta ficha ainda precisa de análise manual das regras de Salvar, Consultar, Excluir, Cancelar e Relatório. Não usar como resultado esperado de teste sem conferir o build instalado.

- Form: `TFrmAuditoriaHistoricoRefeitorio`
- Abertura: `acConAudiHistExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FrmAuditoriaHistoricoRefeitorio` | `TFrmAuditoriaHistoricoRefeitorio` | Auditorias/Históricos | — | `—` | — | Visible=True | — |
| `MetaEquipLocalizar1` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `PnlFundo` | `TPanel` | — | 0 | `—` | — | — | — |
| `BtnContarRegistros` | `THoverSpeedButton` | Contar Registros (F5) | 0 | `—` | — | — | Action=ActContarRegistros, OnClick=ActContarRegistrosExecute |
| `BtnConsultar` | `THoverSpeedButton` | Consultar (F6) | 1 | `—` | — | — | Action=ActConsultar, OnClick=ActConsultarExecute |
| `HoverSpeedButton1` | `THoverSpeedButton` | Relatório (F7) | 2 | `—` | — | — | OnClick=HoverSpeedButton1Click |
| `Pgc_Auditoria` | `TPageControl` | — | 1 | `—` | — | — | OnChange=Pgc_AuditoriaChange |
| `Tbs_Cardapios` | `TTabSheet` | Cardápios | — | `—` | — | — | — |
| `Grid_Cardapios` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `Tbs_FilaComandos` | `TTabSheet` | Fila/Comandos | — | `—` | — | — | — |
| `Grid_FilaComandos` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `Tbs_Refeicoes` | `TTabSheet` | Refeições | — | `—` | — | — | — |
| `Grid_Refeicoes` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `Tbs_RefeicoesReservas` | `TTabSheet` | Refeições Reservas | — | `—` | — | — | — |
| `Grid_RefeicoesReservas` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `Tbs_Refeitorios` | `TTabSheet` | Refeitórios | — | `—` | — | — | — |
| `Grid_Refeitorios` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `Tbs_RegrasAcesso` | `TTabSheet` | Regras Acesso | — | `—` | — | — | — |
| `Grid_RegrasAcesso` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `Panel3` | `TPanel` | — | 2 | `—` | — | — | — |
| `PaginaLoc` | `TPageControl` | — | 0 | `—` | — | — | — |
| `TbsPeriodo` | `TTabSheet` | Período (Ctrl+A) | — | `—` | — | — | — |
| `LblDe` | `TLabel` | De | — | `—` | — | — | — |
| `LblAte` | `TLabel` | Até | — | `—` | — | — | — |
| `dtInicio` | `TMaskEdit` | — | 0 | `!99/99/9999;1; ` | 10 | Text=  /  /     | OnExit=dtInicioExit |
| `DtTermino` | `TMaskEdit` | — | 2 | `!99/99/9999;1; ` | 10 | Text=  /  /     | OnExit=dtInicioExit |
| `tmInicio` | `TMaskEdit` | — | 1 | `!99:99;1; ` | 5 | Text=  :   | OnExit=tmInicioExit |
| `TmTermino` | `TMaskEdit` | — | 3 | `!99:99;1; ` | 5 | Text=  :   | OnExit=tmInicioExit |
| `TbsColetorFuncao` | `TTabSheet` | Coletor/Função (Ctrl+D) | — | `—` | — | — | — |
| `lblCampoColetor` | `TLabel` | Coletor | — | `—` | — | — | — |
| `LblFuncao` | `TLabel` | Função | — | `—` | — | — | — |
| `mlColetor` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `lblColetor` | `TLabel` | lblColetor | — | `—` | — | — | — |
| `edColetor` | `TEdit` | — | 0 | `—` | — | — | OnExit=edColetorExit |
| `EdFuncao` | `TEdit` | — | 1 | `—` | — | — | — |
| `TbsSituacao` | `TTabSheet` | Situação (Ctrl+G) | — | `—` | — | — | — |
| `LblSituacao` | `TLabel` | Situação | — | `—` | — | — | — |
| `CmbSituacao` | `TComboBox` | — | 0 | `—` | — | Text=Ambos, ItemIndex=2 | — |
| `TbsPessoa` | `TTabSheet` | Pessoa (Ctrl+H) | — | `—` | — | — | — |
| `mlPessoa` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `lblPessoa` | `TLabel` | lblPessoa | — | `—` | — | — | — |
| `LblCampoPessoa` | `TLabel` | Pessoa | — | `—` | — | — | — |
| `EdPessoa` | `TEdit` | — | 0 | `—` | — | Text=EdPessoa | OnExit=EdPessoaExit |
| `TbsPreCadastro` | `TTabSheet` | Pré-Cadastro (Ctrl+I) | — | `—` | — | — | — |
| `mlPreCadastro` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `Lbl_PreCadastro` | `TLabel` | Lbl_PreCadastro | — | `—` | — | — | — |
| `Label2` | `TLabel` | Pré-Cadastro | — | `—` | — | — | — |
| `Edt_PreCadastro` | `TEdit` | — | 0 | `—` | — | Text=Edt_PreCadastro | OnExit=Edt_PreCadastroExit |
| `TbsUsuario` | `TTabSheet` | Usuário (Ctrl+J) | — | `—` | — | — | — |
| `Label1` | `TLabel` | Usuário | — | `—` | — | — | — |
| `mlUsuario` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `lblUsuario` | `TLabel` | lblUsuario | — | `—` | — | — | — |
| `EdUsuario` | `TEdit` | — | 0 | `—` | — | Text=EdUsuario | OnExit=EdUsuarioExit |
| `TbsRefeitorios` | `TTabSheet` | Refeitórios (Ctrl+L) | — | `—` | — | — | — |
| `Label12` | `TLabel` | Refeitório | — | `—` | — | — | — |
| `lblRefeitorioFiltro` | `TLabel` | lblRefeitorio | — | `—` | — | — | — |
| `mlRefeitorio` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `EdRefeitorio` | `TEdit` | — | 0 | `—` | — | Text=EdRefeitorio | OnExit=EdRefeitorioExit |
| `TbsCardapios` | `TTabSheet` | Cardápios (Ctrl+M) | — | `—` | — | — | — |
| `Label13` | `TLabel` | Cardápio | — | `—` | — | — | — |
| `mlCardapio` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `lblCardapioFiltro` | `TLabel` | lblRefeitorio | — | `—` | — | — | — |
| `EdCardapio` | `TEdit` | — | 0 | `—` | — | Text=EdCardapio | OnExit=EdCardapioExit |
| `BtnLimparFiltros` | `THoverSpeedButton` | Limpar Filtros (Ctrl+X) | 1 | `—` | — | — | Action=ActLimparFiltros, OnClick=ActLimparFiltrosExecute |
| `ActionList1` | `TActionList` | — | — | `—` | — | — | — |
| `ActFechar` | `TAction` | Fechar (Alt+F4) | — | `—` | — | — | — |
| `ActLimparFiltros` | `TAction` | Limpar Filtros (Ctrl+X) | — | `—` | — | — | — |
| `ActLocalizarPessoa` | `TAction` | ActLocalizarPessoa | — | `—` | — | — | — |
| `ActConsultar` | `TAction` | Consultar (F6) | — | `—` | — | — | — |
| `ActPeriodo` | `TAction` | ActPeriodo | — | `—` | — | — | — |
| `ActCracha` | `TAction` | ActCracha | — | `—` | — | — | — |
| `ActColetorFuncao` | `TAction` | ActColetorFuncao | — | `—` | — | — | — |
| `ActSentido` | `TAction` | ActSentido | — | `—` | — | — | — |
| `ActTipoColeta` | `TAction` | ActTipoColeta | — | `—` | — | — | — |
| `ActSituacao` | `TAction` | ActSituacao | — | `—` | — | — | — |
| `ActPessoa` | `TAction` | ActPessoa | — | `—` | — | — | — |
| `ActContarRegistros` | `TAction` | Contar Registros (F5) | — | `—` | — | — | — |
| `ActBuscarFiltros` | `TAction` | F4 | — | `—` | — | — | — |
| `ActPreCadastro` | `TAction` | ActPreCadastro | — | `—` | — | — | — |
| `ActUsuarios` | `TAction` | ActUsuarios | — | `—` | — | — | — |
| `ActRefeitorios` | `TAction` | — | — | `—` | — | — | — |
| `ActCardapios` | `TAction` | ActCardapios | — | `—` | — | — | — |
| `Cds_Cardapioshora_ini` | `TTimeField` | — | — | `—` | — | — | — |
| `Cds_Cardapioshora_fim` | `TTimeField` | — | — | `—` | — | — | — |
| `Cds_Cardapioshora_ini_reserva` | `TTimeField` | — | — | `—` | — | — | — |
| `Cds_Cardapioshora_fim_reserva` | `TTimeField` | — | — | `—` | — | — | — |
| `frxRelCardapios` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Memo28` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `NomeEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo23` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo25` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo24` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line17` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line18` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo27` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo30` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo37` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo16` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line4` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo19` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line7` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo22` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line13` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line19` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line21` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo31` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line24` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo33` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line26` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo35` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MasterData2` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Memo32` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo29` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo20` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line16` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line23` | `TfrxLineView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_operacao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_final` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo17` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line5` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line6` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo26` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line15` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line20` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line22` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line25` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo34` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line27` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo36` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo38` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBCardapios` | `TfrxDBDataset` | — | — | `—` | — | — | — |
| `frxRelRefeicoes` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `NomeEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo23` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo25` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo24` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line17` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line18` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo27` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo30` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo37` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo19` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line7` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo22` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line13` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line19` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line21` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo31` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line26` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo28` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo33` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line24` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo35` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line29` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo38` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `MasterData2` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Line16` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line23` | `TfrxLineView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_operacao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_final` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo17` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line6` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo20` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo26` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line20` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo29` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line25` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo32` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line27` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line28` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line22` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo34` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo36` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line30` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo39` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBRefeicoes` | `TfrxDBDataset` | — | — | `—` | — | — | — |
| `frxRefeicoesReservas` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `NomeEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo23` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo25` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo24` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line17` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line18` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo30` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo37` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line7` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo22` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line19` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo31` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line26` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo28` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line24` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo35` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line29` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo38` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line21` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo27` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo33` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo40` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line31` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `MasterData2` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Line16` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line23` | `TfrxLineView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_operacao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_final` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line6` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo20` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo26` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line20` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo29` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line25` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line27` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line22` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo36` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line30` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo39` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo32` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo34` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line28` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo41` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Child1` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo42` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo43` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBRefeicoesReservas` | `TfrxDBDataset` | — | — | `—` | — | — | — |
| `frxRelRefeitorios` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `NomeEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo23` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo25` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo24` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line17` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line18` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo27` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo30` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo37` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo16` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line4` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo19` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line7` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo22` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line13` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line19` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo28` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MasterData2` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Line16` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line23` | `TfrxLineView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_operacao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_final` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo17` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line5` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line6` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo20` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo26` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line20` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo29` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo38` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line21` | `TfrxLineView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxBDRefeitorios` | `TfrxDBDataset` | — | — | `—` | — | — | — |
| `frxRelFilaComandos` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `NomeEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo1` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo14` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line6` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line7` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line11` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line15` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line13` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo23` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo25` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo19` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line8` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo20` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo15` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line20` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo16` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line21` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo18` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo22` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line22` | `TfrxLineView` | — | — | `—` | — | — | — |
| `MasterData2` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Shape6` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Line16` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line17` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line9` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line23` | `TfrxLineView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_operacao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_inicial` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_final` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao1` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1id_usuario` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line24` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo17` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo24` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line25` | `TfrxLineView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Child1` | `TfrxChild` | — | — | `—` | — | — | — |
| `Shape4` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Memo26` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line26` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo30` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Child2` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo27` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo31` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line27` | `TfrxLineView` | — | — | `—` | — | — | — |
| `frxDBFilaComandos` | `TfrxDBDataset` | — | — | `—` | — | — | — |
| `frxRelRegrasAcesso` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `NomeEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo23` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo25` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo24` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo26` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line17` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line18` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo27` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo30` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo37` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line21` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line33` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo46` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line35` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo48` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line38` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo49` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MasterData2` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Line16` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line23` | `TfrxLineView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_operacao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_final` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao1` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo17` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line25` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line34` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line36` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo47` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line37` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo50` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo51` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `ChildPessoas` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo28` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line19` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line20` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo29` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo31` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line24` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo32` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `ChildPessoasCabecalho` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo33` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line27` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo34` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line28` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo35` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line29` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo36` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `ChildPreCadastroCabecalho` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo38` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line15` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo39` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line22` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo40` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line26` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo41` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `ChildPreCadastro` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo42` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line30` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line31` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo43` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo44` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line32` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo45` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Child_SetoresCabecalho` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo54` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line39` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo55` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line40` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo56` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line41` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo57` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Child_Setores` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo58` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line42` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line43` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo59` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo60` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line44` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo61` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBRegrasAcesso` | `TfrxDBDataset` | — | — | `—` | — | — | — |
| `frxRelRegrasAcessoSintetico` | `TfrxReport` | — | — | `—` | — | — | — |
| `Data` | `TfrxDataPage` | — | — | `—` | — | — | — |
| `Page1` | `TfrxReportPage` | — | — | `—` | — | — | — |
| `PageHeader1` | `TfrxPageHeader` | — | — | `—` | — | — | — |
| `Shape1` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `Shape3` | `TfrxShapeView` | — | — | `—` | — | — | — |
| `NomeEmpresa` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo5` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo6` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MemoNomeRelatorio` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo3` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo4` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo12` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Picture1` | `TfrxPictureView` | — | — | `—` | — | — | — |
| `Memo21` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo23` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo25` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo24` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo26` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line14` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line17` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line18` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo27` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo30` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo37` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line21` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line33` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo46` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line35` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo48` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line38` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo49` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `MasterData2` | `TfrxMasterData` | — | — | `—` | — | — | — |
| `Line16` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line12` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line23` | `TfrxLineView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_operacao` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1data_hora_final` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `frxDBDataset1tipo_selecao1` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo17` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line25` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line34` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Line36` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo47` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line37` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo50` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Memo51` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `PageFooter1` | `TfrxPageFooter` | — | — | `—` | — | — | — |
| `Memo13` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `ChildPessoasCabecalho` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo33` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line27` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo34` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line28` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo35` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line29` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo36` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `ChildPreCadastroCabecalho` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo38` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line15` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo39` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line22` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo40` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line26` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo41` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Child_SetoresCabecalho` | `TfrxChild` | — | — | `—` | — | — | — |
| `Memo54` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line39` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo55` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line40` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo56` | `TfrxMemoView` | — | — | `—` | — | — | — |
| `Line41` | `TfrxLineView` | — | — | `—` | — | — | — |
| `Memo57` | `TfrxMemoView` | — | — | `—` | — | — | — |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 1069: `Aba não configurada`
- Linha 1094: `Possui `
- Linha 1096: `Página não encontrada.`
- Linha 1377: `Data Inválida!`
- Linha 1400: `Cardápio não cadastrado`
- Linha 1429: `Coletor não cadastrado`
- Linha 1458: `Pessoa não cadastrada`
- Linha 1487: `Refeitório não cadastrado`
- Linha 1516: `Pessoa não cadastrada`
- Linha 1545: `Usuário não cadastrado`
- Linha 1697: `Hora Inválida!`
- Linha 1706: `Data de Início deve ser informada.`
- Linha 1713: `A hora de Início deve ser informada.`
- Linha 1720: `Data de Término deve ser informada.`
- Linha 1727: `A hora de Término deve ser informada.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActBuscarFiltrosExecute`
- `ActCardapiosExecute`
- `ActConsultarExecute`
- `ActContarRegistrosExecute`
- `ActLimparFiltrosExecute`
- `ActPeriodoExecute`
- `ActPessoaExecute`
- `ActPreCadastroExecute`
- `ActRefeitoriosExecute`
- `ActUsuariosExecute`
- `MontarRelatorioRegras`
- `ValidarFiltros`

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
