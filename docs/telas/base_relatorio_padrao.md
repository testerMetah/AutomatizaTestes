# Base comum: `TFrmRelPadrao`

> Fonte estática: `Acesso/UFrmRelPadrao.pas` e `.dfm`, commit `28074dd`. As telas de relatório do menu Refeitório herdam esta base.

## Fluxo do relatório

`ActRelatorioExecute` desabilita temporariamente `BtnImpressao`, lê `RgbSelecao` e coleta os IDs selecionados nas grades de Filtros, Setores, Pessoas, Unidades, Pré-Cadastros ou Empresas de Acesso. Em seleção Geral, não há lista de IDs. A base passa tipo e IDs ao `FRelatorioController`, consulta o modelo de relatório escolhido pelo form filho e chama a rotina `GerarRel...` correspondente, que prepara e exibe um relatório FastReport. O filtro de situação, período, coletor ou cardápio é montado pela tela filha antes de chamar `inherited`.

`ActFecharExecute` fecha o form; `FormClose` usa `caFree`. Esta base não tem Salvar, Excluir ou Cancelar de cadastro. A ação de consulta aqui é gerar o relatório; alguns forms também têm localizadores para compor os filtros.

## Validação de período usada pelas telas filhas

`ValidaCamposDataHoraIniFim` tenta converter as datas/horas. Se ambas as partes de início ou fim estiverem vazias, usa, respectivamente, `01/01/2000 00:00:00` e `31/12/9999 00:00:00`. Mensagens retornadas:

- `"<data> <hora>" não é uma data válida`
- `A data de início não pode ser menor ou igual a 31/12/0099 23:59`
- `A data de início não pode ser maior do que a data de término.`

Essa função é diferente de `ValidarCampos`, que também rejeita datas futuras. Cada form deve ser examinado para saber qual das duas funções usa.

## Controles comuns

`RgbSelecao` decide o universo de pessoas/empresas; `cmbOrdenar` e `cmbOrdem` controlam a ordenação; `BtnImpressao` gera o relatório. As grades de seleção e seus botões ficam no `.dfm` ancestral. A ordem de tabulação é local a cada contêiner e deve ser validada na UI antes de virar seletor pywinauto.
