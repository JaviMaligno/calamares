#!/usr/bin/env python3
"""Construye el bundle de arXiv a partir de paper/.

arXiv no acepta el PDF: compila el LaTeX en sus servidores. El bundle debe
contener las fuentes y todo lo que estas incluyen, con las rutas relativas
intactas (main.tex referencia figures/*.png).

La bibliografia es \\bibitem en linea (entorno thebibliography), asi que no
hace falta .bbl ni .bib.

Uso:  python paper/make_arxiv_bundle.py
Sale: paper/arxiv-bundle.tar.gz  (+ verificacion del contenido)
"""
import os
import re
import sys
import tarfile
from pathlib import Path

AQUI = os.path.dirname(os.path.abspath(__file__))
PRINCIPAL = "main.tex"
SALIDA = os.path.join(AQUI, "arxiv-bundle.tar.gz")

# Lo que NO debe viajar: artefactos de compilacion y el PDF (arXiv lo genera).
EXCLUIR = re.compile(r"\.(aux|log|out|toc|synctex\.gz|fls|fdb_latexmk|blg|pdf)$")


def collect_sources(root, principal=PRINCIPAL):
    """Collect static TeX inputs and graphics, once each, inside the paper root.

    Relative paths follow the compilation working directory, as in the
    manuscript. Cycles are visited once; missing files fail before archiving.
    """
    root = Path(root).resolve()
    members = {}

    def resolve(rel, extensions):
        candidate = (root / rel).resolve()
        candidate.relative_to(root)
        for path in [candidate] + [Path(str(candidate) + ext) for ext in extensions]:
            if path.is_file():
                path.resolve().relative_to(root)
                return path
        raise FileNotFoundError(f'Referenced file does not exist: {rel}')

    def visit(path, is_tex):
        arc = path.relative_to(root).as_posix()
        if arc in members:
            return
        members[arc] = path
        if not is_tex:
            return
        text = re.sub(r'(?<!\\)%.*', '', path.read_text(encoding='utf-8'))
        for rel in re.findall(r'\\(?:input|include)\s*\{([^}]+)\}', text):
            visit(resolve(rel, ('.tex',)), True)
        for rel in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', text):
            visit(resolve(rel, ('.png', '.pdf', '.jpg', '.jpeg', '.eps')), False)

    visit(resolve(principal, ('.tex',)), True)
    return [(str(path), arc) for arc, path in sorted(members.items())]


def main():
    ruta_principal = os.path.join(AQUI, PRINCIPAL)
    if not os.path.isfile(ruta_principal):
        sys.exit("[FALLO] no encuentro %s" % PRINCIPAL)

    try:
        miembros = collect_sources(AQUI)
    except (FileNotFoundError, ValueError) as error:
        sys.exit(f"[FALLO] {error}")

    for disco, arc in miembros:
        if EXCLUIR.search(arc):
            sys.exit("[FALLO] artefacto de compilacion en el bundle: %s" % arc)

    if os.path.exists(SALIDA):
        os.remove(SALIDA)
    # Metadatos de miembros y orden estables; gzip conserva su propia fecha.
    with tarfile.open(SALIDA, "w:gz") as tar:
        for disco, arc in sorted(miembros, key=lambda m: m[1]):
            info = tar.gettarinfo(disco, arcname=arc)
            info.mtime = 0
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            with open(disco, "rb") as fh:
                tar.addfile(info, fh)

    with tarfile.open(SALIDA) as tar:
        nombres = sorted(tar.getnames())
    tam = os.path.getsize(SALIDA)

    print("bundle: %s (%.1f KB)" % (os.path.basename(SALIDA), tam / 1024.0))
    for n in nombres:
        print("  %s" % n)

    ok = PRINCIPAL in nombres and len(nombres) == len(miembros)
    if tam > 50 * 1024 * 1024:          # limite duro de arXiv
        print("[FALLO] el bundle supera los 50 MB que admite arXiv")
        ok = False
    print("VERIFICACION: %s" % ("OK" if ok else "[FALLO]"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
