# Hoja de envío a arXiv (v1)

Estado: LISTO PARA ENVIAR en cuanto llegue el endorsement de
math.MG. El manuscrito es el commit etiquetado `v1-arxiv`
(la nota de autor del paper fija esa correspondencia). La ronda
final ciega (7 referees + meta, 0 fatales, 61 correcciones
aplicadas) está ejecutada — actas en `docs/drafts/ciega/`.

## El fichero a subir

`paper/arxiv-bundle.tar.gz` — regenerado con
`python paper/make_arxiv_bundle.py`; contiene `main.tex` +
`figures/` (3 PNG). Verificado: compila standalone con pdflatex
(2 pasadas), 52 páginas, 0 referencias sin resolver. Sin bibtex
(bibliografía inline), sin paquetes exóticos.

## Metadatos (copy-paste)

**Title:**
Greedy Packing of Nested Rings: Placement Rules, a Golden
Counterexample, and a Tribonacci Floor

**Authors:** Javier Aguilar Martín

**Abstract:** (el del paper, líneas 42-82 de main.tex — pegarlo
tal cual, quitando los saltos de línea de LaTeX; arXiv no admite
\emph: sustituir por texto plano)

**Primary category:** math.MG (Metric Geometry)

**Cross-lists sugeridas:** math.CO, cs.CG

**MSC classes:** 52C15 (primaria); 52C26, 05B40, 68W25

**Comments:**
52 pages, 3 figures. Computational verification scripts for
every numerical claim, extended proofs, adversarial verification
reports, and Lean 4 kernel-checked certificates of the exact
identities are available at
https://github.com/JaviMaligno/calamares (release v1-arxiv).

**License:** CC BY 4.0 (recomendada) o arXiv non-exclusive.

## El endorsement (el único bloqueo)

Cuenta de arXiv con email personal (javiecija96@gmail.com, el del
paper). Al intentar el primer envío a math.MG, arXiv mostrará el
código de endorsement (formato `XXXXXX`). Vías:

1. Contactos académicos que publiquen en math.MG/math.CO (un
   endorser debe haber publicado ~3-4 papers en la categoría en
   los últimos 5 años). El mensaje útil: título + abstract + el
   enlace al repo (los certificados Lean y los scripts hacen el
   paper inusualmente auditable para un endorser).
2. Si no hay endorser a mano: arXiv acepta solicitudes razonadas
   vía moderación (más lento).

## Checklist final antes de subir

- [ ] `git tag v1-arxiv` apunta al commit del manuscrito que se
      sube (¡regenerar el bundle si hay commits nuevos al paper!).
- [ ] `python paper/make_arxiv_bundle.py` → VERIFICACION: OK.
- [ ] El PDF de arXiv (su compilador) puede diferir levemente:
      revisar el preview del envío antes de confirmar.
- [ ] Tras el anuncio: anotar el arXiv ID en la memoria
      (paper-arxiv-estado) y en el README del repo.
