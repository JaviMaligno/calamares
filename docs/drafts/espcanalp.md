# La pesada del canal ocupante ≥ r_m (espcanalp)

Estado: v2 (2026-08-19), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — cero grietas de solidez; la
reducción de dimensión verificada como TEOREMA con fuzz 0/20.000
del referee; H1-H6 aplicadas: la pesada x-en-z d = 1 quedó
CERTIFICADA — no solo declarada — tras afinar el cap del bloque).
Script: `code/espcanalp.py` (5/5). El remate del canal tras
espcanal: el perfil PESADO (ΣS ≥ 1+σ₂) con el anillo extra x.

## 1. El criterio (10 dims): la reducción de dimensión (TEOREMA)

La caja es (ω, σ₂, ΣS, β, X_α, X_z, X_m, α, z, x) — 10 dims
frente a las 14+1 de espfinal+x (el primer intento con piezas
explícitas iba a 3.5 cajas/s: inviable; el reducido va a
~120-400). La reducción es viable GRACIAS a x: con x ≥ (1+ΣS)/φ
(pinza de la cola), c′ ≥ max(z+x, suelo del trío, cola(Y)−ω) es
mucho mayor que el 1+z de espfinal, y TODA la carga A = S∖B* se
paga POR MASA como bloque partible. **El teorema del cap**
(verificado por el acta, fuzz 0/20.000): toda pieza a ∈ A cumple
a ≤ min(β, φ/2, ΣA) — β ≥ σ₁ ≥ max(A) incluso con σ₁ ∈ A ({σ₁}
es candidato a B*), a ≤ φ/2 por maximalidad + ΣS ≤ φ (β+a > 1 y
ΣS ≥ β+a ≥ 2a), y a ≤ ΣA trivial (el refinamiento ΣA del cap —
reparación de la ronda — disolvió la única región atascada de la
pesada-z: β ≈ 0.81 daba cap 0.809 con masa 0.26). Variantes:
bloque único / partido (greedy |m₁−m₂| ≤ cap, teorema de
espfinal) / plegado sobre D_m / creciente corto, en OR. En la
variante creciente el bloque tiene radio cap < masa: sound — la
ventana ψ(cap) mayora las de las piezas r ≤ cap y la holgura
π·masa/z acota el span interno de la cadena (acta H3).

**Podas** (además de perfil y pared del polvo total): pinza de la
cola de x CON EMPATE (vacuidad del gemelo,
perfil-independiente); pared PESADA del nodo (A7) con
σ₁ ≤ min(β, 1); suelo del TRÍO (`suelo_trio`); par antipodal
(z, x) con cota acoplada (A5; con zl de caja: más pesimista que
z_lo, sound — acta §5); **β > 1/2 (poda nueva EXACTA)**: el
greedy del mejor subconjunto para solo cuando toda pieza restante
excede 1−β ⟹ σ₁ > 1−β, y σ₁ ≤ β (fuzz del acta: peor
β = 0.5095 — ajustada de verdad; el clamp usa la forma débil
1−bh para no alterar recuentos, acta H4). La poda disolvió una
banda fantasma con β ≈ 0 (63.894 cajas eps ilegales). Tramos
KZ = 2 × K = 4 heredados (Xzh muerto en el criterio — herencia
de espfinal, ineficiencia sin solidez, acta H6); cola de Y con
x; techo (RY+x).

## 2. La pesada x-EN-z (d = 1; acta H1)

`criterio_pesada_z`: x anidado en el agujero de z — la corona de
v NO cambia ({z, D_m} + bloques por masa; x viaja dentro de z,
lem:DG); cambian las ventanas de z (convivencia α+x, techo Rz+x,
cola de z con x) y la cola de Y. **Certificada ENTERA: 15.571
cajas, 0 sin resolver** (dominio completo, sin bandas).

## 3. El mapa (criterio CONGELADO v2, re-barrido entero)

| banda ΣS (x-en-v) | cajas vistas | certificadas |
|----------|-------------:|-------------:|
| [1.00, 1.05] | 51.713 | 11.924 |
| [1.05, 1.10] | 38.173 | 8.656 |
| [1.10, 1.20] | 20.377 | 7.339 |
| [1.20, 1.40] | 23.169 | 7.822 |
| [1.40, 1.62] | 10.905 | 2.248 |

(la etiqueta de la banda alta es su techo REAL de barrido 1.62 >
φ — acta H2; el exceso (φ, 1.62] se poda por ΣS > φ.) **Total
x-en-v: 144.337 cajas; + x-en-z: 15.571; todo 0 sin resolver, 0
truncado.** Persistencia de pila (CC_ESTADO/CC_TMAX); bandas por
CC_SSLO/CC_SSHI.

## 4. Verificación

[A] enunciado del criterio reducido + gate del techo de la pared
pesada. [B] el mapa + la pesada-z entera. [C] 200 instancias
pesadas legales con x explícito (partición B*/A real por
máscaras; X_z generada ANTES de x — acta H5 — para que la pinza
vea todo el polvo): corona cabe 200/200. [D] pinza del gemelo
poda; pared pesada poda; β < σ₂ poda; NO-TAUTOLOGÍA del
certificador (acta H3: la raíz de una banda da False — el mapa
certifica ~30%, el resto se parte o poda); negativos heredados
(espfinal D, espcanal D-R5). [E] estatus. Sondas del acta:
fuzz de la reducción 0/20.000; monotonía de la cota acoplada
0/4.000; banda [1.2, 1.4] re-ejecutada exacta; 40/40
cajas-punto legales.

## 5. Estatus

**EL CANAL OCUPANTE ≥ r_m QUEDA CERRADO EN EL CONTENEDOR DE Y
(v y torre d = 1) EN AMBOS PERFILES** (espcanal ligera v+z +
este script pesada v+z): tarifa derivada (dos paredes del nodo,
teoremas) + vacuidad del gemelo + pinza de la cola + bandas
certificadas + desbloqueo sobre el techo. Declarado: la banda
[2/φ, techo) en TORRES d ≥ 2 (ligera y pesada), x-en-u
(exclusión estructural de lem:DBo), k ≥ 2 anillos extra (pinza
de colas), ω ≤ 1.6 (tope heredado). Técnicas exportables nuevas:
la reducción de dimensión por pago-por-masa de la partición
entera (β sola, cap = min(β, φ/2, ΣA)) y la poda β > 1/2.
