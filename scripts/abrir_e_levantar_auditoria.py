"""Abre um módulo pela sessão autenticada e levanta Auditorias/Históricos."""

import sys
from pathlib import Path

import win32api
import win32con
import win32process
import pywintypes
from pywinauto import Desktop
from pywinauto.timings import wait_until

from levantar_auditorias_runtime import survey


FOLDER = Path(r"C:\AcessusHostFisico")
MODULES = {
    "portaria": ("Portaria", "Acessus.Portaria.exe"),
    "estacionamento": ("Estacionamento", "Acessus.Estacionamento.exe"),
    "escola": ("Escola", "Acessus.Escola.exe"),
    "administracao": ("Administra", "Acessus.Administracao.exe"),
}


def module_pid(filename):
    expected = (FOLDER / filename).resolve()
    for pid in win32process.EnumProcesses():
        try:
            if process_path(pid) == expected:
                return pid
        except (OSError, PermissionError, pywintypes.error):
            continue
    return None


def process_path(pid):
    handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ,
                                  False, pid)
    try:
        return Path(win32process.GetModuleFileNameEx(handle, 0)).resolve()
    finally:
        handle.Close()


def principal(pid):
    matches = [window for window in Desktop(backend="win32").windows(process=pid)
               if window.class_name().endswith("Principal") and window.is_visible()]
    return matches[0] if len(matches) == 1 else None


def choose_menu(parent, top, prefix):
    parent.set_focus()
    window = Desktop(backend="uia").window(handle=parent.handle)

    def matches():
        return [item for item in window.descendants(control_type="MenuItem")
                if item.is_visible() and item.window_text().startswith(prefix)]

    items = matches()
    if not items:
        window.child_window(title=top, control_type="MenuItem", visible_only=True).click_input()
        items = matches()
    if len(items) != 1:
        raise RuntimeError(f"Menu {prefix!r}: encontrados {len(items)} itens visíveis")
    items[0].click_input()


def main(module):
    prefix, filename = MODULES[module]
    if not (FOLDER / filename).is_file():
        raise RuntimeError(f"Executável não encontrado: {filename}")
    pid = module_pid(filename)
    if pid is None:
        panel = [window for window in Desktop(backend="win32").windows()
                 if window.class_name() == "TFrmModuloViewsPrincipal" and window.is_visible()
                 and process_path(window.process_id()) == (FOLDER / "Acessus.Modulo.exe").resolve()]
        if len(panel) != 1:
            raise RuntimeError("Painel autenticado da cópia física não encontrado")
        choose_menu(panel[0], "Modulos", prefix)
        wait_until(30, 0.5, lambda: module_pid(filename) is not None)
        pid = module_pid(filename)
    wait_until(30, 0.5, lambda: principal(pid) is not None)
    window = principal(pid)
    choose_menu(window, "Consultas", "Auditorias/Hist")
    wait_until(20, 0.5, lambda: any("AuditoriaHistorico" in c.class_name()
                                    for c in principal(pid).descendants()))
    return survey(pid, module)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
