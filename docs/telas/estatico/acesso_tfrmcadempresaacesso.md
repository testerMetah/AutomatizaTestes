# Acesso: TFrmCadEmpresaAcesso

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Pré-Cadastros > Empresas Acesso.

- DFM: `Acesso/UFrmCadEmpresaAcesso.dfm`
- PAS: `Acesso/UFrmCadEmpresaAcesso.pas`
- Handler de abertura: `ActEmpresasAcessoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadEmpresaAcesso | TFrmCadEmpresaAcesso | outro | Cadastros de Empresa de Acesso | — | — | — | — |
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
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| BtnVinculaPessoa | TSpeedButton | ação | Pessoas... | — | — | — | — |
| Image12 | TImage | outro | — | — | — | — | — |
| lblNome | TLabel | rótulo | Nome: | — | — | — | — |
| lblSentido | TLabel | rótulo | CPF/CNPJ: | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | 2 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| MskCNPJCPF | TEdit | campo de texto/data | — | 1 | — | 14 | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | Text=EdNome |
| pnlPessoas | TPanel | contêiner | — | 3 | — | — | — |
| GrdPessoas | TDBGrid | grade | — | 0 | — | — | Visible=True |
| EdBuscar | TEdit | campo de texto/data | — | 1 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| CDSEmpresaAcesso | TClientDataSet | outro | — | — | — | — | — |
| CDSEmpresaAcessoNome | TStringField | outro | — | — | — | — | — |
| CDSEmpresaAcessoId | TIntegerField | outro | — | — | — | — | — |
| DSEmpresaAcesso | TDataSource | outro | — | — | — | — | — |
| dsConsulta | TDataSource | outro | — | — | — | — | — |
| CdsConsulta | TClientDataSet | outro | — | — | — | — | — |
| CdsConsultaID | TStringField | outro | — | — | — | — | — |
| CdsConsultaNOME | TStringField | outro | — | — | — | — | — |
| CdsConsultaSelecionado | TBooleanField | outro | — | — | — | — | — |
| CdsConsultaSelecionadoInicial | TBooleanField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 120 | `FEmpresaAcessoController.Excluir` |
| `ActExibirTudoExecute` | 143 | `FEmpresaAcessoController.GetEmpresaAcessoTodos` |
| `ActIncluirExecute` | 165 | — |
| `ActIrExecute` | 173 | `FEmpresaAcessoController.GetEmpresaAcesso`, `FEmpresaAcessoController.GetEmpresaAcessoPorNome` |
| `FormCreate` | 301 | `TPreCadastroController.Create`, `FPreCadastroController.SetConexao`, `TEmpresaAcessoController.Create`, `FEmpresaAcessoController.SetConexao` |
| `GravaCampos` | 326 | `FEmpresaAcessoController.Inserir`, `FEmpresaAcessoController.Atualizar`, `FPreCadastroController.GetPessoa`, `FPreCadastroController.Atualizar` |
| `ValidarCampos` | 570 | `FEmpresaAcessoController.GetEmpresaAcessoPorCNPJ` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 124: `Excluir o registro?`
- Linha 129: `Problemas com a exclusão no Banco de Dados!`
- Linha 536: `CNPJ Inválido.`
- Linha 549: `CPF Inválido.`
- Linha 556: `O CNPJ ou CPF inválido.`
- Linha 578: `O nome deve ser preenchido`
- Linha 587: `CNPJ inválido`
- Linha 596: `CNPJ já existe.`
- Linha 607: `CPF inválido`
- Linha 616: `CPF já existe.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
