"""Sentinela Win32: hotkey global, toast sem foco e diálogo de pausa."""
import ctypes
import json
import os
import queue
import sys
import threading
import time
import tkinter as tk
from datetime import datetime, timezone
from uuid import uuid4
from ctypes import wintypes
from pathlib import Path

from automatiza.pausa import configuracao, gravar, ler

USER32 = ctypes.windll.user32 if os.name == "nt" else None
KERNEL32 = ctypes.windll.kernel32 if os.name == "nt" else None
MOD_NOREPEAT = 0x4000
MOD_CONTROL = 2
MOD_SHIFT = 4
HOTKEYS = {"Pause": (0, 0x13), "Ctrl+Shift+F9": (MOD_CONTROL | MOD_SHIFT, 0x78),
           "Ctrl+Shift+P": (MOD_CONTROL | MOD_SHIFT, 0x50)}
WS_EX_NOACTIVATE = 0x08000000
WS_EX_TOOLWINDOW = 0x80
WS_EX_TRANSPARENT = 0x20
WS_EX_LAYERED = 0x80000
GWL_EXSTYLE = -20
HWND_TOPMOST = -1
SWP_NOACTIVATE = 0x10
SWP_SHOWWINDOW = 0x40


def escolher_atalho(registrar, atalhos):
    for atalho in atalhos:
        mods, key = HOTKEYS[atalho]
        if registrar(mods | MOD_NOREPEAT, key):
            return atalho
    return None


class Antirrepique:
    def __init__(self, intervalo=0.4):
        self.intervalo = intervalo
        self.anterior = -float("inf")

    def aceitar(self, agora=None):
        agora = time.monotonic() if agora is None else agora
        if agora - self.anterior < self.intervalo:
            return False
        self.anterior = agora
        return True


def _filhos(pid, excluir=()):
    """Enumera a árvore do teste, excluindo o sentinela e seus descendentes."""
    if os.name != "nt":
        return []
    class ENTRY(ctypes.Structure):
        _fields_ = [("dwSize", wintypes.DWORD), ("cntUsage", wintypes.DWORD),
                    ("th32ProcessID", wintypes.DWORD), ("th32DefaultHeapID", ctypes.c_void_p),
                    ("th32ModuleID", wintypes.DWORD), ("cntThreads", wintypes.DWORD),
                    ("th32ParentProcessID", wintypes.DWORD), ("pcPriClassBase", ctypes.c_long),
                    ("dwFlags", wintypes.DWORD), ("szExeFile", ctypes.c_char * 260)]
    snap = KERNEL32.CreateToolhelp32Snapshot(2, 0)
    if snap == ctypes.c_void_p(-1).value:
        return []
    entry = ENTRY()
    entry.dwSize = ctypes.sizeof(entry)
    pairs = []
    try:
        ok = KERNEL32.Process32First(snap, ctypes.byref(entry))
        while ok:
            pairs.append((entry.th32ProcessID, entry.th32ParentProcessID))
            ok = KERNEL32.Process32Next(snap, ctypes.byref(entry))
    finally:
        KERNEL32.CloseHandle(snap)
    return _arvore_do_teste(pid, pairs, excluir, os.getpid())


def _arvore_do_teste(pid, pairs, excluir=(), proprio=None):
    """Inclui o supervisor; nunca inclui a árvore do sentinela."""
    excluidos = set(excluir)
    for _ in range(len(pairs)):
        novos = excluidos | {child for child, parent in pairs if parent in excluidos}
        if novos == excluidos:
            break
        excluidos = novos
    found = {pid} - excluidos
    for _ in range(len(pairs)):
        newer = found | {child for child, parent in pairs if parent in found and child not in excluidos}
        if newer == found:
            break
        found = newer
    return [x for x in found if x != proprio]


def _suspender(pid, pausa):
    handle = KERNEL32.OpenProcess(0x0800, False, pid)  # PROCESS_SUSPEND_RESUME
    if not handle:
        return False
    try:
        func = ctypes.windll.ntdll.NtSuspendProcess if pausa else ctypes.windll.ntdll.NtResumeProcess
        return func(handle) == 0
    finally:
        KERNEL32.CloseHandle(handle)


