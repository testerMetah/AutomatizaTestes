"""Retomada local via protocolo oficial do Codex; somente biblioteca padrão.

O proxy oficial transporta WebSocket sobre o socket local do daemon. Não abre
portas TCP, não lê auth.json e não altera cota, conta, modelo ou permissões.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import queue
import secrets
import struct
import subprocess
import threading
import time


class RpcError(RuntimeError):
    def __init__(self, error):
        self.code = error.get('code')
        self.detail = error
        # Não persistir a mensagem bruta: ela pode carregar entradas do usuário.
        super().__init__('RPC retornou código ' + str(self.code))


class LocalRpc:
    """WebSocket RFC6455, limitado ao proxy local do executável oficial."""
    def __init__(self, executable, *, timeout=30):
        self.timeout = timeout
        self.messages = queue.Queue()
        self.deferred = []
        self.sequence = 0
        self.lock = threading.Lock()
        self.ready = threading.Event()
        self.failure = None
        self.process = subprocess.Popen([str(executable), 'app-server', 'proxy'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0), bufsize=0)
        self.key = base64.b64encode(secrets.token_bytes(16)).decode('ascii')
        handshake = ('GET / HTTP/1.1\r\nHost: localhost\r\nUpgrade: websocket\r\n'
            'Connection: Upgrade\r\nSec-WebSocket-Key: ' + self.key + '\r\n'
            'Sec-WebSocket-Version: 13\r\n\r\n')
        self.process.stdin.write(handshake.encode('ascii'))
        threading.Thread(target=self._read, daemon=True).start()
        if not self.ready.wait(timeout) or self.failure:
            self.close()
            raise ConnectionError('Não foi possível conectar ao daemon local do Codex.')
        self.call('initialize', {'clientInfo': {'name': 'codex_auto_resume_local',
                  'version': '1.0.0'}, 'capabilities': {'experimentalApi': True}})
        self.send({'method': 'initialized', 'params': {}})

    def _exact(self, count):
        result = bytearray()
        while len(result) < count:
            chunk = self.process.stdout.read(count - len(result))
            if not chunk:
                raise EOFError('Proxy local encerrou a conexão.')
            result.extend(chunk)
        return bytes(result)

    def _read(self):
        try:
            headers = bytearray()
            while not headers.endswith(b'\r\n\r\n'):
                if len(headers) > 16384:
                    raise ValueError('Handshake excedeu o limite.')
                headers.extend(self._exact(1))
            lines = headers.decode('ascii').split('\r\n')
            fields = {k.lower().strip(): v.strip() for line in lines[1:] if ':' in line
                      for k, v in [line.split(':', 1)]}
            expected = base64.b64encode(hashlib.sha1((self.key +
                '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').encode('ascii')).digest()).decode('ascii')
            if not lines[0].startswith('HTTP/1.1 101 ') or fields.get('sec-websocket-accept') != expected:
                raise ConnectionError('Handshake WebSocket local inválido.')
            self.ready.set()
            fragments = bytearray()
            text_message = False
            while True:
                first, second = self._exact(2)
                if first & 0x70 or second & 0x80:
                    raise ValueError('Frame inesperado no protocolo local.')
                final, opcode = bool(first & 0x80), first & 0x0f
                size = second & 0x7f
                if size == 126:
                    size = struct.unpack('!H', self._exact(2))[0]
                elif size == 127:
                    size = struct.unpack('!Q', self._exact(8))[0]
                if size > 32 * 1024 * 1024 or len(fragments) + size > 32 * 1024 * 1024:
                    raise ValueError('Mensagem excedeu o limite local.')
                payload = self._exact(size)
                if opcode == 8:
                    raise EOFError('Servidor encerrou a conexão.')
                if opcode == 9:
                    self._frame(payload, opcode=10)
                    continue
                if opcode == 10:
                    continue
                if opcode == 1:
                    if fragments:
                        raise ValueError('Sequência de frames inválida.')
                    text_message = True
                elif opcode != 0 or not text_message:
                    raise ValueError('Tipo de frame não suportado.')
                fragments.extend(payload)
                if final:
                    self.messages.put(json.loads(fragments.decode('utf-8')))
                    fragments.clear()
                    text_message = False
        except Exception as exc:
            self.failure = type(exc).__name__
            self.ready.set()
            self.messages.put({'_connection_failed': self.failure})

    def _frame(self, payload, opcode=1):
        mask = secrets.token_bytes(4)
        size = len(payload)
        header = bytes([0x80 | opcode, 0x80 | min(size, 126)])
        if size >= 65536:
            header = bytes([0x80 | opcode, 0xff]) + struct.pack('!Q', size)
        elif size >= 126:
            header += struct.pack('!H', size)
        encoded = bytes(value ^ mask[i % 4] for i, value in enumerate(payload))
        with self.lock:
            self.process.stdin.write(header + mask + encoded)

    def send(self, message):
        self._frame(json.dumps(message, ensure_ascii=False).encode('utf-8'))

    def receive(self, timeout=None):
        msg = self.messages.get(timeout=self.timeout if timeout is None else timeout)
        if '_connection_failed' in msg:
            raise ConnectionError('Proxy local desconectado: ' + msg['_connection_failed'])
        return msg

    def call(self, method, params=None):
        self.sequence += 1
        request_id = self.sequence
        self.send({'id': request_id, 'method': method, 'params': params or {}})
        deadline = time.monotonic() + self.timeout
        while True:
            msg = self.receive(max(.01, deadline - time.monotonic()))
            if msg.get('id') == request_id and 'method' not in msg:
                if 'error' in msg:
                    raise RpcError(msg['error'])
                return msg.get('result', {})
            # Não reter deltas da conversa nem saídas de ferramentas em memória
            # indefinidamente; somente metadados de fim/solicitação são relevantes.
            if msg.get('method') == 'turn/completed' or ('method' in msg and 'id' in msg):
                self.deferred.append(msg)
            if time.monotonic() >= deadline:
                raise TimeoutError('Prazo da chamada local excedido.')

    def close(self):
        if self.process.poll() is None:
            self.process.terminate()  # Encerra somente este proxy, nunca o daemon.
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()


def probe(executable, thread_id):
    rpc = LocalRpc(executable)
    try:
        limits = rpc.call('account/rateLimits/read')
        thread = rpc.call('thread/read', {'threadId': thread_id})['thread']
        turns = rpc.call('thread/turns/list', {'threadId': thread_id, 'limit': 2, 'itemsView': 'notLoaded'})['data']
        return {'thread': {k: thread.get(k) for k in ('id', 'cwd', 'status')},
                'turns': [{k: t.get(k) for k in ('id', 'status', 'error')} for t in turns],
                'rateLimits': limits.get('rateLimits'),
                'rateLimitsByLimitId': limits.get('rateLimitsByLimitId')}
    finally:
        rpc.close()


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp-' + secrets.token_hex(6))
    with temporary.open('w', encoding='utf-8') as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2))
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def is_usage_limit(error):
    if not error:
        return False
    if isinstance(error, dict):
        # Classificação oficial, não a presença genérica da palavra "token".
        info = error.get('codexErrorInfo')
        values = [info] if isinstance(info, str) else list(info or {})
        values += [error.get('code')]
        return any(str(v).replace('_', '').casefold() in
                   {'usagelimitexceeded', 'usagelimitreached'} for v in values)
    return False


def quota_wait(result, now):
    """Retorna segundos até reconsultar; None significa leitura inconclusiva."""
    buckets = result.get('rateLimitsByLimitId') or {}
    bucket = buckets.get('codex') or result.get('rateLimits')
    if not isinstance(bucket, dict):
        return None
    resets = []
    windows = 0
    for key in ('primary', 'secondary'):
        window = bucket.get(key)
        if isinstance(window, dict):
            windows += 1
            if window.get('usedPercent', 100) >= 100:
                resets.append(max(now + 60, window.get('resetsAt') or now + 900))
    individual = bucket.get('individualLimit')
    if isinstance(individual, dict) and individual.get('usedPercent', 100) >= 100:
        resets.append(max(now + 60, individual.get('resetsAt') or now + 900))
    if resets:
        return max(resets) - now + 30
    if bucket.get('spendControlReached') or bucket.get('rateLimitReachedType'):
        return 900  # Não consumir créditos/reset, nem supor que um bloqueio sumiu.
    return 0 if windows else None


def desktop_available():
    if os.name != 'nt':
        return False
    import ctypes
    from ctypes import wintypes
    user = ctypes.WinDLL('user32', use_last_error=True)
    user.OpenInputDesktop.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    user.OpenInputDesktop.restype = wintypes.HANDLE
    user.GetThreadDesktop.argtypes = [wintypes.DWORD]
    user.GetThreadDesktop.restype = wintypes.HANDLE
    user.GetUserObjectInformationW.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p,
                                             wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
    user.CloseDesktop.argtypes = [wintypes.HANDLE]
    def name(handle):
        buf, size = ctypes.create_unicode_buffer(256), wintypes.DWORD()
        return buf.value if user.GetUserObjectInformationW(handle, 2, buf, ctypes.sizeof(buf), ctypes.byref(size)) else None
    handle = user.OpenInputDesktop(0, False, 1)
    if not handle:
        return False
    try:
        active = name(handle)
        current = name(user.GetThreadDesktop(ctypes.windll.kernel32.GetCurrentThreadId()))
        return active == current == 'Default'
    finally:
        user.CloseDesktop(handle)


RESULT_SCHEMA = {'type': 'object', 'properties': {
    'status': {'type': 'string', 'enum': ['concluido', 'continuar', 'precisa_usuario']},
    'resumo': {'type': 'string'}}, 'required': ['status', 'resumo'], 'additionalProperties': False}


def continuation_text(recovery=False):
    reason = 'recuperação após reinicialização' if recovery else 'renovação real da cota'
    return ('Retomada automática autorizada pelo usuário (' + reason + '). Continue a tarefa vigente '
        'nesta MESMA conversa, preservando histórico, restrições, arquivos e alterações. '
        'Primeiro confira o último trabalho, processos ainda ativos e efeitos de operações '
        'parcialmente executadas; não repita gravações, importações ou atualizações cegamente. '
        'Leia CONTEXTO-PARA-CONTINUAR.md e documentos atuais relevantes quando necessário. '
        'Não troque conta, modelo, autenticação ou permissões e não tente contornar limites. '
        'Não invente credenciais, confirmações ou dados de negócio. Não reative tarefa cancelada '
        'ou substituída por pedido mais recente. Trabalhe até concluir ou encontrar dependência '
        'real do usuário. No JSON final, status=concluido apenas quando a tarefa vigente estiver '
        'realmente concluída; continuar se ainda houver trabalho autônomo útil; precisa_usuario '
        'quando faltar informação, autenticação ou aprovação indispensável. Atualize os arquivos '
        'de continuidade antes de encerrar. Nunca declare testes ou configurações não realizados.')


class Supervisor:
    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.folder = self.config_path.parent
        self.state_path = self.folder / 'state.json'
        self.state = json.loads(self.state_path.read_text(encoding='utf-8')) if self.state_path.exists() else {}

    def save(self, status, **details):
        # Lista permitida: não grava respostas brutas, prompts, tokens ou credenciais.
        self.state.update(status=status, checked_at=time.time(), **details)
        atomic_json(self.state_path, self.state)
        with (self.folder / 'events.jsonl').open('a', encoding='utf-8') as stream:
            stream.write(json.dumps({'at': time.time(), 'status': status,
                **{k: v for k, v in details.items() if k in {'turn_id', 'next_check_at', 'error_type'}}}) + '\n')

    def _result(self, turn):
        for item in reversed(turn.get('items') or []):
            if item.get('type') == 'agentMessage':
                try:
                    value = json.loads(item.get('text', ''))
                    if value.get('status') in {'concluido', 'continuar', 'precisa_usuario'}:
                        return value['status']
                except (ValueError, AttributeError):
                    pass
        return 'precisa_usuario'  # Nunca continuar indefinidamente por resultado ambíguo.

    def tick(self, *, observe_only=False):
        config = json.loads(self.config_path.read_text(encoding='utf-8'))
        if not config.get('enabled'):
            self.save('desativado')
            return False
        if self.state.get('status') in {'concluido', 'precisa_usuario', 'interrompido_usuario'}:
            return False
        if self.state.get('next_check_at', 0) > time.time():
            return True
        rpc = LocalRpc(config['codex_path'])
        try:
            tid = config['thread_id']
            thread = rpc.call('thread/read', {'threadId': tid})['thread']
            if Path(thread['cwd']).resolve() != Path(config['workspace']).resolve():
                self.save('precisa_usuario', error_type='WorkspaceDivergente')
                return False
            runtime = (thread.get('status') or {}).get('type')
            turns = rpc.call('thread/turns/list', {'threadId': tid, 'limit': 1, 'itemsView': 'notLoaded'})['data']
            if not turns:
                self.save('aguardando_trabalho')
                return True
            turn = turns[0]
            own = self.state.get('owned_turn') == turn['id']
            recovery = own and runtime == 'notLoaded' and turn['status'] in {'inProgress', 'interrupted'}
            if runtime == 'active' or (turn['status'] == 'inProgress' and not recovery):
                self.save('observando_execucao', turn_id=turn['id'])
                return True
            continuing = False
            if own and turn['status'] == 'completed':
                full = rpc.call('thread/turns/list', {'threadId': tid, 'limit': 1, 'itemsView': 'full'})['data'][0]
                status = self._result(full)
                if status != 'continuar':
                    self.save(status, owned_turn=None)
                    return False
                continuing = True
            elif own and turn['status'] == 'interrupted' and not recovery:
                self.save('interrompido_usuario', owned_turn=None)
                return False
            elif own and turn['status'] == 'failed' and not is_usage_limit(turn.get('error')):
                self.save('precisa_usuario', error_type='FalhaNaoRelacionadaACota')
                return False
            exhausted = turn['status'] == 'failed' and is_usage_limit(turn.get('error'))
            if turn['status'] == 'failed' and not exhausted:
                self.save('precisa_usuario', error_type='FalhaNaoRelacionadaACota')
                return False
            if not (exhausted or continuing or recovery):
                self.save('armado_sem_falha_de_cota', owned_turn=None)
                return True
            earliest = self.state.get('last_resume_at', 0) + config.get('minimum_retry_seconds', 300)
            if exhausted and earliest > time.time():
                self.save('aguardando_cota', next_check_at=earliest, turn_id=turn['id'])
                return True
            wait = quota_wait(rpc.call('account/rateLimits/read'), time.time())
            if wait is None or wait > 0:
                self.save('aguardando_cota', next_check_at=time.time() + (900 if wait is None else wait),
                          turn_id=turn['id'])
                return True
            if not desktop_available():
                self.save('aguardando_sessao_desbloqueada', next_check_at=time.time() + 60)
                return True
            if observe_only:
                self.save('checagem_sem_geracao', turn_id=turn['id'])
                return True
            # Retoma explicitamente o ID; não usa --last, fork, resets ou overrides.
            rpc.call('thread/resume', {'threadId': tid, 'excludeTurns': True})
            latest = rpc.call('thread/turns/list', {'threadId': tid, 'limit': 1, 'itemsView': 'notLoaded'})['data'][0]
            if latest['id'] != turn['id'] or latest['status'] == 'inProgress':
                self.save('observando_execucao', next_check_at=0)
                return True
            started = rpc.call('turn/start', {'threadId': tid,
                'input': [{'type': 'text', 'text': continuation_text(recovery)}],
                'outputSchema': RESULT_SCHEMA})['turn']
            self.save('retomado', owned_turn=started['id'], turn_id=started['id'], next_check_at=0,
                      last_resume_at=time.time())
            # Manter a conexão viva durante o turno criado por este supervisor.
            while True:
                refreshed = json.loads(self.config_path.read_text(encoding='utf-8'))
                if not refreshed.get('enabled'):
                    self.save('desativado')
                    return False
                try:
                    msg = rpc.deferred.pop(0) if rpc.deferred else rpc.receive(timeout=10)
                except queue.Empty:
                    continue
                params = msg.get('params') or {}
                if 'method' in msg and 'id' in msg:
                    # Não fabricar respostas a login, aprovação ou ferramentas dinâmicas.
                    self.save('precisa_usuario', error_type='SolicitacaoInterativaDoServidor')
                    return False
                if msg.get('method') == 'turn/completed' and params.get('turn', {}).get('id') == started['id']:
                    self.save('verificando_resultado', next_check_at=0)
                    return True
        finally:
            rpc.close()

    def run(self):
        import msvcrt
        self.folder.mkdir(parents=True, exist_ok=True)
        lock = (self.folder / 'supervisor.lock').open('a+b')
        try:
            lock.seek(0)
            if lock.read(1) == b'':
                lock.write(b'0'); lock.flush()
            lock.seek(0)
            try:
                msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError:
                return  # Uma única instância; sem tocar nos locks do Codex.
            while True:
                try:
                    if not self.tick():
                        return
                except Exception as exc:
                    if isinstance(exc, RpcError) and any(word in str(exc.detail).lower()
                            for word in ('unauthorized', 'not logged', 'authentication', '401')):
                        self.save('precisa_usuario', error_type='AutenticacaoNecessaria')
                        return
                    self.save('erro_conexao_local', error_type=type(exc).__name__, next_check_at=time.time() + 300)
                    config = json.loads(self.config_path.read_text(encoding='utf-8'))
                    # Apenas iniciar o daemon oficial existente, nunca atualizar ou reiniciá-lo.
                    subprocess.run([config['codex_path'], 'app-server', 'daemon', 'start'],
                        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                        creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0), timeout=45)
                # Espera curta interrompível por desativação; sem chamadas de geração.
                for _ in range(6):
                    time.sleep(10)
                    if not json.loads(self.config_path.read_text(encoding='utf-8')).get('enabled'):
                        self.save('desativado')
                        return
        finally:
            lock.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['probe', 'watch', 'check', 'disable', 'arm'])
    parser.add_argument('--codex', type=Path)
    parser.add_argument('--thread')
    parser.add_argument('--config', type=Path)
    args = parser.parse_args()
    if args.action == 'probe':
        if not args.codex or not args.thread:
            parser.error('probe exige --codex e --thread.')
        print(json.dumps(probe(args.codex, args.thread), ensure_ascii=False, indent=2))
    else:
        if not args.config:
            parser.error('Informe --config.')
        if args.action in {'disable', 'arm'}:
            config = json.loads(args.config.read_text(encoding='utf-8'))
            config['enabled'] = args.action == 'arm'
            atomic_json(args.config, config)
            if args.action == 'arm':
                state_path = args.config.parent / 'state.json'
                state = json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else {}
                state.update(status='armado', next_check_at=0)
                atomic_json(state_path, state)
        elif args.action == 'watch':
            Supervisor(args.config).run()
        else:
            config = json.loads(args.config.read_text(encoding='utf-8'))
            print(json.dumps({'somente_leitura': True, **probe(config['codex_path'], config['thread_id'])},
                             ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
