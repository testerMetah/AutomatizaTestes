"""Central local para escolher ambientes e executar cenários sem IA."""
import argparse
import json
import queue
import threading
import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import ttk, filedialog, messagebox

from automatiza.config import ROOT, Settings
from automatiza.execucao import load_scenario, run_scenario
from automatiza.lotes import load_suite, run_suite
from automatiza.perfis import discover_aliases, load_profile, profile_settings, save_profile


def gui():
    settings = Settings.load()
    aliases = {a['alias']: a for a in discover_aliases()}
    root = tk.Tk()
    root.title('AutomatizaTestes — ambientes, execução e relatórios')
    root.geometry('850x600')
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)
    ttk.Label(frame, text='Central de testes', font=('Segoe UI', 19, 'bold')).pack(anchor='w')
    ttk.Label(frame, text='Escolha a origem e o destino antes de executar. O mouse e o teclado serão usados nos cenários de tela.', wraplength=790).pack(anchor='w', pady=(4, 15))
    origin = tk.StringVar()
    host = tk.StringVar(value=settings.sql_server)
    database = tk.StringVar(value=settings.sql_database)
    source_info = tk.StringVar(value='Selecione uma conexão do RH.')
    chosen_profile = tk.StringVar()
    chosen_case = tk.StringVar()
    state = tk.StringVar(value='Nenhum teste iniciado.')
    box = ttk.LabelFrame(frame, text='Ambiente de teste', padding=12)
    box.pack(fill='x')
    ttk.Label(box, text='Origem RH').grid(row=0, column=0, sticky='w')
    combo = ttk.Combobox(box, textvariable=origin, values=list(aliases), state='readonly', width=29)
    combo.grid(row=0, column=1, sticky='w', padx=10)
    ttk.Label(box, textvariable=source_info, wraplength=400).grid(row=0, column=2, sticky='w')

    def update_origin(event=None):
        alias = aliases.get(origin.get(), {})
        source_info.set(alias.get('servidor', '') + ' / ' + alias.get('banco', ''))
    combo.bind('<<ComboboxSelected>>', update_origin)
    ttk.Label(box, text='Servidor de destino').grid(row=1, column=0, sticky='w', pady=8)
    ttk.Entry(box, textvariable=host, width=32).grid(row=1, column=1, sticky='w', padx=10)
    ttk.Label(box, text='Banco de destino').grid(row=2, column=0, sticky='w')
    ttk.Entry(box, textvariable=database, width=32).grid(row=2, column=1, sticky='w', padx=10)
    ttk.Label(box, text='A origem selecionada deve estar ativa no RH. O executor confere o importador e não troca bancos silenciosamente.', wraplength=740).grid(row=3, column=0, columnspan=3, sticky='w', pady=10)

    def save_environment():
        if origin.get() not in aliases:
            messagebox.showerror('Ambiente', 'Selecione a origem do RH.')
            return
        path = filedialog.asksaveasfilename(initialdir=str(ROOT / 'profiles'), defaultextension='.json', filetypes=[('Ambiente', '*.json')])
        if not path:
            return
        try:
            profile = {'versao': 1, 'origem_rh': aliases[origin.get()],
                       'destino_sql': {'servidor': host.get().strip(), 'banco': database.get().strip(),
                                       'driver': settings.sql_driver, 'auth': settings.sql_auth,
                                       'encrypt': settings.sql_encrypt, 'trust_certificate': settings.sql_trust_certificate}}
            save_profile(path, profile)
            chosen_profile.set(path)
            state.set('Ambiente salvo. Selecione um cenário.')
        except Exception as exc:
            messagebox.showerror('Não foi possível salvar', str(exc))

    def open_environment():
        path = filedialog.askopenfilename(initialdir=str(ROOT / 'profiles'), filetypes=[('Ambiente', '*.json')])
        if not path:
            return
        try:
            profile = load_profile(path)
            chosen_profile.set(path)
            origin.set(profile['origem_rh']['alias'])
            host.set(profile['destino_sql']['servidor'])
            database.set(profile['destino_sql']['banco'])
            update_origin()
        except Exception as exc:
            messagebox.showerror('Ambiente inválido', str(exc))

    buttons = ttk.Frame(box)
    buttons.grid(row=4, column=0, columnspan=3, sticky='w')
    ttk.Button(buttons, text='Salvar novo ambiente', command=save_environment).pack(side='left')
    ttk.Button(buttons, text='Abrir ambiente salvo', command=open_environment).pack(side='left', padx=8)
    ttk.Label(frame, textvariable=chosen_profile, wraplength=790).pack(anchor='w', pady=8)

    def inspect_environment():
        from automatiza.preparacao import inspect_preparation, save_preparation
        if active['running']:
            return
        try:
            selected_settings = settings
            if chosen_profile.get():
                profile = load_profile(chosen_profile.get())
                if (profile['origem_rh']['alias'] != origin.get() or profile['destino_sql']['servidor'] != host.get().strip()
                        or profile['destino_sql']['banco'] != database.get().strip()):
                    raise ValueError('Salve ou abra um ambiente correspondente aos campos antes de conferir.')
                selected_settings = profile_settings(settings, profile)
        except Exception as exc:
            messagebox.showerror('Ambiente', str(exc))
            return
        active['running'] = True
        runbutton.config(state='disabled')
        state.set('Conferindo arquivos, perfis e SQL. Aguarde o relatório de preparação.')

        def worker():
            try:
                result = inspect_preparation(settings=selected_settings, sql=True)
                folder = save_preparation(result)
                messages.put({'estado': result['estado'], 'pasta': str(folder), 'arquivo': 'preparacao.html'})
            except Exception as exc:
                messages.put({'erro': f'Falha no diagnóstico ({type(exc).__name__}).'})
        threading.Thread(target=worker, daemon=False).start()
        root.after(250, poll)

    ttk.Button(buttons, text='Verificar preparação', command=inspect_environment).pack(side='left', padx=8)
    casebox = ttk.LabelFrame(frame, text='Cenário', padding=12)
    casebox.pack(fill='x', pady=8)

    def open_case():
        path = filedialog.askopenfilename(initialdir=str(ROOT / 'examples/cenarios'), filetypes=[('Cenário', '*.json')])
        if path:
            chosen_case.set(path)
            try:
                case = load_scenario(path)
                state.set(f"Cenário {case['id']}: {len(case['etapas'])} etapa(s). "
                          + ('Este cenário altera dados.' if case.get('permite_alterar_dados') else 'Sem ações genéricas de alteração de dados.'))
            except Exception as exc:
                state.set(str(exc))
    ttk.Button(casebox, text='Selecionar cenário', command=open_case).pack(anchor='w')
    ttk.Label(casebox, textvariable=chosen_case, wraplength=750).pack(anchor='w', pady=5)
    ttk.Label(frame, textvariable=state, wraplength=780).pack(anchor='w', pady=12)
    actions = ttk.Frame(frame)
    actions.pack(fill='x')
    messages = queue.Queue()
    stop = threading.Event()
    active = {'running': False, 'report': None}

    def poll():
        try:
            result = messages.get_nowait()
        except queue.Empty:
            root.after(250, poll)
            return
        active['running'] = False
        root.deiconify()
        runbutton.config(state='normal')
        suitebutton.config(state='normal')
        stopbutton.config(state='disabled')
        if 'erro' in result:
            state.set(result['erro'])
        else:
            active['report'] = Path(result['pasta']) / result.get('arquivo', 'relatorio.html')
            state.set(result['estado'] + ' — ' + str(active['report']))

    def execute(suite_path=None):
        if active['running']:
            return
        if not chosen_profile.get() or (not suite_path and not chosen_case.get()):
            messagebox.showerror('Execução', 'Salve/abra um ambiente e selecione um cenário.')
            return
        try:
            profile = load_profile(chosen_profile.get())
            if suite_path:
                load_suite(suite_path)
            else:
                load_scenario(chosen_case.get())
            if (profile['origem_rh']['alias'] != origin.get() or profile['destino_sql']['servidor'] != host.get().strip()
                    or profile['destino_sql']['banco'] != database.get().strip()):
                raise ValueError('Os campos foram alterados. Salve um novo ambiente antes de executar.')
        except Exception as exc:
            messagebox.showerror('Execução', str(exc))
            return
        stop.clear()
        active['running'] = True
        runbutton.config(state='disabled')
        suitebutton.config(state='disabled')
        stopbutton.config(state='normal')
        state.set('Executando. Não use os sistemas durante um cenário de tela.')
        # A janela da central não fica cobrindo a aplicação que está sendo testada.
        root.iconify()
        profile_path, scenario_path = chosen_profile.get(), suite_path or chosen_case.get()

        def worker():
            import pythoncom
            pythoncom.CoInitialize()
            try:
                executor = run_suite if suite_path else run_scenario
                messages.put(executor(profile_path, scenario_path, cancel_event=stop))
            except Exception as exc:
                messages.put({'erro': f'Não foi possível iniciar ({type(exc).__name__}). Confira ambiente e cenário.'})
            finally:
                pythoncom.CoUninitialize()
        threading.Thread(target=worker, daemon=False).start()
        root.after(250, poll)

    def show_report():
        if active['report']:
            webbrowser.open(active['report'].resolve().as_uri())
    runbutton = ttk.Button(actions, text='Executar cenário', command=execute)
    runbutton.pack(side='left')
    def select_suite():
        if active['running']:
            return
        path = filedialog.askopenfilename(initialdir=str(ROOT / 'examples'), filetypes=[('Lote de cenários', '*.json')])
        if path:
            execute(path)
    suitebutton = ttk.Button(actions, text='Executar lote...', command=select_suite)
    suitebutton.pack(side='left', padx=8)
    stopbutton = ttk.Button(actions, text='Solicitar parada', command=stop.set, state='disabled')
    stopbutton.pack(side='left', padx=8)
    ttk.Button(actions, text='Abrir último relatório', command=show_report).pack(side='left')
    ttk.Label(frame, text='Novo fluxo exige um cenário implementado e resultado esperado. Os modelos de negócio começam desativados.', wraplength=790).pack(anchor='w', pady=15)

    def close():
        if active['running']:
            stop.set()
            state.set('Parada solicitada. Aguarde a ação atual terminar antes de fechar.')
        else:
            root.destroy()
    root.protocol('WM_DELETE_WINDOW', close)
    # Reabre a última seleção sem executar novamente o cenário.
    try:
        histories = sorted((ROOT / 'reports/execucoes').glob('*/resumo.json'))
        if histories:
            context = json.loads(histories[-1].read_text(encoding='utf-8'))['contexto']
            profile_name = context['perfil'].get('nome', '')
            profile_path = ROOT / 'profiles' / (profile_name + '.json')
            if profile_name and profile_path.parent.resolve() == (ROOT / 'profiles').resolve():
                profile = load_profile(profile_path)
                chosen_profile.set(str(profile_path))
                origin.set(profile['origem_rh']['alias'])
                host.set(profile['destino_sql']['servidor'])
                database.set(profile['destino_sql']['banco'])
                update_origin()
            for path in sorted((ROOT / 'examples/cenarios').glob('*.json')):
                case = load_scenario(path)
                if case['id'] == context.get('cenario'):
                    chosen_case.set(str(path))
                    state.set('Última seleção carregada. Nenhum teste iniciado.')
                    break
    except (OSError, ValueError, KeyError, TypeError):
        pass
    root.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--perfil')
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument('--cenario')
    selection.add_argument('--lote')
    args = parser.parse_args()
    if args.perfil or args.cenario or args.lote:
        if not args.perfil or not (args.cenario or args.lote):
            parser.error('Informe --perfil e --cenario ou --lote juntos.')
        result = run_suite(args.perfil, args.lote) if args.lote else run_scenario(args.perfil, args.cenario)
        print(json.dumps(result, ensure_ascii=False))
        raise SystemExit(0 if result['estado'] == 'PASSOU' else 1)
    gui()
