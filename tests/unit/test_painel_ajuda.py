"""Cobertura dos ícones e do conteúdo didático do painel."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HTML = (ROOT / "src/automatiza/painel.html").read_text(encoding="utf-8")
DATA = json.loads((ROOT / "src/automatiza/painel_ajuda.json").read_text(encoding="utf-8"))


class Controls(HTMLParser):
    def __init__(self):
        super().__init__()
        self.missing = []
        self.last_label_help = False
        self.duplicate = []

    def handle_starttag(self, tag, attributes):
        if len(attributes) != len(dict(attributes)):
            self.duplicate.append((tag, attributes))
        attrs = dict(attributes)
        if tag == "label":
            self.last_label_help = bool(attrs.get("data-ajuda"))
        if tag in {"button", "h1", "h2", "th"} and not attrs.get("data-ajuda"):
            self.missing.append((tag, attrs.get("id")))
        if tag in {"input", "select", "textarea"}:
            if not (attrs.get("data-ajuda") or self.last_label_help):
                self.missing.append((tag, attrs.get("id")))
            self.last_label_help = False


def test_todos_os_controles_e_textos_de_ajuda_tem_correspondencia():
    controls = Controls()
    controls.feed(HTML.split("<script>", 1)[0])
    assert not controls.duplicate
    assert not controls.missing

    used = {key for key in re.findall(r'data-ajuda="([^"<]+)"', HTML)
            if "'+" not in key}
    helps = DATA["ajudas"]
    used |= set(re.findall(r"return '([^']+)'", HTML)) & helps.keys()
    assert used <= helps.keys()
    glossary_keys = {"glossario." + term for term in DATA["glossario"]}
    assert 'data-ajuda="glossario.\'+esc(term)' in HTML
    assert glossary_keys <= helps.keys()
    assert helps.keys() == used | glossary_keys
    for key, item in helps.items():
        for field in ("titulo", "o_que_e", "o_que_acontece", "quando_usar", "exemplo",
                      "risco", "como_saber"):
            assert item[field].strip(), (key, field)
        assert item["risco"] in {"Só leitura", "Pode alterar dados"}


def test_catalogo_e_resumos_sao_completos():
    assert len(DATA["catalogo"]) >= 25
    assert len({x["id"] for x in DATA["catalogo"]}) == len(DATA["catalogo"])
    for item in DATA["catalogo"]:
        assert all(item.get(key) for key in ("nome", "serve", "testa", "nao_testa",
                  "tipo", "risco", "banco", "antes", "tempo", "interpreta", "destino", "comando"))
    assert all(5 <= len(lines) <= 8 for lines in DATA["telas"].values())


def test_ajuda_nao_guarda_credenciais():
    text = json.dumps(DATA, ensure_ascii=False)
    assert "PWD=" not in text
    assert "Password=" not in text
    assert "lorem ipsum" not in text.casefold()
