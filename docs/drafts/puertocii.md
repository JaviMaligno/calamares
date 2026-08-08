# Puerto (c-ii): mapa de la celda abierta del ensamblaje

Estado: **mapa completo, PRE-ADVERSARIO** (2026-08-08). Script
`code/puertocii.py` 5/5 en verde (corrida final CC_ITER = 60000:
malla B1 de 1 018 275 nodos; B2 con 176 993 instancias del bloqueo;
C1 con 19 120 coronas, déficit 0.0; D con 20 000 enrutadas, 0 sin
caso). Resultado: (c-ii-1) CERRADA
(computacional-dualidad), (c-ii-2) CERRADA EXACTA salvo un residuo
R2 DELIMITADO en forma cerrada (esquina áurea ω* = 3/(2φ),
σ₂* = 1/2). El residuo se declara, no se fuerza.

## 1. La celda y sus paredes

Configuración (c-ii) del ensamblaje (`ensamblaje.md` §5): u = agujero
de α (el intercambio manda m = 1 a u), α ∉ v. Sub-casos:

- **(c-ii-2)** v = agujero de Y, α fuera del agujero de Y;
- **(c-ii-1)** v = sartén con α anidada: α en el agujero de z, torre
  z < w′ < … < t con raíz t top-level de v (toda torre tiene raíz
  top-level, y top-level = sartén = v: t ∈ v SIEMPRE en (c-ii-1)).

S = anillos < m que P mantiene en u, |S| ≥ 2 (E1), σ₁ ≥ σ₂,
S₀ = σ₁+σ₂, W = ΣS − S₀. Paredes del bloqueo (todas las
colocaciones del par fallan): (D) S₀ > 1; (BH) σ₂ + X_m > 1−ω;
(B2u) 1+σ₂+X_α > α−ω; (Bσ₁) σ₂+X_{σ₁} > σ₁−ω; (RY)
ΣS + X_Y > Y−ω; (Rz) α+X_z+σ₂ > z−ω por nivel de torre; (COR)
corona de v. Legalidades del testigo: α ≥ ΣS+X_α+ω (E4),
α ≥ 1+ω, Y ≥ 1+X_Y+ω, z ≥ α+X_z+ω, X_m ≤ 1−ω. Colas con
ρ ≤ φ: cola(m) ≥ ΣS+X_m; cola(α) ≥ 1+ΣS+X_m+X_α (+Y+X_Y si
Y < α); cola(Y) ≥ 1+ΣS+X_m+X_Y (+α+X_α si α ≤ Y; empates por
convenio de primera copia); cola(z) ≥ 1+ΣS+X_m+X_α+α+X_z, y así
por nivel.

## 2. Las identidades motor (bloque A, sympy, EXACTAS)

**I1 (ligereza automática).** E4 + B2u ⟹ ΣS < 1+σ₂ (X_α y ω se
cancelan idénticamente). Consecuencias: en (c-ii) TODO perfil es
ligero (σ₁+W < 1), y S∖{σ₂} cabe SIEMPRE como fila en D_m (suma
ΣS−σ₂ < 1). El bloqueo de (c-ii) se reduce a colocar σ₂. Además
expulsa a la esquina rígida (σ₁ = 1 da ΣS ≥ 1+σ₂): el análogo del
control «la esquina rígida nunca se certifica» aquí es «la esquina
rígida no vive en (c-ii)».

**I2 (colas cruzadas, rama Y ≥ α).** cola(Y) con α+X_α dentro, E4 y
(RY) son infactibles salvo (φ−1)(X_Y+ω) > 1, es decir X_Y+ω > φ
(1/(φ−1) = φ). Con X_Y = 0 exige ω > φ: la rama Y ≥ α es VACÍA
para todo pivote de anillo (ω < 1) y solo respira con X_Y+ω > φ
(donde la cierra la pinza I3 vía ω_ef, §3).

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

