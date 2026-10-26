import json
from pathlib import Path


def read_query(file: str | None = None) -> str:
    if file:
        sql = Path(file).read_text(encoding="utf-8-sig").strip()
    else:
        print("Cole/digite o SQL em várias linhas. Termine com /executar numa linha separada.")
        print("Use /cancelar para sair sem executar. Não use GO (comando do SSMS).")
        lines = []
        while True:
            try:
                line = input("sql> " if not lines else "...> ")
            except EOFError:
                raise ValueError("Entrada encerrada sem /executar.") from None
            if line.strip().lower() == "/cancelar":
                return ""
            if line.strip().lower() == "/executar":
                break
            lines.append(line)
        sql = "\n".join(lines).strip()
    if not sql:
        raise ValueError("Digite uma consulta antes de executar.")
    return sql


def run_query(db, sql: str, params=(), output: str | None = None):
    rows = db.query(sql, params)
    result = json.dumps(rows, ensure_ascii=False, indent=2, default=str)
    print(result)
    print(f"{len(rows)} linha(s).")
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(result, encoding="utf-8")
        print(f"Resultado salvo em: {path.resolve()}")
    return rows
