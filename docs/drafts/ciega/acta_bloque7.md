# Acta de revisión ciega — BLOQUE 7
## Apéndice «The corona-versus-tails campaign: closure of the residual cells» (paper/main.tex, líneas 3034–3774)

**Revisor**: referee matemático externo (ronda ciega, criterios de rigor propios, sin líneas de ataque suministradas).
**Fecha**: 2026-08-20.
**Contexto usado**: paper/main.tex completo (cuerpo + verifmap + Lean layer descrito), código en `code/` y `lean/`. `docs/` NO consultado (prohibido).
**Scripts ejecutados** (uno a la vez): `insercion.py` (completo, 7/7), `optimizacion.py` (completo, 5/5), `colageometrica.py` (completo, 5/5), `f3converso.py` (5/5 con `CC_ITER=600`; el run por defecto >40 min, abortado — ver Adenda). Inspección estática adicional de `coronacolas.py`, `gaplemma.py`, `espkp.py`, `espcanal.py`, `r2bmulti.py`, `escala.py`, `zigzag.py` y `lean/Calamares/Identities.lean`.

---

## VEREDICTO

**CONFIRMADO CON CORRECCIONES.** El apéndice es, en su conjunto, un documento epistémicamente serio: la taxonomía declarada en el preámbulo (teorema escrito / identidad exacta / certificado por subdivisión / vacuidad / barrido muestreado / model-conditional) se aplica de forma consistente en la gran mayoría de los enunciados, las direcciones de tolerancia de los certificados son las correctas (esquinas pesimistas, re-verificación en float del gap del solver, desigualdades cerradas que certifican EN la tangencia), y «The honest residue» es un inventario esencialmente completo y no inflado: nada de lo listado como residuo está cerrado, y no encontré ningún enunciado muestreado/condicional del apéndice que el inventario omita en sustancia. Las ejecuciones reproducen los márgenes y supremos citados con exactitud (4.7225/5.2644, márgenes 1.56/1.02; sup G ≤ 5.25 con márgenes 0.9832/0.1924; sup real 5.2115 con gap cero en la familia {2φ,2,2/φ}+D_m; control de honestidad del B&B que se atasca exactamente en 5.2115). Las identidades áureas citadas se verifican a mano y contra el Lean layer (golden_pi_trio, strong_breathing, golden_reduction_threshold, diametral_pocket_golden — todas presentes, `decide +kernel`).

Hay dos hallazgos OBLIGATORIOS: un gate que no puede fallar citado como evidencia en la prueba del Corolario DSpan (el chequeo de exhaustividad de coronacolas bloque C es un complemento booleano tautológico), y tres recuentos del cierre de la celda pesada (185k instancias, 4.284 esquinas, re-validación euclidiana 1500/1500) cuya procedencia no es trazable desde los scripts citados. Ninguno de los dos toca la solidez matemática de los cierres (la exhaustividad del reparto de casos es un hecho lógico finito trivialmente demostrable; la celda pesada está además SUPERADA por thm:D1written), pero ambos violan el estándar de honestidad que el propio apéndice se impone.

---

## HALLAZGOS

