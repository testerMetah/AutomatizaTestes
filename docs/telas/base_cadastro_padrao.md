# Base comum: `TFrmPadrao`

> Fonte: `Acesso/UFrmPadrao.pas` e `.dfm`, commit `28074dd`. Esta classe é herdada por vários cadastros, inclusive Refeitório, Cardápios, Refeições e Veículos.

## Controles e ações

| Controle | Classe | Caption | TabOrder local | Ação |
|---|---|---|---:|---|
| `GridCadastro` | `TDBGrid` | Grade | 0 | Selecionar registro |
| `ednomeloc` | `TEdit` | Nome (Ctrl+B) | 0 | Filtro |
| `btnExibirTudo` | `THoverSpeedButton` | Exibir tudo (Ctrl+T) | 1 | `ActExibirTudo` |
| `btnexcluir` | `THoverSpeedButton` | Excluir (Ctrl+Del) | 0 | `ActExcluir` |
| `btnInserir` | `THoverSpeedButton` | Incluir (Ctrl+I) | 1 | `ActIncluir` |
| `btnAlterar` | `THoverSpeedButton` | Alterar (Ctrl+E) | 2 | `ActAlterar` |
| `btnOk` | `THoverSpeedButton` | Salvar (Ctrl+S) | 0 | `ActSalvar` |
| `btnCancelar` | `THoverSpeedButton` | Cancelar (Ctrl+D) | 1 | `ActCancelar` |

## Fluxo herdado

- `ActIncluirExecute` limpa os campos, marca o modo `I` e abre a aba Cadastro.
- `ActAlterarExecute` limpa os campos, marca o modo `A`, carrega o registro e abre Cadastro.
- `ActSalvarExecute` chama `ValidarCampos` e depois `GravaCampos` da tela filha. Se a gravação retornar falso, mostra **`Problemas com a gravação no Banco de Dados!`** + quebra de linha + **`Certifique-se de que o servidor esteja ligado e a rede não esteja congestionada!`**. Em exceção, mostra **`Problemas com a gravação no Banco de Dados!`** + quebra de linha + a mensagem da exceção. Em seguida retorna à grade.
- Fora de DEBUG e ADMINISTRACAO, usuário com ID `99999` recebe **`Usuário MASTER não pode salvar registros.`** e o salvamento é abortado. Na ação Alterar, a mensagem aparece, mas a abertura da aba continua.
- `ActCancelarExecute` volta à aba Grid. Não chama `LimparCampos` por si; algumas telas filhas o fazem.
- `ActExcluirExecute` da base apenas desativa um filtro se a grade estiver vazia; a exclusão efetiva fica em cada tela filha.
- `ActionList1Update` habilita Incluir, Alterar, Excluir e Buscar na grade; Salvar e Cancelar no Cadastro. Permissões `FPermiteInserir/Editar/Excluir` também controlam as ações.
- `ActFecharExecute` fecha a janela; `FormClose` usa `caFree`.

`THoverSpeedButton` pode ser identificado como controle customizado pelo pywinauto. Confirmar `class_name`, hierarquia e texto real na UI antes de fixar seletores.
