"""Cria fichas estáticas para forms acessíveis pelo menu Refeitório.

Não substitui a análise de regras: registra controles, handlers e literais
com sua origem para revisão progressiva.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gerar_mapa_fonte import FONTE, decodificar, menus, acoes, procedimentos, indice_forms, principal
from notas_relatorios_refeitorio import NOTAS, BASE
from notas_coletores_refeitorio import NOTAS as NOTAS_COLETORES

NOTAS = {**NOTAS, **NOTAS_COLETORES}

DESTINO = Path(r"C:\AutomatizaTestes\docs\telas")
CURADOS = {
    "tfrmcadrefeitorios": "refeitorio_cadastro.md",
    "tfrmrefeicoes": "refeitorio_incluir_refeicoes.md",
    "tfrmcadcardapio": "refeitorio_cardapios.md",
    "tfrmgerarrefeicao": "refeitorio_importar_refeicoes.md",
    "tfrmrefeitorioviewsreservasrefeicoes": "refeitorio_reservas_refeicoes.md",
}


def limpar_nome(nome):
    nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", nome.lower()).strip("_")


def propriedade(texto):
    return decodificar(texto) if "'" in texto or "#" in texto else texto.strip()


def controles(dfm):
    linhas = dfm.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    itens = []
    pilha = []
    for n, linha in enumerate(linhas, 1):
        recuo = len(linha) - len(linha.lstrip())
        if linha.strip() and not linha.lstrip().startswith(("item", "end")):
            while pilha and pilha[-1][0] >= recuo:
                pilha.pop()
        m = re.match(r"\s*(object|inherited)\s+(\w+)\s*:\s*(\w+)", linha)
        if m:
            atual = {"nome": m.group(2), "classe": m.group(3), "linha": n, "herdado": m.group(1) == "inherited"}
            itens.append(atual)
            pilha.append((recuo, atual))
            continue
        if pilha:
            p = re.match(r"\s*(Caption|TabOrder|EditMask|MaxLength|Text|ItemIndex|Checked|Visible|Enabled|Style|OnClick|OnExit|OnChange|Action)\s*=\s*(.*)", linha)
            if p and p.group(1) not in pilha[-1][1]:
                pilha[-1][1][p.group(1)] = propriedade(p.group(2))
    return itens


def escapar(valor):
    return str(valor or "—").replace("|", "\\|").replace("\n", " ")


def literais_mensagem(pas):
    texto = pas.read_text(encoding="utf-8-sig", errors="replace")
    saida = []
    for n, linha in enumerate(texto.splitlines(), 1):
        if linha.lstrip().startswith("//"):
            continue
        if re.search(r"\b(?:GetAplicacao\.Msg|PTMessage|ShowMessage|Confirma)\s*\(", linha, re.I):
            partes = re.findall(r"'((?:''|[^'])*)'", linha)
            if partes:
                saida.append((n, partes[0].replace("''", "'")))
    return saida


def main():
    indice = indice_forms()
    principal_dfm = principal("Refeitorio")
    principal_pas = principal_dfm.with_suffix(".pas")
    action_handlers = acoes(principal_dfm)
    proc_forms = procedimentos(principal_pas)
    linhas_indice = ["# Cobertura das telas do menu Refeitório", "", "Fonte: commit `28074dd` da cópia local. As fichas automáticas registram estrutura estática; as fichas analisadas manualmente também explicam regras e fluxo. O build instalado pode diferir.", "", "| Menu | Form | Documento | Estado |", "|---|---|---|---|"]
    vistos = set()
    for ancestrais, item in menus(principal_dfm):
        if not item["action"]:
            continue
        caminho = " > ".join([a["caption"] for a in ancestrais if a["caption"]] + [item["caption"]])
        handler = action_handlers.get(item["action"], "")
        forms = proc_forms.get(handler, [])
        if not forms:
            linhas_indice.append(f"| {escapar(caminho)} | — | — | Ação sem form ou form ausente da cópia |")
            continue
        for form in forms:
            candidatos = indice.get(form.lower(), [])
            if not candidatos:
                linhas_indice.append(f"| {escapar(caminho)} | `{form}` | — | DFM ausente |")
                continue
            nome_doc = CURADOS.get(form.lower(), f"refeitorio_{limpar_nome(form)}.md")
            estado = "Análise manual" if form.lower() in CURADOS else ("Inventário + fluxo" if form.lower() in NOTAS else "Inventário estático")
            linhas_indice.append(f"| {escapar(caminho)} | `{form}` | [{nome_doc}]({nome_doc}) | {estado} |")
            if form.lower() in vistos or form.lower() in CURADOS:
                continue
            vistos.add(form.lower())
            dfm = sorted(candidatos, key=lambda p: (not str(p).startswith(str(FONTE / "Refeitorio")), len(str(p))))[0]
            pas = dfm.with_suffix(".pas")
            if not pas.exists():
                continue
            titulo = f"Refeitório > {caminho}"
            aviso = ("Esta ficha combina inventário estático com notas de leitura manual das procedures; ainda requer conferência de controllers, DAOs e do build instalado." if form.lower() in NOTAS else "Esta ficha ainda precisa de análise manual das regras de Salvar, Consultar, Excluir, Cancelar e Relatório. Não usar como resultado esperado de teste sem conferir o build instalado.")
            doc = [f"# {titulo}", "", f"> Inventário estático de `{dfm.relative_to(FONTE).as_posix()}` e `{pas.relative_to(FONTE).as_posix()}` no commit `28074dd`. {aviso}", "", f"- Form: `{form}`", f"- Abertura: `{handler}` em `{principal_pas.relative_to(FONTE).as_posix()}`", "", "## Controles declarados no DFM", "", "`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.", "", "| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |", "|---|---|---|---:|---|---:|---|---|"]
            for c in controles(dfm):
                if c["classe"] in {"TImage", "TShape", "TImageList", "TClientDataSet", "TDataSource", "TIntegerField", "TStringField", "TBooleanField", "TFloatField", "TDateTimeField"}:
                    continue
                padrao = ", ".join(f"{k}={c[k]}" for k in ("Text", "ItemIndex", "Checked", "Visible", "Enabled") if k in c)
                eventos = ", ".join(f"{k}={c[k]}" for k in ("Action", "OnClick", "OnExit", "OnChange") if k in c)
                doc.append(f"| `{c['nome']}` | `{c['classe']}`{' (herdado)' if c['herdado'] else ''} | {escapar(c.get('Caption'))} | {escapar(c.get('TabOrder'))} | `{escapar(c.get('EditMask'))}` | {escapar(c.get('MaxLength'))} | {escapar(padrao)} | {escapar(eventos)} |")
            doc += ["", "## Mensagens literais detectadas", "", "Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.", ""]
            mensagens = literais_mensagem(pas)
            doc += [f"- Linha {n}: `{escapar(s)}`" for n, s in mensagens] or ["- Nenhuma chamada com literal direto detectada."]
            doc += ["", "## Ações encontradas na unit", "", "A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.", ""]
            texto = pas.read_text(encoding="utf-8-sig", errors="replace")
            nomes = sorted(set(re.findall(r"^procedure\s+\w+\.(\w+)\s*(?:\(|;)", texto, re.M)))
            doc += [f"- `{nome}`" for nome in nomes if re.search(r"Act|btn|Btn|Relat|Report|Consultar|Buscar|Salvar|Excluir|Cancelar|Validar", nome, re.I)] or ["- Nenhuma ação reconhecida pelo nome."]
            if form.lower() in NOTAS:
                doc += ["", "## Fluxo e regras identificados", "", BASE, ""]
                doc += [f"- {nota}" for nota in NOTAS[form.lower()]]
            doc += ["", "## Pendências de análise", "", "- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.", "- Confirmar mensagens completas e controles na UI do build testado.", ""]
            (DESTINO / nome_doc).write_text("\n".join(doc), encoding="utf-8")
    (DESTINO / "README_refeitorio.md").write_text("\n".join(linhas_indice) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
