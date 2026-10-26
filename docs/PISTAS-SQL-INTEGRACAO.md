# Trechos SQL estáticos da integração

Consultas encontradas nos arquivos instalados; não executadas. Literais textuais foram omitidos.
Ter um trecho no executável não comprova que ele foi acionado ou quais parâmetros recebeu.

## Acessus.exe

SHA-256: `cd720c0a1d04bf77a7e7089ff21e43ac5f662cfd0cd0b3dd0b0f2e8846bbcaf1`

Offset 10119092; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni, f.TERMINOGOZOFERIAS dataFim

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO = 1 AND f.INICIOGOZOFERIAS >= :Ini
```

Offset 10119596; codificação utf-16-le; cortado: False.

Flag GERAAFASTAMENTO observada: S.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato, r.OCORRENCIA ocorrencia,
  r.DATAINICIOOCORRENCIA dataIni, r.DATATERMINOOCORRENCIA dataFim,
  o.DESCRICAO40 causa

from RHREGOCORRENCIAS r
join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.CONTRATO

where c.SITUACAO in (1,2) AND r.DATAINICIOOCORRENCIA >= :Ini
  AND o.GERAAFASTAMENTO = '<literal omitido>'
  AND :Hoje BETWEEN r.DATAINICIOOCORRENCIA AND COALESCE(r.DATATERMINOOCORRENCIA, :Hoje)
```

Offset 10123636; codificação utf-16-le; cortado: False.

Flag GERAAFASTAMENTO observada: S.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato, r.OCORRENCIA ocorrencia,
  r.DATAINICIOOCORRENCIA dataIni

from RHREGOCORRENCIAS r
join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.CONTRATO

where c.SITUACAO in (1,2)
  AND o.GERAAFASTAMENTO = '<literal omitido>'
  AND :Hoje BETWEEN r.DATAINICIOOCORRENCIA AND COALESCE(r.DATATERMINOOCORRENCIA, :Hoje)
```

Offset 10126020; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO in (1,2)
  AND (f.TERMINOGOZOFERIAS IS NULL OR f.TERMINOGOZOFERIAS >= :Hoje)
```

Offset 10127292; codificação utf-16-le; cortado: False.

```sql
SELECT * FROM Afastamentos WHERE Id = :Id
```

Offset 10127564; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where Id = :Id 
```

Offset 10127796; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where ID = :id 
```

Offset 10128164; codificação utf-16-le; cortado: False.

```sql
delete from Afastamentos where idpessoa = :idpessoa 
```

Offset 10129880; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where a.Id = :Id
```

Offset 10130224; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where IdPessoa = :idpessoa and :data >= dataInicio and (dataTermino = 0 or :data <= dataTermino)
```

Offset 10130772; codificação utf-16-le; cortado: False.

```sql
select 1 as Achou from Afastamentos where IdPessoa = :idpessoa and IdFreq like :prefixo and :data >= dataInicio and (dataTermino = 0 or :data <= dataTermino)
```

Offset 10131292; codificação utf-16-le; cortado: False.

```sql
select id as Id from Afastamentos as a where IdFreq = :IdFreq;
```

Offset 10131664; codificação utf-16-le; cortado: False.

```sql
SELECT MIN(Id) AS Id FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa   AND DataInicio = :DataInicio   AND IdFreq NOT LIKE :Prefixo
```

Offset 10132552; codificação utf-16-le; cortado: False.

```sql
select Afastamentos.*, p.nome as NomePessoa from Afastamentos inner join Pessoas p on p.id = Afastamentos.idPessoa where IdPessoa = :idpessoa 
```

Offset 10133304; codificação utf-16-le; cortado: False.

```sql
select a.* from Afastamentos a
```

Offset 10133668; codificação utf-16-le; cortado: False.

```sql
SELECT Id, IdPessoa, DataInicio, DataTermino, IdFreq, Causa FROM Afastamentos WHERE IdFreq LIKE :prefixo   AND (DataTermino = :DataZero OR :Hoje <= DataTermino)
```

