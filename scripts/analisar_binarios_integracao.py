"""Lê imports PE e nomes de tabelas em textos embutidos, sem executar binários.

Não exporta strings completas: só dependências e identificadores de tabelas.
Referências textuais são pistas, não confirmação de consultas executadas.
"""
import hashlib
import json
import re
import struct
from pathlib import Path


def imports(data):
    if data[:2] != b'MZ' or len(data) < 64:
        return []
    pe = struct.unpack_from('<I', data, 60)[0]
    if pe + 24 > len(data) or data[pe:pe+4] != b'PE\0\0':
        return []
    count = struct.unpack_from('<H', data, pe+6)[0]
    opt_size = struct.unpack_from('<H', data, pe+20)[0]
    opt = pe+24
    magic = struct.unpack_from('<H', data, opt)[0]
    directory = opt + (96 if magic == 0x10b else 112 if magic == 0x20b else 0)
    if directory == opt:
        return []
    rva, size = struct.unpack_from('<II', data, directory+8)
    sections = []
    for index in range(count):
        offset = opt+opt_size+40*index
        virtual_size, address, raw_size, pointer = struct.unpack_from('<IIII', data, offset+8)
        sections.append((address, max(virtual_size, raw_size), pointer))

    def file_offset(address):
        for start, length, pointer in sections:
            if start <= address < start+length:
                offset = pointer+address-start
                if offset < len(data):
                    return offset
        raise ValueError('RVA de importação fora das seções')

    if not rva or not size:
        return []
    result = []
    start = file_offset(rva)
    for index in range(min(size//20, 4096)):
        entry = struct.unpack_from('<IIIII', data, start+20*index)
        if not any(entry):
            break
        offset = file_offset(entry[3])
        end = data.find(b'\0', offset, offset+260)
        if end < 0:
            raise ValueError('Nome de dependência sem terminador')
        name = data[offset:end].decode('ascii')
        if re.fullmatch(r'[\w.\- ]+\.(?:dll|bpl)', name, flags=re.I):
            result.append(name)
    return sorted(set(result), key=str.casefold)


def main():
    root = Path(__file__).resolve().parents[1]
    output = root / 'reports/levantamento-20261015/binarios-integracao.json'
    schema = json.loads((root / 'reports/banco/20261015-095741/inventario.json').read_text(encoding='utf-8'))
    known = {o['objeto'].casefold(): o['objeto'] for o in schema['objetos'] if o['tipo'] in ('USER_TABLE', 'VIEW')}
    files = [Path(r'C:\acesso') / name for name in (
        'Acessus.Modulo.exe', 'Acessus.exe', 'AcessusSync.exe', 'AcessusSyncImportacao.exe',
        'AcessusSyncService.exe', 'MetahConnect.exe', 'MetahConnectService.exe')]
    files += [Path(r'C:\meta\rhsis') / name for name in ('rh.exe', 'RHID.exe', 'RHPA.exe', 'RHLogin.bpl', 'RHForms.bpl', 'RHForms2.bpl')]
    result = {'metodo': __doc__, 'fonte_nomes_destino': 'Inventário histórico bras1 de 15/10/2026', 'arquivos': []}
    for path in files:
        record = {'arquivo': str(path)}
        result['arquivos'].append(record)
        try:
            data = path.read_bytes()
            record['sha256'] = hashlib.sha256(data).hexdigest()
            record['dependencias_pe'] = imports(data)
            texts = [m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{8,}', data)]
            texts += [m.group().decode('utf-16-le') for m in re.finditer(rb'(?:[\x20-\x7e]\x00){8,}', data)]
            destination, source = set(), set()
            for text in texts:
                # Apenas nomes após palavras SQL; nunca exportar o SQL ou literais.
                for match in re.finditer(r'\b(?:FROM|JOIN|INTO|UPDATE)\s+(?:\[?\w+\]?\.)?\[?([A-Za-z_]\w{1,100})', text, flags=re.I):
                    table = match.group(1)
                    if table.casefold() in known:
                        destination.add(known[table.casefold()])
                    if re.fullmatch(r'RH[A-Z0-9_]{2,100}', table):
                        source.add(table)
            record['tabelas_destino_textualmente_referenciadas'] = sorted(destination)
            record['identificadores_RH_candidatos'] = sorted(source)
        except Exception as exc:
            record['erro'] = type(exc).__name__
        print(json.dumps({'arquivo': path.name, 'dependencias': len(record.get('dependencias_pe', [])),
                          'tabelas_destino': len(record.get('tabelas_destino_textualmente_referenciadas', [])),
                          'identificadores_RH': len(record.get('identificadores_RH_candidatos', []))}), flush=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
