# La pesada especular con TODAS las X > 0 (espfinal)

Estado: v2 (2026-08-18), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — una grieta de solidez quirúrgica en
el cap del bloque F, reparada con impacto numérico nulo;
reparaciones R1-R5 aplicadas). Script: `code/espfinal.py`
(bloques A/C/D/E/F verdes; el B&B del bloque B por bandas, mapa
§3).

## 1. El objetivo y las paredes

Cerrar la pesada especular con X_α/X_z/X_m > 0 (además del
X_Y > 0 de esppesada), completando la celda especular dentro del
convenio (todas las X = polvo < m; el canal ocupante ≥ r_m sigue
model-conditional). **La pared del polvo total** (cola global de
m): ΣS+X_m+X_α+X_z+μ_Y ≤ φ ⟹ cada masa X < φ−1 = 0.618 — los
topes de muestreo del barrido (X_α ≤ 1.5, X_z ≤ 1) dejan de ser
topes; ω ≤ 1.6 sí sigue siendo tope de barrido (ω no es polvo).

## 2. El criterio (v5)

Base esppesada (fusión de polvo, tramos de μ_Y **K = 4** con
crédito de cola — el acta corrigió el «K = 8» del v1: era el
código de esppesada, no el de este script —, pared pesada como
poda, cota acoplada en z) más:

- **Ventanas X de G-g pesada**: α con +X_α en suelo y techo
  (techo de partición con el clamp de β por ligadura), z con
  +X_z, cola con +X_m+X_α+X_z, techo de μ_Y descontando los
  suelos de las X.
- **X_m sin dimensión**: solo entra por su extremo inferior
  (cola +, techo de polvo −, poda) ⟹ X_m = 0 uniformemente
  pesimista — teorema de una línea.
- **X_z sin dimensión**: tramos KZ = 2 con crédito (su techo solo
  entra en el clamp de la ventana de z; verificado término a
  término por el acta).
- **Bloque de polvo PARTIBLE**: el cuello geométrico — el bloque
  atómico no podía repartir masa entre los dos semicírculos y un
  lado se saturaba; el greedy parte cualquier multiconjunto de
  piezas ≤ cap en mitades con |m₁−m₂| ≤ cap ⟹ certificar dos
  sub-bloques de masa M/2+cap/2 cubre todo reparto real
  (`_antipodal2`/`_peor_camino2`: pesos internos POR NODO).
- **Cuatro variantes en OR** (pliegue sí/no × bloque
  único/partido), ordenadas por tasa de éxito.

## 3. El mapa (todo v5 congelado)

- **Bloque F — la franja por REDUCCIÓN DE DEGENERACIÓN**:
  ΣS ∈ (1, 1.016] con X_α, X_z, μ_Y y ω ENTEROS, en **85 cajas**
  (4 dims). La reducción: la pared pesada da σ₂ ≤ ε₀ = 0.016
  (S = σ₁ + polvo fino), el greedy llena β ≥ 1−ε₀ (fuzz 4.075
  perfiles, 0 violaciones), la ventana de α tiene ancho
  1−β ≤ ε₀ y la de z ancho σ₂ ≤ ε₀: el dominio colapsa a
  (ω, X_α, X_z, μ_Y) con holguras ε₀ pesimistas. **Cap del polvo
  2ε₀** (reparación R1 del acta — su única grieta de solidez: σ₁
  puede quedar excluida de B* y caer en A con ε₀ < σ₁ ≤ ΣA ≤ 2ε₀,
  contraejemplo DP del referee; el fix es de una línea y el B&B
  queda idéntico 85/43). La singularidad de coste que bloqueó el
  barrido de 14 dims (decenas de runs matados por la máquina) se
  disuelve. β ≥ 1−ε₀ es TEOREMA (greedy; fuzz del acta con σ₁
  bajos: 0/4000, peor β = 0.9964).
- **Bloque B — bandas de ΣS** (14 dims): [1.016, 1.025] 11.977
  cajas; [1.025, 1.05] 10.595; [1.05, 1.1] 5.207; [1.1, 1.2]
  2.155; [1.2, 1.4] 1.861; [1.4, φ] 283 — **~32.100 cajas**,
  todas verdes.
- Sanity (C): 200/200 instancias pesadas reales con TODO explícito
  (partición B*/A con su polvo en la carga, X's bajo el
  presupuesto, μ_Y en 1..3 piezas, Y en su suelo; clip ΣS ≤ φ−0.05
  declarado). Controles (D): negativos del motor viejo Y del nuevo
  `_antipodal2` (reparación R3) + poda del polvo total. El lado
  vacío de `_peor_camino2` queda como conservador deliberado
  (reparación R4: no porta la guarda del acta de areduccion —
  solo endurece — para no invalidar los recuentos del mapa). El
  acta re-ejecutó 4/6 bandas con recuentos EXACTOS y F a tres ε₀
  (0.016 → 85/43; 0.010 → 83/42; 0.004 → 75/38).

## 4. Estatus

Con este certificado, **la celda especular COMPLETA queda cerrada
dentro del convenio**: ligera (r2bmulti + espkp) y pesada
(areduccion + esppesada + espfinal) con todas las X de polvo en
todo su rango legal. Residuo especular: el canal ocupante ≥ r_m
(model-conditional, tarifa sin derivar) y el tope de barrido
ω ≤ 1.6. Técnicas nuevas exportables: la pared del polvo total,
dimensiones eliminadas por monotonía/tramos, el bloque partible,
y la reducción de degeneración (14 dims → 4 en la franja
ΣS → 1).
