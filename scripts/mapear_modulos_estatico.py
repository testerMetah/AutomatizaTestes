"""Extrai formulários e menus dos sete executáveis Acessus, sem executá-los."""

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

from automatiza.delphi_resources import Reader, flatten, resource_index


SOURCES = {
    "painel": "Acessus.Modulo.exe", "acesso": "Acessus.exe",
    "refeitorio": "Acessus.Refeitorio.exe", "portaria": "Acessus.Portaria.exe",
    "estacionamento": "Acessus.Estacionamento.exe", "escola": "Acessus.Escola.exe",
    "administracao": "Acessus.Administracao.exe",
}


def routes(root):
    actions = {n["nome"]: n["propriedades"] for n in flatten(root)
               if n["classe"] == "TAction"}
    result = []

    def walk(items, parents=()):
        for item in items:
            action = item.get("Action", "")
            caption = item.get("Caption", actions.get(action, {}).get("Caption", ""))
            caption = caption.replace("&", "")
            if not caption or caption == "-":
                continue
            path = (*parents, caption)
            if item.get("Items"):
                walk(item["Items"], path)
            else:
                result.append({"rota_declarada": list(path), "action": action,
                               "legenda_action": actions.get(action, {}).get("Caption", "").replace("&", ""),
                               "validada_em_execucao": False})

    for node in flatten(root):
        for bar in node["propriedades"].get("ActionBars", []):
            walk(bar.get("Items", []))
    return result


def extract(source_folder, output):
    output.mkdir(parents=True, exist_ok=False)
    maps = output / "formularios"
    maps.mkdir()
    catalog = {"capturado_em": datetime.now().astimezone().isoformat(),
               "metodo": "Recursos estáticos; sem executar binários ou carregar DLLs.",
               "limites": ["Formulário embutido não comprova disponibilidade no módulo.",
                           "Propriedades herdadas podem estar em outro recurso.",
                           "Nomes Delphi não são automaticamente automation_id."],
               "modulos": {}, "formularios_unicos": {}}
    for module, filename in SOURCES.items():
        source = source_folder / filename
        record = {"arquivo": str(source), "formularios": [], "falhas": [], "menus": []}
        catalog["modulos"][module] = record
        if not source.is_file():
            record["falhas"].append({"erro": "Arquivo ausente"})
            continue
        data = source.read_bytes()
        record["sha256"] = hashlib.sha256(data).hexdigest()
        for resource in resource_index(data):
            cls = resource["classe"]
            looks_like_form = (any(term in cls.lower() for term in ("frm", "form", "frame"))
                               or (cls.startswith("TF") and not cls.lower().endswith("dao") and cls != "TFmxObject")
                               or cls.endswith("Dialog"))
            if not looks_like_form:
                continue
            try:
                reader = Reader(data, resource["offset"] + 4)
                root = reader.component()
                encoded = json.dumps(root, ensure_ascii=False, sort_keys=True).encode("utf-8")
                key = hashlib.sha256(encoded).hexdigest()[:20]
                relative = f"formularios/{cls}-{key}.json"
                nodes = list(flatten(root))
                entry = {"classe": cls, "nome": resource["nome"], "offset": resource["offset"],
                         "bytes_lidos": reader.pos - resource["offset"],
                         "caption": root["propriedades"].get("Caption", ""),
                         "componentes": len(nodes), "mapa": relative}
                record["formularios"].append(entry)
                if relative not in catalog["formularios_unicos"]:
                    catalog["formularios_unicos"][relative] = {"classe": cls, "componentes": len(nodes)}
                    (output / relative).write_text(json.dumps(root, ensure_ascii=False, indent=2), encoding="utf-8")
                    lines = [f"# {cls}", "", "Mapa estático, sem validação em execução.", "",
                             "| Caminho Delphi | Classe | Legenda | Campo | Ação/evento |", "|---|---|---|---|---|"]
                    for node in nodes:
                        p = node["propriedades"]
                        cells = [node["caminho"], node["classe"], p.get("Caption", ""),
                                 p.get("DataField", ""), p.get("Action", p.get("OnClick", ""))]
                        lines.append("| " + " | ".join(str(v).replace("|", "\\|").replace("\n", " ").replace("\r", " ") for v in cells) + " |")
                    (output / relative).with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
                declared = routes(root)
                if declared:
                    record["menus"].append({"formulario": cls, "rotas": declared})
            except Exception as exc:
                record["falhas"].append({"classe": cls, "offset": resource["offset"],
                                         "erro": f"{type(exc).__name__}: {exc}"})
        print(json.dumps({"modulo": module, "formularios": len(record["formularios"]),
                          "falhas": len(record["falhas"])}, ensure_ascii=True), flush=True)
    (output / "catalogo.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    return catalog


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--origem", type=Path, default=Path(r"C:\acesso"))
    parser.add_argument("--saida", type=Path, required=True)
    args = parser.parse_args()
    extract(args.origem, args.saida)