Offset 10134228; codificação utf-16-le; cortado: False.

Padrões LIKE de IdFreq observados: `%-%`.

```sql
SELECT TOP 1 DataInicio FROM Afastamentos  WHERE IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>'   ORDER BY DataInicio DESC
```

Offset 10138576; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where p.Nome like :Nome
```

Offset 10139176; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdFreq = :IdFreq
```

Offset 10139344; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa AND (:DataTermino = :DataZero OR DataInicio <= :DataTermino) AND (DataTermino = :DataZero OR :DataInicio <= DataTermino)
```

Offset 10207548; codificação utf-16-le; cortado: False.

```sql
select * from pessoas p
left join Afastamentos a on p.id = a.IdPessoa and
  (a.DataInicio <= GETDATE() and
  (a.DataTermino > GETDATE() or a.DataTermino is null or a.DataTermino < :1920))
where (p.status = 0 and a.id is null)
```

Offset 13971172; codificação utf-16-le; cortado: False.

```sql
SELECT p.Nome, p.Id, s.nome as Setor, IdSetor, u.nome as Unidade, IdUnidade,   CASE     WHEN EXISTS (       SELECT 1 FROM AFASTAMENTOS A       WHERE A.IdPessoa = p.Id         AND GETDATE() >= A.DataInicio         AND (A.DataTermino > GETDATE() OR A.DataTermino <= :dataZero)     ) THEN 2 ELSE CASE WHEN p.Status = 2 THEN 0 ELSE p.Status END   END as Status FROM Pessoas p LEFT JOIN Setores s ON s.id = p.IdSetor LEFT JOIN Unidades u ON u.id = p.IdUnidade WHERE 1=1 and p.excluido = '<literal omitido>' 
```

Offset 13972404; codificação utf-16-le; cortado: False.

```sql
SELECT 1 FROM AFASTAMENTOS A    WHERE A.IdPessoa = p.Id      AND GETDATE() >= A.DataInicio      AND (A.DataTermino > GETDATE() OR A.DataTermino <= :dataZero) )
```

Offset 13989052; codificação utf-16-le; cortado: False.

```sql
SELECT
  p.Id,
  p.Nome,
  d.Data,
  CASE
      WHEN COUNT(a.id) > 0 THEN 2 -- Afastado
      WHEN COUNT(m.id) > 0 THEN 1 -- Presente
      ELSE 0                      -- Falta
  END AS Presenca
FROM PESSOAS_UNIFICADAS p
CROSS JOIN RangeDatas d
LEFT JOIN @MarcacoesOnline m ON d.Data = m.DataReferencia
  AND p.id = m.idpessoa
LEFT JOIN Afastamentos a ON a.IdPessoa = p.Id
  AND a.DataInicio <= d.Data
  AND (a.DataTermino >= d.Data OR a.DataTermino < a.DataInicio)

WHERE p.Status = 0
  AND p.excluido = '<literal omitido>'
  &TipoPessoa

GROUP BY p.id, p.nome, d.Data
```

## AcessusSync.exe

SHA-256: `4beccfe74defedd639543ac3ca28b0476b8aa91e199c24eabd8f0c03f1a1c7c8`

Offset 7763464; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni, f.TERMINOGOZOFERIAS dataFim

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO = 1 AND f.INICIOGOZOFERIAS >= :Ini
```

Offset 7763968; codificação utf-16-le; cortado: False.

Flag GERAAFASTAMENTO observada: S.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato, r.OCORRENCIA ocorrencia,
  r.DATAINICIOOCORRENCIA dataIni, r.DATATERMINOOCORRENCIA dataFim,
  o.DESCRICAO40 causa

from RHREGOCORRENCIAS r
join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.CONTRATO

where c.SITUACAO in (1,2) AND r.DATAINICIOOCORRENCIA >= :Ini
  AND o.GERAAFASTAMENTO = '<literal omitido>'
  AND :Hoje BETWEEN r.DATAINICIOOCORRENCIA AND COALESCE(r.DATATERMINOOCORRENCIA, :Hoje)
