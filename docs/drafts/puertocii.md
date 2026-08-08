# Puerto (c-ii): mapa de la celda abierta del ensamblaje

Estado: **ADVERSARIADO — CONFIRMADO CON CORRECCIONES Y RECORTES**
(ronda hostil 2026-08-08, acta en `VEREDICTOS.md`). Script
`code/puertocii.py` 6/6 en verde tras 6 reparaciones. Resultado
honesto tras la ronda:

- **(c-ii-1)**: cerrada (computacional-dualidad) con el perfil pesado
  INCLUIDO (antes se descartaba por un uso erróneo de I1).
- **(c-ii-2) perfil ligero, raíz distinta**: cerrada — EXACTA fuera
  de la caja R2 (I1–I3), y dentro de R2 por la pinza del bolsillo
  espejo (núcleo exacto α > 2, T > √5−1, b₂ > 1 > σ₂).
- **(c-ii-2) perfil pesado / S₀ ≤ 1 (R2W, hallazgo de la ronda)**:
  la "ligereza automática" I1 era FALSA para W > 0; la caja R2W vive
  incluso BAJO ω\* (malla B1b: supervivientes desde ω ≈ 0.52) y se
  cierra con la partición u/D_m + la pinza pesada exacta
  b₂(4/φ, 2/φ) = 12/(7φ) > 1 (raíz distinta).
- **(c-ii-2) raíz compartida (R2b, hallazgo ALTA de la ronda)**:
  cerrada por el bloque [G] (2026-08-08, tarde): la colocación que
  faltaba es el TRÍO MURAL {Y, m, σ₂} en el agujero de α (capacidad
  c = α−ω ≥ ΣS+Y por la tarifa DR), con σ₁ y W en fila a D_m por
  ligereza. La suma del trío decrece en c (exacto), el peor caso es
  el suelo c = ΣS+Y, y el sup sobre la ventana es la ESQUINA
  CERTIFICADA (ω→0, σ₂ = 1/2, Y→1, c→2): π + 4·asin(1/√3) ≈ 5.60 <
  2π, margen 0.68 — la ligereza con σ₁ ≥ σ₂ fuerza σ₂ ≤ 1/2 y el
  umbral analítico de peligro era σ₂ = 2/3 (s/(2−s) = 1/2), fuera de
  la ventana. Rama pesada: cuarteto {Y, σ₂, m, σ₁} mural (déficit 0)
  con B* ≤ 1 a D_m. Profundidad d ≥ 2 y la orientación especular
  heredan por monotonía (subir nivel agranda pieza y disco a la vez:
  la suma no crece). Etiqueta: esquina y monotonía-en-c exactas;
  el sup del interior y la rama pesada, barrido de frontera +
  MC (la monotonía completa en (Y, σ₂) queda como observación).

El residuo se declara, no se fuerza.

## 1. La celda y sus paredes

Configuración (c-ii) del ensamblaje (`ensamblaje.md` §5): u = agujero
de α (el intercambio manda m = 1 a u), α ∉ v. Sub-casos:

- **(c-ii-2)** v = agujero de Y, α fuera del agujero de Y;
- **(c-ii-1)** v = sartén con α anidada: α en el agujero de z, torre
  z < w′ < … < t con raíz t top-level de v (toda torre tiene raíz
  top-level, y top-level = sartén = v: t ∈ v SIEMPRE en (c-ii-1)).

