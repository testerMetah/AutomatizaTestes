# Análise durante os testes manuais

Para consultas parametrizadas e comparação pontual, veja [Consultas e comparação](CONSULTAS-E-COMPARACAO.md).

O observador SQL registra as mudanças em `dbo.Afastamentos` na base escolhida para o teste. A preparação inicial usou `bras1`; veja [como selecionar outra base](BASES-DE-TESTE.md). O acompanhante lê esses arquivos locais e consulta o estado dos serviços, sem controlar janelas ou alterar dados. Novas coletas iniciadas por `scripts/observar.ps1` também iniciam o acompanhante; `-SemAnalise` desativa essa etapa.

```powershell
.\scripts\analisar.ps1                      # acompanhamento oculto da sessão ativa
.\scripts\analisar.ps1 -Acao status
.\scripts\analisar.ps1 -Acao gerar          # atualização pontual
.\scripts\analisar.ps1 -Acao referencias    # consulta pontual de nomes/chaves em Pessoas
.\scripts\analisar.ps1 -Acao exportar       # ZIP local, sem envio
.\scripts\analisar.ps1 -Acao parar          # para somente a análise, mantém a coleta SQL
```

O relatório `analise.html` fica na pasta da sessão em `reports/observacao`. Mostra inclusões, remoções, alterações, antes/depois por pessoa, reaparecimentos da mesma chave de origem, alertas e estados dos serviços. Exporta CSVs e um ZIP com histórico congelado e manifesto SHA256. Não inclui `.env`. Os horários exibidos usam São Paulo; os históricos usam UTC. Estados dos serviços são amostras, não medição exata de disponibilidade nem prova de qual serviço importou.

## Expectativas de cada caso

Copie `examples/caso-offline.modelo.json`, preencha os critérios reais e altere `preparado` para `true`. Registre a expectativa **antes da ação manual** para preservar uma amostra anterior:

```powershell
.\scripts\analisar.ps1 -Acao registrar -Arquivo C:\AutomatizaTestes\meu-caso.json
```

O registro não executa nem comprova a ação no RH. Use um identificador novo por execução. Tipos: `incluir`, `excluir`, `recadastrar` e `ausencia`. Use o IdPessoa interno, causa exata e datas do destino. Recadastro exige também `inicio_anterior` e `termino_anterior`. Prazo, estabilidade e lacuna máxima são configuráveis no modelo.

O avaliador verifica amostra anterior, estabilidade, prazo e lacunas. Exclusão exige que o registro anterior realmente desapareça; mudança de data não basta. Ausência exige a janela completa e falha se houver presença transitória. Estados inconclusivos são preservados quando faltam evidências. Uma pessoa fora do filtro da coleta não é considerada ausente.

Datas antigas dependem da regra de corte da integração, ainda não confirmada. A data literal `1899-12-30` é destacada como possível data-base Delphi, sem presumir fim em aberto. Para um caso que espera esse valor literal, use `permitir_termino_data_base: true`; ele não equivale a `null`.

Esse JSON é diferente do modelo de consultas manuais `integracao-rh.modelo.json`. Nenhum caso real é aprovado apenas por observar mudanças sem saber o resultado esperado.

## Inventário de estrutura

```powershell
.\.venv\Scripts\python.exe .\scripts\mapear_banco.py
```

Consulta somente catálogos de metadados na base configurada ou indicada por `--base`: objetos, colunas, índices, chaves estrangeiras, gatilhos, dependências, parâmetros e opções da base. Salva cada etapa em `reports/banco`, com timeout de cinco segundos e espera por bloqueios de um segundo. Não consulta registros nem definições de procedimentos/configurações que possam conter credenciais. As estimativas de linhas vêm do catálogo; não executa contagens integrais das tabelas. Uma consulta de metadados que falha fica indicada como não concluída, sem ser confundida com resultado vazio.
