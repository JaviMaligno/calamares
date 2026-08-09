# Las dos ramas de agujero: el residuo del puerto como teoremas

Estado: DRAFT con pruebas (2026-08-09), ADVERSARIADO (acta en
VEREDICTOS.md, misma fecha: CONFIRMADO CON CORRECCIONES; 0
contraejemplos en 55k instancias adversarias independientes; las
reparaciones H1-H3 integradas). Script: `code/coronaagujero.py`
(5/5). Cierra las dos ramas abiertas de `puertoescrito.md` §3.1-2 —
el último residuo geométrico del programa τ = φ — con la MISMA
plantilla de los teoremas anidados, aplicada al agujero como
contenedor.

## 1. La observación que lo desbloquea

Los teoremas thm:nestedwritten y thm:gapwritten no usan nada
específico de la sartén: usan (i) una familia top-level del
contenedor per P, (ii) D_m vacante, (iii) el destino de m legal por
el certificado de F, (iv) las cotas de masa. Un agujero (de Y o de
α) con capacidad c es un disco igual que la sartén con R. La
dicotomía se hereda con k = número de ocupantes > m del agujero:

- k ≥ 3 ⟺ plantilla j ≥ 2: la cadena de cascada ENTRE LOS
  OCUPANTES DEL AGUJERO da x₂ ≥ (1+Σ)(1+φ)/φ² = 1+Σ ≥ 2 (la misma
  identidad φ² = 1+φ; las colas de los x contienen a m y a toda la
  masa suelta), y el par del empaquetamiento real del agujero
  (c ≥ x₁+x₂) da el régimen automático c−x ≥ x₂ ≥ 2 > φ ≥ 2s′,
  2 > 2/φ = 2w* (margen 2−φ): SOMBRAS.
- k ≤ 2 ⟺ plantilla j ≤ 1: familia ACOTADA (≤ 5 piezas): criterio
  mural exacto por instancia + cota blindada del trío
  c ≥ máx(pares, mín(R₃, M)) sobre {x₁, x₂, m} (incondicional,
  dicotomía de apilabilidad — `gaplemma.md` §3).

DIFERENCIA REAL que exige script propio (y por la que las cajas
certificadas de `insercionanidada.py`/`gaplemma.py` NO cubren): los
suelos del agujero son MÁS BAJOS — los ocupantes de un agujero no
tienen relación con la pared de la sartén, su suelo es 1 (anillos
≥ m) y la cascada, no 1+ω. El script barre ese dominio propio
(suelo 1, ω hasta 1.35 solo vía tarifas, holgura hasta 10⁴, límite
x₁ → ∞ = π por fórmula).

## 2. Rama 1: (c-ii-2) con Y ≥ α respirando (X_Y + ω > φ)

La única no vacía por I2 (exacta, `puertocii.md`). v = agujero de Y,
capacidad c = Y−ω; per P contiene los anillos > m compartidos
{x₁..x_k}, posible POLVO < m, y m top-level (X_Y en el convenio de
puertocii incluye el polvo — ronda hostil).

**Lema de respiración fuerte (exacto; la reparación H1 del acta).**
El argumento ingenuo «respirar ⟹ k ≥ 1 porque las piezas son ≥ 1»
es FALSO con polvo en X_Y. El correcto: la I2 COMPLETA
((φ−1)(X_Y+ω) > 1+(2−φ)ΣS+X_m+X_α, `survive_c2`) con la pared (D)
(ΣS > 1) y X_m, X_α ≥ 0 da X_Y+ω > φ(3−φ) = 2φ−1 = √5; el polvo de
v está acotado por cola(m) ≤ φ: polvo ≤ φ−ΣS < φ−1; luego la masa
> m cumple X_{>m}+ω > √5−(φ−1) = φ EXACTO (√5−φ+1 = φ). k ≥ 1
genuino, la celda k = 0 vacía de verdad, y el filtro X_{>m}+ω > φ
del script justificado — el umbral áureo reaparece tras descontar
el polvo. El polvo va a la masa suelta Σ (el reparto ya lo hace).

