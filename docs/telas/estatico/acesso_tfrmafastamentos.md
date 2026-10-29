# Acesso: TFrmAfastamentos

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Acesso > Afastamentos Cedidos....

- DFM: `Acesso/UFrmAfastamentos.dfm`
- PAS: `Acesso/UFrmAfastamentos.pas`
- Handler de abertura: `acAceAfastamentosCedidosExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmAfastamentos | TFrmAfastamentos | outro | Afastamentos | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=False |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| BtnImportacao | THoverSpeedButton | ação | Importar Afastamentos (Ctrl+F5) | 3 | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| LblInicio | TLabel | rótulo | Início: | — | — | — | — |
| LblTermino | TLabel | rótulo | Término: | — | — | — | — |
| LblSelecao | TLabel | rótulo | Seleção: | — | — | — | — |
| LblMotivo | TLabel | rótulo | Motivo: | — | — | — | — |
| LblOutro | TLabel | rótulo | Qual: | — | — | — | Visible=False |
| ImgSelecao | TImage | outro | — | — | — | — | — |
| ImgMotivo | TImage | outro | — | — | — | — | — |
| ImgInicio | TImage | outro | — | — | — | — | — |
| ImgTermino | TImage | outro | — | — | — | — | — |
| ImgOutro | TImage | outro | — | — | — | — | Visible=False |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| MskTermino | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| PgTipoSelecao | TPageControl | contêiner | — | 4 | — | — | — |
| TabPessoa | TTabSheet | contêiner | Pessoa | — | — | — | — |
| LblSelecaoPessoa | TLabel | rótulo | Pessoa: | — | — | — | — |
| lblPessoa | TLabel | rótulo | lblPessoa | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | F5 | — | — | — | — |
| ImgSelecaoPessoa | TImage | outro | — | — | — | — | — |
| EdPessoa | TEdit | campo de texto/data | — | 0 | — | — | Text=EdPessoa |
| TabSetor | TTabSheet | contêiner | Setor | — | — | — | — |
| LblSelecaoSetor | TLabel | rótulo | Setor: | — | — | — | — |
| mlSetor | TMetaEquipLocalizar | outro | F5 | — | — | — | — |
| LblSetor | TLabel | rótulo | LblSetor | — | — | — | — |
| ImgSelecaoSetor | TImage | outro | — | — | — | — | — |
| EdSetor | TEdit | campo de texto/data | — | 0 | — | — | Text=EdSetor |
| TabFiltro | TTabSheet | contêiner | Filtro | — | — | — | — |
| LblSelecaoFiltro | TLabel | rótulo | Filtro | — | — | — | — |
| mlFiltro | TMetaEquipLocalizar | outro | F5 | — | — | — | — |
| lblNomeFiltro | TLabel | rótulo | lblNomeFiltro | — | — | — | — |
| ImgSelecaoFiltro | TImage | outro | — | — | — | — | — |
| EdFiltro | TEdit | campo de texto/data | — | 0 | — | — | Text=EdFiltro |
| CmbTipoSelecao | TComboBox | seleção | — | 3 | — | — | Text=Pessoa, ItemIndex=0 |
| MskInicio | TMaskEdit | campo de texto/data | — | 1 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| CmbMotivo | TComboBox | seleção | — | 5 | — | — | Text=Férias, ItemIndex=0 |
| EdtOutro | TEdit | campo de texto/data | — | 6 | — | — | Visible=False |
| chkTerminoInd | TCheckBox | seleção | Término Indeterminado | 7 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActSincronizar | TAction | ação | Importar Afastamentos (Ctrl+F5) | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActBuscarSelecao | TAction | ação | F5 | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsFerias | TDataSource | outro | — | — | — | — | — |
| CdsFerias | TClientDataSet | outro | — | — | — | — | — |
| CdsFeriasId | TIntegerField | outro | — | — | — | — | — |
| CdsFeriasIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsFeriasNomePessoa | TStringField | outro | — | — | — | — | — |
| CdsFeriasCausa | TStringField | outro | — | — | — | — | — |
| CdsFeriasDataInicio | TDateField | outro | — | — | — | — | — |
| CdsFeriasDataTermino | TStringField | outro | — | — | — | — | — |
| CdsFeriasIdFreq | TStringField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActCancelarExecute` | 135 | — |
| `ActExcluirExecute` | 147 | `FAfastamentosController.Excluir` |
| `ActExibirTudoExecute` | 162 | `FAfastamentosController.GetTodos` |
| `ActIrExecute` | 184 | `FAfastamentosController.GetAfastamentos` |
| `FormCreate` | 353 | `TAfastamentosController.Create`, `FAfastamentosController.SetConexao`, `TPessoasController.Create`, `FPessoasController.SetConexao`, `FAfastamentosController.GetTodos` |
| `GravaCampos` | 471 | `FAfastamentosController.GetPessoasPorSetor`, `FAfastamentosController.GetPessoasFiltro`, `FAfastamentosController.Inserir`, `FAfastamentosController.Atualizar` |
| `ValidarCampos` | 659 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 151: `Excluir o registro?`
- Linha 156: `Problemas com a exclusão no Banco de Dados!`
- Linha 519: `Aten��o!`
- Linha 531: `Nenhuma pessoa encontrada para cadastrar afastamento.`
- Linha 669: `Uma pessoa deve ser selecionada.`
- Linha 678: `Um setor deve ser selecionada.`
- Linha 687: `Um filtro deve ser selecionada.`
- Linha 696: `Data de Início é inválida.`
- Linha 703: `Data de Termino é inválida.`
- Linha 738: `A data de início não pode ser maior que a data de término.`
- Linha 744: `É necessário preencher o motivo.`
- Linha 767: `Filtro não cadastrado`
- Linha 800: `Setor não cadastrado`
- Linha 828: `Pessoa não cadastrada`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
