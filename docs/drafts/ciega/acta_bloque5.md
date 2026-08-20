# Acta de revisión — BLOQUE 5 (referee externo, ronda ciega)

**Objeto:** `paper/main.tex`, secciones «The two objectives diverge: a phase diagram»
(994–1020), «Hardness decouples into two layers» (1021–1096), «Generalizations»
(1097–1132), «Open problems» (1133–1221) y «Verification map» (1222–1358).

**Método:** lectura íntegra de las cinco secciones; re-derivación propia de la
NP-dureza (Proposición `prop:additivehard` línea a línea, incluida la dureza de
Equal-Cardinality Partition) y de los puntos frontera del diagrama de fases
(analítica + re-cómputo numérico independiente de la retícula de `franja.py`);
contraste muestral del Verification map contra `code/` (existencia de 30+ scripts,
recuento estático de bloques en 28, ejecución en vivo de `h1.py`, `universal.py`,
`esquina.py` y `espfinal.py --solo A`); contraste de las afirmaciones de los Open
problems contra los enunciados reales de `thm:DP`, `thm:DPp`, `thm:DPr`,
`cor:DSpan`, `thm:D1written`, `thm:nestedwritten`, `thm:gapwritten`,
`conj:golden` y el párrafo «The honest residue» (3735–3773); inspección estática
de `lean/Calamares/Identities.lean`. El directorio `docs/` no se consultó
(protocolo de la ronda); las afirmaciones sobre los informes adversariales del
repositorio quedan por tanto **no contrastadas aquí** y se aceptan como
declaración.

---

## Veredictos por sección

| Sección | Veredicto |
|---|---|
| Phase diagram (994–1020) | **CONFIRMADA CON CORRECCIONES** — puntos frontera y áreas verificados; una frase-mecanismo con un off-by-one (H1) |
| Hardness (1021–1096) | **CONFIRMADA** — la reducción es hermética; re-derivada entera sin hallar grieta |
| Generalizations (1097–1132) | **CONFIRMADA** — etiquetas honestas («research program»); (a) contrastada contra los enunciados reales |
| Open problems (1133–1221) | **CONFIRMADA CON CORRECCIONES** — la frase final «is exactly» de `op:assembly` subdeclara el residuo frente al propio inventario del paper (H2) |
| Verification map (1222–1358) | **CONFIRMADA CON CORRECCIONES** — el muestreo cuadra salvo dos recuentos desactualizados (H3) y una convención de nombres que dificulta la auditoría (H4) |

**Veredicto global: CONFIRMADO CON CORRECCIONES.** Ningún hallazgo fatal.
Tres obligatorias, tres recomendadas, cinco menores.

---

## Hallazgos

### [OBLIGATORIA] H1 — Off-by-one en el mecanismo de la divergencia (líneas 999–1000)

Cita: «the divergence survives only marginally: small rings that fit $k$ times in
the pan but $k-1$ times in the large ring's hole».

Con $k-1$ pequeños en el agujero, la configuración con el grande tiene cardinal
$1+(k-1)=k$ — **empate** con los $k$ pequeños en la sartén, luego no hay
divergencia. La divergencia exige `n_pan >= n_hole + 2`, que es exactamente la
condición del script (`franja.py`: `B_cnt > A_cnt` con `A_cnt = 1 + n_hole`), y
es lo que hace la instancia mínima del propio párrafo: tres 4.2 en la sartén,
**uno** (= $k-2$) en el agujero del 9.0 (dos exigirían $s\le (b-w)/2 = 4 < 4.2$).
Verificación numérica independiente: recomputada la retícula completa de
`franja.py` (19 315 celdas divergentes), **cero** celdas divergentes con
`n_pan = n_hole + 1`.

**Corrección:** «…that fit $k$ times in the pan but at most $k-2$ times in the
large ring's hole» (o reformular: con $k-1$ en el agujero los objetivos empatan).

### [OBLIGATORIA] H2 — La frase final de `op:assembly` subdeclara el residuo (líneas 1186–1191)