S = anillos < m que P mantiene en u, |S| ≥ 2 (E1), σ₁ ≥ σ₂,
S₀ = σ₁+σ₂, W = ΣS − S₀. Paredes del bloqueo (todas las
colocaciones fallan; correcciones de la ronda hostil marcadas):
(D) ΣS > 1 [antes S₀ > 1: esa forma exige W alojada y NO es puerta
universal — S₀ ≤ 1 < ΣS es perfil legítimo]; (BH) σ₂ + X_m > 1−ω;
(B2u/partición) para toda partición A⊎B = S con ΣB ≤ 1:
1+ΣA+X_α > α−ω [la forma clásica 1+σ₂+X_α > α−ω es la rama
A = {σ₂}, solo válida como techo en perfil ligero con S₀ > 1];
(Bσ₁) σ₂+X_{σ₁} > σ₁−ω; (RY) ΣS + X_Y > Y−ω [techo de Y con TODO
S]; (Rz) α+X_z+σ₂ > z−ω por nivel de torre; (COR) corona de v. Legalidades del testigo: α ≥ ΣS+X_α+ω (E4),
α ≥ 1+ω, Y ≥ 1+X_Y+ω, z ≥ α+X_z+ω, X_m ≤ 1−ω. Colas con
ρ ≤ φ: cola(m) ≥ ΣS+X_m; cola(α) ≥ 1+ΣS+X_m+X_α (+Y+X_Y si
Y < α); cola(Y) ≥ 1+ΣS+X_m+X_Y (+α+X_α si α ≤ Y; empates por
convenio de primera copia); cola(z) ≥ 1+ΣS+X_m+X_α+α+X_z, y así
por nivel.

## 2. Las identidades motor (bloque A, sympy, EXACTAS)

**I1 (ligereza CONDICIONAL — corregida en la ronda hostil).** La
identidad E4 + B2u ⟹ ΣS < 1+σ₂ (X_α y ω se cancelan) es exacta,
PERO B2u es solo una rama de la disyunción: la colocación
[A → fila junto a m en u; B = S∖A → fila en D_m] falla sii
(1+ΣA+X_α > α−ω) ∨ (ΣB > 1). En la rama PESADA (ΣS ≥ 1+σ₂, solo
posible con W > 0, k ≥ 3) E4 hace CABER la fila {m, σ₂} en u y el
atasco pasa a {σ₁} ∪ W: I1 NO cierra ahí (el script lo despachaba
como cierre «I1-ligereza»: ERROR reparado). El recurso correcto es
la PARTICIÓN exacta A/B con el techo generalizado
ub(α) = 1+ω+X_α+(ΣS−B\*), B\* = mayor subconjunto de S de suma ≤ 1.
Con S = par (W = 0) la ligereza sí es automática (σ₁ < 1 = m). La
misma corrección desmonta la puerta «(D) como S₀ > 1»: la pared
limpia es ΣS > 1 (fila de TODO S en D_m); S₀ ≤ 1 < ΣS es un perfil
legítimo del bloqueo (antes excluido del muestreo).

**I2 (colas cruzadas, rama Y ≥ α).** cola(Y) con α+X_α dentro, E4 y
(RY) son infactibles salvo (φ−1)(X_Y+ω) > 1, es decir X_Y+ω > φ
(1/(φ−1) = φ). Con X_Y = 0 exige ω > φ: la rama Y ≥ α es VACÍA
para todo pivote de anillo (ω < 1). OJO (ronda hostil): con
X_Y+ω > φ la rama RESPIRA y su cierre es SOLO computacional
(corona-Y sobre los rangos barridos), no la pinza I3 — la
afirmación previa «la cierra I3 vía ω_ef» era incorrecta (I3 es la
rama Y < α).

**I3 (pinza de α, rama Y < α).** cola(α) contiene {m, S, X_m, X_α,
Y, X_Y} con Y ≥ 1+X_Y+ω; B2u da el techo α < 1+σ₂+X_α+ω. La
supervivencia del bloqueo equivale IDÉNTICAMENTE a

    ΣS < φ−2 + φσ₂ + (φ−1)ω + (φ−1)X_α − 2X_Y − X_m.

X_α es la ÚNICA masa que ayuda al adversario (coef φ−1 > 0); X_Y y
X_m cierran (coefs −2, −1). Con X = 0 y las paredes (D) (ΣS > 1) y
σ₁ ≥ σ₂ (ΣS ≥ 2σ₂):

    σ₂ > g(ω) := (3−φ−(φ−1)ω)/φ   y   σ₂ < φω−1,

ventana no vacía ⟺ **ω > ω\* = 3/(2φ) = 3(φ−1)/2 = 0.92705…**
(cruce exacto g(ω\*) = φω\*−1 = **1/2**; la sub-esquina
φω−1 = 1−ω cae en ω = 2/φ² = 4−2φ = 0.76393 < ω\*).

