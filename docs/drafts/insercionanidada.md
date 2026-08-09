# Inserción por sombras en la plantilla anidada: D4-D5 escrito

Estado: DRAFT con pruebas (2026-08-09), PRE-ADVERSARIO. Script:
`code/insercionanidada.py` (5/5). Espejo anidado de `insercion.md`.

## 1. El reparto testigo

Plantilla caso (b): u = agujero de α (α top-level en la sartén),
v = sartén; P tiene m top-level en la sartén y S en el agujero de α;
F tiene m en el agujero de α. La colocación:

1. La sartén según P, SIN MOVER NADA salvo m: m sale (su disco
   unidad D_m queda vacante top-level) y entra en el agujero de α
   según el certificado de F (el contenido > m del agujero es
   compartido; S sale entera; subárboles rígidos — thm:oblivious).
2. σ₁ → D_m (fila de uno, σ₁ < 1: siempre legal).
3. σ₂ mural en la sartén por el Lema de inserción (`insercion.md`,
   Lema A), presupuesto sobre {α, o₁..o_j, D_m como pieza de radio
   1} a las posiciones REALES de P.
4. El resto W' = S∖{σ₁,σ₂} + polvo + extras, de masa < 1/φ
   (cola de m y (D): σ₁+σ₂ > 1 porque la fila del par en D_m falla),
   como un círculo-fila w* ≤ 1/φ (lem:row), inserción de nuevo.

Régimen sombra (del par de la sartén de P, dos círculos exacto):
R ≥ α + máx(o₁, 1) y R ≥ o₁+o₂ (j ≥ 2) ⟹ R − x > 2s para toda
pieza sii s < techo de régimen; la segunda inserción exige además
R − x > 2/φ para toda pieza.

## 2. La cobertura (medida con la cascada anidada real)

s_cap(j, ω) := mayor s con ambos presupuestos < 2π − 0.05 sobre el
dominio (cascada anidada con rank de α barrido y holguras; R = par
mínimo, el peor por monotonía):

- j ≥ 3: s_cap = 0.999 para TODO ω: cobertura COMPLETA (todo σ₂ < 1,
  todo k, p — son masa).
- j = 2: s_cap ≈ 0.95 para todo ω; la ESQUINA-MASA cubre
  σ₂ > φ/2 cuando ω > φ−1 (σ₁+σ₂ ≥ 2σ₂ ≥ 1+ω > φ revienta la cola
  de m; y φ/2 > φ−1 exacto: (2−φ)/2 > 0) ⟹ **D4 = {j = 2,
  ω ∈ [φ/2, 1)} CUBIERTA ENTERA**; para ω ≤ φ−1 queda la franja
  σ₂ ∈ [~0.95, 1) DECLARADA.
- j ≤ 1: NO cubierto — la segunda inserción muere en la navaja
  exacta o₁ = (1+Σ)/φ → 2/φ contra su régimen 2w* = 2/φ (¡el mismo
  punto crítico áureo!): territorio de D6, declarado.

**Teorema (anidado-escrito, j ≥ 2).** En la plantilla anidada con
j ≥ 2 ocupantes, ρ ≤ φ implica que el intercambio no se bloquea,
para todo perfil (k, p libres por masa) y:
- j ≥ 3: todo ω y todo σ₂;
- j = 2: todo ω > φ−1 (en particular D4 entera); y σ₂ ≲ 0.95 si
  ω ≤ φ−1.
Prueba: el reparto de §1; la legalidad de (1)-(2) es exacta; (3)-(4)
por el Lema A con el presupuesto certificado (mismo estándar que
thm:D1written: una maximización certificada por celda). ∎

D5 (k ≥ 4 fuera de la rama de reducción) queda absorbido en los
rangos cubiertos: el tamaño del perfil no aparece.

## 3. Franjas declaradas (pinza dedicada pendiente)

{j ≤ 1} (D6: j = 0 con smalls, j = 1 con la navaja) y
{j = 2, ω ≤ φ−1, σ₂ ∈ [s_cap, 1)}. Ambas siguen cerradas
computacionalmente por la campaña `coronanidada` (adversariada);
convertirlas exige repartos dedicados (candidatos: H_m para W' con
ω < 1/2; partición de w* en dos círculos bajo el régimen; la pinza
I3-anidada de las campañas como techo de dominio).

## 4. Estatus

Exacto: legalidad del reparto (certificado de F + D_m + lem:row),
(D), esquina-masa (2σ₂ ≥ 1+ω > φ ⟺ ω > φ−1), régimen por pares.
Numérico-certificado: los s_cap (bisección por instancia sobre el
dominio muestreado con márgenes ≥ 0.05). Controles: sin la necesidad
de par el presupuesto revienta; la esquina-masa es tight en ω = φ−1.
