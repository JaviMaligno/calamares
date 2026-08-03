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
corrigiendo portándolas (Apéndices B, C y D completos); (3) la longitud
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
- Overfull hbox: 0 en el log tras la pasada de maquetación.
- Fecha: se mantiene \today mientras el manuscrito evoluciona; se fijará
  al congelar.

## Desarrollo posterior al dictamen (debe conocerlo el revisor)

Tras ejecutar la revisión, el propio programa de verificación produjo un
resultado que OBLIGA a reescribir la tesis central del artículo, y así se
ha hecho:

1. **La conjetura del umbral de Tribonacci del manuscrito original es
   FALSA.** La familia áurea — sartén R = φ+1, radios
   {φ, 1, φ/2+2ε, φ/2+ε} — rompe la placement obliviousness en
   ρ = φ+3ε < T (Theorem thm:golden, con prueba exacta: rigidez S5,
   b₂(φ,1) = φ/2, criterios de par; verificación hostil independiente
   incluida la optimización sin asumir rigidez y el solver del repo).
   La versión enviada al primer dictamen conjeturaba umbral = T; el
   error era nuestro y lo encontró nuestro propio flujo adversario.
2. **Reinterpretación**: T es el suelo exacto del intercambio ANIDADO
   (todo el programa de las secciones 8–9 queda en pie, por encima de
   T > φ); el umbral global lo gobierna el intercambio a sartén y la
   nueva conjetura (conj:golden) es que vale exactamente φ, con la
   dirección ≥ demostrada para perfiles par salvo una micro-celda
   declarada (Theorem thm:DP, Apéndice) y la ≤ realizada por la familia.
3. Además se completaron, con verificación adversaria por resultado:
   Ψ_j sin asteriscos (lema de las hojas), el Teorema de las tres piezas
   (thm:DT3, con la esquina racional 17/7 y la corrección honesta sobre
   discos sólidos), y el suelo áureo del intercambio a sartén (thm:DP).
   Las actas de todas las rondas están en el repositorio.

El título pasa a «Golden and Tribonacci Thresholds». Entendemos que esto
es un cambio mayor de contenido respecto del manuscrito dictaminado; a
nuestro juicio lo refuerza (un contraejemplo exacto con familia
realizadora y un umbral conjetural áureo sustituyen a una conjetura
apoyada en búsqueda numérica), y todos los bloqueos del dictamen siguen
atendidos en la nueva versión.

## Verificación de la bibliografía

Además de lo pedido, las 15 entradas se cotejaron contra fuentes primarias
por dos pasadas independientes (DBLP, Springer, ScienceDirect, Wiley,
Dagstuhl, IJPAM): 15/15 correctas; único ajuste, el apellido completo
«Ozuna Espinosa». La nueva cita (Abrahamsen–Miltzow–Seiferth) se verificó
vía Crossref (FOCS 2020, pp. 1014–1021).

---

# Respuesta al SEGUNDO dictamen (2026-08-03)

1. **«T como suelo exacto del intercambio anidado» — ACEPTADO ÍNTEGRO.**
   Reformulado en abstract, introducción, encuadre de la sección 8 y
   conj:golden: «T is the exact floor of the rigid nested family, the
   proved floor of a hierarchy of nested templates, and the conjectured
   universal floor of nested exchanges». Ninguna frase presenta ya a T
   como umbral universal demostrado del anidado.
2. **Paso numérico en el teorema áureo — ACEPTADO y REFORZADO.** El
   testigo tiene ahora certificado algebraico exacto: la corona de
   {φ, σ, σ} existe ⟺ σ < 4(√5−2), vía sin B < sin 2A ⟺
   f(σ)(1+4φ²) < 4φ ⟺ σ(8φ+5) < 4φ³ con 8φ+5 = (2+√5)² y φ³ = 2+√5
   (en ε = 0: 4φ(√5−φ) = 4 > 1). La ventana de ε es explícita
   (ε* = mín((T−φ)/3, (φ/2−ω)/2, (4√5−8−φ/2)/2)) y la frase de
   cobertura es ahora un Corolario demostrado (cor:goldencover, con el
   reparto 2ε+η del exceso). Checks simbólicos en aureo.py [A].
