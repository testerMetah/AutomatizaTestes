import json
import struct

import pytest

from automatiza.delphi_resources import Reader, ResourceError, flatten, map_resource, menu_paths, resource_index


def short(value):
    data = value.encode("cp1252")
    return bytes([len(data)]) + data


def component(class_name, name, properties=b"", children=b"", prefix=b""):
    return prefix + short(class_name) + short(name) + properties + b"\0" + children + b"\0"


def prop(name, tag, data):
    return short(name) + bytes([tag]) + data


def test_utf8_binario_e_propriedades_sensiveis_omitidas(tmp_path):
    caption = "Férias Cedidas".encode("utf-8")
    properties = prop("Caption", 20, struct.pack("<i", len(caption)) + caption)
    properties += prop("Picture.Data", 10, struct.pack("<i", 5) + b"image")
    properties += prop("Text", 6, short("segredo-teste"))
    child = component("TEdit", "Contrato", prop("TabOrder", 2, b"\x00"))
    data = b"TPF0" + component("TForm", "Ferias", properties, child)
    source, output = tmp_path / "rh.bin", tmp_path / "mapa.json"
    source.write_bytes(data)
    result = map_resource(source, "TForm", output)
    assert result["arvore"]["propriedades"] == {"Caption": "Férias Cedidas"}
    assert len(list(flatten(result["arvore"]))) == 2
    assert result["bytes_lidos"] == len(data)
    assert "segredo-teste" not in output.read_text(encoding="utf-8")
    assert "image" not in output.read_text(encoding="utf-8")
    assert source.read_bytes() == data


def test_componente_herdado_com_ordem_nao_perde_alinhamento():
    data = component("TForm", "Main", prefix=b"\xf3\x02\x04")
    root = Reader(data).component()
    assert root["herdado"] is True
    assert root["ordem_herdada"] == 4


def test_colecao_e_tipos_numericos_de_propriedade():
    item = prop("FieldName", 6, short("DataInicio")) + prop("Width", 3, struct.pack("<h", 120))
    collection = b"\x01" + item + b"\0\0"
    root = Reader(component("TDBGrid", "Grid", prop("Columns", 14, collection))).component()
    assert root["propriedades"]["Columns"] == [{"FieldName": "DataInicio", "Width": 120}]


def test_menu_produz_caminho_sem_aceleradores():
    leaf = component("TMenuItem", "Ferias", prop("Caption", 6, short("Férias Cedidas...")))
    top = component("TMenuItem", "Programacoes", prop("Caption", 6, short("&Programações")), leaf)
    root = Reader(component("TMainMenu", "Menu", children=top)).component()
    assert list(menu_paths(root))[-1] == "Programações->Férias Cedidas..."


def test_recurso_truncado_ou_tipo_desconhecido_nao_gera_mapa_parcial(tmp_path):
    with pytest.raises(ResourceError, match="suportado"):
        Reader(component("TForm", "Main", prop("Caption", 99, b""))).component()
    source = tmp_path / "rh.bin"
    source.write_bytes(b"TPF0" + component("TForm", "Main")[:-1])
    output = tmp_path / "mapa.json"
    with pytest.raises(ResourceError):
        map_resource(source, "TForm", output)
    assert not output.exists()
