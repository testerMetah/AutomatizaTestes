# Acesso: TFExportadorMetadados

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ferramentas > Exportador Metadados....

- DFM: `Acesso/UExportadorMetadados.dfm`
- PAS: `Acesso/UExportadorMetadados.pas`
- Handler de abertura: `acFerExportadorMetadadosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FExportadorMetadados | TFExportadorMetadados | outro | Exportador Metadados | — | — | — | Visible=True |
| PnlForm | TPanel | contêiner | — | 0 | — | — | — |
| Panel1 | TPanel | contêiner | — | 0 | — | — | — |
| GroupBox2 | TGroupBox | contêiner | — | 0 | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| Label8 | TLabel | rótulo | Layout: | — | — | — | — |
| Image10 | TImage | outro | — | — | — | — | — |
| Label3 | TLabel | rótulo | Diretório do Arquivo: | — | — | — | — |
| Label1 | TLabel | rótulo | Tipo de Função: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Label4 | TLabel | rótulo | Nome do Arquivo: | — | — | — | — |
| EdDiretorio | TEdit | campo de texto/data | — | 0 | — | — | — |
| GrdLayout | TStringGrid | grade | — | 1 | — | — | — |
| CmbLayout | TComboBox | seleção | — | 2 | — | — | — |
| BtnEditaLayout | THoverSpeedButton | ação | Editar Layout (Ctrl+E) | 3 | — | — | — |
| BtnLayoutNovo | THoverSpeedButton | ação | Novo Layout (Ctrl+N) | 4 | — | — | — |
| BtnLayoutExcluir | THoverSpeedButton | ação | Excluir Layout (Ctrl+Del) | 5 | — | — | Visible=False |
| btnAdicionarDiretorio | THoverSpeedButton | ação |  | 6 | — | — | — |
| clbTipoFuncao | TCheckListBox | seleção | — | 7 | — | — | — |
| edNomeArquivo | TEdit | campo de texto/data | — | 8 | — | — | — |
| chbUtilizarTipoCracha | TCheckBox | seleção | Utilizar tipo crachá específico: | 9 | — | — | — |
| CmbTipoCracha | TComboBox | seleção | — | 10 | — | — | Text=Fixo, ItemIndex=0, Enabled=False |
| cbMinutos | TCheckBox | seleção | Desconsiderar no Intervalo de (Minutos): | 11 | — | — | — |
| EdMinutos | TEdit | campo de texto/data | — | 12 | — | — | Text=0, Enabled=False |
| Panel2 | TPanel | contêiner | — | 1 | — | — | — |
| BtnExportar | THoverSpeedButton | ação | Exportar (Ctrl+S) | 0 | — | — | — |
| Panel3 | TPanel | contêiner | — | 2 | — | — | — |
| GroupBox1 | TGroupBox | contêiner |            Período das Marcações | 0 | — | — | — |
| Image8 | TImage | outro | — | — | — | — | — |
| PnlCamposPeriodo | TPanel | contêiner | — | 0 | — | — | — |
| Label2 | TLabel | rótulo | Até | — | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| DtTermino | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| TmTermino | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActNovoLayout | TAction | ação | Novo Layout (Ctrl+N) | — | — | — | — |
| ActEditarLayout | TAction | ação | Editar Layout (Ctrl+E) | — | — | — | — |
| ActExcluirLayout | TAction | ação | Excluir Layout (Ctrl+Del) | — | — | — | — |
| ActExportar | TAction | ação | Exportar (Ctrl+S) | — | — | — | — |
| fodArquivo | TFileOpenDialog | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 1039 | `TConexaoController.Create`, `FConexaoClienteController.SetConexao` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 149: `Selecione o layout a ser alterado.`
- Linha 198: `Diretório deve ser preenchido.`
- Linha 205: `Diretório inexistente.`
- Linha 212: `Data de Início deve ser informada.`
- Linha 219: `A hora de Início deve ser informada.`
- Linha 226: `Data de Término deve ser informada.`
- Linha 233: `A hora de Término deve ser informada.`
- Linha 240: `Selecione um Layout.`
- Linha 255: `Selecione pelo menos um Tipo de Função.`
- Linha 427: `Exportação concluída para função: `
- Linha 434: `Exportação concluída para `
- Linha 551: `Data Inválida!`
- Linha 561: `Data Inválida!`
- Linha 741: `Diretório deve ser preenchido.`
- Linha 748: `Diretório inexistente.`
- Linha 755: `Data de Início deve ser informada.`
- Linha 762: `A hora de Início deve ser informada.`
- Linha 769: `Data de Término deve ser informada.`
- Linha 776: `A hora de Término deve ser informada.`
- Linha 783: `Selecione um Layout.`
- Linha 798: `Selecione pelo menos um Tipo de Função.`
- Linha 806: `Selecione um Tipo de Crachá.`
- Linha 1003: `Exportação concluída para função: `
- Linha 1011: `Exportação concluída para `
- Linha 1070: `Hora Inválida!`
- Linha 1080: `Hora Inválida!`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
