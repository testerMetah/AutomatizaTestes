"""Migração conservadora: cópia verificada, original preservado no arquivo legado."""
import hashlib
import json
import shutil
import zipfile
from datetime import datetime, timedelta
from pathlib import Path

from automatiza import caminhos
from automatiza.organizacao import iniciar, atualizar, indice, carregar


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for bloco in iter(lambda: f.read(1024 * 1024), b""):
            h.update(bloco)
    return h.hexdigest()


def _iguais(origem, destino):
    if origem.is_file():
        return destino.is_file() and origem.stat().st_size == destino.stat().st_size and digest(origem) == digest(destino)
    antigos = sorted(p.relative_to(origem) for p in origem.rglob("*") if p.is_file())
    novos = sorted(p.relative_to(destino) for p in destino.rglob("*") if p.is_file())
    return antigos == novos and all(_iguais(origem / p, destino / p) for p in antigos)


def _itens():
    antigos = [*caminhos.legado("resultados").glob("auditorias-*"),
               *caminhos.legado("resultados").glob("rodada-*"),
               *caminhos.legado("reports").glob("execucoes/*"),
               *caminhos.legado("reports").glob("observacao/*"),
               caminhos.legado("reports") / "robot"]
    for p in sorted(set(antigos)):
        if p.is_dir() and not p.is_symlink():
            yield p


def plano():
    entries = []
    for src in _itens():
        arquivo = caminhos.arquivo_legado() / src.relative_to(caminhos.raiz())
        if arquivo.exists():
            continue
        tipo = "auditorias" if "auditorias" in src.name else ("robot" if "robot" in src.parts else "observacao" if "observacao" in src.parts else "execucao")
        stamp = datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y%m%d-%H%M%S")
        slug = "".join(c if c.isalnum() or c == "-" else "-" for c in src.name.lower())[:45].strip("-")
        ident = f"{stamp}-{tipo}-{slug}"
        dest = caminhos.rodadas() / ident
        if dest.exists() or (caminhos.arquivo_legado() / src.relative_to(caminhos.raiz())).exists():
            continue
        size = sum(p.stat().st_size for p in src.rglob("*") if p.is_file())
        entries.append((src, dest, arquivo, size))
    for nome in ("passo-a-passo.log", "passo-a-passo-detalhado.jsonl"):
        src = caminhos.legado("resultados") / nome
        dest = caminhos.logs_permanentes() / nome
        arquivo = caminhos.arquivo_legado() / "resultados" / nome
        if src.is_file() and not arquivo.exists():
            entries.append((src, dest, arquivo, src.stat().st_size))
    return entries


def backup():
    folder = caminhos.arquivo_legado() / "backups"
    folder.mkdir(parents=True, exist_ok=True)
    name = datetime.now().strftime("backup-%Y%m%d-%H%M%S.zip")
    path = folder / name
    if path.exists():
        raise FileExistsError(path)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for item in [caminhos.legado("resultados") / "passo-a-passo.log",
                     caminhos.legado("resultados") / "passo-a-passo-detalhado.jsonl",
                     caminhos.saidas() / "INDICE.md", caminhos.saidas() / "INDICE.json"]:
            if item.is_file():
                z.write(item, item.relative_to(caminhos.raiz()))
    return path


def organizar(aplicar=False):
    entries = plano()
    if not aplicar:
        return entries
    caminhos.preparar()
    backup()
    for src, dest, arquivo, _ in entries:
        dest.parent.mkdir(parents=True, exist_ok=True)
        arquivo.parent.mkdir(parents=True, exist_ok=True)
        if src.is_file():
            shutil.copy2(src, dest)
        else:
            shutil.copytree(src, dest)
        if not _iguais(src, dest):
            raise RuntimeError(f"Cópia divergente: {src}")
        # Move preservando o original; nunca usa unlink ou rmtree.
        shutil.move(str(src), str(arquivo))
        if not _iguais(arquivo, dest):
            raise RuntimeError(f"Arquivo legado divergente: {arquivo}")
        if dest.is_dir():
            partes = dest.name.split("-", 3)
            tipo = partes[2] if len(partes) > 2 else "desconhecido"
            iniciar(dest, tipo, src.name, build=None, banco_efetivo=None)
            atualizar(dest, origem="migrado", observacoes=f"Origem legada: {src.relative_to(caminhos.raiz())}",
                      estado_final="INTERROMPIDO")
    indice()
    return entries


def verificar():
    erros = []
    for nome in ("rodadas", "logs-permanentes", "observacao", "mapas", "comparacoes", "exportacoes", "arquivo-legado"):
        if not (caminhos.saidas() / nome).is_dir():
            erros.append(f"Pasta ausente: {nome}")
    for folder in caminhos.rodadas().iterdir() if caminhos.rodadas().exists() else []:
        if folder.is_dir() and not (folder / "manifesto.json").is_file():
            erros.append(f"Rodada sem manifesto: {folder.name}")
        elif folder.is_dir():
            raw = (folder / "manifesto.json").read_text(encoding="utf-8")
            if any(x in raw.lower() for x in ("password=", "pwd=", "senha=")):
                erros.append(f"Segredo possível: {folder.name}")
    for nome in ("INDICE.md", "INDICE.json"):
        if not (caminhos.saidas() / nome).is_file():
            erros.append(f"Índice ausente: {nome}")
    return erros


def marcar(ident, manter=False, nota=None):
    from automatiza.organizacao import atualizar
    pasta = caminhos.rodadas() / ident
    if not pasta.is_dir() or pasta.parent != caminhos.rodadas():
        raise ValueError("Rodada não encontrada")
    fields = {"manter": True} if manter else {}
    if nota is not None:
        fields["nota"] = nota
    result = atualizar(pasta, **fields)
    indice()
    return result


def limpar(aplicar=False, dias=60):
    items = sorted((carregar(p) for p in caminhos.rodadas().iterdir() if (p / "manifesto.json").is_file()),
                   key=lambda x: x["id"], reverse=True)
    ultimos = set()
    selecionados = []
    limite = datetime.now().astimezone() - timedelta(days=dias)
    for item in items:
        tipo = item.get("tipo")
        if tipo not in ultimos:
            ultimos.add(tipo)
            continue
        try:
            antigo = datetime.fromisoformat(item["inicio"]) < limite
        except (TypeError, ValueError):
            antigo = False
        if antigo and not item.get("manter"):
            selecionados.append(item)
    if aplicar:
        for item in selecionados:
            src = caminhos.rodadas() / item["id"]
            dest = caminhos.arquivo_legado() / "compactadas" / (item["id"] + ".zip")
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
                    for f in src.rglob("*"):
                        if f.is_file():
                            z.write(f, f.relative_to(src))
                # Os originais ficam intactos: compactação não é exclusão.
    return selecionados