### [OBLIGATORIA] H1 — Gate que no puede fallar citado como evidencia en la prueba de Cor. DSpan
**Cita** (líneas 3066–3068): «The case assignment of Theorems~\ref{thm:DPp}--\ref{thm:DPr} is exhaustive over $S^{+}$ ($200\,000$ sampled instances, zero unassigned; script \texttt{coronacolas}, block C).»
**Hecho verificado**: en `code/coronacolas.py`, `bloque_C()` (líneas 518–578), la condición residual comprobada — `not (len(Sp) >= 4 and s1 + M <= 1.0 and j >= 3)` — es exactamente el complemento booleano de los `continue` que la preceden: tras los guards, toda instancia superviviente satisface len≥4 ∧ s1+M≤1 ∧ j≥3 *por construcción lógica*. `sin_caso` no puede incrementarse jamás; el bucle de 200.000 muestras es infalsable y no aporta evidencia alguna. (Verificación: los guards cubren len=3 con j∈{1,2,≥3}, len≥4 con j≤2, y len≥4 con s1+M>1 vía H2-PsiB (j≥2) y C2 (j=1) — el complemento es la celda D1 por trichotomía, un hecho de lógica de casos finita.)
**Impacto en solidez**: nulo — la exhaustividad ES verdadera y demostrable en tres líneas de enumeración de casos. Pero presentarla como «200.000 sampled instances, zero unassigned» dentro de un entorno `\begin{proof}` viste un hecho lógico de evidencia computacional vacua, y es precisamente el patrón (gate tautológico) que las propias actas del proyecto han cazado en otros scripts (cf. el gate lp_ok=cajas_ok de espcanalp mencionado en el verifmap).
**Corrección**: sustituir el paréntesis por la enumeración lógica («exhaustive by the case trichotomy on $(|S^+|, j, \sigma_1+M)$») o convertir el chequeo en falsable (contrastar cada guard contra la hipótesis real del teorema que lo cubre). El Open Problem op:assembly llama a DSpan «a complete proof» — con la corrección lo sería sin asterisco.

### [OBLIGATORIA] H2 — Recuentos no trazables en el cierre computacional de la celda pesada
**Cita** (líneas 3112–3114): «the heavy cell $\{p\ge4,\sigma_1+M\le1,j\ge3\}$ of Theorem~\ref{thm:DPr} ($j\le5$, $p\le6$ swept, $185$k instances plus $4\,284$ corners, Euclidean re-validation $1500/1500$)».
**Hecho verificado**: `coronacolas.py` (el script citado para este cierre, junto con `coronanidada`) barre efectivamente j∈{3,4,5}, p∈{4,5,6} (bloque B) — «j≤5, p≤6 swept» es correcto — pero NO imprime ni computa recuento de instancias aceptadas, ni «corners», ni ninguna re-validación euclidiana: `grep -n "185\|4284\|1500\|euclid" coronacolas.py` no da nada, y la salida del bloque B es solo el máximo por (j,p). Los tres números (185k, 4.284, 1500/1500) no son reproducibles desde los scripts emparejados; su procedencia aparente es el informe adversarial de docs/ (fuera del paper y de mi ámbito permitido). Nota: `insercion.py` E(b) imprime un stress euclidiano de 1453 casos — ni el número ni el script coinciden con la cita.
**Impacto**: la celda está SUPERADA por thm:D1written (línea 3194: «This supersedes the computational closure»), así que nada de la cadena lógica descansa aquí; pero el apéndice promete «the swept ranges are stated» y recuentos contrastables, y estos tres no lo son.
**Corrección**: o hacer que `coronacolas` imprima esos contadores (instancias aceptadas, esquinas deterministas, re-validación euclidiana), o citar el script que efectivamente los produce, o eliminar los números y dejar «j≤5, p≤6 swept».

### [RECOMENDADA] H3 — «deficit 0.0» frente al gate real π + 2·10⁻³
**Cita** (líneas 3110–3112): «the constructive corona at $R=R_{\mathrm{lb}}$ succeeds with \emph{uniform tangent duality} (deficit $0.0$; the boundary placement is tangent, hence legal)».
**Hecho verificado**: en `coronacolas.py` bloques B y D el gate es `peor <= PI + 2e-3` — se aceptan excesos numéricos de hasta 2·10⁻³ sobre π atribuidos a la tolerancia de bisección de R_lb (el propio script lo etiqueta «pi + O(tolerancia de biseccion)»), con la sonda complementaria «v decrece en R» (mín > 0 en 200 sondas) para descartar que la lámina tenga grosor. La dirección de la tolerancia es la delicada: un exceso genuino de 10⁻³ pasaría el gate.
**Atenuante**: en la dualidad exacta v=π EN R_lb es una identidad (tangencia), y la sonda de decrecimiento en R cubre el interior; el argumento es correcto.
**Corrección**: declarar la tolerancia en el paper — «deficit $0.0$ (within the $2\cdot10^{-3}$ bisection tolerance of $R_{\mathrm{lb}}$; $v$ strictly decreases in $R$)» — en lugar del 0.0 idealizado.

