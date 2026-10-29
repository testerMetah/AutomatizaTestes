# Estado da documentação e da automação do Acessus

Atualizado em 29/10/2026. Este arquivo permite retomar o trabalho sem o histórico da conversa.

## Objetivo e limites

Gabriel quer documentar o Acessus a partir de `C:\Acessus-Fonte` (somente leitura) e preparar `C:\AutomatizaTestes` para testes Robot/pywinauto genéricos. O código do GitHub pode não corresponder ao executável instalado. Priorizar briefings em `docs/mudancas/`, observação da UI e schema do banco de teste para confirmar resultados esperados. Não alterar a fonte nem escrever em banco fora de cenário autorizado.

## Feito

- Etapa 0: repositório clonado em `C:\Acessus-Fonte`, branch `main`, commit `28074ddf2c3ecae913fd082d453027f148dc50c6` de 28/10/2026 por MetahDev02; 704 `.pas` e 312 `.dfm` versionados. A cópia permanece sem alterações.
- Etapa 1: [mapa_sistema.md](mapa_sistema.md) contém 140 itens acionáveis nos `TActionManager` de Acesso, Administração, Escola, Estacionamento, Módulo, Portaria e Refeitório. Foram ligadas 90 classes de tela distintas por `TelaShow` ou criação modal. `Trabalho` usa navegação customizada e ainda não foi mapeado por completo. `scripts/gerar_mapa_fonte.py` regenera o mapa.
- Etapa 2 em andamento: [índice de Refeitório](telas/README_refeitorio.md) liga os itens do menu às fichas. Há análise manual de Cadastro de Refeitórios, Cardápios, Incluir Refeições, Importar Refeições, Reservas de Refeições, Cadastro de Veículos e das bases `TFrmPadrao`/`TFrmRelPadrao`. Seis relatórios e dois cadastros de coletores têm inventário com notas de fluxo e validações. As demais fichas de Refeitório são inventários estáticos de DFM/PAS, gerados por `scripts/extrair_telas_refeitorio.py`; **não são documentação de regra concluída**.

## Pendências prioritárias

1. Concluir leitura manual das fichas marcadas `Inventário estático` no índice de Refeitório: identificar validações, mensagens completas, dependências e efeitos de cada ação.
2. Completar leitura dos modelos e DAOs de Refeitório e Veículos para confirmar restrições de unicidade, transações e vínculos com TAGs. Já foi confirmado no código que os três cadastros usam exclusão lógica (`excluido='S'`) e nova linha ao inserir; as relações Cardápio–Refeitório são removidas fisicamente.
3. A navegação customizada de Trabalho foi mapeada em [mapa_trabalho.md](mapa_trabalho.md). Restam vínculos de forms sem DFM, como `TFrmSobre`, e confirmar na UI se os cadastros internos de EPIs estão funcionais.
4. Etapa 3: criar YAMLs dos controles documentados; antes de generalizar, validar Cadastro de Veículos no Acessus aberto com fumaça de abrir, preencher um campo sem salvar e fechar. Salvar árvore de controles em `docs/mapas-de-tela/`.
5. Etapas 4–7: ampliar a base inicial descrita abaixo até cobrir todas as telas, com asserções confirmadas, tratamento completo de popups e evidências de banco/serviço quando aplicáveis.

## Avanço das Etapas 3–7 em 29/10/2026

- Criados o primeiro mapa YAML (`src/automatiza/mapas/estacionamento_cadastro_veiculos.yaml`), `TelaGenerica`, `BibliotecaTelas`, uma suíte de fumaça sem gravação e `Rodar-Telas.bat`. O Robot passou em `--dryrun` e os módulos Python passaram em `py_compile`.
- O mapa de Veículos foi validado no build 2.11.1 após abrir Estacionamento pelo painel. `scripts/inspecionar_veiculos_ui.py` exportou a árvore win32; Nome, Placa e botões foram associados ao DFM. A fumaça real sem salvar passou, assim como três validações de campos inválidos. Cadastro de Refeitórios e Cardápios também foram mapeados na UI, com árvores exportadas por `scripts/inspecionar_tela_ui.py`; os dois cenários de Nome obrigatório passaram duas vezes.
- A implementação é uma base inicial, não cobertura funcional de todas as telas: faltam **validar** os YAMLs das demais telas, cenários completos com asserções confirmadas, captura completa de SQL/serviços e validação dos relatórios em execução. Não há escrita em banco nesta suíte.

### Atualização posterior no mesmo dia

