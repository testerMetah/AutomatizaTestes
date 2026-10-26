# Pendências da CLI e do painel

- Credenciais de login automático da cópia do Acessus: configure `TESTE_USUARIO` e `TESTE_SENHA` no `.env`. Sem elas, a abertura automática deve recusar com mensagem clara; processos já autenticados podem ser reutilizados.
- Oráculo de contagem de Auditorias/Históricos: `docs/cenarios/` ainda não contém regra `CONFIRMADA` que associe os filtros da tela a uma consulta SQL de contagem. A suíte permanece exploratória nesses campos; nenhuma regra foi inventada.
