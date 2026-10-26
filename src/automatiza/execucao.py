"""Executor local de cenários explícitos; não usa IA durante a execução."""
import json
import re
import platform
import shutil
import time
from pathlib import Path

from automatiza.auditoria import AuditRun
from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer
from automatiza.observador import observer_lock
from automatiza.perfis import check_origin_definition, destinations_match, import_destination, load_profile, profile_settings

READ_ACTIONS = {'capturar', 'aguardar', 'verificar_janela', 'sql_verificar', 'sql_aguardar', 'sql_reserva_verificar', 'sql_reserva_aguardar', 'sql_estrutura', 'acessus_verificar_janela'}
UI_ACTIONS = {'abrir_ocorrencias', 'abrir_ferias', 'abrir_reservas', 'clicar', 'preencher', 'teclas'}


def load_scenario(path):
    case = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if case.get('versao') != 1 or not case.get('id') or not isinstance(case.get('etapas'), list) or not case['etapas']:
        raise ValueError('Cenário precisa de versao 1, id e etapas.')
    if case.get('preparado') is not True:
        raise ValueError('Cenário desativado: preencha os dados e marque preparado=true.')
    for step in case['etapas']:
        action = step.get('acao')
        if action not in READ_ACTIONS | UI_ACTIONS:
            raise ValueError('Ação de cenário não suportada: ' + str(action))
        if action in {'clicar', 'preencher', 'teclas'} and case.get('permite_alterar_dados') is not True:
            raise ValueError('Ações genéricas de tela exigem permite_alterar_dados=true no cenário.')
        if action in {'sql_verificar', 'sql_aguardar', 'sql_reserva_verificar', 'sql_reserva_aguardar'}:
            if not isinstance(step.get('esperado'), int) or isinstance(step['esperado'], bool) or step['esperado'] < 0:
                raise ValueError('Verificação SQL exige contagem esperada inteira não negativa.')
            if not step.get('filtros'):
                raise ValueError('Verificação SQL precisa de filtros explícitos.')
            if action.startswith('sql_reserva_'):
                from automatiza.reservas import query_spec
                query_spec(step['filtros'])
        if action == 'aguardar' and not 0 <= step.get('segundos', -1) <= 300:
            raise ValueError('Espera fixa deve ficar entre 0 e 300 segundos.')
    return case


