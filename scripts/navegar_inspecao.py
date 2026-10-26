"""Navegação explícita para a sessão de inspeção autorizada.

Abre módulos pelo painel e telas por rotas informadas. Não salva dados.
"""

import argparse
import json
import time
from pathlib import Path

from pywinauto import Application, Desktop, mouse

from inspecionar_telas import snapshot


ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "reports" / "inspecao-telas" / "20261015"
MODULES = {
    "acesso": ("Acesso", "TFrmPrincipal"),
    "refeitorio": ("Refeitório", "TFrmRefeitorioViewsPrincipal"),
    "portaria": ("Portaria", "TFrmPortariaViewsPrincipal"),
    "estacionamento": ("Estacionamento", "TFrmEstacionamentoViewsPrincipal"),
    "escola": ("Escola", "TFrmEscolaViewsPrincipal"),
    "administracao": ("Administração", "TFrmAdministracaoViewsPrincipal"),
}


def menu_click(handle, route, final_alias=None):
    window = Desktop(backend="win32").window(handle=handle).wrapper_object()
    if not window.is_enabled():
        raise RuntimeError("Janela bloqueada por diálogo; inspecionar antes de continuar.")
    if window.is_minimized():
        window.restore()
    try:
        window.set_focus()
    except Exception:
        # Recuperar foco por um clique na barra de título visível, sem tocar
        # nos campos. O terminal pode ter recebido foco entre dois processos.
        rect = window.rectangle()
        mouse.click(coords=(rect.left + max(80, rect.width() // 2), rect.top + 12))
        window.set_focus()
    used = []
    for index, name in enumerate(route):
        names = [name]
        if index == len(route) - 1 and final_alias and final_alias != name:
            names.append(final_alias)
        matches = []
        for attempt in range(5):
            # Recriar o wrapper depois de abrir cada submenu: elementos Delphi
            # obtidos antes do clique podem ter coordenadas antigas/inválidas.
            root = Desktop(backend='uia').window(handle=handle)
            matches = [c for c in root.descendants(control_type='MenuItem')
                       if c.is_visible() and c.element_info.name.replace('&', '') in names]
            if len(matches) == 1:
                rect = matches[0].rectangle()
                if rect.width() > 0 and rect.height() > 0 and max(abs(rect.left), abs(rect.top)) < 20000:
                    break
            time.sleep(.2)
        if len(matches) != 1:
            raise RuntimeError(f"Opção não única: {name}; encontradas {len(matches)}.")
        control = matches[0]
        if not control.is_enabled():
            raise RuntimeError(f"Opção desabilitada: {name}.")
        rect = control.rectangle()
        if rect.width() <= 0 or rect.height() <= 0 or max(abs(rect.left), abs(rect.top)) > 20000:
            raise RuntimeError(f"Opção sem posição válida: {name}.")
        control.click_input()
        used.append(control.element_info.name)
        time.sleep(.2)
    return used


def open_modules():
    panel = Desktop(backend="win32").window(class_name="TFrmModuloViewsPrincipal").wrapper_object()
    registry = {}
    snapshot(panel.handle, FOLDER, "painel-corrigido", "painel", "Painel")
    for key, (caption, cls) in MODULES.items():
        try:
            menu_click(panel.handle, ["Modulos", caption])
            target = Desktop(backend="win32").window(class_name=cls)
            target.wait("exists visible", timeout=15)
            target = target.wrapper_object()
            entry = {"handle": target.handle, "pid": target.process_id(), "classe": cls,
                     "titulo": target.window_text(), "rota_painel": ["Modulos", caption]}
            _, output = snapshot(target.handle, FOLDER, key + "-principal", key, "Principal")
            entry["mapa"] = str(output.relative_to(ROOT))
        except Exception as exc:
            entry = {"erro": f"{type(exc).__name__}: {exc}"}
        registry[key] = entry
        print(json.dumps({"modulo": key, **entry}, ensure_ascii=True), flush=True)
        (FOLDER / "modulos.json").write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")
    return registry


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("acao", choices=["abrir-modulos", "abrir-rota"])
    parser.add_argument("--modulo", choices=MODULES)
    parser.add_argument("--rota", help="Rota JSON explícita")
    args = parser.parse_args()
    if args.acao == "abrir-modulos":
        open_modules()
    else:
        if not args.modulo or not args.rota:
            parser.error("abrir-rota exige --modulo e --rota")
        registry = json.loads((FOLDER / "modulos.json").read_text(encoding="utf-8"))
        route = json.loads(args.rota)
        print(menu_click(registry[args.modulo]["handle"], route))