- `scripts/gerar_catalogo_telas.py` criou inventários estáticos, mapas YAML e esqueletos Robot para 89 forms dos menus; há 89 YAMLs e suítes adicionais de validação para Veículos, Refeitório e Cardápios. Índice: [README_catalogo_geral.md](telas/README_catalogo_geral.md). Os mapas gerados, exceto os três validados, permanecem bloqueados até inspeção da UI. O `--dryrun` dos 92 testes passou; a suíte `--tag smoke` teve 3 PASS e 88 SKIP. Falhas de handle MDI foram corrigidas, com duas repetições PASS das validações de Refeitório/Cardápios.
- A biblioteca agora detecta seletores ambíguos e popups inesperados, registra ações no Robot e distingue `FalhaTeste` de `FalhaSistema` nas asserções. Veículos tem três cenários de validação derivados de `ValidarCampos`, sem escrita esperada.
- [Diagnóstico de conexão](DIAGNOSTICO-CONEXAO-20261029.md): uma instância iniciada diretamente mostrou erro SQL; após encerrá-la, o módulo aberto pelo painel funcionou. A senha do INI é decriptada pelo Delphi; decriptada, a configuração conecta ao mesmo banco de teste que o `.env`. Nenhum INI foi alterado.
- [COBERTURA.md](COBERTURA.md) registra contagens, significado de `PASS`/`SKIP` e a lista de pendências de execução. Os 92 testes declarados em `tests/telas/` passaram no `--dryrun`; isso não valida o comportamento das telas ainda não inspecionadas.
- `src/automatiza/abertura_modulo.py` inicia o painel, autentica com `.env` local e abre o módulo necessário. A fumaça de Veículos passou após fechar previamente módulo e painel, comprovando a execução sem preparação manual nessa rota (`resultados/robot-telas/20261029-104607/`).
- `Rodar-Telas.bat` completo foi executado: **93 testes Robot, 6 PASS, 0 FAIL, 87 SKIP**, com relatório em `resultados/robot-telas/20261029-104645/`. Os PASS correspondem às três fumaças de telas e aos cenários negativos de Veículos, Refeitório e Cardápios; os SKIP são mapas ainda não validados ou bloqueios anteriores. Não houve gravação no banco nesta rodada.
- Os 89 inventários em `docs/telas/estatico/` passaram a incluir tipo do controle e índice de procedures relevantes com chamadas de controller/DAO e linha da unit. Isso acelera leitura manual, mas não substitui a análise das condições e dos efeitos. `C:\acesso\Acessus.Trabalho.exe` não está instalado, portanto Trabalho permanece apenas documentado pela fonte.

## Dúvidas encontradas no código

### Lote Administração (29/10/2026, após rodada 110144)

- Os 82 `SKIP` da rodada `20261029-110144` foram agrupados pelo `output.xml`: 81 por mapa ainda não validado (ex.: `TFAcessoPorPessoa`) e 1 suíte antiga bloqueada (`Checagem leitura`). Por módulo, os mapas pendentes eram Acesso 41, Administração 4, Escola 16, Estacionamento 10, Módulo 1, Portaria 7 e Refeitório 2.
- Administração: `TFrmAdministracaoViewsCadUsuarios` e `TFrmAdministracaoViewsParametrosSistema` abriram e fecharam sem gravação; árvores win32 em `docs/mapas-de-tela/administracao_*-win32-20261029-1108*.txt` (161 e 65 entradas `child_window`). Mapas liberam somente abertura (`controles_validados: []`). Fumaças individuais PASS em `resultados/robot-telas/20261029-111007/` e `20261029-110945/`. A primeira tentativa da fumaça de Usuários falhou por timeout de menu após inspeção de outro item; repetição isolada PASS.
- Administração: `TFrmAdministracaoViewsOpcoesSistema` ficou SKIP porque a legenda estática `Opções do Sistema` não apareceu como item UIA visível na rota; `TFrmAuditoriaHistoricoAdministracao` ficou SKIP porque o YAML gerado contém subitem de menu vazio. Não foram validados nem executados. **Resultado do lote: 2 PASS, 0 FAIL finais, 2 SKIP**. Próximo lote somente após “segue”.

### Lote Refeitório + Portaria (29/10/2026)

- **Refeitório: 0 PASS, 0 FAIL, 2 SKIP.** `TFrmAuditoriaHistoricoRefeitorio` e `TFrmGerarRefeicao` já haviam falhado na rota de menu do build 2.11.1; mantidos bloqueados, sem nova investigação, conforme orientação do Gabriel.
- **Portaria: 4 PASS, 0 FAIL, 3 SKIP.** Configuração de Etiqueta, Importação, Visita Rápida e relatório de Visitantes e Terceiros abriram, tiveram árvores win32 exportadas em `docs/mapas-de-tela/portaria_*-win32-20261029-111*.txt` e fecharam sem gravação. Os quatro mapas permitem só a rota (`controles_validados: []`), exceto o botão de relatório validado em Visitantes e Terceiros. As quatro fumaças isoladas passaram. Auditoria, Cadastro de Visitantes/Terceiros e a classe alternativa `...Dois` não abriram; permaneceram bloqueados, sem investigação.
- O botão `Relatório (Ctrl+I)` de Visitantes e Terceiros foi acionado duas vezes com os filtros padrão do dia. O build exibiu um `TMessageForm` intitulado `Informação`; a árvore win32 do popup expôs apenas `OK`, sem texto legível. O popup foi fechado e não houve gravação. **Resultado da consulta e conteúdo do relatório não confirmados**; não marcar geração como PASS funcional.
- Restam 75 mapas com `validado_na_ui: false` após dois mapas validados na Administração e quatro na Portaria (a contagem inicial era 81). A suíte completa não foi executada, conforme regra de economia. Próximo lote somente após “segue”.

