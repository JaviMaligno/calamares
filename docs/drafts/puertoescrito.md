# El puerto escrito: (c-ii) y R2b como teoremas

Estado: DRAFT (2026-08-09), ADVERSARIADO (acta en VEREDICTOS.md,
misma fecha: CONFIRMADO CON CORRECCIONES; las cuatro reparaciones
integradas aquí y en `code/insercionanidada.py` bloque F). Ensambla
piezas ya adversariadas (puertocii.py bloques A/F/G, insercionanidada
6/6, gaplemma). Es la última familia de celdas del programa τ = φ.

## 1. (c-ii-1) es un COROLARIO de los teoremas anidados

**Corolario.** En (c-ii-1) (v = sartén, α anidada en una torre con
raíz t top-level), ρ ≤ φ implica que el intercambio no se bloquea,
para todo j′ (ocupantes reales de la sartén), ω, perfil y extras —
al estándar heredado de los teoremas anidados (§6 de sus drafts:
exacto en ligaduras y regímenes, numérico-certificado en el sup del
presupuesto; el lema de optimización pendiente es el mismo).

*Prueba.* Los teoremas thm:nestedwritten (j ≥ 2) y thm:gapwritten
(j ≤ 1) usan de la configuración exactamente cuatro cosas:
(i) la sartén de P contiene una familia top-level {grande t, o₁..o_j,
m}; (ii) m sale dejando D_m vacante top-level (v = sartén ⟹ m ES
top-level en P); (iii) el destino de m es legal por el certificado de
F con subárboles rígidos — agnóstico a CUÁL agujero recibe a m: aquí
m va al agujero de α DENTRO de la torre (la torre es la misma en F y
P por el esqueleto compartido; certificado igual de legal); (iv) las
cotas de masa (cola de m, greedy, topes). En (c-ii-1) todas valen con
t (la raíz de la torre de α) en el papel del «α» de los teoremas, y
los suelos que los dominios imponen EN CADA RANGO se satisfacen:
t cumple la cascada de su rango (su cola contiene lo que la cascada
asume — la torre entera, α incluida — y más: cola(t) ≥ (α + torre
interior + 1 + Σ)/φ), t ≥ α+ω ≥ 1+2ω por dos círculos nivel a nivel
(exacto), el suelo E4 sale automático (t ≥ Σ_S+ω por dos ramas,
sympy, bloque F0 — y además gaplemma barre Σ_S ∈ [0, Σ] libre), y
los o_i mayores que piezas de la torre solo engordan su cola
(dirección buena). Sobre los DOMINIOS certificados: `gaplemma.py`
admite valores arbitrarios sobre los suelos (esquinas hasta 10⁴ +
límite α → ∞ por fórmula, margen 1.33); `insercionanidada.py` lo
admite desde su bloque F (exigido por la ronda hostil de este draft):
holgura hasta 10⁴ con una y dos piezas infladas, ω hasta 1.35
(pivote sólido — ω entra solo vía el suelo 1+ω), 0 fallos de
régimen, peor presupuesto 5.2115 EN EL SUELO h = 1, y límite t → ∞
por fórmula (→ π, margen π). La configuración de (c-ii-1) vive
dentro de ambos dominios. ∎

## 2. (c-ii-2): el teorema ensamblado de las pinzas exactas

Piezas EXACTAS ya adversariadas (puertocii.py [A]/[F], actas):
- I1 (ligereza condicional) y la partición u/D_m con techo
  generalizado; I2 (rama Y ≥ α infactible salvo X_Y+ω > φ); I3 (la
  pinza de α: ventana vacía para ω_ef ≤ 3/(2φ), esquina (3/(2φ),
  1/2) exacta); forma cerrada ω_ef = ω + X_α − φ(2X_Y + X_m).
