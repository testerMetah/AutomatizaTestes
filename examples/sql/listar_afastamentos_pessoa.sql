-- Parâmetro: IdPessoa interno do Acessus.
SELECT Id, IdPessoa, DataInicio, DataTermino, Causa, IdFreq
FROM dbo.Afastamentos
WHERE IdPessoa = ?
ORDER BY DataInicio, Id;