```

Offset 7768008; codificação utf-16-le; cortado: False.

Flag GERAAFASTAMENTO observada: S.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato, r.OCORRENCIA ocorrencia,
  r.DATAINICIOOCORRENCIA dataIni

from RHREGOCORRENCIAS r
join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.CONTRATO

where c.SITUACAO in (1,2)
  AND o.GERAAFASTAMENTO = '<literal omitido>'
  AND :Hoje BETWEEN r.DATAINICIOOCORRENCIA AND COALESCE(r.DATATERMINOOCORRENCIA, :Hoje)
```

Offset 7770392; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO in (1,2)
  AND (f.TERMINOGOZOFERIAS IS NULL OR f.TERMINOGOZOFERIAS >= :Hoje)
```

Offset 7771664; codificação utf-16-le; cortado: False.

```sql
SELECT * FROM Afastamentos WHERE Id = :Id
```

Offset 7771936; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where Id = :Id 
```

Offset 7772168; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where ID = :id 
```

Offset 7772536; codificação utf-16-le; cortado: False.

```sql
delete from Afastamentos where idpessoa = :idpessoa 
```

Offset 7774252; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where a.Id = :Id
```

Offset 7774596; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where IdPessoa = :idpessoa and :data >= dataInicio and (dataTermino = 0 or :data <= dataTermino)
```

Offset 7775144; codificação utf-16-le; cortado: False.

```sql
select 1 as Achou from Afastamentos where IdPessoa = :idpessoa and IdFreq like :prefixo and :data >= dataInicio and (dataTermino = 0 or :data <= dataTermino)
```

Offset 7775664; codificação utf-16-le; cortado: False.

```sql
select id as Id from Afastamentos as a where IdFreq = :IdFreq;
```

Offset 7776036; codificação utf-16-le; cortado: False.

```sql
SELECT MIN(Id) AS Id FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa   AND DataInicio = :DataInicio   AND IdFreq NOT LIKE :Prefixo
```

Offset 7776924; codificação utf-16-le; cortado: False.

```sql
select Afastamentos.*, p.nome as NomePessoa from Afastamentos inner join Pessoas p on p.id = Afastamentos.idPessoa where IdPessoa = :idpessoa 
```

Offset 7777676; codificação utf-16-le; cortado: False.

```sql
select a.* from Afastamentos a
```

Offset 7778040; codificação utf-16-le; cortado: False.

```sql
SELECT Id, IdPessoa, DataInicio, DataTermino, IdFreq, Causa FROM Afastamentos WHERE IdFreq LIKE :prefixo   AND (DataTermino = :DataZero OR :Hoje <= DataTermino)
```

Offset 7778600; codificação utf-16-le; cortado: False.

Padrões LIKE de IdFreq observados: `%-%`.

```sql
SELECT TOP 1 DataInicio FROM Afastamentos  WHERE IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>'   ORDER BY DataInicio DESC
```

Offset 7782948; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where p.Nome like :Nome
```

Offset 7783548; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdFreq = :IdFreq
```

Offset 7783716; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa AND (:DataTermino = :DataZero OR DataInicio <= :DataTermino) AND (DataTermino = :DataZero OR :DataInicio <= DataTermino)
```

Offset 7851920; codificação utf-16-le; cortado: False.

```sql
select * from pessoas p
left join Afastamentos a on p.id = a.IdPessoa and
  (a.DataInicio <= GETDATE() and
  (a.DataTermino > GETDATE() or a.DataTermino is null or a.DataTermino < :1920))
where (p.status = 0 and a.id is null)
```

## AcessusSyncImportacao.exe

SHA-256: `45ab464d6c5f97314de7c76eee04a840fcb3676fae0ee9352f345533636e0faa`

