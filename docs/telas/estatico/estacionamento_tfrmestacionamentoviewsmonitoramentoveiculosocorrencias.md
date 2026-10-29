# Estacionamento: TFrmEstacionamentoViewsMonitoramentoVeiculosOcorrencias

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Monitoramento > Ocorrências do Veículos.

- DFM: `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.VeiculosOcorrencias.dfm`
- PAS: `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.VeiculosOcorrencias.pas`
- Handler de abertura: `actMonOcorrenciasExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmEstacionamentoViewsMonitoramentoVeiculosOcorrencias | TFrmEstacionamentoViewsMonitoramentoVeiculosOcorrencias | outro | Monitoramento \| Veículos Ocorrências | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | Nome Veículo (Ctrl+B) | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| LblCadVeiculo | TLabel | rótulo | Veículo: | — | — | — | — |
| mlVeiculo | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblVeiculo | TLabel | rótulo | lblVeiculo | — | — | — | — |
| LblObservacao | TLabel | rótulo | Observação: | — | — | — | — |
| LblCadOcorrencia | TLabel | rótulo | Ocorrência: | — | — | — | — |
| mlOcorrencia | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblOcorrencia | TLabel | rótulo | lblOcorrencia | — | — | — | — |
| LblDataHora | TLabel | rótulo | Data e hora: | — | — | — | — |
| ImgObservacao | TImage | outro | — | — | — | — | — |
| ImgDataHora | TImage | outro | — | — | — | — | — |
| ImgOcorrencia | TImage | outro | — | — | — | — | — |
| ImgVeiculo | TImage | outro | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | 5 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| EdObservacao | TMemo | outro | — | 2 | — | — | — |
| EdOcorrencia | TEdit | campo de texto/data | — | 1 | — | — | — |
| EdVeiculo | TEdit | campo de texto/data | — | 0 | — | — | — |
| EdData | TMaskEdit | campo de texto/data | — | 3 | !99/99/0000;1;_ | 10 | Text=  /  /     |
| EdHora | TMaskEdit | campo de texto/data | — | 4 | !90:00;1;_ | 5 | Text=  :   |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNomeVeiculo | TAction | ação | Nome Veículo (Ctrl+B) | — | — | — | — |
| CdsVeiculosOcorrencias | TClientDataSet | outro | — | — | — | — | — |
| CdsVeiculosOcorrenciasId | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosOcorrenciasIdVeiculo | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosOcorrenciasIdOcorrencia | TIntegerField | outro | — | — | — | — | — |
| CdsVeiculosOcorrenciasObservacao | TStringField | outro | — | — | — | — | — |
| CdsVeiculosOcorrenciasData | TDateField | outro | — | — | — | — | — |
| CdsVeiculosOcorrenciasHora | TTimeField | outro | — | — | — | — | — |
| CdsVeiculosOcorrenciasPlacaVeiculo | TStringField | outro | — | — | AAA\-AAAA;0;_ | — | — |
| CdsVeiculosOcorrenciasNomeVeiculo | TStringField | outro | — | — | — | — | — |
| CdsVeiculosOcorrenciasNomeOcorrencia | TStringField | outro | — | — | — | — | — |
| DsVeiculosOcorrencias | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExibirTudoExecute` | 131 | `FVeiculosOcorrenciasController.GetTodos` |
| `ActIncluirExecute` | 156 | — |
| `ActIrExecute` | 162 | `FVeiculosOcorrenciasController.GetPorNomeVeiculo` |
| `FormCreate` | 286 | `TVeiculosOcorrenciasController.Create`, `FVeiculosOcorrenciasController.SetConexao` |
| `GravaCampos` | 300 | `FVeiculosOcorrenciasController.Inserir`, `FVeiculosOcorrenciasController.Atualizar` |
| `ValidarCampos` | 343 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 118: `Excluir o registro?`
- Linha 124: `Problemas com a exclus�o no Banco de Dados!`
- Linha 238: `Veiculo n�o cadastrado`
- Linha 266: `Ocorr�ncia n�o cadastrada`
- Linha 348: `O ve�culo deve ser informado.`
- Linha 355: `A Ocorr�ncia deve ser informada.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
