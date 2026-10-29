# AutomatizaTestes

## Suíte de telas por mapa YAML

`Rodar-Telas.bat` ativa o Python 32 bits da venv e executa as suítes Robot em `tests/`, excluindo cenários marcados `bloqueado`; gera `resultados/robot-telas/<data-hora>/log.html`. Exemplos: `Rodar-Telas.bat --tela estacionamento_cadastro_veiculos` e `Rodar-Telas.bat --tag smoke`. Se o módulo não estiver aberto, a biblioteca inicia `Acessus.Modulo.exe`, autentica com `TESTE_USUARIO` e `TESTE_SENHA` do `.env` local e abre o módulo pelo menu. Cada gesto é registrado no log; falhas criam `resultados/<data-hora>/<teste>/falha.txt` e screenshot quando a janela está disponível. Suítes com mapas ainda não validados aparecem como `SKIP`, nunca como aprovação da tela.

O mapa `src/automatiza/mapas/estacionamento_cadastro_veiculos.yaml` foi validado no build 2.11.1. Para validar outra tela, abra o módulo pelo `Acessus.Modulo.exe`, exporte a árvore real de controles e compare com o DFM. O exemplo `scripts/inspecionar_veiculos_ui.py` mostra como salvar `print_control_identifiers` em `docs/mapas-de-tela/`. Complete seletores (`found_index` quando necessário) e marque `validado_na_ui: true` somente após uma fumaça sem gravação. A biblioteca bloqueia interação com mapa não validado.

Para adicionar uma tela, use `python scripts/gerar_catalogo_telas.py` para criar o inventário inicial dos forms ligados ao menu, ou crie `src/automatiza/mapas/<nome>.yaml` com `form_class`, `principal_class`, `menu`, `backend` e `controles` lógicos. Em `tests/telas/<nome>.robot`, use `Abrir Tela`, `Preencher Campo`, `Clicar Controle`, `Ler Mensagem`, `Ler Grid` e `Fechar Tela`. O gerador preserva arquivos existentes. Resultados esperados de regras de negócio precisam ser confirmados no build atual antes de adicionar asserções de cadastro. Consulte [o catálogo estático](docs/telas/README_catalogo_geral.md) e [o diagnóstico da conexão](docs/DIAGNOSTICO-CONEXAO-20261029.md).

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
| Pausar ou cancelar um teste | **Execução ao vivo → Pausar / Continuar / Cancelar** | `Pause/Break` pausa/continua (alternativas: `Ctrl+Shift+F9` e `Ctrl+Shift+P`); `Ctrl+Shift+F10` pede confirmação para cancelar |
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

O CI executa somente `tests/unit` com Python Windows 32 bits. Cenários com as tags `desktop` e `banco` dependem da VM de teste. Os mapas volumosos em `docs/mapeamentos/` permanecem locais e não são versionados; o catálogo necessário ao explorador está em `config/rotas-explorador-211.json`.
# Testes exploratórios de Históricos e Relatórios

Execute `Rodar-Relatorios.bat` em uma sessão Windows interativa para testar todos os módulos com a cópia de teste dos executáveis de `C:\acesso`. Consulte [o guia de execução](docs/TESTES-EXPLORATORIOS-RELATORIOS.md) para resultados e execução por módulo.
