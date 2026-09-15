# Calamares — certificados exactos y exclusión cartesiana en Lean 4

Formalización en Lean 4 (v4.32.2, **solo core, sin mathlib**) de la capa de
identidades algebraicas exactas sobre la que descansan las pruebas del paper
de empaquetamiento de anillos (`paper/main.tex`), ampliada el 2026-09-14
con la exclusión cartesiana universal de un trío en cuadrado.
Cero `sorry`, cero axiomas nuevos: los certificados numéricos usan
`decide +kernel`; las desigualdades universales de `Square.lean` usan
pruebas de orden y `grind`, que genera términos comprobados por el kernel.
Se ha verificado con `#print axioms` que solo
dependen de `propext`, `Classical.choice`, `Quot.sound` — los tres axiomas
estándar de core — y ninguno de `Lean.ofReduceBool` ni `sorryAx`.

## Qué formaliza

**Nuevo bloque del cuadrado:** `Calamares/Square.lean` demuestra que los
discos de radios `1.845,0.844,0.841` no caben en un cuadrado de lado
`4.8568`. `d_no_packing` cuantifica sobre todas las coordenadas en un
anillo conmutativo linealmente ordenado y prueba las reflexiones y el
confinamiento. No se limita a coordenadas racionales ni a una malla.
También incluye los certificados racionales del testigo de cuatro aros,
las paredes del voraz, `rho=337/200<X` y un control factible D'. La prueba
escrita y el alcance exacto están en
[`../docs/drafts/cuadrado_certificado.md`](../docs/drafts/cuadrado_certificado.md).

La continuación del mismo día generaliza el Lema Q a parámetros
arbitrarios (`Square.no_packing`, `excluded_of_conditions`).
`Calamares/SquareTwins.lean` lo aplica a las gemelas cuadradas y al
contraejemplo mejorado con `rho=1.68449`; también formaliza el testigo
cartesiano del trío factible de las gemelas. Son **21 teoremas** entre
ambos módulos. Véase
[`../docs/drafts/cuadrado_gemelas.md`](../docs/drafts/cuadrado_gemelas.md).

`Calamares/SquareLimit.lean` añade tres identidades para la cota algebraica
`tau_cuadrado ≤ Y≈1.684487745872346`: la pared equilibrada, su norma
polinomial y la implicación de raíz. El bloque cuadrado suma 24 teoremas,
81 junto a los 57 anteriores. `Calamares/FourRing.lean` añade dos
factorizaciones y `golden_balance`: en un anillo conmutativo linealmente
ordenado, las dos presiones del bolsillo implican `rho>phi`.
La v2 suma **84 teoremas**. La reducción del bosque para `tau_4=phi`
está en `paper/main.tex`, `thm:fourfloor`; no está formalizada.
La familia aproximante de Y y el argumento de
continuidad se prueban por escrito en
[`../docs/drafts/cuadrado_limite.md`](../docs/drafts/cuadrado_limite.md);
no están formalizados en Lean.

**Extras del 2026-09-15:** `Calamares/VariableWidth.lean` añade siete
teoremas: masa positiva, suma de cuadrados, presión de área, comparación
con prefijo común, escalado de la cola y las dos identidades extremales.
`Calamares/FiveRing.lean` añade once: tres tangencias cartesianas del
bolsillo, separación de los dos bolsillos, positividad de radios y
denominador, y seis certificados de las presiones áureas. El total de
la biblioteca pasa entonces a **102 teoremas**. Los 18 nuevos compilan y solo usan
los axiomas estándar arriba indicados.

Las pruebas de bosques para hasta cinco aros y de captura de cola para
el área permanecen escritas en
[`cinco_aros.md`](../docs/drafts/cinco_aros.md) y
[`grosor_variable.md`](../docs/drafts/grosor_variable.md).
Fable acepta los resultados con precisiones menores incorporadas en F5.
Lean no formaliza
el teorema completo `tau_(≤5,d)=phi` ni el algoritmo de selección;
tampoco identifica un tipo concreto de números reales. Las implicaciones
de orden son genéricas sobre anillos conmutativos linealmente ordenados;
los radios divididos por denominadores positivos se interpretan en la
prueba escrita.

`Calamares/PocketSplit.lean` añade después tres teoremas: presión de la
cola completa, invariante de una partición equilibrada y cota final de
las dos sumas. El total pasa entonces a **105 teoremas**, con los mismos
axiomas estándar. La aplicación geométrica se desarrolla en
[`particion_bolsillos.md`](../docs/drafts/particion_bolsillos.md): alinea
el segundo y tercer aro para colas finitas y reduce seis al cuarto aro
con tres mayores en raíz. Fable revisó después la presión, partición
y criterios C1/C2 como dependencias del cierre global de tres mayores.
La clasificación de bosques no está formalizada.