**Reparto testigo** (el de los teoremas anidados, contenedor = el
agujero): m → u por el certificado de F; los extras < m top-level de
v salen (masa contada en Σ, convención idéntica a la sartén);
llenado greedy de D_m hasta s′; s′ mural en v sobre {x₁..x_k, D_m};
resto w* < 1/φ mural otra vez. Ligaduras exactas heredadas:
s′ ≤ mín(Σ/2, φ/2), W″ < mín(1/φ, Σ−1, Σ−2s′).

**Necesidades sobre c** (conservador: SOLO pares del empaquetamiento
real + blindada; la legalidad Y ≥ 1+X_Y+ω NO se usa como suelo):
c ≥ x₁+x₂ (k ≥ 2), c ≥ x₁+1 (par con m), y para k = 2 la blindada
del trío {x₁, x₂, m}. El barrido evalúa en el peor c (las sombras
decrecen en c; la corona acotada se evalúa en el suelo).

Resultados (bloques B y C): k ≥ 3 — 27 920 instancias respirantes
(7 920 deterministas, h hasta 10⁴, una y dos piezas infladas,
k hasta 14), 0 fallos de régimen (exacto), y el presupuesto en el
MAYORANTE DESACOPLADO (H3: s′ = mín(Σ/2, φ/2) Y w* = 1/φ a la vez —
mayoriza todo el trade-off por monotonía en ambos tamaños): peor
5.2115 < 2π−0.05 en el SUELO (k = 3, ω = 0.05, Σ → 1, h = 1 — el
mismo suelo crítico del teorema anidado); límite x₁ → ∞ = π por
fórmula (margen π). k ≤ 2 — 15 964 instancias (1 296 deterministas
con trade-off s′/w* y esquinas de cascada exacta, que incluyen el
punto áureo {2, 2/φ, 1} en k = 2, Σ → 1), 0 fallos de corona.

## 3. Rama 2: corona-α con X_α grande

u = agujero de α, capacidad c = α−ω, ocupantes {x₁..x_k} per P
(masa X_α > 0 ⟹ k ≥ 1; con X_α = 0 el criterio de dos círculos es
exacto y la celda es de I3: fuera). Perfil LIGERO (ΣS < 1+σ₂; el
pesado lo cierra la partición B*/A con la pinza exacta
b₂(4/φ, 2/φ) = 12/(7φ) > 1, y en raíz compartida el cuarteto de
[G]).

**La ligereza regala la partición**: B = S∖{σ₂} tiene masa
ΣS − σ₂ < 1 EXACTA ⟹ B entera va en fila a D_m (en v, vacante).
SOLO σ₂ necesita inserción mural en u, sobre {x₁..x_k, m} (m llega
por el certificado de F; el repack de u es recurso legal —
precedente del pan repack).

**La ventana de c es exacta**: c ∈ [ΣS+X_α, 1+σ₂+X_α) — suelo E4
(α ≥ ΣS+X_α+ω; S vive en u per P, la Σ_S del suelo es ΣS entera) y
techo B2u (si c ≥ 1+σ₂+X_α la fila cabe y no hay bloqueo). X_α se
CANCELA en el ancho 1+σ₂−ΣS > 0 (ligero). Los pares c ≥ x₁+x₂,
x₁+1 y la blindada (k = 2) son necesidades verdaderas pero NUNCA
muerden aquí (H4 del acta: ΣS+X_α ≥ 1+x₁+x₂ > máx(pares, M)
siempre, con ΣS > 1 y x₂ ≥ 1): la ventana efectiva es
[ΣS+X_α, 1+σ₂+X_α) a secas. En rama 2 «X_α > 0 ⟹ k ≥ 1» SÍ es
exacto tal cual (S contiene TODOS los anillos < m de u por
definición: X_α es masa ≥ m, sin polvo).

Dicotomía: k ≥ 3 — régimen automático para σ₂ (c−x ≥ x₂ ≥ 1+Σ ≥ 2 >
2σ₂ al ser σ₂ < 1: margen 2−2σ₂) y presupuesto de sombras de UNA
inserción; k ≤ 2 — corona acotada {x₁, (x₂), m, σ₂} (≤ 4 piezas).

Resultados (bloque D): 28 445 instancias k ≥ 3 (σ₂ barrida hasta
0.95, más allá de la ventana R2 [0.363, 0.804]; k hasta 12), 0
fallos de régimen y 0 de presupuesto (peor 3.1137); 7 180
instancias k ≤ 2, 0 fallos de corona. Esquinas: σ₂ ∈ {0.363, 1/2,
1/φ, 0.804, 0.95}, Σ → 1⁺ y → (1+σ₂)⁻, ω hasta 1.35, h hasta 10⁴.

