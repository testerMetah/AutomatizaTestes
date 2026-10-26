# Decisões das sequências com estado (2026-10-23)

1. **Segurança primeiro no backend real.** Os mapas existentes são de builds anteriores e não provam que um botão do 2.11.1 ainda executa a mesma operação. Por isso ações de escrita sem seletor, regra e limpeza validados retornam BLOQUEADO, sem clicar nem escrever no SQL.
2. **Leitura real como primeiro smoke.** `checagem_leitura.yaml` executa SELECT 1 em ambos os bancos confirmados e observa a janela principal atual. Assim se valida a infraestrutura sem inventar regra de negócio.
3. **Seed obrigatória.** O gerador aleatório usa `random.Random(seed)`, número máximo de passos e volume pequeno por padrão (5). A seed aparece em cada evento para repetição.
4. **Oráculo conservador.** Só regras confirmadas entram no modelo esperado; operações sem regra geram AVISO. O executor não transforma comportamento observado em verdade automaticamente.
5. **Redução de falhas isolada.** `reduce_failure` recebe um replay que recria o ambiente a cada tentativa. Não reexecuta mutações reais sem fixture/limpeza; isso evita multiplicar dados ao reduzir uma falha.
6. **Um banco de destino.** Acessus e serviços usam `AcessoFagundes`; RH usa `RHFagundes`. Os nomes `novo123` e `sm` são dúvidas sobre destinos de configurações de serviços, não bancos novos criados aqui.
7. **Sem dependência do repositório de referência.** `C:\Referencia\Acessus` não existe nesta máquina nesta sessão. Mapas antigos são pistas, e a UI/banco atual têm precedência. A pasta `referencias/` fica fora do commit por conter checkout independente.
8. **Saídas fora do Git.** `reports/` contém screenshots e dados de execução; fica ignorado. O código nunca embute credenciais.

## 23/10/2026: base isolada

9. Destino unico: `desk-tec/Acessus_AUTOTEST_20261023` para Acessus e tres servicos; `RHFagundes` permanece origem RH. Schema copiado sem dados da base antiga.
10. O assistente do Acessus criou a empresa inicial `AUTOTEST_20261023_EMPRESA_INICIAL` e o administrador pela UI. Nenhuma senha entra no Git.
11. Os tres servicos foram iniciados apos verificar destino nos INIs. Sync exigiu login administrativo previo. API esta Running, mas sem configuracao e sem importacao.
12. `TFConfigAPI` recusou salvar porque exige pelo menos um coletor. Nao cadastrar coletor ficticio sem saber impacto em dispositivos. Conexao SQL de `RHFagundes` foi salva no Importador.
13. Gabriel confirmou exclusao logica no Acessus e nova linha ao recriar igual. Coluna e vinculos por entidade ainda pendentes.

## Autonomia da CLI e do painel (26/10/2026)

14. A CLI nova usa `automatiza.nova_cli` como entrada principal e delega comandos históricos a `automatiza.cli`; preserva scripts e compatibilidade sem reescrever fluxos maduros.
15. Dois perfis declarativos separam a cópia de auditorias (`AcessoFagundes`) da instalação principal (`Acessus_AUTOTEST_20261023`); evita banco fixado dentro da suíte.
16. `psutil` não instala na venv Windows/Python 32 bits atual sem compilar C++; descoberta de processos usa pywin32 já instalado e serviços usam `sc.exe`, sem dependência nova.
17. O painel usa `http.server` da biblioteca padrão em `127.0.0.1`, sem Node, CDN ou serviço Windows; o terminal do usuário mantém a sessão desktop interativa.
18. O comando `observar iniciar` cria um processo em segundo plano; assim a coleta SQL não impede iniciar testes de interface pelo painel.
19. Ao editar um perfil e mudar o banco, a marca `confirmado_como_teste` vira falsa; a escrita só volta após confirmação explícita no arquivo de configuração.
20. Contagens de históricos permanecem exploratórias até existir regra `CONFIRMADA` com SQL de contagem restrito e parametrizado em `docs/cenarios/`; nenhuma contagem esperada foi inferida do banco.
21. Scripts legados sem formulário seguro aparecem no Catálogo com comando e pré-requisitos, mas o botão Executar fica desabilitado com motivo visível; isso evita iniciar scripts que exigem PID ou dados de teste sem validação pelo painel.
