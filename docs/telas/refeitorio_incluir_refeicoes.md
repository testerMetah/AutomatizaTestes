# Refeitório > Incluir Refeições

> Fonte estática: `Acesso/UFrmCadRefeicoes.pas` e `.dfm`, commit `28074dd`. Form `TFrmRefeicoes` herdado de `TFrmPadrao`; caption do DFM: `Incluir Refeições Manual`.

## Controles de entrada e filtros

| Nome | Classe | Função | TabOrder local | Máscara/padrão |
|---|---|---|---:|---|
| `dtRefeicao`, `tmRefeicao` | `TMaskEdit` | Data e hora da refeição | 0/1 | `!99/99/9999;1; ` e `!99:99;1; `; ao limpar: hoje e hora vazia |
| `EdColetor` | `TEdit` | Coletor | 2 | Resolve refeitório vinculado |
| `cmbTipoRefeicao` | `TComboBox` | Tipo de refeição | 3 | Ao limpar: `ItemIndex=1` |
| `EdtCardapio` | `TEdit` | Cardápio | Ver DFM | Obrigatório em `ValidarCampos` |
| `CmbTipoSelecao` | `TComboBox` | Tipo de seleção | 5 | Decide filtro, pessoas, setores ou pré-cadastros |
| `EdFiltro`, `LstPessoas`, `LstSetores`, `LstPreCadastro` | diversos | Alvo da seleção | Por aba | Dependem do tipo de seleção |
| `dtInicio`, `tmInicio`, `DtTermino`, `TmTermino` | `TMaskEdit` | Filtro de período | 0–3 | Ao limpar: hoje, 00:00 até 23:59 |
| `CmbLocTipoRefeicao`, `EdPessoaFiltro`, `EdRefeitorio`, `EdCardapio` | combo/edits | Outros filtros da grade | 0 em suas abas | Abas Ctrl+B, Ctrl+G, Ctrl+H, Ctrl+J |

Botões Incluir, Alterar, Excluir, OK e Cancelar vêm da classe base. A tela tem ação de relatório própria (`ActRelatorioExecute`).

## Validações e mensagens exatas

`ValidarCampos` exige data, hora, coletor e cardápio. As mensagens são, respectivamente: **`A data da refeição deve ser informada.`**, **`A hora da refeição deve ser informada.`**, **`O coletor deve ser informado.`**, **`O cardápio deve ser informado.`**. Para seleção por filtro, pessoa ou setor, exige o alvo correspondente: **`O Filtro deve ser informado.`**, **`Selecione alguma pessoa na lista.`**, **`Selecione algum setor na lista.`**. Se o coletor não tiver refeitório vinculado, mostra **`Nenhum refeitório vinculado, vincule pelo cadastro de coletores.`**. A validação de tipo de refeição está comentada no código.

`dtRefeicaoExit` mostra **`Data Inválida!`**; `tmRefeicaoExit`, **`Hora Inválida!`**. Os eventos de saída de cardápio, filtro e refeitório mostram **`Cardápio não cadastrado`**, **`Filtro não cadastrado`** e **`Refeitório não cadastrado`**. Valor malformado mostra **`Valor inválido.`** (`EdValorRefeicaoExit`). `ValidarFiltros` exige início/fim do período e mostra **`Data de Início deve ser informada.`**, **`A hora de Início deve ser informada.`**, **`Data de Término deve ser informada.`** e **`A hora de Término deve ser informada.`**.

## Ações e dependências

- `GravaCampos` inclui refeições para os alvos selecionados, em lotes de até 1000 IDs. Há caminhos separados para pessoa e pré-cadastro. A rotina usa coletor, cardápio e refeitório e pode atualizar saldo de créditos. Na alteração chama `FRefeicoesController.Atualizar` para um registro.
- `ActAlterarExecute` e `ActExcluirExecute` impedem mudar ou excluir uma marcação cuja origem é `E` (importada do coletor). Mensagens: **`Não é possível alterar uma marcação que já foi importada do coletor.`** e **`Não é possível excluir uma marcação que já foi importada do coletor.`**.
- `ActExcluirExecute` pede **`Excluir o registro?`**. Se excluir uma refeição de tipo 1 com controle de créditos, incrementa o saldo da pessoa no mês atual. Falha no banco mostra **`Problemas com a exclusão no Banco de Dados!`** + quebra de linha + **`Certifique-se de que o servidor esteja ligado e a rede não esteja congestionada!`**.
- `FormShow` carrega todos os registros inicialmente. `AplicarFiltros` consulta por período, tipo, pessoa, refeitório e cardápio; se a data não for convertível, retorna sem mensagem. `ResetarFiltros` restaura hoje, 00:00–23:59.
- `ActRelatorioExecute` copia as linhas da grade para `CdsRefeicoesRelatorio` e chama `frxRefeicoes.PrepareReport` e `ShowReport`. O relatório reflete o conjunto atualmente presente na grade.
- `ActSalvarExecute` usa o salvamento herdado e, após inclusão, chama `ActIrExecute`. Cancelar usa a ação herdada; o efeito detalhado depende da classe base.

## Dúvidas

1. Limites e regras de crédito para todos os tipos de refeição exigem leitura dos controllers.
2. `GravaCampos` constrói SQL para lotes; revisar segurança e tratamento de duplicidade antes de transformar isso em teste destrutivo.
3. A visibilidade e ordem dos filtros devem ser confirmadas na UI, pois `FormShow` esconde a aba herdada `TabSheet2`.