**La dirección k (asterisco declarado, H2 del acta).** El
certificado numérico cubre k ≤ 14 (rama 1) y k ≤ 12 (rama 2); el
peor presupuesto DECRECE en k (rama 1: 5.212 → 3.382; rama 2:
3.114 → 3.106), coherente con el crecimiento geométrico de la
cascada (razón φ). Es el análogo exacto de la dirección j de la ley
de escala — mismo estatus de residuo numérico; el lema de cola
geométrica que lo cerraría por fórmula es el mismo pendiente.

## 4. Los teoremas

**Teorema (rama respirante).** En (c-ii-2) con Y ≥ α y X_Y+ω > φ,
ρ ≤ φ implica que el intercambio no se bloquea, para todo ω (pivote
sólido incluido), perfil y extras, con k ≤ 14 certificado y la
dirección k como asterisco decreciente. *Prueba.* Reparto de §2;
k ≥ 3 por el régimen automático heredado (exacto) y el presupuesto
de sombras certificado en el mayorante; k ≤ 2 por la corona acotada
con la cota blindada del trío; k = 0 vacío por el lema de
respiración fuerte (exacto: I2 completa + (D) + cota de polvo). ∎

**Teorema (corona-α).** En (c-ii-2) con Y < α, perfil ligero y
X_α > 0, ρ ≤ φ implica no bloqueo, para todo ω, σ₂ y ΣS, con
k ≤ 12 certificado y la dirección k como asterisco decreciente.
*Prueba.* Partición exacta B/{σ₂} de §3 (ΣB < 1 por ligereza);
σ₂ mural en u: k ≥ 3 por régimen automático (σ₂ < 1, exacto) +
presupuesto certificado; k ≤ 2 por corona acotada en la ventana
exacta de c. ∎

Con ambos, el §3.1-2 de `puertoescrito.md` (las dos ramas abiertas)
queda cerrado AL MISMO ESTÁNDAR que el resto del programa: exacto
en ligaduras, regímenes y ventanas; numérico-certificado en los
sups de presupuesto/corona (el mismo lema de optimización pendiente
común). El residuo computacional del programa se reduce a los
asteriscos heredados de `puertoescrito.md` §3.3-6 (barridos G de
R2b, F2, gap-dualidad F3, lema de optimización) y la dirección j de
la ley de escala.

## 5. Estatus

Exacto (teorema): la cadena de cascada del agujero (x₂ ≥ 1+Σ con
k ≥ 3, misma identidad φ² = 1+φ; la cola es GLOBAL — convención del
paper, verificada en acta — así que vale en ambos agujeros), los
regímenes automáticos de ambas ramas (márgenes 2−φ y 2−2σ₂), el
LEMA DE RESPIRACIÓN FUERTE (I2 completa + (D) ⟹ X_Y+ω > √5; polvo
< φ−1; X_{>m}+ω > φ ⟹ k ≥ 1), la ligereza ⟹ ΣB < 1, la ventana de
c en rama 2 (E4 + techo B2u, X_α cancelada; en rama 2 X_α es masa
≥ m sin polvo y k ≥ 1 es directo), la cota blindada del trío sobre
c (legítima: F empaquetó {x's, m} simultáneos cuando colocó m — los
> m coinciden por maximalidad), las ligaduras de masa, Σ > 1
FORZADA en la celda (pared (D); Σ ≤ 1 imposible, no hace falta la
cláusula de fila), y el límite x₁ → ∞ (por fórmula, margen π).
Numérico-certificado: los presupuestos < 2π (en el MAYORANTE
desacoplado s′-tope + w* = 1/φ) y las coronas acotadas sobre los
dominios muestreados (MC + esquinas deterministas + holgura 10⁴ +
55k instancias adversarias independientes del acta, 0 fallos);
dirección k: asterisco decreciente (k ≤ 14/12 certificado).
Controles: violar el par del agujero revienta la sombra; k = 2 con
σ₂ > 1/φ NO tiene régimen automático (la dicotomía es necesaria);
las celdas excluidas (no respirante, pesada, X_α = 0) tienen cierre
exacto propio ajeno al script.
