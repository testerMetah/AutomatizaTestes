# Refeitório > Cadastro > Coletores

> Inventário estático de `Acesso/uFrmCadColetores.dfm` e `Acesso/uFrmCadColetores.pas` no commit `28074dd`. Esta ficha combina inventário estático com notas de leitura manual das procedures; ainda requer conferência de controllers, DAOs e do build instalado.

- Form: `TFrmCadColetores`
- Abertura: `acCadColetoresExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FrmCadColetores` | `TFrmCadColetores` (herdado) | Cadastro de Coletores | — | `—` | — | — | — |
| `Pagina` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `Grid` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `GridCadastro` | `TDBGrid` (herdado) | — | — | `—` | — | Visible=True | — |
| `pnlCimaPadrao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `PaginaLoc` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `TabSheet2` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `ednomeloc` | `TEdit` (herdado) | — | — | `—` | — | — | OnChange=ednomelocChange |
| `btnExibirTudo` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `pnlFundoPadrao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `btnexcluir` | `THoverSpeedButton` (herdado) | — | — | `—` | — | Visible=False, Enabled=False | — |
| `btnInserir` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `btnAlterar` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `Cadastro` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `pnlFundoCadastro` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `btnOk` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `btnCancelar` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `PgCadastro` | `TPageControl` | — | 1 | `—` | — | — | OnChange=PgCadastroChange |
| `TabGeral` | `TTabSheet` | Geral | — | `—` | — | — | — |
| `Label12` | `TLabel` | Minutos | — | `—` | — | Visible=False | — |
| `lblNomeModelo` | `TLabel` | lblNomeModelo | — | `—` | — | — | — |
| `mlModelo` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `Label1` | `TLabel` | Nome: | — | `—` | — | — | — |
| `Label11` | `TLabel` | Fuso horário: | — | `—` | — | Visible=False | — |
| `Label3` | `TLabel` | Situação: | — | `—` | — | — | — |
| `Label55` | `TLabel` | Modelo: | — | `—` | — | — | — |
| `Label58` | `TLabel` | IP: | — | `—` | — | — | — |
| `Label2` | `TLabel` | Comunicação: | — | `—` | — | — | — |
| `Label4` | `TLabel` | Filtro de Pessoas: | — | `—` | — | — | — |
| `MetaEquipLocalizar2` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `lblFiltroPessoas` | `TLabel` | lblFiltroPessoas | — | `—` | — | — | — |
| `Label32` | `TLabel` | Proximidade: | — | `—` | — | — | — |
| `EdNome` | `TEdit` | — | 0 | `—` | — | Text=EDNOME | — |
| `EdModelo` | `TEdit` | — | 1 | `—` | — | Text=EdModelo, Visible=False, Enabled=False | OnExit=EdModeloExit, OnChange=EdModeloChange |
| `cmbStatus` | `TComboBox` | — | 2 | `—` | — | Text=Ativo, ItemIndex=0 | OnChange=cmbStatusChange |
| `cmbComunicacao` | `TComboBox` | — | 3 | `—` | — | Text=RealTime, ItemIndex=1 | — |
| `CmbFusoHorario` | `TComboBox` | — | 5 | `—` | — | Visible=False | — |
| `EdFusoHorario` | `TEdit` | — | 4 | `—` | — | Text=EdFusoHorario, Visible=False | — |
| `GroupBox1` | `TGroupBox` | Transformar Função  | 6 | `—` | — | — | — |
| `Label73` | `TLabel` | Função de Entrada: | — | `—` | — | — | — |
| `Label6` | `TLabel` | Função de Saída: | — | `—` | — | — | — |
| `EdFuncaoEntrada` | `TEdit` | — | 0 | `—` | — | — | — |
| `EdFuncaoSaida` | `TEdit` | — | 1 | `—` | — | — | — |
| `gbxRefeitorioCardapio` | `TGroupBox` |  Refeitório | 7 | `—` | — | — | — |
| `mlRefeitorio` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `lblRefeitorio` | `TLabel` | lblRefeitorio | — | `—` | — | — | — |
| `Label31` | `TLabel` | Refeitório: | — | `—` | — | — | — |
| `EdRefeitorio` | `TEdit` | — | 0 | `—` | — | — | OnExit=EdRefeitorioExit |
| `pnlIp` | `TPanel` | — | 8 | `—` | — | — | — |
| `LblP1` | `TLabel` | . | — | `—` | — | — | — |
| `LblP2` | `TLabel` | . | — | `—` | — | — | — |
| `LblP3` | `TLabel` | . | — | `—` | — | — | — |
| `EdIp1` | `TEdit` | — | 0 | `—` | 3 | Text=192 | OnChange=EdIp1Change |
| `EdIp2` | `TEdit` | — | 1 | `—` | 3 | Text=168 | OnChange=EdIp2Change |
| `EdIp3` | `TEdit` | — | 2 | `—` | 3 | Text=000 | OnChange=EdIp3Change |
| `EdIp4` | `TEdit` | — | 3 | `—` | 3 | Text=000 | OnChange=EdIp4Change |
| `EdFiltroPessoas` | `TEdit` | — | 9 | `—` | — | Text=EdFiltroPessoas, Enabled=False | OnExit=EdFiltroPessoasExit |
| `cmbProximidade` | `TComboBox` | — | 10 | `—` | — | Text=Acura, ItemIndex=0 | — |
| `TabConfig` | `TTabSheet` | Configurações | — | `—` | — | — | — |
| `pcConfigEspecif` | `TPageControl` | — | 0 | `—` | — | — | OnChange=PgCadastroChange |
| `TabDimepMicroPoint` | `TTabSheet` | TabDimepMicroPoint | — | `—` | — | — | — |
| `Label13` | `TLabel` | Sentido Entrada | — | `—` | — | — | — |
| `Label14` | `TLabel` | Acionamento | — | `—` | — | — | — |
| `Label15` | `TLabel` | Nº Funis | — | `—` | — | — | — |
| `Label16` | `TLabel` | Time Out | — | `—` | — | — | — |
| `Label17` | `TLabel` | Terminal | — | `—` | — | — | — |
| `Label20` | `TLabel` | 1 a 65 (recomendado 20) | — | `—` | — | — | — |
| `Label29` | `TLabel` | Modo de Trabalho | — | `—` | — | — | — |
| `cbxSentidoEntradaDimepMicropoint` | `TComboBox` | — | 2 | `—` | — | — | — |
| `cbxAcionamentoDimepMicropoint` | `TComboBox` | — | 3 | `—` | — | — | — |
| `cbxNrFunisDimepMicropoint` | `TComboBox` | — | 4 | `—` | — | — | — |
| `edtTimeOutDimepMicropoint` | `TSpinEdit` | — | 1 | `—` | — | — | — |
| `edtTerminalDimepMicropoint` | `TSpinEdit` | — | 0 | `—` | 3 | — | — |
| `cbxUsarUrnaDimepMicropoint` | `TCheckBox` | Utilizar urna para visitantes | 6 | `—` | — | — | — |
| `cbxModoTrabalhoDimepMicropoint` | `TComboBox` | — | 5 | `—` | — | — | — |
| `TabDimepBioPoint` | `TTabSheet` | TabDimepBioPoint | — | `—` | — | — | — |
| `Label21` | `TLabel` | 1 a 65 | — | `—` | — | — | — |
| `Label28` | `TLabel` | 0 a 99 | — | `—` | — | — | — |
| `Label5` | `TLabel` | Terminal: | — | `—` | — | — | — |
| `Label10` | `TLabel` | Sentido do Giro: | — | `—` | — | — | — |
| `Label18` | `TLabel` | Timeout (s): | — | `—` | — | — | — |
| `Label19` | `TLabel` | Tempo Acionamento (s): | — | `—` | — | — | — |
| `Label59` | `TLabel` | Acionamento: | — | `—` | — | — | — |
| `Label22` | `TLabel` | Liberação Entrada: | — | `—` | — | — | — |
| `Label23` | `TLabel` | Liberação Saída: | — | `—` | — | — | — |
| `Label24` | `TLabel` | Validação de Digital: | — | `—` | — | — | — |
| `edtTimeOutDimepBiopoint` | `TSpinEdit` | — | 1 | `—` | — | — | — |
| `edtTerminalDimepBiopoint` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `cbxAcionamentoDimepBiopoint` | `TComboBox` | — | 2 | `—` | — | Text=Catraca bidirecional com sentido de giro independente do leitor, ItemIndex=7 | — |
| `cbxLiberaEntradaDimepBiopoint` | `TComboBox` | — | 5 | `—` | — | — | — |
| `cbxLiberaSaidaDimepBiopoint` | `TComboBox` | — | 6 | `—` | — | — | — |
| `cbxSentidoGiroDimepBiopoint` | `TComboBox` | — | 4 | `—` | — | Text=Horário, ItemIndex=1 | — |
| `cbxValidaDigitalDimepBiopoint` | `TComboBox` | — | 7 | `—` | — | — | — |
| `edtTempoAcionamentoDimepBiopoint` | `TSpinEdit` | — | 3 | `—` | — | — | — |
| `cbxUsarUrnaDimepBiopoint` | `TCheckBox` | Utilizar urna para visitantes | 8 | `—` | — | — | — |
| `TabControl_ID` | `TTabSheet` | TabControl_ID | — | `—` | — | — | — |
| `gbxLeitoresControlID` | `TGroupBox` | Leitores  | 2 | `—` | — | — | — |
| `cbxWiegandControlID` | `TCheckBox` | Converte Código Wiegand (RFID) | 0 | `—` | — | — | — |
| `cbxPossuiBiometriaControlID` | `TCheckBox` | Possui Biometria | 1 | `—` | — | — | — |
| `cbxPossuiFaceControlID` | `TCheckBox` | Possui Face | 2 | `—` | — | — | — |
| `gbxConfigEquipamentoControlID` | `TGroupBox` | Configuração do Equipamento  | 1 | `—` | — | — | — |
| `Label36` | `TLabel` | Sentido do Fluxo: | — | `—` | — | — | — |
| `Label37` | `TLabel` | Timeout (ms): | — | `—` | — | — | — |
| `edtTimeOutControlID` | `TSpinEdit` | — | 0 | `—` | 9 | — | — |
| `cbxSentidoFluxoControlID` | `TComboBox` | — | 1 | `—` | — | — | — |
| `gbxConfiguracaoControlID` | `TGroupBox` | Configuração  | 0 | `—` | — | — | — |
| `Label9` | `TLabel` | IP do Servidor: | — | `—` | — | — | — |
| `Label33` | `TLabel` | Porta: | — | `—` | — | — | — |
| `Label34` | `TLabel` | Porta de Escuta: | — | `—` | — | — | — |
| `edtIpServidorControlID` | `TEdit` | — | 1 | `—` | — | Text=192.168.000.000 | OnExit=edtIpServidorControlIDExit |
| `cbxIpAutomaticoControlID` | `TCheckBox` | IP Automático | 2 | `—` | — | — | OnClick=cbxIpAutomaticoControlIDClick |
| `edtPortaControlID` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `edtPortaEscutaControlID` | `TSpinEdit` | — | 3 | `—` | 4 | — | — |
| `gbxAutenticacaoControlID` | `TGroupBox` | Autenticação  | 3 | `—` | — | — | — |
| `Label7` | `TLabel` | Usuário: | — | `—` | — | — | — |
| `Label8` | `TLabel` | Senha: | — | `—` | — | — | — |
| `edtUsuarioControlID` | `TEdit` | — | 0 | `—` | 30 | Text=admin | — |
| `edtSenhaControlID` | `TEdit` | — | 1 | `—` | 30 | Text=admin | OnChange=PgCadastroChange |
| `cbxExibirSenhaControlID` | `TCheckBox` | Exibir senha | 2 | `—` | — | — | OnClick=cbxExibirSenhaControlIDClick |
| `gbSyncBioControlID` | `TGroupBox` | Tipo de sincronização de digitais | 4 | `—` | — | — | — |
| `Label26` | `TLabel` | Tipo de Sincronização: | — | `—` | — | — | — |
| `SpinEdit3` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `cmbSyncBioControlID` | `TComboBox` | — | 1 | `—` | — | — | — |
| `TabControl_ID_Catraca` | `TTabSheet` | TabControl_ID_Catraca | — | `—` | — | — | — |
| `GbxConfigIDBlock` | `TGroupBox` | Configuração  | 0 | `—` | — | — | — |
| `Label35` | `TLabel` | Porta: | — | `—` | — | — | — |
| `Label38` | `TLabel` | IP do Servidor: | — | `—` | — | — | — |
| `Label39` | `TLabel` | Porta de Escuta: | — | `—` | — | — | — |
| `edtIpServidorIDBlock` | `TEdit` | — | 1 | `—` | — | Text=192.168.000.000 | OnExit=edtIpServidorIDBlockExit |
| `cbxIpAutomaticoIDBlock` | `TCheckBox` | IP Automático | 2 | `—` | — | — | OnClick=cbxIpAutomaticoControlIDNextClick |
| `edtPortaIDBlock` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `edtPortaEscutaIDBlock` | `TSpinEdit` | — | 3 | `—` | 4 | — | — |
| `GroupBox3` | `TGroupBox` | Autenticação  | 1 | `—` | — | — | — |
| `Label43` | `TLabel` | Usuário: | — | `—` | — | — | — |
| `Label44` | `TLabel` | Senha: | — | `—` | — | — | — |
| `edtUsuarioIDBlock` | `TEdit` | — | 0 | `—` | 30 | Text=admin | — |
| `edtSenhaIDBlock` | `TEdit` | — | 1 | `—` | 30 | Text=admin | — |
| `cbxExibirSenhaIDBlock` | `TCheckBox` | Exibir senha | 2 | `—` | — | — | OnClick=cbxExibirSenhaIDBlockClick |
| `gbxLeitoresIDBlock` | `TGroupBox` | Leitores  | 2 | `—` | — | — | — |
| `cbxWiegandIDBlock` | `TCheckBox` | Converte Código Wiegand (RFID) | 0 | `—` | — | — | — |
| `cbxPossuiBiometriaIDBlock` | `TCheckBox` | Possui Biometria | 1 | `—` | — | — | — |
| `cbxPossuiFaceIDBlock` | `TCheckBox` | Possui Face | 2 | `—` | — | — | — |
| `GbxConfigEquip` | `TGroupBox` | Configuração do Equipamento  | 3 | `—` | — | — | — |
| `Label40` | `TLabel` | Sentido do Fluxo: | — | `—` | — | — | — |
| `Label41` | `TLabel` | Timeout (ms): | — | `—` | — | — | — |
| `Label42` | `TLabel` | Sentido do Giro: | — | `—` | — | — | — |
| `edtTimeOutIDBlock` | `TSpinEdit` | — | 0 | `—` | 9 | — | — |
| `cbxSentidoFluxoIDBlock` | `TComboBox` | — | 1 | `—` | — | — | — |
| `CmbSentido` | `TComboBox` | — | 2 | `—` | — | — | — |
| `gbxUrnaIDBlock` | `TGroupBox` | Urna | 4 | `—` | — | — | — |
| `chkUrnaIDBlock` | `TCheckBox` | Utilizar urna para visitantes | 0 | `—` | — | — | — |
| `SpinEdit2` | `TSpinEdit` | — | 1 | `—` | 4 | — | — |
| `gbSyncBio` | `TGroupBox` | Tipo de sincronização de digitais | 5 | `—` | — | — | — |
| `Label25` | `TLabel` | Tipo de Sincronização: | — | `—` | — | — | — |
| `SpinEdit1` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `cmbSyncBioIDBlock` | `TComboBox` | — | 1 | `—` | — | — | — |
| `TabControl_ID_Next` | `TTabSheet` | TabControl_ID_Next | — | `—` | — | — | — |
| `GroupBox12` | `TGroupBox` | Configuração do Equipamento  | 0 | `—` | — | — | — |
| `Label45` | `TLabel` | Sentido do Fluxo: | — | `—` | — | — | — |
| `Label46` | `TLabel` | Timeout (ms): | — | `—` | — | — | — |
| `Label47` | `TLabel` | Sentido do Giro: | — | `—` | — | — | — |
| `edtTimeOutControlIDNext` | `TSpinEdit` | — | 0 | `—` | 9 | — | — |
| `cbxSentidoFluxoControlIDNext` | `TComboBox` | — | 1 | `—` | — | — | — |
| `cbxSentidoGiroControlIDNext` | `TComboBox` | — | 2 | `—` | — | — | — |
| `GroupBox13` | `TGroupBox` | Configuração  | 1 | `—` | — | — | — |
| `Label76` | `TLabel` | Porta: | — | `—` | — | — | — |
| `Label77` | `TLabel` | IP do Servidor: | — | `—` | — | — | — |
| `Label78` | `TLabel` | Porta de Escuta: | — | `—` | — | — | — |
| `edtPortaEscutaControlIDNext` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `edtIpServidorControlIDNext` | `TEdit` | — | 1 | `—` | — | Text=192.168.000.000 | OnExit=edtIpServidorIDBlockExit |
| `cbxIpAutomaticoControlIDNext` | `TCheckBox` | IP Automático | 2 | `—` | — | — | OnClick=cbxIpAutomaticoControlIDNextClick |
| `edtPortaControlIDNext` | `TSpinEdit` | — | 3 | `—` | 4 | — | — |
| `GroupBox14` | `TGroupBox` | Autenticação  | 2 | `—` | — | — | — |
| `Label79` | `TLabel` | Usuário: | — | `—` | — | — | — |
| `Label80` | `TLabel` | Senha: | — | `—` | — | — | — |
| `edtUsuarioControlIDNext` | `TEdit` | — | 0 | `—` | 30 | Text=admin | — |
| `edtSenhaControlIDNext` | `TEdit` | — | 1 | `—` | 30 | Text=admin | — |
| `cbxExibirSenhaControlIDNext` | `TCheckBox` | Exibir senha | 2 | `—` | — | — | OnClick=cbxExibirSenhaControlIDNextClick |
| `GroupBox15` | `TGroupBox` | Leitores  | 3 | `—` | — | — | — |
| `cbxWiegandControlIDNext` | `TCheckBox` | Converte Código Wiegand (RFID) | 0 | `—` | — | — | — |
| `cbxPossuiBiometriaControlIDNext` | `TCheckBox` | Possui Biometria | 1 | `—` | — | — | — |
| `cbxPossuiFaceControlIDNext` | `TCheckBox` | Possui Face | 2 | `—` | — | — | — |
| `GroupBox16` | `TGroupBox` | Urna | 4 | `—` | — | — | — |
| `SpinEdit6` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `chkUrnaIDBlockNext` | `TCheckBox` | Utilizar urna para visitantes | 1 | `—` | — | — | — |
| `GroupBox7` | `TGroupBox` | Tipo de sincronização de digitais | 5 | `—` | — | — | — |
| `Label27` | `TLabel` | Tipo de Sincronização: | — | `—` | — | — | — |
| `SpinEdit4` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `cmbSyncBioIDNext` | `TComboBox` | — | 1 | `—` | — | — | — |
| `TabControl_ID_Antena` | `TTabSheet` | TabControl_ID_Antena | — | `—` | — | — | — |
| `gpbLeitorUHF` | `TGroupBox` | Leitor UHF | 0 | `—` | — | — | — |
| `PageControl1` | `TPageControl` | — | 0 | `—` | — | — | — |
| `TabSheet3` | `TTabSheet` | Geral | — | `—` | — | — | — |
| `Label63` | `TLabel` | Saída Wiegand (bits): | — | `—` | — | — | — |
| `Label66` | `TLabel` | Potência de transmissão (dBm): | — | `—` | — | — | — |
| `Label67` | `TLabel` | Modo de Operação: | — | `—` | — | — | — |
| `Label68` | `TLabel` | Intervalo entre leituras da mesma tag (ms): | — | `—` | — | — | — |
| `Label69` | `TLabel` | Intervalo entre leituras da tags diferentes (ms): | — | `—` | — | — | — |
| `EdSaidaWiegand` | `TComboBox` | — | 0 | `—` | — | Text=26, ItemIndex=0 | — |
| `EdPodenciaTransmissao` | `TEdit` | — | 1 | `—` | 30 | Text=2400 | — |
| `cbxModoOperacao` | `TComboBox` | — | 2 | `—` | — | Text=Contínuo, ItemIndex=0 | — |
| `EdIntMesmaTag` | `TEdit` | — | 3 | `—` | 30 | Text=5000 | — |
| `EdIntTagsDiferentes` | `TEdit` | — | 4 | `—` | 30 | Text=100 | — |
| `TabSheet4` | `TTabSheet` | Avançado | — | `—` | — | — | — |
| `Label70` | `TLabel` | Ordem dos bytes | — | `—` | — | — | — |
| `Label71` | `TLabel` | Seleção de Canal  (MHz) | — | `—` | — | — | — |
| `cbxOrdemBytes` | `TComboBox` | — | 0 | `—` | — | Text=Padrão, ItemIndex=0 | — |
| `cbxSelCanal01` | `TCheckBox` | 902.25 | 1 | `—` | — | Checked=True | — |
| `cbxSelCanal02` | `TCheckBox` | 902.75 | 2 | `—` | — | — | — |
| `cbxSelCanal03` | `TCheckBox` | 903.25 | 3 | `—` | — | — | — |
| `cbxSelCanal04` | `TCheckBox` | 903.75 | 4 | `—` | — | — | — |
| `cbxSelCanal05` | `TCheckBox` | 904.25 | 5 | `—` | — | — | — |
| `cbxSelCanal06` | `TCheckBox` | 904.75 | 6 | `—` | — | — | — |
| `cbxSelCanal07` | `TCheckBox` | 905.25 | 7 | `—` | — | — | — |
| `cbxSelCanal08` | `TCheckBox` | 905.75 | 8 | `—` | — | — | — |
| `cbxSelCanal09` | `TCheckBox` | 906.25 | 9 | `—` | — | — | — |
| `cbxSelCanal10` | `TCheckBox` | 906.75 | 10 | `—` | — | — | — |
| `cbxSelCanal11` | `TCheckBox` | 907.25 | 11 | `—` | — | — | — |
| `cbxSelCanal12` | `TCheckBox` | 915.25 | 12 | `—` | — | — | — |
| `cbxSelCanal13` | `TCheckBox` | 915.75 | 13 | `—` | — | — | — |
| `cbxSelCanal14` | `TCheckBox` | 916.25 | 14 | `—` | — | — | — |
| `cbxSelCanal15` | `TCheckBox` | 916.75 | 15 | `—` | — | — | — |
| `cbxSelCanal16` | `TCheckBox` | 917.25 | 16 | `—` | — | — | — |
| `cbxSelCanal17` | `TCheckBox` | 917.75 | 17 | `—` | — | — | — |
| `cbxSelCanal18` | `TCheckBox` | 918.25 | 18 | `—` | — | — | — |
| `cbxSelCanal19` | `TCheckBox` | 918.75 | 19 | `—` | — | — | — |
| `cbxSelCanal20` | `TCheckBox` | 919.25 | 20 | `—` | — | — | — |
| `cbxSelCanal21` | `TCheckBox` | 919.75 | 21 | `—` | — | — | — |
| `cbxSelCanal22` | `TCheckBox` | 920.25 | 22 | `—` | — | — | — |
| `cbxSelCanal23` | `TCheckBox` | 920.75 | 23 | `—` | — | — | — |
| `cbxSelCanal24` | `TCheckBox` | 921.25 | 24 | `—` | — | — | — |
| `cbxSelCanal25` | `TCheckBox` | 921.75 | 25 | `—` | — | — | — |
| `cbxSelCanal26` | `TCheckBox` | 922.25 | 26 | `—` | — | — | — |
| `cbxSelCanal27` | `TCheckBox` | 922.75 | 27 | `—` | — | — | — |
| `cbxSelCanal28` | `TCheckBox` | 923.25 | 28 | `—` | — | — | — |
| `cbxSelCanal29` | `TCheckBox` | 923.75 | 29 | `—` | — | — | — |
| `cbxSelCanal30` | `TCheckBox` | 924.25 | 30 | `—` | — | — | — |
| `cbxSelCanal31` | `TCheckBox` | 924.75 | 31 | `—` | — | — | — |
| `cbxSelCanal32` | `TCheckBox` | 625.25 | 32 | `—` | — | — | — |
| `cbxSelCanal33` | `TCheckBox` | 925.75 | 33 | `—` | — | — | — |
| `cbxSelCanal34` | `TCheckBox` | 926.25 | 34 | `—` | — | — | — |
| `cbxSelCanal35` | `TCheckBox` | 926.75 | 35 | `—` | — | — | — |
| `cbxSelCanal36` | `TCheckBox` | 927.25 | 36 | `—` | — | — | — |
| `cbxSelCanal37` | `TCheckBox` | 927.75 | 37 | `—` | — | — | — |
| `TabSheet5` | `TTabSheet` | Sensores e Atuadores | — | `—` | — | — | — |
| `Label72` | `TLabel` | Modo de Operação | — | `—` | — | — | — |
| `rbModoOpeAcionamento` | `TRadioButton` | Acionamento do Motor (padrão) | 0 | `—` | — | Checked=True | — |
| `rbModoOpeDeteccao` | `TRadioButton` | Detecção de tag | 1 | `—` | — | — | — |
| `GroupBox2` | `TGroupBox` | Configuração  | 1 | `—` | — | — | — |
| `Label48` | `TLabel` | Porta: | — | `—` | — | — | — |
| `Label51` | `TLabel` | IP do Servidor: | — | `—` | — | — | — |
| `Label52` | `TLabel` | Porta de Escuta: | — | `—` | — | — | — |
| `edtPortaControlIDAntena` | `TSpinEdit` | — | 0 | `—` | 4 | — | — |
| `edtIpServidorControlIDAntena` | `TEdit` | — | 1 | `—` | — | Text=192.168.000.000 | OnExit=edtIpServidorIDBlockExit |
| `edtPortaEscutaControlIDAntena` | `TSpinEdit` | — | 2 | `—` | 4 | — | — |
| `cbxIpAutomaticoControlIDAntena` | `TCheckBox` | IP Automático | 3 | `—` | — | — | OnClick=cbxIpAutomaticoControlIDAntenaClick |
| `GroupBox4` | `TGroupBox` | Configuração do Equipamento  | 2 | `—` | — | — | — |
| `Label53` | `TLabel` | Sentido do Fluxo: | — | `—` | — | — | — |
| `Label54` | `TLabel` | Timeout (ms): | — | `—` | — | — | — |
| `cbxSentidoFluxoControlIDAntena` | `TComboBox` | — | 0 | `—` | — | — | — |
| `edtTimeOutControlIDAntena` | `TSpinEdit` | — | 1 | `—` | 9 | — | — |
| `GroupBox5` | `TGroupBox` | Leitores  | 3 | `—` | — | — | — |
| `cbxWiegandControlIDAntena` | `TCheckBox` | Converte Código Wiegand (RFID) | 0 | `—` | — | — | — |
| `cbxPossuiAntena` | `TCheckBox` | Possui Antena | 1 | `—` | — | — | — |
| `GroupBox6` | `TGroupBox` | Autenticação  | 4 | `—` | — | — | — |
| `Label56` | `TLabel` | Usuário: | — | `—` | — | — | — |
| `Label57` | `TLabel` | Senha: | — | `—` | — | — | — |
| `edtUsuarioControlIDAntena` | `TEdit` | — | 0 | `—` | 30 | Text=admin | — |
| `edtSenhaControlIDAntena` | `TEdit` | — | 1 | `—` | 30 | Text=admin | — |
| `cbxExibirSenhaControlIDAntena` | `TCheckBox` | Exibir senha | 2 | `—` | — | — | OnClick=cbxExibirSenhaControlIDAntenaClick |
| `TabTopDataFit` | `TTabSheet` | TopData Fit | — | `—` | — | — | — |
| `Label60` | `TLabel` | Nº Funis | — | `—` | — | — | — |
| `Label61` | `TLabel` | Acionamento | — | `—` | — | — | — |
| `Label62` | `TLabel` | Sentido Entrada | — | `—` | — | — | — |
| `Label64` | `TLabel` | Time Out | — | `—` | — | — | — |
| `Label65` | `TLabel` | Modo de Trabalho | — | `—` | — | — | — |
| `Label81` | `TLabel` | 1 a 65 (recomendado 20) | — | `—` | — | — | — |
| `Label82` | `TLabel` | Terminal | — | `—` | — | — | — |
| `Label83` | `TLabel` | Msg Liberado | — | `—` | — | — | — |
| `Label84` | `TLabel` | Msg Bloqueado | — | `—` | — | — | — |
| `Label85` | `TLabel` | Msg Padrão | — | `—` | — | — | — |
| `Label86` | `TLabel` | Msg Urna | — | `—` | — | — | — |
| `Label87` | `TLabel` | Msg QRCode | — | `—` | — | — | — |
| `Label88` | `TLabel` | Dígitos no Teclado | — | `—` | — | — | — |
| `Label89` | `TLabel` | Tamanho do QR Code | — | `—` | — | — | — |
| `Label90` | `TLabel` | Formato do QR Code | — | `—` | — | — | — |
| `Label91` | `TLabel` | Tipo Leitor | — | `—` | — | — | — |
| `Label92` | `TLabel` | Quantidade Dígitos | — | `—` | — | — | — |
| `Label95` | `TLabel` | Tempo Acionamento | — | `—` | — | — | — |
| `Label94` | `TLabel` | Sentido do Fluxo | — | `—` | — | — | — |
| `Label93` | `TLabel` | Porta | — | `—` | — | — | — |
| `edtTerminalTopData` | `TSpinEdit` | — | 0 | `—` | 3 | — | — |
| `edtTimeOutTopData` | `TSpinEdit` | — | 1 | `—` | — | — | — |
| `cbxSentidoEntradaTopData` | `TComboBox` | — | 2 | `—` | — | — | — |
| `cbxAcionamentoTopData` | `TComboBox` | — | 3 | `—` | — | — | — |
| `cbxNrFunisTopData` | `TComboBox` | — | 4 | `—` | — | — | — |
| `cbxModoTrabalhoTopData` | `TComboBox` | — | 5 | `—` | — | — | — |
| `cbxTipoLeitorTopData` | `TComboBox` | — | 6 | `—` | — | — | — |
| `edtQtdDigitosTopData` | `TSpinEdit` | — | 7 | `—` | — | — | — |
| `cbxModoCatracaTopData` | `TComboBox` | — | 8 | `—` | — | — | — |
| `edtTempoAcionamentoTopData` | `TSpinEdit` | — | 9 | `—` | — | — | — |
| `edtMsgLiberadoTopData` | `TEdit` | — | 10 | `—` | — | Text=Acesso Liberado | — |
| `edtMsgBloqueadoTopData` | `TEdit` | — | 11 | `—` | — | Text=Acesso Bloqueado | — |
| `edtMsgPadraoTopData` | `TEdit` | — | 12 | `—` | — | Text=Passe o cartao | — |
| `edtMsgUrnaTopData` | `TEdit` | — | 13 | `—` | — | Text=Utilize a urna | — |
| `edtMsgQRCodeTopData` | `TEdit` | — | 14 | `—` | — | Text=Leia o QR Code | — |
| `edtDigitosTecladoTopData` | `TSpinEdit` | — | 15 | `—` | — | — | — |
| `edtQRCodeTamanhoTopData` | `TSpinEdit` | — | 16 | `—` | — | — | — |
| `edtQRCodeFormatoTopData` | `TEdit` | — | 17 | `—` | — | — | — |
| `chkUrnaTopData` | `TCheckBox` | Utilizar urna para visitantes | 18 | `—` | — | — | — |
| `chkProximidadeTopData` | `TCheckBox` | Proximidade | 19 | `—` | — | Checked=True | — |
| `chkBiometriaTopData` | `TCheckBox` | Biometria | 20 | `—` | — | — | — |
| `chkQRCodeTopData` | `TCheckBox` | QR Code | 21 | `—` | — | — | — |
| `chkTecladoTopData` | `TCheckBox` | Ecoar Asterisco | 22 | `—` | — | — | — |
| `edtPortaTopData` | `TSpinEdit` | — | 23 | `—` | 5 | — | — |
| `TabFuncao` | `TTabSheet` | Funções | — | `—` | — | — | — |
| `Label30` | `TLabel` | Acesso: | — | `—` | — | — | — |
| `Label74` | `TLabel` | Consumo: | — | `—` | — | — | — |
| `Label75` | `TLabel` | Reserva: | — | `—` | — | — | — |
| `EdFuncAcesso` | `TEdit` | — | 0 | `—` | — | Text=0 | — |
| `EdFuncReserva` | `TEdit` | — | 1 | `—` | — | — | — |
| `EdFuncConsumo` | `TEdit` | — | 2 | `—` | — | — | — |
| `TabMensagens` | `TTabSheet` | Mensagens | — | `—` | — | — | — |
| `lblLiberado` | `TLabel` | lblLiberado | — | `—` | — | — | — |
| `mlMensagens` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `lblBloqueado` | `TLabel` | lblBloqueado | — | `—` | — | — | — |
| `MetaEquipLocalizar1` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `Label49` | `TLabel` | Acesso liberado: | — | `—` | — | — | — |
| `Label50` | `TLabel` | Acesso bloqueado: | — | `—` | — | — | — |
| `EdLiberado` | `TEdit` | — | 0 | `—` | — | — | OnExit=EdLiberadoExit |
| `EdBloqueado` | `TEdit` | — | 1 | `—` | — | — | OnExit=EdBloqueadoExit |
| `Campos` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Panel4` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `ActionList1` | `TActionList` (herdado) | — | — | `—` | — | — | — |
| `ActExcluir` | `TAction` (herdado) | — | — | `—` | — | Visible=False, Enabled=False | — |
| `ActTSNome` | `TAction` | ActTSNome | — | `—` | — | — | — |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 606: `Arquivo de licença não encontrado: `
- Linha 617: `Arquivo de licença vazio ou inválido.`
- Linha 631: `Não foi possível carregar os dados da licença.`
- Linha 698: `Problemas com a exclusão no Banco de Dados!`
- Linha 771: `Arquivo de licença não encontrado: `
- Linha 783: `Arquivo de licença vazio ou inválido.`
- Linha 878: `Arquivo de licença não encontrado: `
- Linha 890: `Arquivo de licença vazio ou inválido.`
- Linha 1492: `Arquivo de licença não encontrado.`
- Linha 1504: `Arquivo de licença inválido.`
- Linha 1549: `ID do filtro inválido. Digite um número válido.`
- Linha 1577: `Filtro não cadastrado com o ID informado.`
- Linha 1591: `Erro ao buscar filtro: `
- Linha 2653: `Modelo de coletor não especificado`
- Linha 2716: `Modelo de coletor não especificado`
- Linha 2739: `O Nome do coletor é obrigatório.`
- Linha 2748: `O Modelo do coletor é obrigatório.`
- Linha 2757: `Endereço IP inválido!`
- Linha 2771: `Este endereço IP está sendo usado pelo coletor: `
- Linha 2788: `O Terminal do coletor é obrigatório.`
- Linha 2805: `Este Nº de Terminal está sendo usado pelo coletor: `
- Linha 2826: `O Acionamento do coletor deve ser informado.`
- Linha 2834: `O Nº de Funis do coletor deve ser informado.`
- Linha 2843: `O TimeOut do coletor deve ser de 1 até 65.`
- Linha 2857: `O Terminal do coletor é obrigatório.`
- Linha 2873: `Este Nº de Terminal está sendo usado pelo coletor: `
- Linha 2886: `O TimeOut do coletor deve ser de 1 até 65.`
- Linha 2905: `O Terminal do coletor `
- Linha 2922: `Este N`
- Linha 2934: `O TimeOut do coletor deve ser de 1 at`
- Linha 2946: `É necessário informar a Função de Acesso.`
- Linha 2956: `Funções não podem ter o mesmo valor.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActAlterarExecute`
- `ActCancelarExecute`
- `ActExcluirExecute`
- `ActExibirTudoExecute`
- `ActIncluirExecute`
- `ActIrExecute`
- `ActSalvarExecute`
- `ActTSNomeExecute`
- `ValidarCampos`

## Fluxo e regras identificados

O fluxo herdado de seleção, consulta, geração e fechamento está em [base_relatorio_padrao.md](base_relatorio_padrao.md). Salvar, Excluir e Cancelar de cadastro não se aplicam a este formulário.

- `ValidarCampos`: Nome e Modelo obrigatórios; IP precisa passar `ValidarIP` e ser único entre coletores. Mensagens: `O Nome do coletor é obrigatório.`, `O Modelo do coletor é obrigatório.`, `Endereço IP inválido!`. IP duplicado mostra `Este endereço IP está sendo usado pelo coletor: ` + CR + ID/Nome + CR + `Informe outro endereço IP.`.
- `ValidarCampos`: Dimep Micropoint, Biopoint e TopData Fit exigem Terminal positivo e exclusivo por marca. Micropoint exige Sentido de Entrada, Acionamento e Nº de Funis; as mensagens literais são `O Sentido de Entra da do coletor deve ser informado.`, `O Acionamento do coletor deve ser informado.` e `O Nº de Funis do coletor deve ser informado.`.
- `ValidarCampos`: TopData Fit exige TimeOut de 1 a 65 com `O TimeOut do coletor deve ser de 1 até 65.`. Em Micropoint/Biopoint a condição usa `> 65 and < 1`, impossível para um único valor: dúvida/possível defeito; não usar como asserção de faixa nessas marcas sem confirmar o build.
- `ValidarCampos`: Função de Acesso obrigatória (`É necessário informar a Função de Acesso.`); funções de Acesso, Reserva e Consumo não podem repetir o mesmo valor (`Funções não podem ter o mesmo valor.`). Campos obrigatórios por marca são selecionados pela aba de configuração.
- `ActExcluirExecute`: aviso exato fixo `ATENÇÃO! Ao fazer exclusão de um coletor todos os dados relacionados a ele, incluindo MARCAÇÕES ONLINE, serão PERDIDOS PERMANENTEMENTE.` seguido de quebra de linha e `Tem certeza que deseja excluir este coletor?`; só exclui após Sim. O código declara perda permanente; confirmar no DAO e no banco de teste antes de automatizar.
- `ActCancelarExecute`: chama o Cancelar herdado e seleciona aba Geral. `GravaCampos` primeiro chama `EdModelo.OnExit`, valida/monta IP e preenche `FColetoresModel` com dados das abas antes de persistir via controller. Não há relatório nesta unit.
- Fonte: `Acesso/uFrmCadColetores.pas`, procedures `ValidarCampos`, `GravaCampos`, `ActExcluirExecute` e `ActCancelarExecute`.

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
