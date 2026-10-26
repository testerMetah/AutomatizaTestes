# Pendências da CLI e do painel

- Credenciais de login automático da cópia do Acessus: configure `TESTE_USUARIO` e `TESTE_SENHA` no `.env`. Sem elas, a abertura automática deve recusar com mensagem clara; processos já autenticados podem ser reutilizados.
- Oráculo de contagem de Auditorias/Históricos: a infraestrutura lê apenas regras `status: CONFIRMADA` com `auditorias_contagens` em `docs/cenarios/`, mas ainda não existe regra desse tipo confirmada pelo Gabriel. A suíte permanece exploratória nesses campos; nenhuma regra foi inventada.
- Login automático a partir de sessão fechada e retomada específica após `Access violation` ainda não foram provocados nesta entrega. A sessão já estava autenticada. Uma rodada real com `--modulo todos --filtro Per` consultou cinco módulos; a Escola tinha aviso modal remanescente, e uma rodada posterior demonstrou captura, reinício do módulo e 35 novas tentativas CONSULTADO. A varredura completa de todos os filtros e a retomada após violação de acesso ainda precisam de uma rodada dedicada.
- Manifesto de exemplo `examples/ciclos-sirh.json` aponta para `novo123`, diferente do perfil de teste atual. A CLI bloqueia `executar`/`suite` até preparar manifesto/plano para banco de teste confirmado e validar a regra/dados.
- Alguns scripts legados de mapeamento, integração e inspeção ainda exigem argumentos próprios (por exemplo PID, sessão ou plano) e não têm formulário seguro no painel. Foram inventariados no Catálogo com comando, pré-requisitos e risco; o botão Executar fica desabilitado com explicação. Para habilitá-los no site, crie um formulário específico e validação do banco/PID antes de chamar o script.

## Validacao da pausa na VM (26/10/2026)

- Uma rodada do painel `auditorias --modulo todos --extremo` ja estava em execucao e clicava no Acessus. Duas auditorias curtas tentadas (`administracao` e `refeitorio`, filtro `Per`) disputaram o foco e nao validam aviso, realinhamento nem cancelamento. Repetir uma unica rodada curta quando o painel estiver ocioso, observando o foco, o dialogo, a tecla que nao chega ao Acessus, ausencia de teclas presas e o relatorio parcial apos cancelar.
- O teste de integracao isolado com SendInput confirmou pausa cooperativa em 156 ms, mas a mesma sessao desktop tinha a rodada acima. Medir novamente sem concorrencia para concluir o limite de 1,5 s no Acessus real.