Offset 7223000; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni, f.TERMINOGOZOFERIAS dataFim

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO = 1 AND f.INICIOGOZOFERIAS >= :Ini
```

Offset 7223504; codificação utf-16-le; cortado: False.

Flag GERAAFASTAMENTO observada: S.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato, r.OCORRENCIA ocorrencia,
  r.DATAINICIOOCORRENCIA dataIni, r.DATATERMINOOCORRENCIA dataFim,
  o.DESCRICAO40 causa

from RHREGOCORRENCIAS r
join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.CONTRATO

where c.SITUACAO in (1,2) AND r.DATAINICIOOCORRENCIA >= :Ini
  AND o.GERAAFASTAMENTO = '<literal omitido>'
  AND :Hoje BETWEEN r.DATAINICIOOCORRENCIA AND COALESCE(r.DATATERMINOOCORRENCIA, :Hoje)
```

Offset 7227548; codificação utf-16-le; cortado: False.

Flag GERAAFASTAMENTO observada: S.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato, r.OCORRENCIA ocorrencia,
  r.DATAINICIOOCORRENCIA dataIni

from RHREGOCORRENCIAS r
join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.CONTRATO

where c.SITUACAO in (1,2)
  AND o.GERAAFASTAMENTO = '<literal omitido>'
  AND :Hoje BETWEEN r.DATAINICIOOCORRENCIA AND COALESCE(r.DATATERMINOOCORRENCIA, :Hoje)
```

Offset 7229944; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO in (1,2)
  AND (f.TERMINOGOZOFERIAS IS NULL OR f.TERMINOGOZOFERIAS >= :Hoje)
```

Offset 7231224; codificação utf-16-le; cortado: False.

```sql
SELECT * FROM Afastamentos WHERE Id = :Id
```

Offset 7231496; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where Id = :Id 
```

Offset 7231728; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where ID = :id 
```

Offset 7232096; codificação utf-16-le; cortado: False.

```sql
delete from Afastamentos where idpessoa = :idpessoa 
```

Offset 7233828; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where a.Id = :Id
```

Offset 7234172; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where IdPessoa = :idpessoa and :data >= dataInicio and (dataTermino = 0 or :data <= dataTermino)
```

Offset 7234720; codificação utf-16-le; cortado: False.

```sql
select 1 as Achou from Afastamentos where IdPessoa = :idpessoa and IdFreq like :prefixo and :data >= dataInicio and (dataTermino = 0 or :data <= dataTermino)
```

Offset 7235240; codificação utf-16-le; cortado: False.

```sql
select id as Id from Afastamentos as a where IdFreq = :IdFreq;
```

Offset 7235612; codificação utf-16-le; cortado: False.

```sql
SELECT MIN(Id) AS Id FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa   AND DataInicio = :DataInicio   AND IdFreq NOT LIKE :Prefixo
```

Offset 7236500; codificação utf-16-le; cortado: False.

```sql
select Afastamentos.*, p.nome as NomePessoa from Afastamentos inner join Pessoas p on p.id = Afastamentos.idPessoa where IdPessoa = :idpessoa 
```

Offset 7237252; codificação utf-16-le; cortado: False.

```sql
select a.* from Afastamentos a
```

Offset 7238524; codificação utf-16-le; cortado: False.

Padrões LIKE de IdFreq observados: `%-%`.

```sql
SELECT TOP 1 DataInicio FROM Afastamentos  WHERE IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>'   ORDER BY DataInicio DESC
```

Offset 7242872; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where p.Nome like :Nome
```

Offset 7243472; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdFreq = :IdFreq
```

Offset 7243640; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa AND (:DataTermino = :DataZero OR DataInicio <= :DataTermino) AND (DataTermino = :DataZero OR :DataInicio <= DataTermino)
```

Offset 7311880; codificação utf-16-le; cortado: False.

```sql
select * from pessoas p
left join Afastamentos a on p.id = a.IdPessoa and
  (a.DataInicio <= GETDATE() and
  (a.DataTermino > GETDATE() or a.DataTermino is null or a.DataTermino < :1920))
where (p.status = 0 and a.id is null)
```

## AcessusSyncService.exe

SHA-256: `c8c4c4d12ca11e9d9332ec0110e5fbb325505e47357a49c1387fac3ca36be0ac`

Offset 7676316; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni, f.TERMINOGOZOFERIAS dataFim

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO = 1 AND f.INICIOGOZOFERIAS >= :Ini
```

