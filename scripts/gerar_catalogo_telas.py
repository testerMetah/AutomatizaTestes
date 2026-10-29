"""Gera inventários e mapas iniciais dos forms ligados aos menus Delphi.

Nunca valida um seletor: mapas gerados ficam bloqueados até inspeção da UI.
Não sobrescreve arquivos existentes, para preservar análise manual.
"""

from pathlib import Path
import re
import sys
import unicodedata
import yaml

sys.path.insert(0, str(Path(__file__).parent))
from gerar_mapa_fonte import FONTE, MODULOS, principal, menus, acoes, procedimentos, indice_forms
from extrair_telas_refeitorio import controles, literais_mensagem

PROJETO = Path(r"C:\AutomatizaTestes")
MAPAS = PROJETO / "src/automatiza/mapas"
FICHAS = PROJETO / "docs/telas/estatico"
SUITES = PROJETO / "tests/telas"
INTERATIVOS = ("Edit", "ComboBox", "CheckBox", "Radio", "Button", "DBGrid", "ListBox", "DateTimePicker")


def tipo_controle(classe):
    if "Edit" in classe or "DateTimePicker" in classe:
        return "campo de texto/data"
    if "Combo" in classe or "Check" in classe or "Radio" in classe or "ListBox" in classe:
        return "seleção"
    if "Button" in classe or classe == "TAction":
        return "ação"
    if "Grid" in classe:
        return "grade"
    if "Label" in classe:
        return "rótulo"
    if any(x in classe for x in ("Panel", "TabSheet", "PageControl", "GroupBox")):
        return "contêiner"
    return "outro"


def metodos_relevantes(pas):
    if not pas.exists():
        return []
    linhas = pas.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    declaracoes = [(i, m.group(1)) for i, linha in enumerate(linhas)
                   if (m := re.match(r"^\s*(?:procedure|function)\s+\w+\.(\w+)", linha, re.I))]
    resultado = []
    for pos, (inicio, nome) in enumerate(declaracoes):
        if not re.search(r"Validar|Grava|Salvar|Excluir|Cancelar|Consultar|Relat|ActIr|ActIncluir|ActExibir|FormCreate", nome, re.I):
            continue
        fim = declaracoes[pos + 1][0] if pos + 1 < len(declaracoes) else len(linhas)
        corpo = "\n".join(linhas[inicio:fim])
        chamadas = list(dict.fromkeys(re.findall(r"\b(?:F\w+(?:Controller|DAO)|\w+Controller)\.\w+", corpo)))
        resultado.append((nome, inicio + 1, chamadas[:8]))
    return resultado


def slug(valor):
    valor = unicodedata.normalize("NFKD", valor).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "_", valor).strip("_")


def nome_logico(controle):
    nome, classe = controle["nome"], controle["classe"]
    n = re.sub(r"^(Ed|edt|ed|cmb|Cmb|cbx|Cbx|chk|Chk|btn|Btn|gbx|rg|Grid|Dbg|MEd)", "", nome)
    prefixo = "campo" if "Edit" in classe or "DateTime" in classe else "btn" if "Button" in classe else "grid" if "Grid" in classe else "opcao"
    return slug(f"{prefixo}_{n or nome}")


