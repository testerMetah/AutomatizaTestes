# TFrmViewsTarefas

Mapa estático, sem validação em execução.

| Caminho Delphi | Classe | Legenda | Campo | Ação/evento |
|---|---|---|---|---|
| /FrmViewsTarefas | TFrmViewsTarefas | Montagem da Tarefa |  |  |
| /FrmViewsTarefas/PnlFundo | TPanel |  |  |  |
| /FrmViewsTarefas/PnlFundo/LblNomeTarefa | TLabel | Nome da Tarefa: |  |  |
| /FrmViewsTarefas/PnlFundo/lblComando | TLabel | Comando: |  |  |
| /FrmViewsTarefas/PnlFundo/lblFrequencia | TLabel | Frequência: |  |  |
| /FrmViewsTarefas/PnlFundo/lblStatus | TLabel | Situação: |  |  |
| /FrmViewsTarefas/PnlFundo/cmbComando | TComboBox |  |  |  |
| /FrmViewsTarefas/PnlFundo/edtTarefa | TEdit |  |  |  |
| /FrmViewsTarefas/PnlFundo/cmbFrequencia | TComboBox |  |  |  |
| /FrmViewsTarefas/PnlFundo/cmbStatus | TComboBox |  |  |  |
| /FrmViewsTarefas/PnlBottomTarefas | TPanel |  |  |  |
| /FrmViewsTarefas/PnlBottomTarefas/btnCancelarSelecao | THoverSpeedButton | Cancelar (Alt+F4) |  | ActCancelar |
| /FrmViewsTarefas/PnlBottomTarefas/btnSalvar | THoverSpeedButton | Salvar (Ctrl+S) |  | ActSalvar |
| /FrmViewsTarefas/Panel1 | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando | TPageControl |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsEquipamentos | TTabSheet | Equipamentos |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsEquipamentos/ChkEquipamentos | TCheckListBox |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsEquipamentos/pnlEquipamentos | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsEquipamentos/pnlEquipamentos/lblEquipamentos | TLabel | Selecionar Equipamentos |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros | TTabSheet | Filtros |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosTopo | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosTopo/lblInfoFiltros | TLabel | Selecione os filtros que serão aplicados nesta tarefa |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/dgFiltros | TDrawGrid |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/lblFiltroSelecionado | TLabel | Filtro Selecionado: |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/lblNomeFiltro | TLabel | Nenhum filtro selecionado |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/mmoDescricaoFiltro | TMemo |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/pnlInfoFiltro | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/pnlInfoFiltro/lblTipoFiltro | TLabel | Tipo:  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/pnlInfoFiltro/lblQtdeItens | TLabel | Quantidade de itens:  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/pnlInfoFiltro/lblStatusFiltro | TLabel | Status:  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/pnlInfoFiltro/lblDataCriacao | TLabel | Criado em:  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/pnlInfoFiltro/lblDataAlteracao | TLabel | Alterado em:  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsFiltros/pnlFiltrosGrid/pnlDetalhesFiltro/btnVerDetalhesFiltro | THoverSpeedButton | Ver Detalhes Completos |  | btnVerDetalhesFiltroClick |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD | TTabSheet | Configuração AFD |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/pnlTipoAFD | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/pnlTipoAFD/lblTipoAFD | TLabel | Tipo de AFD: |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/pnlTipoAFD/lblFormatoCustomizado | TLabel | Formato: |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/pnlTipoAFD/cmbTipoAFD | TComboBox |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/pnlTipoAFD/cmbFormatoCustomizado | TComboBox |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/chkMesmoCaminho | TCheckBox | Usar mesmo caminho para todos equipamentos |  | chkMesmoCaminhoClick |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/edtCaminhoUnico | TEdit |  |  |  |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/btnSelecionarCaminho | TButton | ... |  | btnSelecionarCaminhoClick |
| /FrmViewsTarefas/Panel1/pcComando/tsExportacaoAFD/grdEquipamentosCaminho | TStringGrid |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2 | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia | TPageControl |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario | TTabSheet | tsDiario |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/lblDiasSemana | TLabel | Selecione os dias da semana |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/imgDiasSemana | TImage |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/CheckBox1 | TCheckBox | Segunda-Feira |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/CheckBox2 | TCheckBox | Terça-Feira |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/CheckBox3 | TCheckBox | Quarta-Feira |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/CheckBox4 | TCheckBox | Quinta-Feira |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/CheckBox5 | TCheckBox | Sexta-Feira |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/CheckBox6 | TCheckBox | Sábado |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsDiario/pnlDiasSemana/CheckBox7 | TCheckBox | Domingo |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal | TTabSheet | tsSemanal |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl01 | TPanel | 01 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl02 | TPanel | 02 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl03 | TPanel | 03 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl04 | TPanel | 04 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl05 | TPanel | 05 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl06 | TPanel | 06 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl07 | TPanel | 07 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl08 | TPanel | 08 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl09 | TPanel | 09 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl10 | TPanel | 10 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl11 | TPanel | 11 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl12 | TPanel | 12 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl13 | TPanel | 13 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl14 | TPanel | 14 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl15 | TPanel | 15 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl16 | TPanel | 16 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl17 | TPanel | 17 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl18 | TPanel | 18 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl19 | TPanel | 19 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl20 | TPanel | 20 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl21 | TPanel | 21 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl22 | TPanel | 22 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl23 | TPanel | 23 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl24 | TPanel | 24 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl25 | TPanel | 25 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl26 | TPanel | 26 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl27 | TPanel | 27 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl28 | TPanel | 28 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl29 | TPanel | 29 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl30 | TPanel | 30 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pcFrequencia/tsSemanal/pnlSemanal/pnl31 | TPanel | 31 |  | pnlDiaClick |
| /FrmViewsTarefas/Panel1/Panel2/pnlHorarios | TPanel |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pnlHorarios/Label2 | TLabel | Hora |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pnlHorarios/lbxHorarios | TListBox |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pnlHorarios/edtHora | TMaskEdit |  |  |  |
| /FrmViewsTarefas/Panel1/Panel2/pnlHorarios/BtnAdicionarHora | THoverSpeedButton |  |  | btnAdicionarHoraClick |
| /FrmViewsTarefas/Panel1/Panel2/pnlHorarios/btnRemoverHorario | THoverSpeedButton |  |  | btnRemoverHorarioClick |
| /FrmViewsTarefas/ActionList1 | TActionList |  |  |  |
| /FrmViewsTarefas/ActionList1/ActProximo | TAction | Próximo (Ctrl+N) |  |  |
| /FrmViewsTarefas/ActionList1/ActCancelar | TAction | Cancelar (Alt+F4) |  |  |
| /FrmViewsTarefas/ActionList1/ActSalvar | TAction | Salvar (Ctrl+S) |  |  |
| /FrmViewsTarefas/ActionList1/ActVoltar | TAction | Voltar (Ctrl+B) |  |  |
| /FrmViewsTarefas/ActionList1/ActNovoLayout | TAction | Novo Layout (Ctrl+I) |  |  |
| /FrmViewsTarefas/ActionList1/ActEditarLayout | TAction | Editar Layout (Ctrl+E) |  |  |
| /FrmViewsTarefas/ActionList1/ActAdicionarDiretorio | TAction |  |  |  |
| /FrmViewsTarefas/DefaultIcons | TImageList |  |  |  |