**I4 (pinza de z).** cola(z) + (Rz) ⟹ supervivencia ⟺
α+X_z > φ(1+ΣS) − φ²σ₂ − φ²ω. X_z no tiene techo: la pinza NO
cierra sola; en (c-ii-1) la corona de v toma el relevo (§4). En
torres d ≥ 2 la pinza del nivel superior (misma forma con la masa
acumulada 1+ΣS+X_m+X_α+α+X_z+z+…) cierra la mayoría de las
instancias profundas (los conteos pinza-z2/z3 del bloque C/D).

**Forma cerrada de I3 (ω efectivo).** Con
ω_ef := ω + X_α − φ(2X_Y + X_m), la condición general de
supervivencia de (c-ii-2) es EXACTAMENTE la del caso X = 0 con
ω ↦ ω_ef. Esto da la caja R2 de §5 en forma cerrada.

**Refinamiento del sondeo del acta.** La cadena del acta ((RY) +
cola(Y) con X_Y = 0 ⟹ S₀ > φ−φ²ω) es correcta pero solo cierra en
ω ≈ 0; el cierre real del caso X = 0 es I3 (cola de α con Y dentro),
hasta ω\* — verificado en [E](d): los 83 supervivientes de la malla
fina cumplen la conclusión del sondeo.

## 3. (c-ii-2): cerrada exacta bajo ω\*, residuo R2 delimitado

Bloque B. **B1 (exacto por malla, X = 0, LIGERO)**: ~1.09·10⁶ nodos
(ω × σ₂ × σ₁ × W): NINGUNA instancia ligera del bloqueo sobrevive
con ω ≤ ω\*; toda superviviente (ω > ω\*) cae en la ventana
σ₂ ∈ (g(ω), φω−1). **B1b (malla PESADA, ronda hostil)**: 3.06·10⁵
nodos, 5621 sobreviven a la partición u/D_m con ω desde 0.525 (4683
BAJO ω\*): el perfil pesado NO respeta la esquina áurea; en todos
aplica la pinza F-pesada de raíz distinta. **B2 (MC general, X > 0,
hasta pivote sólido ω ≤ 1.35, X_α ≤ 3, sin S₀ > 1 de fábrica)**:
los cierres se reparten entre cola de m, pinza de colas/partición
(I2/I3 generalizada), corona del agujero de Y y corona del agujero
de α; el residuo ligero cae ÍNTEGRO en la caja R2 (0 fuera) y el
pesado/S₀ ≤ 1 en R2W (todos con pinza F-pesada aplicable). **B3**:
la esquina del residuo LIGERO es (ω, σ₂) = (3/(2φ), 1/2) EXACTA
(la caja R2W no la respeta: su suelo de ω lo pone el barrido, no
una esquina exacta).

Hallazgo geométrico del barrido (corrección sobre el diseño): con
X_α > 0 la pared B2u es una FILA, no un criterio de dos círculos —
el agujero de α admite corona {m, σ₂} ∪ X_α en su peor capacidad
(α mínimo legal; subir α solo agranda el disco). Ese desbloqueo
(corona-α) cierra la gran mayoría del pseudo-residuo con X_α
grande; sin él, la caja habría incluido ω físicos ≈ 0.4 con
ω_ef > ω\*. Con X_α = 0 el criterio de dos círculos sí es exacto y
B2u no admite corona.

## 4. (c-ii-1): CERRADA (computacional-dualidad)

Bloque C. Tras I1 y cola de m, las pinzas por nivel (α, z1, z2, z3)
cierran una fracción; TODO superviviente va a la corona de la sartén
con la maquinaria de coronanidada reutilizada verbatim (cascada
anidada con la raíz t de la torre en el rango de los ocupantes,
suelo de t = su torre muestreada con colas acumuladas; necesidad
R_lb de {t, m = 1, o₁..o_j} con confinamiento por el gigante;
suficiencia con bin D_m = miembro 1.0 que recibe la fila S∖{σ₂} —
SIEMPRE legal por I1 — y variantes de reparto). Resultado: déficit
0.0 UNIFORME en MC + esquinas deterministas (tangencia dual en
R = R_lb), torres d = 1..3, j = 0..3, ω hasta pivote sólido 1.35.
Pared activa: al 90% de R_lb la corona falla ([E](e)).

