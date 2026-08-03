# Estado de la sesión (2026-08-03) — LA CONJETURA DE T ES FALSA: el umbral es áureo

**BOMBA (2026-08-03, `drafts/umbral_aureo.md`, `aureo.py` 5/5, acta
CONFIRMADO con verificación hostil):** el primer resultado de la
Batalla 2 (u = sartén) REFUTA la conjetura del umbral de Tribonacci. La
familia áurea — sartén R = φ+1, radios {φ, 1, φ/2+2ε, φ/2+ε},
ω ∈ (0.191, 0.618) — tiene ρ = φ+3ε < T, lex-max = 4, y worst fit coloca
3: {φ,1} queda diametralmente rígida y todo tercer círculo ≤ b₂(φ,1) =
φ/2 (S5 exacto). Mecanismo: sin (W) — que solo existe con u = agujero —
el ínfimo cae al primer peldaño de la escalera (el bolsillo): φ. La
instancia es áurea 4 veces (A = φ punto fijo de 2bA = 1+2b; b₂ = φ/2;
(1+φ)/φ = φ; ρ → φ). REINTERPRETACIÓN: T = suelo exacto del intercambio
ANIDADO (toda la Batalla 1 en pie, > T > φ con margen); nueva conjetura:
el umbral global es exactamente φ. El paper ya está reescrito
(thm:golden + conj:golden, abstract, encuadre nested/pan). Y el suelo φ
está CASI CERRADO en S par (**Teorema P**, `drafts/batalla2.md`,
`batalla2.py` 5/5, acta CONFIRMADO): j = 1 toda ω (punto fijo áureo,
cruce (A²−A−1)(2A+1)); rama B todo j y toda ω (hoja estricta,
Ψ_B(1) = φ); rama A por la escalera Ψ (Ψ₁(1/2) = Ψ₂(φ/2) = φ,
Ψ₃(1) = √3); Lema Z; y en 2ª ronda el rincón CERRADO: j = 2 completo
toda ω vía la PARED DE BOLSILLOS ESPEJO (bloqueo ⟹ b₂(o₁,o₂) < 1, cruce
áureo o₂* = √(1+2o₁)−1, Ā(2) = √5−1); j = 3 por árbol de casos salvo
una sub-celda de discos sólidos declarada (torre esbozada, evidencia
2.37). OJO CORRECCIÓN: «S ⊂ (ω,1)» NO es necesidad (discos sólidos
legales); el 13/7-uniforme de T3 es condicional a σ₃ > ω. QUEDA: la
sub-celda de j = 3, |S| ≥ 3 a sartén, pequeños extra, y el ensamblaje
del lema universal con umbral φ.**

## (histórico) Batalla 1: pasos 1–4 y el asalto geométrico cerrados

Documento de retoma para una sesión nueva. Todo lo listado como cerrado está
verificado adversarialmente, consolidado en los documentos y pusheado.
**El programa de la conjetura del umbral de Tribonacci tiene un único hueco
bloqueante: `reinsercion.md` §10.1, partido en las Batallas 1 y 2 de abajo.
En esta racha cayeron: el paso 1 (criterio de coronas, `drafts/corona.md`,
con dos correcciones al plan original), los pasos 2 y 4 en plantilla libre
(`drafts/ocupantes.md`: el precio del ocupante) y el paso 3a
(`drafts/bloqueadores.md`: agujeros ocupados a profundidad arbitraria,
ρ > Ψ(ω) = (1−ω)+√((1−ω)²+1) > T para ω < (T−1)²/2, el Teorema B″ que
elimina «m con hijos», y el ASALTO GEOMÉTRICO (`drafts/bolsillo.md`): el
Lema G (pared del bolsillo doble, σ₁ > b₂(α,o₁), S5 reescalada sin feas3)
con el rincón dorado (α = 2, o₁ = √5−1, b₂ = 1 exacto) y la curva
ρ > φ² − (φ/2)ω > T para todo ω < ω_A = 0.9626 con un ocupante (Teorema G′, ambas ramas; N₁(1/2) = 3/2 y Ψ_B(1/2) = 2 exactos en el parche); Ψ_j =
(1−ω)+√((1−ω)²+j) para j ocupantes; y el Corolario S (pequeños gratis
para la combinatoria)). Actas en VEREDICTOS.md. El antiguo parche del caso hijo-nodo de Ψ_j está
RESUELTO por el **lema de las hojas** (`bolsillo.md` §4, bloque [D] de
`bolsillo.py`; verificación adversaria CONFIRMADA, acta 4ª ronda en
VEREDICTOS.md — reparó el paso de la rama B, doble conteo de M): Ψ_j vale
sin asteriscos para todo j y toda ocupación. Y el frente «S con más de
dos piezas» está CERRADO en la canónica (**Teorema T3**,
`drafts/striple.md`, `striple.py` 5/5, acta CONFIRMADO+REFORZADO):
bloqueo con S = 3 piezas y H_m arbitrario ⟹ ρ > máx(Φ(ω), 13/7) para
todo ω, sin excepciones — el polvo cabalga sobre el par si σ₃ anida; si
no, el U₄ leído al revés fuerza el zigzag, y el zigzag implica
σ₂ > b(α), con la deformación áurea γ_ω (raíz de α³ = α²+α+ω(α²+α+1),
γ₀ = φ, γ₍₂/₇₎ = 2 exacto: 8 = 4+2+2) y el suelo racional **17/7** en
esa rama (la esquina hermana de 13/7); la Proposición T3j hereda Ψ_j
con ocupantes en la rama de reducción. Lo que queda de la Batalla 1:
(a) las puntitas de ω extremo (j=1 ω≥0.9626; j=2 ω≥0.624; j=3 ω≥0.896),
(b) el LEMA DEL HUECO cuantitativo (pequeños frente a la pared
geométrica; σ₂ minúsculo), y (c) k ≥ 4 y j ≥ 1 con k ≥ 3 fuera de la
rama de reducción (numéricamente ≥ 2.2; huecos de `striple.md`).
Después: Batalla 2 (u = sartén) y el ensamblaje del lema universal.**

