"""Consulta ao estado de serviços Windows; não expõe operações de controle."""

import ctypes
from ctypes import wintypes

SERVICES = {
    "FrmSyncImpViewsPrincipal": "Acessus - Importação API",
    "FrmViewsPrincipalService": "AcessusSync",
    "MetahConnectServiceTarefas": "MetahConnectService",
    "SrvAcessusCom": "Acessus - Comunicação",
}
STATES = {1: "PARADO", 2: "INICIANDO", 3: "PARANDO", 4: "EXECUTANDO",
          5: "RETOMANDO", 6: "PAUSANDO", 7: "PAUSADO"}


class ServiceStatus(ctypes.Structure):
    _fields_ = [(name, wintypes.DWORD) for name in
                ("tipo", "estado", "controles", "erro_windows", "erro_servico", "checkpoint",
                 "espera", "processo_id", "flags")]


def snapshot_services(names=SERVICES):
    api = ctypes.WinDLL("advapi32", use_last_error=True)
    api.OpenSCManagerW.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.DWORD]
    api.OpenSCManagerW.restype = wintypes.HANDLE
    api.OpenServiceW.argtypes = [wintypes.HANDLE, wintypes.LPCWSTR, wintypes.DWORD]
    api.OpenServiceW.restype = wintypes.HANDLE
    api.QueryServiceStatusEx.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p,
                                       wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
    api.QueryServiceStatusEx.restype = wintypes.BOOL
    api.CloseServiceHandle.argtypes = [wintypes.HANDLE]
    api.CloseServiceHandle.restype = wintypes.BOOL
    manager = api.OpenSCManagerW(None, None, 0x0001)  # SC_MANAGER_CONNECT
    if not manager:
        raise OSError(ctypes.get_last_error(), "Não foi possível consultar o gerenciador de serviços.")
    result = []
    try:
        for name in names:
            item = {"nome": name, "descricao": SERVICES.get(name, name)}
            handle = api.OpenServiceW(manager, name, 0x0004)  # SERVICE_QUERY_STATUS
            if not handle:
                error = ctypes.get_last_error()
                item.update(estado="NAO_ENCONTRADO" if error == 1060 else "INDISPONIVEL", codigo_erro=error)
            else:
                try:
                    status, needed = ServiceStatus(), wintypes.DWORD()
                    if api.QueryServiceStatusEx(handle, 0, ctypes.byref(status), ctypes.sizeof(status), ctypes.byref(needed)):
                        item.update(estado=STATES.get(status.estado, "DESCONHECIDO"), processo_id=status.processo_id)
                    else:
                        item.update(estado="INDISPONIVEL", codigo_erro=ctypes.get_last_error())
                finally:
                    api.CloseServiceHandle(handle)
            result.append(item)
    finally:
        api.CloseServiceHandle(manager)
    return result


def service_changes(before, after):
    old = {item["nome"]: item for item in before}
    events = []
    for item in after:
        previous = old.get(item["nome"])
        if previous is not None and previous != item:
            events.append({"nome": item["nome"], "antes": previous, "depois": item})
    return events
