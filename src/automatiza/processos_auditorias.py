"""Descoberta por caminho absoluto via API Windows já presente na venv 32 bits."""
from pathlib import Path


def caminho_processo(pid):
    import win32api
    import win32con
    import win32process
    handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
    try:
        return Path(win32process.GetModuleFileNameEx(handle, 0)).resolve()
    finally:
        handle.Close()


def descobrir(executavel, *, enum_processes=None, resolver=None):
    import win32process
    enum_processes = enum_processes or win32process.EnumProcesses
    resolver = resolver or caminho_processo
    expected = Path(executavel).resolve()
    found = []
    for pid in enum_processes():
        try:
            if Path(resolver(pid)).resolve() == expected:
                found.append(pid)
        except (OSError, PermissionError):
            continue
    if len(found) > 1:
        raise RuntimeError(f"Há {len(found)} processos para {expected}; feche os extras ou use --pid.")
    return found[0] if found else None


def validar_pid(pid, executavel, *, resolver=None):
    resolver = resolver or caminho_processo
    if Path(resolver(pid)).resolve() != Path(executavel).resolve():
        raise ValueError(f"PID {pid} não corresponde ao executável do perfil.")
    return pid
