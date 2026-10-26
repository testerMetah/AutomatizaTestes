import pytest


@pytest.mark.banco
def test_sql_server_responde(db):
    assert db.scalar("SELECT CAST(1 AS int) AS resultado") == 1
