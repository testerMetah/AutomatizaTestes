# TFrmMetahConnectViewsComunicacao

Mapa estático, sem validação em execução.

| Caminho Delphi | Classe | Legenda | Campo | Ação/evento |
|---|---|---|---|---|
| /FrmMetahConnectViewsComunicacao | TFrmMetahConnectViewsComunicacao | Comunicação com Equipamentos |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal | TPageControl |  |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos | TTabSheet | Comandos |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/pnlEquipamentoSelecionado | TPanel | Nenhum equipamento selecionado |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/rgComandos | TRadioGroup | Comandos Disponíveis: |  | rgComandosClick |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas | TGroupBox | Filtrar |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/lblPessoa | TLabel | Pessoa: |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/cbTipoFiltro | TComboBox |  |  | cbTipoFiltroClick |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/edtPessoa | TEdit |  |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/lbPessoasSelecionadas | TListBox |  |  | lbPessoasSelecionadasClick |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/btnRemoverPessoa | THoverSpeedButton | Remover (Shift+Del) |  | actRemoverPessoa |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/btnLimparLista | THoverSpeedButton | Limpar Lista |  | actLimparLista |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/Panel1 | TPanel | Acesso |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/Panel1/Shape3 | TShape |  |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/Panel1/mlPessoas | TMetaEquipLocalizar |  |  | mlPessoasClick |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/pnlAFD | TPanel |  |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/pnlAFD/clAFDFim | TCalendarPicker |  |  |  |
| /FrmMetahConnectViewsComunicacao/pgcPrincipal/tabComandos/gbFiltroPessoas/pnlAFD/clAFDIni | TCalendarPicker |  |  |  |
| /FrmMetahConnectViewsComunicacao/pnlLeft | TPanel |  |  |  |
| /FrmMetahConnectViewsComunicacao/pnlLeft/pgcEquipamentos | TPageControl |  |  |  |
| /FrmMetahConnectViewsComunicacao/pnlLeft/pgcEquipamentos/tabEquipamentos | TTabSheet | Equipamentos |  |  |
| /FrmMetahConnectViewsComunicacao/pnlLeft/pgcEquipamentos/tabEquipamentos/DrawGridEquipamentos | TDrawGrid |  |  |  |
| /FrmMetahConnectViewsComunicacao/pnlRodapeEquipamentos | TPanel |  |  |  |
| /FrmMetahConnectViewsComunicacao/pnlRodapeEquipamentos/btnFechar | THoverSpeedButton | Fechar (Alt+F4) |  | actFechar |
| /FrmMetahConnectViewsComunicacao/pnlRodapeEquipamentos/btnEnviarComando | THoverSpeedButton | Enviar (Ctrl+S) |  | actEnviarComando |
| /FrmMetahConnectViewsComunicacao/ActionList1 | TActionList |  |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actAtualizarEquipamentos | TAction | Atualizar (F5) |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actSelecionarEquipamento | TAction |  |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actNovoComando | TAction | Novo Comando (Ctrl+N) |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actEnviarComando | TAction | Enviar (Ctrl+S) |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actCancelar | TAction | Voltar (Ctrl+D) |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actAdicionarPessoa | TAction | Adicionar |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actRemoverPessoa | TAction | Remover (Shift+Del) |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actLimparLista | TAction | Limpar Lista |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actAdicionarDoFiltro | TAction | Adicionar Selecionados |  |  |
| /FrmMetahConnectViewsComunicacao/ActionList1/actFechar | TAction | Fechar (Alt+F4) |  |  |
| /FrmMetahConnectViewsComunicacao/dsEquipamentos | TDataSource |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsEquipamentos | TClientDataSet |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsEquipamentos/cdsEquipamentosId | TIntegerField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsEquipamentos/cdsEquipamentosNome | TStringField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsEquipamentos/cdsEquipamentosIP | TStringField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsEquipamentos/cdsEquipamentosModelo | TStringField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsEquipamentos/cdsEquipamentosStatus | TStringField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsEquipamentos/cdsEquipamentosSelecionado | TBooleanField |  |  |  |
| /FrmMetahConnectViewsComunicacao/dsFilaComandos | TDataSource |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsFilaComandos | TClientDataSet |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsFilaComandos/cdsFilaComandosId | TIntegerField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsFilaComandos/cdsFilaComandosDataHora | TDateTimeField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsFilaComandos/cdsFilaComandosIdEquipamento | TIntegerField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsFilaComandos/cdsFilaComandosEquipamento | TStringField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsFilaComandos/cdsFilaComandosComando | TIntegerField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsFilaComandos/cdsFilaComandosComandoStr | TStringField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsFilaComandos/cdsFilaComandosStatus | TStringField |  |  |  |
| /FrmMetahConnectViewsComunicacao/TimerAtualizacao | TTimer |  |  |  |
| /FrmMetahConnectViewsComunicacao/ImageList1 | TImageList |  |  |  |
| /FrmMetahConnectViewsComunicacao/dsPessoasFiltro | TDataSource |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsPessoasFiltro | TClientDataSet |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsPessoasFiltro/cdsPessoasFiltroId | TIntegerField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsPessoasFiltro/cdsPessoasFiltroNome | TStringField |  |  |  |
| /FrmMetahConnectViewsComunicacao/cdsPessoasFiltro/cdsPessoasFiltroSelecionado | TBooleanField |  |  |  |
