# El gap lemma escrito: anidado j ≤ 1 por corona directa

Estado: DRAFT con pruebas (2026-08-09), PRE-ADVERSARIO. Script:
`code/gaplemma.py` (5/5). Cierra la última celda anidada; con
`insercionanidada.md` (j ≥ 2), la plantilla anidada queda ENTERA.

## 1. La observación que lo desbloquea

La navaja áurea mata el método de sombras en j ≤ 1, pero allí la
sartén es una familia ACOTADA: {α, (o₁ si j = 1), el disco unidad
con la fila greedy de D_m dentro, s′, w*} — a lo sumo 5 círculos.
No hacen falta sombras: el criterio mural directo de k ≤ 5 piezas
(mín exhaustivo sobre ≤ 12 órdenes cíclicos; posiciones por camino
más largo con TODAS las parejas validadas — solidez adversariada en
zigzag/compactación) es EXACTO y finito, y el dominio es una caja
compacta: maximización certificada, el estándar de thm:DPr.

## 2. El reparto y las cotas (heredadas, exactas)

Idéntico al del teorema j ≥ 2 salvo el paso mural: (1) m → agujero
de α por el certificado de F; (2) llenado greedy de D_m (fila
decreciente hasta s′); (3) REPACK MURAL de la sartén entera con las
≤ 5 piezas (el disco-1 con la fila dentro es una pieza: lem:row,
interior no visible; el repack es recurso legal — pan repack de
thm:DP); (4) s′ ≤ mín(Σ/2, φ/2), W″ < mín(1/φ, Σ − ℓ₁ − s′) ≤
mín(1/φ, Σ − 2s′) (¡ligadura de masa que hace INFACTIBLE la esquina
s′ = φ/2 ∧ w* = 1/φ simultáneos!), Σ ∈ (1, φ].

## 3. La necesidad del trío (la pieza nueva, teorema)

Para j = 1 el par mínimo R = máx(α+o₁, o₁+1) NO basta (en la navaja
α = o₁ = 2/φ el trío {α, o₁, m} suma > 2π ahí). La cota correcta es
la NECESIDAD DEL TRÍO: cualquier disco que empaquete {a, b, c} con
pares no apilables cumple θ(a,b) + θ(b,c) + θ(c,a) ≤ 2π (P1 +
partición del círculo — teorema, `compactacion.md`; para tres piezas
todos los órdenes cíclicos son el mismo ciclo). R₃(α, o₁, m) se
define por la igualdad y P empaqueta el trío: R ≥ R₃. En el rango
relevante los pares son no apilables (R₃ < máx + 2mín: verificado en
el barrido; p.ej. navaja: R₃ = 2.57 < 3.24).

## 4. El teorema

**Teorema (gap lemma, anidado j ≤ 1).** En la plantilla anidada con
j ≤ 1, ρ ≤ φ implica que el intercambio no se bloquea, para todo ω
(incluido pivote sólido), todo perfil y todos los extras/polvo.
*Prueba.* Reparto de §2; en R ≥ máx(pares, R₃) (necesidades
escritas: dos círculos exacto + trío §3), la corona de ≤ 5 piezas
cabe en todo el dominio: j = 0, 20000 instancias + esquinas
deterministas + límite α → ∞, 0 fallos, margen ≥ 0.021 en toda la
malla del núcleo; j = 1, 10000 instancias + esquinas (navaja
incluida, con la ligadura de masa exacta), 0 fallos. Maximización
certificada. ∎

Controles: violar el suelo α ≥ Σ+ω hace fallar el cuarteto (las
legalidades del testigo pagan); la navaja no bloquea la corona
directa (R₃ = 2.573, quinteto cabe).

## 5. Consecuencia

Con `insercionanidada.md` (j ≥ 2) + este teorema (j ≤ 1), la
plantilla anidada del caso (b) queda CERRADA COMO TEOREMA ESCRITO
para todo j, ω, σ₂, perfil y extras. El residuo escrito-pendiente
del programa τ = φ se reduce a: el puerto ((c-ii) con j′ ≤ 1 de la
sartén real y la raíz compartida R2b como redacción) y el lema de
optimización de los sups.