**Revisión mayor del paper (2026-08-02, plan en `docs/revision_paper.md`,
respuesta al revisor en `docs/respuesta_revision.md`): pasadas 1–2
ejecutadas — Apéndices B (suelo rígido), C (programa de anchura ÍNTEGRO:
ρ*₂/ρ*₃/ρ*_k, frontera cerrada + κ, curva del grosor, Teorema 13/7) y D
(contenedores genéricos ÍNTEGROS: Lema U, coronas/U₄, V1/V2, Lema R,
B/B″, Lema G/G′, Ψ_j por hojas, Corolario S) portados al paper (32 pp.);
secciones 8–9 referencian los apéndices; NP-dureza reforzada (sartén
cuadrada + reducción PARTITION propia; la cita FKS Thm 5.1 del revisor NO
verificable y no usada). Queda: maquetación final, y de Javier: repo
público + Zenodo antes de arXiv; endorsement a Bas Lemmens después.**

## 1. Mapa de lo cerrado (no retocar; actas en `drafts/VEREDICTOS.md`)

| resultado | dónde | código |
|---|---|---|
| Teorema S (suelo rígido, sin idealización) + S5 + S6 + **Lema S6a** | `drafts/suelo_rigido.md` | `rigido.py` 7/7 |
| **H1**: κ = √(g(σ₂)/g(σ₁)) ∀α>1; frontera t(σ₁)+t(σ₂) = t(b(α)); cierre Tribonacci | `drafts/h1.md` | `h1.py` 5/5 |
| Grosor: Φ(ω), cota T+0.0098 | `drafts/grosor_positivo.md` | `grosor.py` 8/8 |
| **Curva exacta del grosor + Teorema de la esquina**: inf T_can = 13/7 sin módulo; ω₁ cúbica; α_m séxtica; bump (ω₁ mín local, ω_peak grado 8) | `drafts/esquina.md` | `esquina.py` 5/5 |
| Perfil k=3: ρ*₃ cerrada, meseta áurea | `drafts/perfil_tres.md` | `tresk.py` |
| **ρ*_k = ρ*₃ ∀k≥3; ω_c = ω_T = 1/T−1/2 exacto** (árbol general; ¡el Corolario 2 NO basta para k≥5!) | `drafts/cuatro.md` | `cuatrok.py` 5/5 |
| Cuadrado: X, b_□(X) = X−1 (con sus matices de acta) | `drafts/cuadrado.md` | `cuadrado.py` |
| **Lema U (frontera universal) + Teorema S con holgura (Corolario U1)** | `drafts/universal.md` | `universal.py` 5/5 |
| **Criterio de coronas + Lema U₄** (paso 1 de la Batalla 1): LP por orden; certificados de subconjunto ∀k; k=4 = trío top + zigzag; k=5 = + pentagrama (C7) | `drafts/corona.md` | `corona.py` 5/5 |
| **El precio del ocupante** (pasos 2 y 4 en plantilla libre): bloqueo ⟹ o_k ≤ 1+ω y ρ > (j+2)/(1+ω); > T hasta ω₅ = 2/T−1/2 (j=1) y ∀ω (j≥2); conjetura fina demostrada en plantilla | `drafts/ocupantes.md` | `ocupantes.py` 5/5 |
| **Los bloqueadores pagan** (pasos 3a+3b, agujeros ocupados ∀profundidad, H_m incluido): Lema R, nodo mínimo, ρ > Ψ(ω) = (1−ω)+√((1−ω)²+1); Teorema B″ (m con hijos): rama B = Ψ_B ≥ Ψ, plata 1+√2, umbrales (T−1)²/2 y (T−1)² | `drafts/bloqueadores.md` | `bloqueadores.py` 6/6 |
| **La pared del bolsillo doble** (asalto geométrico): Lema G (σ₁ > b₂(α,o₁), S5 reescalada, bolsillos espejo a 4b₂); Teoremas G y G′: rincón dorado, ρ > φ²−(φ/2)ω > T ∀ω < 0.9626 (j=1, ambas ramas); Ψ_j; Corolario S (pequeños gratis) | `drafts/bolsillo.md` | `bolsillo.py` 6/6 |

