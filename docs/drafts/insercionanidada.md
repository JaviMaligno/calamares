# Inserción por sombras en la plantilla anidada: teorema j ≥ 2

Estado: DRAFT con pruebas (2026-08-09), ADVERSARIADO (acta en
VEREDICTOS.md, misma fecha; segunda ronda vía el puerto escrito,
misma fecha: bloque F añadido). Script: `code/insercionanidada.py`
(6/6). Espejo anidado de `insercion.md`.

## 1. El reparto testigo

Plantilla caso (b): u = agujero de α (α top-level en la sartén),
v = sartén; P tiene m top-level en la sartén y S en el agujero de α;
F tiene m en el agujero de α. Masa suelta: Σ := S + extras + polvo
(todo lo < m que hay que recolocar; si Σ ≤ 1 la fila de D_m se lo
traga entero y el intercambio cierra: en adelante Σ ∈ (1, φ]). La
colocación:

1. La sartén TOP-LEVEL según P: solo m se va (su disco unidad D_m
   queda vacante). m entra en el agujero de α y el INTERIOR del
   agujero se recoloca según el certificado de F: cuando F colocó m,
   los ocupantes del agujero eran exactamente los anillos > m que P
   le asigna (m es el mayor discrepante y F procesa en orden
   decreciente: nada < m estaba colocado aún), y F certificó ese
   conjunto + m; cada anillo viaja con su subárbol rígido
   (thm:oblivious). S (todo lo < m del agujero según P) sale entera;
   el polvo/extras < m top-level de la sartén salen también.
2. LLENADO GREEDY de D_m: fila (lem:row) con la masa suelta en orden
   decreciente hasta la primera pieza que no cabe, s′. El peor caso
   es (D): s′ = σ₂ con σ₁+σ₂ > 1; s′ puede ser también un extra de
   la sartén.
3. s′ mural en la sartén por el Lema de inserción (`insercion.md`,
   Lema A), presupuesto sobre {α, o₁..o_j, D_m como pieza de radio
   1} a las posiciones REALES de P (la cota de sombra es uniforme en
   la profundidad; contar D_m entero cubre la fila de dentro). El
   presupuesto crece en s: cubrir el tope min(Σ/2, φ/2) cubre todo
   s′ posible.
4. El resto W″ como círculo-fila w* ≤ 1/φ (lem:row), inserción de
   nuevo con la sombra de s′ ya contada. La cota de masa es EXACTA:
   fila colocada + s′ > 1 (la fila falló en s′) y cola(m) ≤ φ dan
   W″ < φ − 1 = 1/φ. Esto cierra también el caso σ₁+σ₂ ≤ 1 < Σ (el
   draft v1 lo dejaba abierto: con solo σ₁ en D_m la cota 1/φ no
   salía).

## 2. Las dos paredes exactas

**Tope del insertando (incondicional en ω).** El greedy mete primero
la mayor pieza suelta ℓ₁ (< 1: siempre cabe), luego s′ ≤ ℓ₂ (segunda
mayor). De ℓ₁+ℓ₂ ≤ Σ y ℓ₁+ℓ₂ ≤ cola(m) ≤ φ:

    s′ ≤ min(Σ/2, φ/2),   exacto, para piezas de S Y para extras.

Sin condición alguna en ω — la versión v1 (2σ₂ ≥ 1+ω > φ sii
ω > φ−1) era innecesariamente débil y declaraba una franja
{j = 2, ω ≤ φ−1, σ₂ ∈ [0.95, 1)} que en realidad es vacía por masa.
D4 = {j = 2, ω ∈ [φ/2, 1)} queda subsumida (φ/2 > φ−1 exacto). La
cota (α−ω)/2 del par del testigo dentro del agujero NO se usa (no
vale para extras).

**Régimen automático (j ≥ 2, uniforme).** Sea T = {α, o₁..o_j} el
top-level ≥ m de la sartén, |T| = j+1 ≥ 3, ordenado t₁ ≥ t₂ ≥ t₃…
La cascada con ρ ≤ φ (convenio de primera copia, adversariado en la
sartén; toda la masa suelta y m están bajo cada t):

    t₃ ≥ (1+Σ)/φ,   t₂ ≥ (t₃+1+Σ)/φ ≥ (1+Σ)(1+φ)/φ² = 1+Σ ≥ 2

(identidad φ² = 1+φ). El par de P (dos círculos en un disco sii la
suma de radios cabe) da R ≥ t₁+t₂, luego para TODA pieza x del
presupuesto: R − x ≥ R − t₁ ≥ t₂ ≥ 2 > φ ≥ 2s′ y 2 > 2/φ = 2w*.
Ambos regímenes son estrictos con margen 2−φ, sin usar
α ≥ σ₁+σ₂+ω. El viejo régimen «s < (1+ω)/2» descansaba en la
premisa o₁ ≥ 1+ω, que NO es una necesidad de los ocupantes (solo α
admite a m en su agujero); el lema automático lo reemplaza y lo
mejora.

