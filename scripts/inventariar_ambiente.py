"""Inventário local de arquivos e chaves de configuração, sem executar sistemas.

Nunca publica valores de credenciais, connection strings, tokens ou licenças.
"""
import argparse
import configparser
import hashlib
import json
import platform
import re
import struct
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path


SAFE_KEYS = {'server', 'servername', 'servidor', 'host', 'hostname', 'database',
             'databasename', 'banco', 'dbname', 'port', 'porta', 'drivername',
             'driver', 'provider', 'dbms', 'instance', 'instancia'}


def safe_value(key, value):
    normalized = re.sub(r'[^a-z]', '', key.lower())
    if normalized in SAFE_KEYS and re.fullmatch(r'[\w .\\:/,\-]{1,160}', value):
        return value
    return None


def config_structure(path):
    result = {'arquivo': path.name, 'chaves': [],
              'politica': 'Valores omitidos, exceto nomes simples de servidor/base/driver/porta.'}
    try:
        raw = path.read_bytes()
        result['sha256'] = hashlib.sha256(raw).hexdigest()
        text = raw.decode('utf-8-sig') if not raw.startswith(b'\xff\xfe') else raw.decode('utf-16')
    except UnicodeError:
        text = raw.decode('cp1252', errors='replace')
    except OSError as exc:
        result['erro'] = type(exc).__name__
        return result
    if path.suffix.lower() == '.config':
        try:
            root = ET.fromstring(text)
            for node in root.iter():
                tag = node.tag.split('}')[-1]
                key = node.attrib.get('key', node.attrib.get('name', tag))
                # Nomes arbitrários de conexões também não são publicados.
                entry = {'tipo': tag, 'atributos': sorted(node.attrib)}
                if re.fullmatch(r'[\w .:/\\\-]{1,160}', key):
                    entry['chave'] = key
                value = safe_value(key, node.attrib.get('value', ''))
                if value is not None:
                    entry['valor_nao_secreto'] = value
                result['chaves'].append(entry)
        except ET.ParseError:
            result['erro'] = 'XML não reconhecido; conteúdo não exportado'
    else:
        parser = configparser.ConfigParser(interpolation=None, strict=False, allow_no_value=True)
        try:
            parser.read_string(text)
            for section in parser.sections():
                for key, value in parser.items(section):
                    entry = {'secao': section, 'chave': key}
                    value = safe_value(key, value or '')
                    if value is not None:
                        entry['valor_nao_secreto'] = value
                    result['chaves'].append(entry)
        except configparser.Error:
            result['erro'] = 'INI não reconhecido; conteúdo não exportado'
    return result


def binary_info(path):
    record = {'arquivo': path.name, 'bytes': path.stat().st_size,
              'modificado_em': datetime.fromtimestamp(path.stat().st_mtime).astimezone().isoformat()}
    data = path.read_bytes()
    record['sha256'] = hashlib.sha256(data).hexdigest()
    if len(data) >= 64 and data[:2] == b'MZ':
        offset = struct.unpack_from('<I', data, 60)[0]
        if offset + 6 <= len(data) and data[offset:offset+4] == b'PE\0\0':
            machine = struct.unpack_from('<H', data, offset+4)[0]
            record['arquitetura'] = {0x14c: 'x86', 0x8664: 'x64', 0xaa64: 'ARM64'}.get(machine, hex(machine))
    try:
        import win32api
        info = win32api.GetFileVersionInfo(str(path), '\\')
        ms, ls = info['FileVersionMS'], info['FileVersionLS']
        record['versao_arquivo'] = '.'.join(map(str, (ms >> 16, ms & 65535, ls >> 16, ls & 65535)))
    except Exception:
        pass
    return record


def inspect(output):
    output.mkdir(parents=True, exist_ok=False)
    result = {'capturado_em': datetime.now().astimezone().isoformat(),
              'plataforma': platform.platform(), 'python_execucao': platform.python_version(),
              'limites': 'Inventário local; arquivos não foram executados. Configurações não foram alteradas.',
              'instalacoes': {}}
    try:
        import pyodbc
        result['drivers_odbc'] = pyodbc.drivers()
    except ImportError:
        result['drivers_odbc'] = []
    for label, folder in {'acessus': Path(r'C:\acesso'), 'rh': Path(r'C:\meta\rhsis')}.items():
        entry = {'pasta': str(folder), 'binarios': [], 'configuracoes': [], 'documentacao_local': []}
        result['instalacoes'][label] = entry
        for path in sorted(folder.iterdir()):
            if not path.is_file():
                continue
            suffix = path.suffix.lower()
            try:
                if suffix in {'.exe', '.bpl'}:
                    entry['binarios'].append(binary_info(path))
                elif suffix in {'.ini', '.config'}:
                    entry['configuracoes'].append(config_structure(path))
                elif suffix in {'.chm', '.hlp', '.pdf', '.txt'}:
                    entry['documentacao_local'].append({'arquivo': path.name, 'bytes': path.stat().st_size})
            except OSError as exc:
                entry.setdefault('falhas', []).append({'arquivo': path.name, 'tipo': type(exc).__name__})
    (output / 'ambiente.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: {'binarios': len(v['binarios']), 'configuracoes': len(v['configuracoes'])}
                      for k, v in result['instalacoes'].items()}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--saida', type=Path, required=True)
    inspect(parser.parse_args().saida)
