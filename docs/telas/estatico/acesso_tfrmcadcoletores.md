# Acesso: TFrmCadColetores

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Coletores > Cadastro de Coletores....

- DFM: `Acesso/uFrmCadColetores.dfm`
- PAS: `Acesso/uFrmCadColetores.pas`
- Handler de abertura: `acCadColetoresExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadColetores | TFrmCadColetores | outro | Cadastro de Coletores | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | Visible=False, Enabled=False |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| PgCadastro | TPageControl | contêiner | — | 1 | — | — | — |
| TabGeral | TTabSheet | contêiner | Geral | — | — | — | — |
| Label12 | TLabel | rótulo | Minutos | — | — | — | Visible=False |
| lblNomeModelo | TLabel | rótulo | lblNomeModelo | — | — | — | — |
| mlModelo | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| Image50 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| Label11 | TLabel | rótulo | Fuso horário: | — | — | — | Visible=False |
| Image51 | TImage | outro | — | — | — | — | Visible=False |
| Label3 | TLabel | rótulo | Situação: | — | — | — | — |
| Image52 | TImage | outro | — | — | — | — | — |
| Label55 | TLabel | rótulo | Modelo: | — | — | — | — |
| Image53 | TImage | outro | — | — | — | — | — |
| Image54 | TImage | outro | — | — | — | — | — |
| Label58 | TLabel | rótulo | IP: | — | — | — | — |
| Label2 | TLabel | rótulo | Comunicação: | — | — | — | — |
| Image55 | TImage | outro | — | — | — | — | — |
| Image56 | TImage | outro | — | — | — | — | — |
| Label4 | TLabel | rótulo | Filtro de Pessoas: | — | — | — | — |
| MetaEquipLocalizar2 | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblFiltroPessoas | TLabel | rótulo | lblFiltroPessoas | — | — | — | — |
| Image63 | TImage | outro | — | — | — | — | — |
| Label32 | TLabel | rótulo | Proximidade: | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | Text=EDNOME |
| EdModelo | TEdit | campo de texto/data | — | 1 | — | — | Text=EdModelo, Visible=False, Enabled=False |
| cmbStatus | TComboBox | seleção | — | 2 | — | — | Text=Ativo, ItemIndex=0 |
| cmbComunicacao | TComboBox | seleção | — | 3 | — | — | Text=RealTime, ItemIndex=1 |
| CmbFusoHorario | TComboBox | seleção | — | 5 | — | — | Visible=False |
| EdFusoHorario | TEdit | campo de texto/data | — | 4 | — | — | Text=EdFusoHorario, Visible=False |
| GroupBox1 | TGroupBox | contêiner | Transformar Função  | 6 | — | — | — |
| Label73 | TLabel | rótulo | Função de Entrada: | — | — | — | — |
| Image7 | TImage | outro | — | — | — | — | — |
| Label6 | TLabel | rótulo | Função de Saída: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| EdFuncaoEntrada | TEdit | campo de texto/data | — | 0 | — | — | — |
| EdFuncaoSaida | TEdit | campo de texto/data | — | 1 | — | — | — |
| gbxRefeitorioCardapio | TGroupBox | contêiner |  Refeitório | 7 | — | — | — |
| mlRefeitorio | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblRefeitorio | TLabel | rótulo | lblRefeitorio | — | — | — | — |
| Label31 | TLabel | rótulo | Refeitório: | — | — | — | — |
| Image62 | TImage | outro | — | — | — | — | — |
| EdRefeitorio | TEdit | campo de texto/data | — | 0 | — | — | — |
| pnlIp | TPanel | contêiner | — | 8 | — | — | — |
| LblP1 | TLabel | rótulo | . | — | — | — | — |
| LblP2 | TLabel | rótulo | . | — | — | — | — |
| LblP3 | TLabel | rótulo | . | — | — | — | — |
| EdIp1 | TEdit | campo de texto/data | — | 0 | — | 3 | Text=192 |
| EdIp2 | TEdit | campo de texto/data | — | 1 | — | 3 | Text=168 |
| EdIp3 | TEdit | campo de texto/data | — | 2 | — | 3 | Text=000 |
| EdIp4 | TEdit | campo de texto/data | — | 3 | — | 3 | Text=000 |
| EdFiltroPessoas | TEdit | campo de texto/data | — | 9 | — | — | Text=EdFiltroPessoas, Enabled=False |
| cmbProximidade | TComboBox | seleção | — | 10 | — | — | Text=Acura, ItemIndex=0 |
| TabConfig | TTabSheet | contêiner | Configurações | — | — | — | — |
| pcConfigEspecif | TPageControl | contêiner | — | 0 | — | — | — |
| TabDimepMicroPoint | TTabSheet | contêiner | TabDimepMicroPoint | — | — | — | — |
| Label13 | TLabel | rótulo | Sentido Entrada | — | — | — | — |
| Label14 | TLabel | rótulo | Acionamento | — | — | — | — |
| Label15 | TLabel | rótulo | Nº Funis | — | — | — | — |
| Label16 | TLabel | rótulo | Time Out | — | — | — | — |
| Label17 | TLabel | rótulo | Terminal | — | — | — | — |
| Label20 | TLabel | rótulo | 1 a 65 (recomendado 20) | — | — | — | — |
| Label29 | TLabel | rótulo | Modo de Trabalho | — | — | — | — |
| cbxSentidoEntradaDimepMicropoint | TComboBox | seleção | — | 2 | — | — | — |
| cbxAcionamentoDimepMicropoint | TComboBox | seleção | — | 3 | — | — | — |
| cbxNrFunisDimepMicropoint | TComboBox | seleção | — | 4 | — | — | — |
| edtTimeOutDimepMicropoint | TSpinEdit | campo de texto/data | — | 1 | — | — | — |
| edtTerminalDimepMicropoint | TSpinEdit | campo de texto/data | — | 0 | — | 3 | — |
| cbxUsarUrnaDimepMicropoint | TCheckBox | seleção | Utilizar urna para visitantes | 6 | — | — | — |
| cbxModoTrabalhoDimepMicropoint | TComboBox | seleção | — | 5 | — | — | — |
| TabDimepBioPoint | TTabSheet | contêiner | TabDimepBioPoint | — | — | — | — |
| Label21 | TLabel | rótulo | 1 a 65 | — | — | — | — |
| Label28 | TLabel | rótulo | 0 a 99 | — | — | — | — |
| Label5 | TLabel | rótulo | Terminal: | — | — | — | — |
| Image57 | TImage | outro | — | — | — | — | — |
| Image58 | TImage | outro | — | — | — | — | — |
| Label10 | TLabel | rótulo | Sentido do Giro: | — | — | — | — |
| Label18 | TLabel | rótulo | Timeout (s): | — | — | — | — |
| Image59 | TImage | outro | — | — | — | — | — |
| Label19 | TLabel | rótulo | Tempo Acionamento (s): | — | — | — | — |
| Image60 | TImage | outro | — | — | — | — | — |
| Label59 | TLabel | rótulo | Acionamento: | — | — | — | — |
| Image61 | TImage | outro | — | — | — | — | — |
| Label22 | TLabel | rótulo | Liberação Entrada: | — | — | — | — |
| Image64 | TImage | outro | — | — | — | — | — |
| Label23 | TLabel | rótulo | Liberação Saída: | — | — | — | — |
| Image65 | TImage | outro | — | — | — | — | — |
| Image66 | TImage | outro | — | — | — | — | — |
| Label24 | TLabel | rótulo | Validação de Digital: | — | — | — | — |
| Image67 | TImage | outro | — | — | — | — | — |
| edtTimeOutDimepBiopoint | TSpinEdit | campo de texto/data | — | 1 | — | — | — |
| edtTerminalDimepBiopoint | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| cbxAcionamentoDimepBiopoint | TComboBox | seleção | — | 2 | — | — | Text=Catraca bidirecional com sentido de giro independente do leitor, ItemIndex=7 |
| cbxLiberaEntradaDimepBiopoint | TComboBox | seleção | — | 5 | — | — | — |
| cbxLiberaSaidaDimepBiopoint | TComboBox | seleção | — | 6 | — | — | — |
| cbxSentidoGiroDimepBiopoint | TComboBox | seleção | — | 4 | — | — | Text=Horário, ItemIndex=1 |
| cbxValidaDigitalDimepBiopoint | TComboBox | seleção | — | 7 | — | — | — |
| edtTempoAcionamentoDimepBiopoint | TSpinEdit | campo de texto/data | — | 3 | — | — | — |
| cbxUsarUrnaDimepBiopoint | TCheckBox | seleção | Utilizar urna para visitantes | 8 | — | — | — |
| TabControl_ID | TTabSheet | contêiner | TabControl_ID | — | — | — | — |
| gbxLeitoresControlID | TGroupBox | contêiner | Leitores  | 2 | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| Image12 | TImage | outro | — | — | — | — | — |
| Image13 | TImage | outro | — | — | — | — | — |
| cbxWiegandControlID | TCheckBox | seleção | Converte Código Wiegand (RFID) | 0 | — | — | — |
| cbxPossuiBiometriaControlID | TCheckBox | seleção | Possui Biometria | 1 | — | — | — |
| cbxPossuiFaceControlID | TCheckBox | seleção | Possui Face | 2 | — | — | — |
| gbxConfigEquipamentoControlID | TGroupBox | contêiner | Configuração do Equipamento  | 1 | — | — | — |
| Label36 | TLabel | rótulo | Sentido do Fluxo: | — | — | — | — |
| Label37 | TLabel | rótulo | Timeout (ms): | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| Image10 | TImage | outro | — | — | — | — | — |
| edtTimeOutControlID | TSpinEdit | campo de texto/data | — | 0 | — | 9 | — |
| cbxSentidoFluxoControlID | TComboBox | seleção | — | 1 | — | — | — |
| gbxConfiguracaoControlID | TGroupBox | contêiner | Configuração  | 0 | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| Label9 | TLabel | rótulo | IP do Servidor: | — | — | — | — |
| Label33 | TLabel | rótulo | Porta: | — | — | — | — |
| Image6 | TImage | outro | — | — | — | — | — |
| Image8 | TImage | outro | — | — | — | — | — |
| Label34 | TLabel | rótulo | Porta de Escuta: | — | — | — | — |
| edtIpServidorControlID | TEdit | campo de texto/data | — | 1 | — | — | Text=192.168.000.000 |
| cbxIpAutomaticoControlID | TCheckBox | seleção | IP Automático | 2 | — | — | — |
| edtPortaControlID | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| edtPortaEscutaControlID | TSpinEdit | campo de texto/data | — | 3 | — | 4 | — |
| gbxAutenticacaoControlID | TGroupBox | contêiner | Autenticação  | 3 | — | — | — |
| Label7 | TLabel | rótulo | Usuário: | — | — | — | — |
| Label8 | TLabel | rótulo | Senha: | — | — | — | — |
| Image15 | TImage | outro | — | — | — | — | — |
| Image16 | TImage | outro | — | — | — | — | — |
| edtUsuarioControlID | TEdit | campo de texto/data | — | 0 | — | 30 | Text=admin |
| edtSenhaControlID | TEdit | campo de texto/data | — | 1 | — | 30 | Text=admin |
| cbxExibirSenhaControlID | TCheckBox | seleção | Exibir senha | 2 | — | — | — |
| gbSyncBioControlID | TGroupBox | contêiner | Tipo de sincronização de digitais | 4 | — | — | — |
| Image71 | TImage | outro | — | — | — | — | — |
| Label26 | TLabel | rótulo | Tipo de Sincronização: | — | — | — | — |
| SpinEdit3 | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| cmbSyncBioControlID | TComboBox | seleção | — | 1 | — | — | — |
| TabControl_ID_Catraca | TTabSheet | contêiner | TabControl_ID_Catraca | — | — | — | — |
| GbxConfigIDBlock | TGroupBox | contêiner | Configuração  | 0 | — | — | — |
| Image17 | TImage | outro | — | — | — | — | — |
| Label35 | TLabel | rótulo | Porta: | — | — | — | — |
| Label38 | TLabel | rótulo | IP do Servidor: | — | — | — | — |
| Image18 | TImage | outro | — | — | — | — | — |
| Image19 | TImage | outro | — | — | — | — | — |
| Label39 | TLabel | rótulo | Porta de Escuta: | — | — | — | — |
| edtIpServidorIDBlock | TEdit | campo de texto/data | — | 1 | — | — | Text=192.168.000.000 |
| cbxIpAutomaticoIDBlock | TCheckBox | seleção | IP Automático | 2 | — | — | — |
| edtPortaIDBlock | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| edtPortaEscutaIDBlock | TSpinEdit | campo de texto/data | — | 3 | — | 4 | — |
| GroupBox3 | TGroupBox | contêiner | Autenticação  | 1 | — | — | — |
| Label43 | TLabel | rótulo | Usuário: | — | — | — | — |
| Image23 | TImage | outro | — | — | — | — | — |
| Image24 | TImage | outro | — | — | — | — | — |
| Label44 | TLabel | rótulo | Senha: | — | — | — | — |
| edtUsuarioIDBlock | TEdit | campo de texto/data | — | 0 | — | 30 | Text=admin |
| edtSenhaIDBlock | TEdit | campo de texto/data | — | 1 | — | 30 | Text=admin |
| cbxExibirSenhaIDBlock | TCheckBox | seleção | Exibir senha | 2 | — | — | — |
| gbxLeitoresIDBlock | TGroupBox | contêiner | Leitores  | 2 | — | — | — |
| Image25 | TImage | outro | — | — | — | — | — |
| Image26 | TImage | outro | — | — | — | — | — |
| Image27 | TImage | outro | — | — | — | — | — |
| cbxWiegandIDBlock | TCheckBox | seleção | Converte Código Wiegand (RFID) | 0 | — | — | — |
| cbxPossuiBiometriaIDBlock | TCheckBox | seleção | Possui Biometria | 1 | — | — | — |
| cbxPossuiFaceIDBlock | TCheckBox | seleção | Possui Face | 2 | — | — | — |
| GbxConfigEquip | TGroupBox | contêiner | Configuração do Equipamento  | 3 | — | — | — |
| Image20 | TImage | outro | — | — | — | — | — |
| Image21 | TImage | outro | — | — | — | — | — |
| Image22 | TImage | outro | — | — | — | — | — |
| Label40 | TLabel | rótulo | Sentido do Fluxo: | — | — | — | — |
| Label41 | TLabel | rótulo | Timeout (ms): | — | — | — | — |
| Label42 | TLabel | rótulo | Sentido do Giro: | — | — | — | — |
| edtTimeOutIDBlock | TSpinEdit | campo de texto/data | — | 0 | — | 9 | — |
| cbxSentidoFluxoIDBlock | TComboBox | seleção | — | 1 | — | — | — |
| CmbSentido | TComboBox | seleção | — | 2 | — | — | — |
| gbxUrnaIDBlock | TGroupBox | contêiner | Urna | 4 | — | — | — |
| Image68 | TImage | outro | — | — | — | — | — |
| chkUrnaIDBlock | TCheckBox | seleção | Utilizar urna para visitantes | 0 | — | — | — |
| SpinEdit2 | TSpinEdit | campo de texto/data | — | 1 | — | 4 | — |
| gbSyncBio | TGroupBox | contêiner | Tipo de sincronização de digitais | 5 | — | — | — |
| Image70 | TImage | outro | — | — | — | — | — |
| Label25 | TLabel | rótulo | Tipo de Sincronização: | — | — | — | — |
| SpinEdit1 | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| cmbSyncBioIDBlock | TComboBox | seleção | — | 1 | — | — | — |
| TabControl_ID_Next | TTabSheet | contêiner | TabControl_ID_Next | — | — | — | — |
| GroupBox12 | TGroupBox | contêiner | Configuração do Equipamento  | 0 | — | — | — |
| Image28 | TImage | outro | — | — | — | — | — |
| Image29 | TImage | outro | — | — | — | — | — |
| Image30 | TImage | outro | — | — | — | — | — |
| Label45 | TLabel | rótulo | Sentido do Fluxo: | — | — | — | — |
| Label46 | TLabel | rótulo | Timeout (ms): | — | — | — | — |
| Label47 | TLabel | rótulo | Sentido do Giro: | — | — | — | — |
| edtTimeOutControlIDNext | TSpinEdit | campo de texto/data | — | 0 | — | 9 | — |
| cbxSentidoFluxoControlIDNext | TComboBox | seleção | — | 1 | — | — | — |
| cbxSentidoGiroControlIDNext | TComboBox | seleção | — | 2 | — | — | — |
| GroupBox13 | TGroupBox | contêiner | Configuração  | 1 | — | — | — |
| Image31 | TImage | outro | — | — | — | — | — |
| Label76 | TLabel | rótulo | Porta: | — | — | — | — |
| Label77 | TLabel | rótulo | IP do Servidor: | — | — | — | — |
| Image32 | TImage | outro | — | — | — | — | — |
| Image33 | TImage | outro | — | — | — | — | — |
| Label78 | TLabel | rótulo | Porta de Escuta: | — | — | — | — |
| edtPortaEscutaControlIDNext | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| edtIpServidorControlIDNext | TEdit | campo de texto/data | — | 1 | — | — | Text=192.168.000.000 |
| cbxIpAutomaticoControlIDNext | TCheckBox | seleção | IP Automático | 2 | — | — | — |
| edtPortaControlIDNext | TSpinEdit | campo de texto/data | — | 3 | — | 4 | — |
| GroupBox14 | TGroupBox | contêiner | Autenticação  | 2 | — | — | — |
| Label79 | TLabel | rótulo | Usuário: | — | — | — | — |
| Image34 | TImage | outro | — | — | — | — | — |
| Image35 | TImage | outro | — | — | — | — | — |
| Label80 | TLabel | rótulo | Senha: | — | — | — | — |
| edtUsuarioControlIDNext | TEdit | campo de texto/data | — | 0 | — | 30 | Text=admin |
| edtSenhaControlIDNext | TEdit | campo de texto/data | — | 1 | — | 30 | Text=admin |
| cbxExibirSenhaControlIDNext | TCheckBox | seleção | Exibir senha | 2 | — | — | — |
| GroupBox15 | TGroupBox | contêiner | Leitores  | 3 | — | — | — |
| Image36 | TImage | outro | — | — | — | — | — |
| Image37 | TImage | outro | — | — | — | — | — |
| Image38 | TImage | outro | — | — | — | — | — |
| cbxWiegandControlIDNext | TCheckBox | seleção | Converte Código Wiegand (RFID) | 0 | — | — | — |
| cbxPossuiBiometriaControlIDNext | TCheckBox | seleção | Possui Biometria | 1 | — | — | — |
| cbxPossuiFaceControlIDNext | TCheckBox | seleção | Possui Face | 2 | — | — | — |
| GroupBox16 | TGroupBox | contêiner | Urna | 4 | — | — | — |
| Image69 | TImage | outro | — | — | — | — | — |
| SpinEdit6 | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| chkUrnaIDBlockNext | TCheckBox | seleção | Utilizar urna para visitantes | 1 | — | — | — |
| GroupBox7 | TGroupBox | contêiner | Tipo de sincronização de digitais | 5 | — | — | — |
| Image14 | TImage | outro | — | — | — | — | — |
| Label27 | TLabel | rótulo | Tipo de Sincronização: | — | — | — | — |
| SpinEdit4 | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| cmbSyncBioIDNext | TComboBox | seleção | — | 1 | — | — | — |
| TabControl_ID_Antena | TTabSheet | contêiner | TabControl_ID_Antena | — | — | — | — |
| gpbLeitorUHF | TGroupBox | contêiner | Leitor UHF | 0 | — | — | — |
| PageControl1 | TPageControl | contêiner | — | 0 | — | — | — |
| TabSheet3 | TTabSheet | contêiner | Geral | — | — | — | — |
| Label63 | TLabel | rótulo | Saída Wiegand (bits): | — | — | — | — |
| Label66 | TLabel | rótulo | Potência de transmissão (dBm): | — | — | — | — |
| Label67 | TLabel | rótulo | Modo de Operação: | — | — | — | — |
| Label68 | TLabel | rótulo | Intervalo entre leituras da mesma tag (ms): | — | — | — | — |
| Label69 | TLabel | rótulo | Intervalo entre leituras da tags diferentes (ms): | — | — | — | — |
| EdSaidaWiegand | TComboBox | seleção | — | 0 | — | — | Text=26, ItemIndex=0 |
| EdPodenciaTransmissao | TEdit | campo de texto/data | — | 1 | — | 30 | Text=2400 |
| cbxModoOperacao | TComboBox | seleção | — | 2 | — | — | Text=Contínuo, ItemIndex=0 |
| EdIntMesmaTag | TEdit | campo de texto/data | — | 3 | — | 30 | Text=5000 |
| EdIntTagsDiferentes | TEdit | campo de texto/data | — | 4 | — | 30 | Text=100 |
| TabSheet4 | TTabSheet | contêiner | Avançado | — | — | — | — |
| Label70 | TLabel | rótulo | Ordem dos bytes | — | — | — | — |
| Label71 | TLabel | rótulo | Seleção de Canal  (MHz) | — | — | — | — |
| cbxOrdemBytes | TComboBox | seleção | — | 0 | — | — | Text=Padrão, ItemIndex=0 |
| cbxSelCanal01 | TCheckBox | seleção | 902.25 | 1 | — | — | Checked=True |
| cbxSelCanal02 | TCheckBox | seleção | 902.75 | 2 | — | — | — |
| cbxSelCanal03 | TCheckBox | seleção | 903.25 | 3 | — | — | — |
| cbxSelCanal04 | TCheckBox | seleção | 903.75 | 4 | — | — | — |
| cbxSelCanal05 | TCheckBox | seleção | 904.25 | 5 | — | — | — |
| cbxSelCanal06 | TCheckBox | seleção | 904.75 | 6 | — | — | — |
| cbxSelCanal07 | TCheckBox | seleção | 905.25 | 7 | — | — | — |
| cbxSelCanal08 | TCheckBox | seleção | 905.75 | 8 | — | — | — |
| cbxSelCanal09 | TCheckBox | seleção | 906.25 | 9 | — | — | — |
| cbxSelCanal10 | TCheckBox | seleção | 906.75 | 10 | — | — | — |
| cbxSelCanal11 | TCheckBox | seleção | 907.25 | 11 | — | — | — |
| cbxSelCanal12 | TCheckBox | seleção | 915.25 | 12 | — | — | — |
| cbxSelCanal13 | TCheckBox | seleção | 915.75 | 13 | — | — | — |
| cbxSelCanal14 | TCheckBox | seleção | 916.25 | 14 | — | — | — |
| cbxSelCanal15 | TCheckBox | seleção | 916.75 | 15 | — | — | — |
| cbxSelCanal16 | TCheckBox | seleção | 917.25 | 16 | — | — | — |
| cbxSelCanal17 | TCheckBox | seleção | 917.75 | 17 | — | — | — |
| cbxSelCanal18 | TCheckBox | seleção | 918.25 | 18 | — | — | — |
| cbxSelCanal19 | TCheckBox | seleção | 918.75 | 19 | — | — | — |
| cbxSelCanal20 | TCheckBox | seleção | 919.25 | 20 | — | — | — |
| cbxSelCanal21 | TCheckBox | seleção | 919.75 | 21 | — | — | — |
| cbxSelCanal22 | TCheckBox | seleção | 920.25 | 22 | — | — | — |
| cbxSelCanal23 | TCheckBox | seleção | 920.75 | 23 | — | — | — |
| cbxSelCanal24 | TCheckBox | seleção | 921.25 | 24 | — | — | — |
| cbxSelCanal25 | TCheckBox | seleção | 921.75 | 25 | — | — | — |
| cbxSelCanal26 | TCheckBox | seleção | 922.25 | 26 | — | — | — |
| cbxSelCanal27 | TCheckBox | seleção | 922.75 | 27 | — | — | — |
| cbxSelCanal28 | TCheckBox | seleção | 923.25 | 28 | — | — | — |
| cbxSelCanal29 | TCheckBox | seleção | 923.75 | 29 | — | — | — |
| cbxSelCanal30 | TCheckBox | seleção | 924.25 | 30 | — | — | — |
| cbxSelCanal31 | TCheckBox | seleção | 924.75 | 31 | — | — | — |
| cbxSelCanal32 | TCheckBox | seleção | 625.25 | 32 | — | — | — |
| cbxSelCanal33 | TCheckBox | seleção | 925.75 | 33 | — | — | — |
| cbxSelCanal34 | TCheckBox | seleção | 926.25 | 34 | — | — | — |
| cbxSelCanal35 | TCheckBox | seleção | 926.75 | 35 | — | — | — |
| cbxSelCanal36 | TCheckBox | seleção | 927.25 | 36 | — | — | — |
| cbxSelCanal37 | TCheckBox | seleção | 927.75 | 37 | — | — | — |
| TabSheet5 | TTabSheet | contêiner | Sensores e Atuadores | — | — | — | — |
| Label72 | TLabel | rótulo | Modo de Operação | — | — | — | — |
| rbModoOpeAcionamento | TRadioButton | seleção | Acionamento do Motor (padrão) | 0 | — | — | Checked=True |
| rbModoOpeDeteccao | TRadioButton | seleção | Detecção de tag | 1 | — | — | — |
| GroupBox2 | TGroupBox | contêiner | Configuração  | 1 | — | — | — |
| Image39 | TImage | outro | — | — | — | — | — |
| Label48 | TLabel | rótulo | Porta: | — | — | — | — |
| Label51 | TLabel | rótulo | IP do Servidor: | — | — | — | — |
| Image40 | TImage | outro | — | — | — | — | — |
| Image41 | TImage | outro | — | — | — | — | — |
| Label52 | TLabel | rótulo | Porta de Escuta: | — | — | — | — |
| edtPortaControlIDAntena | TSpinEdit | campo de texto/data | — | 0 | — | 4 | — |
| edtIpServidorControlIDAntena | TEdit | campo de texto/data | — | 1 | — | — | Text=192.168.000.000 |
| edtPortaEscutaControlIDAntena | TSpinEdit | campo de texto/data | — | 2 | — | 4 | — |
| cbxIpAutomaticoControlIDAntena | TCheckBox | seleção | IP Automático | 3 | — | — | — |
| GroupBox4 | TGroupBox | contêiner | Configuração do Equipamento  | 2 | — | — | — |
| Image42 | TImage | outro | — | — | — | — | — |
| Image43 | TImage | outro | — | — | — | — | — |
| Label53 | TLabel | rótulo | Sentido do Fluxo: | — | — | — | — |
| Label54 | TLabel | rótulo | Timeout (ms): | — | — | — | — |
| cbxSentidoFluxoControlIDAntena | TComboBox | seleção | — | 0 | — | — | — |
| edtTimeOutControlIDAntena | TSpinEdit | campo de texto/data | — | 1 | — | 9 | — |
| GroupBox5 | TGroupBox | contêiner | Leitores  | 3 | — | — | — |
| Image45 | TImage | outro | — | — | — | — | — |
| Image46 | TImage | outro | — | — | — | — | — |
| cbxWiegandControlIDAntena | TCheckBox | seleção | Converte Código Wiegand (RFID) | 0 | — | — | — |
| cbxPossuiAntena | TCheckBox | seleção | Possui Antena | 1 | — | — | — |
| GroupBox6 | TGroupBox | contêiner | Autenticação  | 4 | — | — | — |
| Label56 | TLabel | rótulo | Usuário: | — | — | — | — |
| Image48 | TImage | outro | — | — | — | — | — |
| Image49 | TImage | outro | — | — | — | — | — |
| Label57 | TLabel | rótulo | Senha: | — | — | — | — |
| edtUsuarioControlIDAntena | TEdit | campo de texto/data | — | 0 | — | 30 | Text=admin |
| edtSenhaControlIDAntena | TEdit | campo de texto/data | — | 1 | — | 30 | Text=admin |
| cbxExibirSenhaControlIDAntena | TCheckBox | seleção | Exibir senha | 2 | — | — | — |
| TabTopDataFit | TTabSheet | contêiner | TopData Fit | — | — | — | — |
| Label60 | TLabel | rótulo | Nº Funis | — | — | — | — |
| Label61 | TLabel | rótulo | Acionamento | — | — | — | — |
| Label62 | TLabel | rótulo | Sentido Entrada | — | — | — | — |
| Label64 | TLabel | rótulo | Time Out | — | — | — | — |
| Label65 | TLabel | rótulo | Modo de Trabalho | — | — | — | — |
| Label81 | TLabel | rótulo | 1 a 65 (recomendado 20) | — | — | — | — |
| Label82 | TLabel | rótulo | Terminal | — | — | — | — |
| Label83 | TLabel | rótulo | Msg Liberado | — | — | — | — |
| Label84 | TLabel | rótulo | Msg Bloqueado | — | — | — | — |
| Label85 | TLabel | rótulo | Msg Padrão | — | — | — | — |
| Label86 | TLabel | rótulo | Msg Urna | — | — | — | — |
| Label87 | TLabel | rótulo | Msg QRCode | — | — | — | — |
| Label88 | TLabel | rótulo | Dígitos no Teclado | — | — | — | — |
| Label89 | TLabel | rótulo | Tamanho do QR Code | — | — | — | — |
| Label90 | TLabel | rótulo | Formato do QR Code | — | — | — | — |
| Label91 | TLabel | rótulo | Tipo Leitor | — | — | — | — |
| Label92 | TLabel | rótulo | Quantidade Dígitos | — | — | — | — |
| Label95 | TLabel | rótulo | Tempo Acionamento | — | — | — | — |
| Label94 | TLabel | rótulo | Sentido do Fluxo | — | — | — | — |
| Label93 | TLabel | rótulo | Porta | — | — | — | — |
| edtTerminalTopData | TSpinEdit | campo de texto/data | — | 0 | — | 3 | — |
| edtTimeOutTopData | TSpinEdit | campo de texto/data | — | 1 | — | — | — |
| cbxSentidoEntradaTopData | TComboBox | seleção | — | 2 | — | — | — |
| cbxAcionamentoTopData | TComboBox | seleção | — | 3 | — | — | — |
| cbxNrFunisTopData | TComboBox | seleção | — | 4 | — | — | — |
| cbxModoTrabalhoTopData | TComboBox | seleção | — | 5 | — | — | — |
| cbxTipoLeitorTopData | TComboBox | seleção | — | 6 | — | — | — |
| edtQtdDigitosTopData | TSpinEdit | campo de texto/data | — | 7 | — | — | — |
| cbxModoCatracaTopData | TComboBox | seleção | — | 8 | — | — | — |
| edtTempoAcionamentoTopData | TSpinEdit | campo de texto/data | — | 9 | — | — | — |
| edtMsgLiberadoTopData | TEdit | campo de texto/data | — | 10 | — | — | Text=Acesso Liberado |
| edtMsgBloqueadoTopData | TEdit | campo de texto/data | — | 11 | — | — | Text=Acesso Bloqueado |
| edtMsgPadraoTopData | TEdit | campo de texto/data | — | 12 | — | — | Text=Passe o cartao |
| edtMsgUrnaTopData | TEdit | campo de texto/data | — | 13 | — | — | Text=Utilize a urna |
| edtMsgQRCodeTopData | TEdit | campo de texto/data | — | 14 | — | — | Text=Leia o QR Code |
| edtDigitosTecladoTopData | TSpinEdit | campo de texto/data | — | 15 | — | — | — |
| edtQRCodeTamanhoTopData | TSpinEdit | campo de texto/data | — | 16 | — | — | — |
| edtQRCodeFormatoTopData | TEdit | campo de texto/data | — | 17 | — | — | — |
| chkUrnaTopData | TCheckBox | seleção | Utilizar urna para visitantes | 18 | — | — | — |
| chkProximidadeTopData | TCheckBox | seleção | Proximidade | 19 | — | — | Checked=True |
| chkBiometriaTopData | TCheckBox | seleção | Biometria | 20 | — | — | — |
| chkQRCodeTopData | TCheckBox | seleção | QR Code | 21 | — | — | — |
| chkTecladoTopData | TCheckBox | seleção | Ecoar Asterisco | 22 | — | — | — |
| edtPortaTopData | TSpinEdit | campo de texto/data | — | 23 | — | 5 | — |
| TabFuncao | TTabSheet | contêiner | Funções | — | — | — | — |
| Label30 | TLabel | rótulo | Acesso: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| Label74 | TLabel | rótulo | Consumo: | — | — | — | — |
| Label75 | TLabel | rótulo | Reserva: | — | — | — | — |
| EdFuncAcesso | TEdit | campo de texto/data | — | 0 | — | — | Text=0 |
| EdFuncReserva | TEdit | campo de texto/data | — | 1 | — | — | — |
| EdFuncConsumo | TEdit | campo de texto/data | — | 2 | — | — | — |
| TabMensagens | TTabSheet | contêiner | Mensagens | — | — | — | — |
| lblLiberado | TLabel | rótulo | lblLiberado | — | — | — | — |
| mlMensagens | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblBloqueado | TLabel | rótulo | lblBloqueado | — | — | — | — |
| MetaEquipLocalizar1 | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| Image44 | TImage | outro | — | — | — | — | — |
| Label49 | TLabel | rótulo | Acesso liberado: | — | — | — | — |
| Label50 | TLabel | rótulo | Acesso bloqueado: | — | — | — | — |
| Image47 | TImage | outro | — | — | — | — | — |
| EdLiberado | TEdit | campo de texto/data | — | 0 | — | — | — |
| EdBloqueado | TEdit | campo de texto/data | — | 1 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| CdsColetores | TClientDataSet | outro | — | — | — | — | — |
| CdsColetoresId | TIntegerField | outro | — | — | — | — | — |
| CdsColetoresNome | TStringField | outro | — | — | — | — | — |
| CdsColetoresstatus | TIntegerField | outro | — | — | — | — | — |
| CdsColetoresidmodelo | TIntegerField | outro | — | — | — | — | — |
| CdsColetoresIP | TStringField | outro | — | — | — | — | — |
| CdsColetoresComunicacao | TIntegerField | outro | — | — | — | — | — |
| CdsColetoresfusosinal | TStringField | outro | — | — | — | — | — |
| CdsColetoresfusomin | TIntegerField | outro | — | — | — | — | — |
| CdsColetoresFuncEntrada | TStringField | outro | — | — | — | — | — |
| CdsColetoresFuncSaida | TStringField | outro | — | — | — | — | — |
| CdsColetoresFuncAcesso | TStringField | outro | — | — | — | — | — |
| CdsColetoresFuncReserva | TStringField | outro | — | — | — | — | — |
| CdsColetoresFuncConsumo | TStringField | outro | — | — | — | — | — |
| CdsColetoresModelo | TStringField | outro | — | — | — | — | — |
| CdsColetoresMarca | TIntegerField | outro | — | — | — | — | — |
| DsColetores | TDataSource | outro | — | — | — | — | — |
| DsModeloColetores | TDataSource | outro | — | — | — | — | — |
| CdsModeloColetores | TClientDataSet | outro | — | — | — | — | — |
| CdsModeloColetoresCODIGO | TIntegerField | outro | — | — | — | — | — |
| CdsModeloColetoresNOME | TStringField | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActTSNome | TAction | ação | ActTSNome | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActCancelarExecute` | 675 | — |
| `ActExcluirExecute` | 681 | `FColetoresController.Excluir` |
| `ActExibirTudoExecute` | 707 | `FColetoresController.GetColetoresTodos` |
| `ActIncluirExecute` | 755 | `FColetoresController.GetTotalColetoresAtivos` |
| `ActIrExecute` | 814 | `FColetoresController.GetColetor`, `FColetoresController.GetColetoresPorDescricao` |
| `ActSalvarExecute` | 855 | `FColetoresController.GetTotalColetoresAtivos`, `FColetoresController.VerificarColetorIPExistente`, `FColetoresController.ExcluirModelConfig` |
| `FormCreate` | 1939 | `TColetoresController.Create`, `FColetoresController.SetConexao`, `TModeloColetoresController.Create`, `FModeloColetoresController.SetConexao` |
| `GravaCampos` | 2166 | `FColetoresController.Inserir`, `FColetoresController.Atualizar` |
| `ValidarCampos` | 2731 | `FColetoresController.GetColetoresPorIP`, `FColetoresController.GetColetoresPorTerminal` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

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

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
