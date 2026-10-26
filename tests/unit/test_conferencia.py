import json
from unittest.mock import MagicMock
import pytest
from automatiza.config import Settings
from automatiza.database import SqlServer
from automatiza.conferencia import capture, compare_files, query_spec


def row(id=1, cause="Férias"):
    return {"Id": id, "IdPessoa": 2, "Causa": cause, "DataInicio": "2026-10-01T00:00:00",
            "DataTermino": None, "IdFreq": str(id)}


def test_filtros_parametrizados():
    sql, params, limit = query_spec({"pessoas": [3, 2, 2], "contrato": 7, "causa": "x'; DROP TABLE x;--"})
    assert params == (1001, 2, 3, 7, "x'; DROP TABLE x;--")
    assert "DROP" not in sql and "a.IdPessoa IN (?,?)" in sql
    assert limit == 1000


@pytest.mark.parametrize("spec", [{}, {"sql": "SELECT 1"}, {"pessoas": [0]}, {"pessoas": [True]},
    {"contrato": -1}, {"causa": ""}, {"limite": 10001, "pessoas": [2]},
    {"inicio_de": "2026-10-01Z"}, {"inicio_de": "2026-10-02", "inicio_ate": "2026-10-01"}])
def test_rejeita_filtros_invalidos(spec):
    with pytest.raises((ValueError, TypeError)):
        query_spec(spec)


def test_limite_nao_salva_truncado(tmp_path):
    db = MagicMock(spec=SqlServer)
    db.query.return_value = [row(1), row(2)]
    with pytest.raises(ValueError, match="Limite excedido"):
        capture(Settings(sql_database="bras1"), {"pessoas": [2], "limite": 1}, tmp_path / "x.json", db=db)
    assert not (tmp_path / "x.json").exists()


def test_compara_alteracoes_reais_e_escapa_html(tmp_path):
    db = MagicMock(spec=SqlServer)
    db.query.side_effect = [[row()], [row(cause="<script>")]]
    settings = Settings(sql_database="bras1", sql_server="teste")
    a, b = tmp_path / "a.json", tmp_path / "b.json"
    capture(settings, {"pessoas": [2]}, a, db=db)
    capture(settings, {"pessoas": [2]}, b, db=db)
    result = compare_files(a, b, tmp_path / "comparacao")
    assert result["eventos"][0]["campos_alterados"] == ["Causa"]
    html = (tmp_path / "comparacao/comparacao.html").read_text(encoding="utf-8")
    assert "<script>" not in html and "&lt;script&gt;" in html
    data = json.loads(b.read_text(encoding="utf-8"))
    data["filtros"] = {"pessoas": [3]}
    b.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError, match="filtros idênticos"):
        compare_files(a, b, tmp_path / "outro")


def test_amostras_de_bases_diferentes_nao_podem_ser_comparadas(tmp_path):
    db = MagicMock(spec=SqlServer)
    db.query.return_value = [row()]
    a, b = tmp_path / 'a.json', tmp_path / 'b.json'
    capture(Settings(sql_database='teste-ferias'), {'pessoas': [2]}, a, db=db)
    capture(Settings(sql_database='teste-ocorrencias'), {'pessoas': [2]}, b, db=db)
    assert json.loads(a.read_text(encoding='utf-8'))['banco'] == 'teste-ferias'
    with pytest.raises(ValueError, match='mesma origem'):
        compare_files(a, b, tmp_path / 'comparacao')