3. **Apéndice del intercambio a sartén — ACEPTADO.** Renombrado
   «Partial golden floor for pan exchanges», enunciado por casos
   cerrados (i)–(iv) con la micro-celda como conjetura explícita, árbol
   j = 3 portado al texto, y la frase de apertura del apéndice
   cualificada.
4. **FKS Theorem 5.1 — ACEPTADO CON AGRADECIMIENTO y RETIRAMOS nuestra
   discrepancia anterior.** Verificado en la versión de revista (open
   access): el enunciado existe literalmente. Citado como
   [Theorem 5.1, FKS DCG 69 (2023)]; el problema abierto del disco se
   retira (queda solo la pertenencia a NP vs ∃R). Nuestra objeción
   anterior valía únicamente para el preprint.
5. **Padding de Equal-Cardinality Partition — ACEPTADO.** Sustituido
   por la reducción estándar correcta: {bᵢ+K} ∪ {K}×m con K > Σbᵢ y
   subconjuntos de cardinalidad exactamente m y suma mK+B₀.
6. **run_all y códigos de salida — ACEPTADO.** Los 8 scripts antiguos
   terminan ahora con sys.exit según su veredicto; el agregador
   reconoce además «HAY FALLOS» y «<-- REVISAR»; modo --quick (~8 min,
   omite cuadrado.py) y duración documentada; aureo.py sin restos de la
   familia simétrica (etiquetada como mecanismo); README corregido
   (umbral áureo conjeturado; dependencias numpy/scipy/sympy/
   matplotlib).

Presentación: figuras recolocadas junto a la sección de divergencia
(páginas 12–14, vía placeins/FloatBarrier); título cambiado al sugerido
por el revisor («Placement Rules, a Golden Counterexample, and a
Tribonacci Floor»).

---

# Respuesta al TERCER dictamen (revisión moderada)

1. **Notación de la prueba del intercambio a sartén — ACEPTADO ÍNTEGRO.**
   (Ry) se introduce ahora formalmente en el preámbulo del apéndice
   (σ₁+σ₂+X_y^rest > y−ω, ecuación etiquetada, derivada del Lema R sobre
   el agujero de y); la colisión de s resuelta con S₀ := σ₁+σ₂ y
   q := σ₂+X_{L′}; y o_i+o_k pasa a o_i+o_ℓ con i ≠ ℓ.
2. **Parametrización del umbral aditivo — ACEPTADO ÍNTEGRO** (el
   revisor tenía razón: el s libre no daba límite 1). Fijado s = r₁/2,
   R = 3r₁/2, w ∈ (r₁/4, r₁/2−δ), perturbación δ con r₃+r₄ = s+δ; las
   tres razones de cola se calculan explícitamente
   (1+δ/r₁, 1+2δ/r₁, →1) y ρ = 1+2δ/r₁ → 1.
3. **Anchura en el corolario de cobertura — ACEPTADO ÍNTEGRO.** Se fija
   ω = 0.3 y se verifican explícitamente las cinco desigualdades
   (s₁ < 1; certificado de corona; s₂ > 1−ω; s₁+s₂ > φ−ω;
   s₂ > s₁−ω con η < ω; s₁ ≤ φ−ω).
4. **Contrato de run_all — ACEPTADO ÍNTEGRO.** ocupantes/bloqueadores/
   bolsillo terminan ahora con sys.exit según su resumen; cuadrado.py
   separa los «FALLO de best fit» (fenómeno estudiado) de la
   verificación y sale con un booleano global real (identidades de X y
   b_□); el agregador reconoce además el patrón «=FALLO» de los
   resúmenes.
   Menores: hoja de ruta del README reescrita (conjetura áurea + suelo
   anidado), retirado el «listo para arXiv», definición formal del
   umbral τ = inf{ρ(I) : alguna ejecución voraz falla} en la sección de
   umbrales (y la conjetura enuncia τ = φ), y best/worst fit definidos
   en el enunciado de la irrelevancia de colocación.
