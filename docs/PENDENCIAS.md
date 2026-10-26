# Pendências da CLI e do painel

- Credenciais de login automático da cópia do Acessus: configure `TESTE_USUARIO` e `TESTE_SENHA` no `.env`. Sem elas, a abertura automática deve recusar com mensagem clara; processos já autenticados podem ser reutilizados.
- Oráculo de contagem de Auditorias/Históricos: a infraestrutura lê apenas regras `status: CONFIRMADA` com `auditorias_contagens` em `docs/cenarios/`, mas ainda não existe regra desse tipo confirmada pelo Gabriel. A suíte permanece exploratória nesses campos; nenhuma regra foi inventada.
- Validação ponta a ponta de login, abertura de todos os módulos e retomada após `Access violation`: depende da sessão Windows com a cópia da build disponível e credenciais locais configuradas. Foram feitos testes unitários e de rotas HTTP, mas a execução completa de interface não deve ser declarada aprovada sem uma rodada real.
- Manifesto de exemplo `examples/ciclos-sirh.json` aponta para `novo123`, diferente do perfil de teste atual. A CLI bloqueia `executar`/`suite` até preparar manifesto/plano para banco de teste confirmado e validar a regra/dados.