## 2. El arsenal para las batallas (léase `drafts/universal.md` primero)

- **Lema U.** Trío {A, x, y} tangente a pared en disco R arbitrario, con
  c = R−A, T_c(x) = √((c−x)/x): infactible-angular ⟺ T_c(x)+T_c(y) ≤ c/√(AR),
  **BAJO la hipótesis A ≥ mín(x,y)** (sin ella es FALSO — ver acta; la
  dirección ⟹, la que usan las cotas inferiores, es incondicional).
- **Bolsillo general** b_R(A) = ARc/(AR+c²), creciente en R, ≤ A.
- **κ = √(g_c(y)/g_c(x))**, g_c(s) = s³(c−s); umbral afilado del κ ≥ 1:
  3c² ≤ 4AR; en la banda x,y ≤ A margen κ² ≥ 2.442.
- **G_c-identidad**: G_c = (c²/4)U′², U(z) = c/(1+z²) — monotonía de G_c ⟺
  concavidad de U; motor único de TODAS las optimizaciones del programa.
- **Cota de existencia**: bloqueo con cabeza A solo si R < (1+2/√3)A ≈ 2.1547A.
- **Lema S6a** (cierre/monotonía): propaga infactibilidades a [0, δ₀);
  con S5 hace genuinas las familias en σ₁ → 1 (sin módulo feas3).
- **Patrón de prueba de `cuatro.md` §2** (árbol general de perfiles): la
  presión aditiva es monótona en el tamaño; sospecho que la Batalla 1 tiene
  un árbol análogo en "número de ocupantes".
- **Lema U₄** (`corona.md`): corona de {a₁≥a₂≥a₃≥a₄} ⟺ θ₁₂+θ₁₃+θ₂₃ ≤ 2π
  (lineal en T_c, cabeza a₁) y Σθ − θ₁₂ − θ₃₄ ≤ 2π (zigzag). El triángulo
  θ(a,c) ≤ θ(a,b)+θ(b,c) SOLO con b ≥ mín(a,c) (Lema C3). La dirección
  necesaria (certificados de subconjunto, Lema C2) vale para todo k.

## 3. BATALLA 1: v genérico (ocupantes interiores) — el corazón

**Enunciado objetivo.** En el paso de intercambio, v es un disco de radio R
con ocupantes O = {o₁ ≥ … ≥ o_j} ∪ {m} empaquetados (los mayores que m
coinciden en F y en P; normalizar m = 1); m sale; S debe reinsertarse en
v ∪ H_m ∪ anidamientos. Probar: todo bloqueo tiene ρ ≥ T (ρ = colas de la
instancia completa, que INCLUYEN a los o_i).

