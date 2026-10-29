# Portaria: TFrmAuditoriaHistoricoPortaria

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Consultas > Auditorias/Históricos....

- DFM: `Acesso/UFrmAuditoriaHistoricoPortaria.dfm`
- PAS: `Acesso/UFrmAuditoriaHistoricoPortaria.pas`
- Handler de abertura: `acConsAudiHistExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmAuditoriaHistoricoPortaria | TFrmAuditoriaHistoricoPortaria | outro | Consulta de Visitantes e Terceiros | — | — | — | Visible=True |
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
| TbsVisitante | TTabSheet | contêiner | Visitante (Ctrl+B) | — | — | — | — |
| Label1 | TLabel | rótulo | Visitante | — | — | — | — |
| mlVisitante | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblVisitante | TLabel | rótulo | lblVisitante | — | — | — | — |
| EdVisitante | TEdit | campo de texto/data | — | 0 | — | — | Text=EdVisitante |
| TbsCracha | TTabSheet | contêiner | Crachá (Ctrl+C) | — | — | — | — |
| LblCracha | TLabel | rótulo | Número de Crachá | — | — | — | — |
| ednrocracha | TEdit | campo de texto/data | — | 0 | — | — | — |
| TbsColetor | TTabSheet | contêiner | Coletor (Ctrl+D) | — | — | — | — |
| lblCampoColetor | TLabel | rótulo | Coletor | — | — | — | — |
| mlColetor | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblColetor | TLabel | rótulo | lblColetor | — | — | — | — |
| edColetor | TEdit | campo de texto/data | — | 0 | — | — | — |
| TbsUsuario | TTabSheet | contêiner | Usuário (Ctrl+E) | — | — | — | — |
| Label2 | TLabel | rótulo | Usuário | — | — | — | — |
| mlUsuario | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblUsuario | TLabel | rótulo | lblUsuario | — | — | — | — |
| EdUsuario | TEdit | campo de texto/data | — | 0 | — | — | Text=EdUsuario |
| TbsRefeitorio | TTabSheet | contêiner | Refeitório (Ctrl+F) | — | — | — | — |
| Label12 | TLabel | rótulo | Refeitório | — | — | — | — |
| mlRefeitorio | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblRefeitorioFiltro | TLabel | rótulo | lblRefeitorio | — | — | — | — |
| EdRefeitorio | TEdit | campo de texto/data | — | 0 | — | — | Text=EdRefeitorio |
| TbsCardapio | TTabSheet | contêiner | Cardápio (Ctrl+G) | — | — | — | — |
| Label13 | TLabel | rótulo | Cardápio | — | — | — | — |
| mlCardapio | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblCardapioFiltro | TLabel | rótulo | lblRefeitorio | — | — | — | — |
| EdCardapio | TEdit | campo de texto/data | — | 0 | — | — | Text=EdCardapio |
| BtnLimparFiltros | THoverSpeedButton | ação | Limpar Filtros (Ctrl+X) | 1 | — | — | — |
| Grid_Visitantes | TDBGrid | grade | — | 2 | — | — | Visible=True |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActLimparFiltros | TAction | ação | Limpar Filtros (Ctrl+X) | — | — | — | — |
| ActConsultar | TAction | ação | Consultar (F6) | — | — | — | — |
| ActPeriodo | TAction | ação | ActPeriodo | — | — | — | — |
| ActContarRegistros | TAction | ação | Contar Registros (F5) | — | — | — | — |
| ActBuscarFiltros | TAction | ação | F4 | — | — | — | — |
| ActVisitantes | TAction | ação | ActVisitantes | — | — | — | — |
| ActCracha | TAction | ação | ActCracha | — | — | — | — |
| ActColetor | TAction | ação | ActColetor | — | — | — | — |
| ActUsuarios | TAction | ação | ActUsuarios | — | — | — | — |
| ActRefeitorios | TAction | ação | ActRefeitorios | — | — | — | — |
| ActCardapios | TAction | ação | ActCardapios | — | — | — | — |
| Cds_Visitantes | TClientDataSet | outro | — | — | — | — | — |
| Cds_VisitantesId | TIntegerField | outro | — | — | — | — | — |
| Cds_VisitantesIdVisitantesTercHist | TIntegerField | outro | — | — | — | — | — |
| Cds_VisitantesIdVisitantes | TIntegerField | outro | — | — | — | — | — |
| Cds_VisitantesNrCracha | TStringField | outro | — | — | — | — | — |
| Cds_VisitantesObservacao | TStringField | outro | — | — | — | — | — |
| Cds_VisitantesCardapio | TIntegerField | outro | — | — | — | — | — |
| Cds_VisitantesColetor | TIntegerField | outro | — | — | — | — | — |
| Cds_VisitantesUsuario | TStringField | outro | — | — | — | — | — |
| Cds_VisitantesDataHoraInicio | TDateTimeField | outro | — | — | — | — | — |
| Cds_VisitantesDataHoraTermino | TDateTimeField | outro | — | — | — | — | — |
| Cds_VisitantesIdResponsavel | TIntegerField | outro | — | — | — | — | — |
| Cds_VisitantesRefeitorio | TIntegerField | outro | — | — | — | — | — |
| Cds_VisitantesDataCriacao | TDateTimeField | outro | — | — | — | — | — |
| Cds_VisitantesPassagens | TIntegerField | outro | — | — | — | — | — |
| Dts_Visitantes | TDataSource | outro | — | — | — | — | — |
| frxRelVisitantes | TfrxReport | outro | — | — | — | — | — |
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
| Memo27 | TfrxMemoView | outro | — | — | — | — | — |
| Memo30 | TfrxMemoView | outro | — | — | — | — | — |
| Memo19 | TfrxMemoView | outro | — | — | — | — | — |
| Line7 | TfrxLineView | outro | — | — | — | — | — |
| Memo22 | TfrxMemoView | outro | — | — | — | — | — |
| Line13 | TfrxLineView | outro | — | — | — | — | — |
| Line8 | TfrxLineView | outro | — | — | — | — | — |
| Memo18 | TfrxMemoView | outro | — | — | — | — | — |
| Line10 | TfrxLineView | outro | — | — | — | — | — |
| Memo29 | TfrxMemoView | outro | — | — | — | — | — |
| Line15 | TfrxLineView | outro | — | — | — | — | — |
| Memo32 | TfrxMemoView | outro | — | — | — | — | — |
| Line18 | TfrxLineView | outro | — | — | — | — | — |
| Memo34 | TfrxMemoView | outro | — | — | — | — | — |
| Line20 | TfrxLineView | outro | — | — | — | — | — |
| Memo36 | TfrxMemoView | outro | — | — | — | — | — |
| MasterData2 | TfrxMasterData | outro | — | — | — | — | — |
| Line12 | TfrxLineView | outro | — | — | — | — | — |
| Line23 | TfrxLineView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_operacao | TfrxMemoView | outro | — | — | — | — | — |
| frxDBDataset1data_hora_final | TfrxMemoView | outro | — | — | — | — | — |
| Memo17 | TfrxMemoView | outro | — | — | — | — | — |
| Line5 | TfrxLineView | outro | — | — | — | — | — |
| Line6 | TfrxLineView | outro | — | — | — | — | — |
| Memo20 | TfrxMemoView | outro | — | — | — | — | — |
| Memo26 | TfrxMemoView | outro | — | — | — | — | — |
| Line9 | TfrxLineView | outro | — | — | — | — | — |
| Line11 | TfrxLineView | outro | — | — | — | — | — |
| Memo28 | TfrxMemoView | outro | — | — | — | — | — |
| Memo31 | TfrxMemoView | outro | — | — | — | — | — |
| Line16 | TfrxLineView | outro | — | — | — | — | — |
| Line19 | TfrxLineView | outro | — | — | — | — | — |
| Memo33 | TfrxMemoView | outro | — | — | — | — | — |
| Line21 | TfrxLineView | outro | — | — | — | — | — |
| Memo35 | TfrxMemoView | outro | — | — | — | — | — |
| Memo37 | TfrxMemoView | outro | — | — | — | — | — |
| PageFooter1 | TfrxPageFooter | outro | — | — | — | — | — |
| Memo13 | TfrxMemoView | outro | — | — | — | — | — |
| frxDBVisitantes | TfrxDBDataset | outro | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActConsultarExecute` | 289 | — |
| `FormCreate` | 516 | `TVisitantesTerceirosHistoricosRegController.Create`, `FVisitantesTerceirosController.SetConexao` |
| `ValidarFiltros` | 621 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 297: `Possui `
- Linha 357: `Data Inválida!`
- Linha 380: `Cardápio não cadastrado`
- Linha 409: `Coletor não cadastrado`
- Linha 438: `Refeitório não cadastrado`
- Linha 467: `Usuário não cadastrado`
- Linha 496: `Visitante não cadastrado`
- Linha 616: `Hora Inválida!`
- Linha 625: `Data de Início deve ser informada.`
- Linha 632: `A hora de Início deve ser informada.`
- Linha 639: `Data de Término deve ser informada.`
- Linha 646: `A hora de Término deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
