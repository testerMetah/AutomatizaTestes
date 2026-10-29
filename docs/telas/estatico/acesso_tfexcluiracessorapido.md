# Acesso: TFExcluirAcessoRapido

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Acesso > Acesso Rápido... > Excluir Acesso Rápido....

- DFM: `Acesso/uFExcluirAcessoRapido.dfm`
- PAS: `Acesso/uFExcluirAcessoRapido.pas`
- Handler de abertura: `acAceAcessoRapidoExcExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FExcluirAcessoRapido | TFExcluirAcessoRapido | outro | Excluir Acesso Rápido por Pessoa | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | 3 | — | — | — |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| lblFiltrarPessoa | TLabel | rótulo | Filtrar Pessoa: | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | 3 | — | — | Visible=False |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | Visible=False |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | Visible=False |
| btnExcluirAcesso | THoverSpeedButton | ação | Excluir Acesso Selecionado (Ctrl+Del) | 0 | — | — | — |
| btnSelecionarTodos | THoverSpeedButton | ação | Selecionar Todos | 4 | — | — | — |
| DGridAcessos | TDrawGrid | grade | — | 0 | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActIncluir | TAction | ação | — | — | — | — | — |
| ActAlterar | TAction | ação | — | — | — | — | — |
| ActExcluir | TAction | ação | Excluir Acesso Selecionado (Ctrl+Del) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| QryAcessosRapidos | TFDQuery | outro | — | — | — | — | — |
| DsAcessosRapidos | TDataSource | outro | — | — | — | — | — |
| QryExcluir | TFDQuery | outro | — | — | — | — | — |
| CdsAcessoRapido | TClientDataSet | outro | — | — | — | — | — |
| CdsAcessoRapidoid | TIntegerField | outro | — | — | — | — | — |
| CdsAcessoRapidoNome | TStringField | outro | — | — | — | — | — |
| CdsAcessoRapidoStatus | TIntegerField | outro | — | — | — | — | — |
| CdsAcessoRapidoCpf | TStringField | outro | — | — | — | — | — |
| CdsAcessoRapidoTipoPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsAcessoRapidoEmpresaAcesso | TIntegerField | outro | — | — | — | — | — |
| DsAcessoRapido | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 159 | — |
| `ActExcluirExecute` | 469 | — |
| `ActExibirTudoExecute` | 474 | — |
| `ExcluirAcessosSelecionados` | 997 | — |
| `GravaCampos` | 1102 | — |
| `ValidarCampos` | 1112 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 436: `Erro ao carregar acessos: `
- Linha 485: `Nenhum acesso rápido encontrado.`
- Linha 1029: `Selecione pelo menos um acesso rápido para excluir.`
- Linha 1035: `Deseja realmente excluir os %d acesso(s) rápido(s) selecionado(s)?`
- Linha 1064: `%d acesso(s) excluído(s) com sucesso.`
- Linha 1068: `Ocorreram alguns erros:`
- Linha 1091: `Deseja excluir este acesso rápido?`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