- Dentro de la caja R2: el repack de la sartén con el bolsillo
  espejo: α > 2 (N > 3+ω* ⟹ N/φ > 2 vía 2φ > 1), T ≥ Y > 2/φ =
  √5−1 (cola de Y con ΣS > 1), b₂ estrictamente creciente y
  b₂(2, √5−1) = 1 ⟹ b₂(α, T) > 1 > σ₂. EXACTO — condicionado a la
  legalidad del repack de la sartén ([ENUNCIADO] F2, confirmado
  contra la definición del paper en acta, formalización pendiente).
- Rama pesada: partición B*/A + pinza b₂(4/φ, 2/φ) = 12/(7φ) > 1.
- R2b (raíz compartida): el trío mural {Y, m, σ₂} en c = α−ω ≥
  ΣS+Y (tarifa), suma decreciente en c (exacto), sup = esquina
  certificada π + 4·asin(1/√3) < 2π (margen 0.68). El resto del
  bloque G (sup del interior, X′ > 0, rama pesada por cuarteto,
  profundidad d ≥ 2, espejo con tarifa derivada) es
  computacional-con-esquina-exacta: barridos sobre rangos declarados
  (ω ≤ 1.6, X ≤ 1–3, |W| ≤ 8), no pinzas exactas.

**Teorema (puerto, ensamblado).** En (c-ii-2), ρ ≤ φ implica no
bloqueo salvo en el residuo listado en §3, cuyo cierre sigue siendo
computacional. Con §1, el caso (c) entero del ensamblaje queda:
(c-i) heredado de (b) [teorema vía los anidados escritos, con sus
asteriscos de §6], (c-ii-1) corolario (mismo estándar), (c-ii-2)
teorema ensamblado módulo §3.

## 3. Lo que queda computacional (el residuo, lista COMPLETA)

Ramas 1-2: **CERRADAS** (2026-08-09, `coronaagujero.md` +
`code/coronaagujero.py` 5/5, adversariado — 0 contraejemplos en 55k
instancias): la plantilla anidada DENTRO del agujero (k ≥ 3 régimen
automático heredado; k ≤ 2 corona acotada + trío blindado), con el
lema de respiración fuerte (X_{>m}+ω > φ exacto tras descontar
polvo, vía √5−(φ−1) = φ) y la ventana exacta de c en corona-α.
Alcance k ≤ 14/12 con dirección k asterisco decreciente:
1. ~~(c-ii-2) rama Y ≥ α «respirando»~~ CERRADA (teorema, rama
   respirante).
2. ~~(c-ii-2) corona-α con X_α grande~~ CERRADA (teorema, corona-α
   con partición exacta B/{σ₂}).

Estatus computacional heredado (no ramas abiertas, sino asteriscos
de las piezas que el teorema ensambla — la ronda hostil exige
listarlos aquí):
3. Los barridos del bloque G de R2b al nivel
   computacional-con-esquina-exacta (rangos ω ≤ 1.6, X ≤ 1–3,
   |W| ≤ 8; la esquina del trío sí es certificada).
4. [ENUNCIADO] F2: legalidad del repack de la sartén (del que
   dependen las pinzas de bolsillo espejo F1e/F1f).
5. El gap-dualidad de F3 (≥ 3 tops casi iguales,
   R_fit/R_lb ≤ 1.0116) y las coronas de extras top-level, sobre
   sus rangos barridos (X ≤ 3, ω ≤ 1.35, d ≤ 3, j ≤ 3).
6. El lema de optimización de los sups (común a todos los teoremas
   escritos; opcional al estándar de thm:DPr).

Con §1-§2 integrados, el mapa del ensamblaje entero queda: (a)
teorema, (b) teorema, (c-i) teorema, (c-ii-1) corolario, (c-ii-2)
teorema módulo el residuo, R2b esquina-certificada — todos al
estándar de thm:DPr (exacto en ligaduras/regímenes,
numérico-certificado en los sups). El residuo computacional del
programa se reduce a las DOS ramas de agujero (§3.1-2) + los
asteriscos heredados (§3.3-6).
