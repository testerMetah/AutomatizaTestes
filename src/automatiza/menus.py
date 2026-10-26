"""Leitura de HMENU pelo Windows sem memória remota do processo Delphi."""
import ctypes
from ctypes import wintypes


def click_uia_menu(window, route):
    """Menus Delphi TActionMainMenuBar sem HMENU; exige item visível único."""
    from pywinauto import Desktop
    if not route or any(not isinstance(part, str) or not part.strip() for part in route):
        raise ValueError('Informe uma rota de menu com legendas não vazias.')
    if not window.is_visible() or not window.is_enabled():
        raise RuntimeError('Janela indisponível ou bloqueada por diálogo.')
    window.set_focus()
    panel = Desktop(backend='uia').window(handle=window.handle)
    for caption in route:
        # Filtrar visibilidade é essencial: o provedor Delphi repete itens
        # de menus fechados, inclusive Pessoas em Cadastros e Relatórios.
        item = panel.child_window(title=caption, control_type='MenuItem', visible_only=True)
        item.wait('visible enabled', timeout=10)
        item.click_input()


def native_menu(handle):
    user = ctypes.WinDLL('user32', use_last_error=True)
    user.GetMenu.argtypes = [wintypes.HWND]
    user.GetMenu.restype = wintypes.HMENU
    user.GetSubMenu.argtypes = [wintypes.HMENU, ctypes.c_int]
    user.GetSubMenu.restype = wintypes.HMENU
    user.GetMenuItemCount.argtypes = [wintypes.HMENU]
    user.GetMenuStringW.argtypes = [wintypes.HMENU, wintypes.UINT, wintypes.LPWSTR, ctypes.c_int, wintypes.UINT]
    user.GetMenuItemID.argtypes = [wintypes.HMENU, ctypes.c_int]
    user.GetMenuItemID.restype = wintypes.UINT
    user.GetMenuState.argtypes = [wintypes.HMENU, wintypes.UINT, wintypes.UINT]
    user.GetMenuState.restype = wintypes.UINT
    menu = user.GetMenu(handle)
    if not menu:
        return []
    seen = set()

    def walk(current, parents=(), depth=0):
        if current in seen or depth > 10:
            return []
        seen.add(current)
        entries = []
        for index in range(max(0, user.GetMenuItemCount(current))):
            buffer = ctypes.create_unicode_buffer(1024)
            user.GetMenuStringW(current, index, buffer, len(buffer), 0x400)
            caption = buffer.value.split('\t')[0]
            state = user.GetMenuState(current, index, 0x400)
            if state == 0xffffffff or state & 0x800 or not caption:
                continue
            route = [*parents, caption.replace('&', '')]
            sub = user.GetSubMenu(current, index)
            entry = {'legenda': caption, 'rota': route, 'habilitado': not bool(state & 3),
                     'id_comando': None if sub else user.GetMenuItemID(current, index),
                     'filhos': walk(sub, route, depth+1) if sub else []}
            entries.append(entry)
        return entries
    return walk(menu)


def leaves(tree, enabled=True):
    for entry in tree:
        allowed = enabled and entry['habilitado']
        if entry['filhos']:
            yield from leaves(entry['filhos'], allowed)
        else:
            yield {**entry, 'habilitado': allowed}


def invoke_native(window, route):
    if not window.is_visible() or not window.is_enabled():
        raise RuntimeError('Janela indisponível ou bloqueada por diálogo.')
    matches = [e for e in leaves(native_menu(window.handle)) if e['rota'] == route]
    if len(matches) != 1 or not matches[0]['habilitado']:
        raise RuntimeError('A rota não está disponível de forma única e habilitada.')
    command = matches[0]['id_comando']
    if command is None or command in (0, 0xffffffff):
        raise RuntimeError('A rota não possui comando nativo válido.')
    # PostMessage evita bloquear o executor enquanto o aplicativo exibe modal.
    user = ctypes.WinDLL('user32', use_last_error=True)
    user.PostMessageW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
    if not user.PostMessageW(window.handle, 0x111, command, 0):
        raise ctypes.WinError(ctypes.get_last_error())
    return command