**Plan de ataque (en orden), con el paso 1 ya cerrado:**
1. **Corona exacta — CERRADO (`drafts/corona.md`, `code/corona.py` 5/5,
   acta en VEREDICTOS.md; verificación adversaria sin claims refutados).**
   OJO, el enunciado que este plan proponía era FALSO en sus dos intuiciones:
   la suma de arcos consecutivos ≤ 2π NO es suficiente para k ≥ 4
   (contraejemplo {0.47×3, 0.02}: el triángulo θ(a,c) ≤ θ(a,b)+θ(b,c) falla
   con intermedio pequeño), y el orden decreciente NO es óptimo (el zigzag
   sí: {0.499, 0.499, 0.33, 0.33} solo empaqueta alternado). Lo correcto:
   factibilidad por orden = LP en los huecos; certificados de subconjunto
   necesarios ∀k (la dirección de las cotas inferiores, incondicional);
   **Lema U₄ (k=4, el caso del paso 2): corona ⟺ DOS desigualdades — trío
   top ≤ 2π (lineal en T_c vía Lema U) y total del zigzag (a₁,a₃,a₂,a₄)
   ≤ 2π** — demostrado para θ arbitrarias por dualidad de restricciones de
   diferencias; k=5 exacto con el certificado extra del pentagrama (Teorema
   C7; su redundancia geométrica = Conjetura C8, hueco declarado).
2. **Dos ocupantes — CERRADO en la plantilla libre, y mejor de lo esperado
   (`drafts/ocupantes.md`, `ocupantes.py` 5/5, acta en VEREDICTOS.md).**
   La pared que el plan no listaba lo decide todo: el agujero de cada
   ocupante extra es un recurso de reinserción (σ₂ ⊂ o_k si σ₂ ≤ o_k − ω),
   y bloquearlo fuerza o_k < σ₂ + ω ≤ 1 + ω. La cola del mayor da
   ρ > (j+2)/(1+ω) — SIN geometría, sin Lema U₄, sin feas3. Corolarios:
   ρ > T para ω < ω₅ = 2/T − 1/2 = 2T²−2T−5/2 = 0.5874 (j = 1; cota fina
   4/(1+2ω) del verificador en ω ≥ 1/2) y para todo ω con j ≥ 2;
   ρ ≥ 13/7 hasta ω ≤ 15/26; conjetura fina DEMOSTRADA en plantilla
   (ρ > 2 > curva canónica, vía Φ(ω) < 2 ∀ω — identidad exacta del 2).
   La evidencia de `universal.py` [E] (mejor ρ = 2.56, cola de γ dominante)
   queda explicada cuantitativamente: 3/(1+ω) ≥ 2.4 en su caja.
3. **Paso 3a — CERRADO (`drafts/bloqueadores.md`, `bloqueadores.py` 5/5,
   acta en VEREDICTOS.md).** Agujeros ocupados a profundidad arbitraria:
   **Lema R** (el disco opuesto, tangencia exacta: bloquear un agujero
   cuesta masa ≥ la holgura ⟹ pared general y < σ₂ + ω + X_y) + **Teorema
   B** (nodo mínimo del árbol, dos colas, sin inducción):
   ρ > Ψ(ω) = (1−ω)+√((1−ω)²+1); Ψ(0) = 1+√2; Ψ(1/4) = 2 exacto;
   > T ⟺ ω < (T−1)²/2 = 0.3522. OJO al acta: la primera versión de §5
   («la fuga») fue REFUTADA — la dicotomía de evacuación correcta es
   bloqueo ⟹ σ₂ > 1−ω ∨ σ₁+Σhijos(m) > 1, y la evidencia dice que «m con
   hijos» probablemente NO necesita geometría.

   **Paso 3b — CERRADO (Teorema B″, mismo borrador, acta 2ª ronda).**
   «m con hijos» cae por la dicotomía de evacuación: rama A = Teorema B
   literal; rama B (σ₁+Σhijos(m) > 1) = media metálica Ψ_B = raíz de
   u²−(2−ω)u−1 ≥ Ψ = raíz de u²−2(1−ω)u−1 (la raíz crece con b), dominada.
   Umbral de la rama B: (T−1)² exacto (su identidad ES el polinomio de
   Tribonacci); Ψ(0) = 1+√2 = razón de plata. Corolario B2: la canónica
   tampoco necesita la hipótesis (ρ > Φ(ω)). OJO del acta: la definición de
   nodo excluye a m explícitamente (sin ello se rompe el paso 3 de B).

   **LO QUE QUEDA de la Batalla 1 (por orden sugerido):**
   (i) *Ocupantes de v menores que m* (aplastamiento por pequeños) y
   *tramos de ω grande* (ω ≥ (T−1)²/2 con agujeros ocupados; ω ≥ 0.5874 con
   libres): rama geométrica del testigo con el Lema U₄ en R̄ (evidencia:
   las 2000 bloqueadas-por-paredes de menor ρ en ω ∈ [0.5, 0.63] admiten
   todas corona ⟹ estaban desbloqueadas). Para pequeños: "lema del hueco"
   vía densidad crítica 1/2 de Fekete–Keldenich–Scheffer y la pista √δ de
   `rigido.py` V7b; presupuesto de masa por la cola de m.
   (ii) *S con más de dos piezas* (ρ*_k = ρ*₃ acota por el lado
   combinatorio; rehacer las optimizaciones si hiciera falta).
   Después: Batalla 2 (u = sartén, `universal.md` §3) y el ensamblaje del
   lema universal de reinserción (§5 de este documento).
