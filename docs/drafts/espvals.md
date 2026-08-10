# La vacuidad de la variedad del bolsillo diametral

Estado: v2 (2026-08-10), tras acta REFUTADO del v1 («el vals de las
bolas vacantes» — retirado). Script: `code/espvals.py` (5/5, v2).
El resultado final del hilo espxy→espvals: **la variedad peligrosa
de espxy era VACÍA bajo ρ ≤ φ**, por una pared que faltaba en los
generadores, y la celda ESP X_Y > 0 ligera se cierra por vacuidad +
sub-bolsillo universal.

## 1. La pared que faltaba: cola global de m

La cola de m = 1 incluye TODA pieza menor del multiconjunto
(definición del paper), en particular las X_Y:
**ΣS + X_m + ΣX_Y ≤ φ**. Los generadores de espxy/espvals-v1 solo
imponían ΣS(+X_m) ≤ φ — la trampa: las paredes del prover pueden
omitir masas opcionales (cotas inferiores válidas), pero la
LEGALIDAD del adversario exige la cola entera. Incompatibilidad
exacta: ligera ΣS > 1 (pared D) y x > x*(z) ≥ x*(2.8) = 0.914 ⟹
ΣS+x > 1.91 > φ. Medido: 300/300 puntos del generador de espxy
(misma semilla que su acta) violan cola(m), mínimo 1.962.
**ERRATA al acta de espxy**: sus «300 puntos legales» no lo eran.

## 2. La rigidez del suelo (derribo independiente)

En c′ = 1+z el par (z, m) es tangente RÍGIDO (|c_z−c_m| = z+1
forzado) y el hueco máximo restante en v es EXACTAMENTE el bolsillo
x* (máximo círculo inscrito en la luna; tangencias resueltas
numéricamente a 1e-8): **P mismo es infactible con x > x* en v** —
la obligación «corona con x» era fantasma: si P existe, x no estaba
mural en v.

## 3. La consecuencia positiva: sub-bolsillo universal

Toda pieza LEGAL de X_Y mide ≤ φ−ΣS < φ−1 = 0.618, y
x*(z) > 0.618 en todo el dominio (z ≥ 1+2ω > 1.29): **las X_Y
legales son siempre sub-bolsillo del hueco diametral**. El peligro
de la corona con X_Y > 0 en la ligera especular NO EXISTE; el
cierre de la celda = vacuidad + inserción sub-bolsillo de k piezas
pequeñas en los huecos del trío certificado (certificación
k-piezas PENDIENTE declarada; herramienta: el motor de r2bmulti —
piezas ≤ 0.618 con capacidad ≥ 2.8 son polvo cómodo).

## 4. El vals v1, retirado

F2 da por contenedor O el recurso posicional (bolas vacantes sobre
la realización de P) O el certificado fresco (fila/corona que la
sustituye) — no ambos. El vals mezclaba los dos modos (la bola de
x muere cuando el trío repacka v). Lección para testigos futuros:
elegir modo y cerrar su hueco (presupuesto de sombras para el
posicional; suficiencia k = 4 para el fresco).

## 5. Lo que sobrevive y las lecciones

Sobrevive de espxy: TODA el álgebra exacta (x* = p(z,1;1+z),
anchura 1/(z²+z+1), x*(φ) = φ/2, 3φ−1 — teoremas Lean 40-41) como
GEOMETRÍA de fronteras de coronas, no como variedad legal.
Lecciones: (1) la legalidad del adversario exige las colas
globales de todas las piezas; (2) en los suelos de tangencia,
comprobar que P mismo existe (rigidez); (3) el referee dirigido de
espxy no miró cola(m) porque no se le apuntó allí — evidencia
directa para la ronda final CIEGA comprometida con Javi.