Offset 7676820; codificação utf-16-le; cortado: False.

Flag GERAAFASTAMENTO observada: S.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato, r.OCORRENCIA ocorrencia,
  r.DATAINICIOOCORRENCIA dataIni, r.DATATERMINOOCORRENCIA dataFim,
  o.DESCRICAO40 causa

from RHREGOCORRENCIAS r
join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.CONTRATO

where c.SITUACAO in (1,2) AND r.DATAINICIOOCORRENCIA >= :Ini
  AND o.GERAAFASTAMENTO = '<literal omitido>'
  AND :Hoje BETWEEN r.DATAINICIOOCORRENCIA AND COALESCE(r.DATATERMINOOCORRENCIA, :Hoje)
```

Offset 7680860; codificação utf-16-le; cortado: False.

Flag GERAAFASTAMENTO observada: S.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato, r.OCORRENCIA ocorrencia,
  r.DATAINICIOOCORRENCIA dataIni

from RHREGOCORRENCIAS r
join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.CONTRATO

where c.SITUACAO in (1,2)
  AND o.GERAAFASTAMENTO = '<literal omitido>'
  AND :Hoje BETWEEN r.DATAINICIOOCORRENCIA AND COALESCE(r.DATATERMINOOCORRENCIA, :Hoje)
```

Offset 7683244; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO in (1,2)
  AND (f.TERMINOGOZOFERIAS IS NULL OR f.TERMINOGOZOFERIAS >= :Hoje)
```

Offset 7684516; codificação utf-16-le; cortado: False.

```sql
SELECT * FROM Afastamentos WHERE Id = :Id
```

Offset 7684788; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where Id = :Id 
```

Offset 7685020; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where ID = :id 
```

Offset 7685388; codificação utf-16-le; cortado: False.

```sql
delete from Afastamentos where idpessoa = :idpessoa 
```

Offset 7687104; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where a.Id = :Id
```

Offset 7687448; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where IdPessoa = :idpessoa and :data >= dataInicio and (dataTermino = 0 or :data <= dataTermino)
```

Offset 7687996; codificação utf-16-le; cortado: False.

```sql
select 1 as Achou from Afastamentos where IdPessoa = :idpessoa and IdFreq like :prefixo and :data >= dataInicio and (dataTermino = 0 or :data <= dataTermino)
```

Offset 7688516; codificação utf-16-le; cortado: False.

```sql
select id as Id from Afastamentos as a where IdFreq = :IdFreq;
```

Offset 7688888; codificação utf-16-le; cortado: False.

```sql
SELECT MIN(Id) AS Id FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa   AND DataInicio = :DataInicio   AND IdFreq NOT LIKE :Prefixo
```

Offset 7689776; codificação utf-16-le; cortado: False.

```sql
select Afastamentos.*, p.nome as NomePessoa from Afastamentos inner join Pessoas p on p.id = Afastamentos.idPessoa where IdPessoa = :idpessoa 
```

Offset 7690528; codificação utf-16-le; cortado: False.

```sql
select a.* from Afastamentos a
```

Offset 7690892; codificação utf-16-le; cortado: False.

```sql
SELECT Id, IdPessoa, DataInicio, DataTermino, IdFreq, Causa FROM Afastamentos WHERE IdFreq LIKE :prefixo   AND (DataTermino = :DataZero OR :Hoje <= DataTermino)
```

Offset 7691452; codificação utf-16-le; cortado: False.

Padrões LIKE de IdFreq observados: `%-%`.

```sql
SELECT TOP 1 DataInicio FROM Afastamentos  WHERE IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>'   ORDER BY DataInicio DESC
```

Offset 7695800; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where p.Nome like :Nome
```

Offset 7696400; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdFreq = :IdFreq
```

Offset 7696568; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa AND (:DataTermino = :DataZero OR DataInicio <= :DataTermino) AND (DataTermino = :DataZero OR :DataInicio <= DataTermino)
```

