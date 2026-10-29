# Acesso: TFGerAcessoRapido

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Acesso > Acesso Rápido... > Gerar Acesso Rápido....

- DFM: `Acesso/UGerAcessoRapido.dfm`
- PAS: `Acesso/UGerAcessoRapido.pas`
- Handler de abertura: `acAceAcessoRapidoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FGerAcessoRapido | TFGerAcessoRapido | outro | Acesso Rápido | — | — | — | Visible=True |
| LblSentido | TLabel | rótulo | Sentido: | — | — | — | — |
| LblSelecao | TLabel | rótulo | Seleção: | — | — | — | — |
| ImgSentido | TImage | outro | — | — | — | — | — |
| ImgSelecao | TImage | outro | — | — | — | — | — |
| GbPeriodo | TGroupBox | contêiner |           Período: | 0 | — | — | — |
| ImgPeriodo | TImage | outro | — | — | — | — | — |
| PnlPeriodo | TPanel | contêiner | — | 0 | — | — | — |
| lblAte | TLabel | rótulo | Até | — | — | — | — |
| MEdDataInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdHoraInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;  | 5 | Text=  :   |
| MEdDataFim | TMaskEdit | campo de texto/data | — | 2 | !99/99/9999;1;  | 10 | Text=  /  /     |
| MEdHoraFim | TMaskEdit | campo de texto/data | — | 3 | !99:99;1;  | 5 | Text=  :   |
| CmbSentido | TComboBox | seleção | — | 2 | — | — | Text=Todos, ItemIndex=2 |
| PnlFundo | TPanel | contêiner | — | 1 | — | — | — |
| BtnGerarAcesso | THoverSpeedButton | ação | Gerar Acesso Rápido (Ctrl+G) | 0 | — | — | — |
| BtnFechar | THoverSpeedButton | ação | Fechar (Alt+F4) | 1 | — | — | — |
| CmbTipoSelecao | TComboBox | seleção | — | 3 | — | — | — |
| GbColetores | TGroupBox | contêiner |           Coletores: | 4 | — | — | — |
| ImgColetores | TImage | outro | — | — | — | — | — |
| ChkColetores | TCheckListBox | seleção | — | 0 | — | — | — |
| PgcTipoSelecoes | TPageControl | contêiner | — | 5 | — | — | — |
| TabPessoas | TTabSheet | contêiner | TabPessoas | — | — | — | — |
| LblPessoas | TLabel | rótulo | Lista de Pessoas: | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| ImgPessoas | TImage | outro | — | — | — | — | — |
| LstPessoas | TListBox | seleção | — | 0 | — | — | — |
| BtnRemoverPessoa | THoverSpeedButton | ação | Ctrl+Del | 1 | — | — | — |
| TabPreCadastros | TTabSheet | contêiner | TabPreCadastros | — | — | — | — |
| LblPreCadastros | TLabel | rótulo | Lista de Pré-Cadastros:  | — | — | — | — |
| mlPreCadastro | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| ImgPreCadastros | TImage | outro | — | — | — | — | — |
| LstPreCadastro | TListBox | seleção | — | 0 | — | — | — |
| BtnRemoverPreCadastro | THoverSpeedButton | ação | Ctrl+Del | 1 | — | — | — |
| TabCrachas | TTabSheet | contêiner | TabCrachas | — | — | — | — |
| Label3 | TLabel | rótulo | Crachá: | — | — | — | — |
| EdCrachas | TEdit | campo de texto/data | — | 0 | — | — | Text=EdPessoa |
| TabFiltros | TTabSheet | contêiner | Filtros | — | — | — | — |
| Label5 | TLabel | rótulo | Filtro:  | — | — | — | — |
| mlFiltros | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblFiltro | TLabel | rótulo | lblFiltro | — | — | — | — |
| EdFiltro | TEdit | campo de texto/data | — | 0 | — | — | — |
| TabSetores | TTabSheet | contêiner | Setores | — | — | — | — |
| Label4 | TLabel | rótulo | Lista de Setores: | — | — | — | — |
| mlSetores | TMetaEquipLocalizar | outro | — | — | — | — | — |
| BtnRemoverSetores | TSpeedButton | ação | — | — | — | — | — |
| LstSetores | TListBox | seleção | — | 0 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActGerar | TAction | ação | Gerar Acesso Rápido (Ctrl+G) | — | — | — | — |
| ActFechar | TAction | ação | Fechar (Alt+F4) | — | — | — | — |
| ActBuscarSelecao | TAction | ação | F4 | — | — | — | — |
| ActExcluirSelecao | TAction | ação | Ctrl+Del | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 201 | — |
| `ActExcluirSelecaoExecute` | 234 | — |
| `ValidarCampos` | 484 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 125: `Selecione um setor na lista para remover.`
- Linha 128: `Não existe setor na lista para remover.`
- Linha 178: `Filtro não cadastrado`
- Linha 245: `Não existem pessoas na lista para remover.`
- Linha 251: `Selecione uma pessoa na lista para remover.`
- Linha 263: `Não existem pré-cadastros na lista para remover.`
- Linha 269: `Selecione um pré-cadastro na lista para remover.`
- Linha 377: `Geração de Acesso concluída`
- Linha 550: `Selecione alguma pessoa na lista.`
- Linha 564: `Nenhum coletor selecionado.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
