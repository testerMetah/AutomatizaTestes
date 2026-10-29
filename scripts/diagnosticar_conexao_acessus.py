"""Compara conexões de leitura com credenciais da venv e do INI decriptado."""

from pathlib import Path
from dotenv import dotenv_values
import pyodbc


def testar(server, database, usuario, senha, driver):
    parametros = [f"DRIVER={{{driver}}}", f"SERVER={server}", f"DATABASE={database}",
                  f"UID={usuario}", f"PWD={senha}", "Connection Timeout=5"]
    try:
        with pyodbc.connect(";".join(parametros), timeout=5) as conexao:
            banco = conexao.cursor().execute("SELECT DB_NAME()").fetchone()[0]
        return f"OK: {banco}"
    except pyodbc.Error as erro:
        return f"FALHA: {type(erro).__name__}"  # Erros de driver podem conter informação sensível.


def main():
    env = dotenv_values(Path(__file__).parents[1] / ".env")
    linhas = Path(r"C:\acesso\ConexaoConfig.ini").read_text(encoding="utf-8-sig").splitlines()
    ini = dict(linha.strip().split("=", 1) for linha in linhas if "=" in linha)
    driver = env.get("SQL_DRIVER", "ODBC Driver 17 for SQL Server")
    print("Ambiente:", testar(env["SQL_SERVER"], env["SQL_DATABASE"], env["SQL_USER"], env["SQL_PASSWORD"], driver))
    # UDMConexaoBD.SetConfigBD chama UFEncrypt.DesCriptografa(..., 99).
    senha_ini = "".join(chr(ord(caractere) - 99) for caractere in ini["Password"])
    print("INI Acessus decriptado:", testar(ini["Server"], ini["Database"], ini["User_Name"], senha_ini, driver))
    print("Mesmo servidor/banco/usuário:", (env["SQL_SERVER"], env["SQL_DATABASE"], env["SQL_USER"]) ==
          (ini["Server"], ini["Database"], ini["User_Name"]))
    print("Senha decriptada igual à do ambiente:", env["SQL_PASSWORD"] == senha_ini)


if __name__ == "__main__":
    main()