Offset 7764772; codificação utf-16-le; cortado: False.

```sql
select * from pessoas p
left join Afastamentos a on p.id = a.IdPessoa and
  (a.DataInicio <= GETDATE() and
  (a.DataTermino > GETDATE() or a.DataTermino is null or a.DataTermino < :1920))
where (p.status = 0 and a.id is null)
```

## MetahConnect.exe

SHA-256: `d348f5cb5ec69dc498c0b2414c8314476c76367d9fa669d33a434e898c32bb54`

Offset 7566660; codificação utf-16-le; cortado: False.

```sql
select * from pessoas p
left join Afastamentos a on p.id = a.IdPessoa and
  (a.DataInicio <= GETDATE() and
  (a.DataTermino > GETDATE() or a.DataTermino is null or a.DataTermino < :1920))
where (p.status = 0 and a.id is null)
```

Offset 10199728; codificação utf-16-le; cortado: False.

```sql
SELECT f.UNIDADE unidade, f.CONTRATO contrato,
  f.INICIOGOZOFERIAS dataIni, f.TERMINOGOZOFERIAS dataFim

FROM RHFERIASCEDIDASPA f
JOIN RHCONTRATOS c ON f.CONTRATO = c.CONTRATO

WHERE c.SITUACAO = 1 AND f.INICIOGOZOFERIAS >= :Ini
```

Offset 10200232; codificação utf-16-le; cortado: False.

```sql
select r.UNIDADE unidade, r.CONTRATO contrato,
  r.DATAINICIOOCORRENCIA dataIni, r.DATATERMINOOCORRENCIA dataFim,
  o.DESCRICAO40 causa

from RHREGOCORRENCIAS r
left join RHOCORRENCIAS o on o.OCORRENCIA = r.OCORRENCIA
join RHCONTRATOS c on r.CONTRATO = c.PESSOA

where c.SITUACAO in (1,2) AND r.DATAINICIOOCORRENCIA >= :Ini
```

Offset 10202756; codificação utf-16-le; cortado: False.

```sql
SELECT * FROM Afastamentos WHERE Id = :Id
```

Offset 10203028; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where Id = :Id 
```

Offset 10203260; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where ID = :id 
```

Offset 10204520; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where a.Id = :Id
```

Offset 10204864; codificação utf-16-le; cortado: False.

```sql
select * from Afastamentos where IdPessoa = :idpessoa and :data between dataInicio and dataTermino
```

Offset 10205224; codificação utf-16-le; cortado: False.

```sql
select id as Id from Afastamentos as a where IdFreq = :IdFreq;
```

Offset 10205792; codificação utf-16-le; cortado: False.

```sql
select Afastamentos.*, p.nome as NomePessoa from Afastamentos inner join Pessoas p on p.id = Afastamentos.idPessoa where IdPessoa = :idpessoa 
```

Offset 10206544; codificação utf-16-le; cortado: False.

```sql
select a.* from Afastamentos a
```

Offset 10206744; codificação utf-16-le; cortado: False.

Padrões LIKE de IdFreq observados: `%-%`.

```sql
SELECT TOP 1 DataInicio FROM Afastamentos  WHERE IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>' AND    IdFreq NOT LIKE '<literal omitido>'   ORDER BY DataInicio DESC
```

Offset 10211048; codificação utf-16-le; cortado: False.

```sql
select a.*, p.nome from Afastamentos a inner join Pessoas p on a.IdPessoa = p.Id where p.Nome like :Nome
```

Offset 10211644; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdPessoa = :IdPessoa AND IdFreq = :IdFreq
```

Offset 10211896; codificação utf-16-le; cortado: False.

```sql
SELECT COUNT(*) as Qtd FROM Afastamentos WHERE IdPessoa = :IdPessoa AND Causa = :Causa AND ((DataInicio BETWEEN :DataInicio AND :DataTermino) OR      (DataTermino BETWEEN :DataInicio AND :DataTermino) OR      (:DataInicio BETWEEN DataInicio AND DataTermino))
```