### Validação adicional de UI em 29/10/2026

- Reservas de Refeições: árvore win32 da grade e da aba de inclusão exportada por `scripts/inspecionar_mapa_pendente.py`; menu real, Incluir e Cancelar validados no build 2.11.1. Fumaça Robot passou em `resultados/robot-telas/20261029-105219/`. O YAML libera somente `btn_inserir` e `btn_cancelar` via `controles_validados`, pois os demais seletores ainda não foram conferidos na UI. Nenhum dado foi gravado.
- O script de inspeção aceita `--incluir-cancelar` para exportar a aba de cadastro e cancelar sem salvar. `TelaGenerica._controle` recusa controles fora da lista validada quando o mapa a define.
- A pendência anterior que pedia criar o primeiro YAML e validar Veículos está concluída; as pendências reais são conferir os seletores das demais telas e construir cenários com resultado esperado verificável.
- Rodada completa após essa validação: `resultados/robot-telas/20261029-105301/`, **93 testes, 7 PASS, 0 FAIL, 86 SKIP**. Os `SKIP` seguem bloqueados por mapa não validado ou por condição anterior. O repositório de fonte continuou sem alterações (`git status --porcelain` vazio). O projeto de testes já tinha muitas alterações e exclusões pré-existentes; não foram revertidas.
- Quatro rotas adicionais de Refeitório (Refeições, Créditos, Refeições Total e relatório de Reservas) abriram e fecharam na UI. Árvores exportadas em `docs/mapas-de-tela/`; detalhes e duas rotas que não abriram em [VALIDACAO-ROTAS-REFEITORIO-20261029.md](VALIDACAO-ROTAS-REFEITORIO-20261029.md). Seus mapas liberam somente a abertura, com `controles_validados: []`. Fumaça por tag após correção do `.bat`: `resultados/robot-telas/20261029-105936/`, 90 testes, 8 PASS, 0 FAIL, 82 SKIP. O relatório anterior `20261029-105843/` foi antes da correção do filtro.
- Validação funcional adicional: Reservas sem pessoa gerou `É necessário selecionar uma pessoa.` como em `ValidarCampos`; `tests/telas/refeitorio_reservas_validacoes.robot` passou sem gravação. Rodada integral mais recente: `resultados/robot-telas/20261029-110144/`, **94 testes, 12 PASS, 0 FAIL, 82 SKIP**. A pasta `docs/VALIDACAO-ROTAS-REFEITORIO-20261029.md` descreve a evidência. Continuam pendentes os cenários com gravação, limpeza, verificação em banco, relatórios executados e validação dos demais mapas.

- Cadastro de Veículos: duas abas anunciam Ctrl+F (Placa e Estacionamento); `ActIrExecute` itera `VeiculosItem`, mas usa `FVeiculosModel` ao preencher a grade.
- Reservas: DFM mostra Cardápio (Ctrl+Q), ação mostra Cardápio (Ctrl+D). `GravaCampos` parece retornar `True` mesmo se o controller falhar.
- Importar Refeições: validações de período estão comentadas; o cartão futuro aparece no DFM, mas a ação chama sempre a importação rápida.
- Cardápios: `GravarRelacaoRefeitorios` insere relações selecionadas, sem remoção evidente de relações desmarcadas. Horas inválidas podem virar zero em `StrToTimeDef`.
- Refeitório: opção de controle de créditos invisível no DFM, mas gravada pelo form.
- Coletores: aviso de exclusão afirma perda permanente inclusive de marcações online; verificar no DAO e no banco de teste antes de testar exclusão. As condições de faixa de TimeOut de Dimep Micropoint/Biopoint usam `> 65 and < 1`, que não pode ser verdadeiro; TopData Fit usa `or`.
- Modelo de Coletores: `GravaCampos` ignora o retorno de `GravaCamposLayout`, deixando dúvida sobre falha parcial na gravação.

## Como reproduzir a extração estática

No PowerShell, dentro de `C:\AutomatizaTestes`:

```powershell
Set-ExecutionPolicy -Scope Process Bypass -Force
& 'C:\python32b\venv32\Scripts\Activate.ps1'
python scripts/gerar_mapa_fonte.py
python scripts/extrair_telas_refeitorio.py
```

Os geradores leem `C:\Acessus-Fonte` e escrevem somente em `docs/`. Eles não acessam o banco nem controlam a UI. Não sobrescrevem as fichas de análise manual listadas em `CURADOS`.
