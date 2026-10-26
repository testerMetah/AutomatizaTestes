"""Percorre um lote explícito de rotas de inspeção, sem salvar ou processar.

Usar somente durante uma sessão liberada para controle de janelas.
Não executa casos de teste, consultas ou comandos de equipamentos.
"""

import argparse
import ctypes
import json
import time
from pathlib import Path

from pywinauto import Application, Desktop

from inspecionar_telas import snapshot
from navegar_inspecao import FOLDER, MODULES, ROOT, menu_click


CATALOG = ROOT / "docs/mapeamentos/acessus-completo/estatico-20261015-v2/catalogo.json"


def visible_screens(entry):
    root = Desktop(backend="win32").window(handle=entry["handle"]).wrapper_object()
    result = {}
    top_windows = Desktop(backend="win32").windows(process=entry["pid"])
    top_handles = {w.handle for w in top_windows}
    candidates = root.descendants() + top_windows
    mdi_handles = {c.handle for c in root.descendants() if c.class_name() == "MDIClient"}
    for w in candidates:
        if w.handle == entry["handle"] or not w.is_visible():
            continue
        cls = w.class_name().lower()
        if (ctypes.windll.user32.GetParent(w.handle) in mdi_handles
                or cls.startswith(("tf", "#32770", "tmessage"))
                or (w.handle in top_handles and w.window_text() and cls not in {"tapplication", "gdi+ hook window class", "msctfime ui", "ime", "combolbox"})):
            result[w.handle] = w
    return result


def safe_buttons(window, prefix):
    return {b.handle: b for b in window.descendants()
            if ("button" in b.class_name().lower() or b.class_name() == 'TBitBtn') and b.is_visible() and b.is_enabled()
            and b.window_text().startswith(prefix)}


def explore_tabs(window, module, slug, route):
    app = Application(backend="uia").connect(process=window.process_id())
    root = app.window(handle=window.handle)
    observed = set()
    outputs = []
    # Reenumerar após cada seleção; algumas abas são construídas sob demanda.
    for _ in range(24):
        tabs = [t for t in root.descendants(control_type="TabItem")
                if t.is_visible() and t.is_enabled() and t.element_info.name not in observed]
        if not tabs:
            break
        tab = tabs[0]
        name = tab.element_info.name
        observed.add(name)
        if name in {"Grid", "Cadastro"}:
            continue
        tab.click_input()
        time.sleep(.15)
        result, path = snapshot(window.handle, FOLDER, f"{slug}-aba-{len(outputs) + 1:02d}",
                                module, route + " > Aba: " + name)
        outputs.append({"aba": name, "mapa": str(path.relative_to(ROOT))})
    return outputs


