"""Reabre o módulo Escola da cópia de teste após uma exceção Delphi."""

from pywinauto import Desktop
from pywinauto.timings import wait_until

from abrir_e_levantar_auditoria import choose_menu, module_pid, principal, process_path, FOLDER


def main():
    pid = module_pid("Acessus.Escola.exe")
    if pid is None:
        panel = [w for w in Desktop(backend="win32").windows()
                 if w.class_name() == "TFrmModuloViewsPrincipal" and w.is_visible()
                 and process_path(w.process_id()) == (FOLDER / "Acessus.Modulo.exe").resolve()]
        if len(panel) != 1:
            raise RuntimeError("Painel da cópia de teste não encontrado")
        choose_menu(panel[0], "Modulos", "Escola")
        wait_until(30, 0.5, lambda: module_pid("Acessus.Escola.exe") is not None)
        pid = module_pid("Acessus.Escola.exe")
    wait_until(30, 0.5, lambda: principal(pid) is not None)
    for _ in range(3):
        if any("AuditoriaHistorico" in c.class_name()
               for c in principal(pid).descendants()):
            print(pid)
            return
        choose_menu(principal(pid), "Consultas", "Auditorias/Hist")
        try:
            wait_until(10, 0.5, lambda: any("AuditoriaHistorico" in c.class_name()
                                             for c in principal(pid).descendants()))
            print(pid)
            return
        except Exception:
            pass
    raise RuntimeError("Auditorias/Históricos não abriu após três tentativas")


if __name__ == "__main__":
    main()
