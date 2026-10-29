"""Abre uma tela ainda não validada, exporta a árvore win32 e fecha sem gravar."""

import argparse
from datetime import datetime
from pathlib import Path

from pywinauto import Desktop
from pywinauto.timings import wait_until_passes

from automatiza.abertura_modulo import abrir_modulo
from automatiza.menus import click_uia_menu
from automatiza.tela_generica import TelaGenerica


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mapa")
    parser.add_argument("--incluir-cancelar", action="store_true",
                        help="Inspeciona também a aba de inclusão e cancela sem gravar")
    args = parser.parse_args()
    tela = TelaGenerica(args.mapa)
    principal = abrir_modulo(tela.mapa["principal_class"])

    def form_aberto():
        forms = [w for w in principal.descendants()
                 if w.class_name() == tela.mapa["form_class"] and w.is_visible()]
        if not forms:
            raise RuntimeError(f"Aguardando {tela.mapa['form_class']}")
        return forms[0]

    click_uia_menu(principal, tela.mapa["menu"])
    form = wait_until_passes(15, 0.2, form_aberto)
    destino = Path(__file__).parents[1] / "docs" / "mapas-de-tela" / (
        f"{args.mapa}-win32-{datetime.now():%Y%m%d-%H%M%S}.txt")
    try:
        Desktop(backend="win32").window(handle=form.handle).print_control_identifiers(filename=str(destino))
        print(destino)
        if args.incluir_cancelar:
            botoes = form.descendants(class_name="THoverSpeedButton", title="Incluir (Ctrl+I)")
            if len(botoes) != 1:
                raise RuntimeError(f"Botão Incluir ambíguo: {len(botoes)}")
            botoes[0].click_input()
            def cancelar_visivel():
                controles = [w for w in form.descendants(class_name="THoverSpeedButton")
                             if "Cancelar" in w.window_text() and w.is_visible()]
                if len(controles) != 1:
                    raise RuntimeError(f"Aguardando Cancelar: {len(controles)}")
                return controles[0]
            cancelar = wait_until_passes(10, 0.2, cancelar_visivel)
            inclusao = destino.with_name(destino.stem + "-inclusao.txt")
            Desktop(backend="win32").window(handle=form.handle).print_control_identifiers(filename=str(inclusao))
            print(inclusao)
            cancelar.click_input()
    finally:
        form.close()


if __name__ == "__main__":
    main()
