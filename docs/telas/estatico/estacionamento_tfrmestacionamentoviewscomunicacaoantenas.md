# Estacionamento: TFrmEstacionamentoViewsComunicacaoAntenas

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Comunicação com Equipamentos > Comunicação com Antenas.

- DFM: `Estacionamento/Views/ComunicacaoComEquipamentos/Acessus.Estacionamento.Views.ComunicacaoAntenas.dfm`
- PAS: `Estacionamento/Views/ComunicacaoComEquipamentos/Acessus.Estacionamento.Views.ComunicacaoAntenas.pas`
- Handler de abertura: `actComunicacaoComAntenasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEstacionamentoViewsComunicacaoAntenas | TFrmEstacionamentoViewsComunicacaoAntenas | outro | Comunicação com Antenas | — | — | — | Visible=True |
| PgComandos | TPageControl | contêiner | — | 0 | — | — | — |
| TabFilaComandos | TTabSheet | contêiner | Fila de Comandos | — | — | — | — |
| dbgFilaComandos | TDBGrid | grade | — | 0 | — | — | Visible=False |
| Panel11 | TPanel | contêiner | — | 1 | — | — | — |
| BtnNovoComando | THoverSpeedButton | ação | Novo Comando (Ctrl+N) | 0 | — | — | — |
| BtnAtualizarFilaComandos | THoverSpeedButton | ação | Atualizar (F5) | 1 | — | — | — |
| BtnExcluirListaComandos | THoverSpeedButton | ação | Excluir Item (Ctrl+Del) | 2 | — | — | — |
| TabEnviarInfo | TTabSheet | contêiner | Enviar Informações | — | — | — | — |
| Panel12 | TPanel | contêiner | — | 0 | — | — | — |
| BtnVoltar | THoverSpeedButton | ação | Voltar (Ctrl+D) | 0 | — | — | — |
| BtnEnviarSelecionado | THoverSpeedButton | ação | Enviar (Ctrl+S) | 1 | — | — | — |
| rdgEnviar | TRadioGroup | seleção | Adicionar à fila: | 1 | — | — | — |
| pnlSelecaoColetor | TPanel | contêiner | Selecione um coletor... | 2 | — | — | — |
| GbFiltrar | TGroupBox | contêiner | Filtrar: | 3 | — | — | — |
| PgFiltrar | TPageControl | contêiner | — | 0 | — | — | — |
| TabFiltro | TTabSheet | contêiner | TabFiltro | — | — | — | — |
| dbgPessoasFiltro | TDBGrid | grade | — | 0 | — | — | Visible=True |
| pnFiltro | TPanel | contêiner | — | 1 | — | — | — |
| TabPessoa | TTabSheet | contêiner | TabPessoa | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| LblPessoa | TLabel | rótulo | Pessoa: | — | — | — | — |
| PnlPessoas | TPanel | contêiner | Acesso | 0 | — | — | — |
| ShpPessoas | TShape | outro | — | — | — | — | — |
| MlPessoas | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lbPessoas | TListBox | seleção | — | 1 | — | — | — |
| btnExcluiFiltro | THoverSpeedButton | ação | Shift+Del | 2 | — | — | — |
| cbTipoFiltro | TComboBox | seleção | — | 1 | — | — | — |
| pnlLeft | TPanel | contêiner | — | 1 | — | — | — |
| dbgColetores | TDBGrid | grade | — | 0 | — | — | Visible=True |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActEnviarDataHora | TAction | ação | Enviar | — | — | — | — |
| ActAtualizarFilaComandos | TAction | ação | Atualizar (F5) | — | — | — | — |
| ActFechar | TAction | ação | Fechar (Alt+F4) | — | — | — | — |
| ActEnviarConfig | TAction | ação | Enviar | — | — | — | — |
| ActStatusColetor | TAction | ação | Solicitar Status | — | — | — | — |
| ActStatusComunicacao | TAction | ação | Solicitar | — | — | — | — |
| ActExcluirListaComandos | TAction | ação | Excluir Item (Ctrl+Del) | — | — | — | — |
| ActEnviarSelecionado | TAction | ação | Enviar (Ctrl+S) | — | — | — | — |
| ActNovoComando | TAction | ação | Novo Comando (Ctrl+N) | — | — | — | — |
| ActVoltar | TAction | ação | Voltar (Ctrl+D) | — | — | — | — |
| ActEnviarUsuarios | TAction | ação | ActEnviarUsuarios | — | — | — | — |
| ActExcluirUsuarios | TAction | ação | ActExcluirUsuarios | — | — | — | — |
| ActBuscarPessoas | TAction | ação | F4 | — | — | — | — |
| ActRemoverPessoas | TAction | ação | Shift+Del | — | — | — | — |
| ActLimpezaTotal | TAction | ação | ActLimpezaTotal | — | — | — | — |
| DsFilaComandos | TDataSource | outro | — | — | — | — | — |
| CdsFilaComandos | TClientDataSet | outro | — | — | — | — | — |
| CdsFilaComandosid | TIntegerField | outro | — | — | — | — | — |
| CdsFilaComandosDataHora | TDateTimeField | outro | — | — | — | — | — |
| CdsFilaComandosIdColetor | TIntegerField | outro | — | — | — | — | — |
| CdsFilaComandosComando | TIntegerField | outro | — | — | — | — | — |
| CdsFilaComandosOrdem | TIntegerField | outro | — | — | — | — | — |
| CdsFilaComandosPrioridade | TIntegerField | outro | — | — | — | — | — |
| CdsFilaComandosNome | TStringField | outro | — | — | — | — | — |
| CdsFilaComandosColetorNome | TStringField | outro | — | — | — | — | — |
| CdsFilaComandosTipo | TIntegerField | outro | — | — | — | — | — |
| CdsFilaComandosIdFiltro | TIntegerField | outro | — | — | — | — | — |
| CdsFilaComandosPessoas | TWideStringField | outro | — | — | — | — | — |
| CdsStatusColetor | TClientDataSet | outro | — | — | — | — | — |
| CdsStatusColetorId | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorDataHora | TDateTimeField | outro | — | — | — | — | — |
| CdsStatusColetorColetor | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorNomeColetor | TStringField | outro | — | — | — | — | — |
| CdsStatusColetorTipoColetor | TStringField | outro | — | — | — | — | — |
| CdsStatusColetorNrTerminal | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorIP | TStringField | outro | — | — | — | — | — |
| CdsStatusColetorQuantidade_Registros | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorTamanho_Buffer_Registros | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorQuantidade_Cartoes_Lista | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorTamanho_Lista_Cartoes | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorQuantidade_Digitos | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorDataHoraColetor | TDateTimeField | outro | — | — | — | — | — |
| CdsStatusColetorNumero_Tipo_Acionamento | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorTipo_Acionamento | TStringField | outro | — | — | — | — | — |
| CdsStatusColetorNumero_Checagem | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorChecagem | TStringField | outro | — | — | — | — | — |
| CdsStatusColetorNumero_Sentido_Giro | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorSentido_Giro | TStringField | outro | — | — | — | — | — |
| CdsStatusColetorNumero_Ativacao | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorAtivacao | TStringField | outro | — | — | — | — | — |
| CdsStatusColetorNumero_Acesso_Controlado | TIntegerField | outro | — | — | — | — | — |
| CdsStatusColetorAcesso_Controlado | TStringField | outro | — | — | — | — | — |
| CdsStatusColetorVersao_Firmware | TStringField | outro | — | — | — | — | — |
| DsStatusColetor | TDataSource | outro | — | — | — | — | — |
| Timer1 | TTimer | outro | — | — | — | — | — |
| ImageList1 | TImageList | outro | — | — | — | — | — |
| CdsColetoresStatusConexao | TClientDataSet | outro | — | — | — | — | — |
| CdsColetoresStatusConexaoStatus | TStringField | outro | — | — | — | — | — |
| CdsColetoresStatusConexaoIdColetor | TIntegerField | outro | — | — | — | — | Visible=False |
| CdsColetoresStatusConexaoNome | TStringField | outro | — | — | — | — | — |
| CdsColetoresStatusConexaoIP | TStringField | outro | — | — | — | — | — |
| CdsColetoresStatusConexaoSelecao | TBooleanField | outro | — | — | — | — | — |
| DsColetoresStatusConexao | TDataSource | outro | — | — | — | — | — |
| dsPessoasFiltro | TDataSource | outro | — | — | — | — | — |
| cdsPessoasFiltro | TClientDataSet | outro | — | — | — | — | — |
| cdsPessoasFiltroid | TIntegerField | outro | — | — | — | — | — |
| cdsPessoasFiltronome | TStringField | outro | — | — | — | — | — |
| cdsPessoasFiltroColetorNome | TStringField | outro | — | — | — | — | — |
| cdsPessoasFiltroFiltroNome | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 260 | `TColetoresStatusConexaoController.Create`, `FColetoresStatusConexaoController.SetConexao`, `TColetaStatusController.Create`, `FColetaStatusController.SetConexao`, `TFilaComandosController.Create`, `FFilaComandosController.SetConexao`, `TFilaComandosCrachasController.Create`, `FFilaComandosCrachasController.SetConexao` |
| `ActExcluirUsuariosExecute` | 615 | — |
| `ActExcluirListaComandosExecute` | 728 | `FFilaComandosCrachasController.ExcluirTudo`, `FFilaComandosController.Excluir` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 344: `Selecione uma opção de envio antes de selecionar as antenas.`
- Linha 354: `Erro: Comando não encontrado`
- Linha 397: `Erro ao interagir com a antena: `
- Linha 573: `Selecione um item para excluí-lo.`
- Linha 704: `Selecione um item para excluí-lo.`
- Linha 885: `Erro ao gravar fila para a antena: `
- Linha 897: `Comandos processados e enviados à fila.`
- Linha 1072: `Selecione uma opção para enviar!`
- Linha 1303: `Selecione uma opção para enviar!`
- Linha 1311: `Selecione pelo menos uma antena na lista!`
- Linha 1322: `É necessário selecionar o tipo de filtragem`
- Linha 1336: `Comando não reconhecido: `

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
