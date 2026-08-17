# La pesada especular con TODAS las X > 0 (espfinal)

Estado: **WIP, PRE-ADVERSARIO EN CURSO** (2026-08-17). Script:
`code/espfinal.py` (bloques A/C/D verdes; el B&B del bloque B con
el mapa de bandas de abajo, criterio evolucionado v2→v5 DURANTE el
barrido — **el verde oficial exige re-barrer todo con el criterio
congelado**). NO se reclama cierre todavía.

## 1. El objetivo y las paredes

Cerrar la pesada especular con X_α/X_z/X_m > 0 (además del X_Y > 0
de esppesada), completando la celda especular. Dentro del convenio
(todas las X = polvo < m): **la pared del polvo total** (cola
global de m) da ΣS+X_m+X_α+X_z+μ_Y ≤ φ ⟹ cada masa X < φ−1 =
0.618 — los topes de muestreo del barrido (X_α ≤ 1.5, X_z ≤ 1)
dejan de ser topes; ω ≤ 1.6 sí sigue siendo tope de barrido.

## 2. El criterio (v5) y sus lecciones

Base esppesada (fusión de polvo, tramos de μ_Y, pared pesada, cota
acoplada) más: ventanas X de G-g pesada; **X_m sin dimensión**
(solo entra por su extremo inferior: X_m = 0 uniformemente
pesimista — teorema de una línea); **X_z sin dimensión** (tramos
KZ = 2 con crédito: su techo solo entra en el clamp de la ventana
de z); **bloque de polvo PARTIBLE** (el cuello geométrico: el
bloque atómico no podía repartir masa entre los dos semicírculos y
un lado se saturaba; el greedy parte cualquier multiconjunto de
piezas ≤ cap en mitades con |m₁−m₂| ≤ cap ⟹ certificar dos
sub-bloques de masa M/2+cap/2 cubre todo reparto real); **cuatro
variantes en OR** (pliegue sí/no × bloque único/partido, ordenadas
por tasa de éxito — el pliegue de piezas medianas infla y el
bloque único satura); clamp de β por ligadura. Chunking por
CC_SS_LO/HI, CC_XP_LO/HI, CC_W_LO/HI (la máquina mata runs > ~10
min; el DFS no es resumible).

## 3. El mapa de bandas (verdes con criterio MIXTO — re-barrer)

- ΣS ∈ [1.016, φ] × X_α entero: verde (v2; [1.4,φ] 403, [1.2,1.4]
  2325, [1.1,1.2] 2247, [1.05,1.1] 6521, [1.025,1.05] 13165,
  [1.016,1.025] 14209).
- ΣS ∈ [1.0, 1.016] × X_α ∈ [0.155, 0.618]: verde (v2/v3; 157 +
  397).
- ΣS ∈ [1.008, 1.016] × X_α < 0.155: verde (v4; ω[0,0.4] 7649,
  ω[0.4,0.8] 6765, ω[0.8,1.6] 633).
- ΣS ∈ [1.004, 1.008] × X_α < 0.155: verde (v4; 17815 + 7951 +
  665).
- ΣS ∈ [1.0, 1.004] × X_α < 0.155: ω[0.8,1.6] verde (v4, 713);
  **ω ∈ (0, 0.8) PENDIENTE** — la singularidad de coste pegada a
  ΣS = 1 (el techo del polvo φ−ΣS máximo con la pesada
  casi-degenerada σ₂ ≤ 0.004) no cabe en el tope de tiempo de la
  máquina ni con v5.

## 4. Plan de cierre (próxima sesión)

(i) Congelar el criterio v5; (ii) re-barrer TODAS las bandas del
mapa (runs cortos, ~16 llamadas); (iii) la lasca [1.0, 1.004] ×
X_α < 0.155 × ω ∈ (0, 0.8): más mitades de ω/X_α con máquina
descargada, o derivación analítica del límite ΣS → 1 (la pesada
degenerada: β → 1, A → polvo, ventana de α de ancho ≤ ΣS−1 —
candidata a tratamiento tipo f3vacio); (iv) borrador final + ronda
hostil + acta.
