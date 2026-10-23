from contextlib import contextmanager

import pyodbc

from automatiza.config import Settings


class SqlServer:
    def __init__(self, settings: Settings):
        self.settings = settings

    def assert_database(self):
        """Confirma o destino configurado, sem pressupor um nome fixo de base."""
        expected = configured_database(self.settings)
        actual = self.scalar("SELECT DB_NAME() AS banco")
        if not isinstance(actual, str) or actual.casefold() != expected.casefold():
            raise ValueError("A conexão não está na base configurada; operação recusada.")
        return actual

    @contextmanager
    def connection(self):
        connection = pyodbc.connect(self.settings.connection_string(),
                                    timeout=self.settings.sql_timeout, autocommit=False)
        try:
            connection.timeout = self.settings.sql_timeout
            yield connection
        finally:
            # Consultas nunca confirmam alterações automaticamente.
            try:
                connection.rollback()
            finally:
                connection.close()

    def query(self, sql: str, params=()) -> list[dict]:
        """Execute uma consulta parametrizada; use ? para os parâmetros.

        Use um login com permissão somente de leitura para validações.
        Rollback não transforma SQL arbitrário em SQL seguro/somente leitura.
        """
        with self.connection() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(sql, tuple(params))
                if cursor.description is None:
                    raise ValueError("A consulta precisa retornar colunas.")
                columns = [column[0] for column in cursor.description]
                if len(set(columns)) != len(columns):
                    raise ValueError("Use aliases únicos para as colunas da consulta.")
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
            finally:
                cursor.close()

    def scalar(self, sql: str, params=()):
        rows = self.query(sql, params)
        if len(rows) != 1 or len(rows[0]) != 1:
            raise ValueError("A consulta scalar deve retornar uma linha e uma coluna.")
        return next(iter(rows[0].values()))


def configured_database(settings):
    name = settings.sql_database
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Configure SQL_DATABASE com a base deste teste.")
    return name
