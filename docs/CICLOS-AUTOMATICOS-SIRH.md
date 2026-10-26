# Ciclos automáticos de CRUD e importação SIRH

O executor gera sequências de operações, altera os dados pela interface do RH e confere origem, API e Acessus. Não precisa de um agente de IA para executar as etapas.

## Executar

Na pasta `C:\AutomatizaTestes`, usando a instalação Python do projeto:

```powershell
# Gerar ordens reproduzíveis; não altera dados.
.\.venv\Scripts\python.exe -m automatiza.ciclos_cli planejar `
  --arquivo examples/ciclos-sirh.json `
  --saida reports/ciclos/plano-211.json --semente 211 --rodadas 3

# Executar o plano; este comando altera os registros de teste descritos nele.
.\.venv\Scripts\python.exe -m automatiza.ciclos_cli executar `
  --arquivo reports/ciclos/plano-211.json `
  --saida reports/ciclos/execucao-211
```

Para retomar uma execução interrompida, repetir o segundo comando com **o mesmo plano e a mesma pasta**. Para executar outro plano, usar outra pasta. A semente define a ordem; alterar a semente produz outra combinação.

Para executar uma série de ordens diferentes automaticamente:

```powershell
.\.venv\Scripts\python.exe -m automatiza.ciclos_cli suite `
  --arquivo examples/ciclos-sirh.json `
  --saida reports/ciclos/suite-211 `
  --semente 211 --sementes 5 --rodadas 3