### [RECOMENDADA] H4 — «certified maximization»: un término, dos estándares
**Citas**: «a certified directed maximization» (3188–3189, thm:D1written), «certified maximization with deterministic corners» (3224–3225, thm:nestedwritten), «a certified maximization» (3269, thm:gapwritten), «certified over a deterministic corner mesh» (3648, esquina 1.082).
**Hecho verificado**: `gaplemma.py` define honestamente su «maximizacion certificada» como «el estandar de thm:DPr» — es decir, grid-plus-refinement con criterio por instancia exacto, NO aritmética de intervalos. El residuo (v) admite que el asterisco de optimización de los barridos de familia acotada sigue abierto SALVO para los presupuestos de sombras (donde `optimizacion.py` sí es un B&B certificado — verificado en ejecución: cotas de esquina por monotonía, poda exacta, control de honestidad). El texto usa «certified» para ambos estándares sin distinguirlos, y la esquina sintética 1.082 «certified over a deterministic corner mesh» es directamente un oxímoron (una malla es muestreo).
**Corrección**: definir una vez en el preámbulo del apéndice qué significa «certified maximization» (el estándar thm:DPr, con su asterisco heredado por el residuo (v)) y reservar «certified» sin calificar para los B&B de cotas válidas por caja (optimizacion, espkp, espcanal, espcanalp, espfinal, r2bcert/r2bmulti); en 3648, «evaluated over a deterministic corner mesh».

### [RECOMENDADA] H5 — «the light channel is closed entirely» sin su calificador de dominio in situ
**Cita** (líneas 3572–3588): «the light channel is \emph{closed entirely}: the exact tie $x=r_m$ ... the band $x\in(r_m,2/\varphi)$ ... the high band certifies by subdivision ($79\,277$ boxes ...) and above the node wall the cell unblocks outright».
**Problema**: leído aisladamente, el reparto en bandas parece cubrir todo x — pero el propio apéndice dice tres líneas después (3609–3611) y en el residuo (iii) que queda «the mid band $x\in[2/\varphi,\sigma_2+\omega+X_x)$ at tower depth $\ge2$»: el «entirely» vale en el contenedor $v$ y en el corte de torre de profundidad 1, no en torres más profundas. El calificador existe en el paper pero llega tarde; un lector que cite 3572 sin 3609 sobre-lee el cierre. (`espcanal.py` declara la banda alta como [1.05, techo], consistente con el solapamiento redundante de las bandas (ii)/(iii).)
**Corrección**: «the light channel is closed entirely \emph{on $v$ and on the depth-one tower cut}: ...» en 3572.

### [RECOMENDADA] H6 — Recuentos atribuidos a rondas adversariales, no reproducibles desde script+paper
**Citas**: «domination unbroken under ${\sim}45$k families» (3449, colageometrica); «zero counterexamples under 55k independent adversarial instances» (3420–3421, coronaagujero); «$20\,000$-instance fuzz» (3607), «$1\,460$ directed tests» (3633) y análogos.
**Hecho verificado**: la ejecución de `colageometrica.py` con parámetros por defecto da 14.976 + 8.000 = 22.976 familias en los bloques de dominación — no ∼45k; `coronaagujero.py` no contiene ni imprime «55k» (grep vacío). Estos recuentos provienen de las rondas adversariales (docs/, fuera del paper y de mi ámbito permitido): desde el material publicado no son contrastables.
**Corrección**: distinguir tipográficamente los recuentos de script (reproducibles con el repo) de los recuentos de ronda (figuras de informe), o hacer que los scripts reproduzcan los segundos. Tal como está, un lector que ejecute los scripts obtendrá números distintos de los citados sin explicación.

### [MENOR] H7 — El párrafo del converso no cita su script
El cierre exacto del converso «gap ⇒ cell» (3678–3701: peeling, dicotomía par-apilable/dominación, 4.000 familias / 1.266 gaps) no nombra a `f3converso` — la lista de scripts que le sigue (3702) acredita solo a f3cierre/auditcolas/f3vacio, que respaldan el párrafo ANTERIOR (la vacuidad near-equal-tops). `f3converso` solo aparece en el verifmap (línea 1303). Añadir «(script \texttt{f3converso}, 5/5)» al final del párrafo del converso.

