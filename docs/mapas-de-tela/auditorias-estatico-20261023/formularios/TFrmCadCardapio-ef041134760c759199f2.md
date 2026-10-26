# TFrmCadCardapio

Mapa estático, sem validação em execução.

| Caminho Delphi | Classe | Legenda | Campo | Ação/evento |
|---|---|---|---|---|
| /FrmCadCardapio | TFrmCadCardapio | Cadastro de Cardápios |  |  |
| /FrmCadCardapio/Pagina | TPageControl |  |  |  |
| /FrmCadCardapio/Pagina/Grid | TTabSheet |  |  |  |
| /FrmCadCardapio/Pagina/Grid/GridCadastro | TDBGrid |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlCimaPadrao | TPanel |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlCimaPadrao/PaginaLoc | TPageControl |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlCimaPadrao/PaginaLoc/TabSheet2 | TTabSheet |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlCimaPadrao/PaginaLoc/TabSheet2/ednomeloc | TEdit |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlCimaPadrao/PaginaLoc/TabSheet2/btnExibirTudo | THoverSpeedButton |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlFundoPadrao | TPanel |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlFundoPadrao/btnexcluir | THoverSpeedButton |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlFundoPadrao/btnInserir | THoverSpeedButton |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlFundoPadrao/btnAlterar | THoverSpeedButton |  |  |  |
| /FrmCadCardapio/Pagina/Grid/pnlFundoPadrao/btnImportar | THoverSpeedButton | Importar Cardápios (Ctrl + F5) |  | ActImportar |
| /FrmCadCardapio/Pagina/Cadastro | TTabSheet |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/Label1 | TLabel | Nome: |  |  |
| /FrmCadCardapio/Pagina/Cadastro/Label2 | TLabel | Situação: |  |  |
| /FrmCadCardapio/Pagina/Cadastro/Label32 | TLabel | Refeitórios: |  |  |
| /FrmCadCardapio/Pagina/Cadastro/mlRefeitorio | TMetaEquipLocalizar | F4 |  |  |
| /FrmCadCardapio/Pagina/Cadastro/lblRefeitorio | TLabel | lblRefeitorio |  |  |
| /FrmCadCardapio/Pagina/Cadastro/pnlFundoCadastro | TPanel |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/pnlFundoCadastro/btnOk | THoverSpeedButton |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/pnlFundoCadastro/btnCancelar | THoverSpeedButton |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/EdNome | TEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/cmbStatus | TComboBox |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios | TGroupBox | Valores do Cardápio |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/Label4 | TLabel | Reserva sem Consumo: R$ |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/Label5 | TLabel | Consumo sem Reserva: R$ |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/Label6 | TLabel | Reserva com consumo:  R$ |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/lblTempoDesc | TLabel | Minutos a Desconsiderar: |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/EdReservaSemConsumo | TEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/EdConsumoSemReserva | TEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/EdReservaComConsumo | TEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/pnlDesconsiderarDup | TPanel |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/pnlDesconsiderarDup/lblDesconsiderarDup | TLabel | Desconsiderar Reservas Duplicadas |  | lblDesconsiderarDupClick |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/pnlDesconsiderarDup/chkDesconsiderarDup | TCheckBox |  |  | chkDesconsiderarDupClick |
| /FrmCadCardapio/Pagina/Cadastro/GrbValoresCardapios/EdTempoDesc | TEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/EdRefeitorio | TEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbHorarioConsumo | TGroupBox | Horário Para Consumir |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbHorarioConsumo/Label7 | TLabel | Até |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbHorarioConsumo/MskHoraIniC | TMaskEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbHorarioConsumo/MskHoraFimC | TMaskEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbHorarioReserva | TGroupBox | Horário Para Reservar |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbHorarioReserva/Label3 | TLabel | Até |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbHorarioReserva/MskHoraFimR | TMaskEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/GrbHorarioReserva/MskHoraIniR | TMaskEdit |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/pnlGrid | TPanel |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/pnlGrid/GridItens | TDBGrid |  |  |  |
| /FrmCadCardapio/Pagina/Cadastro/btnInformacao | THoverSpeedButton |  |  | ActInformacao |
| /FrmCadCardapio/Pagina/Campos | TTabSheet |  |  |  |
| /FrmCadCardapio/Pagina/Campos/Panel4 | TPanel |  |  |  |
| /FrmCadCardapio/ActionList1 | TActionList |  |  |  |
| /FrmCadCardapio/ActionList1/ActExcluir | TAction |  |  |  |
| /FrmCadCardapio/ActionList1/ActImportar | TAction | Importar Cardápios (Ctrl + F5) |  |  |
| /FrmCadCardapio/ActionList1/ActTSNome | TAction | Nome (Ctrl+B) |  |  |
| /FrmCadCardapio/ActionList1/ActInformacao | TAction |  |  |  |
| /FrmCadCardapio/DefaultIcons | TImageList |  |  |  |
| /FrmCadCardapio/DsCardapios | TDataSource |  |  |  |
| /FrmCadCardapio/CdsCardapios | TClientDataSet |  |  |  |
| /FrmCadCardapio/CdsCardapios/CdsCardapiosId | TIntegerField |  |  |  |
| /FrmCadCardapio/CdsCardapios/CdsCardapiosNome | TStringField |  |  |  |
| /FrmCadCardapio/CdsCardapios/CdsCardapiosSituacao | TIntegerField |  |  |  |
| /FrmCadCardapio/dsConsulta | TDataSource |  |  |  |
| /FrmCadCardapio/CdsConsulta | TClientDataSet |  |  |  |
| /FrmCadCardapio/CdsConsulta/CdsConsultaSELECIONADO | TIntegerField |  |  |  |
| /FrmCadCardapio/CdsConsulta/CdsConsultaID | TStringField |  |  |  |
| /FrmCadCardapio/CdsConsulta/CdsConsultaNOME | TStringField |  |  |  |