class Sentinela:
    def __init__(self, pasta):
        self.pasta = Path(pasta)
        self.cfg = configuracao()
        self.meta = ler(self.pasta / "meta.json")
        self.fila = queue.SimpleQueue()
        self.root = tk.Tk()
        self.root.withdraw()
        self.toast = None
        self.dialogo = None
        self.atalho = None
        self.repeticao = Antirrepique()
        self.ultimo_pedido = None
        self.inicio_pausa = None
        self.total_pausado_ms = 0
        self.suspensos = []
        self.modo = ""
        self.ultima_lembranca = 0
        self.terminado = False
        self.ultimo_heartbeat = 0

    def registrar(self):
        def loop():
            ids = []
            hook = None
            callback = None
            for i, nome in enumerate(self.cfg["atalhos"], 1):
                mods, vk = HOTKEYS[nome]
                if USER32.RegisterHotKey(None, i, mods | MOD_NOREPEAT, vk):
                    ids.append(i)
                    self.fila.put(("registrado", nome))
            if not ids:
                # O hook de baixo nível consome a tecla. Polling sozinho deixaria
                # a tecla chegar ao Acessus e não atende ao requisito de segurança.
                CALLBACK = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
                def interceptar(ncode, wparam, lparam):
                    if ncode >= 0 and wparam in (0x0100, 0x0104):
                        vk = ctypes.cast(lparam, ctypes.POINTER(wintypes.DWORD)).contents.value
                        for nome in self.cfg["atalhos"]:
                            mods, tecla = HOTKEYS[nome]
                            ctrl = bool(USER32.GetAsyncKeyState(0x11) & 0x8000)
                            shift = bool(USER32.GetAsyncKeyState(0x10) & 0x8000)
                            if vk == tecla and ctrl == bool(mods & MOD_CONTROL) and shift == bool(mods & MOD_SHIFT):
                                self.fila.put(("atalho", nome))
                                return 1
                    return USER32.CallNextHookEx(None, ncode, wparam, lparam)
                callback = CALLBACK(interceptar)
                hook = USER32.SetWindowsHookExW(13, callback, KERNEL32.GetModuleHandleW(None), 0)
                if hook:
                    self.fila.put(("registrado", self.cfg["atalhos"][0]))
                else:
                    self.fila.put(("indisponivel", None))
            msg = wintypes.MSG()
            while USER32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
                if msg.message == 0x0312:
                    i = msg.wParam
                    if i in ids:
                        self.fila.put(("atalho", self.cfg["atalhos"][i - 1]))
                if (self.pasta / "encerrar.json").exists():
                    break
            for i in ids:
                USER32.UnregisterHotKey(None, i)
            if hook:
                USER32.UnhookWindowsHookEx(hook)
        threading.Thread(target=loop, daemon=True).start()

    def _toast(self, titulo, texto, segundos, cor):
        if not self.cfg["avisos"]:
            return
        if self.toast:
            self.toast.destroy()
        win = tk.Toplevel(self.root)
        win.withdraw()  # Nunca mostrar a janela antes de aplicar NOACTIVATE.
        self.toast = win
        win.overrideredirect(True)
        win.attributes("-topmost", True)
        win.configure(bg=cor)
        tk.Label(win, text=titulo, fg="white", bg=cor, font=("Segoe UI", 13, "bold"), anchor="w").pack(fill="x", padx=16, pady=(12, 2))
        tk.Label(win, text=texto, fg="white", bg=cor, font=("Segoe UI", 10), justify="left", anchor="w").pack(fill="x", padx=16, pady=(0, 12))
        win.update_idletasks()
        width, height = 350, win.winfo_reqheight()
        win.geometry(f"{width}x{height}+{win.winfo_screenwidth()-width-18}+{win.winfo_screenheight()-height-65}")
        win.update_idletasks()
        hwnd = USER32.GetAncestor(win.winfo_id(), 2) or win.winfo_id()  # GA_ROOT: janela real do Tk.
        style = USER32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        USER32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_NOACTIVATE | WS_EX_TOOLWINDOW | WS_EX_TRANSPARENT | WS_EX_LAYERED)
        USER32.ShowWindow(hwnd, 4)  # SW_SHOWNOACTIVATE
        USER32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, 0x1 | 0x2 | SWP_NOACTIVATE | SWP_SHOWWINDOW)
        fim = time.monotonic() + segundos
        def expirar():
            if not win.winfo_exists():
                return
            x, y = USER32.GetCursorPos, wintypes.POINT()
            x(ctypes.byref(y))
            sobre = win.winfo_rootx() <= y.x <= win.winfo_rootx() + width and win.winfo_rooty() <= y.y <= win.winfo_rooty() + height
            if sobre:
                self.root.after(200, expirar)
            elif time.monotonic() < fim:
                self.root.after(100, expirar)
            else:
                win.destroy()
                if self.toast is win:
                    self.toast = None
        self.root.after(100, expirar)

    def _dialogo(self):
        if self.dialogo and self.dialogo.winfo_exists():
            self.dialogo.lift()
            return
        win = tk.Toplevel(self.root)
        self.dialogo = win
        win.title("Teste PAUSADO")
        win.attributes("-topmost", True)
        win.resizable(False, False)
        win.protocol("WM_DELETE_WINDOW", lambda: None)
        self.info = tk.StringVar()
        tk.Label(win, text="Teste PAUSADO", font=("Segoe UI", 15, "bold")).pack(padx=24, pady=(18, 6))
        tk.Label(win, textvariable=self.info, justify="left", wraplength=430).pack(padx=24)
        tk.Label(win, text="A automação parou de mexer no mouse e no teclado. Você pode usar a máquina. Escolha:", wraplength=430).pack(padx=24, pady=12)
        box = tk.Frame(win)
        box.pack(pady=(0, 18))
        tk.Button(box, text="Continuar", command=self.continuar, default="active").pack(side="left", padx=8)
        tk.Button(box, text="Cancelar teste", command=self.confirmar_cancelamento).pack(side="left", padx=8)
        win.bind("<Return>", lambda _: self.continuar())
        win.bind("<c>", lambda _: self.continuar())
        win.bind("<x>", lambda _: self.confirmar_cancelamento())
        win.bind("<Escape>", lambda _: "break")
        win.update_idletasks()
        win.geometry(f"+{(win.winfo_screenwidth()-win.winfo_width())//2}+{(win.winfo_screenheight()-win.winfo_height())//2}")
        win.lift()
        win.focus_force()

    def confirmar_cancelamento(self):
        import tkinter.messagebox as mb
        if mb.askyesno("Cancelar teste", "Cancelar mesmo?", parent=self.dialogo):
            self.cancelar()

    def pedir_pausa(self, origem):
        if self.inicio_pausa is not None:
            self._dialogo()
            return
        self.inicio_pausa = time.monotonic()
        self.origem = origem
        gravar(self.pasta / "controle.json", {"estado": "PAUSADO", "instante": time.time(), "origem": origem,
                                               "janela_anterior": USER32.GetForegroundWindow()})
        self.modo = "Aguardando ponto seguro"
        self._dialogo()

    def continuar(self):
        if self.inicio_pausa is None:
            return
        for pid in reversed(self.suspensos):
            _suspender(pid, False)
        self.suspensos.clear()
        anterior = ler(self.pasta / "controle.json").get("janela_anterior")
        duracao = round((time.monotonic()-self.inicio_pausa)*1000, 1)
        self.total_pausado_ms += duracao
        gravar(self.pasta / "controle.json", {"estado": "RODANDO", "instante": time.time(),
                                               "janela_anterior": anterior, "pausado_total_ms": self.total_pausado_ms})
        self._evento("PAUSA_RETOMADA", duracao_ms=duracao, modo=self.modo)
        self.inicio_pausa = None
        if self.dialogo:
            self.dialogo.destroy()
            self.dialogo = None

    def cancelar(self):
        for pid in reversed(self.suspensos):
            _suspender(pid, False)
        self.suspensos.clear()
        gravar(self.pasta / "controle.json", {"estado": "CANCELANDO", "instante": time.time()})
        self._evento("CANCELADO_PELO_USUARIO", modo=self.modo)
        self.inicio_pausa = None
        if self.dialogo:
            self.dialogo.destroy()
            self.dialogo = None

    def _evento(self, tipo, **dados):
        instante = datetime.now().astimezone()
        local = {"tipo": tipo, "data_hora": instante.timestamp(), **dados}
        with (self.pasta / "eventos.jsonl").open("a", encoding="utf-8") as out:
            out.write(json.dumps(local, ensure_ascii=False) + "\n")
        if tipo not in {"PAUSA_INICIADA", "PAUSA_RETOMADA", "CANCELADO_PELO_USUARIO"}:
            return
        from automatiza.caminhos import logs_permanentes
        linha = (f"[{instante:%d/%m/%Y - %H:%M:%S}] Tela: Execução ao vivo | "
                 f"Módulo: {self.meta.get('nome', 'Teste')} | Histórico: (pausa) | "
                 f"Filtro: (pausa) | {tipo}: {dados}")
        detalhe = {"versao_formato": 1, "execucao_id": self.pasta.name,
                   "evento_id": uuid4().hex, "data_hora_local": instante.isoformat(timespec="milliseconds"),
                   "data_hora_utc": instante.astimezone(timezone.utc).isoformat(timespec="milliseconds"),
                   "contexto_execucao": self.meta, "tipo": tipo, "linha_passo_a_passo": linha, **dados}
        resultado = logs_permanentes()
        resultado.mkdir(exist_ok=True)
        with (resultado / "passo-a-passo.log").open("a", encoding="utf-8") as out:
            out.write(linha + "\n")
        with (resultado / "passo-a-passo-detalhado.jsonl").open("a", encoding="utf-8") as out:
            out.write(json.dumps(detalhe, ensure_ascii=False) + "\n")

    def _tic(self):
        if time.monotonic() - self.ultimo_heartbeat >= 0.2:
            gravar(self.pasta / "heartbeat.json", {"instante": time.time(), "pid": os.getpid()})
            self.ultimo_heartbeat = time.monotonic()
        while not self.fila.empty():
            tipo, valor = self.fila.get_nowait()
            if tipo == "registrado" and self.atalho is None:
                self.atalho = valor
                gravar(self.pasta / "sentinela.json", {"estado": "ATIVA", "atalho": valor})
                self._toast("Teste iniciado", f"{self.meta.get('nome', 'Teste')}\nPerfil: {self.meta.get('perfil', '?')} · Banco: {self.meta.get('banco', '?')}\nPara pausar: {valor}", self.cfg["inicio_segundos"], "#17618b")
            elif tipo == "indisponivel":
                gravar(self.pasta / "sentinela.json", {"estado": "SEM_ATALHO", "atalho": None})
                self._toast("Teste iniciado", "Atalho indisponível; use Pausar no painel.", self.cfg["inicio_segundos"], "#8b5e17")
            elif tipo == "atalho" and self.repeticao.aceitar():
                self._evento("ATALHO_DETECTADO", atalho=valor)
                self.pedir_pausa("atalho")
        pedido = ler(self.pasta / "pedido.json")
        if pedido and pedido.get("instante") != self.ultimo_pedido:
            self.ultimo_pedido = pedido.get("instante")
            acao = pedido.get("acao")
            if acao == "pausar": self.pedir_pausa(pedido.get("origem", "painel"))
            elif acao == "continuar": self.continuar()
            elif acao == "cancelar": self.cancelar()
        if self.inicio_pausa is not None:
            ack = ler(self.pasta / "confirmacao.json")
            if ack.get("estado") == "PAUSADO" and ack.get("instante", 0) >= ler(self.pasta / "controle.json").get("instante", 0):
                if self.modo != "Pausado entre ações":
                    self.modo = "Pausado entre ações"
                    self._evento("PAUSA_INICIADA", origem=self.origem, modo=self.modo,
                                 latencia_ms=round((time.monotonic()-self.inicio_pausa)*1000, 1))
            elif time.monotonic() - self.inicio_pausa >= 1.35 and self.modo == "Aguardando ponto seguro" and self.cfg["congelamento"]:
                # Filhos primeiro; o processo supervisor também pode enviar entradas.
                self.suspensos = [p for p in reversed(_filhos(self.meta["pid"], {os.getpid()})) if _suspender(p, True)]
                self.modo = "Pausado à força" if self.suspensos else "Pausa solicitada; congelamento indisponível"
                self._evento("PAUSA_INICIADA", origem=self.origem, modo=self.modo,
                             latencia_ms=round((time.monotonic()-self.inicio_pausa)*1000, 1))
            if self.dialogo and self.dialogo.winfo_exists():
                self.info.set(f"{self.meta.get('nome', 'Teste')}\n{self.modo}\nDecorrido: {int(time.monotonic()-self.meta['inicio_monotonico'])} s")
            if time.monotonic()-self.inicio_pausa >= 600 and time.monotonic()-self.ultima_lembranca >= 300:
                self.ultima_lembranca = time.monotonic()
                self._toast("Teste pausado", "Aguardando sua escolha: Continuar ou Cancelar.", 5, "#7a5a18")
        final = ler(self.pasta / "final.json")
        if final and not self.terminado:
            self.terminado = True
            estado = final.get("estado", "FALHOU")
            self._toast({"CONCLUIDO": "Teste concluído", "CANCELADO": "Teste cancelado"}.get(estado, "Teste falhou"),
                        final.get("resumo", "") + "\n" + final.get("pasta", ""), self.cfg["fim_segundos"],
                        {"CONCLUIDO": "#1b7449", "CANCELADO": "#81601c"}.get(estado, "#9a3030"))
            self.root.after(int(self.cfg["fim_segundos"]*1000)+500, self.root.destroy)
        self.root.after(30, self._tic)

    def executar(self):
        self.registrar()
        self.root.after(30, self._tic)
        self.root.mainloop()


if __name__ == "__main__":
    Sentinela(sys.argv[1]).executar()
