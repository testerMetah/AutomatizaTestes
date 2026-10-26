# AutomatizaTestes

Automação local do **Acessus** (desktop Delphi/VCL), RH Metadados/Frequência e SQL Server. O caminho principal é o [Painel de Testes](Abrir-Painel.bat): abra com duplo clique na sessão Windows em que você usa o Acessus. Ele funciona sem internet e mostra o banco de teste, os comandos executados, a saída ao vivo e as evidências.

## Quero fazer…

| Tarefa | No painel | Na CLI |
| --- | --- | --- |
| Conferir o ambiente | **Início → Rodar checagem** | `automatiza ambiente` |
| Testar históricos e filtros | **Auditorias/Históricos → Executar** | `automatiza auditorias --modulo refeitorio` |
| Testar os seis módulos | Escolha **todos** | `automatiza auditorias --modulo todos` |
| Incluir entradas extremas | Marque **Variações extremas** | `automatiza auditorias --modulo escola --extremo` |
| Ver falhas e screenshots | **Resultados** | Abra `resultados/<rodada>/RELATORIO.html` |
| Ver cada ação em ordem | **Resultados → Logs permanentes** | Abra `resultados/passo-a-passo.log` |
| Pausar ou cancelar um teste | **Execução ao vivo → Pausar / Continuar / Cancelar** | `Pause/Break` (alternativas: `Ctrl+Shift+F9` e `Ctrl+Shift+P`) |
| Aprender todos os comandos | **Comandos** | `automatiza comandos` |

O [Guia de Uso](docs/GUIA-DE-USO.md) explica cada tarefa, perfil, aviso, relatório e opção. A [Arquitetura](docs/ARQUITETURA.md) descreve as partes internas e como evoluir o projeto. Leia [AGENTS.md](AGENTS.md) antes de modificar testes.

## Primeira auditoria

1. Abra [Abrir-Painel.bat](Abrir-Painel.bat). O painel usa `C:\python32b\venv32` (Python **32 bits**) e abre em `127.0.0.1`; feche a janela de console para encerrar.
2. Em **Início**, confira Python, executável, INIs, SQL e serviços. Erros aparecem com motivo.
3. Em **Auditorias/Históricos**, escolha módulo e perfil `auditorias`. O banco desse perfil é `desk-tec/AcessoFagundes`, confirmado como teste. Mantenha a sessão Windows desbloqueada.
4. Clique **Executar**. O painel localiza ou abre o módulo, entra com a conta de teste configurada no `.env`, abre a tela, mapeia seus controles e executa as tentativas. A página **Execução ao vivo** mostra o progresso.
5. Em **Resultados**, abra o relatório da rodada e os logs permanentes. As imagens de erro mostram o diálogo antes de ele ser fechado.

Para abertura automática, configure `TESTE_USUARIO` e `TESTE_SENHA` **somente** no `.env` local, usando [.env.example](.env.example). Se o módulo já estiver autenticado, ele pode ser reutilizado. Nenhuma senha vai para código, documentação ou relatório.

## Dois bancos de teste, dois perfis

- `profiles/auditorias.json`: executáveis em `C:\AcessusHostFisico`, banco `desk-tec/AcessoFagundes`.
- `profiles/sequencias.json`: instalação principal em `C:\acesso`, banco `desk-tec/Acessus_AUTOTEST_20261023`.
- Origem RH: `desk-tec/RHFagundes`.

Os testes de escrita exigem `--confirmo-escrita` na CLI ou confirmação do **banco efetivo** no painel. O projeto verifica `DB_NAME()` e a lista de bancos de teste permitidos. Não use produção.

## Instalar ou atualizar a CLI

No ambiente já preparado, a CLI é instalada pelo entry point do [pyproject.toml](pyproject.toml):

```powershell
& 'C:\python32b\venv32\Scripts\python.exe' -m pip install -e . --no-deps
& 'C:\python32b\venv32\Scripts\automatiza.exe' comandos
```

Use `--no-deps` apenas quando as dependências do projeto já estiverem instaladas nessa venv. O painel e a CLI recusam Python que não seja 32 bits. Scripts antigos continuam disponíveis para manutenção, mas o uso diário começa no painel.

## Evidências e limites

`resultados/passo-a-passo.log` e `resultados/passo-a-passo-detalhado.jsonl` são **permanentes**, escritos pelo projeto em modo de acréscimo. Cada rodada tem `tentativas.jsonl`, screenshots, `resumo.json` e `RELATORIO.html`. Outros fluxos gravam em `reports/`. Essas pastas ficam fora do Git.

Auditorias/Históricos é principalmente uma suíte **exploratória**: detecta erros, travamentos, mensagens e contagens. Quando houver regra de contagem `CONFIRMADA` em `docs/cenarios/`, o oráculo poderá declarar `PASSOU` ou `FALHOU`; hoje não há regra desse tipo confirmada. O motor genérico Robot tem ações de escrita ainda bloqueadas. Consulte [Pendências](docs/PENDENCIAS.md) e [Handoff](docs/HANDOFF.md).