Por qué cierra donde (c-ii-2) no: en (c-ii-1) el escape del
adversario (X_z grande) infla z y por cola/legalidad infla t, y un
ocupante enorme en la sartén da R_lb grande y arcos chicos: la
corona coloca a σ₂. En (c-ii-2) no hay corona de v utilizable (v es
el agujero de Y, y con S₀ > Y−ω el par no cabe NI en corona: dos
círculos es exacto), por eso allí el cierre es de pinzas y el
residuo sobrevive en ω_ef > ω\*.

## 5. El residuo R2 (DELIMITADO, no forzado)

    R2 = { (c-ii-2), Y < α, perfil LIGERO (ΣS < 1+σ₂) con S₀ > 1,
           ω_ef := ω + X_α − φ(2X_Y+X_m) > 3/(2φ),
           σ₂ ∈ ( g(ω_ef), φω_ef − 1 ),  g(x) = (3−φ−(φ−1)x)/φ,
           1 < ΣS < mín(1+σ₂, φ−2+φσ₂+(φ−1)ω_ef),
           σ₂ ≤ σ₁ < 1,  σ₂ > 1−ω−X_m,  ΣS+X_m ≤ φ,
           Y ∈ [máx(1+X_Y+ω, (1+ΣS+X_m+X_Y)/φ), ΣS+X_Y+ω),
           α ∈ [máx(ΣS+X_α+ω, (2+ΣS+X_m+X_α+2X_Y+ω)/φ),
                1+ω+X_α+(ΣS−B\*)) }.

    (Correcciones de la ronda hostil: el techo de Y es ΣS+X_Y+ω —
    la pared (RY) es la fila de TODO S; el S₀+X_Y+ω anterior era
    anticonservador. El techo de α es el generalizado por partición,
    B\* = mayor subconjunto de S con suma ≤ 1; con perfil ligero y
    S₀ > 1 coincide con el clásico 1+σ₂+X_α+ω.)

Cajas hermanas de la ronda hostil:

    R2W = { (c-ii-2), perfil PESADO (ΣS ≥ 1+σ₂) o S₀ ≤ 1 < ΣS,
            supervivencia de la partición u/D_m: lb(α) < ub_gen(α),
            resto de paredes/colas como arriba }.
    — Vive incluso BAJO ω\* (malla B1b: ω desde ≈ 0.525). En raíz
    distinta la cierra la pinza F1f: BH + pesado ⟹ N ≥ 4,
    α ≥ 4/φ, T > 2/φ, b₂(4/φ, 2/φ) = 12/(7φ) > 1 (EXACTO: 289 >
    245): σ₁ y σ₂ a los dos bolsillos espejo, W ≤ 1 a D_m.

    R2b = { (c-ii-2) con la torre de Y y la torre de α compartiendo
            RAÍZ top-level: Y (o su ancestro z) miembro directo del
            agujero de α, o α anidada bajo la torre de Y;
            X_α ≥ Y ≥ 1+X_Y+ω }.
    — El par {α, T} DEGENERA (T = raíz = α): las pinzas F1e/F1f NO
    aplican; la sartén puede ser {α} sola con R = α. Cierre SOLO
    computacional (F5: coronas con la pieza grande dentro de u, en
    la peor capacidad α = lb(α); 0 residuo en los barridos d = 1..2).
    ABIERTA como celda exacta; profundidades mayores y la variante
    especular declaradas dentro de ella.

