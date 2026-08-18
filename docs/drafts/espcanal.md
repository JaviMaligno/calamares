# El canal ocupante ≥ r_m: la tarifa derivada y la vacuidad del gemelo (espcanal)

Estado: v2 (2026-08-18), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — cero grietas de solidez en lo
certificado; el hallazgo del referee INVIRTIÓ el residuo: la
«lámina del gemelo» que el ciclo declaraba es VACÍA y el reclamo
final es MÁS fuerte que el del draft v1; reparaciones R1-R8
aplicadas). Script: `code/espcanal.py` (5/5).

## 1. El canal y por qué era model-conditional

El último épsilon MC de la celda especular: un anillo extra
x ≥ r_m = 1 que P mantiene en el contenedor de Y (v = agujero de
Y, o anidado en su torre interior z). Las actas (espxy corr. 5,
espkp corr. 1) lo declararon MODEL-CONDITIONAL «con tarifa sin
derivar»: el convenio de todos los cierres especulares es
X = polvo < r_m, y una pieza ≥ r_m no se puede evacuar (el acuerdo
de thm:oblivious es de contenedor en anillos ≥ r_m).

## 2. LA TARIFA DERIVADA: las dos paredes del nodo (TEOREMAS)

**Pared del nodo ligera (lem:DBo portado).** En el perfil ligero
(ΣS < 1+σ₂), el bloqueo implica x < σ₂ + ω + X_x. Derivación: si
x−ω ≥ σ₂+X_x, el opposite-disk (lem:DR) mete {σ₂} ∪ children(x)
en el agujero de x (si un child excede σ₂, el lema con ese child
de mayor); σ₂ solo cambia de contenedor (thm:oblivious); la fila
S∖{σ₂} < 1 (ligereza) va al disco vacante de m en v (lem:row).
Nada más se mueve. El acta verificó el desbloqueo movimiento a
movimiento.

**Pared pesada del nodo (partición hacia x).** En TODO perfil, el
bloqueo implica x < ω + ΣS − 1 + σ₁ + X_x. Derivación: greedy
descendente llenando A hasta ≤ 1 — al parar A > 1−σ₁, luego
B = S∖A pesa < ΣS−1+σ₁; lem:DR mete B ∪ children(x) en el agujero
de x (la mayor de B ≤ σ₂ ≤ x−ω) y A va en fila al disco vacante
de m. El acta verificó el greedy (σ₁ ∈ A, partición completa).

**El techo derivado** (cola global de m): x MINIMAL ⟹
children(x) = polvo ⟹ X_x ≤ φ−ΣS−X_m−μ_Y ⟹
x < σ₂+ω+(φ−1) ≤ 3.217. La «tarifa sin derivar» desaparece.

## 3. LA VACUIDAD DEL GEMELO (el hallazgo del acta, R1)

El ciclo delimitó primero una «lámina del gemelo»
V* = {x = r_m exacto} ∩ {α < 1+ω+σ₂+X_α} ∩ {z < α+X_z+σ₂+ω} — el
rincón multi-razor donde σ₂ queda sin casa para toda la lista de
testigos. **El referee la mató**: el convenio de primera copia
hace exactamente lo contrario de lo que el v1 le atribuía — «the
tail of a ring collects all later copies»: con x = r_m exacto hay
dos anillos de radio 1 y la cola de la PRIMERA copia recoge a la
otra MÁS S y el polvo:

    cola(primera)/r_m ≥ 1 + ΣS + X_m + X_α + X_z + μ > 2 > φ

por la pared D (ΣS > 1). Bloqueo + ρ ≤ φ excluyen el empate:
**V\* = ∅**. El mismo movimiento del hecho (2) de thm:DBpp y de
cor:DV34. Otra vacuidad de frontera de la campaña (espxy, F3, la
frontera ΣS = 1+σ₂…: la lista crece).

**Pinza de la cola de x (unificada, empate incluido)**: para todo
x ≥ r_m del canal, 1+ΣS+X_total ≤ φx; con ΣS > 1 la banda
[r_m, 2/φ = 1.236) es ρ-ilegal SIEMPRE.

## 4. LA COBERTURA SIN RESIDUO (A9)

El bloqueo ligero con x en v es IMPOSIBLE:

1. x ∈ [1, 1.236): ρ-ILEGAL (vacuidad del gemelo + pinza).
2. x ∈ [1.05, techo del nodo): CERTIFICADO por B&B — banda alta
   entera, **79.277 cajas, 0 sin resolver** (motor: par antipodal
   (z,x) con cotas acopladas + ciclo arc-LP con polvo plegado +
   creciente no-mural + pooling; suelo c′ = max(z+x, suelo del
   trío, cola(Y)−ω)).
3. x ≥ σ₂+ω+X_x: desbloqueo (pared del nodo).

Corolarios redundantes (sound): pool-u si α ≥ 1+ω+σ₂+X_α, pool-z
si z ≥ α+X_z+σ₂+ω. Solapes: 1.05 < 1.236 y x_top 3.227 > 3.217.
**EL CANAL LIGERO x-EN-v QUEDA CERRADO ENTERO.** x-en-z
(profundidad 1): certificada entera (1 caja — la cola con x
empuja z_lo y todo arco cabe).

## 5. Los testigos y lemas nuevos (exportables)

- **El testigo de identidad + pooling del polvo**: m → u (cabe
  por E4+D); S∖{σ₂} → fila en el disco vacante de m; z, x y el
  polvo QUIETOS — v empaqueta por construcción. σ₂ y el polvo
  estorbo se redistribuyen a los huecos (lem:DR/lem:row):
  room_z = z−ω−α, room_u = α−ω−1, room_D = 1−(ΣS−σ₂); cargas
  {σ₂, X_α, X_z} atómicas, asignación exhaustiva 3³. Las paredes
  B2u/Rz con las X fijas eran solo UNA asignación.
- **El lema del creciente** (trío {z, m, x} con gigante
  casi-mural): necesidad por lúnulas (ventana ψ(u) con h ↓ en u,
  h ↑ en t bajo gate — el peor c_z es el mural; monotonías
  sympy A8; segmentación en u + convexidad de d² a esquinas;
  bisección ⟹ `suelo_trio`, que clava el óptimo clásico
  1+2/√3 del trío igual a 1.1e-13) y suficiencia gemela
  (`_creciente_cabe`: cadena tangente a z, γ exactas, pares
  no-consecutivos explícitos con guard de wrap ≤ π — R4,
  ventanas con desplazamiento δ, polvo πμ/z). El testigo del
  rincón es NO-mural: el arc-LP mural no lo ve.
- **La pinza de la cola de x** con el empate (R1).

## 6. Verificación

[A] 8 gates sympy + 4 enunciados: convivencia, opposite-disk,
ligereza, techo, monotonías del creciente, greedy pesado (A7b),
cobertura A9. [B] banda alta 79.277 cajas / 19.977 certificadas /
0 sin resolver (recuentos re-ejecutados EXACTOS por el acta) +
rebanada [1.005, 1.05] vacua por pinza + x-en-z 1 caja. [C] 250
puntos legales de la banda alta: testigo 250/250 (mural /
pooling / creciente); control de la vacuidad del gemelo: 98/98
candidatos x = r_m violan la cola de la primera copia. [D] pared
del nodo como poda; certificador antipodal rechaza lo imposible;
negativos de los certificadores nuevos (R5): creciente-imposible
False, pooling sin huecos False / sin cargas True,
suelo_trio(1,1,1) ≤ 1+2/√3 y suelo_trio(2,1,1) ≥ 3; empalme
polvo/canal exacto por vacuidad de la juntura. [E] estatus. El
sanity muestrea X_α = X_z = 0 (X_m 30%) — más estrecho que el
dominio del B&B (nota R8).

## 7. Estatus

**La tarifa del canal está DERIVADA** (las dos paredes del nodo,
teoremas) y **el canal ligero x-en-v y x-en-z (profundidad 1)
CERRADO ENTERO, sin lámina residual** — el candidato a residuo
resultó vacuo. Declarado: la PESADA con x (pared A7 derivada; el
certificado con x explícito = fusión con espfinal, continuación
natural); la banda [1.236, techo) en la TORRE d ≥ 2 (la pinza y
la pared del nodo son posición-independientes y matan el resto a
toda profundidad — R3); x-en-u (exclusión estructural de
lem:DBo); k ≥ 2 anillos extra (pinza de colas); ω ≤ 1.6 (tope
heredado). Técnicas exportables: pared del nodo, pooling,
creciente (nec+suf), pinza de la cola de x con empate.
