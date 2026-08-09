# El gap lemma escrito: anidado j ≤ 1 por corona directa

Estado: DRAFT con pruebas (2026-08-09), ADVERSARIADO (acta en
VEREDICTOS.md, misma fecha). Script: `code/gaplemma.py` (5/5;
estrés 150k + semillas alternas en verde). Cierra la última celda
anidada; con `insercionanidada.md` (j ≥ 2), la plantilla anidada
queda ENTERA (al mismo estándar: exacto en las ligaduras,
numérico-certificado en el sup, §6).

## 1. La observación que lo desbloquea

La navaja áurea mata el método de sombras en j ≤ 1, pero allí la
sartén es una familia ACOTADA: {α, (o₁ si j = 1), el disco unidad
con la fila greedy de D_m dentro, s′, w*} — a lo sumo 5 círculos.
No hacen falta sombras: el criterio mural directo de k ≤ 5 piezas
(mín exhaustivo sobre ≤ 12 órdenes cíclicos — el código prueba las
24 permutaciones de 4, que duplican por reflexión: sobra; posiciones
por camino más largo con TODAS las parejas validadas — solidez
adversariada en zigzag/compactación) es EXACTO y finito por
instancia, y el dominio es una caja compacta: el mismo esquema de
maximización que thm:DPr (el estatus fino del sup, en §6).

## 2. El reparto y las cotas (heredadas, exactas)

Idéntico al del teorema j ≥ 2 salvo el paso mural: (1) m → agujero
de α por el certificado de F; (2) llenado greedy de D_m (fila
decreciente hasta s′); (3) REPACK MURAL de la sartén entera con las
≤ 5 piezas (el disco-1 con la fila dentro es una pieza: lem:row,
interior no visible; el repack es recurso legal — pan repack de
thm:DP); (4) s′ ≤ mín(Σ/2, φ/2), W″ < mín(1/φ, Σ − 1, Σ − 2s′)
(fila + s′ > 1 y ℓ₁ ≥ s′; ¡ligadura de masa que hace INFACTIBLE la
esquina s′ = φ/2 ∧ w* = 1/φ simultáneos!), Σ ∈ (1, φ].

Los suelos del dominio, con la S DEL AGUJERO separada (ronda hostil
2026-08-09): α ≥ máx(1+ω, Σ_S+X_α+ω, (1+Σ+X_α)/φ), donde Σ_S ≤ Σ
es SOLO la masa del agujero de α — los extras/polvo top-level de la
sartén no están en el agujero y NO pueden entrar en el suelo E4 (el
barrido v1 usaba Σ total ahí: anticonservador; corregido, Σ_S se
barre en [0, Σ] independiente, incluido el suelo mínimo absoluto
Σ_S = 0 con α = máx(1+ω, (1+Σ)/φ)). Los suelos de cascada sí llevan
Σ total: la cola de α y la de o₁ contienen m y TODA la masa suelta,
extras incluidos (o₁ ≥ (1+Σ)/φ).

## 3. La necesidad del trío (la pieza nueva, teorema)

Para j = 1 el par mínimo R = máx(α+o₁, o₁+1) NO basta (en la navaja
α = o₁ = 2/φ el trío {α, o₁, m} suma > 2π ahí). La cota correcta es
la NECESIDAD DEL TRÍO: cualquier disco que empaquete {a, b, c} con
pares no apilables cumple θ(a,b) + θ(b,c) + θ(c,a) ≤ 2π (P1 +
partición del círculo — teorema, `compactacion.md`; para tres piezas
todos los órdenes cíclicos son el mismo ciclo, (3−1)!/2 = 1). R₃ se
define por la igualdad.

**Cota blindada (sin hipótesis de apilabilidad).** Sea M := mín
sobre pares de (máx + 2mín) — el umbral de apilabilidad. Dicotomía
sobre el radio real R_P de la sartén de P (que empaqueta {α, o₁, m}
top-level, con m top-level per P): si todos los pares son no
apilables a R_P, la necesidad del trío da R_P ≥ R₃; si algún par es
apilable a R_P, entonces R_P ≥ máx+2mín de ese par ≥ M. En ambos
casos R_P ≥ mín(R₃, M): cota INCONDICIONAL. El script usa
R = máx(pares, mín(R₃, M)) y además CHEQUEA explícitamente (ronda
hostil: antes solo se afirmaba) que en todo el dominio muestreado,
cuando R₃ > pares (trío activo), R₃ ≤ M — 0 violaciones — luego
mín(R₃, M) = R₃ y la necesidad del trío aplica tal cual. El margen
M − R₃ se anula EXACTAMENTE solo en el punto áureo
(α, o₁) = (2, 2/φ): ahí pr(α,o₁) = 1 y pr(α,m) + pr(o₁,m) = 1
(identidades exactas, sympy: o₁ = 2/φ es la raíz de o₁²+2o₁−4 = 0),
la suma del trío a R = o₁+2 es exactamente 2π, y a la vez
α+o₁ = o₁+2 = M = 1+√5: pares = R₃ = M colapsan y el intervalo
peligroso [M, R₃) es vacío. Fuera del dominio (o₁ < 2/φ) sí hay
R₃ > M: la restricción o₁ ≥ (1+Σ)/φ > 2/φ es la que salva la cota,
y por eso el check es obligatorio, no decorativo. La corona se
construye a R (el peor): θ decrece en R, luego cabe a R_P ≥ R.

