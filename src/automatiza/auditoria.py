"""Histórico por ação com horários UTC/local, duração e evidências locais."""
import hashlib
import json
import os
import re
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from uuid import uuid4


class AuditRun:
    def __init__(self, base, title, *, context=None, secrets=(), capture=None):
        self.folder = Path(base) / (datetime.now().strftime('%Y%m%d-%H%M%S') + '-' + uuid4().hex[:8])
        self.folder.mkdir(parents=True, exist_ok=False)
        self.secrets = tuple(s for s in secrets if isinstance(s, str) and s)
        self.capture = capture
        self.events = []
        self.summary = {'titulo': title, 'estado': 'EM_EXECUCAO', 'contexto': self.clean(context or {}),
                        'inicio': self.stamp(), 'fim': None, 'etapas': 0, 'falhas': 0}
        self.event('INICIO', title)

    @staticmethod
    def stamp():
        value = datetime.now(timezone.utc)
        return {'utc': value.isoformat(), 'local': value.astimezone().isoformat()}

    def clean(self, value):
        if isinstance(value, dict):
            return {str(k): '[omitido]' if re.search(r'password|senha|secret|token|connection.?string', str(k), re.I)
                    else self.clean(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [self.clean(v) for v in value]
        if isinstance(value, str):
            for secret in sorted(self.secrets, key=len, reverse=True):
                value = value.replace(secret, '[omitido]')
            return value
        return value

    def event(self, kind, description, **details):
        entry = self.clean({'sequencia': len(self.events) + 1, 'tipo': kind,
                            'descricao': description, 'horario': self.stamp(), **details})
        # Persistir antes da próxima ação; uma interrupção não apaga o que ocorreu.
        with (self.folder / 'eventos.jsonl').open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(entry, ensure_ascii=False, default=str) + '\n')
            stream.flush()
            os.fsync(stream.fileno())
        self.events.append(entry)
        self.render()
        return entry

    def evidence(self, step, stage):
        if self.capture is None:
            return None
        path = self.folder / 'capturas' / f'{step:04d}-{stage}.png'
        path.parent.mkdir(exist_ok=True)
        try:
            if self.capture(path) is False:
                self.event('EVIDENCIA_OMITIDA', 'Captura omitida por privacidade ou janela indisponível.', etapa=step)
                return None
            if not path.is_file():
                raise RuntimeError('O capturador não produziu arquivo')
            return path.relative_to(self.folder).as_posix()
        except Exception as exc:
            self.event('FALHA_EVIDENCIA', 'Não foi possível capturar a janela.', etapa=step, erro_tipo=type(exc).__name__)
            return None

    @contextmanager
    def step(self, description, *, action, details=None):
        self.summary['etapas'] += 1
        number = self.summary['etapas']
        # Registrar a intenção antes de qualquer interação.
        self.event('ETAPA_INICIO', description, etapa=number, acao=action, detalhes=details or {})
        before = self.evidence(number, 'antes')
        start = time.perf_counter()
        try:
            yield number
        except BaseException as exc:
            self.summary['falhas'] += 1
            after = self.evidence(number, 'falha')
            self.event('ETAPA_FALHA', description, etapa=number, acao=action,
                       duracao_ms=round((time.perf_counter()-start)*1000, 3),
                       erro_tipo=type(exc).__name__, erro=str(exc)[:4000], antes=before, depois=after)
            raise
        else:
            after = self.evidence(number, 'depois')
            self.event('ETAPA_FIM', description, etapa=number, acao=action,
                       duracao_ms=round((time.perf_counter()-start)*1000, 3), antes=before, depois=after)

    def finish(self, state):
        if self.summary['falhas'] and state in {'PASSOU', 'INSPECAO_CONCLUIDA'}:
            raise ValueError('Execução com falhas não pode ser concluída como sucesso.')
        self.summary['estado'] = state
        self.summary['fim'] = self.stamp()
        self.event('FIM', state)
        manifest = {}
        for path in sorted(self.folder.rglob('*')):
            if path.is_file() and path.name != 'manifesto-sha256.json':
                manifest[path.relative_to(self.folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        (self.folder / 'manifesto-sha256.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
        return self.folder

    def render(self):
        (self.folder / 'resumo.json').write_text(json.dumps(self.summary, ensure_ascii=False, indent=2, default=str), encoding='utf-8')
        rows = []
        for event in self.events:
            links = ' '.join(f'<a href="{escape(event[key], quote=True)}">{key}</a>' for key in ('antes', 'depois') if event.get(key))
            cells = [str(event['sequencia']), event['horario']['local'], event['horario']['utc'],
                     event['tipo'], event.get('acao', ''), event['descricao'], str(event.get('duracao_ms', ''))]
            rows.append('<tr>' + ''.join('<td>' + escape(c) + '</td>' for c in cells) + '<td>' + links + '</td><td><pre>'
                        + escape(json.dumps({k: v for k, v in event.items() if k not in {'horario', 'descricao'}}, ensure_ascii=False, default=str))
                        + '</pre></td></tr>')
        html = ('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Execução de automação</title>'
                '<style>body{font:15px system-ui;margin:24px;color:#182939}table{border-collapse:collapse;width:100%}'
                'td,th{border:1px solid #ccd;padding:7px;text-align:left;vertical-align:top}pre{white-space:pre-wrap;max-width:34em}</style>'
                '<h1>' + escape(self.summary['titulo']) + '</h1><p>Estado: <strong>' + escape(self.summary['estado']) + '</strong></p>'
                '<p>Cada linha registra uma ação do executor. Não é gravação de todas as atividades do Windows.</p>'
                '<p>Horário local com fuso e UTC; duração medida por relógio monotônico em milissegundos.</p><pre>'
                + escape(json.dumps(self.summary['contexto'], ensure_ascii=False, indent=2, default=str)) + '</pre>'
                '<p><a href="eventos.jsonl">Histórico JSONL</a> · <a href="resumo.json">Resumo JSON</a></p>'
                '<table><tr><th>#</th><th>Data/hora local</th><th>UTC</th><th>Estado</th><th>Ação</th><th>Descrição</th>'
                '<th>ms</th><th>Capturas</th><th>Detalhes</th></tr>' + ''.join(rows) + '</table></html>')
        (self.folder / 'relatorio.html').write_text(html, encoding='utf-8')