def montar():
    MAPAS.mkdir(parents=True, exist_ok=True)
    FICHAS.mkdir(parents=True, exist_ok=True)
    SUITES.mkdir(parents=True, exist_ok=True)
    indice = indice_forms()
    registrados = set()
    linhas_indice = ["# Catálogo estático de telas", "", "Gerado da fonte GitHub. Mapas e suítes ficam pendentes de validação na UI do build instalado; cenários não validados são ignorados pelo Robot.", "", "| Tela | Rota | DFM | Ficha | YAML | Robot |", "|---|---|---|---|---|---|"]
    for modulo in MODULOS:
        try:
            raiz = principal(modulo)
        except (StopIteration, FileNotFoundError):
            continue
        principal_class = re.search(r":\s*(T\w+)", raiz.read_text(encoding="utf-8-sig", errors="replace").splitlines()[0]).group(1)
        handlers = acoes(raiz)
        procs = procedimentos(raiz.with_suffix(".pas"))
        for pais, item in menus(raiz):
            handler = handlers.get(item["action"], "")
            rota = [p["caption"] for p in pais if p["caption"] and p["caption"] != "-"] + [item["caption"]]
            for form in procs.get(handler, []):
                chave = form.lower()
                if chave in registrados or chave not in indice:
                    continue
                registrados.add(chave)
                dfm = sorted(indice[chave], key=lambda x: len(str(x)))[0]
                pas = dfm.with_suffix(".pas")
                nome = ("estacionamento_cadastro_veiculos" if chave == "tfrmestacionamentoviewscadastroveiculos"
                        else f"{slug(modulo)}_{slug(form)}")
                mapa_path = MAPAS / f"{nome}.yaml"
                ficha_path = FICHAS / f"{nome}.md"
                robot_path = SUITES / f"{nome}.robot"
                itens = controles(dfm)
                mapa = {"nome": nome, "form_class": form, "principal_class": principal_class,
                        "backend": "win32", "menu_backend": "uia", "menu": rota,
                        "validado_na_ui": False, "fonte": dfm.relative_to(FONTE).as_posix(), "controles": {}}
                for c in itens:
                    if not any(t in c["classe"] for t in INTERATIVOS):
                        continue
                    logico = nome_logico(c)
                    if logico in mapa["controles"]:
                        logico += "_" + slug(c["nome"])
                    mapa["controles"][logico] = {"class_name": c["classe"], "nome_dfm": c["nome"],
                                                    "found_index": None}
                if not mapa_path.exists():
                    mapa_path.write_text(yaml.safe_dump(mapa, allow_unicode=True, sort_keys=False), encoding="utf-8")
                doc = [f"# {modulo}: {form}", "", f"> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: {' > '.join(rota)}.", "", f"- DFM: `{dfm.relative_to(FONTE).as_posix()}`", f"- PAS: `{pas.relative_to(FONTE).as_posix()}`", f"- Handler de abertura: `{handler}`", "", "## Controles", "", "| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |", "|---|---|---|---|---:|---|---:|---|"]
                for c in itens:
                    padrao = ", ".join(f"{k}={c[k]}" for k in ("Text", "ItemIndex", "Checked", "Visible", "Enabled") if k in c)
                    doc.append("| " + " | ".join(str(x).replace("|", "\\|") for x in (c["nome"], c["classe"], tipo_controle(c["classe"]), c.get("Caption", "—"), c.get("TabOrder", "—"), c.get("EditMask", "—"), c.get("MaxLength", "—"), padrao or "—")) + " |")
                doc += ["", "## Procedures relevantes da unit", "", "A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.", "", "| Procedure | Linha | Chamadas identificadas |", "|---|---:|---|"]
                doc += [f"| `{nome_metodo}` | {linha} | {', '.join('`'+c+'`' for c in chamadas) or '—'} |" for nome_metodo, linha, chamadas in metodos_relevantes(pas)]
                doc += ["", "## Mensagens literais da unit", "", "Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.", ""]
                doc += [f"- Linha {n}: `{msg}`" for n, msg in literais_mensagem(pas)] if pas.exists() else []
                if not doc[-1].startswith("- Linha"):
                    doc.append("- Nenhum literal simples encontrado.")
                doc += ["", "## Pendente", "", "Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.", ""]
                ficha_path.write_text("\n".join(doc), encoding="utf-8")
                if not robot_path.exists():
                    robot_path.write_text(f"*** Settings ***\nLibrary    automatiza.biblioteca_telas.BibliotecaTelas\nTest Teardown    Fechar Tela\n\n*** Test Cases ***\nFumaca {form}\n    [Tags]    smoke    cadastro-{slug(form)}    desktop    mapa-estatico\n    Mapa Deve Estar Validado    {nome}\n    Abrir Tela    {nome}\n", encoding="utf-8")
                linhas_indice.append(f"| `{form}` | {' > '.join(rota)} | `{dfm.relative_to(FONTE).as_posix()}` | [{nome}.md](estatico/{nome}.md) | `{nome}.yaml` | `{nome}.robot` |")
    (PROJETO / "docs/telas/README_catalogo_geral.md").write_text("\n".join(linhas_indice) + "\n", encoding="utf-8")
    print(f"Forms catalogados: {len(registrados)}")


if __name__ == "__main__":
    montar()
