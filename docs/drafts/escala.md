# La ley de escala: el lema del bolsillo-φ (p, k exactos) y j extendido

Estado: script `code/escala.py` 5/5 (2026-08-08), PRE-ADVERSARIO.
Reduce el asterisco de escala (j, p, k) de todas las campañas.

## 1. El lema del bolsillo-φ (EXACTO): p y k libres

**Lema.** En D1/D3 (j ≥ 3, ρ ≤ φ, Σ > 1), el perfil y el polvo
enteros (piezas < m, cantidad arbitraria) caben en fila en UN
bolsillo del par mayor {o₁, o₂} colocado adyacente-tangente en la
corona. En consecuencia las direcciones p (tamaño del perfil) y k
(número de pequeños) del asterisco de escala quedan CERRADAS EXACTAS,
condicionadas solo a la corona de ocupantes (dirección j).

*Prueba.* (i) En R = o₁+o₂ el discriminante de Descartes del par
mural tangente se anula IDÉNTICAMENTE (sympy): el bolsillo vale
p = 1/(1/o₁ + 1/o₂ − 1/(o₁+o₂)). (ii) p crece en o₁, o₂ (derivada
exacta −1/o₁² + 1/(o₁+o₂)² < 0 para k_p) y en R (k_w = −1/R).
(iii) La cascada con j ≥ 3 da o₂ ≥ 2 y o₁ ≥ 2φ exactos (identidades
(2/φ+2)/φ = 2 y o₁ᵐⁱⁿ = 2φ, ya en coronacolas [A]), y
**p(2φ, 2, 2φ+2) = φ EXACTO** (1/(2φ) + 1/2 − 1/(2φ+2) = 1/φ).
(iv) Toda pieza pequeña es < m = 1 y su suma vive en la cola de m:
masa total ≤ φ·r_m = φ. (v) Fila en el bolsillo por el lema de fila
(suma ≤ capacidad). Masa < φ ≤ bolsillo. ∎

El lema es TIGHT: masa → φ al agotar la cola de m y bolsillo = φ en
el mínimo de la cascada — otra aparición del punto crítico áureo.
Control: en la instancia áurea (j = 1) el bolsillo es φ/2 < φ: el
lema exige j ≥ 3 (fuera mandan DP/DPp, y la áurea es su frontera).

## 2. La dirección j: extendida y con estructura exacta

- Barridos extendidos con dualidad tangente uniforme (déficit 0.0 en
  R = R_lb): sartén j = 3..9 (p = 4..10), anidado j = 1..8. El rango
  triplica el de las campañas.
- Estructura exacta: la masa acumulada de la cascada crece con razón
  ≥ φ POR NIVEL (T_{k−1} = T_k + o_{k−1} ≥ T_k(1 + 1/φ) = T_k·φ,
  con 1 + 1/φ = φ exacto): los ocupantes crecen geométricamente y la
  espina queda acotada (≤ 7 en todos los barridos de zigzag [C]).
- La dirección j sigue siendo el único paso numérico del programa
  τ = φ, ahora con rango extendido, crecimiento geométrico exacto y
  el mecanismo p/k despejado.

## 3. Qué es exacto y qué no

EXACTO (sympy): disc = 0 idéntico en R = o₁+o₂; p(2φ,2,2φ+2) = φ;
monotonías del bolsillo; o₂ ≥ 2, o₁ ≥ 2φ; masa ≤ φ (cola de m);
1 + 1/φ = φ (razón de la cascada). [ENUNCIADO]: el lema de fila del
paper y la colocación adyacente del par en la corona (la realizan los
barridos con déficit 0). NUMÉRICO: la dualidad tangente en los rangos
extendidos de j.
