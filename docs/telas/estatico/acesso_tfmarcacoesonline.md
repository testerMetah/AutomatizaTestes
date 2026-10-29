# Acesso: TFMarcacoesOnline

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Consultas > Marcações Online....

- DFM: `Acesso/UMarcacoesOnline.dfm`
- PAS: `Acesso/UMarcacoesOnline.pas`
- Handler de abertura: `acConsMarcacoesOnlineExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FMarcacoesOnline | TFMarcacoesOnline | outro | Consulta de Marcações Online | — | — | — | Visible=True |
| MetaEquipLocalizar1 | TMetaEquipLocalizar | outro | — | — | — | — | — |
| GridConsulta | TDBGrid | grade | — | 0 | — | — | Visible=True |
| PnlFundo | TPanel | contêiner | — | 1 | — | — | — |
| BtnContarRegistros | THoverSpeedButton | ação | Contar Registros (F5) | 0 | — | — | — |
| BtnConsultar | THoverSpeedButton | ação | Consultar (F6) | 1 | — | — | — |
| Panel3 | TPanel | contêiner | — | 2 | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | 0 | — | — | — |
| TbsPeriodo | TTabSheet | contêiner | Período (Ctrl+A) | — | — | — | — |
| LblDe | TLabel | rótulo | De | — | — | — | — |
| LblAte | TLabel | rótulo | Até | — | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| DtTermino | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| TmTermino | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| TbsCracha | TTabSheet | contêiner | Crachá (Ctrl+B) | — | — | — | — |
| LblCracha | TLabel | rótulo | Número de Crachá | — | — | — | — |
| ednrocracha | TEdit | campo de texto/data | — | 0 | — | — | — |
| TbsColetorFuncao | TTabSheet | contêiner | Coletor/Função (Ctrl+D) | — | — | — | — |
| lblCampoColetor | TLabel | rótulo | Coletor | — | — | — | — |
| LblFuncao | TLabel | rótulo | Função | — | — | — | — |
| mlColetor | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblColetor | TLabel | rótulo | lblColetor | — | — | — | — |
| edColetor | TEdit | campo de texto/data | — | 0 | — | — | — |
| EdFuncao | TEdit | campo de texto/data | — | 1 | — | — | — |
| TbsSentido | TTabSheet | contêiner | Sentido (Ctrl+E) | — | — | — | — |
| LblSentido | TLabel | rótulo | Sentido | — | — | — | — |
| CmbSentido | TComboBox | seleção | — | 0 | — | — | Text=Todos, ItemIndex=3 |
| TbsTipoColeta | TTabSheet | contêiner | Tipo de Coleta (Ctrl+F) | — | — | — | — |
| LblTipoColeta | TLabel | rótulo | Tipo de Coleta | — | — | — | — |
| CmbTipoColeta | TComboBox | seleção | — | 0 | — | — | Text=Todas, ItemIndex=2 |
| TbsSituacao | TTabSheet | contêiner | Situação (Ctrl+G) | — | — | — | — |
| LblSituacao | TLabel | rótulo | Situação | — | — | — | — |
| CmbSituacao | TComboBox | seleção | — | 0 | — | — | Text=Ambos, ItemIndex=2 |
| TbsPessoa | TTabSheet | contêiner | Pessoa (Ctrl+H) | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | F4 | — | — | — | Visible=False |
| lblPessoa | TLabel | rótulo | lblPessoa | — | — | — | Visible=False |
| EdPessoa | TEdit | campo de texto/data | — | 0 | — | — | Text=EdPessoa, Visible=False |
| cmbTipoPessoa | TComboBox | seleção | — | 1 | — | — | Text=Todos, ItemIndex=0 |
| BtnLimparFiltros | THoverSpeedButton | ação | Limpar Filtros (Ctrl+X) | 1 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActFechar | TAction | ação | Fechar (Alt+F4) | — | — | — | — |
| ActLimparFiltros | TAction | ação | Limpar Filtros (Ctrl+X) | — | — | — | — |
| ActLocalizarPessoa | TAction | ação | ActLocalizarPessoa | — | — | — | — |
| ActConsultar | TAction | ação | Consultar (F6) | — | — | — | — |
| ActPeriodo | TAction | ação | ActPeriodo | — | — | — | — |
| ActCracha | TAction | ação | ActCracha | — | — | — | — |
| ActColetorFuncao | TAction | ação | ActColetorFuncao | — | — | — | — |
| ActSentido | TAction | ação | ActSentido | — | — | — | — |
| ActTipoColeta | TAction | ação | ActTipoColeta | — | — | — | — |
| ActSituacao | TAction | ação | ActSituacao | — | — | — | — |
| ActPessoa | TAction | ação | ActPessoa | — | — | — | — |
| ActContarRegistros | TAction | ação | Contar Registros (F5) | — | — | — | — |
| ActBuscarFiltros | TAction | ação | F4 | — | — | — | — |
| CdsMarcacoesOnline | TClientDataSet | outro | — | — | — | — | — |
| CdsMarcacoesOnlineDATAHORA | TDateTimeField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineIDCRACHA | TStringField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineFUNCAO | TIntegerField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineIDCOLETOR | TIntegerField | outro | — | — | — | — | — |
| CdsMarcacoesOnlinePESSOA | TIntegerField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineSENTIDO | TIntegerField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineTIPOCOLETA | TIntegerField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineSITUACAO | TIntegerField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineMSG | TStringField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineNOME | TStringField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineNomeColetor | TStringField | outro | — | — | — | — | — |
| CdsMarcacoesOnlineTipoPessoa | TStringField | outro | — | — | — | — | — |
| DSMarcacoesOnline | TDataSource | outro | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActConsultarExecute` | 148 | `FMarcacoesController.GetMarcacoes` |
| `BtnConsultarClick` | 262 | `FMarcacoesController.DataHoraInicio`, `FMarcacoesController.DataHoraTermino`, `FMarcacoesController.NroCracha`, `FMarcacoesController.Coletor`, `FMarcacoesController.Funcao`, `FMarcacoesController.Sentido`, `FMarcacoesController.TipoColeta`, `FMarcacoesController.Situacao` |
| `FormCreate` | 572 | `TMarcacoesOnLineController.Create`, `FMarcacoesController.SetConexao` |
| `ValidarFiltros` | 705 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 213: `Possui `
- Linha 409: `Data Inválida!`
- Linha 432: `Coletor não cadastrado`
- Linha 700: `Hora Inválida!`
- Linha 709: `Data de Início deve ser informada.`
- Linha 716: `A hora de Início deve ser informada.`
- Linha 723: `Data de Término deve ser informada.`
- Linha 730: `A hora de Término deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
