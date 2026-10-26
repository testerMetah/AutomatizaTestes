"""Extrai trechos SQL de integração com literais omitidos; nunca executa SQL."""
import hashlib
import json
import re
from pathlib import Path


def redact(text):
    # Troca literais de texto completos e também um literal aberto no fim do trecho.
    text = re.sub(r"'(?:''|[^'])*(?:'|$)", "'<literal omitido>'", text)
    text = re.sub(r'\b0x[0-9A-Fa-f]+\b', '<binario omitido>', text)
    return text


def main():
    result = {'metodo': 'Strings estáticas; literais textuais omitidos; SQL nunca executado.',
              'limites': ['Trechos podem estar incompletos ou não ser usados em execução.',
                          'Não comprova parâmetros efetivos, banco do RH nem regra de integração.'], 'arquivos': []}
    for name in ('Acessus.exe', 'AcessusSync.exe', 'AcessusSyncImportacao.exe', 'AcessusSyncService.exe', 'MetahConnect.exe'):
        path = Path(r'C:\acesso') / name
        data = path.read_bytes()
        entries, seen = [], set()
        for encoding, pattern in [('ascii', rb'[\x09\x0a\x0d\x20-\x7e]{16,}'), ('utf-16-le', rb'(?:[\x09\x0a\x0d\x20-\x7e]\x00){16,}')]:
            for match in re.finditer(pattern, data):
                raw = match.group().decode(encoding)
                if not re.search(r'\b(?:Afastamentos|RHFERIASCEDIDASPA|RHREGOCORRENCIAS)\b', raw, re.I):
                    continue
                start = re.search(r'\b(?:SELECT|INSERT\s+INTO|UPDATE|DELETE\s+FROM)\b', raw, re.I)
                if not start or re.search(r'password|passwd|senha|secret|token|connectionstring', raw, re.I):
                    continue
                safe = redact(raw[start.start():])
                if safe in seen:
                    continue
                seen.add(safe)
                entries.append({'offset': match.start(), 'codificacao': encoding,
                                'prefixos_IdFreq_like': re.findall(r"\bIdFreq\s+(?:NOT\s+)?LIKE\s+'([A-Za-z_%-]{1,16})'", raw, flags=re.I),
                                'flag_geraafastamento': re.findall(r"\bGERAAFASTAMENTO\s*=\s*'([SN])'", raw, flags=re.I),
                                'trecho_sanitizado': safe[:8000], 'cortado': len(safe) > 8000})
        result['arquivos'].append({'arquivo': name, 'sha256': hashlib.sha256(data).hexdigest(), 'trechos': entries})
    output = Path('reports/levantamento-20261015/pistas-sql-integracao.json')
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({r['arquivo']: len(r['trechos']) for r in result['arquivos']}))


if __name__ == '__main__':
    main()
