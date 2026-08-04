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

AQUI = os.path.dirname(os.path.abspath(__file__))
PRINCIPAL = "main.tex"
SALIDA = os.path.join(AQUI, "arxiv-bundle.tar.gz")

# Lo que NO debe viajar: artefactos de compilacion y el PDF (arXiv lo genera).
EXCLUIR = re.compile(r"\.(aux|log|out|toc|synctex\.gz|fls|fdb_latexmk|blg|pdf)$")


def graficos_referenciados(ruta_tex):
    """Rutas de \\includegraphics tal y como las escribe el .tex."""
    with open(ruta_tex, encoding="utf-8") as fh:
        texto = fh.read()
    # \includegraphics[...]{ruta}  -- las opciones son opcionales
    return re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", texto)


def resuelve(rel):
    """Encuentra el fichero en disco; anade extension si el .tex la omite."""
    cand = os.path.join(AQUI, rel)
    if os.path.isfile(cand):
        return cand
    for ext in (".png", ".pdf", ".jpg", ".jpeg", ".eps"):
        if os.path.isfile(cand + ext):
            return cand + ext
    return None


def main():
    ruta_principal = os.path.join(AQUI, PRINCIPAL)
    if not os.path.isfile(ruta_principal):
        sys.exit("[FALLO] no encuentro %s" % PRINCIPAL)

    miembros = [(ruta_principal, PRINCIPAL)]
    faltan = []
    for rel in graficos_referenciados(ruta_principal):
        disco = resuelve(rel)
        if disco is None:
            faltan.append(rel)
            continue
        # El nombre dentro del tar conserva la ruta relativa del \includegraphics,
        # con la extension real del fichero en disco.
        arc = rel if os.path.basename(disco) == os.path.basename(rel) \
            else rel + os.path.splitext(disco)[1]
        miembros.append((disco, arc.replace(os.sep, "/")))

    if faltan:
        sys.exit("[FALLO] figuras referenciadas que no existen: %s" % faltan)

    for disco, arc in miembros:
        if EXCLUIR.search(arc):
            sys.exit("[FALLO] artefacto de compilacion en el bundle: %s" % arc)

    if os.path.exists(SALIDA):
        os.remove(SALIDA)
    # mtime fijo y orden estable => bundle reproducible byte a byte.
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
