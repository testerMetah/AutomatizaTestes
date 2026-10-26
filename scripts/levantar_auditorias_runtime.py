"""Levantamento de leitura das abas de Auditorias/Históricos já abertas.

Uso: python scripts/levantar_auditorias_runtime.py <pid> <modulo>
Não altera dados nem aciona impressão/exportação.
"""

import json
import re
import sys
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path

from pywinauto import Application, Desktop, mouse


ROOT = Path(__file__).resolve().parents[1]


def click_tab(item):
    """Clique físico: SelectionItem.Select não dispara OnChange do Delphi."""
    rect = item.rectangle()
    mouse.click(coords=((rect.left + rect.right) // 2, (rect.top + rect.bottom) // 2))


def tabs(handle, *, upper):
    window = Desktop(backend="uia").window(handle=handle)
    controls = window.descendants(control_type="TabItem")
    midpoint = (window.rectangle().top + window.rectangle().bottom) // 2
    return [item for item in controls if (item.rectangle().top < midpoint) == upper]


def visible_page(handle, expected):
    window = Desktop(backend="win32").window(handle=handle)
    return any(
        child.class_name() == "TTabSheet" and child.is_visible()
        and child.window_text() == expected
        for child in window.descendants()
    )


def survey(pid, module):
    app = Application(backend="win32").connect(process=pid)
    principals = [window for window in Desktop(backend="win32").windows(process=pid)
                  if window.class_name().endswith("Principal") and window.is_visible()]
    if len(principals) != 1:
        raise RuntimeError(f"Esperada uma janela principal; encontradas {len(principals)}")
    main = app.window(handle=principals[0].handle)
    main.wait("visible enabled", timeout=10)
    children = [child for child in main.wrapper_object().descendants()
                if "AuditoriaHistorico" in child.class_name() and child.is_visible()]
    if len(children) != 1:
        raise RuntimeError(f"Esperada uma janela de auditoria; encontradas {len(children)}")
    target = children[0]
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output = ROOT / "resultados" / f"auditorias-runtime-{stamp}" / module
    output.mkdir(parents=True, exist_ok=False)
    with (output / "arvore-controles.txt").open("w", encoding="utf-8") as stream:
        with redirect_stdout(stream):
            app.window(handle=target.handle).print_control_identifiers()

    result = {"modulo": module, "janela": target.class_name(),
              "titulo": target.window_text(), "historicos": [], "falhas": []}
    upper = tabs(target.handle, upper=True)
    if not upper:
        upper = [None]  # Portaria tem formulário sem abas superiores.
    for index, original in enumerate(upper):
        title = original.window_text() if original is not None else target.window_text()
        record = {"historico": title, "abriu": False, "filtros": []}
        result["historicos"].append(record)
        try:
            target.set_focus()
            if original is not None:
                current = tabs(target.handle, upper=True)
                click_tab(current[index])
                record["abriu"] = visible_page(target.handle, title)
                if not record["abriu"]:
                    raise RuntimeError(f"A aba {title!r} não ficou visível após o clique")
            else:
                record["abriu"] = True
            safe_name = re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-") or "janela"
            target.capture_as_image().save(output / f"{index+1:02d}-{safe_name}.png")
            lower = tabs(target.handle, upper=False)
            for filter_index, filter_item in enumerate(lower):
                current = tabs(target.handle, upper=False)
                if filter_index >= len(current):
                    raise RuntimeError("Lista de filtros mudou durante o mapeamento")
                label = current[filter_index].window_text()
                target.set_focus()
                click_tab(current[filter_index])
                visible = [c for c in target.descendants()
                           if c.class_name() == "TTabSheet" and c.is_visible()
                           and c.rectangle().top > target.rectangle().top + target.rectangle().height() // 2]
                controls = []
                if visible:
                    controls = [{"classe": c.class_name(), "texto": c.window_text()}
                                for c in visible[0].descendants()
                                if c.class_name() in ("TEdit", "TMaskEdit", "TComboBox", "TCheckBox")]
                record["filtros"].append({"nome": label, "abriu": bool(visible), "controles": controls})
        except Exception as exc:
            record["erro"] = f"{type(exc).__name__}: {exc}"
            result["falhas"].append(record["erro"])
            target.capture_as_image().save(output / f"falha-{index+1:02d}.png")
    (output / "resultado.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"saida": str(output), "historicos": len(result["historicos"]),
                      "filtros": sum(len(x["filtros"]) for x in result["historicos"]),
                      "falhas": result["falhas"]}, ensure_ascii=False))
    return 1 if result["falhas"] else 0


if __name__ == "__main__":
    raise SystemExit(survey(int(sys.argv[1]), sys.argv[2]))
