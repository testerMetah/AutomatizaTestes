"""Execução sequencial de uma lista explícita de cenários preparados."""
import json
import os
import platform
import shutil
from html import escape
from pathlib import Path

from automatiza.auditoria import AuditRun
from automatiza.config import ROOT
from automatiza.execucao import load_scenario, run_scenario
from automatiza.observador import observer_lock
from automatiza.perfis import load_profile


def load_suite(path):
    path = Path(path).resolve()
    suite = json.loads(path.read_text(encoding='utf-8-sig'))
    names = suite.get('cenarios')
    if suite.get('versao') != 1 or not suite.get('id') or not isinstance(names, list) or not names:
        raise ValueError('Lote exige versao 1, id e lista não vazia de cenarios.')
    cases, ids = [], set()
    for name in names:
        if not isinstance(name, str):
            raise ValueError('Cada cenário do lote precisa de um caminho relativo.')
        candidate = (path.parent / name).resolve()
        if Path(name).is_absolute() or not candidate.is_relative_to(path.parent):
            raise ValueError('Cenário precisa ficar na pasta do lote ou em uma subpasta.')
        case = load_scenario(candidate)
        if case['id'] in ids:
            raise ValueError('O lote não pode repetir um cenário.')
        ids.add(case['id'])
        cases.append((candidate, case))
    return suite, cases


def run_suite(profile_path, suite_path, *, base=None, cancel_event=None, runner=None):
    # Validar todos os arquivos antes da primeira ação; modelos inválidos não
    # devem descobrir seu erro depois que outro cenário já modificou o sistema.
    load_profile(profile_path)
    suite, cases = load_suite(suite_path)
    publish = runner is None
    runner = runner or run_scenario
    audit = AuditRun(base or ROOT / 'reports/lotes', str(suite['id']))
    results = []
    blocked = False
    try:
        with observer_lock(ROOT / 'reports/controle-lote', label='um lote de cenários'):
            for path, case in cases:
                cancelled = cancel_event is not None and cancel_event.is_set()
                if blocked or cancelled:
                    results.append({'cenario': case['id'], 'estado': 'NAO_EXECUTADO'})
                    continue
                try:
                    result = runner(profile_path, path, base=audit.folder / 'cenarios', cancel_event=cancel_event)
                    state = result['estado']
                    report = Path(result['pasta']) / 'relatorio.html'
                    results.append({'cenario': case['id'], 'estado': state,
                                    'relatorio': Path(os.path.relpath(report, audit.folder)).as_posix()})
                except Exception as exc:
                    state = 'FALHOU'
                    results.append({'cenario': case['id'], 'estado': state, 'erro_tipo': type(exc).__name__})
                audit.event('RESULTADO_CENARIO', case['id'], estado=state)
                blocked = state != 'PASSOU'
    except (Exception, KeyboardInterrupt) as exc:
        audit.event('LOTE_INTERROMPIDO', 'Lote interrompido.', erro_tipo=type(exc).__name__)
        for _, case in cases[len(results):]:
            results.append({'cenario': case['id'], 'estado': 'NAO_EXECUTADO'})
    cancelled = cancel_event is not None and cancel_event.is_set()
    state = 'PASSOU' if all(r['estado'] == 'PASSOU' for r in results) else 'INTERROMPIDO' if cancelled else 'FALHOU'
    audit.summary['cenarios'] = results
    rows = []
    for result in results:
        link = ('<a href="' + escape(result['relatorio'], quote=True) + '">Detalhes</a>') if result.get('relatorio') else ''
        rows.append('<tr><td>' + escape(result['cenario']) + '</td><td>' + escape(result['estado']) + '</td><td>' + link + '</td></tr>')
    (audit.folder / 'indice.html').write_text(
        '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Lote de testes</title>'
        '<style>body{font:16px system-ui;margin:30px}td,th{padding:10px;border:1px solid #ccc}table{border-collapse:collapse}</style>'
        '<h1>' + escape(str(suite['id'])) + '</h1><p>Estado: <strong>' + state + '</strong></p>'
        '<p>O lote para no primeiro resultado diferente de PASSOU. Cenários não executados não são aprovações.</p>'
        '<table><tr><th>Cenário</th><th>Resultado</th><th>Relatório</th></tr>' + ''.join(rows) + '</table>'
        '<p><a href="relatorio.html">Auditoria do lote</a></p></html>', encoding='utf-8')
    audit.finish(state)
    if publish and platform.node().split('.')[0].casefold() == 'testesvm':
        shared = Path(r'\\VBOXSVR\ResultadoVM')
        if shared.is_dir():
            try:
                shutil.copytree(audit.folder, shared / 'lotes' / audit.folder.name)
            except OSError:
                pass  # O lote completo permanece salvo na VM.
    return {'estado': state, 'pasta': str(audit.folder), 'arquivo': 'indice.html'}