`Calamares/UniformExchange.lean` añade tres teoremas sobre un número
arbitrario de sumandos representados por su masa: la presión
`(k+1)U≤k²m`, su consecuencia `U≤m` en el corte áureo, y un control
racional que falla en el modelo aditivo pese a satisfacer las cotas.
Este bloque eleva el total a **108 teoremas**, todos sin admisiones. La reducción
a un intercambio de dos aros consecutivos y el corolario para bosques
binarios de tamaño arbitrario están escritos en
[`intercambio_uniforme.md`](../docs/drafts/intercambio_uniforme.md).
El intercambio con grados arbitrarios se cierra posteriormente por T3.

`Calamares/Reservoir.lean` añade siete certificados para la
[`reducción estructural uniforme`](../docs/drafts/nucleo_uniforme.md):
cota phi<5/3, suma de cuadrados de una lista acotada, margen positivo
para dos plazas cuando el segundo ocupante tiene radio al menos 9m,
su expansión como desigualdad de áreas, dos plazas superiores de radio
b/2 junto a un par diametral a,b, exclusión de seis radios en
la franja (m,9m) y de seis aros consecutivos en una cadena sin holgura.
Este bloque eleva el total a **115 teoremas**. El argumento escrito limita a dos
ramificaciones, seis hojas y 40 aros mayores el intercambio residual;
la cola puede tener longitud arbitraria. La unión de regiones prohibidas
para centros y el recuento del árbol no están formalizados. Esta reducción
histórica no se usa en el cierre global posterior y no tiene dictamen externo.

`Calamares/ThreeCore.lean` añade siete certificados para la
[prueba de tres mayores](../docs/drafts/tres_mayores.md):
identidad y signo del margen angular de dos discos en un arbelos,
identidad y signo de la suma de los huecos opuestos, signo auxiliar
de altura, cotas de las dos envolventes de la cola
y paso de curvaturas a radios. El total actual es **122 teoremas**.
Fable acepta la prueba escrita completa de la garantía universal rho≤phi
con sus dependencias. La disyunción de los dos incírculos se demuestra
por inversión, no por el certificado auxiliar de altura. No se ha
formalizado en Lean el teorema de empaquetamiento completo ni tau=phi.

La **capa anterior de certificados exactos**: las identidades de aritmética exacta en
ℚ y ℚ[√5] que los scripts de `code/` verifican con sympy y sobre las que se
apoyan los teoremas del paper.

- La aritmética áurea del contraejemplo (`thm:golden`): φ² = φ+1, la rigidez
  b2(φ,1) = φ/2, la cola áurea, el punto fijo y su factorización en ℤ[A], el
  certificado del testigo con s* = 4(√5−2), el margen ε₀ y la ventana de ω.
- Los certificados de los medios metálicos de la Batalla 2 / Teorema P
  (`thm:DP`): 2b(φ) = φ, g(φ) = φ, el certificado polinomial de que g es
  decreciente, y las evaluaciones Ψ(1/2) = φ, Ψ_B(1) = φ, Ψ₂(φ/2) = φ,
  Ψ₃(1) = √3 > φ (con el patrón de eliminación de raíces cuadradas:
  se exhibe x con x² = radicando y x > 0).
- El suelo Tribonacci (`thm:rigidfloor`): P(φ) = −1 < 0, el encajonamiento
  1.8392 < T < 1.8393 y el certificado de monotonía estricta de P en x ≥ 1
  (P(1+e+d) − P(1+e) = d·Q(e,d) con Q de coeficientes ≥ 0 y coeficiente de
  d con término constante 2 > 0).
- La esquina 13/7 (`thm:corner`): γ_{2/7} = 2 y 1 + b(2) = 13/7.
- Los certificados de perfiles mayores (`thm:DPp`): la legalidad
  universal de los espejos (φ−1 < 2/3 = b(1)) y las cadenas pesadas.
- El cierre de la región pesada (`thm:DPr`): la frontera de la
  pinza-con-Σ con margen exacto 23−14φ y la esquina π de j = 2
  (sin²(θ/2) = 1/2 ∓ √5/10, suma 1, par diametral exacto).