Cita: «What remains for a full proof of Conjecture~\ref{conj:golden} is
\emph{exactly}: the occupant-count direction $j$ of the computational scaling
closures …, and written proofs replacing the remaining adversarially verified
computational closures.»

El propio paper, en «The honest residue» (3735–3773), inventaría **cinco**
partidas, y al menos dos no caben bajo ninguna de las dos categorías de la frase:

1. **Los topes de barrido** (residuo (ii)): $\omega\le1.6$ en la rama especular y
   $X_Y\le3$ en las cajas del motor son «sampling ceilings, not derived walls» —
   fuera de esas cajas **no hay cierre computacional que reescribir**: hay
   dominio sin cubrir.
2. **El canal ocupante** (residuo (iii) y línea 3609–3611: «what remains of the
   channel is the mid band at tower depth $\ge2$ and the structural exclusion of
   $u$'s content»): la banda media en torres de profundidad $\ge2$ **queda
   abierta**, ni siquiera cerrada computacionalmente; es además la única pieza
   model-conditional de la especular, condición que la conjetura (incondicional
   sobre $\rho<\varphi$) no puede heredar en silencio.
3. Menor pero en la misma línea: el asterisco de optimización (residuo (v)) y el
   barrido muestreado / rama de dominación no ejercitada del converso F3
   (residuo (iv)) — este último defendible por la vacuidad de la celda realista,
   pero la frase «exactly» no deja hueco ni para decirlo.

La misma sobre-declaración se repite, en eco, en `conj:golden` (682–683:
«leaving as the numeric core the occupant-count direction … alone») y en su
«every residual cell of the exchange assembly is closed computationally» (673),
que choca con «what remains of the channel is the mid band…» (3609).

**Corrección:** sustituir la enumeración «is exactly: …» por una remisión
explícita al inventario del residuo («exactly the five-item inventory of the
honest-residue paragraph, Appendix~\ref{app:campaign}») o incorporar los ítems
(ii) y (iii) a la frase; alinear la cláusula final de `conj:golden` con ello.
Los criterios 1–2 y 5 del protocolo (etiquetas honestas; dominios reclamados =
barridos; fidelidad de los Open problems) exigen este ajuste: el resto del paper
es escrupuloso en esto y la frase «exactly» es el único punto donde el residuo
declarado se queda corto respecto del residuo real.

### [OBLIGATORIA] H3 — Dos recuentos desactualizados en el Verification map

1. **`espfinal` «(5/5 …)» (línea 1288):** el runner del script ejecuta por
   defecto `etiquetas = list("ABCDFE")` — **seis** bloques (A, B, C, D, F, E;
   `code/espfinal.py` línea 623). Una corrida verde completa reporta 6/6, no
   5/5. (Verificado además en vivo: `--solo A` corre y devuelve verde.)
   Presumiblemente el bloque F se añadió tras redactar el mapa.
2. **«Its forty-two theorems» del desarrollo Lean (línea 1322):**
   `lean/Calamares/Identities.lean` contiene **45** declaraciones `theorem`
   (recuento estático; `sorry` solo aparece en un comentario; sin
   `native_decide`, patrón `decide +kernel` — coherente con el resto del
   párrafo).

**Corrección:** actualizar ambos números. El mapa es el instrumento de
auditoría del paper; sus recuentos deben ser exactos.

### [RECOMENDADA] H4 — Tres entradas del mapa nombran drafts, no scripts

«\texttt{suelo\_rigido}», «\texttt{perfil\_tres}» y «\texttt{cuatro}» no existen
como ficheros en `code/`; los scripts reales son `rigido.py` (implementa
`suelo_rigido.md`; sus 7 unidades V1–V8 con V2V3 fusionado sí cuadran con los
«7 blocks» declarados), `tresk.py` (`perfil_tres.md`) y `cuatrok.py`
(`cuatro.md` — aquí el mapa sí añade «(\texttt{cuatrok} 5/5 blocks)»). Un lector
que busque `suelo_rigido.py` no encuentra nada. **Corrección:** dar siempre el
nombre del fichero de `code/`, con el draft entre paréntesis si se quiere.

### [RECOMENDADA] H5 — «$n$ calls to a sibling-packing feasibility oracle» (líneas 1090–1091)

La reducción es real pero el recuento y la cita son imprecisos: (a) el voraz
debe decidir, por anillo, si **algún** contenedor vigente lo admite — hasta
$O(n)$ consultas de empaquetamiento de hermanos por anillo, $O(n^2)$ en total
(o $n$ llamadas a un oráculo más fuerte «¿admite la colocación actual a $i$?»);
(b) la descomposición en consultas de hermanos por contenedor viene de
Theorem~\ref{thm:oblivious} (el voraz con regla arbitraria), no de
Theorem~\ref{thm:selection} (cuyo oráculo es de factibilidad de conjuntos).
**Corrección:** precisar el oráculo y el conteo, y citar `thm:oblivious`.

### [RECOMENDADA] H6 — `cor:DSpan` como «a complete proof» en `op:assembly` (línea 1156)

El argumento a-fortiori del corolario sí es una prueba escrita, pero su segunda
afirmación («the residual cell of the case assignment over $S^{+}$ is again
$\{p\ge4,\sigma_1+M\le1,j\ge3\}$») descansa en la exhaustividad del case
assignment verificada por muestreo («$200\,000$ sampled instances, zero
unassigned», líneas 3066–3068). La partición de casos parece tautológica sobre
desigualdades complementarias y probablemente demostrable en dos líneas, pero
tal como está escrita, «a complete proof» sin matiz sobredeclara respecto del
propio texto de la prueba. **Corrección:** o probar la exhaustividad
simbólicamente, o matizar la etiqueta en `op:assembly`.

### [MENOR] H7 — Bloques sin gate dentro de los recuentos «all green»

`universal.py` bloque E es exploración declarada «SIN ESTATUS» que siempre
devuelve OK, y varios scripts (p. ej. `espfinal.py` bloque A) tienen bloques
`[ENUNCIADO]` que son declaraciones, no verificaciones. Los scripts lo etiquetan
honestamente; el mapa, al reportar «5/5 blocks, all green», no distingue. Una
frase en el preámbulo del mapa («some blocks are declared explorations or
statements of convention and cannot fail») lo resolvería.

### [MENOR] H8 — Hipótesis ociosa $K>\sum b_i$ (línea 1061)

En la dureza de Equal-Cardinality Partition, la suma de todo $m$-subconjunto es
$mK+\sum_{\text{chosen}}b_i$ para **cualquier** $K\ge1$; la condición
$K>\sum_i b_i$ no se usa en el argumento. Inofensiva; eliminarla o justificarla.

### [MENOR] H9 — «The minimal instance» (línea 1000)

Minimal es cierto en número de anillos (con 3 anillos los cardinales empatan
siempre: $b$+1 anidado vs. 2 sueltos), pero el texto ni define la métrica ni lo
argumenta. Sugerencia: «A minimal instance (four rings; three never diverge)».

### [MENOR] H10 — `op:oracle` sin el cualificador de dominio (líneas 1194–1198)

Tal como está enunciado, bajo radios superincrecientes la respuesta es
trivialmente afirmativa (Sección~\ref{sec:hardness}); el problema abierto es
para radios arbitrarios. Añadir «for arbitrary (non-superincreasing) radii».

### [MENOR] H11 — Generalizations (e): el testigo es solo $v\equiv1$

«weighted counts and concave values fall outside and, by
Proposition~\ref{prop:count}, genuinely so»: la proposición atestigua el fallo
solo para $v\equiv1$ (que es a la vez un weighted count y cóncava). Como frase
de frontera de clase es defendible; como afirmación sobre toda la familia,
sobrelee el testigo. Matiz opcional.

---

## Verificado en positivo

**Hardness (re-derivación completa, criterio 7).**
- Dureza de Equal-Cardinality Partition: correspondencia $m$-subconjuntos de
  suma $mK+B_0$ ↔ subconjuntos de suma $B_0$ comprobada en ambas direcciones
  (el padding con copias de $K$ siempre cabe).
- `prop:additivehard`: banda sin anidamiento verificada
  ($r_i\ge\delta(3B+1)>w$ por $\delta>w/3B$; $r_{\max}-r_{\min}\le\delta(2B-1)<w$
  por $\delta<w/2B$); factibilidad aditiva $=\sum_S r_i\le R^+$ legítima en el
  modelo de `thm:additive` (enunciado contrastado: «a set of siblings fits iff
  their radii sum to at most the container capacity»); ida: $s=n/2$, $t=B$
  alcanza $\Theta$ con igualdad y es factible con igualdad; vuelta: $s>n/2$
  infactible por $(s-\tfrac n2)M\ge M>B\ge B-t$; $s=n/2-q$ imposible — la
  cadena $2\delta(qM+B-t)\ge2\delta(qM-B)\ge2\delta q(M-B)=4\delta qB>wq$
  re-derivada paso a paso (usa $t\le2B$, $q\ge1$, $M=3B$, $\delta>w/4B$
  implicada); $s=n/2$ fuerza $t=B$ por el par área/factibilidad. La etiqueta
  «weakly NP-hard» es la correcta (números polinomiales en los valores;
  $\delta$ racional representable), y es coherente con la pregunta
  pseudopolinomial de `op:misc`.
- Capa geométrica: la especialización a sartén cuadrada es legítima porque
  `thm:selection`/`thm:oblivious` están enunciados y probados para contenedor
  arbitrario en $\R^d$ (enunciados leídos y confirmados); cita
  Demaine–Fekete–Lang (3-Partition, círculos en cuadrado) apropiada; marco
  $\exists\R$ (Abrahamsen–Miltzow–Seiferth, FOCS 2020) apropiado; el
  Teorema 5.1 de la versión journal de Fekete–Keldenich–Scheffer (DCG 69,
  2023) se acepta sobre la cita (no verificable offline en esta ronda) — el
  paper es además transparente sobre su procedencia («we thank the referee»).
  El uso del teorema de densidad crítica (área $\le$ mitad ⇒ empaqueta, $1/2$
  ajustado) coincide con el resultado citado.

**Phase diagram (puntos frontera, criterio 7).**
- Áreas de la instancia mínima recomputadas: $a(9)+a(4.2)=24.4\pi\approx76.65$
  («76.7» ✓), $3a(4.2)=22.2\pi\approx69.74$ («69.7» ✓); coexistencia $9+4.2>10$
  bloqueada ✓; tres 4.2 caben en la sartén ($4.2<0.4641\cdot10=4.641$) ✓; solo
  uno en el agujero de 8 ✓.
- Borde superior re-derivado analíticamente: para $\rho>0.4641R$ solo caben 2 en
  la sartén y la divergencia con $n_{\rm pan}=2$ exige $n_{\rm hole}=0$
  ($b<\rho+1$) y a la vez $a(b)>2a(\rho)$ ($b>2\rho-\tfrac12$) — incompatibles;
  numéricamente, máx. $\rho$ divergente $=4.64$ en retícula 0.01 contra
  $4.6410$ ✓ «exactly the three-circle threshold».
- Robustez del generador: el script ignora configuraciones mixtas (grande +
  pequeños al lado en la sartén), pero **cero** celdas divergentes tienen
  $b+\rho\le R$ en la caja barrida — la omisión nunca muerde ✓. La escalera usa
  solo óptimos demostrados $n\le10$ (Pirl 1969, GLNO 1998; $\rho/R\ge0.265>
  Q_{10}=0.2623$ mantiene el barrido dentro del rango probado) y las citas
  correspondientes están en la bibliografía ✓. Ambos ficheros de figura existen
  en `paper/figures/` ✓.

**Generalizations.** (a) contrastada con los enunciados de
`thm:selection`/`thm:oblivious` y su remark (contenedor arbitrario, $\R^d$,
«acts inside the vacated ball») ✓; sharpness declarada disk-specific y abierta
para cuadrado/$\R^3$ — honesto ✓; (b)–(d) etiquetadas como programa, sin
reclamo de prueba ✓.

**Open problems (consistencia interna, criterio 5).** El recuento de celdas de
`op:assembly`(a) casa con los enunciados reales: `thm:DP` (i)–(iv) deja fuera
exactamente el pivote sólido $\omega\ge1$, $j\ge3$, que `thm:D1written` cubre
(«including the solid pivot», con la rama $\sigma_2>\varphi-1$ cerrada por masa
y presupuesto paramétrico) ✓; los regímenes light/nested/heavy-large/heavy-$\Psi_B$
citados son (i)–(iv) de `thm:DPp` y «$p=3$ with one occupant at every width» es
su (iii)+(v) ✓; la celda pesada $\{p\ge4,\sigma_1+M\le1,j\ge3\}$ es la de
`thm:DPr` ✓; «the entire nested template, every $j$» casa con
`thm:nestedwritten` ($j\ge2$) + `thm:gapwritten` ($j\le1$) y el texto puente
(3274–3278) ✓. Re-derivaciones puntuales: el cruce
$2b(A)A=1+2b(A)$ factoriza como $(A^2-A-1)(2A+1)$ — expandido a mano,
$2A^3-A^2-3A-1$ ✓; $P(\varphi)=-1$ vía $\varphi^3=2\varphi+1$ ✓;
$\pi+4\arcsin(1/\sqrt3)\approx5.603<2\pi$ ✓;
$5t_0=\varphi-\beta^*$ con $\beta^*=(9-\sqrt5)/8$ ✓; $\varphi(3-\varphi)=\sqrt5$,
$\varphi^2+\varphi+1=2\varphi^2$, $\varphi(4-\varphi)=3\varphi-1$ ✓; el cúbico
áureo $r^3+(2-\varphi)r^2+(2-\varphi)r-\varphi$ expandido a mano ✓;
$q(9/10)=171/271$ y $\varphi-9/10-171/271=0.0870<25/83=0.3012$ ✓.

**Verification map (muestreo).**
- Existencia: los ~30 nombres de script citados existen en `code/` (con la
  salvedad de nombres H4).
- Recuentos estáticos de bloques contrastados en 28 scripts: `insercion` 7 ✓,
  `puertocii` 7 ✓, `ensamblaje` 6 ✓, `bloqueadores` 6 ✓, `bolsillo` 6 ✓,
  `rstar` 6 ✓, `batalla2` 6 ✓, `insercionanidada` 6 ✓, `espcanal` 5 por defecto
  (A–E; el bloque auxiliar M no corre) ✓, y 5 en `microcelda`, `zigzag`,
  `escala`, `gaplemma`, `f3converso`, `espcanalp`, `esppesada`, `espkp`,
  `espxy`, `espvals`, `auditcolas`, `f3vacio`, `f3cierre`, `r2bmulti`,
  `r2bcert`, `areduccion`, `arcolp`, `bolsillos`, `compactacion`,
  `colageometrica`, `coronaagujero`, `optimizacion`, `repack`, `coronacolas`,
  `coronanidada`, `aureo`, `striple`, `corona`, `ocupantes`, `cuatrok` ✓ —
  **única discrepancia: `espfinal` (H3)**.
- Ejecuciones en vivo: `h1.py` → 5/5 verde (mapa: 5/5 ✓; margen E1
  $+8.79\cdot10^{-5}>0$ en la dirección correcta), `universal.py` → 5/5 verde ✓,
  `esquina.py` → 5/5 verde ✓ (E3 decrece a $13/7$ por arriba, dirección
  correcta), `espfinal.py --solo A` → verde.
- Lean: sin `sorry` (solo en comentario), sin `native_decide`, patrón
  `decide +kernel` sin mathlib — todo coherente con el párrafo del mapa; el
  alcance declarado («the geometric layer proper … is *not* formalized») es una
  etiqueta ejemplar de honestidad; único defecto el recuento 42≠45 (H3).

**Tolerancias y gates (criterios 3–4).** En los scripts ejecutados las
comparaciones frontera van en la dirección conservadora (mínimos positivos
reportados con signo, límites alcanzados por el lado correcto); no encontré
gates tautológicos más allá de los bloques-declaración de H7, que los propios
scripts etiquetan.

---

*Referee externo, ronda ciega — Bloque 5. Basado exclusivamente en
`paper/main.tex`, `code/` y `lean/`; `docs/` no consultado.*
