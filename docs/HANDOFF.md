# Handoff — 2026-10-23

## Estado

O projeto real fica em `C:\AutomatizaTestes`. Python 32 bits em `C:\python32b\venv32`. Acessus 2.11.1 em `C:\acesso`; banco destino `desk-tec/AcessoFagundes`; RH origem `desk-tec/RHFagundes`, ambos declarados como teste. O repositório de referência solicitado em `C:\Referencia\Acessus` não estava presente; não houve alteração nele. Leia `AGENTS.md` e `docs/CLAUDE-CODE-BRIEFING.md`.

Foi criado o motor de sequências YAML (`src/automatiza/sequencias/`), ações (`src/automatiza/acoes/`), gateway único de UI para as novas sequências (`src/automatiza/ui/`), suíte Robot e relatório de eventos. As sequências de leitura acessam SQL só com SELECT e observam a UI. CRUD/importação/reinício seguem BLOQUEADOS até seletor, regra, estratégia de limpeza e destino do serviço serem confirmados. O código legado ainda usa pywinauto fora do gateway; migrar tela por tela, sem reescrever cegamente.

Execução de 2026-10-23: 234 testes Python e 3 subtestes passaram; Robot teve 1 PASSOU, 0 FALHOU e 4 BLOQUEADOS. `scripts/verificar_ambiente.ps1` passou em todos os itens. A checagem de leitura mais recente está em `reports/20261023-094102-833899-9d7324/RELATORIO.html` e também exportou inventário da janela principal em `eventos.jsonl`.

## Decisões, pendências e riscos

Decisões: `docs/DECISOES.md`. Perguntas humanas: `docs/PERGUNTAS-ABERTAS.md`. Nenhum teste de escrita real foi executado nesta entrega. Não iniciar nem instalar Sync (`novo123`) ou Comunicação (`sm`) sem autorização; não modificar INIs, `C:\Referencia`, banco não confirmado ou UPDATE/DELETE sem filtro AUTOTEST_. O relatório é gerado mesmo quando casos ficam bloqueados. A pasta `reports/` é ignorada pelo Git por conter evidências possivelmente sensíveis.

O próximo passo recomendado é validar uma tela e uma regra de cadastro simples no build atual, criar dados com prefixo único e limpeza segura, ligar o backend real daquela entidade, depois acrescentar checkpoints de banco/tela. Não trate fonte antiga ou banco atual sozinho como regra confirmada. Para mudança nova, use `docs/mudancas/MODELO.md`.

## Execução

`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verificar_ambiente.ps1`; `$env:PYTHONPATH='C:\AutomatizaTestes\src'`; `C:\python32b\venv32\Scripts\python.exe -m automatiza.sequencias.cli`. Robot: `C:\python32b\venv32\Scripts\python.exe -m robot --outputdir reports\robot --include smoke tests\sequencias\suites.robot`. O HTML principal de cada sequência fica em `reports/<data-hora>/RELATORIO.html`.

## Permissões Claude Code

Não foi criado `.claude/settings.json` porque o formato de permissão da versão local não foi verificado. Fluxos estão em `docs/FLUXOS.md`. Exigir aprovação para comandos de serviço e SQL de escrita; impedir comandos destrutivos fora de `reports/`. Consultas devem usar SELECT parametrizado e confirmar DB_NAME().
