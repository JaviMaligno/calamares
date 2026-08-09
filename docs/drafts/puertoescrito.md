# El puerto escrito: (c-ii) y R2b como teoremas

Estado: DRAFT (2026-08-09), PRE-ADVERSARIO, sin script propio aún —
ensambla piezas ya adversariadas (puertocii.py bloques A/F/G,
insercionanidada, gaplemma). Es la última familia de celdas del
programa τ = φ.

## 1. (c-ii-1) es un COROLARIO de los teoremas anidados

**Corolario.** En (c-ii-1) (v = sartén, α anidada en una torre con
raíz t top-level), ρ ≤ φ implica que el intercambio no se bloquea,
para todo j′ (ocupantes reales de la sartén), ω, perfil y extras.

*Prueba.* Los teoremas thm:nestedwritten (j ≥ 2) y thm:gapwritten
(j ≤ 1) usan de la configuración exactamente cuatro cosas:
(i) la sartén de P contiene una familia top-level {grande t, o₁..o_j,
m}; (ii) m sale dejando D_m vacante top-level; (iii) el destino de m
es legal por el certificado de F con subárboles rígidos (agnóstico a
CUÁL agujero recibe a m); (iv) las cotas de masa (cola de m, greedy,
topes). En (c-ii-1) todas valen con t (la raíz de la torre de α) en
el papel del «α» de los teoremas: m va al agujero de α DENTRO de la
torre (certificado de F, igual de legal), y los suelos del dominio
solo SUBEN (cola(t) ≥ (α + torre interior + 1 + Σ)/φ ≥ los suelos de
cola(α); t ≥ α + ω ≥ 1 + 2ω). Los dominios certificados de ambos
teoremas admiten valores arbitrarios por encima de los suelos
(holguras libres y límites α → ∞ por fórmula): la configuración vive
DENTRO de sus dominios. ∎

## 2. (c-ii-2): el teorema ensamblado de las pinzas exactas

Piezas EXACTAS ya adversariadas (puertocii.py [A]/[F], actas):
- I1 (ligereza condicional) y la partición u/D_m con techo
  generalizado; I2 (rama Y ≥ α infactible salvo X_Y+ω > φ); I3 (la
  pinza de α: ventana vacía para ω_ef ≤ 3/(2φ), esquina (3/(2φ),
  1/2) exacta); forma cerrada ω_ef = ω + X_α − φ(2X_Y + X_m).
- Dentro de la caja R2: el repack de la sartén con el bolsillo
  espejo: α > 2 (N > 3+ω* ⟹ N/φ > 2 vía 2φ > 1), T ≥ Y > 2/φ =
  √5−1 (cola de Y con ΣS > 1), b₂ estrictamente creciente y
  b₂(2, √5−1) = 1 ⟹ b₂(α, T) > 1 > σ₂. EXACTO.
- Rama pesada: partición B*/A + pinza b₂(4/φ, 2/φ) = 12/(7φ) > 1.
- R2b (raíz compartida): el trío mural {Y, m, σ₂} en c = α−ω ≥
  ΣS+Y (tarifa), suma decreciente en c (exacto), sup = esquina
  certificada π + 4·asin(1/√3) < 2π (margen 0.68); pesada por
  cuarteto; profundidad/espejo por barrido directo con tarifas
  derivadas.

**Teorema (puerto, ensamblado).** En (c-ii-2), ρ ≤ φ implica no
bloqueo salvo en las ramas listadas en §3, cuyo cierre sigue siendo
computacional. Con §1, el caso (c) entero del ensamblaje queda:
(c-i) heredado de (b) [ahora TEOREMA vía los anidados escritos],
(c-ii-1) corolario, (c-ii-2) teorema ensamblado módulo §3.

## 3. Lo que queda computacional (las últimas ramas)

1. (c-ii-2) rama Y ≥ α «respirando» (X_Y + ω > φ): cierre por
   corona-Y (computacional). Candidato escrito: familia acotada del
   agujero de Y ({X_Y grandes, D_m-disco, σ₂}) con la necesidad del
   trío — la jugada del gap lemma dentro del agujero.
2. (c-ii-2) corona-α con X_α grande (B2u como fila): ídem, familia
   del agujero de α.
3. El lema de optimización de los sups (común a todos los teoremas;
   opcional al estándar de thm:DPr).

Con §1-§2 integrados, el mapa del ensamblaje entero queda: (a)
teorema, (b) teorema, (c-i) teorema, (c-ii-1) corolario, (c-ii-2)
teorema módulo las dos ramas de §3, R2b esquina-certificada. El
residuo computacional del programa se reduce a DOS ramas de agujero
+ el lema de optimización.
