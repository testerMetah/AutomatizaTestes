"""Keywords genéricas para mapas de telas Delphi validados no build atual."""

from pathlib import Path
from datetime import datetime
import re

from robot.api import logger

from automatiza.tela_generica import TelaGenerica, FalhaTeste, FalhaSistema


class BibliotecaTelas:
    ROBOT_LIBRARY_SCOPE = "TEST"

    def __init__(self):
        self.tela = None

    def mapa_deve_estar_validado(self, nome):
        from robot.libraries.BuiltIn import BuiltIn
        mapa = TelaGenerica(nome)
        if not mapa.mapa.get("validado_na_ui"):
            BuiltIn().skip(f"Mapa {nome} ainda não validado no build instalado")

    def _evidencia(self, erro):
        from pywinauto import Desktop
        from robot.libraries.BuiltIn import BuiltIn
        teste = BuiltIn().get_variable_value("${TEST NAME}", "sem_nome")
        teste = re.sub(r"[^a-zA-Z0-9_-]+", "_", teste).strip("_") or "sem_nome"
        pasta = Path("resultados") / datetime.now().strftime("%Y%m%d-%H%M%S-%f") / teste
        pasta.mkdir(parents=True, exist_ok=True)
        janelas = []
        for w in Desktop(backend="win32").windows():
            try:
                texto = w.window_text()
                if w.class_name() == "#32770":
                    texto += " | " + " | ".join(x.window_text() for x in w.descendants() if x.window_text())
                janelas.append(f"{w.class_name()} | {texto}")
            except Exception:
                continue
        (pasta / "falha.txt").write_text(
            f"{datetime.now().isoformat()}\n{type(erro).__name__}: {erro}\nJanelas:\n" + "\n".join(janelas), encoding="utf-8"
        )
        try:
            from dotenv import dotenv_values
            ambiente = dotenv_values(Path(__file__).parents[2] / ".env")
            executavel = Path(r"C:\acesso\Acessus.exe")
            resumo = [f"Banco configurado: {ambiente.get('SQL_SERVER', '?')}/{ambiente.get('SQL_DATABASE', '?')}",
                      f"Executável: {executavel}",
                      f"Modificado: {datetime.fromtimestamp(executavel.stat().st_mtime).isoformat() if executavel.exists() else 'ausente'}"]
            (pasta / "contexto.txt").write_text("\n".join(resumo) + "\n", encoding="utf-8")
        except Exception:
            pass
        if self.tela:
            try:
                imagem = pasta / "acessus.png"
                alvo = self.tela._principal()
                alvo.capture_as_image().save(imagem)
                logger.info(f'<a href="{imagem.resolve().as_uri()}">Screenshot</a>', html=True)
            except Exception as exc:
                logger.warn(f"Screenshot indisponível: {exc}")
        logger.error(f"{type(erro).__name__}: {erro}; evidências em {pasta.resolve()}")

    def _acao(self, nome, funcao, *args):
        exibicao = (args[0], "[oculto]") if nome == "preencher" and args and "senha" in str(args[0]).lower() else args
        logger.info(f"Tela={self.tela.nome if self.tela else '-'} ação={nome} controle/valor={exibicao}")
        try:
            resultado = funcao(*args)
            logger.info(f"Tela={self.tela.nome} ação={nome} resultado={resultado!r}")
            return resultado
        except Exception as exc:
            self._evidencia(exc)
            raise

    def abrir_tela(self, nome):
        self.tela = TelaGenerica(nome)
        return self._acao("abrir", self.tela.abrir)

    def preencher_campo(self, campo, valor):
        return self._acao("preencher", self.tela.preencher, campo, valor)

    def clicar_controle(self, botao):
        return self._acao("clicar", self.tela.clicar, botao)

    def teclar_na_tela(self, teclas):
        return self._acao("teclar", self.tela.teclar, teclas)

    def ler_mensagem(self):
        return self._acao("ler_mensagem", self.tela.ler_mensagem)

    def ler_grid(self, nome="grid"):
        return self._acao("ler_grid", self.tela.ler_grid, nome)

    def fechar_tela(self):
        if self.tela:
            return self._acao("fechar", self.tela.fechar)

    def fechar_popup(self):
        if self.tela:
            return self._acao("fechar_popup", self.tela.fechar_popup)

    def mensagem_deve_conter(self, mensagem, trecho):
        if trecho not in " | ".join(mensagem):
            erro = FalhaSistema(f"Esperado texto {trecho!r}; obtido: {mensagem!r}; tela: {self.tela.nome}")
            self._evidencia(erro)
            raise erro

    def resultado_deve_ser(self, obtido, esperado):
        if obtido != esperado:
            erro = FalhaSistema(f"Esperado: {esperado!r}; obtido: {obtido!r}; tela: {self.tela.nome if self.tela else '-'}")
            self._evidencia(erro)
            raise erro