class WindowsActions:
    def __init__(self, settings):
        from automatiza.rh import RhApp
        self.app = RhApp(settings)
        self.window = None

    def start(self):
        self.app.start(authenticate=False)
        self.window = self.app.window

    def active(self):
        if self.window is None:
            raise RuntimeError('Nenhuma tela foi aberta pelo cenário.')
        return self.window.wrapper_object() if hasattr(self.window, 'wrapper_object') else self.window

    def capture(self, path):
        if self.window is None:
            return False
        window = self.active()
        if 'login' in window.class_name().lower():
            return False
        if any('edit' in c.class_name().lower() and c.is_visible() and c.has_style(0x20)
               for c in window.descendants()):
            return False
        self.app._restore(window)
        window.capture_as_image().save(str(path))
        return True

    def origin_alias(self):
        from pywinauto import Desktop
        from automatiza.menus import invoke_native
        panels = self.app._panels()
        if len(panels) != 1:
            raise RuntimeError('Painel do RH não encontrado de forma única para verificar a origem.')
        panel = self.app._restore(panels[0])
        # Este menu do painel expõe texto nativo. Apenas abre e cancela a consulta.
        route = ['Opções', 'Alias do Banco de Dados...']
        try:
            invoke_native(panel, route)
        except RuntimeError:
            panel.menu_select('->'.join(route))
        dialog = Desktop(backend='win32').window(class_name='TFrm_Alias', process=panel.process_id())
        dialog.wait('visible enabled', timeout=10)
        dialog = dialog.wrapper_object()
        combos = [c for c in dialog.descendants(class_name='TComboBox') if c.is_visible()]
        cancel = [b for b in dialog.descendants(class_name='TBitBtn')
                  if b.window_text().replace('&', '').casefold() == 'cancelar']
        if len(combos) != 1 or len(cancel) != 1:
            raise RuntimeError('Diálogo de alias mudou; não alterar configuração.')
        value = combos[0].window_text()
        cancel[0].click_input()
        return value

    def control(self, spec):
        from pywinauto import Desktop
        if not isinstance(spec, dict) or not set(spec) <= {'janela_classe', 'classe', 'titulo', 'id_controle'}:
            raise ValueError('Seletor inválido; use janela_classe, classe, titulo e/ou id_controle.')
        window = self.active()
        if spec.get('janela_classe'):
            windows = [w for w in Desktop(backend='win32').windows(process=window.process_id())
                       if w.class_name() == spec['janela_classe'] and w.is_visible()]
            # Inclui formulários MDI.
            windows += [w for w in self.app.window.descendants(class_name=spec['janela_classe']) if w.is_visible()]
            windows = list({w.handle: w for w in windows}.values())
            if len(windows) != 1:
                raise RuntimeError('Janela do seletor não encontrada de forma única.')
            window = windows[0]
        controls = [c for c in window.descendants() if c.is_visible() and c.is_enabled()]
        for key, getter in [('classe', lambda c: c.class_name()), ('titulo', lambda c: c.window_text()),
                            ('id_controle', lambda c: c.control_id())]:
            if key in spec:
                controls = [c for c in controls if getter(c) == spec[key]]
        if len(controls) != 1:
            raise RuntimeError(f'Seletor precisa resolver um controle; encontrou {len(controls)}.')
        return controls[0]

    def do(self, step):
        action = step['acao']
        if action.startswith('abrir_'):
            self.window = self.app.open_screen(action.removeprefix('abrir_'))
        elif action == 'clicar':
            self.control(step['seletor']).click_input()
        elif action == 'preencher':
            from automatiza.rh import _fill_without_logging
            control = self.control(step['seletor'])
            if 'edit' not in control.class_name().lower() or control.has_style(0x20):
                raise ValueError('Preenchimento genérico somente em campo de dados sem senha.')
            _fill_without_logging(control, str(step['valor']))
        elif action == 'teclas':
            keys = step['teclas']
            if keys not in {'{TAB}', '{ENTER}', '{ESC}', '^i', '^s', '^d', '{F2}', '{F3}', '{F4}', '{F5}'}:
                raise ValueError('Sequência de teclas não permitida no executor.')
            self.app._restore(self.active())
            self.active().type_keys(keys)
        elif action == 'verificar_janela':
            if self.active().class_name() != step['classe']:
                raise AssertionError('A classe da janela não corresponde ao esperado.')
        elif action == 'capturar':
            self.active()  # As capturas antes/depois pertencem à auditoria.