- La **pinza** que cierra j = 3 del intercambio a sartén (`thm:DP` (iv)):
  la constante exacta s* = (6φ−1)/(2φ+1) = 11−4√5 = 15−8φ, que s < 2 la
  cumple, y la contradicción en el extremo (φ³ = 4.236 < φ+3 = 4.618, con
  margen exactamente 2−φ).
- La cobertura T/2 < s* (vía 18393/20000 < 4√5 − 8).
- El umbral aditivo: la familia (1/4+2δ/3, 1/4+δ/3)/(1/2) = 1+2δ como
  identidad de polinomios en δ.

## Qué NO formaliza

La **geometría general de empaquetamiento**: rigidez de coronas, criterios angulares
θ(a,b,R), árboles de colocación del voraz, evacuaciones y bolsillos espejo.
Esa capa está verificada por los scripts de `code/` (bloques B–E de
`aureo.py` y `batalla2.py`, `corona.py`, `rigido.py`, …); aquí solo se
formaliza el esqueleto algebraico exacto que esos argumentos consumen.
Las excepciones son el criterio cartesiano paramétrico del cuadrado,
sus exclusiones, el testigo de las gemelas y las identidades cartesianas
de los dos bolsillos de `FiveRing.lean`, descritos arriba.
No se ha definido en Lean un tipo de disco euclidiano ni el bosque
del algoritmo: el puente entre desigualdades cartesianas, círculos reales
y ejecución de best fit está escrito en la nota del cuadrado.

## Estructura

- `Calamares/Basic.lean` — `Q5` = ℚ[x]/(x²−5) como pares `(a b : Rat)` con
  aritmética completa; el orden del encaje real con √5 > 0 (`Q5.posb`,
  decidible); polinomios como listas de coeficientes ascendentes: `Poly`
  (ℚ[X]), `PolyZ` (ℤ[X]) y `Poly2` ((ℚ[e])[d]).
- `Calamares/Identities.lean` — 57 teoremas (la tabla de abajo cubre 1–32; los lotes posteriores — `golden_reduction_threshold`, `diametral_pocket_golden`, `forbidden_triple_cubic` y las identidades de la campaña corona-contra-colas hasta `additive_family` — están documentados en el propio fichero, con sus controles negativos y `#print axioms` limpios).
- `Calamares.lean` — raíz de la librería.
- `Calamares/Square.lean` — 14 teoremas: dos lemas de desigualdades,
  exclusión normalizada y con reflexiones de D, versión paramétrica de
  ambas exclusiones y su predicado cartesiano, certificados de D/X y
  testigo factible D'.
- `Calamares/SquareTwins.lean` — 7 teoremas: dos exclusiones para las
  gemelas, su testigo factible, exclusión de la instancia mejorada y
  tres certificados de paredes y colas.
- `Calamares/SquareLimit.lean` — 3 identidades sobre anillos conmutativos
  para la pared equilibrada y el polinomio de Y. Usa importaciones mínimas
  de core; `Square.lean` tampoco necesita importar toda la biblioteca Std.
- `Calamares/FourRing.lean` — dos identidades y una implicación ordenada
  para el suelo áureo del caso de cuatro aros. No presupone el resultado
  deseado: recibe la ecuación áurea, la definición multiplicada del
  bolsillo y las dos desigualdades estrictas derivadas en la prueba escrita.
- `Calamares/VariableWidth.lean` — siete teoremas algebraicos para la
  garantía exacta de área con agujeros independientes.
- `Calamares/FiveRing.lean` — once teoremas para los dos bolsillos y las
  presiones con uno o dos aros mayores; importa `FourRing.lean`.
- `Calamares/PocketSplit.lean` — tres teoremas para partición de colas
  finitas; importa `FourRing.lean` y `VariableWidth.lean`.
- `Calamares/UniformExchange.lean` — presión de dos colas consecutivas,
  corte áureo y control del modelo aditivo. El control no es un
  contraejemplo euclidiano.
- `Calamares/Reservoir.lean` — siete certificados para el criterio de
  plazas libres y las cotas de ramificación y cadenas con grosor común.
- `Calamares/ThreeCore.lean` — siete certificados algebraicos de la
  prueba uniforme basada en los tres discos mayores, aceptada por Fable.

Nota técnica: `decide` a secas se atasca con `Rat` (el elaborador no reduce
`Nat.gcd`, definido por recursión bien fundada); `decide +kernel` sí
funciona porque el kernel acelera `Nat.gcd` sobre literales. No hace falta
`native_decide` en ningún teorema.

