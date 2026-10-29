# Refeitório > Reservas > Refeições

> Fonte estática: `Refeitorio/Views/Acessus.Refeitorio.Views.ReservasRefeicoes.pas` e `.dfm`, commit `28074dd`. Form `TFrmRefeitorioViewsReservasRefeicoes`, caption `Liberação de Reserva de Refeições`.

## Controles principais

| Nome | Classe | Função/caption | TabOrder local | Máscara/padrão |
|---|---|---|---:|---|
| `edGestor`, `edCracha`, `edCardapio`, `edPessoa` | `TEdit` | Gestor, credencial, cardápio, pessoa | 0–3 | Códigos resolvidos em eventos de saída |
| `mskIni`, `mskFim` | `TMaskEdit` | Início/fim de consumo | 4/5 | `!99/99/9999;1;_`, dez caracteres |
| `cmbTipoPessoa` | `TComboBox` | Pessoa/pré-cadastro | 6 | Alterna tipo de pessoa |
| `GridCadastro` | `TDBGrid` herdado | Reservas | 0 | Colunas incluem Autorizar, Data, Credencial, Pessoa, Cardápio, Início, Fim, Refeições, Autorização e Gestor |
| `dtInicio`, `tmInicio`, `DtTermino`, `TmTermino` | `TMaskEdit` | Filtro por período | 1–4 | Data `!99/99/9999;1; `; hora `!99:99;1; ` |
| `ednrocracha`, `edBuscaCardapio`, `cmbBuscaTipoPessoa`, `CmbSituacao`, `ednomeloc` | edit/combo | Filtros da grade | 0 em suas abas | Crachá, Cardápio, Tipo de Pessoa, Situação e Pessoa |
| `btnConfirmar` / ação `AcConfirmar` | `THoverSpeedButton` | Confirmar (Ctrl+C) | 3 na barra | Autoriza/desautoriza as reservas marcadas |
| `btnImportar` / ação `AcImportar` | `THoverSpeedButton` | Importar Reservas (Ctrl+F5) | 4 na barra | Importação |

O DFM mostra `Cardápio (Ctrl+Q)` na aba de filtro, mas a ação `ActTSCardapio` tem caption `Cardápio (Ctrl+D)`. Registrar como **conflito de atalhos** até conferir a UI. A seleção de cardápio abre uma aba própria com `GridItens`, Confirmar (Ctrl+Alt+C) e Cancelar (caption `Cmd+Alt+D` no DFM).

## Validações e mensagens

`ValidarCampos` impede alterar reserva já liberada: **`Não é possível alterar uma reserva que já foi liberada para consumo.`**. Exige pessoa e cardápio: **`É necessário selecionar uma pessoa.`** e **`É necessário selecionar um cardápio.`**. Data inválida gera **`"<valor>" não é uma data válida.`**. Início anterior a hoje gera **`A data de início não pode ser menor que a data atual.`**. Cardápio ausente gera **`Não foi possível encontrar o cardápio com ID: <id>`**. As combinações de data com horários do cardápio são verificadas, com mensagens **`Data/hora inicial inválida após combinação.`**, **`Data/hora final inválida após combinação.`** e **`A data/hora inicial não pode ser maior que a data/hora final.`** (esta última inclui início e fim em linhas separadas).

## Ações e dependências

- `GravaCampos` usa o cardápio para obter horários de consumo; monta início e fim a partir das datas e desses horários. Na inclusão, chama `FReservasRefeicoesController.Inserir`; na alteração, `Atualizar`. Há **possível falha**: a função retorna `True` mesmo quando o controller retorna falso e mostra erro.
- `GridCadastroDblClick` impede alterar reserva liberada. `ActAlterarExecute` também precisa ser lido para todas as condições de edição.
- `ActExcluirExecute` pede **`Excluir todos os registros selecionados?`** e avisa **`As reservas não poderão ser excluídas ou desautorizadas após o horário de início do consumo.`**. Ignora reserva de situação 2 cujo início já passou. Para reserva autorizada excluída, remove faixas de acesso ligadas aos crachás e recalcula acessos. Erro por exceção mostra **`Erro ao excluir reserva: `** + detalhe.
- `AcConfirmarExecute` chama `GravaSituacao` e processa autorizações/desautorizações; se a operação é cancelada, mostra **`Operação cancelada pelo usuário.`**. O fluxo também depende dos parâmetros `ObterExcluirAcessoAoReservar` e `ObterAutorizarReservasDurantePeriodoConsumo`.
- `AcImportarExecute` importa reservas e pode mostrar resultado de informação, aviso, confirmação ou erro conforme retorno do importador.
- `ActIrExecute`/`ActExibirTudoExecute` consultam a grade. Não foi identificada ação de relatório nesse formulário; relatório de reservas é item separado no menu.
- Cancelar do cadastro segue a base e volta à grade. Ver [base_cadastro_padrao.md](base_cadastro_padrao.md).

## Dúvidas

1. Valores concretos de `Situacao` e a regra de autorização exigem leitura do modelo, controller e parâmetros.
2. Quando um erro de gravação é mascarado pelo retorno `True` de `GravaCampos`.
3. Atalho real da aba Cardápio e da ação Cancelar da escolha.
