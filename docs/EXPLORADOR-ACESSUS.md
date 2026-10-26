# Explorador automático de telas do Acessus

O comando `automatiza.explorador_cli` abre módulos e formulários, descobre
controles habilitados, experimenta valores e cliques em sequências reproduzíveis
e escreve o passo a passo em `passos.log` e `passos.jsonl`. Ele funciona sem IA
durante a execução.

## Preparar o plano

```powershell
cd C:\AutomatizaTestes
.\.venv\Scripts\python.exe -m automatiza.explorador_cli gerar-config `
  --incluir-pendentes --saida examples\meu-explorador.json
```

O arquivo [exemplo](../examples/explorador-acessus-2111.json) já contém 72 rotas
candidatas dos seis módulos. A origem é o mapa da versão 2.11.0; ainda não foi
validada na 2.11.1. A geração exclui comandos de menu imediatos como Sair,
Excluir, Gerar, Importar e Exportar. Rotas pendentes podem falhar ao abrir e o
diário registrará a falha.

Edite `valores` para usar dados próprios de teste. Use `regras_campos` quando um
campo exigir valor específico, por exemplo:

```json
"regras_campos": [
  {"classe": "TEdit", "id_controle": 12345, "valores": ["ABC", "123"]},
  {"rotulo_regex": "Data", "valores": ["21/10/2026"]}
]
```

`id_controle` e legenda precisam ser conferidos na tela real. O explorador não
digita em controles com estilo de senha nem usa valores existentes da tela como
dados de teste. Com `exploracao.combo_auto=true`, ele também testa até
`max_opcoes_combo` opções oferecidas pelo próprio controle. O plano de exemplo
entra no estado de inclusão dos cadastros antes de descobrir os campos.

## Executar

O Windows precisa estar em sessão interativa, com login do Acessus disponível.
O explorador abre o Painel de Módulos se necessário, usa os menus dos módulos e
confere que a instalação continua na versão 2.11.1.0 e o importador aponta para
`desk-tec/novo123`. Use uma pasta de saída nova por execução:

```powershell
.\.venv\Scripts\python.exe -m automatiza.explorador_cli executar `
  --arquivo examples\explorador-acessus-2111.json `
  --saida reports\explorador\execucao-001
```

Cada ação elegível é tentada sozinha. O planejador também testa pares em ordens
diferentes e caminhos aleatórios; `semente` torna a ordem reproduzível. Ajuste
`limites` para ampliar ou encurtar a execução. Não é possível percorrer todas as
ordens matematicamente possíveis de dezenas de controles; o limite e a ordem
realizados ficam no diário. Um formulário é reaberto entre sequências. Após cada
sequência, o executor tenta Cancelar/Fechar e recusa continuar se não conseguir
voltar a um estado conhecido.

## Validação dos resultados

Depois de preencher texto, selecionar uma opção, alterar data/hora ou alternar
checkbox/radio, o executor lê o controle novamente e compara com o valor esperado.
O diário registra `VALIDACAO_APROVADO`, `VALIDACAO_FALHOU` ou
`VALIDACAO_NAO_VERIFICADO` para cada ação. Diálogos bloqueadores são registrados
com a mensagem exibida e dispensados automaticamente quando há resposta segura.

Ao fim da execução, `validacao-resumo.md` e `validacao-resumo.json` mostram todas
as rotas planejadas, inclusive as que não abriram, e contam verificações, falhas,
ações sem validação e erros de execução. Uma diferença observada pode ser uma regra
intencional do sistema: por exemplo, o piloto mostrou que o campo Empresa transforma
`abc` em `ABC`. O diário preserva esperado e observado para análise.

Essa validação prova o estado visível após cada ação. Gravação, cancelamento no
banco e regras de negócio exigem casos específicos com dados de teste e resultados
esperados conhecidos; o relatório não declara essas ações aprovadas sem essa prova.

## O que o diário registra

- Horário, módulo, rota, sequência e ação.
- Menu ou controle acionado: classe, ID, legenda e posição observados.
- Cada valor de teste enviado a um campo, antes e depois da tentativa.
- Janela observada após a ação, erro da biblioteca ou do aplicativo e ações de
  recuperação.
- Controles ignorados e motivo, incluindo limite de ações e botões não
  autorizados.

`estado.json` registra sequências concluídas e uma ação pendente. Repetir o mesmo
comando e pasta retoma sequências concluídas sem repeti-las. Se havia ação pendente
na interrupção, a retomada para e exige conferência da tela antes de prosseguir.
Capturas de erro ficam desativadas por padrão para não exportar dados pessoais;
`politica.capturar_erros=true` permite salvá-las.

## Política de cliques

O exemplo entra em Inclusão, preenche campos, altera controles de seleção,
percorre abas e descarta a edição com Cancelar. Ele clica apenas em botões de
navegação/cancelamento durante as sequências.
Botões que podem gravar, excluir, importar, exportar, gerar, imprimir ou enviar
precisam de configuração explícita em uma base descartável:

```json
"politica": {
  "permitir_gravacao": true,
  "base_descartavel_confirmada": true,
  "botoes_autorizados": ["Salvar", "Excluir"],
  "capturar_erros": false
}
```

`botoes_autorizados: ["*"]` habilita todos os botões detectados, inclusive
botões sem legenda; use somente em ambiente preparado para receber qualquer
alteração. O explorador não restaura dados gravados pelo Acessus. Para testes de
CRUD com restauração e conferência de integração, use os
[ciclos SIRH](CICLOS-AUTOMATICOS-SIRH.md).

## Estado de validação

O planejador, o diário, a retomada e o tratamento de erro foram verificados com
backend simulado. Um piloto na versão 2.11.1 completou 15 sequências na tela
Cadastros > Pessoas, preenchendo campos em Inclusão, alternando checkbox e
percorrendo aba. O piloto com validação completou 15 sequências na tela Empresa,
com 22 verificações aprovadas e duas diferenças de maiúsculas registradas. A
execução completa validada de 72 rotas está registrada no caminho apontado por
`reports/explorador/EXECUCAO-VALIDADA-ATUAL.txt`; consulte `estado.json`,
`passos.log` e, ao terminar, `validacao-resumo.md` nessa pasta.
Controles Delphi que mudam de posição, grades, árvores, diálogos não reconhecidos,
campos médicos e equipamentos podem exigir adaptadores adicionais. O relatório
registra essas lacunas como erro ou controle ignorado; não as chama de aprovação.
