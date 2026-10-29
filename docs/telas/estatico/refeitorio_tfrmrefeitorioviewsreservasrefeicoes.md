# Refeitorio: TFrmRefeitorioViewsReservasRefeicoes

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Reservas > Refeições.

- DFM: `Refeitorio/Views/Acessus.Refeitorio.Views.ReservasRefeicoes.dfm`
- PAS: `Refeitorio/Views/Acessus.Refeitorio.Views.ReservasRefeicoes.pas`
- Handler de abertura: `acResRefeicoesExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmRefeitorioViewsReservasRefeicoes | TFrmRefeitorioViewsReservasRefeicoes | outro | Liberação de Reserva de Refeições | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet1 | TTabSheet | contêiner | Período (Ctrl+A) | — | — | — | — |
| Label2 | TLabel | rótulo | Até | — | — | — | — |
| cmbTipoPeriodo | TComboBox | seleção | — | 0 | — | — | Text=Início, ItemIndex=1 |
| dtInicio | TMaskEdit | campo de texto/data | — | 1 | !99/99/9999;1;  | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 2 | !99:99;1;  | 5 | Text=  :   |
| DtTermino | TMaskEdit | campo de texto/data | — | 3 | !99/99/9999;1;  | 10 | Text=  /  /     |
| TmTermino | TMaskEdit | campo de texto/data | — | 4 | !99:99;1;  | 5 | Text=  :   |
| TabSheet5 | TTabSheet | contêiner | Crachá (Ctrl+B) | — | — | — | — |
| Label5 | TLabel | rótulo | Número de Crachá | — | — | — | — |
| ednrocracha | TEdit | campo de texto/data | — | 0 | — | — | — |
| TabSheet4 | TTabSheet | contêiner | Cardápio (Ctrl+Q) | — | — | — | — |
| lblBuscaCardapio | TLabel | rótulo | lblBuscaCardapio | — | — | — | — |
| mlBuscarCardapio | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblNomeBuscaCardapio | TLabel | rótulo | Cardápio | — | — | — | — |
| edBuscaCardapio | TEdit | campo de texto/data | — | 0 | — | — | Visible=False |
| pnlDelCardapio | TPanel | contêiner | — | 1 | — | — | — |
| shpDelCardapio | TShape | outro | — | — | — | — | — |
| spbDelCardapio | TSpeedButton | ação | — | — | — | — | — |
| TabSheet6 | TTabSheet | contêiner | Tipo de Pessoa (Ctrl+G) | — | — | — | — |
| lblTipoPesso | TLabel | rótulo | Tipo de Pessoa | — | — | — | — |
| cmbBuscaTipoPessoa | TComboBox | seleção | — | 0 | — | — | Text=Todos, ItemIndex=0 |
| TabSheet3 | TTabSheet | contêiner | Situação (Ctrl+F) | — | — | — | — |
| Label8 | TLabel | rótulo | Situação | — | — | — | — |
| CmbSituacao | TComboBox | seleção | — | 0 | — | — | Text=Aguard. Autorização, ItemIndex=1 |
| TabSheet2 | TTabSheet | contêiner | Pessoa (Ctrl+M) | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | Visible=False |
| pnlBuscar | TPanel | contêiner | Acesso | 1 | — | — | — |
| shpBuscar | TShape | outro | — | — | — | — | — |
| spbBuscar | TSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| spbConfirmar | THoverSpeedButton | ação | Confirmar (Ctrl+C) | 3 | — | — | — |
| bntImportar | THoverSpeedButton | ação | Importar Reservas (Ctrl+F5) | 4 | — | — | — |
| pnlTop | TPanel | contêiner | — | 3 | — | — | — |
| lblDesmarcarTodos | TLabel | rótulo | Desmarcar Todos | — | — | — | — |
| lblMarcarTodos | TLabel | rótulo | Marcar Todos | — | — | — | — |
| spbDesmarcarTodos | TSpeedButton | ação | — | — | — | — | — |
| spbMarcarTodos | TSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| pnlCamposPrincipal | TPanel | contêiner | — | 1 | — | — | — |
| pnlCampos | TPanel | contêiner | — | 0 | — | — | — |
| lblGestor | TLabel | rótulo | Gestor | — | — | — | — |
| lblNomeGestor | TLabel | rótulo | txt | — | — | — | — |
| lblCardapio | TLabel | rótulo | Cardápio | — | — | — | — |
| lblNomeCardapio | TLabel | rótulo | txt | — | — | — | — |
| lblNomePessoa | TLabel | rótulo | txt | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | — | — | — | — | — |
| mlGestor | TMetaEquipLocalizar | outro | — | — | — | — | — |
| imgPessoa | TImage | outro | — | — | — | — | — |
| imgGestor | TImage | outro | — | — | — | — | — |
| imgCardapio | TImage | outro | — | — | — | — | — |
| imgPeriodo | TImage | outro | — | — | — | — | — |
| lblPeriodoConsumo | TLabel | rótulo | Período de Consumo | — | — | — | — |
| lblAte | TLabel | rótulo | Até | — | — | — | — |
| mlCardapio | TMetaEquipLocalizar | outro | — | — | — | — | — |
| edGestor | TEdit | campo de texto/data | — | 0 | — | — | Visible=False |
| edCracha | TEdit | campo de texto/data | — | 1 | — | — | Visible=False |
| edCardapio | TEdit | campo de texto/data | — | 2 | — | — | Visible=False |
| edPessoa | TEdit | campo de texto/data | — | 3 | — | — | Visible=False |
| mskIni | TMaskEdit | campo de texto/data | — | 4 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| mskFim | TMaskEdit | campo de texto/data | — | 5 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| cmbTipoPessoa | TComboBox | seleção | — | 6 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| EscolhaCardapio | TTabSheet | contêiner | Escolha Cardápio | — | — | — | — |
| pnlEscolha | TPanel | contêiner | — | 0 | — | — | — |
| pnlEscolhaGrid | TPanel | contêiner | — | 0 | — | — | — |
| GridItens | TDBGrid | grade | — | 0 | — | — | Visible=True |
| pnlFundoEscolha | TPanel | contêiner | — | 1 | — | — | — |
| HoverSpeedButton1 | THoverSpeedButton | ação | Confirmar (Ctrl+Alt+C) | 0 | — | — | — |
| HoverSpeedButton2 | THoverSpeedButton | ação | Cancelar (Cmd+Alt+D) | 1 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActFechar | TAction | ação | — | — | — | — | — |
| ActExibirTudo | TAction | ação | — | — | — | — | — |
| ActAlterar | TAction | ação | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | — |
| ActIr | TAction | ação | — | — | — | — | — |
| ActLocalizarCodigo | TAction | ação | — | — | — | — | — |
| ActCancelar | TAction | ação | — | — | — | — | — |
| AcConfirmar | TAction | ação | Confirmar (Ctrl+C) | — | — | — | — |
| AcImportar | TAction | ação | Importar Reservas (Ctrl+F5) | — | — | — | — |
| AcConfirmarEscolha | TAction | ação | Confirmar (Ctrl+Alt+C) | — | — | — | — |
| ActCancelarEscolha | TAction | ação | Cancelar (Cmd+Alt+D) | — | — | — | — |
| ActMarcarTodos | TAction | ação | — | — | — | — | — |
| ActDesmarcarTodos | TAction | ação | — | — | — | — | — |
| ActEscolherCardapio | TAction | ação | ActEscolherCardapio | — | — | — | — |
| ActTSPeriodo | TAction | ação | Período (Ctrl+A) | — | — | — | — |
| ActTSCracha | TAction | ação | Crachá (Ctrl+B) | — | — | — | — |
| ActTSCardapio | TAction | ação | Cardápio (Ctrl+D) | — | — | — | — |
| ActTSTipoPessoa | TAction | ação | Tipo de Pessoa (Ctrl+G) | — | — | — | — |
| ActTSSituacao | TAction | ação | Situação (Ctrl+F) | — | — | — | — |
| ActTSPessoa | TAction | ação | Pessoa (Ctrl+M) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| dsConsulta | TDataSource | outro | — | — | — | — | — |
| CdsConsulta | TClientDataSet | outro | — | — | — | — | — |
| CdsConsultaSELECIONADO | TIntegerField | outro | — | — | — | — | — |
| CdsConsultaID | TStringField | outro | — | — | — | — | — |
| CdsConsultaNOME | TStringField | outro | — | — | — | — | — |
| CdsConsultaIniReserva | TTimeField | outro | — | — | — | — | — |
| CdsConsultaFimReserva | TTimeField | outro | — | — | — | — | — |
| CdsConsultaIniConsumo | TTimeField | outro | — | — | — | — | — |
| CdsConsultaFimConsumo | TTimeField | outro | — | — | — | — | — |
| CdsConsultaFaixaReserva | TStringField | outro | — | — | — | — | — |
| CdsConsultaFaixaConsumo | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoes | TClientDataSet | outro | — | — | — | — | — |
| CdsReservasRefeicoesID | TIntegerField | outro | — | — | — | — | — |
| CdsReservasRefeicoesIDGESTOR | TIntegerField | outro | — | — | — | — | — |
| CdsReservasRefeicoesIDUSUARIOLIBEROU | TIntegerField | outro | — | — | — | — | — |
| CdsReservasRefeicoesDATAHORALIBERACAO | TDateTimeField | outro | — | — | — | — | — |
| CdsReservasRefeicoesSITUACAO | TIntegerField | outro | — | — | — | — | — |
| CdsReservasRefeicoesCREDENCIAL | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesDATAHORA | TDateTimeField | outro | — | — | — | — | — |
| CdsReservasRefeicoesNOMEPESSOA | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesNOMEUSUARIOLIBEROU | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesNOMEGESTOR | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesLIBERAR | TBooleanField | outro | — | — | — | — | — |
| CdsReservasRefeicoesREFEICOES | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesIDPESSOA | TIntegerField | outro | — | — | — | — | — |
| CdsReservasRefeicoesdatahoraini | TDateTimeField | outro | — | — | — | — | — |
| CdsReservasRefeicoesdatahorafim | TDateTimeField | outro | — | — | — | — | — |
| CdsReservasRefeicoesIdFreq | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesViewIni | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesViewFim | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesViewDataLiberacao | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesViewDataHoraRegistro | TStringField | outro | — | — | — | — | — |
| CdsReservasRefeicoesNomeCardapio | TStringField | outro | — | — | — | — | — |
| dsReservasRefeicoes | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActCancelarEscolhaExecute` | 834 | — |
| `ActExcluirExecute` | 916 | `FReservasRefeicoesController.GetReservasRefeicoes`, `FReservasRefeicoesController.Excluir`, `FCrachaController.GetCrachasPorPessoa`, `FCrachaController.GetCrachasPorPreCadastro`, `FFaixaAceColController.ExcluirPorCrachaEDataHora` |
| `ActExibirTudoExecute` | 1040 | `FReservasRefeicoesController.GetReservasRefeicoesTodos` |
| `ActIrExecute` | 1054 | — |
| `FormCreate` | 1750 | `TReservasRefeicoesController.Create`, `FReservasRefeicoesController.SetConexao`, `TCrachaController.Create`, `FCrachaController.SetConexao`, `TFaixaAcessoColetoresController.Create`, `FFaixaAceColController.SetConexao`, `TParametrosSistemaController.Create`, `FParametrosController.SetConexao` |
| `GravaCampos` | 2122 | `TCardapiosController.Create`, `CardapiosController.SetConexao`, `CardapiosController.GetCardapio`, `FReservasRefeicoesController.Inserir`, `FReservasRefeicoesController.GetReservasRefeicoes`, `FReservasRefeicoesController.Atualizar` |
| `GravaSituacao` | 2242 | `TCrachaController.Create`, `FCrachaController.SetConexao`, `TPessoasController.Create`, `FPessoasController.SetConexao`, `TPreCadastroController.Create`, `FPreCadastroController.SetConexao`, `FReservasRefeicoesController.GetReservasRefeicoes`, `FPessoasController.GetPessoa` |
| `ValidarCampos` | 2894 | `TCardapiosController.Create`, `CardapiosController.SetConexao`, `CardapiosController.GetCardapio` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 383: `Atenção: Houve erros no processamento das programações de regras.`
- Linha 395: `Atenção: Erro ao reaplicar cortes de reservas ativas.`
- Linha 399: `Erro ao processar cortes de reservas: `
- Linha 404: `Geração de Acesso concluída com sucesso!`
- Linha 409: `Erro ao Gerar Acesso: `
- Linha 444: `Operação cancelada pelo usuário.`
- Linha 780: `É necessário selecionar um registro para poder alterá-lo.`
- Linha 791: `Não é possível alterar uma reserva que já foi liberada para consumo.`
- Linha 824: `Registro não encontrado.`
- Linha 930: `Excluir todos os registros selecionados?`
- Linha 933: `As reservas não poderão ser excluídas ou desautorizadas após o horário de início do consumo.`
- Linha 1250: `Refeitório não cadastrado.`
- Linha 1272: `Cardápio não cadastrado.`
- Linha 1293: `Gestor não cadastrado.`
- Linha 2482: `As reservas não poderão ser excluídas ou desautorizadas após o horário de início do consumo.`
- Linha 2620: `Não é possível alterar uma reserva que já foi liberada para consumo.`
- Linha 2906: `Não é possível alterar uma reserva que já foi liberada para consumo.`
- Linha 2913: `É necessário selecionar uma pessoa.`
- Linha 2920: `É necessário selecionar um cardápio.`
- Linha 2927: `"`
- Linha 2933: `"`
- Linha 2939: `A data de início não pode ser menor que a data atual.`
- Linha 2951: `Não foi possível encontrar o cardápio com ID: `
- Linha 2960: `Data/hora inicial inválida após combinação.`
- Linha 2966: `Data/hora final inválida após combinação.`
- Linha 2972: `A data/hora inicial não pode ser maior que a data/hora final.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
