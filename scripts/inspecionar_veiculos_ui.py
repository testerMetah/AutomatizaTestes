"""Exporta a árvore real de Veículos sem preencher nem salvar dados."""

from datetime import datetime
from pathlib import Path
from pywinauto import Desktop


CLASSE = "TFrmEstacionamentoViewsCadastroVeiculos"
DESTINO = Path(r"C:\AutomatizaTestes\docs\mapas-de-tela")


def main():
    principais = Desktop(backend="win32").windows(class_name="TFrmEstacionamentoViewsPrincipal", visible_only=True)
    janelas = [filho for principal in principais for filho in principal.descendants()
               if filho.class_name() == CLASSE and filho.is_visible()]
    if len(janelas) != 1:
        raise SystemExit(f"Esperada uma janela {CLASSE} aberta; encontradas {len(janelas)}. Abra Estacionamento > Cadastros > Veículos.")
    janela = janelas[0]
    DESTINO.mkdir(parents=True, exist_ok=True)
    destino = DESTINO / f"veiculos-win32-{datetime.now():%Y%m%d-%H%M%S}.txt"
    Desktop(backend="win32").window(handle=janela.handle).print_control_identifiers(filename=str(destino))
    print(destino)
    print("Compare EdNomeVeiculo, EdPlaca e botões com o DFM; registre found_index apenas após associação inequívoca.")


if __name__ == "__main__":
    main()