Esquina: (ω, σ₂) → (3/(2φ), 1/2) con X = 0. Con X = 0 el residuo
vive solo en ω ∈ (0.927, 1) ∪ [1, ∞) (pivote sólido); con X_α > 0
alcanza ω físicos menores solo si la corona del agujero de α
también falla (raro: en la corrida final corona-α cierra 10 028 y
el residuo MC queda en 581 instancias con ω ∈ [0.989, 1.35],
ω_ef ∈ [0.982, 1.447], σ₂ ∈ [0.363, 0.804]; la franja teórica
ω ∈ (0.927, 1) con X = 0 la exhibe la malla B1: 83 nodos).
Instancia representativa: (ω, σ₁, σ₂) = (1.17, 0.651, 0.608),
X = 0, ΣS = 1.259.

Qué significaba: en R2 las paredes portadas + colas + coronas de la
LISTA ORIGINAL de recursos no producían contradicción. **CERRADA EN
SU SUB-CELDA DE RAÍZ DISTINTA (bloque [F], adversariado
2026-08-08)**: el recurso que faltaba es el REPACK DE LA SARTEN.
Legalidad (confirmada en la ronda hostil, A1): la factibilidad de
una colocación es empaquetabilidad por contenedor — definición del
paper: «Feasibility is a property of the assignment (siblings may
be rearranged freely inside their container)» — y el intercambio
solo exige acuerdo DE CONTENEDOR en los anillos ≥ m (thm:oblivious:
«agreeing with F on all rings of radius ≥ r_m»; el «which do not
move» de esa prueba es el certificado constructivo del caso
superincreciente, no una restricción de la noción); re-empaquetar
la sartén no cambia ningún contenedor. Precedentes en el paper:
lem:DG («full repacking is a legal resource: children travel inside
their parents, positions are existential») y el «pan repack» de
thm:DP — el mismo paso de intercambio bloqueado.

RESTRICCIÓN ESTRUCTURAL (hallazgo ALTA de la ronda): la sartén
contiene a raíz(α) y a raíz(Y) como par top-level SOLO si las dos
torres tienen raíces DISTINTAS. Si comparten raíz (sub-celda R2b de
§5) el par degenera y la pinza NO aplica. La pinza EXACTA que vacía
el núcleo raíz-distinta de R2 (ligero):

- α > 2: N = 2+ΣS+X_m+X_α+2X_Y+ω y ω = ω_ef − X_α + φ(2X_Y+X_m)
  dan N = 2+ΣS+ω_ef+(1+φ)X_m+(2+2φ)X_Y > 3+ω\* (X_α se cancela;
  coeficientes positivos), y (3+3/(2φ))/φ > 2 ⟺ 2φ > 1 (vía
  φ² = φ+1). Sube a las raíces: raíz(α) ≥ α, raíz(Y) ≥ Y.
- T ≥ Y > 2/φ = √5−1: la cola de Y con ΣS > 1.
- b₂ estrictamente creciente en cada argumento
  (∂b₂/∂α · D²/y² = y(2α+y) > 0) y b₂(2, √5−1) = 1 exacto
  (Lean: `b2_mirror_corner`) ⟹ **b₂ > 1 > σ₂**: σ₂ cabe en el
  bolsillo espejo (prop:S5, espejos disjuntos y₀ = 2b₂, contención
  monótona R ≥ suma del par). La MISMA esquina áurea del muro
  espejo de thm:DP.
- Perfil PESADO (R2W, raíz distinta): F1f — N ≥ 4 por BH+pesado,
  b₂(4/φ, 2/φ) = 12/(7φ) > 1: los DOS bolsillos alojan σ₁ y σ₂ y
  W ≤ 1 va a D_m.

Con miembros top-level extra, la corona de la sartén (con
confinamiento por el gigante en R_lb — la trampa de un parámetro de
las campañas) coloca la carga en todos los barridos (bloque F3)
SALVO un puñado de instancias de gap-dualidad (≥ 3 tops casi
iguales, donde el certificado angular R_lb subestima el radio real:
R_fit/R_lb ≤ 1.012 observado, cota declarada 1.15) — DELIMITADAS
con el mismo estatus que la ley de escala; etiqueta
computacional-dualidad como D1–D6 para toda esta parte.

## 6. Qué es exacto y qué es barrido (tras la ronda hostil)

