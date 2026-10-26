"""Consolida somente evidências locais; não acessa SQL, serviços ou desktop."""
import json
from pathlib import Path
from collections import Counter


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8-sig'))


def cell(value):
    return str(value).replace('|', '\\|').replace('\r', ' ').replace('\n', ' ')


def table(headers, rows):
    return ['| ' + ' | '.join(headers) + ' |', '|' + '---|'*len(headers)] + [
        '| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows]


def main():
    schema_path = 'reports/banco/20261015-095741/inventario.json'
    schema = read(schema_path)
    indexes = {(r['esquema'], r['tabela'], r['indice']) for r in schema['indices']}
    fks = {(r['esquema_origem'], r['tabela_origem'], r['chave']) for r in schema['relacionamentos']}
    lines = ['# Dicionário da bras1 — evidência histórica', '',
             f"Fonte: `{schema_path}`; observado em {schema['observado_em']}.",
             'Documento gerado agora a partir dessa coleta anterior. Não foi revalidado no servidor nesta sessão.',
             'Sem registros de negócio ou definições SQL. Permissões do login podem limitar a cobertura.', '',
             f"{len(schema['objetos'])} objetos; {len(schema['colunas'])} colunas; {len(indexes)} índices distintos; "
             f"{len(fks)} restrições FK, com {len(schema['relacionamentos'])} vínculos de colunas.", '']
    for obj in schema['objetos']:
        name, owner = obj['objeto'], obj['esquema']
        lines += ['## ' + owner + '.' + name, '', obj['tipo'], '']
        columns = [r for r in schema['colunas'] if r['esquema'] == owner and r['objeto'] == name]
        if columns:
            lines += table(['Coluna', 'Tipo', 'Máximo em bytes', 'Precisão/escala', 'Nulo', 'Identidade', 'Calculada'],
                           [[r['coluna'], r['tipo'], r['bytes_maximos'], f"{r['precisao']}/{r['escala']}",
                             r['aceita_nulo'], r['identidade'], r['calculada']] for r in columns]) + ['']
        entries = [r for r in schema['indices'] if r['esquema'] == owner and r['tabela'] == name]
        if entries:
            lines += table(['Índice', 'Tipo', 'Único', 'PK', 'Coluna', 'Ordem', 'Incluída'],
                           [[r[k] for k in ('indice', 'tipo', 'unico', 'chave_primaria', 'coluna', 'ordem', 'incluida')]
                            for r in entries]) + ['']
        outgoing = [r for r in schema['relacionamentos'] if r['esquema_origem'] == owner and r['tabela_origem'] == name]
        for r in outgoing:
            lines += [f"- {r['coluna_origem']} → {r['esquema_destino']}.{r['tabela_destino']}.{r['coluna_destino']} "
                      f"({r['chave']}); exclusão: {r['ao_excluir']}; desabilitada: {r['desabilitada']}; não validada: {r['nao_validada']}."]
        if outgoing:
            lines.append('')
    (ROOT / 'docs/DICIONARIO-BRAS1-HISTORICO.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    rh_paths = ['docs/mapeamentos/rh-completo/estatico-20261015/catalogo.json',
                'docs/mapeamentos/rh-completo/estatico-complementar-20261015/catalogo.json']
    combined, references = {}, {}
    for path in rh_paths:
        catalog = read(path)
        for key, value in catalog['formularios'].items():
            if key in combined:
                value = {**value, 'origens': sorted(set(value['origens']) | set(combined[key]['origens']))}
            combined[key] = value
            references[key] = str(Path(path).parent.relative_to('docs/mapeamentos/rh-completo') / value['mapa']).replace('\\', '/')
    rh = ['# Índice ampliado do RH', '',
          'Recursos estáticos de EXE/BPL/DLL da pasta rhsis, incluindo bibliotecas sem prefixo RH.',
          'Não comprova telas disponíveis, regras ou vínculo exclusivo de uma biblioteca a Frequência.', '',
          f"{len(combined)} estruturas distintas; {sum(v['componentes'] for v in combined.values())} componentes declarados.", '']
    rh += table(['Classe', 'Legenda', 'Componentes', 'Origens'],
                [[f"[{v['classe']}]({references[k]})", v['caption'], v['componentes'], ', '.join(v['origens'])]
                 for k, v in combined.items()])
    (ROOT / 'docs/mapeamentos/rh-completo/INDICE-AMPLIADO.md').write_text('\n'.join(rh) + '\n', encoding='utf-8')
    access = read('docs/mapeamentos/acessus-completo/estatico-20261015-ampliado/catalogo.json')
    sql = read('reports/levantamento-20261015/pistas-sql-integracao.json')
    sql_doc = ['# Trechos SQL estáticos da integração', '',
               'Consultas encontradas nos arquivos instalados; não executadas. Literais textuais foram omitidos.',
               'Ter um trecho no executável não comprova que ele foi acionado ou quais parâmetros recebeu.', '']
    for source in sql['arquivos']:
        sql_doc += ['## ' + source['arquivo'], '', 'SHA-256: `' + source['sha256'] + '`', '']
        for entry in source['trechos']:
            sql_doc += [f"Offset {entry['offset']}; codificação {entry['codificacao']}; cortado: {entry['cortado']}.", '']
            if entry['flag_geraafastamento']:
                sql_doc += ['Flag GERAAFASTAMENTO observada: ' + ', '.join(entry['flag_geraafastamento']) + '.', '']
            if entry['prefixos_IdFreq_like']:
                sql_doc += ['Padrões LIKE de IdFreq observados: `' + '`, `'.join(entry['prefixos_IdFreq_like']) + '`.', '']
            sql_doc += ['```sql', entry['trecho_sanitizado'], '```', '']
    (ROOT / 'docs/PISTAS-SQL-INTEGRACAO.md').write_text('\n'.join(sql_doc), encoding='utf-8')
    summary = {'rh_arquivos': sum(len(read(p)['arquivos']) for p in rh_paths),
               'rh_estruturas_distintas': len(combined), 'rh_componentes': sum(v['componentes'] for v in combined.values()),
               'acessus_arquivos': len(access['modulos']), 'acessus_estruturas_distintas': len(access['formularios_unicos']),
               'acessus_componentes': sum(v['componentes'] for v in access['formularios_unicos'].values()),
               'sql_historico_objetos_por_tipo': dict(Counter(r['tipo'] for r in schema['objetos'])),
               'sql_historico_indices_distintos': len(indexes), 'sql_historico_chaves_estrangeiras': len(fks),
               'trechos_sql_estaticos': sum(len(r['trechos']) for r in sql['arquivos']),
               'sql_historico_data': schema['observado_em']}
    (ROOT / 'reports/levantamento-20261015/resumo-consolidado.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=True))


if __name__ == '__main__':
    main()
