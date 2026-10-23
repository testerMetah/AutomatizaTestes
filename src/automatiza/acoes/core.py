from dataclasses import dataclass


class Blocked(RuntimeError):
    pass


@dataclass
class ActionResult:
    action: str
    entity: str
    state: str
    details: dict


class Actions:
    def __init__(self, backend, report):
        self.backend, self.report = backend, report

    def execute(self, step):
        name = step["acao"]
        method = getattr(self, name, None)
        if method is None or name.startswith("_"):
            raise ValueError(f"Ação desconhecida: {name}")
        entity = step.get("entidade", "")
        try:
            details = method(step) or {}
            self.report.emit("ACAO", acao=name, entidade=entity, resultado="PASSOU", quantidade=details.get("quantidade", 0), detalhes=details)
            return ActionResult(name, entity, "PASSOU", details)
        except Blocked as exc:
            self.report.emit("ACAO", acao=name, entidade=entity, resultado="BLOQUEADO", motivo=str(exc))
            return ActionResult(name, entity, "BLOQUEADO", {"motivo": str(exc)})
        except Exception as exc:
            self.report.emit("ACAO", acao=name, entidade=entity, resultado="FALHOU", erro=f"{type(exc).__name__}: {exc}")
            return ActionResult(name, entity, "FALHOU", {"erro": str(exc)})

    def _mutate(self, name, step):
        if not self.backend.supports(name, step.get("entidade")):
            raise Blocked(f"{name}/{step.get('entidade')}: mapa de tela e limpeza do build atual não validados")
        return self.backend.mutate(name, step)

    def cadastrar(self, step): return self._mutate("cadastrar", step)
    def alterar(self, step): return self._mutate("alterar", step)
    def deletar(self, step): return self._mutate("deletar", step)
    def recriar_igual(self, step): return self._mutate("recriar_igual", step)

    def cadastrar_em_massa(self, step):
        n = int(step.get("quantidade", 1))
        if not 1 <= n <= int(step.get("limite_massa", 5)):
            raise Blocked("Volume excede o limite configurado")
        if not self.backend.supports("cadastrar", step.get("entidade")):
            raise Blocked("Cadastro em massa: mapa de tela e limpeza não validados")
        for index in range(n):
            self.backend.mutate("cadastrar", {**step, "indice": index})
        return {"quantidade": n}

    def importar(self, step):
        if not self.backend.supports("importar", step.get("entidade")):
            raise Blocked("Disparo e término da importação não mapeados para este fluxo")
        return self.backend.mutate("importar", step)

    def reiniciar_servico(self, step):
        raise Blocked("Serviços Sync (novo123) e Comunicação (sm): início/reinício exige autorização explícita")

    def fechar_e_reabrir_acessus(self, step):
        if not self.backend.supports("fechar_e_reabrir_acessus", step.get("entidade")):
            raise Blocked("Reabertura depende de login e estado da aplicação; fluxo não validado no build atual")
        return self.backend.mutate("fechar_e_reabrir_acessus", step)

    def verificar_banco(self, step):
        from automatiza.sequencias.verificar import check_database
        from automatiza.sequencias.targets import target
        info = target(step.get("banco", "destino"))
        rows = check_database(self.report, server=info["servidor"], database=info["banco"],
                              sql=step.get("sql", "SELECT 1 AS valor"), params=step.get("parametros", []),
                              expected=step.get("esperado", {"valor": 1}))
        return {"linhas": len(rows)}

    def observar_acessus(self, step):
        from automatiza.ui import Gateway, UiBlocked
        try:
            gateway = Gateway(self.report)
            gateway.connect()
            gateway.screenshot("observacao")
            return {"janela": gateway.window.window_text(), "classe": gateway.window.class_name()}
        except UiBlocked as exc:
            raise Blocked(str(exc)) from exc

    def mapear_tela(self, step):
        from automatiza.ui import Gateway, UiBlocked
        try:
            gateway = Gateway(self.report)
            items = gateway.inventory()
            gateway.screenshot("mapa")
            return {"controles": len(items)}
        except UiBlocked as exc:
            raise Blocked(str(exc)) from exc
