# Acesso: TFGerarAcesso

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Acesso > Gerar Acesso....

- DFM: `Acesso/UGerarAcesso.dfm`
- PAS: `Acesso/UGerarAcesso.pas`
- Handler de abertura: `acAceGerarAcessoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FGerarAcesso | TFGerarAcesso | outro | Gerar Acesso | — | — | — | Visible=True |
| pnlPrincipal | TPanel | contêiner | — | 1 | — | — | — |
| LblNroDiasGerar | TLabel | rótulo | Nº de Dias para Gerar: | — | — | — | — |
| LblSelecao | TLabel | rótulo | Seleção: | — | — | — | — |
| ImgNroDiasGerar | TImage | outro | — | — | — | — | — |
| ImgSelecao | TImage | outro | — | — | — | — | — |
| ImgVersao | TImage | outro | — | — | — | — | — |
| lblVersao | TLabel | rótulo | Versão do Gerador de Acesso: | — | — | — | — |
| EdNroDiasGerar | TSpinEdit | campo de texto/data | — | 0 | — | 2 | — |
| CmbTipoSelecao | TComboBox | seleção | — | 1 | — | — | Text=Geral, ItemIndex=0 |
| CmbVersao | TComboBox | seleção | — | 2 | — | — | Text=2.0, ItemIndex=1 |
| CpTipoSelecoes | TCardPanel | contêiner | — | 3 | — | — | — |
| CdFiltros | TCard | outro | Filtros | 0 | — | — | — |
| PnlFiltro | TPanel | contêiner | — | 0 | — | — | — |
| ImgFiltro | TImage | outro | — | — | — | — | — |
| MlFiltro | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| LblFiltro | TLabel | rótulo | Filtro: | — | — | — | — |
| lblNomeFiltro | TLabel | rótulo | lblNomeFiltro | — | — | — | — |
| EdFiltro | TEdit | campo de texto/data | — | 0 | — | — | Text=EdFiltro |
| CdPessoas | TCard | outro | Pessoas | 1 | — | — | — |
| LblPessoas | TLabel | rótulo | Lista de Pessoas: | — | — | — | — |
| ImgPessoas | TImage | outro | — | — | — | — | — |
| mlPessoa | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| LstPessoas | TListBox | seleção | — | 0 | — | — | — |
| BtnRemoverPessoa | THoverSpeedButton | ação | Ctrl+Del | 1 | — | — | — |
| CdSetores | TCard | outro | Setores | 2 | — | — | — |
| mlSetor | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| ImgSetores | TImage | outro | — | — | — | — | — |
| LblSetores | TLabel | rótulo | Lista de Setores: | — | — | — | — |
| LstSetores | TListBox | seleção | — | 0 | — | — | — |
| BtnExcluirSetor | THoverSpeedButton | ação | Ctrl+Del | 1 | — | — | — |
| CdVeiculos | TCard | outro | Veiculos | 3 | — | — | — |
| Image8 | TImage | outro | — | — | — | — | — |
| Label3 | TLabel | rótulo | Lista de Veículos: | — | — | — | — |
| mlVeiculo | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| LstVeiculos | TListBox | seleção | — | 0 | — | — | — |
| BtnRemoverVeiculo | THoverSpeedButton | ação | Ctrl+Del | 1 | — | — | — |
| CdEscola | TCard | outro | Escola | 4 | — | — | — |
| imgEscola | TImage | outro | — | — | — | — | — |
| lblEscola | TLabel | rótulo | Lista de Alunos: | — | — | — | — |
| mlEscola | TMetaEquipLocalizar | outro | F4 | — | — | — | — |
| imgTurnos | TImage | outro | — | — | — | — | Visible=False |
| imgTurmas | TImage | outro | — | — | — | — | Visible=False |
| imgAlunos | TImage | outro | — | — | — | — | Visible=False |
| LstEscola | TListBox | seleção | — | 0 | — | — | — |
| btnRemoverEscola | THoverSpeedButton | ação | Ctrl+Del | 1 | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | 0 | — | — | — |
| btngeraracesso | THoverSpeedButton | ação | Gerar Acesso (Ctrl+G) | 0 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActGerar | TAction | ação | Gerar Acesso (Ctrl+G) | — | — | — | — |
| ActFechar | TAction | ação | ActFechar | — | — | — | — |
| ActBuscar | TAction | ação | F4 | — | — | — | — |
| ActApagar | TAction | ação | Ctrl+Del | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 338 | — |
| `ValidarCampos` | 765 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 171: `Geração de Acesso Concluída`
- Linha 306: `Filtro não cadastrado`
- Linha 665: `Atenção: Erro ao reaplicar cortes de reservas ativas.`
- Linha 669: `Erro ao processar cortes de reservas: `
- Linha 677: `Erro ao Gerar Acesso: `
- Linha 771: `Inclua pelo menos um aluno na lista.`
- Linha 779: `Inclua pelo menos uma turma na lista.`
- Linha 787: `Inclua pelo menos um turno na lista.`
- Linha 797: `Selecione algum veículo na lista.`
- Linha 806: `O Filtro deve ser informado.`
- Linha 814: `Selecione alguma pessoa na lista.`
- Linha 822: `Selecione algum setor na lista.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
