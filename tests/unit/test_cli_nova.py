from pathlib import Path
from unittest.mock import Mock

import pytest

from automatiza.nova_cli import parser_cli
from automatiza.processos_auditorias import descobrir
from automatiza.relatorio_auditorias import agrupar_erros, comparar, normalizar
from automatiza.perfis_teste import validar_escrita
from automatiza.oraculos_auditorias import verificar


def test_cli_filtros_e_confirmacao():
    args = parser_cli().parse_args(["auditorias", "--modulo", "escola",
                                    "--extremo", "--pular", "1,3"])
    assert args.extremo and args.pular == "1,3"
    assert not parser_cli().parse_args(["ciclos", "planejar", "--arquivo", "x",
                                        "--saida", "y"]).confirmo_escrita


def test_descobre_por_caminho_absoluto(tmp_path):
    exe = tmp_path / "Acessus.exe"
    exe.touch()
    found = descobrir(exe, enum_processes=lambda: [7, 8],
                      resolver=lambda pid: exe if pid == 8 else tmp_path / "outro.exe")
    assert found == 8


def test_agrupa_mensagens_variaveis():
    records = [{"status": "ERRO_APLICACAO", "mensagens_consulta": [
        {"mensagens": ["Coluna ambígua 123 em 0xAABB"]}]},
        {"status": "ERRO_APLICACAO", "mensagens_consulta": [
            {"mensagens": ["coluna ambígua 456 em 0xCCDD"]}]}]
    assert agrupar_erros(records)[0]["quantidade"] == 2


def test_compara_estado_por_modulo_historico_filtro(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    a.mkdir(); b.mkdir()
    (a / "tentativas.jsonl").write_text(
        '{"modulo":"escola","historico":"Alunos","filtro":"Pessoa","status":"ERRO_APLICACAO"}\n', encoding="utf-8")
    (b / "tentativas.jsonl").write_text(
        '{"modulo":"escola","historico":"Alunos","filtro":"Pessoa","status":"CONSULTADO"}\n', encoding="utf-8")
    result = comparar(a, b)
    assert len(result["corrigidos"]) == 1


def test_valida_banco_antes_de_conectar(monkeypatch):
    monkeypatch.setattr("automatiza.perfis_teste.permitidos", lambda: {"base_teste"})
    settings = Mock(sql_database="producao")
    with pytest.raises(ValueError, match="fora da lista"):
        validar_escrita(settings)


def test_oraculo_so_roda_regra_confirmada():
    record = {"modulo": "acesso", "historico": "Pessoas", "filtro": "Pessoa",
              "valor_exibido": "123", "contagem": 2}
    assert verificar(Mock(), record, rules=[]) is None
    db = Mock()
    db.scalar.return_value = 2
    rule = {"modulo": "acesso", "historico": "Pessoas", "filtro": "Pessoa",
            "sql": "SELECT COUNT(*) FROM [HISTORICO_PESSOAS] WHERE [id_pessoa] = ?"}
    assert verificar(db, record, rules=[rule])["status"] == "PASSOU"
    db.scalar.assert_called_once_with(rule["sql"], ("123",))
