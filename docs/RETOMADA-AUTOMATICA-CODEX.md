# Retomada automática do Codex — 20/10/2026

Configurada e comprovada por uma interrupção real de cota nesta conversa.
A tarefa vigente é configurar esta retomada; a inspeção do Acessus ficou
preservada e não foi reiniciada durante a configuração.

## Instalação e operação

- Codex CLI existente: 0.163.0; Python existente: 3.12. Nenhuma dependência
  adicional instalada. Assinaturas Authenticode dos executáveis Codex,
  python.exe e pythonw.exe verificadas como válidas.
- Código: `scripts/codex_auto_resume.py`; gerenciamento:
  `scripts/configurar-retomada-codex.ps1`.
- Cópia executada, configuração e diagnóstico em
  `%LOCALAPPDATA%\CodexAutoResume`. Não contém cópias de senhas ou auth.json.
- Tarefa do Windows: `CodexAutoResume-AutomatizaTestes`, usuário autom,
  sessão interativa, privilégio normal. Gatilhos no login e a cada cinco
  minutos; uma única instância, sem janela. Não configura login automático.
- Conversa vinculada: `01a15515-452d-70b1-a0b6-dae8f534facf`,
  diretório `C:\AutomatizaTestes`. Não seleciona outra conversa por `--last`.

O supervisor usa o proxy local do app-server oficial, com WebSocket e JSON-RPC.
Lê o erro oficial `usageLimitExceeded` e os limites reais da conta. Aguarda
as janelas esgotadas e consulta novamente antes de acrescentar um turno à
mesma conversa. Não altera conta, modelo, autenticação, permissões ou créditos.
Não abre porta TCP nem responde automaticamente a pedidos de aprovação/login.

O novo turno recebe instruções para conferir processos e operações parciais
antes de repetir ações. Resposta final `continuar` permite outro turno;
`concluido` encerra o trabalho; `precisa_usuario` suspende a continuação.
Interrupção manual reconhecida e falhas sem relação com cota também suspendem.
Não gera enquanto outro turno está ativo. O arquivo de lock é exclusivo deste
supervisor, sem alterar locks nativos do Codex.

## Evidências reais

Horários locais de São Paulo:

- 19/10 às 15:37:47: supervisor registrou `aguardando_cota`.
- Turno `01a1556c-ea2a-7711-981f-7c73d7af2eac` foi confirmado na API local
  como `failed`, com classificação `usageLimitExceeded`.
- Próxima consulta prevista após a janela: 19/10 às 18:23:47.
- Última inicialização do Windows informada pelo sistema: 20/10 às 08:09:40.
- 20/10 às 08:14:13: registro `retomado`, turno
  `01a15904-dc10-7dd3-b20e-2871eb582473`, nesta mesma conversa.
- Consulta somente de leitura confirmou esse turno ativo e a cota disponível.
  Não houve simulação de renovação nem compra/reset de créditos.
- Atualização do supervisor durante o turno preservou seu ID e manteve uma
  única instância. Hash da cópia instalada conferido com o código do projeto.
- Desativação e reativação reais testadas: tarefa passou de Disabled para
  Running, mantendo o turno original e somente um pythonw.exe supervisor.
  SHA256 do controlador instalado e do código, iguais:
  `53CC710FE0C42AA17F67351EE36E427B3D4FED1B1DA7CBB9E1B1E0C05312A785`.
- `python -m pytest tests/unit/test_codex_auto_resume.py -q -p no:cacheprovider`:
  10 testes aprovados, três subcasos aprovados. São testes locais de decisões;
  não constituem prova dos fluxos de negócio Acessus/RH.

Os registros privados `events.jsonl` e `state.json` guardam IDs e estados,
sem persistir o texto da conversa. O histórico original continua no Codex.
A retomada após uma inicialização do Windows foi observada; não foi provocado
outro reboot para testes, nem prometida execução durante desligamento/suspensão.

## Limites e intervenção

Retomar significa abrir outro turno na mesma conversa, com seu histórico e
arquivos; não recuperar uma instrução de CPU ou uma transação de aplicação
interrompida. Janelas, conexões SQL e operações externas precisam ser conferidas.
Após reboot, exige login normal do usuário e área de trabalho desbloqueada.
Autenticação expirada, aprovação, erro de protocolo ou dependência de negócio
podem exigir intervenção. Não desbloqueia Windows nem contorna UAC ou limites.

O transporte foi validado na versão instalada. Atualizações futuras do Codex
podem mudar o protocolo; falhas de conexão são registradas sem presumir sucesso.
Recuperação de cota persistida após reboot foi comprovada; outros tipos de queda
no meio de uma operação não foram integralmente testados. Não usar a automação
como garantia de gravação exatamente uma vez em sistemas externos.

Após `concluido`/`precisa_usuario`, o supervisor fica sem continuar a tarefa.
Para autorizar uma nova tarefa nesta conversa, dar a instrução no Codex e
reativar pelo comando abaixo. Não vincula automaticamente novas conversas.

## Comandos

No PowerShell, dentro de `C:\AutomatizaTestes`:

```powershell
# Ver estado
.\scripts\configurar-retomada-codex.ps1 -Acao Status
# Desativar novas retomadas
.\scripts\configurar-retomada-codex.ps1 -Acao Desativar
# Reativar nesta conversa, após resolver uma dependência
.\scripts\configurar-retomada-codex.ps1 -Acao Ativar
# Remover tarefa, preservando arquivos de auditoria
.\scripts\configurar-retomada-codex.ps1 -Acao Remover
```

Se a política bloquear o script, usar apenas para essa execução:
`powershell -NoProfile -ExecutionPolicy Bypass -File scripts\configurar-retomada-codex.ps1 -Acao Desativar`.
A instalação não altera a política permanente. Desativar não cancela um turno
do Codex já iniciado; para isso usar a interrupção normal no próprio Codex.

Referências oficiais consultadas:
[app-server](https://learn.chatgpt.com/docs/app-server) e
[execução não interativa](https://learn.chatgpt.com/docs/non-interactive-mode).
O esquema local gerado pelo CLI instalado orientou a compatibilidade efetiva.
