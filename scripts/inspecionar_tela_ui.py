"""Exporta controles win32 de uma tela validada sem alterar dados."""

import argparse
from datetime import datetime
from pathlib import Path

from pywinauto import Desktop
from automatiza.tela_generica import TelaGenerica


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mapa", help="Nome do YAML em src/automatiza/mapas")
    args = parser.parse_args()
    tela = TelaGenerica(args.mapa)
    janela = tela.abrir()
    pasta = Path(r"C:\AutomatizaTestes\docs\mapas-de-tela")
    pasta.mkdir(parents=True, exist_ok=True)
    destino = pasta / f"{args.mapa}-win32-{datetime.now():%Y%m%d-%H%M%S}.txt"
    Desktop(backend="win32").window(handle=janela.handle).print_control_identifiers(filename=str(destino))
    tela.fechar()
    print(destino)


if __name__ == "__main__":
    main()
