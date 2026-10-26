"""Consolida os arquivos locais da inspeção; não acessa janelas nem SQL."""

import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from navegar_inspecao import FOLDER, MODULES, ROOT


DOCS = ROOT / "docs/mapeamentos/acessus-completo"
STATIC = DOCS / "estatico-20261015-v2"


def nodes(root):
    yield root
    for child in root.get("filhos", []):
        yield from nodes(child)


def md(value):
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def consolidate():
    static = json.loads((STATIC / "catalogo.json").read_text(encoding="utf-8"))
    output = {"gerado_em": datetime.now().astimezone().isoformat(),
              "sessao": str(FOLDER.relative_to(ROOT)),
              "catalogo_estatico": str((STATIC / "catalogo.json").relative_to(ROOT)),
              "formularios_estaticos_distintos": len(static["formularios_unicos"]),
              "componentes_estaticos_distintos": sum(f["componentes"] for f in static["formularios_unicos"].values()),
              "limites": ["Inspeção de navegação e controles, sem validar regras de negócio.",
                          "Formulários vazios de inclusão foram cancelados; sem preenchimento ou salvamento.",
                          "Não foram acionados botões de processamento, exclusão, impressão ou envio a equipamentos.",
                          "Menus UIA têm filhos espúrios; hierarquia declarada vem de ActionBars e rotas observadas.",
                          "Leitura de abas por TabControlWrapper causou erro COMCTL32; técnica abandonada.",
                          "Formulários embutidos nos executáveis podem não estar disponíveis no módulo.",
                          "Valores de campos, grades e listas foram omitidos dos mapas em execução."],
              "modulos": {}}
    code = {"observacao": "Rotas observadas e seletores candidatos. Revalidar unicidade ao conectar; não executar ações automaticamente.",
            "modulos": {}}
    overview = ["# Inspeção do painel e dos seis módulos", "", "Inspeção autorizada em 15/10/2026.", "",
                "Mapas de navegação e controles para preparar a automação. A abertura de uma tela não valida suas regras de negócio.", "",
                "| Módulo | Rotas declaradas | Inspecionadas | Diálogos/avisos | Outras situações |", "|---|---:|---:|---:|---:|"]
    registry = json.loads((FOLDER / "modulos.json").read_text(encoding="utf-8"))
    panel_help = json.loads((FOLDER / "painel-percurso.json").read_text(encoding="utf-8")) if (FOLDER / "painel-percurso.json").exists() else {}
    output["painel"] = {"mapa": str((FOLDER / "painel-corrigido.json").relative_to(ROOT)),
                         "modulos": registry, "ajuda": panel_help,
                         "nao_acionados": ["Modulos > LogOff", "Modulos > Sair"]}
    code["painel"] = {"janela": {"class_name": "TFrmModuloViewsPrincipal"},
                       "barra_menus": {"class_name": "TActionMainMenuBar"},
                       "metodo_observado": "UIA: click_input no menu e em cada item da rota.",
                       "limites": "Sem HMENU nativo nesta sessão; select/Invoke UIA falhou. Não presumir que menu_select funciona.",
                       "modulos": {m: data.get("rota_painel") for m, data in registry.items()}}
    panel_doc = ["# Painel de Módulos", "", "Classe observada: `TFrmModuloViewsPrincipal`.",
                 "Título observado: Sistema Acessus | Painel de Módulos - v2.10.0.", "",
                 "Os seis módulos foram abertos pelo menu `Modulos`. Os botões gráficos são `THoverButton` sem título acessível;",
                 "seus IDs numéricos mudam entre sessões. Preferir as rotas de menu observadas.", "",
                 "| Módulo | Rota confirmada |", "|---|---|"]
    for module, (caption, _) in MODULES.items():
        panel_doc.append(f"| [{caption}]({module}.md) | Modulos → {caption} |")
    panel_doc.extend(["", "Ajuda → Novidades foi aberta, mapeada e fechada. LogOff e Sair não foram acionados.",
                      "", "Os mapas estão em `reports/inspecao-telas/20261015/painel-corrigido.json` e `painel-novidades-1.json`.",
                      "A imagem do painel está em `reports/inspecao-telas/20261015/painel.png`.", "",
                      "A barra é `TActionMainMenuBar`, sem HMENU nativo observado. A sessão usou `click_input` em itens UIA;",
                      "`select`/Invoke UIA falhou. A árvore UIA repete irmãos como filhos em alguns itens: não inferir submenus recursivamente.", ""])
    (DOCS / "painel.md").write_text("\n".join(panel_doc), encoding="utf-8")
    for module, (caption, main_class) in MODULES.items():
        expected = next(m["rotas"] for m in static["modulos"][module]["menus"] if m["formulario"] == main_class)
        log = FOLDER / f"{module}-percurso.jsonl"
        current = {}
        if log.exists():
            for line in log.read_text(encoding="utf-8").splitlines():
                item = json.loads(line)
                current[item["indice"]] = item
        records = []
        code_module = {"painel": registry.get(module, {}).get("rota_painel"),
                       "principal": {"class_name": main_class, "title": registry.get(module, {}).get("titulo")}, "telas": []}
        lines = [f"# {caption}", "", "| Rota | Situação | Formulário observado | Mapas ao vivo |", "|---|---|---|---|"]
        for index, route in enumerate(expected, 1):
            record = current.get(index, {"indice": index, **route, "situacao": "PENDENTE", "mapas": []})
            if record["situacao"] == "INSPECIONADA":
                record["validada_em_execucao"] = True
            records.append(record)
            title = "; ".join(f"{w['classe']} — {w['titulo']}" for w in record.get("janelas", []))
            links = " ".join(f"[{n + 1}](../../../{filename.replace(chr(92), '/')})"
                             for n, filename in enumerate(record.get("mapas", [])))
            lines.append("| " + " | ".join(md(x) for x in (" → ".join(route["rota_declarada"]), record["situacao"], title, links)) + " |")
            screen = {"action_delphi": route["action"], "rota_declarada": route["rota_declarada"],
                      "rota_observada": record.get("rota_observada"), "situacao": record["situacao"],
                      "formularios": []}
            state_maps = list(record.get("mapas", []))
            state_maps.extend(a["mapa"] for a in record.get("abas", []))
            state_maps.extend(a["mapa"] for a in record.get("abas_inclusao", []))
            for filename in dict.fromkeys(state_maps):
                path = ROOT / filename
                if not path.is_file():
                    continue
                snap = json.loads(path.read_text(encoding="utf-8"))
                tree = snap["janela"]
                visible = [n for n in nodes(tree) if n["visivel"]]
                signatures = Counter((n["classe"], n.get("texto")) for n in visible)
                form = {"janela": {"class_name": tree["classe"], "title": tree["texto"]},
                        "mapa_execucao": filename, "rota_captura": snap["rota"],
                        "controles_visiveis": len(visible), "botoes_com_titulo_unico_na_captura": [],
                        "formularios_estaticos": [str((STATIC / f["mapa"]).relative_to(ROOT))
                            for f in static["modulos"][module]["formularios"] if f["classe"] == tree["classe"]]}
                for node in visible:
                    text = node.get("texto")
                    if "button" in node["classe"].lower() and text and signatures[(node["classe"], text)] == 1:
                        form["botoes_com_titulo_unico_na_captura"].append({"class_name": node["classe"], "title": text,
                                                                                     "enabled": node["habilitado"]})
                screen["formularios"].append(form)
            code_module["telas"].append(screen)
        counts = Counter(r["situacao"] for r in records)
        output["modulos"][module] = {"rotas": records, "totais": dict(counts),
                                       "formularios_embutidos": len(static["modulos"][module]["formularios"])}
        code["modulos"][module] = code_module
        overview.append(f"| [{caption}]({module}.md) | {len(expected)} | {counts['INSPECIONADA']} | {counts['DIALOGO_OBSERVADO']} | {len(expected) - counts['INSPECIONADA'] - counts['DIALOGO_OBSERVADO']} |")
        lines.extend(["", "## Arquivos e uso", "",
                      "As árvores em execução e as abas estão referenciadas no [catálogo consolidado](catalogo-telas.json).",
                      "As rotas, classes, títulos e botões candidatos estão em [rotas para o código](rotas-para-codigo.json).",
                      "Os formulários estáticos incluem campos, rótulos, posições declaradas, eventos e componentes não visuais.",
                      "Não usar handles, IDs numéricos ou coordenadas de uma sessão como seletores permanentes.", ""])
        (DOCS / f"{module}.md").write_text("\n".join(lines), encoding="utf-8")
    all_records = [r for data in output["modulos"].values() for r in data["rotas"]]
    output["totais"] = {"rotas_declaradas": len(all_records),
                          "rotas_inspecionadas": sum(r["situacao"] == "INSPECIONADA" for r in all_records),
                          "variacoes_de_abas": sum(len(r.get("abas", [])) + len(r.get("abas_inclusao", [])) for r in all_records),
                          "inclusoes_vazias_canceladas": sum("cancelado sem salvar" in r.get("inclusao", "") for r in all_records)}
    totals = output["totais"]
    overview.extend(["", f"Foram inspecionadas {totals['rotas_inspecionadas']} rotas, {totals['variacoes_de_abas']} variações de abas e {totals['inclusoes_vazias_canceladas']} formulários vazios de inclusão, cancelados sem salvar.",
                     "", "## Material salvo", "",
                     "- [Painel de Módulos](painel.md): módulos, abertura e ajuda.",
                     "- [Catálogo consolidado](catalogo-telas.json): cobertura, rotas, abas, avisos e pendências.",
                     "- [Rotas para o código](rotas-para-codigo.json): classes, títulos e botões únicos nas capturas.",
                     "- [Catálogo estático](estatico-20261015-v2/catalogo.json): fontes, hashes e mapas de formulários.",
                     f"- {output['formularios_estaticos_distintos']} estruturas distintas e {output['componentes_estaticos_distintos']} componentes declarados, incluindo não visuais.",
                     "- Árvores de execução e histórico em `reports/inspecao-telas/20261015`.", "",
                     "## Limites e ocorrências", ""] + ["- " + s for s in output["limites"]] + ["",
                     "A opção Administração → Opções do Sistema existe no recurso, mas não aparece no menu em execução. A causa não foi confirmada.",
                     "As quatro opções Sair dos módulos e LogOff/Sair do painel foram inventariadas sem acionamento.", "",
                     "As barras TActionMainMenuBar não expuseram HMENU nativo. A navegação desta sessão usou cliques em itens UIA.",
                     "Os métodos atuais do projeto que dependem de menu_select precisam considerar essa diferença antes da automação dos cenários.", "",
                     "Arquivos iniciais sem o sufixo `validado` para as janelas principais e o mapa `acesso-pessoas-inicial.json`",
                     "foram substituídos por capturas com a hierarquia corrigida. O mapa inicial `painel.json` também foi substituído",
                     "por `painel-corrigido.json`; não inferir submenus pela árvore UIA inicial.", ""])
    for filename, payload in [("catalogo-telas.json", output), ("rotas-para-codigo.json", code)]:
        (DOCS / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    (DOCS / "LEIA-ME.md").write_text("\n".join(overview), encoding="utf-8")
    manifest = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                for base in [DOCS, FOLDER] for p in base.rglob("*")
                if p.is_file() and p.name != "manifesto-sha256.json"}
    (FOLDER / "manifesto-sha256.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({m: d["totais"] for m, d in output["modulos"].items()}, ensure_ascii=True))


if __name__ == "__main__":
    consolidate()