Bloque B. **B1 (exacto por malla, X = 0)**: 1 018 275 nodos
(ω × σ₂ × σ₁ × W): NINGUNA instancia del bloqueo sobrevive con
ω ≤ ω\*; toda superviviente (ω > ω\*) cae en la ventana
σ₂ ∈ (g(ω), φω−1). **B2 (MC general, X > 0, hasta pivote sólido
ω ≤ 1.35)**: los cierres se reparten entre I1-ligereza, cola de m,
pinza de colas (I2/I3), corona del agujero de Y y corona del agujero
de α; el residuo cae ÍNTEGRO en la caja R2 (0 fuera). **B3**: la
esquina del residuo es (ω, σ₂) = (3/(2φ), 1/2) EXACTA.

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

    R2 = { (c-ii-2), Y < α, α top-level (si α anidada, la pinza de
           su torre cierra más),
           ω_ef := ω + X_α − φ(2X_Y+X_m) > 3/(2φ),
           σ₂ ∈ ( g(ω_ef), φω_ef − 1 ),  g(x) = (3−φ−(φ−1)x)/φ,
           1 < ΣS < mín(1+σ₂, φ−2+φσ₂+(φ−1)ω_ef),
           σ₂ ≤ σ₁ < 1,  σ₂ > 1−ω−X_m,  ΣS+X_m ≤ φ,
           Y ∈ [máx(1+X_Y+ω, (1+ΣS+X_m+X_Y)/φ), S₀+X_Y+ω),
           α ∈ [máx(ΣS+X_α+ω, (2+ΣS+X_m+X_α+2X_Y+ω)/φ),
                1+σ₂+X_α+ω) }.

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
LISTA ORIGINAL de recursos no producían contradicción. **CERRADO
(bloque [F], 2026-08-08)**: el recurso que faltaba es el REPACK DE
LA SARTEN. La factibilidad de una colocación es empaquetabilidad por
contenedor (existencial en posiciones) y el intercambio solo exige
acuerdo DE CONTENEDOR en los anillos ≥ m (thm:oblivious: «agreeing
with F on all rings of radius ≥ r_m»); re-empaquetar la sartén no
cambia ningún contenedor, y el precedente en el propio paper es el
«pan repack» de thm:DP (con ocupantes > m re-colocados en corona).
En (c-ii-2) la sartén contiene a α y al tope T de la torre de Y
(top-level, compartidos), luego «σ₂ → bolsillo espejo del par
{α, T} re-empaquetado diametral» es una colocación del testigo y su
fallo es pared del bloqueo. La pinza EXACTA que vacía R2:

- α > 2: N = 2+ΣS+X_m+X_α+2X_Y+ω y ω ≥ ω_ef − X_α + φ(2X_Y+X_m)
  dan N > 3+ω\*, y (3+3/(2φ))/φ > 2 ⟺ 2φ > 1 (vía φ² = φ+1).
- T ≥ Y > 2/φ = √5−1: la cola de Y con ΣS > 1.
- b₂ estrictamente creciente en cada argumento
  (∂b₂/∂α · D²/y² = y(2α+y) > 0) y b₂(2, √5−1) = 1 exacto
  (Lean: `b2_mirror_corner`) ⟹ **b₂(α, T) > 1 > σ₂**: σ₂ cabe en
  el bolsillo espejo (prop:S5, espejos disjuntos y₀ = 2b₂,
  contención monótona R ≥ α+T). La MISMA esquina áurea del muro
  espejo de thm:DP cierra la última celda.

Con miembros top-level extra, la corona de la sartén (con
confinamiento por el gigante en R_lb — la trampa de un parámetro de
las campañas) coloca σ₂ en todos los barridos (bloque F3, 0 fallos);
etiqueta computacional-dualidad como D1–D6 para esa parte.

## 6. Qué es exacto y qué es barrido

- EXACTO (sympy, bloque A): I1, I2, I3 (a-d), I4, ω\* = 3/(2φ),
  σ₂\* = 1/2, 2/φ² = 4−2φ, la forma cerrada ω_ef y el
  refinamiento del sondeo.
- EXACTO por malla densa (B1, 10⁶ nodos): el cierre X = 0 bajo ω\*
  (la malla verifica la infactibilidad que I3 demuestra; el
  argumento es el algebraico, la malla es control).
- Barrido MC + dualidad tangente (B2, C, D): los cierres corona-Y,
  corona-α y corona-v, con déficit 0.0 uniforme y esquinas
  deterministas; MISMA etiqueta que D1–D6 (evidencia computacional;
  el cierre formal pende del lema de dualidad/zigzag y la ley de
  escala).
- Controles (E): sin colas la pared es vacua (1447/1447); sin (D)
  no hay bloqueo (fila construida); la rígida no vive en (c-ii)
  (expulsada por I1) y la áurea es del caso (a); pared activa al
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

## 8. Consecuencia para el ensamblaje

Con esta campaña Y el bloque [F], el teorema de ensamblaje queda:
(a), (b), (c-i) como estaban; (c-ii-1) cerrada al nivel de D1–D6;
(c-ii-2) cerrada — EXACTA fuera de la caja R2 (pinzas I1–I3) y
dentro de R2 por la pinza del bolsillo espejo (núcleo EXACTO:
α > 2, T > √5−1, b₂ > 1 > σ₂; extras por corona con etiqueta
computacional). La celda (c-ii) deja de ser residuo del ensamblaje:
el teorema pierde su condicionalidad estructural y el residuo total
de τ = φ vuelve a ser exactamente el de las campañas: el lema de
dualidad/zigzag (adversariado) + la ley de escala (j, p, k) + las
etiquetas computacionales de D1–D6, (c-i)/(c-ii)-coronas.
[PENDIENTE: ronda hostil de esta campaña, incluido [F].]