## 3. La cobertura (medida con la cascada anidada real)

Con las dos paredes, el único requisito restante es el PRESUPUESTO:
ambas sumas de sombras < 2π en s = s′ y en w* = 1/φ. Medido por
instancia (bisección s_cap con `cascada_anidada` real, suelo honesto
α ≥ 1+ω, rank de α barrido, holguras + esquinas deterministas con
holgura 1 exacta, Σ → 1⁺, Σ = φ, ranks extremos; R = par mínimo, el
peor por monotonía; margen 0.05):

- j ≥ 2: presupuestos bajo 2π − 0.05 hasta el objetivo por instancia
  min(Σ/2, φ/2) — el tope exacto de s′ — con CERO fallos (s_cap
  observados ≥ 0.94 en j = 2, 0.999 en j ≥ 3): cobertura COMPLETA
  en todo ω, todo σ₂ y todos los extras.
- Holgura GRANDE (bloque F, exigido por la ronda hostil del puerto):
  piezas hasta 10⁴ sobre el suelo (una y dos infladas a la vez, rank
  barrido, MC log-uniforme), ω hasta 1.35 (pivote sólido incluido —
  ω entra solo vía el suelo 1+ω), 0 fallos de régimen (t₂ ≥ 1+Σ es
  exacto e independiente de holguras) y peor presupuesto 5.2115 EN
  EL SUELO h = 1: inflar solo ayuda. Límite t → ∞ POR FÓRMULA: con
  R = t+t₂, la sombra de t → π (razón → 1, régimen t₂−2s ≥ 2−φ
  exacto) y las demás → 0: presupuesto → π < 2π, margen π (análogo
  del bloque D de `gaplemma.py`). Con esto el dominio admite valores
  ARBITRARIOS sobre los suelos — lo que necesita (c-ii-1), donde la
  raíz t de la torre viene inflada por la torre entera.
- j ≤ 1: NO cubierto — muere por PRESUPUESTO en la navaja exacta
  o₁ = (1+Σ)/φ → 2/φ contra el régimen de w*, 2w* = 2/φ: la razón
  (w*+α)/(R−w*) = (α+1/φ)/(α+2/φ−1/φ) = 1 IDÉNTICA en α (¡el mismo
  punto crítico áureo!), arcsin → π/2 y la sola α come π: territorio
  de D6, declarado.

**Teorema (anidado-escrito, j ≥ 2).** En la plantilla anidada con
j ≥ 2 ocupantes, ρ ≤ φ implica que el intercambio no se bloquea,
para todo ω, todo σ₂, todo perfil (k, p libres por masa) y todos los
extras/polvo de la sartén.
Prueba: el reparto de §1; la legalidad de (1)-(2) es exacta
(certificado de F + maximalidad de m + lem:row); las paredes de §2
son exactas; (3)-(4) por el Lema A con el presupuesto certificado
(mismo estándar que thm:D1written: una maximización certificada por
celda). ∎

D4 y D5 (k ≥ 4 fuera de la rama de reducción) quedan absorbidas en
el teorema: ni ω ni el tamaño del perfil aparecen.

## 4. Franja declarada (pinza dedicada pendiente)

{j ≤ 1} entera (D6: j = 0 con smalls; j = 1 con la navaja). Sigue
cerrada computacionalmente por la campaña `coronanidada`
(adversariada); convertirla exige repartos dedicados (candidatos:
H_m para W″ con ω < 1/2; partición de w* en dos círculos bajo el
régimen; la pinza I3-anidada de las campañas como techo de dominio).

## 5. Estatus

Exacto: legalidad del reparto (certificado de F + maximalidad de m +
D_m + llenado greedy con lem:row), cota W″ < 1/φ, tope del
insertando s′ ≤ min(Σ/2, φ/2) (incondicional), régimen automático
j ≥ 2 (cadena t₂ ≥ 1+Σ con φ² = 1+φ; margen 2−φ), navaja j = 1
(razón idéntica 1), límite t → ∞ (por fórmula, margen π), suelo
t ≥ Σ_S+ω automático en raíces de torre (sympy, dos ramas: ω ≥ φ−1
vía 1+2ω; ω < φ−1 vía cascada con Σ+ω ≤ 2φ−1 < 2φ).
Numérico-certificado: los presupuestos < 2π sobre el dominio
muestreado (bisección por instancia + esquinas deterministas +
holgura grande hasta 10⁴ con ω hasta 1.35, margen ≥ 0.05); el
cierre formal del sup es el mismo lema de optimización pendiente
que en `insercion.md`. Controles: sin
la necesidad de par el presupuesto revienta; el tope es tight en
s′ = φ/2 (cola(m) = φ exacta, ℓ₁ = ℓ₂ = φ/2) y sigue en régimen con
margen 2−φ; el lema de régimen se valida en el muestreo (0 fallos
esperados y observados).
