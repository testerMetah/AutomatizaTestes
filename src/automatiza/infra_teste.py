"""Primitivas da infraestrutura de testes, sem efeitos ao importar o módulo.

O banco de teste deve ser declarado separadamente da conexão SQL normal.
Este módulo não abre conexão, altera serviço nem grava no banco por conta própria.
"""

import os
import time
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TestTarget:
    server: str
    database: str

    @classmethod
    def from_config(cls, path=None):
        path = Path(path) if path else Path(__file__).resolve().parents[2] / 'config' / 'ambiente-teste.json'
        target = json.loads(path.read_text(encoding='utf-8'))['sql_destino']
        server, database = target['servidor'].strip(), target['banco'].strip()
        if not server or not database:
            raise ValueError('Servidor e banco de teste devem estar preenchidos em config/ambiente-teste.json.')
        return cls(server, database)

    @classmethod
    def from_environment(cls, environ=None):
        values = os.environ if environ is None else environ
        server = values.get('TEST_SQL_SERVER', '').strip()
        database = values.get('TEST_SQL_DATABASE', '').strip()
        if not server or not database:
            raise ValueError('Defina TEST_SQL_SERVER e TEST_SQL_DATABASE para habilitar operações de teste.')
        return cls(server, database)

    def assert_matches(self, settings, db=None):
        """Confere configuração e, quando fornecido, o banco real da conexão."""
        if (settings.sql_server.strip().casefold() != self.server.casefold()
                or settings.sql_database.strip().casefold() != self.database.casefold()):
            raise ValueError('A conexão SQL configurada não corresponde ao banco de teste declarado.')
        if db is not None and db.assert_database().casefold() != self.database.casefold():
            raise ValueError('A conexão SQL real não está no banco de teste declarado.')


def wait_until(predicate, *, timeout, interval=0.2, description='condição', clock=None, sleep=None):
    """Consulta uma condição até ela retornar valor verdadeiro ou atingir o prazo."""
    if timeout <= 0 or interval <= 0:
        raise ValueError('timeout e interval devem ser positivos.')
    clock = clock or time.monotonic
    sleep = sleep or time.sleep
    deadline = clock() + timeout
    while True:
        result = predicate()
        if result:
            return result
        remaining = deadline - clock()
        if remaining <= 0:
            raise TimeoutError(f'Tempo esgotado ao esperar {description} ({timeout}s).')
        sleep(min(interval, remaining))


class TestServiceController:
    """Controla somente o serviço explicitamente declarado para o banco de teste."""

    STOPPED = 1
    RUNNING = 4

    def __init__(self, *, settings, db, target, service_name, adapter=None, config_path=None):
        if not service_name or not service_name.strip():
            raise ValueError('Informe o nome do serviço de teste explicitamente.')
        self.settings = settings
        self.db = db
        self.target = target
        self.service_name = service_name.strip()
        self.adapter = adapter
        self.config_path = config_path

    def _adapter(self):
        if self.adapter is None:
            import win32serviceutil
            self.adapter = win32serviceutil
        return self.adapter

    def _guard(self):
        self.target.assert_matches(self.settings, self.db)
        path = Path(self.config_path) if self.config_path else Path(__file__).resolve().parents[2] / 'config' / 'ambiente-teste.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        if self.target != TestTarget.from_config(path):
            raise ValueError('O destino informado não corresponde ao banco de teste do projeto.')
        allowed = {item['nome_windows'].casefold() for item in data['servicos'].values()
                   if isinstance(item.get('nome_windows'), str) and item['nome_windows']}
        if self.service_name.casefold() not in allowed:
            raise ValueError('O serviço não está confirmado em config/ambiente-teste.json.')

    def status(self):
        self._guard()
        return self._adapter().QueryServiceStatus(self.service_name)[1]

    def _require_control_authorization(self):
        approved = os.environ.get('TEST_SERVICE_CONTROL_APPROVED', '').strip()
        if approved.casefold() != self.service_name.casefold():
            raise PermissionError('Controle do serviço exige autorização explícita para este nome interno.')

    def start(self, *, timeout=30):
        self._require_control_authorization()
        state = self.status()
        if state != self.RUNNING:
            if state != self.STOPPED:
                raise RuntimeError(f'Serviço em estado inesperado antes de iniciar: {state}.')
            self._adapter().StartService(self.service_name)
        wait_until(lambda: self.status() == self.RUNNING, timeout=timeout,
                   description=f'serviço {self.service_name} iniciar')

    def stop(self, *, timeout=30):
        self._require_control_authorization()
        state = self.status()
        if state != self.STOPPED:
            if state != self.RUNNING:
                raise RuntimeError(f'Serviço em estado inesperado antes de parar: {state}.')
            self._adapter().StopService(self.service_name)
        wait_until(lambda: self.status() == self.STOPPED, timeout=timeout,
                   description=f'serviço {self.service_name} parar')

    def restart(self, *, timeout=30):
        self.stop(timeout=timeout)
        self.start(timeout=timeout)
