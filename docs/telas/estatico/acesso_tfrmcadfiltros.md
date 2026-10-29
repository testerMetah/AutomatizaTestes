# Acesso: TFrmCadFiltros

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Filtros....

- DFM: `Acesso/UFrmCadFiltros.dfm`
- PAS: `Acesso/UFrmCadFiltros.pas`
- Handler de abertura: `acCadFiltroExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadFiltros | TFrmCadFiltros | outro | Filtros | — | — | — | — |
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
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| PnlCampos | TPanel | contêiner | — | 1 | — | — | — |
| lblNome | TLabel | rótulo | Nome: | — | — | — | — |
| imgNome | TImage | outro | — | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | Text=EdNome |
| dbgSelecao | TDBGrid | grade | — | 1 | — | — | Visible=True |
| btnEditaFiltro | THoverSpeedButton | ação | Editar (Ctrl+Alt+E) | 2 | — | — | — |
| btnExcluiFiltro | THoverSpeedButton | ação | Excluir (Shift+Del) | 3 | — | — | — |
| BtnAdicionar | THoverSpeedButton | ação | Adicionar (Ctrl+N) | 4 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| Filtro | TTabSheet | contêiner | Filtro | — | — | — | — |
| lblTipo | TLabel | rótulo | Tipo: | — | — | — | — |
| imgTipo | TImage | outro | — | — | — | — | — |
| cmbFiltro | TComboBox | seleção | — | 0 | — | — | — |
| pnlFundoFiltro | TPanel | contêiner | — | 1 | — | — | — |
| btnConfirmar | THoverSpeedButton | ação | Confirmar (Ctrl+Alt+S) | 0 | — | — | — |
| btnCalcelaFiltro | THoverSpeedButton | ação | Cancelar (Ctrl+Alt+D) | 1 | — | — | — |
| cdSelecao | TCardPanel | contêiner | — | 2 | — | — | — |
| CardPessoa | TCard | outro | Pessoas | 0 | — | — | — |
| mlPessoas | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblPessoas | TLabel | rótulo | Pessoas: | — | — | — | — |
| imgPessoas | TImage | outro | — | — | — | — | — |
| lbPessoas | TListBox | seleção | — | 0 | — | — | — |
| CardSetores | TCard | outro | Setores | 1 | — | — | — |
| lblSetores | TLabel | rótulo | Setores: | — | — | — | — |
| mlSetores | TMetaEquipLocalizar | outro | — | — | — | — | — |
| imgSetores | TImage | outro | — | — | — | — | — |
| lbSetores | TListBox | seleção | — | 0 | — | — | — |
| CardPreCadastros | TCard | outro | Pré-Cadastros | 2 | — | — | — |
| lblPreCadastros | TLabel | rótulo | Pré-Cadastros: | — | — | — | — |
| mlPreCadastros | TMetaEquipLocalizar | outro | — | — | — | — | — |
| imgPreCadastros | TImage | outro | — | — | — | — | — |
| lbPreCadastros | TListBox | seleção | — | 0 | — | — | — |
| CardUnidades | TCard | outro | Unidades | 3 | — | — | — |
| mlUnidades | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblUnidades | TLabel | rótulo | Unidades: | — | — | — | — |
| imgUnidades | TImage | outro | — | — | — | — | — |
| lbUnidades | TListBox | seleção | — | 0 | — | — | — |
| BtnExcluirSelecao | THoverSpeedButton | ação | (Alt+Del) | 3 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActCancelar | TAction | ação | — | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActAdicionar | TAction | ação | Adicionar (Ctrl+N) | — | — | — | — |
| ActAlterarTipoFiltro | TAction | ação | Editar (Ctrl+Alt+E) | — | — | — | — |
| ActExcluirTipoFiltro | TAction | ação | Excluir (Shift+Del) | — | — | — | — |
| ActExcluirSelecao | TAction | ação | (Alt+Del) | — | — | — | — |
| ActConfirmarFiltro | TAction | ação | Confirmar (Ctrl+Alt+S) | — | — | — | — |
| ActCancelarFiltro | TAction | ação | Cancelar (Ctrl+Alt+D) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsSetoresNSel | TDataSource | outro | — | — | — | — | — |
| DSSetoresSel | TDataSource | outro | — | — | — | — | — |
| CdsSetoresNSel | TClientDataSet | outro | — | — | — | — | — |
| CdsSetoresNSelCODIGO | TIntegerField | outro | — | — | — | — | — |
| CdsSetoresNSelNOME | TStringField | outro | — | — | — | — | — |
| CdsSetoresSel | TClientDataSet | outro | — | — | — | — | — |
| CdsSetoresSelCODIGO | TIntegerField | outro | — | — | — | — | — |
| CdsSetoresSelNOME | TStringField | outro | — | — | — | — | — |
| DsFiltros | TDataSource | outro | — | — | — | — | — |
| CdsFiltros | TClientDataSet | outro | — | — | — | — | — |
| CdsFiltrosId | TIntegerField | outro | — | — | — | — | — |
| CdsFiltrosNome | TStringField | outro | — | — | — | — | — |
| CdsFiltrosPessoas | TStringField | outro | — | — | — | — | — |
| CdsFiltrosSetores | TStringField | outro | — | — | — | — | — |
| CdsFiltrosPreCadastros | TStringField | outro | — | — | — | — | — |
| CdsFiltrosUnidade | TStringField | outro | — | — | — | — | — |
| CdsPessoasNSel | TClientDataSet | outro | — | — | — | — | — |
| CdsPessoasNSelCODIGO | TIntegerField | outro | — | — | — | — | — |
| CdsPessoasNSelNOME | TStringField | outro | — | — | — | — | — |
| CdsPessoasSel | TClientDataSet | outro | — | — | — | — | — |
| CdsPessoasSelCODIGO | TIntegerField | outro | — | — | — | — | — |
| CdsPessoasSelNOME | TStringField | outro | — | — | — | — | — |
| DSPessoasSel | TDataSource | outro | — | — | — | — | — |
| DSPessoasNSel | TDataSource | outro | — | — | — | — | — |
| CdsColetoresSel | TClientDataSet | outro | — | — | — | — | — |
| CdsColetoresSelCODIGO | TIntegerField | outro | — | — | — | — | — |
| CdsColetoresSelNOME | TStringField | outro | — | — | — | — | — |
| CdsColetoresNSel | TClientDataSet | outro | — | — | — | — | — |
| CdsColetoresNSelCODIGO | TIntegerField | outro | — | — | — | — | — |
| CdsColetoresNSelNOME | TStringField | outro | — | — | — | — | — |
| DsColetoresSel | TDataSource | outro | — | — | — | — | — |
| DsColetoresNSel | TDataSource | outro | — | — | — | — | — |
| cdsGridFiltro | TClientDataSet | outro | — | — | — | — | — |
| cdsGridFiltroTipo | TIntegerField | outro | — | — | — | — | — |
| cdsGridFiltroTipoFiltro | TStringField | outro | — | — | — | — | — |
| cdsGridFiltroQuantidade | TStringField | outro | — | — | — | — | — |
| dsGridFiltro | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActCancelarFiltroExecute` | 306 | — |
| `ActExcluirExecute` | 355 | `FFiltrosController.Excluir` |
| `ActExcluirSelecaoExecute` | 371 | — |
| `ActExcluirTipoFiltroExecute` | 404 | — |
| `ActExibirTudoExecute` | 434 | `FFiltrosController.GetFiltroTodos` |
| `ActIncluirExecute` | 455 | — |
| `ActIrExecute` | 462 | `FFiltrosController.GetFiltro`, `FFiltrosController.GetFiltrosPorDescricao` |
| `FormCreate` | 893 | `TFiltrosController.Create`, `FFiltrosController.SetConexao`, `TSetoresController.Create`, `FSetoresController.SetConexao`, `TPessoasController.Create`, `FPessoasController.SetConexao`, `TPreCadastroController.Create`, `FPreCadastrosController.SetConexao` |
| `GravaCampos` | 1011 | `FFiltrosController.Inserir`, `FFiltrosController.Atualizar` |
| `GravaGrid` | 1054 | — |
| `ValidarCampos` | 1155 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 230: `Selecione um item para edita-lo.`
- Linha 359: `Excluir o registro?`
- Linha 364: `Problemas com a exclusão no Banco de Dados!`
- Linha 379: `Selecione um item para excluí-lo.`
- Linha 410: `Selecione um item para excluí-lo.`
- Linha 569: `Selecione um item para excluí-lo.`
- Linha 805: `Este filtro já foi adicionado e não pode ser selecionado novamente.`
- Linha 848: `Este registro já está em edição. Não é possível alterar o tipo enquanto ele estiver sendo modificado.`
- Linha 1135: `Todos os filtros já foram adicionados! Edite os registros para continuar.`
- Linha 1160: `O Nome do Filtro deve ser informado.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
