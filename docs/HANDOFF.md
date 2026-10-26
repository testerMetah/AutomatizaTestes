# Handoff — 2026-10-23

## Atualização de 26/10/2026 — CLI e painel autônomos

### Ajuda contextual do painel

O painel agora lê `src/automatiza/painel_ajuda.json`: textos dos ícones ⓘ, glossário, resumos de cada tela e cartões do Catálogo de Testes. O menu destaca o catálogo; filtros por tipo, risco e busca ajudam a escolher. Os cartões mostram também o que cada teste não cobre. Casos legados sem formulário seguro no site exibem o comando real e o motivo pelo qual o botão Executar está desabilitado. `tests/unit/test_painel_ajuda.py` verifica cobertura e textos sem uso. O guia em `docs/GUIA-DE-USO.md` explica como acrescentar novas chaves. Mensagens de erro do site usam linguagem direta e guardam detalhes técnicos em área recolhida.

O projeto agora tem `Abrir-Painel.bat` e `automatiza.nova_cli` como entrada única. A CLI anterior permanece disponível para comandos históricos. Os perfis `profiles/auditorias.json` (`AcessoFagundes`, cópia `C:\AcessusHostFisico`) e `profiles/sequencias.json` (`Acessus_AUTOTEST_20261023`, instalação principal) substituem o banco fixado na suíte cronológica. A checagem `automatiza ambiente` valida bitness, executáveis, INIs, ODBC, SQL e serviços; `automatiza comandos` imprime o catálogo usado pelo painel.

O supervisor de Auditorias/Históricos encontra PID pelo executável, abre painel/login com credenciais locais, navega, monitora processo/janela/diário, retoma tentativas concluídas após travamento e gera `RELATORIO.html`. Os dois logs permanentes mantêm formato e modo de acréscimo. O painel serve apenas em `127.0.0.1`, oferece execução ao vivo, resultados, build, perfis e confirmação de escrita com `DB_NAME()`. Ações de escrita em ciclos também verificam destino do manifesto/plano contra o perfil; o exemplo antigo `novo123` é bloqueado. O processo filho recebe o servidor e banco já validados pelo perfil.

Documentação nova: `docs/GUIA-DE-USO.md`, `docs/ARQUITETURA.md`, `CLAUDE.md`; pendências em `docs/PENDENCIAS.md`. A suíte isolada e rotas HTTP foram testadas. Em 26/10, `automatiza ambiente` e `automatiza comandos` passaram. Uma rodada real `--modulo todos --filtro Per` consultou Acesso, Refeitório, Portaria, Estacionamento e Administração. A Escola estava bloqueada por aviso modal “Turno não cadastrado”; o supervisor foi ajustado para registrar a caixa e reiniciar o módulo. A rodada `resultados/smoke-cli-escola-20261026` levantou 7 históricos/30 filtros e concluiu 35 tentativas CONSULTADO. O login desde sessão fechada e a varredura completa de filtros não foram validados nesta entrega. Os parágrafos abaixo são histórico anterior e podem citar o banco antigo.

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

## Continuacao apos base isolada (23/10/2026, 10:16)

O destino antigo descrito acima e historico. Destino atual: `desk-tec/Acessus_AUTOTEST_20261023`, confirmado como teste. Os tres servicos e o Acessus usam esse banco; RH usa `RHFagundes`. A base tem schema sem dados, empresa e administrador iniciais criados no assistente, conexao SQL de origem salva, zero pessoas/unidades/coletores e nenhuma configuracao API. `TFConfigAPI` exige um coletor. Nao criar coletor associado a dispositivo real sem saber impacto.

O atualizador tentou 415 scripts sobre schema atual e reportou erros; auditar. Tres servicos Running; log da API informa `DADOS_IMPORTACAO_API` vazia, sem importacao. Sync exigiu login administrativo antes de iniciar. `scripts/verificar_ambiente.ps1` passou em todos os itens. Robot: 1 PASSOU, 0 FALHOU, 4 BLOQUEADOS. Relatorio: `reports/robot-nova-base/report.html`; checagem detalhada: `reports/20261023-101611-015292-092edd/RELATORIO.html`. Proximo passo: coletor seguro de teste, salvar API, verificar importacao, criar fixture pessoa/unidade e validar soft delete.

## Pausa e avisos (26/10/2026)

A sentinela registra Pause/Break como atalho principal, com Ctrl+Shift+F9 e Ctrl+Shift+P como alternativas. O teste de integracao com SendInput e laco falso mediu 156 ms entre o pedido e a confirmacao de pausa cooperativa; retomada apos 375 ms. A validacao isolada com Acessus ainda esta pendente porque uma rodada do painel (`auditorias --modulo todos --extremo`) ja controlava a area de trabalho durante os ensaios.
