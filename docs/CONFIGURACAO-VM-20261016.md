# Configuração conferida na VM em 16/10/2026

## Atualização da validação real, até 15:05

- Após autorização explícita do usuário, confirmada a substituição da licença.
  O gerador exibiu erro de chave única ao inserir a licença, mas a exportação
  seguinte confirmou `C:\acesso\product.key`. O painel Acessus aceitou o login
  informado e o Módulo de Acesso abriu sem aviso de licença nessa tentativa.
- Cenário `04-conferir-janela-acessus.json` executado pela Central: PASSOU.
  Conferiu conexão automática com a janela visível e habilitada, salvando captura.
  Relatório publicado no host em `reports/vm/TESTESVM/execucoes/20261016-150441-`:
  consulte a pasta com esse prefixo para o identificador completo.
- 143 testes unitários aprovados na VM na última instalação.
- Corrigido o uso de handlers de log fechados herdados da preparação gráfica.
  O problema interrompia `type_keys` antes de concluir o preenchimento do RH.
  Os testes cobrem a substituição do handler fechado e a preservação do válido.
- Depois dessa correção, o RH exibiu **Usuário inválido** para o login salvo
  `master`. Não foram feitas tentativas com outras credenciais. O login recusado
  foi cancelado; nenhuma ocorrência ou férias foi cadastrada/excluída.
- Cenário de ocorrências bloqueado na autenticação, antes da abertura da tela.
  Relatório: `reports/vm/TESTESVM/execucoes/20261016-150114-6ebb1629/`.
- Falta confirmar as credenciais e a origem ativa do RH antes de prosseguir.
  O perfil escolhido na Central foi RHFagundes → novo123; isso não comprova
  que o RH ou a integração estejam usando essa origem.

O texto abaixo preserva o registro da preparação anterior. A pendência da
licença descrita nele foi resolvida conforme a atualização acima.

Trabalho realizado pela interface da VM AutomatizaTestes, Windows TESTESVM.

- Código, scripts, exemplos, testes e guias atualizados com backup.
- Credenciais RH ausentes reutilizadas do `.env` de origem, sem expor os valores.
  Isso não comprova autenticação bem-sucedida no RH.
- Conferência SQL padrão alinhada ao destino já configurado no importador:
  `desk-tec / novo123`. A configuração do serviço não foi alterada.
- Perfis preservados para `bras1` e criados para `novo123`, com origens
  RHFagundes, RHBraslux e ORACLE-METAH. O alias ativo do RH e a origem efetiva
  usada pela integração ainda precisam corresponder ao perfil escolhido.
- 141 testes unitários aprovados dentro da VM, sem avisos na última execução.
- Cenário `01-conferir-estrutura-sql.json` executado pela Central com o perfil
  `RHFagundes_para_novo123.json`: PASSOU. Esse cenário confere conexão, banco
  e estrutura de Pessoas/Afastamentos; não confere importação de negócio.

Evidências publicadas no host:
`reports/vm/TESTESVM/configuracao-20261016-144419-625224/`.
Resultado: `PREPARACAO_TECNICA_CONFERIDA`.
Backup correspondente dentro da VM:
`C:\AutomatizaTestes\reports\atualizacao\20261016-144419-625224\backup`.
Relatório do cenário SQL dentro da VM:
`C:\AutomatizaTestes\reports\execucoes\20261016-144543-0a007bd7\relatorio.html`.

## Licença Acessus

O Key.exe não conectava ao servidor `dev-manager`. O host confirmou
`192.168.50.105:1433`; o endereço foi ajustado apenas no gerador da VM,
preservando os demais campos. O aplicativo confirmou conexão bem-sucedida
e configurações salvas.

Cliente `teste` selecionado em Acessus; acionados Gerar Licença e Gerar.
O aplicativo avisou que já existe licença ativa e que uma nova licença de rede
desativará a anterior. A confirmação ficou pendente de resposta do usuário.
Não há confirmação de novo arquivo `.key` gerado nesta etapa.

## Limites

Os cenários de abertura de ocorrências e férias estão disponíveis, mas não
foram executados nesta etapa. Cadastros, exclusões e recadastros automáticos
ainda exigem validação das telas e resultados esperados. Também faltam
confirmar regras de datas antigas, vínculo de pessoas/contratos, ciclo da
integração e tratamento do término. O login Oracle não foi validado.
