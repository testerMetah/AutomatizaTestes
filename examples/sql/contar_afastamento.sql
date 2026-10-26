-- Parâmetros: IdPessoa interno do Acessus, DataInicio, DataTermino e Causa.
-- Use os horários completos esperados na integração, inclusive no término.
SELECT COUNT(*) AS quantidade
FROM dbo.Afastamentos
WHERE IdPessoa = ?
  AND DataInicio = CONVERT(datetime, ?, 126)
  AND DataTermino = CONVERT(datetime, ?, 126)
  AND Causa = ?;
