# Respuesta al dictamen (borrador para el revisor)

Registro punto por punto de cómo se ha tratado cada observación del
dictamen, incluyendo — marcadas con **[DISCREPAMOS]** — las decisiones que
contradicen la recomendación del revisor, con sus motivos. Criterio general
adoptado: donde el dictamen sugería retirar afirmaciones o acortar, se ha
preferido demostrar o completar («reforzar, no rebajar»).

## Sobre la recomendación general (partir en dos / acortar)

**[DISCREPAMOS — parcialmente].** El dictamen recomienda elegir entre
artículo corto cerrado o monografía, inclinándose por el corto. Optamos por
la **versión completa en una sola pieza**: cuerpo con enunciados formales y
apéndices con demostraciones íntegras. Motivos: (1) el programa es un todo
coherente — las secciones de anchura y contenedores genéricos usan la misma
maquinaria (bolsillos de Descartes, identidad del medio ángulo, colas) que
el suelo rígido, y partirlas duplicaría preliminares; (2) los resultados de
las secciones 8–9 no son «evidencia»: son teoremas con demostraciones
completas ya escritas (en los borradores del repositorio), y el defecto era
de *presentación* (no estaban portadas al paper), no de contenido — se está
corrigiendo portándolas (Apéndice B hecho; C y D en curso); (3) la longitud
resultante es la habitual en artículos de geometría discreta con apéndices
técnicos. Si tras completar los apéndices el conjunto no cohesionara, se
reconsiderará la partición.

## Bloqueo 1 (pruebas ausentes)

**Aceptado**, con la solución «completar», no «recortar»: Apéndice B
(suelo rígido, íntegro), Apéndice C (programa de anchura completo:
umbrales de perfiles, frontera cerrada + identidad κ, curva exacta del
grosor y Teorema 13/7 con familia genuina) y Apéndice D (contenedores
genéricos completos: Lema U, criterio de coronas, paredes de ocupantes,
Lema R + Teoremas B/B″, bolsillo doble + recta dorada, Ψ_j, Corolario S)
ya en el texto, con las secciones 8–9 del cuerpo referenciando cada
enunciado a su prueba. El «pending recursion patch» de
Ψ_j ha sido **demostrado** (no retirado): el lema de las hojas
(`docs/drafts/bolsillo.md` §4; en el paper, la Proposición «$\Psi_j$
ladder, unconditional» del Apéndice D) cierra el caso
general sin asteriscos, y los caveats correspondientes se han eliminado
del texto.

## Bloqueo 2 (hipótesis de v)

**Aceptado íntegro.** «positiva, estrictamente creciente, superaditiva» en
abstract, contribuciones, teoremas y generalizaciones; el contraejemplo
v ≡ −1 del dictamen se cita en un remark. Gracias por la caza.

## Bloqueo 3 (complejidad)

**Aceptado el diagnóstico; [DISCREPAMOS] en la receta de la cita.**

- El dictamen propone citar Fekete–Keldenich–Scheffer, *Discrete &
  Computational Geometry* 69:51–90 (2023), «Teorema 5.1», como prueba de
  NP-dureza para contenedor disco. **No hemos podido verificar que ese
  teorema exista con ese contenido**: (i) el preprint arXiv:1903.07908
  (única versión pública del artículo) no contiene ningún resultado de
  NP-dureza — su introducción atribuye la dureza a Demaine–Fekete–Lang
  *para contenedor cuadrado*; (ii) la survey de related work de los
  propios autores en SoCG 2021 (Fekete et al., «Packing Squares into a
  Disk», §1.1) tampoco menciona dureza para contenedor circular, cosa
  improbable si su propia versión de revista (enviada en ese periodo) la
  hubiera demostrado. Sin acceso a la versión de pago no citamos un número
  de teorema que no hemos visto. Si el revisor dispone del texto de ese
  Teorema 5.1, agradeceremos la cita exacta y la incorporaremos.
- En su lugar la sección se ha REFORZADO por vía verificable: (a) como
  nuestros teoremas valen para contenedor arbitrario, el modelo con sartén
  cuadrada y banda sin anidamiento contiene literalmente el problema de
  DFL ⟹ la capa geométrica del modelo es NP-dura sin citas dudosas;
  (b) el estatus del contenedor disco se declara abierto (Open Problem 3),
  con el contexto ∃R de Abrahamsen–Miltzow–Seiferth (FOCS 2020, verificado
  en Crossref); (c) la reducción de la capa aditiva ya no es «≈»: nueva
  Proposición con reducción completa desde Equal-Cardinality Partition
  (desplazamiento M = 3B, escala δ ∈ (w/3B, w/2B)) que controla la
  cardinalidad y domina la penalización −πw²|S| señalada por el revisor.

## Bloqueo 4 (novedad)

**Aceptado íntegro**: remark de posicionamiento (sistemas de independencia,
Edmonds y Korte–Hausmann citados en texto; mochila supercreciente, Gupte);
la novedad se reclama para el teorema geométrico de placement-obliviousness;
«No analogue was known» → «We are not aware of»; aviso temprano de que el
selection greedy es una cota de información con oráculo, no un algoritmo.

## Bloqueo 5 (repositorio)

**Aceptado casi íntegro**: URL en el paper (el commit exacto y el DOI de
Zenodo se fijarán al congelar la versión de arXiv), `run_all.py` como
comando único, `requirements.txt` corregido, clasificación
exacto-vs-numérico explícita (es la estructura de bloques de cada script),
y la garantía epistémica explicitada (pruebas escritas + simbólico exacto;
el flujo adversario es control de calidad, no garantía).

**Matiz [DISCREPAMOS en el énfasis]**: coincidimos en que la verificación
por agentes no es garantía matemática y así se declara; no obstante, los
informes adversarios se conservan y se citan como parte de la metodología
porque cazaron errores reales documentados (hipótesis ausente del Lema U,
una familia «bloqueada» que no lo estaba, el caso α < o₁), lo que es
información de auditoría valiosa para el lector, análoga a un log de
revisión interna.

## Editoriales

- Abstract: reducido a ~250 palabras. **[Matiz]**: por indicación del
  autor, la brevedad no es objetivo en sí; se ha priorizado que el abstract
  siga siendo fiel al contenido completo.
- Contribuciones partidas en «teoremas principales» / «programa».
- Umbral aditivo formulado como universal. Aceptado.
- Edmonds, Korte–Hausmann y Litvinchev: ahora citados en texto.
- Figuras: autocontenidas en `paper/figures/` (raíz lista para arXiv).
- «Draft» eliminado de la nota del autor.
- Overfull hbox de las gemelas y colocación de figuras: pendientes de la
  pasada final de maquetación (anotado).
- Fecha: se mantiene \today mientras el manuscrito evoluciona; se fijará
  al congelar.

## Verificación de la bibliografía

Además de lo pedido, las 15 entradas se cotejaron contra fuentes primarias
por dos pasadas independientes (DBLP, Springer, ScienceDirect, Wiley,
Dagstuhl, IJPAM): 15/15 correctas; único ajuste, el apellido completo
«Ozuna Espinosa». La nueva cita (Abrahamsen–Miltzow–Seiferth) se verificó
vía Crossref (FOCS 2020, pp. 1014–1021).