### [MENOR] H8 — Gramática/estilo
- Línea 3384: «those theorems use of the configuration exactly four things» — falta puntuación o reordenar («those theorems use, of the configuration, exactly four things» / «use exactly four things of the configuration»).
- Línea 3097: «$p(\varphi,1;\varphi+1)=\varphi/2$» se enuncia dos veces en el apéndice (3097 y 3539) con roles distintos; correcto ambas, pero la segunda podría remitir a la primera.

### [MENOR] H9 — «kernel-checked in Lean» para el trío-π: el kernel comprueba el núcleo algebraico
**Cita** (3311–3314): «one more exact golden identity, kernel-checked in Lean: $\theta(\varphi,1/\varphi)+\theta(1/\varphi,1)+\theta(1,\varphi)=\pi$ at $R=2\varphi$».
**Hecho verificado**: `lean/Calamares/Identities.lean:394` (`golden_pi_trio`) demuestra por `decide +kernel` las dos igualdades algebraicas en $\mathbb{Q}[\sqrt5]$ a las que la identidad de adición de senos reduce el enunciado (más $7\sqrt5>15$), con la reducción y la desambiguación de rama documentadas en el docstring pero fuera de Lean — coherente con la política declarada del repo (la capa Lean cubre «the exact-certificate layer»; la geometría queda fuera a propósito). La frase del paper es defendible pero un lector estricto entendería que el enunciado trigonométrico entero está formalizado. Sugerencia: «whose algebraic core is kernel-checked in Lean».

### [MENOR] H10 — Tolerancia del certificador de gaps no declarada en el paper
`f3converso.py` usa `TOL_GAP = 2e-6` para certificar un gap y declara honestamente en su bloque E que «la banda de gaps (1e-9, 2e-6] no barrida se declara». El paper (3697: «every one of the $1\,266$ certified gaps») no menciona el umbral. Cubierto genéricamente por «its supporting sweep remaining sampled» (residuo (iv)), pero convendría citar el umbral de certificación de gap junto al recuento.

---

## VERIFICADO EN POSITIVO

**Ejecuciones (recuentos y márgenes contra el texto):**
1. `insercion.py` — 7/7. Esquina j=3: presupuesto σ₂ = **4.7225** (margen **1.5607**) y segunda inserción w* = **5.2644** (margen **1.0188**) — el texto dice «4.7225 and 5.2644 against 2π, margins 1.56 and 1.02» (3184–3185): coincidencia exacta. Uniformidad en j (3..14, máx 4.7225), monotonía exacta en o₂, bañera en o₁ con límite π, regímenes A5 exactos (4−2φ>0), control A4 que refuta la versión mural ingenua (la que el texto dice que la ronda adversarial refutó y reparó, 3189–3191 — confirmado), rama F con vacuidad σ₂>φ/2 por masa y F2 = (1+Σ)(1+φ)/φ²=1+Σ.
2. `optimizacion.py` — 5/5. **sup G ≤ 5.25 CERTIFICADO** (cotas finales 5.2499, 4.495/5.126 cajas, modos 1 y 2); margen **2π−0.05−5.25 = 0.9832** ✓ «0.98»; cola t₂>1000 certificada con cota 6.0408 < 2π−0.05, margen **0.1924** ✓ «0.19»; control de honestidad: objetivo 5.20 NO certifica, atascado exactamente en **5.2115** ✓ (3730–3733); control E(a): sin t₂≥1+Σ la navaja da 6.93>2π ✓ «6.37→» (ver colageometrica).
3. `colageometrica.py` — 5/5. Identidades (S)/(D)/(N)/(M) exactas en sympy; dominación G ≥ presupuesto real con 0 violaciones (14.976 + 8.000 familias); sup del box = **5.2115** con gap **0 exacto** en la familia real {2φ, 2, 2/φ} + D_m ✓ (3437–3440); sin el vínculo t₁: 6.3734 > 2π ✓ «6.37» (3437); navaja áurea n=2 con razón idénticamente 1 ✓ frontera declarada (3441–3445); límites por fórmula (t₂→∞: 5.5237; t₁→∞: π) ✓.
4. `f3converso.py` — 5/5 con `CC_ITER=600` (el run por defecto excede el presupuesto de tiempo; ver adenda): 600 familias / 183 gaps / 183 en la celda / 0 fuera / 183 por la vía apilable — cualitativamente idéntico al 4.000/1.266 del texto.