def run_scenario(profile_path, scenario_path, *, base=None, adapter=None, database=None, cancel_event=None):
    profile = load_profile(profile_path)
    case = load_scenario(scenario_path)
    original = Settings.load()
    settings = profile_settings(original, profile)
    needs_ui = any(s['acao'] in UI_ACTIONS or s['acao'] in {'capturar', 'verificar_janela'} for s in case['etapas'])
    ui = adapter if adapter is not None else WindowsActions(settings) if needs_ui else None
    db = database or SqlServer(settings)
    run = AuditRun(base or ROOT / 'reports/execucoes', case['id'], context={
        'perfil': profile, 'cenario': case['id'], 'permite_alterar_dados': case.get('permite_alterar_dados', False)},
        secrets=(original.sql_password, original.rh_password, settings.sql_password), capture=ui.capture if ui else None)
    checks = 0
    sql_checks = 0

    def wait(seconds):
        if cancel_event is not None:
            if cancel_event.wait(seconds):
                raise KeyboardInterrupt()
        else:
            time.sleep(seconds)
    try:
        with observer_lock(ROOT / 'reports/controle-executor', label='uma execução de cenário'):
            with run.step('Conferir base SQL selecionada', action='precondicao_sql'):
                db.assert_database()
            if needs_ui:
                with run.step('Conferir definição da origem selecionada', action='precondicao_origem'):
                    check_origin_definition(profile)
                if case.get('verificar_destino_importador', True):
                    with run.step('Conferir destino configurado no importador', action='precondicao_importador'):
                        actual = import_destination(Path(settings.app_work_dir or r'C:\acesso') / 'ConexaoConfig.ini')
                        if not destinations_match(actual, profile['destino_sql']):
                            raise ValueError('O importador aponta para outra origem/destino. Nenhuma configuração foi alterada.')
                with run.step('Conectar ao RH/Frequência', action='conectar_rh'):
                    ui.start()
                with run.step('Conferir alias ativo no RH', action='precondicao_alias_ativo'):
                    actual = ui.origin_alias()
                    if actual != profile['origem_rh']['alias']:
                        raise ValueError('O alias ativo do RH difere do perfil escolhido. Selecione a origem no painel do RH antes de repetir.')
            for step in case['etapas']:
                if cancel_event is not None and cancel_event.is_set():
                    raise KeyboardInterrupt()
                action = step['acao']
                details = {k: v for k, v in step.items() if k not in {'valor', 'descricao'}}
                with run.step(step.get('descricao', action), action=action, details=details):
                    if action == 'aguardar':
                        wait(step['segundos'])
                    elif action == 'sql_estrutura':
                        from automatiza.preparacao import check_schema
                        check_schema(db)
                        checks += 1
                    elif action == 'acessus_verificar_janela':
                        from automatiza.desktop import DesktopApp
                        application = DesktopApp(settings).connect()
                        if not application.window.is_visible() or not application.window.is_enabled():
                            raise AssertionError('O Módulo de Acesso não está disponível.')
                        image = run.folder / 'capturas/acessus-janela.png'
                        application.screenshot(image)
                        run.event('JANELA_ACESSUS_CONFIRMADA', 'Módulo de Acesso conectado, visível e habilitado.',
                                  depois='capturas/acessus-janela.png')
                        checks += 1
                    elif action in {'sql_verificar', 'sql_aguardar', 'sql_reserva_verificar', 'sql_reserva_aguardar'}:
                        if action.startswith('sql_reserva_'):
                            from automatiza.reservas import query_spec
                        else:
                            from automatiza.conferencia import query_spec
                        sql, params, limit = query_spec(step['filtros'])
                        waiting = action in {'sql_aguardar', 'sql_reserva_aguardar'}
                        timeout = step.get('prazo_segundos', 180) if waiting else 0
                        interval = step.get('intervalo_segundos', 15)
                        stability = step.get('estabilidade_segundos', 15) if waiting else 0
                        if not 0 <= timeout <= 3600 or not 5 <= interval <= 300 or not 0 <= stability <= timeout:
                            raise ValueError('Prazo, intervalo ou estabilidade SQL inválidos.')
                        end, matched = time.monotonic()+timeout, None
                        while True:
                            rows = db.query(sql, params)
                            if len(rows) > limit:
                                raise ValueError('Resultado SQL truncado; refine os filtros.')
                            run.event('AMOSTRA_SQL', 'Contagem filtrada no destino', linhas=len(rows), esperado=step['esperado'])
                            if action.startswith('sql_reserva_'):
                                run.event('AMOSTRA_RESERVA_SQL', 'Reservas filtradas no banco do Acessus.', registros=rows)
                            if len(rows) == step['esperado']:
                                matched = matched if matched is not None else time.monotonic()
                                if time.monotonic()-matched >= stability:
                                    checks += 1
                                    sql_checks += 1
                                    break
                            else:
                                matched = None
                            if time.monotonic() >= end:
                                raise AssertionError('O resultado SQL esperado não ficou confirmado no prazo.')
                            wait(min(interval, max(0, end-time.monotonic())))
                    else:
                        ui.do(step)
                        if action == 'verificar_janela':
                            checks += 1
        if case.get('permite_alterar_dados') and not sql_checks:
            state = 'EXECUTADO_SEM_VERIFICACAO_NEGOCIO'
        else:
            state = 'PASSOU' if checks else 'EXECUTADO_SEM_VERIFICACAO_DE_RESULTADO'
    except KeyboardInterrupt:
        state = 'INTERROMPIDO'
    except Exception as exc:
        run.event('EXECUCAO_FALHOU', 'Execução interrompida no primeiro problema.', erro_tipo=type(exc).__name__)
        state = 'FALHOU'
    run.summary['verificacoes_concluidas'] = checks
    run.finish(state)
    if adapter is None and database is None and platform.node().split('.')[0].casefold() == 'testesvm':
        shared = Path(r'\\VBOXSVR\ResultadoVM')
        if shared.is_dir():
            try:
                shutil.copytree(run.folder, shared / 'execucoes' / run.folder.name)
            except OSError:
                pass  # O relatório original continua disponível na VM.
    return {'estado': state, 'pasta': str(run.folder)}
