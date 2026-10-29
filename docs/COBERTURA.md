# Cobertura e critérios de execução — 29/10/2026

| Camada | Situação | Evidência |
|---|---|---|
| Repositório fonte | Clonado, branch/commit/contagens registrados; somente leitura | [mapa_sistema.md](mapa_sistema.md) |
| Menus | 140 ações mapeadas em sete módulos; Trabalho tem oito rotas laterais documentadas | [mapa_sistema.md](mapa_sistema.md), [mapa_trabalho.md](mapa_trabalho.md) |
| Documentação de telas | 89 inventários estáticos com controles, tipo, máscara, padrão, mensagens literais e índice de procedures; mais fichas manuais prioritárias de Refeitório e Veículos | [catálogo geral](telas/README_catalogo_geral.md), [índice de Refeitório](telas/README_refeitorio.md) |
| Mapas pywinauto | 89 YAMLs para 89 forms; Veículos, Cadastro de Refeitórios e Cardápios validados no build 2.11.1, os demais pendentes | `src/automatiza/mapas/` |
| Biblioteca Robot | Ações genéricas, abertura automática pelo painel, popups, logs e evidência básica em falhas | `src/automatiza/tela_generica.py`, `src/automatiza/biblioteca_telas.py`, `src/automatiza/abertura_modulo.py` |
| Casos Robot | 92 testes declarados em `tests/telas/`; `--dryrun`: 92 PASS. Execução completa do `.bat`: 93 testes Robot, 6 PASS, 0 FAIL, 87 SKIP (inclui uma suíte antiga fora de `tests/telas/`). | `resultados/robot-telas/20261029-104645/` |
| Fumaça real de Veículos | PASS: abrir, Incluir, preencher Nome, Cancelar e fechar; três mensagens de validação também PASS | `resultados/robot-telas/20261029-103429/`, `resultados/robot-telas/20261029-103448/` |
| Validações de Refeitório e Cardápios | PASS: Nome vazio gera a mensagem esperada em ambos, repetido em duas rodadas; sem gravação | `resultados/robot-telas/20261029-104209/`, `resultados/robot-telas/20261029-104222/` |
| Reservas de Refeições | PASS: abrir pelo menu real, Incluir, Cancelar, fechar; sem gravação. Somente os dois botões usados estão liberados no mapa. | `resultados/robot-telas/20261029-105219/`, `docs/mapas-de-tela/refeitorio_tfrmrefeitorioviewsreservasrefeicoes-win32-20261029-105139-inclusao.txt` |
| Rodada completa posterior | 93 testes Robot: 7 PASS, 0 FAIL, 86 SKIP. O novo PASS é a fumaça de Reservas. | `resultados/robot-telas/20261029-105301/` |
| Rodada integral mais recente | 94 testes Robot: 12 PASS, 0 FAIL, 82 SKIP. Inclui quatro novas fumaças e a validação de Reserva sem pessoa. | `resultados/robot-telas/20261029-110144/` |
| Abertura autônoma | PASS: fumaça de Veículos rodou com módulo e painel previamente fechados; a biblioteca abriu ambos | `resultados/robot-telas/20261029-104607/` |
| Cenários com gravação e limpeza | Pendentes de ambiente funcional, confirmação do banco efetivo e autorização específica por cenário | [AGENTS.md](../Agents.md) |

`PASS` no `--dryrun` comprova apenas que as keywords e a sintaxe Robot estão conectadas. `SKIP` comprova que o bloqueio por mapa não validado funciona. Nenhum desses resultados demonstra comportamento correto do Acessus.

## Próximas verificações concretas

1. Repetir inspeção de controles nas demais telas de Refeitório e validar `found_index`/hierarquia no build instalado.
2. Aprofundar as fichas estáticas com procedures, controllers, DAOs e briefings de mudança. Incluir caminho feliz e limpeza apenas quando o banco efetivo e a regra esperada estiverem confirmados.
3. Estender evidências automáticas de SQL/serviços para os fluxos que os usam.
4. O módulo Trabalho aparece na fonte, mas `C:\acesso\Acessus.Trabalho.exe` não está instalado nesta máquina; seu mapa é somente estático.

## Telas ainda sem cobertura funcional

As telas do [catálogo](telas/README_catalogo_geral.md), exceto Veículos, Cadastro de Refeitórios e Cardápios, têm apenas esqueleto de teste. `TFrmSobre` não possui DFM nesta cópia. Os cadastros internos da aba Trabalho/EPIs não têm handlers ligados aos botões na fonte consultada. A lista nominal completa está no catálogo, evitando duplicação que ficaria desatualizada.