def inspect_route(module, index, route, entry):
    path = route["rota_declarada"]
    slug = f"{module}-{index:03d}"
    record = {"indice": index, **route, "situacao": "PENDENTE", "mapas": []}
    # As rotas de exclusão rápida e importação de refeições possuem formulários
    # intermediários identificados nos recursos. Abrir esses formulários não
    # inclui acionar seus botões de exclusão/importação.
    unsafe = {"Sair", "LogOff"}
    if path[-1] in unsafe:
        record.update(situacao="NAO_ACIONADA", motivo="Ação de saída ou potencial processamento; mapa estático preservado.")
        return record
    before = visible_screens(entry)
    if before:
        raise RuntimeError("Há uma tela anterior aberta; não navegar sobre ela.")
    stage = 'abrir_rota'
    try:
        record["rota_observada"] = menu_click(entry["handle"], path, route.get("legenda_action"))
        time.sleep(.5)
        opened = visible_screens(entry)
        if not opened:
            time.sleep(.5)
            opened = visible_screens(entry)
        if not opened:
            # Alguns menus trocam um card dentro da janela principal (Visita
            # Rápida) em vez de criar um formulário filho. Preservar esse estado.
            _, saved = snapshot(entry['handle'], FOLDER, slug + '-painel', module, ' > '.join(path))
            record['mapas'].append(str(saved.relative_to(ROOT)))
            record.update(situacao="PAINEL_CAPTURADO", motivo="Rota acionada; janela principal capturada, sem novo formulário filho.")
            return record
        for window in opened.values():
            # Formul?rios MDI podem abrir mais altos que o desktop e deixar
            # Incluir/Cancelar fora da tela. Maximizar antes dos cliques.
            parent = ctypes.windll.user32.GetParent(window.handle)
            mdi = {c.handle for c in Desktop(backend="win32").window(handle=entry["handle"]).descendants()
                   if c.class_name() == "MDIClient"}
            if parent in mdi:
                window.maximize()
        for n, window in enumerate(opened.values(), 1):
            stage = 'salvar_tela'
            _, saved = snapshot(window.handle, FOLDER, f"{slug}-tela-{n:02d}", module, " > ".join(path))
            record["mapas"].append(str(saved.relative_to(ROOT)))
            record.setdefault("janelas", []).append({"classe": window.class_name(), "titulo": window.window_text()})
        # Erros/avisos recebem inventário próprio e são encerrados por OK/Não.
        dialogs = [w for w in opened.values() if w.class_name() == "#32770"]
        if dialogs:
            record["situacao"] = "DIALOGO_OBSERVADO"
            for dialog in dialogs:
                buttons = safe_buttons(dialog, "OK") or safe_buttons(dialog, "&Não") or safe_buttons(dialog, "Não")
                if len(buttons) == 1:
                    next(iter(buttons.values())).click_input()
                else:
                    dialog.close()
        else:
            record["situacao"] = "INSPECIONADA"
            record["validada_em_execucao"] = True
            for n, window in enumerate(opened.values(), 1):
                if not window.is_enabled():
                    continue
                stage = 'inspecionar_abas'
                record.setdefault("abas", []).extend(explore_tabs(window, module, f"{slug}-tela-{n:02d}", " > ".join(path)))
                stage = 'inclusao_vazia'
                include = safe_buttons(window, "Incluir (Ctrl+I)")
                if len(include) == 1:
                    next(iter(include.values())).click_input()
                    time.sleep(.25)
                    current = visible_screens(entry)
                    added = [w for handle, w in current.items() if handle not in opened]
                    for extra_index, extra in enumerate(added, 1):
                        _, saved = snapshot(extra.handle, FOLDER,
                            f'{slug}-tela-{n:02d}-incluir-dialogo-{extra_index:02d}', module,
                            ' > '.join(path) + ' > Incluir (diálogo vazio, sem salvar)')
                        record['mapas'].append(str(saved.relative_to(ROOT)))
                        record.setdefault('janelas_inclusao', []).append({'classe': extra.class_name(), 'titulo': extra.window_text()})
                        if extra.is_enabled():
                            record.setdefault('abas_inclusao', []).extend(explore_tabs(extra, module,
                                f'{slug}-tela-{n:02d}-incluir-dialogo-{extra_index:02d}',
                                ' > '.join(path) + ' > Incluir (diálogo vazio, sem salvar)'))
                    if any(w.class_name() == "#32770" for w in current.values()):
                        record["inclusao"] = "AVISO_AO_ABRIR; não preencher nem salvar"
                        break
                    cancel = safe_buttons(window, "Cancelar")
                    for extra in added:
                        cancel.update(safe_buttons(extra, 'Cancelar'))
                    if len(cancel) != 1:
                        record["inclusao"] = "Sem cancelamento inequívoco; exige inspeção específica"
                        break
                    if added:
                        next(iter(cancel.values())).click_input()
                        record['inclusao'] = 'Diálogo vazio inspecionado e cancelado sem salvar'
                        continue
                    _, saved = snapshot(window.handle, FOLDER, f"{slug}-tela-{n:02d}-incluir", module,
                                        " > ".join(path) + " > Incluir (sem preencher)")
                    record["mapas"].append(str(saved.relative_to(ROOT)))
                    record.setdefault("abas_inclusao", []).extend(explore_tabs(window, module,
                        f"{slug}-tela-{n:02d}-incluir", " > ".join(path) + " > Incluir (sem preencher)"))
                    cancel = safe_buttons(window, "Cancelar (Ctrl+D)")
                    if len(cancel) != 1:
                        raise RuntimeError("Cancelamento deixou de ser único.")
                    next(iter(cancel.values())).click_input()
                    record["inclusao"] = "Formulário vazio inspecionado e cancelado sem salvar"
        stage = 'fechar_telas'
        remaining = visible_screens(entry)
        for window in reversed(list(remaining.values())):
            if not ctypes.windll.user32.IsWindow(window.handle):
                continue
            if not window.is_enabled():
                continue
            cancel = safe_buttons(window, "Cancelar (Ctrl+D)")
            if len(cancel) == 1:
                next(iter(cancel.values())).click_input()
            # Algumas telas (ex.: inclusão manual de refeições) se destroem
            # ao cancelar. Não enviar WM_CLOSE a um handle já liberado.
            if ctypes.windll.user32.IsWindow(window.handle):
                try:
                    window.close()
                except Exception:
                    # Delphi destrói os filhos antes da janela principal;
                    # o wrapper pode observar um filho inválido durante Close.
                    time.sleep(.3)
                    if ctypes.windll.user32.IsWindow(window.handle) and window.is_visible():
                        raise
        if visible_screens(entry):
            raise RuntimeError("Tela/aviso permaneceu aberto; interrompido para inspeção específica.")
        return record
    except Exception as exc:
        record.update(situacao="FALHA_INSPECAO", erro_etapa=stage, erro=f"{type(exc).__name__}: {exc}")
        return record


def run(module, start, end):
    registry = json.loads((FOLDER / "modulos.json").read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    routes = next(m["rotas"] for m in catalog["modulos"][module]["menus"]
                  if m["formulario"] == MODULES[module][1])
    log = FOLDER / f"{module}-percurso.jsonl"
    for index, route in enumerate(routes, 1):
        if index < start or (end and index > end):
            continue
        if visible_screens(registry[module]):
            print("INTERROMPIDO: há formulário aberto; inspecionar antes de continuar.", flush=True)
            break
        record = inspect_route(module, index, route, registry[module])
        with log.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(json.dumps({"modulo": module, "indice": index, "rota": route["rota_declarada"],
                          "situacao": record["situacao"], "erro": record.get("erro"),
                          "mapas": len(record["mapas"])}, ensure_ascii=True), flush=True)
        if record["situacao"] == "FALHA_INSPECAO":
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--modulo", choices=MODULES, required=True)
    parser.add_argument("--inicio", type=int, default=1)
    parser.add_argument("--fim", type=int)
    args = parser.parse_args()
    run(args.modulo, args.inicio, args.fim)