## 4. El teorema

**Teorema (gap lemma, anidado j ≤ 1).** En la plantilla anidada con
j ≤ 1, ρ ≤ φ implica que el intercambio no se bloquea, para todo ω
(incluido pivote sólido), todo perfil y todos los extras/polvo.
*Prueba.* Reparto de §2; en R ≥ máx(pares, mín(R₃, M)) (necesidades
escritas: dos círculos exacto + trío blindado §3), la corona de ≤ 5
piezas cabe en todo el dominio con los suelos HONESTOS (Σ_S ∈
[0, Σ] libre): j = 0, 20000–50000 instancias + esquinas
deterministas (Σ_S ∈ {0, Σ/2, Σ}, trade-off s′/w* con la ligadura
de masa exacta en el suelo mínimo) + límite α → ∞ por fórmula, 0
fallos; j = 1, 10000–25000 instancias + esquinas (navaja, suelo
mínimo Σ_S = 0, doble suelo α = o₁ = (1+Σ)/φ con trade-off y o₁
hasta 20, límite α → ∞), 0 fallos, check de no-apilabilidad en
verde. El criterio k ≤ 5 es exacto POR INSTANCIA; el sup sobre el
dominio es barrido + esquinas (§6). ∎

El límite α → ∞ (j = 0) es benigno por fórmula: con R = α+1,
θ(α, x) → 2 asin √x y los θ entre piezas chicas → 0; en el orden
[1, s′, α, w*] el π diametral del par (α, 1) absorbe θ(α, s′) ≤
2 asin √(φ/2) ≈ 2.24 < π y el total límite es π + 2 asin √(1/φ) =
4.951 < 2π (margen 1.33); puntos hasta α = 10⁴ lo confirman (j = 0
y j = 1).

Controles: violar el suelo α ≥ Σ_S+ω hace fallar el cuarteto (las
legalidades del testigo pagan); la navaja no bloquea la corona
directa (R₃ = 2.573, quinteto cabe). Margen del núcleo j = 0 con el
suelo honesto mínimo: s′ puede crecer ≥ 0.007 sobre su tope —
positivo pero FINO (el 0.021 del v1 venía del suelo inflado Σ+ω; la
esquina crítica real está más apretada).

## 5. Consecuencia

Con `insercionanidada.md` (j ≥ 2) + este teorema (j ≤ 1), la
plantilla anidada del caso (b) queda CERRADA para todo j, ω, σ₂,
perfil y extras, al estándar del §6 (los extras top-level de la
sartén en j ≤ 1 van a la fila de D_m o a w*, y su masa está contada
en Σ: sin hueco entre los dos teoremas — j ∈ {0, 1} aquí, j ≥ 2
allá). El residuo escrito-pendiente del programa τ = φ se reduce a:
el puerto ((c-ii) con j′ ≤ 1 de la sartén real y la raíz compartida
R2b como redacción) y el lema de optimización de los sups.

## 6. Estatus

Exacto (teorema): legalidad del reparto (certificado de F +
maximalidad de m + D_m + llenado greedy con lem:row + disco-1 como
pieza), P1 + partición del círculo (necesidad angular), la cota
blindada del trío R_P ≥ máx(pares, mín(R₃, M)) (dicotomía
apilable/no apilable, incondicional), el punto áureo (2, 2/φ) con
pares = R₃ = M = 1+√5 (identidades sympy), las ligaduras de masa
s′ ≤ mín(Σ/2, φ/2) y W″ < mín(1/φ, Σ−1, Σ−2s′), el criterio k ≤ 5
por instancia (exhaustivo en órdenes), y el límite α → ∞ (por
fórmula, margen 1.33). Numérico-certificado: que la corona cabe en
TODO el dominio es un sup sobre la caja muestreado (barridos con
suelos honestos + esquinas deterministas + estrés 150k/semillas);
el cierre formal del sup es el mismo lema de optimización pendiente
que en `insercion.md`/`insercionanidada.md`. El check de
no-apilabilidad (R₃ ≤ M en las instancias activas) es parte del
barrido, no un teorema aparte — fuera del dominio (o₁ < 2/φ) es
FALSO, así que no puede suprimirse.
