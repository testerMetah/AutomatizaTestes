"""Inventário de controles de uma janela autorizada, sem ler campos de dados.

Não abre sistemas nem aciona controles. A navegação é feita separadamente.
"""

import argparse
import json
import ctypes
from collections import Counter
from datetime import datetime
from pathlib import Path

from pywinauto import Application, Desktop


BASE = Path(__file__).resolve().parents[1] / "reports" / "inspecao-telas"
DATA_CLASSES = ("edit", "memo", "grid", "listview", "listbox", "combobox",
                "richedit", "statusbar", "datetime", "monthcal")


def window_list(pid):
    return [{"handle_sessao": w.handle, "classe": w.class_name(),
             "titulo": w.window_text(), "visivel": w.is_visible(),
             "habilitado": w.is_enabled()}
            for w in Desktop(backend="win32").windows(process=pid,
                                                        visible_only=False)]


def menu_tree(window):
    """Lê menus e um nível de itens. O provider Delphi cria filhos espúrios.

    Não recursar nos filhos das opções: em algumas versões eles repetem os
    irmãos seguintes como se fossem submenus. Submenus exigem inspeção própria
    ou a estrutura ActionBars extraída estaticamente.
    """
    app = Application(backend="uia").connect(process=window.process_id())
    root = app.window(handle=window.handle).wrapper_object()

    def walk(control, route=(), depth=0):
        result = []
        for child in control.children():
            info = child.element_info
            if info.control_type not in {"MenuItem", "Menu", "MenuBar"}:
                continue
            name = info.name.replace("&", "")
            current = (*route, name) if info.control_type == "MenuItem" else route
            result.append({"nome": name, "tipo": info.control_type,
                           "rota": list(current), "habilitado": child.is_enabled(),
                           "filhos": walk(child, current, depth + 1) if depth < 1 else [],
                           "submenus_nao_inferidos": depth >= 1})
        return result

    menus = []
    for bar in root.children():
        if bar.element_info.control_type == "MenuBar":
            menus.extend(walk(bar))
    return menus


def snapshot(handle, folder, slug, module, route, *, include_menus=True):
    window = Desktop(backend="win32").window(handle=handle).wrapper_object()

    def walk(control, path=(), index=0, suppressed=False, depth=0):
        cls = control.class_name()
        suppressed = suppressed or any(term in cls.lower() for term in DATA_CLASSES)
        current = (*path, f"{cls}[{index}]")
        rect = control.rectangle()
        entry = {"classe": cls, "caminho_estrutural": list(current),
                 "visivel": control.is_visible(), "habilitado": control.is_enabled(),
                 "texto": None if suppressed else control.window_text(),
                 "valor_omitido": suppressed,
                 "handle_sessao": control.handle,
                 "id_controle_sessao": control.control_id(), "filhos": []}
        entry["retangulo_sessao"] = {"left": rect.left, "top": rect.top,
                                     "right": rect.right, "bottom": rect.bottom}
        # Não enumerar linhas/células nem itens de controles com dados.
        if not suppressed and depth < 25:
            counts = Counter()
            for child in control.children():
                if ctypes.windll.user32.GetParent(child.handle) != control.handle:
                    continue
                child_class = child.class_name()
                idx = counts[child_class]
                counts[child_class] += 1
                entry["filhos"].append(walk(child, current, idx, depth=depth + 1))
        return entry

    result = {"capturado_em": datetime.now().astimezone().isoformat(),
              "modulo": module, "rota": route, "pid_sessao": window.process_id(),
              "metodo": "Inspeção win32 e menus UIA em execução, sem leitura dos valores dos campos.",
              "limites": ["Handles e IDs numéricos podem mudar entre sessões.",
                          "Caminhos estruturais são candidatos e exigem resolução única.",
                          "Seletores de classe/título só confirmados para a janela capturada.",
                          "Itens de listas, grades e valores de campos são omitidos."],
              "janela": walk(window), "menus": []}
    if include_menus:
        try:
            result["menus"] = menu_tree(window)
        except Exception as exc:
            result["erro_menus"] = type(exc).__name__
    else:
        result['menus_nao_inspecionados'] = 'UIA desativada explicitamente nesta captura.'
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    output = folder / f"{slug}.json"
    if output.exists():
        raise FileExistsError(f"Mapa existente preservado: {output}")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result, output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pid", type=int)
    parser.add_argument("--handle", type=int)
    parser.add_argument("--modulo", default="")
    parser.add_argument("--rota", default="")
    parser.add_argument("--nome")
    parser.add_argument("--pasta", type=Path, default=BASE / datetime.now().strftime("%Y%m%d-%H%M%S"))
    args = parser.parse_args()
    if args.handle:
        if not args.nome:
            parser.error("--handle exige --nome")
        result, output = snapshot(args.handle, args.pasta, args.nome, args.modulo, args.rota)
        print(json.dumps({"arquivo": str(output), "classe": result["janela"]["classe"],
                          "titulo": result["janela"]["texto"]}, ensure_ascii=True))
    elif args.pid:
        print(json.dumps(window_list(args.pid), ensure_ascii=True, indent=2))
    else:
        parser.error("Informe --pid para listar ou --handle e --nome para salvar")


if __name__ == "__main__":
    main()
