# Preparação e limites atuais

## Execução em lote (19/10/2026)

Após atualizar a VM, a Central oferece **Executar lote...**. Abra o ambiente
salvo, entre no RH, confira o alias ativo e deixe o Módulo de Acesso aberto.
Selecione `examples/lote-preparacao.json`: ele confere SQL, janela Acessus,
tela de ocorrências e tela de férias, nessa ordem. Para no primeiro resultado
diferente de PASSOU, identificando os restantes como NAO_EXECUTADO.

O índice HTML reúne os resultados e os links para as evidências individuais.
Fica em `reports/lotes/<execução>/indice.html` na VM; com ResultadoVM disponível,
o lote completo também é copiado para a pasta compartilhada de resultados.
Isso valida os quatro cenários implementados, sem cadastrar/excluir dados.

Na conferência inicial de 19/10 não havia compartilhamentos. Eles foram
restaurados, conferidos dentro da VM e salvos permanentemente:

| Nome | Pasta no computador principal | Acesso |
| --- | --- | --- |
| OrigemAutomatiza | C:\AutomatizaTestes | Somente leitura |
| ResultadoVM | C:\AutomatizaTestes\reports\vm\TESTESVM | Leitura e escrita |

Para conferir/reparar novamente no host, execute
`scripts/reparar-compartilhamentos-vm.ps1`. Ele preserva a configuração anterior,
confere os caminhos e não substitui compartilhamentos divergentes.
O login do RH continua dependendo de autenticação válida pelo usuário.
A primeira atualização desta etapa passou em 149 testes unitários dentro da VM;
o cenário SQL real também passou em novo123. Consulte a evidência mais recente em
[Estado da VM](ESTADO-VM-20261019.md). Testes unitários não são testes de negócio.
O lote `examples/lote-sql.json` permite conferir a estrutura sem usar telas.

Dentro da VM, abra `\\VBOXSVR\OrigemAutomatiza\ATUALIZAR-TESTES-VM.cmd`.
O atualizador preserva o `.env`, os perfis existentes e as configurações dos
sistemas. Guarda backup dos arquivos substituídos, roda os testes unitários e
gera um diagnóstico com consultas SQL limitadas, sem cadastrar ou excluir dados.
Feche e reabra a Central após a atualização.

Na Central, use **Verificar preparação** e depois **Abrir último relatório**.
O diagnóstico confere o ambiente salvo selecionado; sem perfil selecionado,
confere a configuração padrão da automação. Salve alterações nos campos antes
de conferir o ambiente.

O aplicativo gráfico `Preparar-Testes.pyw`, aberto pelo atalho em `Pronto-VM`,
também atualiza o projeto sem abrir terminal. Se faltarem credenciais RH na VM,
ele reutiliza somente os valores disponíveis no `.env` de origem, sem exibi-los.
Confere o destino real do importador com consultas de leitura e, se a estrutura
estiver disponível, alinha a conferência SQL a esse destino e cria perfis
adicionais. Preserva os perfis existentes e faz backup das configurações locais.
Não altera o banco ou a configuração do serviço de importação.

Os quatro cenários disponíveis em `examples/cenarios` são:

- `01-conferir-estrutura-sql.json`: confere conexão, nome do banco e colunas usadas nas verificações.
- `02-abrir-ocorrencias.json`: confere abertura da tela, sem inclusão.
- `03-abrir-ferias.json`: confere abertura da tela, sem inclusão.
- `04-conferir-janela-acessus.json`: conecta ao Módulo de Acesso já aberto,
  verifica disponibilidade e salva uma captura de evidência.

Para os cenários de tela, entre no RH antes, confira o alias ativo, abra o
ambiente correspondente na Central e reserve o mouse e teclado da VM.
Esses cenários ainda precisam ser validados na instalação em execução.
Uma aprovação deles não aprova a importação de férias ou ocorrências.

Os oito casos em `examples/casos-offline` continuam disponíveis para acompanhar
operações manuais e conferir o resultado esperado no destino. Exigem pessoa,
causa e datas reais. Não habilite modelos com dados ilustrativos.

Para automatizar a sequência completa ainda é necessário validar os controles de
gravação/exclusão, confirmar pessoa e contrato nos dois sistemas e definir os
resultados esperados. Também falta confirmar a origem usada pela integração,
seu ciclo, a regra de datas antigas e o tratamento do término sem data.
O ambiente Oracle exige serviço/SID e autenticação validados.

Um perfil da Central seleciona o destino da conferência SQL. Ele não reconfigura
o importador nem troca o alias do RH. Os bloqueios por divergência devem ser
resolvidos conferindo a origem e o destino reais, sem desativar as verificações.
