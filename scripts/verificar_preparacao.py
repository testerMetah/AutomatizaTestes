"""Diagnóstico de preparação; --sql habilita consultas limitadas somente de leitura."""
import argparse
from automatiza.preparacao import inspect_preparation, save_preparation


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sql', action='store_true')
    args = parser.parse_args()
    result = inspect_preparation(sql=args.sql)
    folder = save_preparation(result)
    print(result['estado'])
    for check in result['verificacoes']:
        print(check['estado'] + ': ' + check['item'] + ' — ' + str(check['detalhe']))
    print('RELATORIO: ' + str(folder / 'preparacao.html'))
    raise SystemExit(0 if result['estado'] == 'PREPARACAO_TECNICA_CONFERIDA' else 2)