- EXACTO (sympy, bloque A): las identidades I1 (como identidad de la
  rama ligera, NO como «todo perfil es ligero»), I2 (con su rama
  respirante X_Y+ω > φ declarada), I3 (a-d), I4, ω\* = 3/(2φ),
  σ₂\* = 1/2, 2/φ² = 4−2φ, la forma cerrada ω_ef, el refinamiento
  del sondeo, y las nuevas pinzas del repack: F1a-F1d, F1f
  (b₂(4/φ, 2/φ) = 12/(7φ) > 1) y el argumento F1e/F1f de bolsillos
  (módulo el [ENUNCIADO] de legalidad F2, anclado en la definición
  de placement del paper).
- EXACTO por malla densa (B1, ~10⁶ nodos ligeros): el cierre X = 0
  LIGERO bajo ω\*. La malla pesada B1b es DELIMITACIÓN (3·10⁵
  nodos, supervivientes desde ω ≈ 0.525, todos con pinza F-pesada
  aplicable en raíz distinta).
- Barrido MC + dualidad tangente (B2, C, D, F3, F5): los cierres
  corona-Y, corona-α, corona-z, corona-v y partición, con déficit
  0.0 y esquinas deterministas; MISMA etiqueta que D1–D6. El
  gap-dualidad de F3 (≥ 3 tops casi iguales, R_fit/R_lb ≤ 1.012
  observado) queda DELIMITADO con el estatus de la ley de escala.
- La sub-celda R2b (raíz compartida) es SOLO computacional (F5) y
  además con alcance declarado (d = 1..2; profundidades mayores y
  variante especular declaradas sin barrido propio).
- Controles (E): sin colas la pared es vacua (1447/1447); sin (D)
  no hay bloqueo (fila construida); la rígida no es un perfil de
  (c-ii) (σ₁ < m estricto; su límite σ₁ → 1 es pesado y va por
  partición/F-pesada) y la áurea es del caso (a); pared activa al
  90% de R_lb.

## 7. Conservadurismo

Colas omiten masas opcionales salvo las declaradas (cotas más
débiles ⟹ cierre más difícil); corona_suf y los mínimos
heurísticos son cota superior del mínimo (si una variante cabe,
desbloquea); R real ≥ R_lb con déficit 0.0 = tangencia legal
(dualidad); el clamp de la cascada va dentro del max; las coronas
de agujero usan la PEOR capacidad legal (contenedor mínimo;
monotonía en R verificada en las campañas previas); las
composiciones de X son parte de la instancia muestreada.

## 8. Consecuencia para el ensamblaje (tras la ronda hostil)

Con esta campaña y el bloque [F] ADVERSARIADOS, el teorema de
ensamblaje queda: (a), (b), (c-i) como estaban; (c-ii-1) cerrada al
nivel de D1–D6 (perfil pesado incluido); (c-ii-2):

- sub-celda RAÍZ DISTINTA: cerrada — EXACTA fuera de las cajas
  (pinzas I1-corregida/I2/I3/partición) y dentro de R2/R2W por las
  pinzas del bolsillo espejo F1e/F1f (núcleo EXACTO módulo el
  [ENUNCIADO] de legalidad del repack F2); extras por corona con
  etiqueta computacional y el gap-dualidad de F3 delimitado.
- sub-celda RAÍZ COMPARTIDA (R2b): cierre SOLO computacional (F5,
  d = 1..2, 0 residuo en los barridos); ABIERTA como celda exacta.

La celda (c-ii) NO desaparece del todo como residuo del ensamblaje:
se reduce a (i) R2b al nivel computacional-declarado, (ii) el
[ENUNCIADO] F2 (legalidad del repack — anclado en la definición de
placement del paper y en lem:DG/thm:DP, pendiente solo de
formalización), y (iii) las etiquetas computacionales habituales.
El residuo total de τ = φ queda: lema de dualidad/zigzag
(adversariado) + ley de escala (j, p, k) + D1–D6 y
(c-i)/(c-ii)-coronas + **R2b declarada**.
[Ronda hostil de esta campaña COMPLETADA: 2026-08-08, acta en
`VEREDICTOS.md` («Acta: campaña (c-ii) y cierre de R2»).]
