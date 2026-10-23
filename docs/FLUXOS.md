# Fluxos para Claude Code ou terminal

Os arquivos `.claude/commands/*.md` usam o formato simples de comando por arquivo. A política exata de permissões do Claude Code não foi confirmada nesta instalação; portanto não foi criado `.claude/settings.json`. Ao usar qualquer assistente, aprovar manualmente somente consultas e leitura; exigir confirmação para `sc start/stop/delete`, SQL de escrita, alterações de INI e ações destrutivas fora de `reports/`.

1. **Verificar ambiente:** na raiz, ative a venv 32 bits; rode `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verificar_ambiente.ps1`; abra `docs/HANDOFF.md`.
2. **Testar mudança:** leia `docs/mudancas/MODELO.md`, o briefing da mudança e `docs/cenarios/`; liste cenários, execute smoke/regressão e guarde evidências.
3. **Rodar sequência:** `$env:PYTHONPATH='C:\AutomatizaTestes\src'`; `python -m automatiza.sequencias.cli --arquivo tests/sequencias/checagem_leitura.yaml` ou `--seed 42 --passos 8`.
4. **Gerar relatório:** o CLI e Robot já geram `reports/<data-hora>/RELATORIO.html`; leia `resumo.json` e `eventos.jsonl` da mesma pasta. Não edite eventos após execução.

