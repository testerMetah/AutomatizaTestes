# Acesso: TFAcessoPorPessoa

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Consultas > Acesso por Pessoa....

- DFM: `Acesso/UAcessoPorPessoa.dfm`
- PAS: `Acesso/UAcessoPorPessoa.pas`
- Handler de abertura: `acConsPorPessoaExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FAcessoPorPessoa | TFAcessoPorPessoa | outro | Acesso por Pessoa | — | — | — | Visible=True |
| pnlTopo | TPanel | contêiner | — | 0 | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblPessoa | TLabel | rótulo | lblPessoa | — | — | — | — |
| Label3 | TLabel | rótulo | Crachá: | — | — | — | — |
| Label4 | TLabel | rótulo | Coletor: | — | — | — | — |
| lblPeriodoCalculado | TLabel | rótulo | lblPeriodoCalculado | — | — | — | — |
| Label5 | TLabel | rótulo | Período Calculado: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| EdPessoa | TEdit | campo de texto/data | — | 1 | — | — | Text=EdPessoa |
| CmbCracha | TComboBox | seleção | — | 3 | — | — | — |
| CmbTipoPessoa | TComboBox | seleção | — | 0 | — | — | Text=Pessoas, ItemIndex=0 |
| gbPeriodo | TGroupBox | contêiner |       Período | 4 | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| PnlPeriodo | TPanel | contêiner | — | 0 | — | — | — |
| Label2 | TLabel | rótulo | Até | — | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;_ | 5 | Text=  :   |
| DtEncerramento | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| tmTermino | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;_ | 5 | Text=  :   |
| CmbColetorFuncao | TComboBox | seleção | — | 2 | — | — | — |
| BtnBuscarNomePadrao | THoverSpeedButton | ação | Consultar (F5) | 5 | — | — | — |
| PnlDados | TPanel | contêiner | — | 1 | — | — | — |
| ScbAcessos | TScrollBox | outro | — | 2 | — | — | — |
| imgBloqueado | TImage | outro | — | — | — | — | Visible=False |
| imgLiberado | TImage | outro | — | — | — | — | Visible=False |
| StbDetalhes | TStatusBar | outro | — | — | — | — | — |
| CdsAcessos | TClientDataSet | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActConsultar | TAction | ação | Consultar (F5) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActConsultarExecute` | 103 | `TMarcacoesOnLineController.Create`, `TCrachaController.Create`, `TFaixaAcessoColetoresController.Create`, `TColetoresController.Create`, `TParametrosSistemaController.Create`, `marcacoesController.SetConexao`, `crachaController.SetConexao`, `coletoresController.SetConexao` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 163: `Selecione um crachá.`
- Linha 173: `Crachá inválido.`
- Linha 292: `Não existem dados calculados para esse crachá e coletor.`
- Linha 899: `Pessoa deve ser informada.`
- Linha 907: `Coletor/Função deve ser informado.`
- Linha 914: `A data de início deve ser informada.`
- Linha 921: `A hora de início deve ser informada.`
- Linha 928: `A data de encerramento deve ser informada.`
- Linha 935: `A hora de término deve ser informada.`
- Linha 942: `O crachá deve ser informado.`
- Linha 997: `Aluno não cadastrado`
- Linha 1022: `Pessoa não cadastrada`
- Linha 1047: `Pessoa não cadastrada`
- Linha 1075: `Pessoa não cadastrada`
- Linha 1101: `Pessoa não cadastrada`
- Linha 1240: `Aluno não possui crachá.`
- Linha 1259: `Responsavel não possui crachá.`
- Linha 1276: `Pessoa não possui crachá.`
- Linha 1294: `Pessoa não possui crachá.`
- Linha 1310: `Pré-Cadastro não possui crachá.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
