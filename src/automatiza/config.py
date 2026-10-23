import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]


def odbc_value(value: str) -> str:
    """Protege valores com ponto e vírgula e chaves na conexão ODBC."""
    return "{" + value.replace("}", "}}") + "}"


@dataclass(frozen=True)
class Settings:
    app_path: str = ""
    app_work_dir: str = ""
    app_backend: str = "win32"
    app_title_re: str = ""
    launcher_path: str = ""
    launcher_title_re: str = ""
    launcher_menu_path: str = ""
    ui_timeout: int = 20
    rh_path: str = r"C:\meta\rhsis\rh.exe"
    rh_work_dir: str = r"C:\meta\rhsis"
    rh_user: str = ""
    rh_password: str = field(default="", repr=False)
    rh_frequency_menu: str = "Módulos->Frequência"
    rh_continue_invalid_config: str = "no"
    sql_server: str = ""
    sql_database: str = ""
    sql_driver: str = "ODBC Driver 18 for SQL Server"
    sql_auth: str = "windows"
    sql_user: str = ""
    sql_password: str = field(default="", repr=False)
    sql_encrypt: str = "yes"
    sql_trust_certificate: str = "no"
    sql_timeout: int = 15

    @classmethod
    def load(cls):
        load_dotenv(ROOT / ".env", override=False)
        fields = {}
        for name in cls.__dataclass_fields__:
            value = os.getenv(name.upper())
            if value is not None:
                fields[name] = int(value) if name.endswith("timeout") else value
        return cls(**fields)

    def connection_string(self) -> str:
        if not self.sql_server or not self.sql_database:
            raise ValueError("Configure SQL_SERVER e SQL_DATABASE no .env.")
        if self.sql_auth not in {"windows", "sql"}:
            raise ValueError("SQL_AUTH deve ser windows ou sql.")
        if self.sql_encrypt not in {"yes", "no"} or self.sql_trust_certificate not in {"yes", "no"}:
            raise ValueError("SQL_ENCRYPT e SQL_TRUST_CERTIFICATE devem ser yes ou no.")
        parts = [f"DRIVER={odbc_value(self.sql_driver)}", f"SERVER={odbc_value(self.sql_server)}",
                 f"DATABASE={odbc_value(self.sql_database)}", f"Encrypt={self.sql_encrypt}",
                 f"TrustServerCertificate={self.sql_trust_certificate}"]
        if self.sql_auth == "windows":
            parts.append("Trusted_Connection=yes")
        else:
            if not self.sql_user or not self.sql_password:
                raise ValueError("Configure SQL_USER e SQL_PASSWORD.")
            parts.extend([f"UID={odbc_value(self.sql_user)}", f"PWD={odbc_value(self.sql_password)}"])
        return ";".join(parts) + ";"