## Tabla teorema Lean ↔ resultado del paper ↔ script

| # | Teorema Lean | Resultado del paper | Script |
|---|---|---|---|
| 1 | `phi_sq`, `phi_pos` | `thm:golden` | `aureo.py` [A] |
| 2 | `b2_phi_one` | `thm:golden` (rigidez S5) | `aureo.py` [A] |
| 3 | `tail_golden` | `thm:golden` | `aureo.py` [A] |
| 4 | `fixed_point` | `thm:golden` / `thm:DP` | `aureo.py` [A] |
| 5 | `fixed_point_factor` | `thm:golden` / `thm:DP` | `aureo.py` [A] |
| 6 | `witness_cert` | `thm:golden` (testigo, s*) | `aureo.py` [A] |
| 7 | `eight_phi`, `phi_cubed` | `thm:golden` (cadena del testigo) | `aureo.py` [A] |
| 8 | `eps0_margin` | `thm:golden` (margen ε₀) | `aureo.py` [A] |
| 9 | `window` | `thm:golden` (ventana de ω) | `aureo.py` [A] |
| 10 | `two_b_phi`, `g_phi` | `thm:DP` (caso j = 1) | `batalla2.py` [A] |
| 11 | `g_decreasing_cert` | `thm:DP` (g decreciente) | `batalla2.py` [A] |
| 12 | `Psi_half` | `thm:DP` (Ψ(1/2) = φ) | `batalla2.py` [A] |
| 13 | `PsiB_one` | `thm:DP` (rama B, Ψ_B(1) = φ) | `batalla2.py` [A] |
| 14 | `Psi2_goldenhalf` | `thm:DP` (rama A, Ψ₂(φ/2) = φ) | `batalla2.py` [A] |
| 15 | `Psi3_gt_phi` | `thm:DP` (rama A, Ψ₃(1) = √3 > φ) | `batalla2.py` [A] |
| 16 | `P_phi` | `thm:rigidfloor` (φ < T) | `striple.py` |
| 17 | `T_bracket` | `thm:rigidfloor` (1.8392 < T < 1.8393) | `striple.py` / `cuadrado.py` |
| 18 | `P_mono_cert` | `thm:rigidfloor` (P creciente en x ≥ 1) | `striple.py` |
| 19 | `gamma_27` | `thm:corner` (carve-out, γ_{2/7} = 2) | `esquina.py` |
| 20 | `corner_137` | `thm:corner` (ínfimo 13/7) | `esquina.py` |
| 21 | `coverage` | `thm:golden` + `thm:rigidfloor` (T/2 < s*) | `aureo.py` [C] |
| 22 | `additive_family` | umbral aditivo | `umbral.py` / `frontera.py` |
| 23 | `tail_crossing` | `thm:DP` (iv) (3/φ+3 = 3φ) | `microcelda.py` [A] |
| 24 | `inv_two_sub_phi` | `thm:DP` (iv) (el factor de (C4)) | `microcelda.py` [A] |
| 25 | `pincer_constant` | `thm:DP` (iv) (s* = 11−4√5 = 15−8φ) | `microcelda.py` [A] |
| 26 | `pincer_applies` | `thm:DP` (iv) (s < 2 < s*) | `microcelda.py` [A] |
| 27 | `pincer_gap` | `thm:DP` (iv) (φ³ < φ+3, margen 2−φ) | `microcelda.py` [B] |
| 28 | `pincer_child` | `thm:DP` (iv) (la torre no acaba en v*) | `microcelda.py` [A] |
| 29 | `mirror_legal` | `thm:DPp` (v)-(vi) (φ−1 < 2/3 = b(1)) | `perfilp.py` [A] |
| 30 | `heavy_chains` | `thm:DPp` (iii),(vi) (cadenas pesadas) | `perfilp.py` [A]/[C] |
| 31 | `pincer_sigma` | `thm:DPr` (i) (frontera (φ−1)Σ+16−9φ, margen 23−14φ) | `rstar.py` [A]/[B] |
| 32 | `corner_pi` | `thm:DPr` (iv) (la esquina π: sin² = 1/2∓√5/10) | `rstar.py` [A2] |

## Compilar

```bash
cd lean
lake build   # exit 0, sin sorry, sin warnings
```

En PowerShell, si elan no encuentra su directorio aunque esté instalado:

```powershell
$env:ELAN_HOME = 'C:\Users\Usuario\.elan'
lake build
lake env lean Calamares/Square.lean  # imprime los axiomas del bloque nuevo
```
