# Acesso: TFrmAcessosAutorizados

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Acesso > Autorização de Acessos....

- DFM: `Acesso/UFrmAcessosAutorizados.dfm`
- PAS: `Acesso/UFrmAcessosAutorizados.pas`
- Handler de abertura: `acAceAcessosAutorizadosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmAcessosAutorizados | TFrmAcessosAutorizados | outro | Autorização de Acessos | — | — | — | Visible=True |
| Pagina | TPageControl | contêiner | — | 0 | — | — | — |
| Grid | TTabSheet | contêiner | Grid | — | — | — | — |
| GridConsulta | TDBGrid | grade | — | 0 | — | — | Visible=True |
| Panel1 | TPanel | contêiner | — | 1 | — | — | — |
| btnexcluir | THoverSpeedButton | ação | Excluir (Ctrl+Del) | 0 | — | — | — |
| btnConfirmar | THoverSpeedButton | ação | Autorizar (Ctrl+E) | 1 | — | — | Visible=False, Enabled=False |
| HoverSpeedButton5 | THoverSpeedButton | ação | Atualizar (Ctrl+W) | 2 | — | — | — |
| Panel3 | TPanel | contêiner | — | 2 | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | 0 | — | — | — |
| TbsPeriodo | TTabSheet | contêiner | Período (Ctrl+A) | — | — | — | — |
| Label1 | TLabel | rótulo | De | — | — | — | — |
| Label2 | TLabel | rótulo | Até | — | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| DtTermino | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| TmTermino | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| HoverSpeedButton1 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 4 | — | — | — |
| TbsPessoa | TTabSheet | contêiner | Pessoa (Ctrl+P) | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | 0 | — | — | — |
| HoverSpeedButton4 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| TbsCracha | TTabSheet | contêiner | Crachá (Ctrl+B) | — | — | — | — |
| HoverSpeedButton2 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 0 | — | — | — |
| edNroCracha | TEdit | campo de texto/data | — | 1 | — | — | — |
| TbsSituacao | TTabSheet | contêiner | Situação (Ctrl+G) | — | — | — | Enabled=False |
| Label8 | TLabel | rótulo | Situação | — | — | — | — |
| CmbSituacao | TComboBox | seleção | — | 0 | — | — | — |
| HoverSpeedButton3 | THoverSpeedButton | ação | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| BtnExibirTudo | TBitBtn | outro | Exibir tudo (Ctrl+T) | 1 | — | — | — |
| Cadastro | TTabSheet | contêiner | Cadastro | — | — | — | — |
| Label3 | TLabel | rótulo | Início: | — | — | — | — |
| Label4 | TLabel | rótulo | Fim: | — | — | — | — |
| Label6 | TLabel | rótulo | Pessoa: | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| lblPessoa | TLabel | rótulo | lblPessoa | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| MskDataIni | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MskHoraIni | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| MskDataFim | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MskHoraFim | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| EdPessoa | TEdit | campo de texto/data | — | 4 | — | — | — |
| PnlFundoCadastro | TPanel | contêiner | — | 5 | — | — | — |
| BtnSalvar | THoverSpeedButton | ação | Salvar (Ctrl + S) | 0 | — | — | — |
| BtnCarncelar | THoverSpeedButton | ação | Cancelar (Ctrl+D) | 1 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActFechar | TAction | ação | Fechar (Alt+F4) | — | — | — | — |
| ActExibirTudo | TAction | ação | Exibir tudo (Ctrl+T) | — | — | — | — |
| ActAutorizar | TAction | ação | Autorizar (Ctrl+E) | — | — | — | Visible=False, Enabled=False |
| ActSalvar | TAction | ação | Salvar (Ctrl + S) | — | — | — | — |
| ActCancelar | TAction | ação | Cancelar (Ctrl+D) | — | — | — | — |
| ActAdicionar | TAction | ação | Adicionar | — | — | — | Visible=False, Enabled=False |
| ActExcluir | TAction | ação | Excluir (Ctrl+Del) | — | — | — | — |
| ActtbsPeriodo | TAction | ação | Período (Ctrl+A) | — | — | — | — |
| ActtbsCracha | TAction | ação | Crachá (Ctrl+B) | — | — | — | — |
| ActtbsSituacao | TAction | ação | Situação (Ctrl+G) | — | — | — | Visible=False, Enabled=False |
| ActtbsPessoa | TAction | ação | Pessoa (Ctrl+ P) | — | — | — | — |
| ActAtualizar | TAction | ação | Atualizar (Ctrl+W) | — | — | — | — |
| dsAcessosAutorizados | TDataSource | outro | — | — | — | — | — |
| CdsAcessosAutorizados | TClientDataSet | outro | — | — | — | — | — |
| CdsAcessosAutorizadosId | TIntegerField | outro | — | — | — | — | — |
| CdsAcessosAutorizadosDataHoraInicio | TDateTimeField | outro | — | — | — | — | — |
| CdsAcessosAutorizadosDataHoraFim | TDateTimeField | outro | — | — | — | — | — |
| CdsAcessosAutorizadosAutorizado | TIntegerField | outro | — | — | — | — | — |
| CdsAcessosAutorizadosIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsAcessosAutorizadosPessoa | TStringField | outro | — | — | — | — | — |
| CdsAcessosAutorizadosIdFreq | TStringField | outro | — | — | — | — | — |
| CdsAcessosAutorizadosNroCracha | TStringField | outro | — | — | — | — | — |
| CdsAcessosAutorizadosImportado | TStringField | outro | — | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActCancelarExecute` | 393 | — |
| `ActExcluirExecute` | 431 | `FAceAutorizaController.ExcluirAPI` |
| `ActExibirTudoExecute` | 452 | `FAceAutorizaController.GetTodos` |
| `ActSalvarExecute` | 485 | `TConexaoController.Create`, `FConexaoController.SetConexao`, `FConexaoController.GetConexao`, `FAceAutorizaController.ImportarAcessosAutorizados`, `FAceAutorizaController.GetTodos` |
| `FormCreate` | 622 | `TAceAutorizaController.Create`, `FAceAutorizaController.SetConexao`, `FAceAutorizaController.GetTodos` |
| `GravarCampos` | 847 | `FAceAutorizaController.Inserir`, `FAceAutorizaController.GetNome` |
| `ValidarCampos` | 989 | — |
| `ValidarConsultas` | 1088 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 308: `Esta pessoa não possui nenhum crachá.`
- Linha 435: `Deseja excluir o registro?`
- Linha 442: `Erro ao excluir!`
- Linha 491: `Problemas com a gravação no Banco de Dados!`
- Linha 496: `Problemas com a gravação no Banco de Dados!`
- Linha 1015: `Data de início inválida`
- Linha 1024: `A data de início deve ser maior ou igual a data de hoje`
- Linha 1044: `Data de encerramento inválida`
- Linha 1064: `Código de pessoa inválido`
- Linha 1072: `Código de pessoa inválido`
- Linha 1081: `A pessoa deve ser informada`
- Linha 1116: `Data de início inválida`
- Linha 1137: `Data de encerramento inválida`
- Linha 1155: `O código do crachá não pode ter valor negativo`
- Linha 1172: `É necessário preencher o código do crachá`
- Linha 1180: `Código de crachá inválido`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
