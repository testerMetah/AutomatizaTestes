"""Inspeção de rotas RH por mnemônicos declarados, sem preencher ou salvar dados."""
import argparse
import ctypes
import json
import re
import time
import unicodedata
import win32gui
from dataclasses import replace
from pathlib import Path

from pywinauto import Application, Desktop
from automatiza.auditoria import AuditRun
from automatiza.config import ROOT, Settings
from automatiza.observador import observer_lock
from automatiza.rh import RhApp
from inspecionar_telas import snapshot


def mnemonic(caption):
    found = re.search(r'&(.)', caption)
    return found.group(1).casefold() if found and found.group(1).isascii() else None


def plan():
    base = ROOT / 'docs/mapeamentos/rh-completo/estatico-20261015'
    catalog = json.loads((base / 'catalogo.json').read_text(encoding='utf-8'))
    entry = next(v for v in catalog['formularios'].values() if v['classe'] == 'TFrm_RHPA0010')
    root = json.loads((base / entry['mapa']).read_text(encoding='utf-8'))
    menu = next(n for n in root['filhos'] if n['nome'] == 'Mnm_Principal')
    inherited = {'Mnm_Arquivo': '&Arquivo', 'Mnm_Janelas': '&Janelas', 'Mnm_Ajuda': 'Aj&uda'}
    routes = []

    def walk(nodes, parents=(), keys=(), issue=None):
        captions = [n['propriedades'].get('Caption', inherited.get(n['nome'], '')) for n in nodes]
        mnemonics = [mnemonic(c) for c in captions]
        for node, caption, key in zip(nodes, captions, mnemonics):
            if not caption or caption == '-':
                continue
            route = (*parents, caption.replace('&', ''))
            reason = issue
            if key is None:
                reason = reason or 'Sem mnemônico inequívoco no recurso.'
            elif mnemonics.count(key) != 1:
                reason = reason or 'Mnemônico repetido entre irmãos; não selecionar por tentativa.'
            current_keys = (*keys, key)
            children = [n for n in node['filhos'] if n['classe'] == 'TMenuItem']
            if children:
                walk(children, route, current_keys, reason)
            else:
                text = unicodedata.normalize('NFKD', ' '.join(route)).encode('ascii', 'ignore').decode().casefold()
                unsafe = ('excluir', 'exclusao', 'desligamento', 'gerar', 'recalcular', 'realocar', 'calculo',
                          'calcular', 'importar', 'exportar', 'cancelar lancamentos', 'efetuar', 'sair',
                          'logoff', 'restaurar', 'backup', 'liberar', 'enviar', 'digitais', 'faces',
                          'online', 'on-line', 'off-line', 'telema', 'ponto movel', 'cercas')
                if any(term in text for term in unsafe):
                    reason = 'Rotina de processamento, equipamento ou saída; somente mapa estático.'
                if not caption.endswith('...'):
                    reason = reason or 'Sem indicação de abertura de formulário; exige revisão específica.'
                routes.append({'rota': list(route), 'teclas': list(current_keys),
                               'situacao': 'NAO_ACIONAR' if reason else 'CANDIDATA', 'motivo': reason})
    walk(menu['filhos'])
    return routes


def screens(main):
    desktop = Desktop(backend='win32')
    mdiclient = {c.handle for c in main.children() if c.class_name() == 'MDIClient'}
    handles = []
    win32gui.EnumChildWindows(main.handle, lambda h, _: handles.append(h), None)
    candidates = desktop.windows(process=main.process_id())
    for handle in handles:
        if ctypes.windll.user32.GetParent(handle) in mdiclient:
            try:
                candidates.append(desktop.window(handle=handle).wrapper_object())
            except Exception:
                continue
    result = {}
    for window in candidates:
        try:
            if not ctypes.windll.user32.IsWindow(window.handle) or not window.is_visible() or window.handle == main.handle:
                continue
            parent = ctypes.windll.user32.GetParent(window.handle)
            cls = window.class_name()
            if parent in mdiclient or cls.startswith('TFrm_') or cls in {'TMessageForm', '#32770'}:
                if cls not in {'TFrm_RHPA0010', 'TFrm_Espera'}:
                    result[window.handle] = window
        except Exception:
            # Formulários transitórios podem ser destruídos durante a enumeração.
            # Se nada estável for encontrado, a rota ficará sem confirmação.
            continue
    return result


