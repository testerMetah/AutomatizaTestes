# Acesso: TFrmCadEmpresas

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Empresa....

- DFM: `Acesso/uFrmCadEmpresas.dfm`
- PAS: `Acesso/uFrmCadEmpresas.pas`
- Handler de abertura: `acCadEmpresaExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadEmpresas | TFrmCadEmpresas | outro | Cadastro de Empresas | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | — |
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
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| LblCpfCnpj | TLabel | rótulo | CNPJ: | — | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 1 | — | — | — |
| EdCpf_Cnpj | TEdit | campo de texto/data | — | 2 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsEmpresas | TDataSource | outro | — | — | — | — | — |
| CdsEmpresas | TClientDataSet | outro | — | — | — | — | — |
| CdsEmpresasId | TIntegerField | outro | — | — | — | — | — |
| CdsEmpresasNome | TStringField | outro | — | — | — | — | — |
| CdsEmpresasCpf_Cnpj | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 72 | `FEmpresasController.VerificarRegistroEmpUser`, `FEmpresasController.Excluir` |
| `ActExibirTudoExecute` | 90 | `FEmpresasController.GetEmpresasTodos` |
| `ActIncluirExecute` | 108 | — |
| `ActIrExecute` | 115 | `FEmpresasController.GetEmpresa`, `FEmpresasController.GetEmpresasPorDescricao` |
| `FormCreate` | 250 | `TEmpresasController.Create`, `FEmpresasController.SetConexao` |
| `GravaCampos` | 267 | `FEmpresasController.Inserir`, `FEmpresasController.Atualizar` |
| `ValidarCampos` | 301 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 76: `Excluir o registro?`
- Linha 79: `Esta empresa est� vinculada � sua sess�o atual e n�o pode ser exclu�da!`
- Linha 84: `Problemas com a exclus�o no Banco de Dados!`
- Linha 203: `CNPJ com erro! Favor verificar.`
- Linha 217: `CPF com erro! Favor verificar.`
- Linha 224: `O CPF tem 11 n� e CNPJ tem 14 n�.`
- Linha 307: `O Nome da empresa � obrigat�rio.`
- Linha 314: `O CPF/CNPJ da empresa � obrigat�rio.`
- Linha 322: `CPF inv�lido.`
- Linha 324: `CNPJ inv�lido.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
