# Hoja de envío a arXiv (v1)

Estado: **ANUNCIADO el 2026-09-15 como [`arXiv:2609.15554`](https://arxiv.org/abs/2609.15554)**
(DOI `10.48550/arXiv.2609.15554`). Enviado el 2026-09-14 como `submit/8077477`;
moderacion pasada sin incidencias. Verificado en la propia pagina de arXiv:
titulo, autor, primaria math.MG y cross-lists cs.CG y math.CO, todo como se
envio. El manuscrito es el commit etiquetado `v1-arxiv`

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

**Abstract:** ⚠ **El del paper NO cabe**: son 2954 caracteres y
arXiv corta en 1920 (*"abstracts longer than 1920 characters will not
be accepted"*, info.arxiv.org/help/prep.html). El del PDF se queda
como está; solo se abrevia el campo de metadatos. Versión abreviada
lista para pegar, **1900 caracteres**, ya en texto plano (sin
`\emph`, sin `` ``…'' ``, sin saltos de LaTeX; el math en `$…$` lo
renderiza arXiv):

> Cada párrafo posterior al primero empieza con **un espacio**: arXiv
> elimina los saltos de línea salvo que la línea siguiente empiece con
> espacio en blanco. Respetar esa sangría al pegar o se fundirá todo
> en un párrafo único.

```text
We study packings of annuli ("rings") of a common width into a disk, where a ring may nest inside the hole of a strictly larger one, a selection-oriented relative of the Recursive Circle Packing Problem. The two natural objectives, cardinality and contact area, genuinely diverge. For superincreasing radii (each exceeding the sum of all smaller ones) we prove that the descending greedy maximizes every positive, increasing, superadditive objective. Our main structural theorem shows more: the placement rule is irrelevant - any choice among feasible containers yields the lexicographically maximal feasible set, for containers of arbitrary shape and in every dimension. Both hypotheses are sharp: placement irrelevance holds for at most three rings and fails at four, and twin instances rule out every rule that is a function of the observable state.
 Write $\rho=\max_i(\sum_{j>i}r_j)/r_i$ for the violation of superincreasingness. The additive relaxation has universal threshold exactly $\rho=1$. In the geometric model we prove, with no tangency idealization, that the rigid four-ring family has infimum exactly the Tribonacci constant $T\approx1.83929$. Yet $T$ is not the global threshold: an explicit golden family breaks placement obliviousness at $\rho=\varphi+3\varepsilon$ for every small $\varepsilon>0$, proving $\tau\le\varphi<T$ for the geometric threshold $\tau$ and refuting the natural Tribonacci-threshold conjecture. The matching bound $\tau\ge\varphi$ remains conjectural; we prove it for pair profiles and outside an explicit heavy region.
 We also give a phase diagram for this divergence and split hardness into a geometric layer and a combinatorial (subset-sum) layer, of which superincreasingness eliminates exactly the latter. The main theorems carry complete written proofs; every computer-assisted closure carries an epistemic label and a script in the verification map.
```

Qué se recortó respecto del abstract del paper, por si hace falta
revisarlo: el detalle del programa hacia la conjetura (la curva de
anchura positiva con mínimo $13/7$, los umbrales de perfil en forma
cerrada, los muros de bloqueo con suelos de medias metálicas), la
frase sobre el valor áureo como «teorema en una dirección y abierto en
la otra», y la enumeración de las etiquetas epistémicas (proved,
box-certified, grid-swept, sampled). Ningún resultado desaparece: se
pierden matices, no enunciados.

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

## El endorsement — CONSEGUIDO

**2026-09-14: Ramón Flores (Universidad de Sevilla, Dpto. de Geometría
y Topología) concedió el endorsement de math.MG.** Fue el tutor del TFG
del autor; se le escribió el 2026-09-12 a su correo institucional y al
personal.

Historia, por si hiciera falta repetir el proceso algún día: las tres
primeras peticiones fueron emails en frío a especialistas de geometría
discreta (Lemmens, Fodor, Ambrus) y **ninguna obtuvo respuesta**. La que
funcionó fue la primera dirigida a alguien que conocía al autor. arXiv
lo dice en su propia ayuda y conviene creerlo: se pide a quien te
conoce.

**Corrección de un error que arrastraba esta hoja**: no hace falta que
el endorser haya publicado en math.MG. Matemáticas es **un único
dominio de endorsement** — *"most high-level subject areas … are
currently endorsement domains, with the notable exception of physics,
in which individual subject classes … are endorsement domains"*
(info.arxiv.org/help/endorsement.html). Basta con 4 envíos a cualquier
`math.*` entre 3 meses y 5 años atrás. Eso amplía muchísimo el conjunto
de candidatos posibles y es lo que hizo viable la vía de los contactos
personales.

El detalle de la cola de candidatos y los correos, en
`docs/email_endorsement.md` (fichero privado, fuera de git).

## Checklist final antes de subir

- [x] **Endorsement de math.MG concedido** (Ramón Flores, 2026-09-14).
- [x] `git tag v1-arxiv` apunta al commit del manuscrito que se sube:
      `c0d1fa2`, y `git diff v1-arxiv HEAD -- paper/` está **vacío**
      (el paper no ha cambiado desde el tag). Tag pusheado a origin.
- [x] `python paper/make_arxiv_bundle.py` → **VERIFICACION: OK**
      (regenerado el 2026-09-14; 1072.2 KB: `main.tex` + 3 PNG).
- [x] PDF comprobado: **60 páginas**, 1.4 MB — coincide con el campo
      Comments.
- [x] Abstract abreviado a 1900 caracteres (el del paper no cabía).
- [x] ~~Retomar el submission 8015141~~: **había desaparecido** de la
      cuenta (la lista de Article Submissions estaba vacía). Se abrió uno
      nuevo: **submission `8077477`**, https://arxiv.org/submit/8077477
- [x] **Formulario relleno y verificado el 2026-09-14**: licencia CC BY
      4.0, primary math.MG, cross-lists cs.CG y math.CO, MSC, comments,
      título, autor y el abstract de 1900. arXiv convirtió el acento del
      autor a TeX (`Mart'in`), que es lo normal.
- [x] **arXiv compiló con pdflatex (TeX Live 2025): SUCCEEDED, 60
      páginas, 1384162 bytes** — mismas 60 páginas que el PDF local. Log
      limpio: solo el aviso de shell-escape de epstopdf (no se usa eps) y
      una sustitución de fuente OMS/cmr/m/it -> cmsy. Cero referencias sin
      resolver. Conversión a HTML accesible: Success.
- [x] MathJax renderiza bien el math del abstract en el preview
      (rho, varphi, varepsilon, tau <= varphi < T).
- [x] **PDF del preview revisado por el autor y `Submit Article`
      pulsado el 2026-09-14.** La cuenta muestra `submit/8077477`,
      tipo `New`, status **`submitted`**.
- [x] **Esperar al anuncio.** Hecho: 2026-09-15. Mientras esté en `submitted` el envío
      sigue siendo editable (`Update`) y retirable (`Unsubmit`) desde
      https://arxiv.org/user. Los envíos se congelan a las 14:00 ET de
      cada día laborable y se anuncian a las 20:00 ET; math.MG pasa por
      moderación, así que puede tardar más de un ciclo.
- [ ] **Cuando llegue el arXiv ID**: anotarlo aquí, en el README del
      repo y en la memoria (`paper-arxiv-estado`).
- [ ] El PDF de arXiv (su compilador) puede diferir levemente:
      revisar el preview del envío antes de confirmar.
- [x] Tras el anuncio: arXiv ID anotado en la memoria, en los dos articulos
      del blog (`count-the-rings`, `proved-certified-swept-sampled`), en sus
      hilos de X y en `src/data/publications.ts` del repo personal-website
      (paper-arxiv-estado) y en el README del repo.
