# Refeitório > Cardápios

> Fonte estática: `Acesso/uFrmCadCardapio.pas` e `.dfm`, commit `28074dd`. Form `TFrmCadCardapio`, herdado de `TFrmPadrao`.

## Controles de entrada

| Nome | Classe | Função/caption | TabOrder local | Máscara/padrão/limite |
|---|---|---|---:|---|
| `EdNome` | `TEdit` | Nome | 0 | Texto inicial do DFM `EdNome`, limpo por `LimparCampos` |
| `cmbStatus` | `TComboBox` | Situação | 1 | Ativo (`ItemIndex=0`) |
| `EdRefeitorio` | `TEdit` | Código do refeitório | 2 | Validado ao sair |
| `EdReservaComConsumo` | `TEdit` | Valor da reserva com consumo | 0 no grupo | Valor monetário convertido por `StrToFloatDef` |
| `EdReservaSemConsumo` | `TEdit` | Valor da reserva sem consumo | 1 no grupo | Idem |
| `EdConsumoSemReserva` | `TEdit` | Valor do consumo sem reserva | 2 no grupo | Idem |
| `chkDesconsiderarDup` | `TCheckBox` | Desconsiderar Reservas Duplicadas | 0 no painel | Mostra/oculta `EdTempoDesc` |
| `EdTempoDesc` | `TEdit` | Minutos a desconsiderar | 4 no grupo | `MaxLength=3`, padrão `0` |
| `MskHoraIniC`, `MskHoraFimC` | `TMaskEdit` | Início/fim do consumo | 0/1 no grupo | `!99:99;1; `, cinco caracteres |
| `MskHoraIniR`, `MskHoraFimR` | `TMaskEdit` | Início/fim da reserva | 0/1 no grupo | `!99:99;1; `, cinco caracteres |
| `GridItens` | `TDBGrid` | Refeitórios relacionados | 0 no painel | Colunas Selecionar, Id, Nome |
| `btnImportar` | `THoverSpeedButton` | Importar Cardápios (Ctrl+F5) | 3 na barra | `ActImportar` |
| `btnInformacao` | `THoverSpeedButton` | Informação (só ícone) | 8 | `ActInformacao` |

Botões Incluir, Alterar, Excluir, OK, Cancelar e Exibir Tudo são herdados; confirmar identificação e ordem no DFM ancestral e na UI.

## Regras, ações e mensagens

- `ValidarCampos`: exige nome não vazio após `Trim`; mensagem **`O Nome do cardápio deve ser informado.`**. Não há validação explícita de período/hora nesta procedure.
- `EdRefeitorioExit`: busca o código; se não existir, mostra **`Refeitório não cadastrado`**, limpa o campo e tenta devolver o foco.
- `EdReservaComConsumoExit`, `EdReservaSemConsumoExit` e `EdConsumoSemReservaExit`: texto não vazio que `StrToFloatDef` não reconhece mostra **`Valor inválido.`**, substitui por `0` e aborta a saída.
- `GravaCampos`: monta o modelo com nome, status, valores, tempo, refeitório, quatro horários e empresa atual. Usa `StrToFloatDef`, `StrToIntDef` e `StrToTimeDef`; entradas inválidas que escapem dos eventos podem virar zero. Na inclusão chama `Inserir`; na alteração, `Atualizar`; depois chama `GravarRelacaoRefeitorios`.
- `GravarRelacaoRefeitorios`: insere a relação com cada refeitório marcado. O laço não mostra remoção explícita das relações desmarcadas; verificar no controller e no build.
- `ActExcluirExecute`: pede **`Excluir o registro?`**, exclui relações por cardápio e depois chama `FCardapiosController.Excluir`. Falha mostra **`Problemas com a exclusão no Banco de Dados!`** + quebra de linha + **`Certifique-se de que o servidor esteja ligado e a rede não esteja congestionada!`**. `TCardapiosRefeitoriosDAO.ExcluirPorCardapio` remove fisicamente as relações; `TCardapiosDAO.Excluir` marca `Cardapios.excluido = 'S'` e registra histórico `D`. `Inserir` cria nova linha `excluido = 'N'` e histórico `I`.
- `ActCancelarExecute` chama a ação herdada e `LimparCampos`. `ActIrExecute` e `ActExibirTudoExecute` consultam a lista de cardápios; o filtro é `ednomeloc` (Nome, Ctrl+B).
- `ActImportarExecute` chama a importação do controller; mostra **`Importação realizada com sucesso`** ou **`Erro ao gravar informações no Banco de Dados: `** + erro.
- `ActInformacaoExecute` explica: **`Em caso de consumo sem reserva, caso haja horários de consumo conflitantes para o mesmo refeitório será levado em consideração o cardápio de menor id.`**
- Relatório não é ação deste formulário; há telas separadas de relatório no menu.

## Dúvidas

1. Critérios de sobreposição de horários e efeito completo da opção de reservas duplicadas, além da mensagem informativa.
2. Se relações de refeitórios desmarcadas são removidas em outro ponto.
3. Tratamento de horários inválidos pela classe base, pelo controller ou pelo banco; `GravaCampos` usa `StrToTimeDef(..., 0)`.
