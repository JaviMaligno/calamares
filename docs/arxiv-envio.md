# Hoja de envío a arXiv (v1)

Estado: LISTO PARA ENVIAR en cuanto llegue el endorsement de
math.MG. El manuscrito es el commit etiquetado `v1-arxiv`
(la nota de autor del paper fija esa correspondencia). La ronda
final ciega (7 referees + meta, 0 fatales, 61 correcciones
aplicadas) está ejecutada — actas en `docs/drafts/ciega/`.

## El fichero a subir

`arxiv-bundle.tar.gz` (raíz del repo) — regenerado con
`python paper/make_arxiv_bundle.py` (VERIFICACION: OK); contiene
`main.tex` + `figures/` (3 PNG). Verificado: compila standalone
con pdflatex (2 pasadas), **60 páginas**, 0 referencias sin
resolver, 0 overfull. Sin bibtex (bibliografía inline); usa
`tikz`, `longtable` y `array`, todos estándar en TeX Live.

## Metadatos (copy-paste)

**Title:**
Greedy Packing of Nested Rings: Placement Rules, a Golden
Counterexample, and a Tribonacci Floor

**Authors:** Javier Aguilar Martín

**Abstract:** (el del paper, primeras líneas de main.tex — son
tres párrafos; pegarlo
tal cual, quitando los saltos de línea de LaTeX; arXiv no admite
\emph: sustituir por texto plano)

**Primary category:** math.MG (Metric Geometry)

**Cross-lists sugeridas:** math.CO, cs.CG

**MSC classes:** 52C15 (primaria); 52C26, 05B40, 68W25

**Comments:**
60 pages, 3 figures plus 3 diagrams. Computational verification scripts for
every numerical claim, extended proofs, adversarial verification
reports, and Lean 4 kernel-checked certificates of the exact
identities are available at
https://github.com/JaviMaligno/calamares (release v1-arxiv).

**License:** CC BY 4.0 (recomendada) o arXiv non-exclusive.

## El endorsement (el único bloqueo)

Cuenta de arXiv con email personal (javiecija96@gmail.com, el del
paper). Al intentar el primer envío a math.MG, arXiv mostrará el
código de endorsement (formato `XXXXXX`). Vías:

**Candidatos identificados y verificados contra arXiv, y los dos
emails ya redactados, en `docs/email_endorsement.md` (fichero
privado, fuera de git).** Resumen: el endorser debe haber
publicado en math.MG entre 3 meses y 5 años atrás; el primer
candidato es un contacto personal del doctorado cuya área es
metric geometry y que cumple el criterio con margen; hay un
segundo candidato de respaldo citado en la bibliografía del
paper. arXiv desaconseja escribir a varios a la vez.

Si ninguno saliera: arXiv admite solicitudes razonadas vía
moderación (más lento).

## Checklist final antes de subir

- [ ] `git tag v1-arxiv` apunta al commit del manuscrito que se
      sube (¡regenerar el bundle si hay commits nuevos al paper!).
- [ ] `python paper/make_arxiv_bundle.py` → VERIFICACION: OK.
- [ ] El PDF de arXiv (su compilador) puede diferir levemente:
      revisar el preview del envío antes de confirmar.
- [ ] Tras el anuncio: anotar el arXiv ID en la memoria
      (paper-arxiv-estado) y en el README del repo.
