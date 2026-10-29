"""Extrai menus estáticos dos formulários principais do código Delphi."""

from __future__ import annotations

import re
from pathlib import Path

FONTE = Path(r"C:\Acessus-Fonte")
SAIDA = Path(r"C:\AutomatizaTestes\docs\mapa_sistema.md")
MODULOS = ["Acesso", "Administracao", "Escola", "Estacionamento", "Modulo", "Portaria", "Refeitorio", "Trabalho"]


def decodificar(valor: str) -> str:
    partes = re.findall(r"'((?:''|[^'])*)'|#(\d+)", valor)
    return "".join(chr(int(n)) if n else s.replace("''", "'") for s, n in partes).replace("&", "")


def menus(dfm: Path):
    linhas = dfm.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    inicio = next((i for i, linha in enumerate(linhas) if re.search(r"object \w+: TActionManager", linha)), None)
    if inicio is None:
        return []
    pilha = []
    entradas = []
    for linha in linhas[inicio + 1 :]:
        s = linha.strip()
        if re.match(r"object \w+: ", s):
            break
        if s == "item":
            item = {"caption": "", "action": ""}
            pilha.append(item)
            entradas.append((list(pilha[:-1]), item))
        elif s.startswith("Action = ") and pilha:
            pilha[-1]["action"] = s.split("=", 1)[1].strip()
        elif s.startswith("Caption = ") and pilha:
            pilha[-1]["caption"] = decodificar(s.split("=", 1)[1].strip())
        elif (s == "end" or s.startswith("end>")) and pilha:
            pilha.pop()
    return entradas


def acoes(dfm: Path):
    texto = dfm.read_text(encoding="utf-8-sig", errors="replace")
    return dict(re.findall(r"object (\w+): TAction\b.*?OnExecute = (\w+)", texto, re.S))


def procedimentos(pas: Path):
    texto = pas.read_text(encoding="utf-8-sig", errors="replace")
    encontrados = {}
    padrao = r"(?ms)^procedure\s+\w+\.(\w+)\s*(?:\([^;]*\))?\s*;(.+?)(?=^procedure\s+\w+\.|^function\s+\w+\.|\Z)"
    for nome, corpo in re.findall(padrao, texto):
        forms = re.findall(r"\bTelaShow\s*\(\s*\w+\s*,\s*(T\w+)", corpo, re.I)
        if not forms:
            forms = re.findall(r"\b(T\w+)\.Create\s*\(", corpo)
        encontrados[nome] = forms
    return encontrados


def indice_forms():
    resultado = {}
    for dfm in FONTE.rglob("*.dfm"):
        try:
            primeira = dfm.open(encoding="utf-8-sig", errors="replace").readline()
        except OSError:
            continue
        m = re.match(r"(?:object|inherited)\s+\w+\s*:\s*(T\w+)", primeira.lstrip("\ufeff"))
        if m:
            resultado.setdefault(m.group(1).lower(), []).append(dfm)
    return resultado


def principal(modulo):
    if modulo == "Acesso":
        return FONTE / "Acesso/uFrmPrincipal.dfm"
    return next((FONTE / modulo / "Views").glob("*.Views.Principal.dfm"))


def main():
    indice = indice_forms()
    cabecalho = SAIDA.read_text(encoding="utf-8").split("## Menus e telas")[0]
    linhas = [cabecalho.rstrip(), "", "## Menus e telas", "", "Extração estática das `TActionManager` dos formulários principais. A presença real de cada item depende das permissões do usuário e do build instalado. `?` indica vínculo não resolvido automaticamente. O caminho da unit é relativo a `C:\\Acessus-Fonte`.", "", "| Módulo | Menu > submenu > item | Form aberto | Unit `.pas` / `.dfm` |", "|---|---|---|---|"]
    total = 0
    telas = set()
    pendentes = []
    for modulo in MODULOS:
        dfm = principal(modulo)
        pas = dfm.with_suffix(".pas")
        actions = acoes(dfm)
        procs = procedimentos(pas)
        for ancestrais, item in menus(dfm):
            if not item["action"] or item["caption"] == "-":
                continue
            caminho = " > ".join([a["caption"] for a in ancestrais if a["caption"]] + [item["caption"]])
            handler = actions.get(item["action"], "")
            forms = procs.get(handler, [])
            executavel = ""
            if modulo == "Modulo" and item["caption"] in {"Acesso", "Refeitório", "Portaria", "Estacionamento", "Escola", "Administração"}:
                executavel = {"Acesso": "Acessus.exe", "Refeitório": "Acessus.Refeitorio.exe", "Portaria": "Acessus.Portaria.exe", "Estacionamento": "Acessus.Estacionamento.exe", "Escola": "Acessus.Escola.exe", "Administração": "Acessus.Administracao.exe"}[item["caption"]]
            telas.update(forms)
            form = ", ".join(forms) if forms else (f"Executa {executavel}" if executavel else "—")
            units = []
            for f in forms:
                candidatos = indice.get(f.lower(), [])
                if candidatos:
                    preferidos = sorted(candidatos, key=lambda p: (not str(p).startswith(str(FONTE / modulo)), len(str(p))))
                    escolhido = preferidos[0]
                    rel = escolhido.relative_to(FONTE).as_posix()
                    units.append(f"`{rel[:-4]}.pas` / `{rel}`")
                else:
                    units.append("?")
            unit = ", ".join(units) if units else (f"`{pas.relative_to(FONTE).as_posix()}`" if executavel or not forms else "?")
            if unit == "?":
                pendentes.append(f"- **{modulo} > {caminho}**: ação `{item['action']}`, handler `{handler or '?'}`; vínculo com form/arquivo não resolvido por `TelaShow`.")
            linhas.append(f"| {modulo} | {caminho} | `{form}` | {unit} |")
            total += 1
    linhas += ["", f"**Total:** {total} itens acionáveis nos `TActionManager` de 7 módulos; {len(telas)} classes de tela distintas identificadas por `TelaShow` ou criação modal. O módulo Trabalho usa navegação customizada e não entra nessas contagens.", "", "## Vínculos pendentes de inspeção", ""] + (pendentes or ["Nenhum."])
    linhas += ["", "## Limites da extração", "", "- O formulário principal de `Trabalho` não contém `TActionManager`; seus comandos exigem inspeção específica."]
    trabalho = (SAIDA.parent / "mapa_trabalho.md").read_text(encoding="utf-8")
    SAIDA.write_text("\n".join(linhas) + "\n\n" + trabalho, encoding="utf-8")


if __name__ == "__main__":
    main()
