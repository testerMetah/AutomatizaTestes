# Refeitorio: TFrmCadCardapio

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Refeitório > Cardapios....

- DFM: `Acesso/uFrmCadCardapio.dfm`
- PAS: `Acesso/uFrmCadCardapio.pas`
- Handler de abertura: `acRefCardapiosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadCardapio | TFrmCadCardapio | outro | Cadastro de Cardápios | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| btnImportar | THoverSpeedButton | ação | Importar Cardápios (Ctrl + F5) | 3 | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| Label2 | TLabel | rótulo | Situação: | — | — | — | — |
| Label32 | TLabel | rótulo | Refeitórios: | — | — | — | — |
| mlRefeitorio | TMetaEquipLocalizar | outro | F4 | — | — | — | Visible=False |
| lblRefeitorio | TLabel | rótulo | lblRefeitorio | — | — | — | Visible=False |
| pnlFundoCadastro | TPanel | contêiner | — | 6 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | Text=EdNome |
| cmbStatus | TComboBox | seleção | — | 1 | — | — | Text=Ativo, ItemIndex=0 |
| GrbValoresCardapios | TGroupBox | contêiner | Valores do Cardápio | 3 | — | — | — |
| Label4 | TLabel | rótulo | Reserva sem Consumo: R$ | — | — | — | — |
| Label5 | TLabel | rótulo | Consumo sem Reserva: R$ | — | — | — | — |
| Label6 | TLabel | rótulo | Reserva com consumo:  R$ | — | — | — | — |
| lblTempoDesc | TLabel | rótulo | Minutos a Desconsiderar: | — | — | — | Visible=False |
| EdReservaSemConsumo | TEdit | campo de texto/data | — | 1 | — | — | Text=EdReservaSemConsumo |
| EdConsumoSemReserva | TEdit | campo de texto/data | — | 2 | — | — | Text=EdConsumoSemReserva |
| EdReservaComConsumo | TEdit | campo de texto/data | — | 0 | — | — | Text=EdReservaComConsumo |
| pnlDesconsiderarDup | TPanel | contêiner | — | 3 | — | — | — |
| lblDesconsiderarDup | TLabel | rótulo | Desconsiderar Reservas Duplicadas | — | — | — | — |
| chkDesconsiderarDup | TCheckBox | seleção | — | 0 | — | — | — |
| EdTempoDesc | TEdit | campo de texto/data | — | 4 | — | 3 | Text=0, Visible=False |
| EdRefeitorio | TEdit | campo de texto/data | — | 2 | — | — | Text=EdRefeitorio, Visible=False |
| GrbHorarioConsumo | TGroupBox | contêiner | Horário Para Consumir | 5 | — | — | — |
| Label7 | TLabel | rótulo | Até | — | — | — | — |
| MskHoraIniC | TMaskEdit | campo de texto/data | — | 0 | !99:99;1;  | 5 | Text=  :   |
| MskHoraFimC | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| GrbHorarioReserva | TGroupBox | contêiner | Horário Para Reservar | 4 | — | — | — |
| Label3 | TLabel | rótulo | Até | — | — | — | — |
| MskHoraFimR | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| MskHoraIniR | TMaskEdit | campo de texto/data | — | 0 | !99:99;1;  | 5 | Text=  :   |
| pnlGrid | TPanel | contêiner | — | 7 | — | — | — |
| GridItens | TDBGrid | grade | — | 0 | — | — | Visible=True |
| btnInformacao | THoverSpeedButton | ação |  | 8 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActImportar | TAction | ação | Importar Cardápios (Ctrl + F5) | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActInformacao | TAction | ação | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsCardapios | TDataSource | outro | — | — | — | — | — |
| CdsCardapios | TClientDataSet | outro | — | — | — | — | — |
| CdsCardapiosId | TIntegerField | outro | — | — | — | — | — |
| CdsCardapiosNome | TStringField | outro | — | — | — | — | — |
| CdsCardapiosSituacao | TIntegerField | outro | — | — | — | — | — |
| dsConsulta | TDataSource | outro | — | — | — | — | — |
| CdsConsulta | TClientDataSet | outro | — | — | — | — | — |
| CdsConsultaSELECIONADO | TIntegerField | outro | — | — | — | — | — |
| CdsConsultaID | TStringField | outro | — | — | — | — | — |
| CdsConsultaNOME | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActCancelarExecute` | 131 | — |
| `ActExcluirExecute` | 137 | `FCardRefController.ExcluirPorCardapio`, `FCardapiosController.Excluir` |
| `ActExibirTudoExecute` | 168 | `FCardapiosController.GetCardapiosTodos` |
| `ActIncluirExecute` | 279 | — |
| `ActIrExecute` | 293 | `FCardapiosController.GetCardapiosPorDescricao` |
| `ActSalvarExecute` | 331 | — |
| `FormCreate` | 526 | `TCardapiosController.Create`, `FCardapiosController.SetConexao`, `TRefeitoriosController.Create`, `FRefeitoriosController.SetConexao`, `TCardapiosRefeitoriosController.Create`, `FCardRefController.SetConexao` |
| `GravaCampos` | 550 | `FCardapiosController.Inserir`, `FCardapiosController.Atualizar` |
| `GravarRelacaoRefeitorios` | 593 | `FCardRefController.Inserir`, `FCardRefController.Excluir` |
| `ValidarCampos` | 713 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 146: `Excluir o registro?`
- Linha 240: `Erro ao gravar informações no Banco de Dados: `
- Linha 244: `Importação realizada com sucesso`
- Linha 288: `Em caso de consumo sem reserva, caso haja horários de consumo `
- Linha 447: `Refeitório não cadastrado`
- Linha 464: `Valor inválido.`
- Linha 483: `Valor inválido.`
- Linha 497: `Valor inválido.`
- Linha 718: `O Nome do cardápio deve ser informado.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