**Identidades verificadas a mano (todas exactas):**
- h(R−a,R−b) = 1−2f(a)f(b) (álgebra directa, 3080);
- Descartes con pared: k_p = k_a+k_b−1/R+2√(k_ak_b−(k_a+k_b)/R) (3087) y anulación idéntica del discriminante en R=a+b (3454, 3279);
- el punto crítico áureo: f(φ)f(1)=1 y (f(φ)+f(1))f(φ/2)=1 en R=φ+1 (3099);
- bolsillo 1/(1/o₁+1/o₂−1/(o₁+o₂)) = φ en (2φ,2,2φ+2) (3455–3457);
- p(u)=u(u+1)/(u²+u+1) creciente, p(φ)=φ/2 — la tangencia del cap s'=φ/2 con el bolsillo áureo en Σ=φ, α=φ (3281–3289);
- t₂ ≥ (1+Σ)(1+φ)/φ² = 1+Σ (3221); o ≥ φ(1+Σ) en near-ties vía 1/(φ−1)=φ (3109);
- φ(3−φ)=2φ−1=√5 y √5−(φ−1)=φ (respiración fuerte, 3410–3413);
- t₀=(φ−1)/4=1/(4φ), β*=(9−√5)/8, 5t₀=φ−β*, 4t₀=φ−1 (3491–3495);
- φ²+φ+1=2φ², anchura del sliver 1/(2φ²), p(φ,1;φ+1)=φ/2 (3537–3540);
- β>1/2 del prune (β≥σ₁>1−β) y el cap min(β,φ/2,ΣA) con a≤min(β,φ−β)≤φ/2 (3594–3603);
- empate x=r_m: 1+Σ_S>2>φ (3572–3576) y banda (r_m,2/φ) por la cola de x (3578);
- tripleta prohibida: 2·(φ/2)=φ y 0.9>φ/2 (3652–3657);
- cúbica áurea: q(r)=φ−r ⟺ r³+(2−φ)r²+(2−φ)r−φ=0, r*≈0.9637 raíz (verificado numéricamente), techo en r₂=0.9: 2/(φ−0.9−171/271)=22.99≈23.0 (3663–3667);
- π+4arcsin(1/√3)=5.6035, margen 0.68 ✓ (3374); π+2arcsin√(1/φ)=4.948, margen 1.335 ✓ «1.33» (3267);
- óptimos clásicos 1+2/√3 (3 círculos) y 1+√2 (4 círculos) correctos (3646).

**Capa Lean contrastada** (`lean/Calamares/Identities.lean`): golden_pi_trio (394), strong_breathing (376), golden_reduction_threshold (412), diametral_pocket_golden (430), b2_mirror_corner (369), golden_line_N — todos por `decide +kernel`, coincidiendo uno a uno con la lista del verifmap (1332–1351) y con las citas del apéndice.

**Etiquetado honesto verificado:**
- El preámbulo (3039–3046) define las dos etiquetas y el cuerpo del apéndice las usa: los tres teoremas «written» llevan proof sketch con su único paso certificado declarado y con la equiparación explícita al estándar de thm:DPr (3196–3198), que en el cuerpo declara sus maximizaciones «computer-assisted» sin ambages (2989–3028);
- las vacuidades (sliver del bolsillo diametral, empate del gemelo, frontera Σ_S=1+σ₂, tripleta prohibida) están argumentadas como teoremas de exclusión, no como barridos;
- lo model-conditional está nombrado como tal y confinado al canal ocupante (3524–3525, residuo (iii));
- los topes de muestreo se declaran como «sampling ceilings, not derived walls» (residuo (ii)) y `r2bmulti.py` lo repite en su cabecera («el techo Y≤6.6 viene de los topes de MUESTREO X_Y≤3, w≤1.6 — no de una pared derivada; X_Y>3 queda FUERA, declarado»);
- la predicción no ejercitada (rama de dominación del converso) está declarada como tal (3764).

