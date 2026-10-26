"""Leitura estática de formulários TPF0 dos binários Delphi instalados.

Não carrega/executa DLLs, não acessa processos e não controla janelas.
Suporte voltado aos recursos encontrados nesta instalação; tipos desconhecidos
são recusados em vez de tentar adivinhar o restante do formulário.
"""

import hashlib
import json
import re
import struct
from pathlib import Path

SAFE_PROPERTIES = {
    "Caption", "Hint", "Left", "Top", "Width", "Height", "ClientWidth", "ClientHeight",
    "TabOrder", "Enabled", "Visible", "PasswordChar", "MaxLength", "Tag", "Align",
    "ModalResult", "Default", "Cancel", "DataField", "DataSource", "ReadOnly", "EditMask",
    "OnClick", "OnChange", "OnExit", "OnEnter", "OnKeyPress", "OnShow", "OnCreate",
    "Items.Strings", "Columns", "FieldName", "DisplayLabel", "DisplayWidth", "Title.Caption",
    "ShortCut", "GroupIndex", "Checked", "AutoCheck", "AllowAllUp", "TabStop", "Style",
    "Action", "ActionBars", "Items", "ActionBar", "Category", "ImageIndex",
    "Tabs.Strings", "ActivePage", "FormStyle", "BorderStyle", "ShowHint",
    "TextHint", "OnExecute", "OnUpdate",
}


class ResourceError(ValueError):
    pass


class Reader:
    def __init__(self, data, offset=0):
        self.data, self.pos = data, offset

    def read(self, size):
        if size < 0 or self.pos + size > len(self.data):
            raise ResourceError(f"Recurso truncado no offset {self.pos}.")
        value = self.data[self.pos:self.pos + size]
        self.pos += size
        return value

    def number(self, fmt):
        return struct.unpack("<" + fmt, self.read(struct.calcsize("<" + fmt)))[0]

    def peek(self):
        if self.pos >= len(self.data):
            raise ResourceError("Fim inesperado de recurso.")
        return self.data[self.pos]

    def short(self):
        return self.read(self.number("B")).decode("cp1252", errors="replace")

    def value(self, depth=0):
        if depth > 100:
            raise ResourceError("Profundidade excessiva.")
        tag = self.number("B")
        if tag in (0, 13):
            return None
        if tag == 1:
            values = []
            while self.peek() != 0:
                values.append(self.value(depth + 1))
            self.read(1)
            return values
        if tag in (2, 3, 4, 15, 17, 19, 21, 22):
            return self.number({2: "b", 3: "h", 4: "i", 15: "f", 17: "d", 19: "q", 21: "d", 22: "Q"}[tag])
        if tag == 5:
            # O float Extended de 80 bits não é necessário para os seletores.
            return {"extended80": self.read(10).hex()}
        if tag in (6, 7):
            return self.short()
        if tag in (8, 9):
            return tag == 9
        if tag == 10:
            length = self.number("i")
            if length < 0 or self.pos + length > len(self.data):
                raise ResourceError("Comprimento binário inválido.")
            self.pos += length
            return {"binario_omitido_bytes": length}
        if tag == 11:
            values = []
            while True:
                item = self.short()
                if not item:
                    return values
                values.append(item)
        if tag in (12, 18, 20):
            length = self.number("i")
            if tag == 18:
                return self.read(length * 2).decode("utf-16-le", errors="replace")
            return self.read(length).decode("utf-8" if tag == 20 else "cp1252", errors="replace")
        if tag == 14:
            values = []
            while self.peek() != 0:
                index = self.value(depth + 1) if self.peek() in (2, 3, 4) else None
                if self.number("B") != 1:
                    raise ResourceError(f"Item de coleção inválido no offset {self.pos}.")
                item = self.properties(depth + 1)
                if index is not None:
                    item["indice"] = index
                values.append(item)
            self.read(1)
            return values
        if tag == 16:
            return str(self.number("q") / 10000)
        raise ResourceError(f"Tipo de propriedade não suportado: {tag}, offset {self.pos - 1}.")

    def properties(self, depth=0):
        properties = {}
        while True:
            name = self.short()
            if not name:
                return properties
            value = self.value(depth + 1)
            if name in SAFE_PROPERTIES:
                properties[name] = value

    def header(self):
        flags, position = 0, None
        if self.peek() & 0xF0 == 0xF0:
            flags = self.number("B") & 0x0F
            if flags & 2:
                position = self.value()
        class_name, name = self.short(), self.short()
        if not re.fullmatch(r"T[A-Za-z_][A-Za-z_0-9]*", class_name):
            raise ResourceError("Cabeçalho de componente inválido.")
        return class_name, name, flags, position

    def component(self, depth=0):
        if depth > 100:
            raise ResourceError("Hierarquia excessiva.")
        class_name, name, flags, position = self.header()
        node = {"classe": class_name, "nome": name, "herdado": bool(flags & 1),
                "propriedades": self.properties(), "filhos": []}
        if position is not None:
            node["ordem_herdada"] = position
        while self.peek() != 0:
            node["filhos"].append(self.component(depth + 1))
        self.read(1)
        return node


def resource_index(data):
    roots = []
    for match in re.finditer(b"TPF0", data):
        try:
            class_name, name, _, _ = Reader(data, match.start() + 4).header()
        except ResourceError:
            continue
        roots.append({"offset": match.start(), "classe": class_name, "nome": name})
    return roots


def flatten(node, parent=""):
    path = parent + "/" + node["nome"]
    yield {"caminho": path, **{key: node[key] for key in ("classe", "nome", "herdado", "propriedades")}}
    for child in node["filhos"]:
        yield from flatten(child, path)


def menu_paths(node, parents=()):
    caption = node["propriedades"].get("Caption", "")
    current = parents
    if node["classe"] == "TMenuItem" and caption and caption != "-":
        current = (*parents, caption.replace("&", ""))
        yield "->".join(current)
    for child in node["filhos"]:
        yield from menu_paths(child, current)


def map_resource(source, class_name, output):
    source = Path(source).resolve()
    data = source.read_bytes()
    matches = [item for item in resource_index(data) if item["classe"] == class_name]
    if len(matches) != 1:
        raise ResourceError(f"Esperado um recurso {class_name}; encontrados {len(matches)}.")
    reader = Reader(data, matches[0]["offset"] + 4)
    root = reader.component()
    result = {"origem": str(source), "sha256": hashlib.sha256(data).hexdigest(), "offset": matches[0]["offset"],
              "bytes_lidos": reader.pos - matches[0]["offset"],
              "metodo": "Recurso binário estático; não é inspeção de controles em execução.",
              "arvore": root, "menus": list(menu_paths(root))}
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    def cell(value):
        return str(value).replace("|", "\\|").replace("\r", " ").replace("\n", " ")
    lines = ["# " + class_name, "", "Origem: " + str(source), "",
             "Mapa estático dos recursos instalados. Não confirma visibilidade, estado ou seletores de execução.",
             "Componentes herdados podem ter propriedades apenas no formulário ancestral. Nomes Delphi não são automaticamente automation_id.",
             "", "| Componente | Classe | Legenda | DataField | TabOrder | Enabled |", "|---|---|---|---|---|---|"]
    for node in flatten(root):
        props = node["propriedades"]
        values = (node["nome"], node["classe"], props.get("Caption", ""), props.get("DataField", ""),
                  props.get("TabOrder", ""), props.get("Enabled", "não explícito"))
        lines.append("| " + " | ".join(cell(value) for value in values) + " |")
    if result["menus"]:
        lines += ["", "## Menus declarados", ""] + ["- " + item for item in result["menus"]]
    output.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return result
