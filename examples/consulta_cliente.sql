-- Exemplo: substitua tabela e colunas pelos nomes reais.
-- O ? recebe um parâmetro pelo pyodbc.
SELECT codigo, nome
FROM dbo.Clientes
WHERE codigo = ?;
