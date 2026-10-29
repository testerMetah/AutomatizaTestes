# Refeitório > Cadastro

> Fonte estática: `Acesso/uFrmCadRefeitorio.pas` e `.dfm` no commit `28074dd`. Confirmar no build instalado. Form `TFrmCadRefeitorios`, herdado de `TFrmPadrao`.

## Controles

| Nome | Classe | Caption/função | TabOrder | Padrão/limite |
|---|---|---|---:|---|
| `EdNome` | `TEdit` | Nome | 0 | `MaxLength=50` definido em `FormCreate` |
| `cmbStatus` | `TComboBox` | Situação | 1 | Ativo; opções Ativo/Inativo |
| `cmbSentidoAcesso` | `TComboBox` | Sentido de Acesso | 2 | Entrada; opções Entrada/Entrada e Saída |
| `ChUtilizaControleCreditos` | `TCheckBox` | Utilizar Controle de Créditos | 3 | `Visible=False` no DFM |
| `GridItens` | `TDBGrid` | Coletores de Acesso | 0 no painel | Colunas Selecionar, Id, Nome |
| `btnImportar` | `THoverSpeedButton` | Importar Refeitórios (Ctrl+F5) | 3 na barra | Aciona `ActImportar` |
| `ednomeloc` | `TEdit` herdado | Filtro por nome | Herdado | Aba Nome (Ctrl+B) |
| `btnInserir`, `btnAlterar`, `btnexcluir`, `btnOk`, `btnCancelar`, `btnExibirTudo` | `THoverSpeedButton` herdados | Ações da tela padrão | Herdado | Conferir DFM ancestral |

## Regras e mensagens

- `ValidarCampos`: nome vazio após `Trim` aborta com **`O Nome do refeitório deve ser informado.`**. É o único campo obrigatório explícito nesta unit; a classe base pode acrescentar validações.
- `GravaCampos`: Salvar cria `TRefeitoriosModel` com nome, status, sentido, controle de créditos e empresa do usuário. Em inclusão chama `FRefeitoriosController.Inserir`; em alteração, `Atualizar`. Se a gravação for bem-sucedida, chama `AtualizaColetores` para sincronizar vínculos com os coletores selecionados.
- `CadastroShow`: lista coletores ativos, exceto os da marca `tmcControlID_IdAntena`. Marca os coletores já ligados ao refeitório. Essa exclusão de marca é regra explícita do código, ainda sujeita à confirmação no build.
- `ActExcluirExecute`: pede **`Excluir o registro?`**, chama primeiro `FCardRefController.ExcluirPorRefeitorio`, depois `FRefeitoriosController.Excluir`. Se uma etapa falhar, mostra **`Problemas com a exclusão no Banco de Dados!`** + quebra de linha + **`Certifique-se de que o servidor esteja ligado e a rede não esteja congestionada!`**. `TCardapiosRefeitoriosDAO.ExcluirPorRefeitorio` remove fisicamente as linhas da tabela de vínculo; `TRefeitoriosDAO.Excluir` marca `Refeitorios.excluido = 'S'` e registra histórico `D`. `Inserir` cria nova linha `excluido = 'N'` e histórico `I`.
- `ActIrExecute`: consulta por descrição/nome via `GetRefeitoriosPorDescricao` quando o filtro não está vazio. `ActExibirTudoExecute` usa `GetRefeitoriosTodos`; ambos ordenam a grade por `NOME`.
- `ActIncluirExecute` foca `EdNome`. `ActAlterarExecute` só abre o cadastro quando a grade tem registros. Para usuário MASTER fora de DEBUG, exibe **`Usuário MASTER não pode salvar registros.`** e continua a abertura; a base aborta a tentativa de salvar (`TFrmPadrao.ActSalvarExecute`).
- `ActImportarExecute`: abre conexão com banco do cliente e chama `ImportarRefeitorios`. Resultado sem texto de erro mostra **`Importação realizada com sucesso`**. Resultado com erro mostra **`Erro ao gravar informações no Banco de Dados: `** seguido do texto retornado.
- Cancelar volta à grade pela ação herdada. Não há comando de relatório neste formulário; relatórios são telas separadas no menu. Ver [base_cadastro_padrao.md](base_cadastro_padrao.md).

## Dúvidas e dependências

1. Se a remoção das relações e a exclusão lógica do refeitório são atômicas; o código do form chama as duas etapas em sequência.
2. A opção de controle de créditos está invisível no DFM, mas é lida e persistida por `GravaCampos`.