def inspect(limit, start):
    settings = replace(Settings.load(), rh_continue_invalid_config='yes')
    app = RhApp(settings).start()
    main = app.window
    main.maximize()

    def capture(path):
        for window in Desktop(backend='win32').windows(process=main.process_id()):
            if 'login' in window.class_name().casefold():
                return False
        for control in main.descendants():
            if 'edit' in control.class_name().casefold() and control.is_visible() and control.has_style(0x20):
                return False
        main.capture_as_image().save(str(path))
        return True

    run = AuditRun(ROOT / 'reports/inspecao-ampliada', 'Inspeção RH/Frequência',
                   context={'escopo': 'Navegação e controles; sem salvar/preencher/processar.', 'nao_valida_regras': True},
                   secrets=(settings.rh_password, settings.sql_password), capture=capture)
    routes = plan()
    (run.folder / 'plano.json').write_text(json.dumps(routes, ensure_ascii=False, indent=2), encoding='utf-8')
    records = []
    state = 'INSPECAO_CONCLUIDA'
    try:
        with observer_lock(ROOT / 'reports/controle-executor', label='uma automação de tela'):
            initial = screens(main)
            if initial:
                raise RuntimeError('Há formulário prévio aberto. Nenhuma navegação foi feita.')
            selected = [(i, r) for i, r in enumerate(routes, 1) if r['situacao'] == 'CANDIDATA' and i >= start][:limit]
            for index, route in selected:
                record = {'indice': index, **route, 'mapas': [], 'abas': []}
                with run.step('Focar Frequência', action='foco', details={'rota': route['rota']}):
                    app._restore(main)
                for depth, key in enumerate(route['teclas']):
                    keys = '%' + key if depth == 0 else key
                    with run.step('Abrir menu: ' + route['rota'][depth], action='teclas_menu', details={'teclas': keys}):
                        main.type_keys(keys, pause=.1, set_foreground=False)
                        time.sleep(.15)
                deadline = time.monotonic() + 5
                time.sleep(.4)
                opened = screens(main)
                while not opened and time.monotonic() < deadline:
                    time.sleep(.25)
                    opened = screens(main)
                if not opened:
                    record['situacao'] = 'SEM_FORMULARIO_CONFIRMADO'
                    with run.step('Fechar menu sem formulário', action='teclas_menu'):
                        main.type_keys('{ESC}{ESC}{ESC}', set_foreground=False)
                    records.append(record)
                    continue
                if any(w.class_name() in {'TMessageForm', '#32770'} for w in opened.values()):
                    record['situacao'] = 'AVISO_EXIGE_REVISAO'
                    records.append(record)
                    state = 'INSPECAO_INTERROMPIDA_POR_AVISO'
                    break
                for number, window in enumerate(opened.values(), 1):
                    record.setdefault('janelas', []).append({'classe': window.class_name(), 'titulo': window.window_text()})
                    with run.step('Mapear formulário', action='inspecionar_controles', details={'classe': window.class_name()}):
                        _, path = snapshot(window.handle, run.folder / 'mapas', f'{index:03d}-{number}', 'rh-frequencia',
                                           ' > '.join(route['rota']), include_menus=False)
                        record['mapas'].append(path.relative_to(ROOT).as_posix())
                    root = Application(backend='uia').connect(process=main.process_id()).window(handle=window.handle)
                    # Não usar TabControlWrapper/TCM_* em TPageControl Delphi.
                    tabs = [t for t in root.descendants(control_type='TabItem') if t.is_visible() and t.is_enabled()]
                    names = [t.element_info.name for t in tabs]
                    for tab_number, tab in enumerate(tabs[:10], 1):
                        name = tab.element_info.name
                        if not name or names.count(name) != 1:
                            continue
                        with run.step('Inspecionar aba: ' + name, action='clicar_aba', details={'aba': name}):
                            tab.click_input()
                            time.sleep(.15)
                            _, path = snapshot(window.handle, run.folder / 'mapas', f'{index:03d}-{number}-aba-{tab_number}',
                                               'rh-frequencia', ' > '.join(route['rota']) + ' > ' + name, include_menus=False)
                            record['abas'].append({'aba': name, 'mapa': path.relative_to(ROOT).as_posix()})
                record['situacao'] = 'FORMULARIO_INSPECIONADO_SEM_ALTERACOES'
                for window in reversed(list(screens(main).values())):
                    if not ctypes.windll.user32.IsWindow(window.handle):
                        continue
                    if window.is_enabled():
                        with run.step('Fechar formulário sem edição', action='fechar_janela', details={'classe': window.class_name()}):
                            window.close()
                            time.sleep(.2)
                records.append(record)
                if screens(main):
                    raise RuntimeError('Uma janela permaneceu aberta; interrompido para revisão.')
                (run.folder / 'cobertura.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
                print(json.dumps({'indice': index, 'rota': route['rota'], 'situacao': record['situacao']}, ensure_ascii=True), flush=True)
    except KeyboardInterrupt:
        state = 'INTERROMPIDO'
    except Exception as exc:
        run.event('FALHA_INSPECAO', 'Inspeção interrompida.', erro_tipo=type(exc).__name__, erro=str(exc))
        state = 'FALHA_INSPECAO'
    (run.folder / 'cobertura.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    run.finish(state)
    print(json.dumps({'pasta': str(run.folder), 'estado': state, 'rotas': len(records)}, ensure_ascii=True), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limite', type=int, default=10)
    parser.add_argument('--inicio', type=int, default=1)
    parser.add_argument('--somente-plano', action='store_true')
    args = parser.parse_args()
    if args.somente_plano:
        routes = plan()
        print(json.dumps({'total': len(routes), 'candidatas': sum(r['situacao'] == 'CANDIDATA' for r in routes), 'rotas': routes}, ensure_ascii=True))
    else:
        inspect(args.limite, args.inicio)