**Direcciones de tolerancia verificadas:**
- esquinas pesimistas: piezas en techos, capacidad en suelo — cota superior válida por monotonía exacta (∂θ/∂pieza>0, ∂θ/∂R<0, verificado en sympy por insercion A y optimizacion A);
- el gap del LP re-verificado en float puro (3471–3472, r2bmulti header) — no se confía en el solver;
- arc-LP con desigualdades cerradas certifica EN la tangencia (3297–3298) — la dirección correcta para suficiencia;
- `lp_min` heurístico ≥ exhaustivo (coronacolas E(c)) — usar el heurístico como cota del camino es conservador;
- el clamp de coordenadas a ventanas (lección de bolsillos) declarado en r2bmulti.

**Circularidad — no encontrada:**
- Todos los cierres asumen ρ≤φ para derivar la contradicción con el bloqueo — la forma correcta (bloqueo ⇒ ρ>φ); el uso de la legalidad de colas para matar instancias del gap (auditcolas) es legítimo porque el programa solo necesita certificados sobre instancias legales;
- el cuerpo consume el apéndice solo como evidencia de conj:golden y en op:assembly, con etiquetas computacionales conservadas (674–683, 1154–1191); thm:oblivious (el teorema principal) no depende del apéndice;
- la cadena de supersesión es acíclica: coronacolas/coronanidada → thm:D1written/nestedwritten/gapwritten → puerto → colageometrica+optimizacion (uniformidad en j y cierre del asterisco de sombras); escala queda como la única capa computacional viva, y es exactamente lo que el residuo (i) declara.

**«The honest residue» — inventario contrastado punto a punto:**
- (i) j≤9 sartén / j≤8 anidado: coincide con `escala.py` (líneas 22, 116, 179, 335: «j <= 9 sarten, j <= 8 anidado») ✓; la uniformidad en j de los teoremas escritos vía cola geométrica está efectivamente certificada (ejecuciones 2–3) ✓;
- (ii) ω≤1.6 y X_Y≤3 como techos primitivos: los demás topes de caja (Y≤6.6, α≤5.1, z≤8.7, X_α≤1.5, X_z≤1) se derivan de esos dos más paredes verdaderas (r2bmulti header; espkp: caja «SUPERCONJUNTO del legal»; dentro de la convención de polvo la cola global acota cada X por φ−1<1) — la enumeración de dos techos primitivos es correcta ✓;
- (iii) banda media en torres d≥2 + exclusión estructural de u + convención de polvo declarada: coincide con espcanal/espcanalp y con la cita 3609–3611 ✓ (con la salvedad de redacción H5);
- (iv) los enunciados abstractos del arc-LP sobreviven, el converso cerrado en forma exacta con su barrido de apoyo muestreado y la rama de dominación no ejercitada: coincide con 3678–3701 ✓; el 1.0116 retirado está justificado por la vacuidad (auditcolas/f3vacio), no por decreto ✓;
- (v) asterisco de optimización cerrado SOLO para presupuestos de sombras: coincide con optimizacion.py (ejecutado) y con el estándar thm:DPr de las demás maximizaciones ✓;
- No encontré ítems del apéndice muestreados/abiertos/condicionales ausentes del inventario, ni ítems del inventario que estén en realidad cerrados. Los «direct sweeps with derived tariffs» de puertocii (3377–3378) quedan cubiertos por (v) como barridos de familia acotada; los large-slack sweeps a 10⁴ del puerto quedan cubiertos por el cierre B&B de las sombras (t₂→∞ analítico en optimizacion C).

**Existencia y correspondencia de scripts:** los 30+ scripts citados en el apéndice existen todos en `code/` (incluido `zigzag.py`, que un listado truncado inicial parecía omitir); las descripciones del verifmap coinciden con las cabeceras de los scripts inspeccionados; `docs/drafts/VEREDICTOS.md` existe (existencia comprobada; contenido no leído por la prohibición de docs/).

