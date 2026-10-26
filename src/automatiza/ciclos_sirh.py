"""Adaptador real: alterações pela interface RH; SQL somente para conferência."""
import json
import os
import ssl
import time
import urllib.parse
import urllib.request
from dataclasses import replace
from datetime import datetime
from pathlib import Path

from automatiza.ciclos import Blocked
from automatiza.config import Settings
from automatiza.database import SqlServer


def normalized(value):
    return None if value is None else datetime.fromisoformat(str(value)).isoformat(timespec="seconds")


class SirhBackend:
    def __init__(self, config):
        self.config = config
        self.settings = Settings.load()
        self.origin = SqlServer(replace(self.settings, sql_database=config["origem"]))
        self.dest = SqlServer(replace(self.settings, sql_database=config["destino"]))
        self.token = None
        self.ui = None
        self.context = (ssl._create_unverified_context() if config.get("tls_diagnostico_sem_validacao")
                        else ssl.create_default_context())

    def preflight(self):
        self.origin.assert_database()
        self.dest.assert_database()
        from automatiza.perfis import import_destination
        actual = import_destination(Path(self.settings.app_work_dir or "C:/acesso") / "ConexaoConfig.ini")
        # Usa o comparador existente para impedir atuação com importador em outro destino.
        from automatiza.perfis import destinations_match
        if not destinations_match(actual, {"servidor": self.settings.sql_server,
                                           "banco": self.config["destino"]}):
            raise Blocked("Destino do importador diferente do manifesto.")
        if self.dest.scalar("SELECT COUNT(*) FROM Pessoas WHERE Id=? AND IdExportacao=?",
                            (self.config["pessoa"], str(self.config["contrato"]))) != 1:
            raise Blocked("Pessoa de destino não corresponde ao contrato.")
        password = os.environ.get("SIRH_TEST_PASSWORD")
        if not password:
            # Senha do banco Acessus pode estar cifrada. Reutiliza o cofre do Windows.
            import win32cred
            try:
                credential = win32cred.CredRead("AutomatizaTestes/SIRH", win32cred.CRED_TYPE_GENERIC)
            except Exception:
                raise Blocked("Credencial SIRH ausente no cofre Windows e no ambiente.") from None
            email = credential["UserName"]
            password = credential["CredentialBlob"].decode("utf-16le")
        else:
            email = os.environ.get("SIRH_TEST_EMAIL", self.config["email_api"])
        configured = self.dest.query("SELECT url_api FROM DADOS_IMPORTACAO_API WHERE id=1")
        if len(configured) != 1 or configured[0]["url_api"].rstrip("/") != self.config["api"].rstrip("/"):
            raise Blocked("URL configurada no importador difere do manifesto.")
        request = urllib.request.Request(self.config["api"].rstrip("/") + "/login",
            data=json.dumps({"email": email, "senha": password}).encode(),
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(request, context=self.context, timeout=30) as response:
            self.token = json.load(response)["accessToken"]
        with urllib.request.urlopen(self.config["api"].rstrip("/") + "/swagger/v1/swagger.json",
                                    context=self.context, timeout=30) as response:
            routes = list(json.load(response)["paths"])
        self.reservation_routes = [route for route in routes if any(
            word in route.lower() for word in ("reserv", "refeic", "consumo"))]

    def available(self, case):
        if case["tipo"] == "reserva":
            if self.reservation_routes:
                raise Blocked("Rota de reserva encontrada, mas adaptador CRUD/API ainda requer mapeamento.")
            raise Blocked("API instalada sem endpoint de reservas; ciclo CRUD de reserva não iniciado.")
        if case["tipo"] == "ocorrencia" and datetime.fromisoformat(case["inicio"]).time() != datetime.min.time():
            if case["ocorrencia"] != "013" or case["gera_afastamento"]:
                raise Blocked("Fluxo horário de ocorrência exige mapeamento próprio para este código.")
            if any(datetime.fromisoformat(case[key]).time() == datetime.min.time()
                   for key in ("termino", "termino_alterado")):
                raise Blocked("Faixa Horas exige horário explícito nos dois términos.")

    def source(self, case):
        params = [self.config["unidade"], self.config["contrato"], datetime.fromisoformat(case["inicio"])]
        if case["tipo"] == "ferias":
            rows = self.origin.query("""SELECT TERMINOGOZOFERIAS AS fim FROM RHFERIASCEDIDASPA
                WHERE UNIDADE=? AND CONTRATO=? AND INICIOGOZOFERIAS=?""", params)
        elif case["tipo"] == "ocorrencia":
            rows = self.origin.query("""SELECT DATATERMINOOCORRENCIA AS fim FROM RHREGOCORRENCIAS
                WHERE UNIDADE=? AND CONTRATO=? AND DATAINICIOOCORRENCIA=? AND OCORRENCIA=?""",
                params + [case["ocorrencia"]])
        else:
            raise Blocked("Consulta de ciclo reserva depende de endpoint não disponível.")
        if len(rows) > 1:
            raise Blocked("Chave de origem não é única.")
        return normalized(rows[0]["fim"]) if rows else None

    def api_state(self, case):
        holidays = case["tipo"] == "ferias"
        route = "/frequencia/feriasCedidas" if holidays else "/cadastro/registrosOcorrencias"
        query = dict(unidade=self.config["unidade"], contrato=self.config["contrato"])
        matches = []
        previous = None
        for page in range(1, 51):
            query["pagina"] = page
            request = urllib.request.Request(self.config["api"].rstrip("/") + route + "?" +
                urllib.parse.urlencode(query), headers={"Authorization": "Bearer " + self.token})
            with urllib.request.urlopen(request, context=self.context, timeout=30) as response:
                data = json.load(response)
            if not isinstance(data, list):
                raise Blocked("Resposta API fora do formato esperado.")
            if not data:
                break
            signature = json.dumps(data, sort_keys=True)
            if signature == previous:
                raise Blocked("API repetiu página.")
            previous = signature
            for row in data:
                if str(row.get("unidade")) != self.config["unidade"] or row.get("contrato") != self.config["contrato"]:
                    raise Blocked("API ignorou filtro de unidade/contrato.")
                start_key, end_key = (("inicioGozoFerias", "terminoGozoFerias") if holidays
                                      else ("dataInicioOcorrencia", "dataTerminoOcorrencia"))
                if normalized(row.get(start_key)) == case["inicio"] and (
                        holidays or row.get("ocorrencia") == case["ocorrencia"]):
                    matches.append(normalized(row.get(end_key)))
        else:
            raise Blocked("Paginação API excedeu limite.")
        return matches

    def target(self, case):
        days = (datetime.fromisoformat(case["inicio"]) - datetime(1899, 12, 30)).days
        prefix = "AFAST_F" if case["tipo"] == "ferias" else "AFAST_O"
        key = f'{prefix}_{self.config["unidade"]}_{self.config["contrato"]}_'
        if case["tipo"] == "ocorrencia":
            key += case["ocorrencia"] + "_"
        key += str(days)
        rows = self.dest.query("""SELECT Id,IdPessoa,DataInicio,DataTermino,Causa,IdFreq
            FROM Afastamentos WHERE IdFreq=?""", (key,))
        return [{**r, "DataInicio": normalized(r["DataInicio"]), "DataTermino": normalized(r["DataTermino"])}
                for r in rows]

    def observe(self, case, end, directory, emit):
        log = Path(self.config.get("log_servico", "C:/acesso/Logs/AcessusSyncProcessoService.log"))
        position = log.stat().st_size
        marker = ("Finalizou " + ("GetFeriasCedidas" if case["tipo"] == "ferias"
                                 else "GetAfastamentos") + " com sucesso.").encode()
        started = time.monotonic()
        timeout = self.config.get("timeout_segundos", 240)
        cycles = 0
        stable = 0
        previous_ids = None
        original_ids = [r["Id"] for r in self.target(case)]
        today = datetime.combine(datetime.now().date(), datetime.min.time())
        eligible = end is not None and datetime.fromisoformat(end) >= today
        if case["tipo"] == "ocorrencia":
            eligible = eligible and case["gera_afastamento"] and datetime.fromisoformat(case["inicio"]) <= today
        expected_api = [] if end is None else [end]
        while True:
            if log.stat().st_size < position:
                position = 0
            with log.open("rb") as f:
                f.seek(position)
                chunk = f.read()
                position = f.tell()
            cycles += chunk.count(marker)
            api = self.api_state(case)
            rows = self.target(case)
            dates_ok = (not rows if not eligible else len(rows) == 1 and
                        rows[0]["IdPessoa"] == self.config["pessoa"] and
                        rows[0]["DataInicio"] == case["inicio"] and rows[0]["DataTermino"] == end)
            text_ok = not rows or rows[0]["Causa"] == case["causa_esperada"]
            ids = [r["Id"] for r in rows]
            identity_ok = not eligible or not original_ids or ids == original_ids
            stable = stable + 1 if dates_ok and api == expected_api and ids == previous_ids else 0
            previous_ids = ids
            observed = dict(api=api, destino=rows, ciclos_concluidos=cycles,
                            datas_corretas=bool(dates_ok), texto_correto=text_ok,
                            ids_preservados=identity_ok)
            emit(dict(api=expected_api, destino_quantidade=int(eligible), termino=end,
                      causa=case["causa_esperada"]), observed)
            if cycles >= 1 and stable >= 2:
                return dict(status=("FALHOU_IDENTIDADE" if not identity_ok else
                                    "PASSOU" if text_ok else "FALHOU_TEXTO"), **observed)
            if time.monotonic() - started >= timeout:
                return dict(status="FALHOU_TIMEOUT", **observed)
            time.sleep(min(self.config.get("intervalo_segundos", 10),
                           max(0, timeout - (time.monotonic() - started))))

    def mutate(self, case, action, end, directory, step):
        if self.ui is None:
            from automatiza.ciclos_ui import RhLifecycleUI
            self.ui = RhLifecycleUI(self.settings, self.config)
        self.ui.apply(case, action, end, Path(directory) / f"etapa-{step:04}.png",
                      expected_before=self.source(case))
        for _ in range(20):
            if self.source(case) == end:
                return
            time.sleep(.5)
        raise Blocked("Gravação/remoção não confirmada na origem após fechar a tela.")