4. **k ocupantes — CERRADO en la plantilla libre, sin inducción (mismo
   `drafts/ocupantes.md`).** La cota ρ > (j+2)/(1+ω) es uniforme en j (una
   pared por agujero + la cola del mayor ocupante): cada ocupante paga
   1/(1+ω), y con j ≥ 2 la cota supera T para TODO ω < 1. El "árbol en
   número de ocupantes" que este plan conjeturaba resultó ser una sola
   desigualdad.

**Riesgos conocidos:** (i) corona ≠ empaquetamiento general (ocupantes
interiores existen de verdad) — por eso el paso 3 es el corazón; el criterio
de `corona.md` caracteriza coronas, no empaquetamientos; (ii) OJO con la
dirección de las hipótesis del Lema U cuando la "cabeza" del trío no sea el
mayor (usar solo la dirección ⟹ o verificar A ≥ mín) — en el Lema U₄ el trío
top tiene cabeza = máximo y la hipótesis es automática; (iii) ρ de la
instancia completa incluye colas de aros que no están en v — formular con
cuidado qué instancia realiza el bloqueo (véase cómo lo hace la Proposición 3
/ grosor_positivo §1); (iv) la rama nueva del zigzag (total de 4 θ) no es
lineal en T_c: tratarla con las identidades g/G_c de `universal.md` o
directamente.

## 4. BATALLA 2: u = sartén (después de la 1)

Si u (contenedor de m según F) es la sartén, (W) deja de ser una capacidad:
el testigo colocó S en la sartén junto a los ocupantes mayores. El análogo
de (W) es una condición de corona — lineal en T_c por el Lema U_k del paso 1
de la Batalla 1. Formulación en `universal.md` §3. Sin explorar.

## 5. Después de las batallas (en orden)

1. Ensamblar el **lema universal de reinserción** (ρ < T ⟹ el intercambio
   nunca se bloquea): combinatoria (ρ*_k = ρ*₃, ω_c = ω_T) para ω < ω_T +
   geometría (Batallas 1–2) para ω ≥ ω_T. Con él, la conjetura del umbral de
   Tribonacci queda a un paso (revisar el argumento completo del Teorema 2).
2. Rigor menor: cota ρ > √2 del cuadrado solo α ≥ 1 (hoja §7.5); exactitud
   de feas3 (§7.6, esquivable con direcciones constructivas).
3. ~~Consolidar `paper/main.tex`~~ — HECHO (2026-08-02): toda la cosecha
   integrada (incluida la Batalla 1), revisada contra los drafts y
   recompilada; queda el pulido fino (nombres, abstract) de hoja §6.

## 6. Protocolo y entorno (imprescindible)

- **Workflow por resultado**: explorar en scratchpad → `code/<nombre>.py`
  con bloques [A] simbólico / [B–D] numérico / verde total → borrador en
  `docs/drafts/<nombre>.md` con huecos declarados → **verificación
  adversaria** (agente independiente, protocolo 2 fases: Fase 1 rederivar
  SIN mirar los ficheros nuevos; Fase 2 auditar + ejecutar) → consolidar en
  resultados.md §9 / hoja_de_ruta / reinsercion + acta en VEREDICTOS.md →
  commit. **Las 4 verificaciones de esta racha cazaron errores reales**
  (hueco del Corolario 2, extremo de S6a, hipótesis del Lema U, α_peak):
  no saltarse el paso.
- sympy/mpmath SOLO en `python3.12` (el python3 por defecto no los tiene).
- Tiempos: esquina.py ~12 min, cuatrok.py ~15 min, universal.py ~4 min —
  lanzar en background.
- Si los subagentes fallan con 401 persistente: `/login`; con 529: backoff y
  reintentar (SendMessage al mismo agente retoma su transcripción).
- Scratchpads de esta racha (fuera del repo): explora_esquina.py,
  explora_cuatro.py, explora_universal.py, verif_esquina/, verif_cuatro/,
  verif_universal/ — los oráculos independientes de los verificadores son
  reutilizables.
