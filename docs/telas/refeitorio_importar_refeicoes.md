# Refeitório > Importar Refeições

> Fonte estática: `Refeitorio/Views/Acessus.Refeitorio.Views.UFrmImportarRefeicao.pas` e `.dfm`, commit `28074dd`. Form `TFrmGerarRefeicao`.

## Controles principais

| Nome | Classe | Caption/função | TabOrder | Máscara/padrão |
|---|---|---|---:|---|
| `btnImportarRefeicoes` | `THoverSpeedButton` | Importar Refeições (Ctrl+I) | 0 | Aciona `ActImportarRefeicaoExecute` |
| `ChkDesc` | `TCheckBox` | Desconsiderar Marcações Duplicadas | 0 | Habilita `MskTmp` |
| `MskTmp` | `TMaskEdit` | Intervalo das Marcações | 1 | `!90:00;1;_`, `MaxLength=5`, `00:00` |
| `CPImp` | `TCardPanel` | Tipo Importação | 1 | Cartões `impAtual` e `impF` |
| `CmbSelecao` | `TComboBox` | Seleção da importação futura | Ver DFM | Muda `CpSelecao` |
| `ChkDesconsiderarDuplicadas` | `TCheckBox` | Desconsiderar duplicadas (cartão futuro) | 0 | Habilita `MskIntervalo` |
| `MskIntervalo` | `TMaskEdit` | Intervalo (cartão futuro) | 0 | `!90:00;1;_`, `MaxLength=5`, `00:00` |
| `MskDiaIni`, `MskHoraIni`, `MskDiaFim`, `MskHoraFim` | `TMaskEdit` | Período (cartão futuro) | Ver DFM | Validação de datas comentada no `.pas` |

O cartão `impF` contém listas e localizadores de Pessoas, Pré-Cadastros, Setores, Empresas de Acesso e Filtros. `CmbSelecaoChange` limpa todas essas listas, oculta a seleção quando o índice é 0 e mostra o cartão correspondente quando é maior que 0.

## Regras e ações

- `ActImportarRefeicaoExecute` chama `ValidarCampos`, cria `TCalculoAcesso`, repassa `ChkDesc.Checked` para `DesconsiderarMarcacoes`, define `IntervaloMarcacoes` com `MskTmp` se a opção estiver marcada e chama `ImportarMarcacoesRefeitorioRapido` para a empresa atual.
- Ao terminar, mostra **`Importação de Refeições Concluída`** + quebra de linha + **`Tempo decorrido: `** e o tempo calculado (`hh:nn:ss:zzz`).
- `ValidarCampos`: se `ChkDesc` estiver marcado e `MskTmp` não puder ser convertido por `StrToTime`, mostra **`"<valor>" não é um horário válido`**, foca o campo e aborta.
- A validação de data inicial/final e ordem do período está **comentada** na versão do repositório. Não usar esses trechos comentados como resultado esperado de teste. O cartão `impF` se chama `Implementação futura` no DFM; sua execução real precisa de confirmação na UI.
- A tela não contém Salvar, Consultar, Excluir ou relatório próprio. O botão executa importação diretamente; `FormClose` libera a referência do form.

## Dúvidas

1. O seletor `CPImp` permite ao usuário escolher o cartão futuro no build instalado? O código de importação chama sempre a rotina rápida, sem ramificar pelo cartão.
2. A máscara `90:00` aceita uma entrada que `StrToTime` rejeita; validar o comportamento visual no build.
3. Quais efeitos e critérios de duplicidade existem dentro de `TCalculoAcesso.ImportarMarcacoesRefeitorioRapido`? Esta unit só repassa a opção e o intervalo.