```

Cada semente ganha sua própria pasta e diário. A série só inicia a próxima ordem quando férias e ocorrências retornaram ao estado-base. Um defeito de importação fica registrado e a série continua; erro de interface interrompe a execução.
Casos marcados `presente=false` são criados na primeira semente e reutilizados como
existentes nas sementes seguintes. O manifesto de exemplo inclui a ocorrência
criada no piloto em 01/03/2027; como é futura em 21/10/2026, a API deve apresentá-la e o
filtro de vigência observado deve deixá-la fora dos afastamentos do Acessus.

## Sequências programadas

Cada caso pode seguir ordens como:

- Alterar → importar → importar novamente → excluir → importar → cadastrar novamente → importar.
- Excluir → importar → cadastrar → importar → alterar → importar → restaurar → importar.
- Alterar → importar → restaurar → importar → excluir → importar → cadastrar → importar duas vezes.

Casos inicialmente ausentes começam com cadastro e importação. Os casos são intercalados sem violar a dependência entre as operações. Ao terminar normalmente, os registros ficam presentes com o término-base do manifesto. Não há limpeza cega após erro: uma divergência de origem bloqueia o caso e preserva as evidências.

O manifesto utiliza poucos registros sintéticos já existentes. A criação posterior à exclusão é um novo cadastro pela interface. Para testar uma chave adicional, adicionar um caso com `presente=false`, início ainda inexistente e períodos explícitos. O executor recusa sobrescrever uma origem que difere do estado esperado.

## Diário e resultados

Cada execução grava:

- `plano.json`: semente, casos e ordem completa.
- `estado.json`: posição de retomada e operação pendente.
- `diario.txt` e `diario.jsonl`: horário, ação, expectativa, observação e resultado.
- `relatorio.html`: leitura do diário no navegador, sem servidor.
- `etapa-NNNN.png`: tela do registro antes da confirmação; exclusão inclui a confirmação.

Uma etapa de importação acompanha o serviço automático já configurado. Consulta a API com paginação, verifica períodos, pessoa, quantidade, causa e IDs no Acessus e exige conclusão de ciclo posterior ao início da observação. Ausência momentânea no banco, sozinha, não aprova exclusão. O log do serviço é usado somente como sinal de ciclo; seu conteúdo bruto não é copiado.

Falhas de negócio, como `FÃ©rias`, ficam registradas e o ciclo continua. Divergência na origem, layout inesperado ou confirmação não reconhecida bloqueiam o caso. Erros de execução conservam a operação pendente. Na retomada, se o efeito já estiver na origem, a ação é registrada como recuperada e não é repetida.

## Ambiente e credenciais

- SQL usa as configurações existentes do projeto; todas as consultas de conferência são de leitura.
- Confere banco configurado no importador, pessoa/contrato e alias ativo do RH.
- Seleciona a unidade explicitamente na interface.
- Senha API é lida de `SIRH_TEST_PASSWORD` ou da credencial `AutomatizaTestes/SIRH` do cofre Windows do usuário. Não é salva em manifesto/diário.
- Nesta VM, o cofre foi configurado com a credencial já fornecida pelo usuário.
- O manifesto explicita a exceção TLS apenas para consultas diagnósticas ao servidor atual. Não altera TLS do Windows ou do Acessus.
- O adaptador de tela atual exige a resolução/layout de 1280 pixels validado nesta VM. Não depende de handles da sessão anterior.
- Uma trava impede dois executores do projeto de operarem a interface simultaneamente.

## Cobertura e limites

O executor e o adaptador implementam criar, alterar término, excluir e recriar férias,
ocorrências em dias e ocorrência 013 na modalidade `Faixa Horas`. O manifesto traz
08:15–12:45 e 23:30–01:30 no dia seguinte, ambas validadas em pilotos reais. A
lista de tipos não significa que todos os formulários especiais de ocorrência foram
validados: tipos que exigem informações médicas adicionais precisam de adaptador
específico antes da utilização.

Reservas participam do plano, mas a instalação atual não publica endpoint API correspondente. O adaptador registra `BLOQUEADO` antes de modificar uma reserva. Isso preserva a diferença entre fluxo disponível e fluxo aprovado; não troca silenciosamente para SQL.

Ocorrências horárias de outros códigos são bloqueadas pelo adaptador até que tenham
mapeamento próprio. A ocorrência 013 não gera afastamento; os pilotos conferiram
presença e horário na API e ausência no Acessus após ciclos completos do serviço.

Os testes unitários usam backend simulado para validar sequenciamento, interrupção, retomada, divergência externa e tratamento de falhas. São distintos das execuções reais em `reports/ciclos-dev/piloto-real-v5`, `piloto-ferias-reserva` e `piloto-ocorrencia-nova`.

## Pilotos reais em 21/10/2026

`piloto-real-v5` concluiu as nove etapas da ocorrência vigente 011: alteração,
importações, exclusão com remoção posterior no destino, recadastro e nova importação.
A retomada reconheceu um recadastro já gravado na origem e não o repetiu. O resultado
final foi `PASSOU`; o diário preserva as interrupções e correções de interface.

`piloto-ferias-reserva` concluiu 18 etapas com ressalvas. A exclusão da férias
retirou o afastamento do destino após um ciclo; recadastro e alterações de término
foram refletidos com períodos corretos. A causa continuou incorreta no Acessus
(`FÃ©rias` em vez de `Férias`) em quatro verificações. Reserva foi bloqueada antes
de qualquer alteração porque a API publicada não contém rota de reservas.

`piloto-ocorrencia-nova` concluiu 11 etapas com `PASSOU`: cadastro realmente novo e
futuro, alteração, restauração, exclusão, recadastro e importações repetidas. A API
acompanhou cada estado; o Acessus não criou afastamento para essa data futura.
Consultar `estado.json` e `diario.txt` dessa pasta para cada observação e ciclo.

`piloto-ocorrencia-horaria` concluiu 10 etapas com `PASSOU` para 03/11/2026,
08:15–12:45 (alterado temporariamente para 13:15). `piloto-ocorrencia-virada`
concluiu 8 etapas com `PASSOU` para 04/11/2026 23:30 até 05/11/2026 01:30
(alterado temporariamente para 02:00). Ambos incluem exclusão, recadastro e
importações. Os diários registram uma interrupção de layout no primeiro e duas
desconexões do operador no segundo; a retomada conferiu a origem antes de escrever.
