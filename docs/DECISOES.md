# Decisões das sequências com estado (2026-10-23)

1. **Segurança primeiro no backend real.** Os mapas existentes são de builds anteriores e não provam que um botão do 2.11.1 ainda executa a mesma operação. Por isso ações de escrita sem seletor, regra e limpeza validados retornam BLOQUEADO, sem clicar nem escrever no SQL.
2. **Leitura real como primeiro smoke.** `checagem_leitura.yaml` executa SELECT 1 em ambos os bancos confirmados e observa a janela principal atual. Assim se valida a infraestrutura sem inventar regra de negócio.
3. **Seed obrigatória.** O gerador aleatório usa `random.Random(seed)`, número máximo de passos e volume pequeno por padrão (5). A seed aparece em cada evento para repetição.
4. **Oráculo conservador.** Só regras confirmadas entram no modelo esperado; operações sem regra geram AVISO. O executor não transforma comportamento observado em verdade automaticamente.
5. **Redução de falhas isolada.** `reduce_failure` recebe um replay que recria o ambiente a cada tentativa. Não reexecuta mutações reais sem fixture/limpeza; isso evita multiplicar dados ao reduzir uma falha.
6. **Um banco de destino.** Acessus e serviços usam `AcessoFagundes`; RH usa `RHFagundes`. Os nomes `novo123` e `sm` são dúvidas sobre destinos de configurações de serviços, não bancos novos criados aqui.
7. **Sem dependência do repositório de referência.** `C:\Referencia\Acessus` não existe nesta máquina nesta sessão. Mapas antigos são pistas, e a UI/banco atual têm precedência. A pasta `referencias/` fica fora do commit por conter checkout independente.
8. **Saídas fora do Git.** `reports/` contém screenshots e dados de execução; fica ignorado. O código nunca embute credenciais.

