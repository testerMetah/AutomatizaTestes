# Casos para RH → Acessus

Esta matriz prepara a automação sem alterar o ambiente. A execução atual é:
ação manual no RH + observação SQL do destino. As ações automáticas de
cadastro/exclusão no RH continuam pendentes de validação dos controles reais.

## Identificação e evidência necessárias

Antes de cada caso, registre contrato no RH, `IdPessoa` no Acessus, tipo/código
da ocorrência (quando houver), período completo esperado, causa no destino e
estado inicial. Não confunda matrícula/contrato com o ID interno do Acessus.
Uma forma inicial de localizar a correspondência para uma pessoa conhecida é:

```sql
SELECT id, IdExportacao, ContratoExportacao
FROM dbo.Pessoas
WHERE id = ?;
```

Esses campos são pistas de integração; a correspondência precisa ser confirmada.
O observador armazena os IDs e períodos do destino sem consultar documentos,
biometria, senhas ou dados de contato das pessoas.

| Caso | Ação no RH | Conferência no Acessus |
|---|---|---|
| Ocorrência: incluir | Cadastrar um tipo que efetivamente gere afastamento | Afastamento esperado por pessoa, causa e período; conferir ID e `IdFreq` observados |
| Ocorrência: excluir | Excluir o registro que já foi importado | Registro previamente existente deixa de aparecer; correlacionar com a ação manual |
| Ocorrência: recadastrar | Cadastrar novamente com outras datas | Período antigo ausente e novo período presente, sem presumir reutilização do mesmo ID |
| Ocorrência antiga | Cadastrar período antes do corte definido pelo serviço | Comparar com a regra de corte confirmada; até lá, relatar apenas o comportamento observado |
| Férias: incluir | Cadastrar férias cedidas | Pessoa e período esperados aparecem como afastamento; confirmar horários convertidos pelo serviço |
| Férias: excluir | Excluir férias previamente importadas | Afastamento antigo deixa de aparecer, com existência anterior comprovada |
| Férias: recadastrar | Cadastrar novas datas após a exclusão | Antigo período ausente e novo presente |
| Férias antigas | Cadastrar período anterior ao corte | Esperado condicionado à regra real; a janela de ausência não comprova execução do serviço |

## Várias pessoas

Repita os mesmos casos para contratos diferentes, com um caso/identificador
por pessoa. O observador pode acompanhar todas ou apenas uma lista de IDs.
Os formulários de programação coletiva também foram mapeados estaticamente,
mas não foram acionados. O resultado coletivo deverá ser conferido pessoa a
pessoa; a tela de conclusão de uma operação em lote não comprova todos os registros.

## O que conta como resultado

- O observador mostra mudanças por `Id`, com antes/depois e intervalo entre amostras.
- O comando `acompanhar` valida contagens definidas no caso, depois da ação manual.
- Zero registros desde o início não comprova que uma exclusão propagou.
- Uma alteração pode ser feita no mesmo ID ou por remoção/inclusão com novo ID.
  Ambos devem ser relatados conforme observados.
- Duplicidade de pessoa/período/causa precisa ser confrontada com os registros
  de origem: duas origens legítimas não podem ser classificadas como erro apenas por coincidirem nas datas.
- Erro de consulta ou serviço indisponível deve ficar separado de divergência de dados.

O nome do serviço, seu ciclo, a regra de corte e as conversões de datas ainda
precisam ser confirmados. Um diagnóstico somente de leitura dos serviços foi
salvo junto ao relatório da observação, em `servicos-diagnostico.json`.