**Reparaciones adversariales verificadas en el código** (el texto las relata y el código las contiene):
- la reparación «σ₁ excluida de B* ⇒ cap 2ε₀» de espfinal (3527–3530) está implementada literalmente (`espfinal.py` ~547–550: «REPARACION R1 del acta ... cap 2 eps0», con `cap = max(2*EPS0, muy_eff)`);
- la sustitución del gate tautológico de espcanalp/f3converso (verifmap 1303–1309) es real: `f3converso.py` A3b contrasta ahora contra `primal_factible` (1500 tríos, 0 discrepancias) y lo anota («el gate v2 era TAUTOLOGICO, lp_ok = cajas_ok; ahora compara de verdad»);
- la refutación del enunciado mural ingenuo de lem:insert (3189–3191) tiene su control ejecutable (insercion A4/A6: exceso 2.08 sobre el θ mural en la versión ingenua, ejecutado en verde);
- el techo Y≤6.6 de r2bmulti declarado como consecuencia de topes de muestreo, no pared derivada (header, corrección de acta) — coherente con el residuo (ii).

**Limitación de esta revisión**: los certificados por subdivisión grandes (espcanal 79.277 cajas, espcanalp 144.337+15.571, espfinal 85+~32.100, esppesada ~34.800, espkp 1.329, r2bcert/r2bmulti) no fueron re-ejecutados por presupuesto de tiempo — sus recuentos son impresiones dinámicas de runtime, contrastadas solo contra los docstrings/cabeceras donde figuran (espcanal declara 79.277 en cabecera y claims; los demás son dinámicos). La muestra ejecutada (4 scripts, coincidencia exacta de todos los números contrastables) y la coherencia interna dan confianza, pero la reproducción completa de esos recuentos queda fuera de esta acta.

---

## ADENDA — ejecución de f3converso.py

El run completo (ITER=4000 por defecto) superó con creces el presupuesto de tiempo (>40 min sin terminar; abortado). Re-ejecutado con `CC_ITER=600` (~6 min): **5/5 bloques en verde**, y el contraste cualitativo con el texto (3678–3701) es exacto a escala reducida:
- Barrido del converso: **600 familias (k=3..6, tres modos incluida la zona F3), 183 con gap del certificado cíclico, 183/183 en la celda exacta (i')∨(ii'), 0 fuera** — proporcionalmente consistente con el 4.000/1.266 del texto (tasa de gap 30.5% vs 31.7%); **anatomía: 183/183 por la vía (i') par apilable** — confirma «all of them via the stackable-pair route» y la inversión de la narrativa v1 (3697–3701).
- G1 (pelado): monotonías globales simbólicas con residuo 0 (dp/dR<0 — verificado también a mano: el bolsillo de Descartes decrece con R y p_inf=ab/(√a+√b)² es el suelo uniforme, 3682–3686); pelado masivo 400/400 con discrepancia 0.00e+00 en R_arclp.
- G2 (tres sin gap): reducción a cajas con contraste REAL contra primal_factible (1500 tríos, 0 discrepancias) — el gate tautológico v2 (lp_ok=cajas_ok) que el acta del proyecto cazó está efectivamente sustituido; firma numérica 5.69e-12 en 196 tríos.
- Controles del detector (ii'): False en radio holgado (el detector v1 vacuo devolvía True — reparación confirmada), False en n=3.
- Etiquetas honestas en el propio script: el barrido [C] declarado «MUESTREO de respaldo», y **la banda de gaps (1e-9, 2e-6] no barrida se declara** — este último detalle (tolerancia TOL_GAP del certificador de gaps) no está en el paper; queda cubierto por el «its supporting sweep remaining sampled» del residuo (iv), pero sería deseable explicitarlo.
- **No reproducido por tiempo**: los recuentos absolutos 4.000/1.266 del texto (el run por defecto excede el presupuesto de ejecución de esta revisión); verificados en su lugar a escala 600/183 con las mismas propiedades cualitativas (0 fuera de la celda, 100% vía apilable).
