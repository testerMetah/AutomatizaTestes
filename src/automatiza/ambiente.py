"""Verificação de desktop e Schannel, sem mudar permissões ou configuração."""
import ctypes
import os
from ctypes import wintypes


def desktop_context():
    if os.name != 'nt':
        return {'disponivel': False, 'motivo': 'A automação de tela exige Windows.'}
    user = ctypes.WinDLL('user32', use_last_error=True)
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    user.GetThreadDesktop.argtypes = [wintypes.DWORD]
    user.GetThreadDesktop.restype = wintypes.HANDLE
    user.OpenInputDesktop.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    user.OpenInputDesktop.restype = wintypes.HANDLE
    user.CloseDesktop.argtypes = [wintypes.HANDLE]
    user.GetUserObjectInformationW.argtypes = [wintypes.HANDLE, ctypes.c_int,
                                               ctypes.c_void_p, wintypes.DWORD,
                                               ctypes.POINTER(wintypes.DWORD)]

    def name(handle):
        buffer = ctypes.create_unicode_buffer(512)
        length = wintypes.DWORD()
        if not user.GetUserObjectInformationW(handle, 2, buffer, ctypes.sizeof(buffer), ctypes.byref(length)):
            return None
        return buffer.value

    current = name(user.GetThreadDesktop(kernel.GetCurrentThreadId()))
    incoming = user.OpenInputDesktop(0, False, 1)  # DESKTOP_READOBJECTS, somente leitura
    expected = None
    if incoming:
        try:
            expected = name(incoming)
        finally:
            user.CloseDesktop(incoming)
    isolated = bool(current and current.startswith('CodexSandboxDesktop'))
    available = bool(current and expected and current == expected and not isolated)
    return {'disponivel': available, 'desktop_processo': current,
            'desktop_entrada': expected, 'isolado_codex': isolated,
            'motivo': None if available else 'O processo não está no desktop de entrada do usuário ou não pôde verificá-lo.'}


def require_interactive_desktop():
    context = desktop_context()
    if not context['disponivel']:
        raise RuntimeError('Automação de tela indisponível nesta sessão: desktop isolado ou inacessível. '
                           'Nenhum aplicativo foi iniciado e nenhuma credencial foi preenchida. '
                           'Revise o acesso autorizado à área de trabalho nos controles da sessão.')
    return context


def schannel_probe():
    """Testa inicialização TLS local; não abre rede nem fornece credenciais de usuário."""
    if os.name != 'nt':
        return {'disponivel': False, 'motivo': 'Schannel é específico do Windows.'}

    class Credential(ctypes.Structure):
        _fields_ = [('dwVersion', wintypes.DWORD), ('cCreds', wintypes.DWORD),
                    ('paCred', ctypes.c_void_p), ('hRootStore', ctypes.c_void_p),
                    ('cMappers', wintypes.DWORD), ('aphMappers', ctypes.c_void_p),
                    ('cSupportedAlgs', wintypes.DWORD), ('palgSupportedAlgs', ctypes.c_void_p),
                    ('grbitEnabledProtocols', wintypes.DWORD), ('dwMinimumCipherStrength', wintypes.DWORD),
                    ('dwMaximumCipherStrength', wintypes.DWORD), ('dwSessionLifespan', wintypes.DWORD),
                    ('dwFlags', wintypes.DWORD), ('dwCredFormat', wintypes.DWORD)]

    class Handle(ctypes.Structure):
        _fields_ = [('lower', ctypes.c_size_t), ('upper', ctypes.c_size_t)]

    security = ctypes.WinDLL('secur32')
    security.AcquireCredentialsHandleW.argtypes = [wintypes.LPWSTR, wintypes.LPWSTR, wintypes.ULONG,
                                                  ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
                                                  ctypes.c_void_p, ctypes.POINTER(Handle), ctypes.c_void_p]
    security.AcquireCredentialsHandleW.restype = wintypes.LONG
    security.FreeCredentialsHandle.argtypes = [ctypes.POINTER(Handle)]
    credential = Credential()
    credential.dwVersion = 4  # SCHANNEL_CRED_VERSION, defaults de protocolo do Windows
    handle = Handle()
    expiry = ctypes.c_longlong()
    status = security.AcquireCredentialsHandleW(None, 'Microsoft Unified Security Protocol Provider',
                                                2, None, ctypes.byref(credential), None, None,
                                                ctypes.byref(handle), ctypes.byref(expiry))
    if status == 0:
        security.FreeCredentialsHandle(ctypes.byref(handle))
    code = status & 0xffffffff
    return {'disponivel': status == 0, 'codigo_sspi': f'0x{code:08X}',
            'sem_conexao_de_rede': True, 'sem_credenciais_do_usuario': True,
            'descricao': {0: 'SEC_E_OK', 0x8009030e: 'SEC_E_NO_CREDENTIALS',
                          0x80090304: 'SEC_E_INTERNAL_ERROR'}.get(code, 'Outro status SSPI')}
