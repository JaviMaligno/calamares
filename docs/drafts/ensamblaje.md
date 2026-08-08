# El teorema de ensamblaje: todo intercambio bloqueado cae en un caso cerrado

Estado: DRAFT (2026-08-08), PRE-ADVERSARIO. Script de contabilidad:
`code/ensamblaje.py`. Es la segunda de las dos piezas que faltaban
para τ = φ como teorema (módulo computacional); la primera es el lema
de dualidad/zigzag (`zigzag.md`).

## 1. El objeto

Por la localización del Teorema de obliviousness, toda diferencia
F ≠ P se reduce a un PASO DE INTERCAMBIO: m es el mayor anillo que F y
P colocan en contenedores distintos u = c_F(m), v = c_P(m); los
anillos > m son COMPARTIDOS (idénticos en F y P, por maximalidad de
m); el conjunto S de anillos < m que P mantiene en u debe reinsertarse
con los recursos liberados: D_m (disco vacante), H_m (agujero de m,
capacidad 1−ω, viaja con m), anidamiento en S, y la geometría de v.
Normalizamos r_m = 1, ω = w/r_m.

Cada contenedor es la sartén o el agujero de un anillo. Como u ≠ v,
el árbol de casos es:

    (a) u = SARTÉN (⟹ v = agujero del portador y):
        el intercambio de sartén (app:pan-app).
    (b) u = agujero de α, v = SARTÉN, α a nivel superior:
        el intercambio anidado canónico (sec:width/sec:generic).
    (c) el PUERTO DE CONTENEDOR (resto):
        (c1) u = agujero de α, v = agujero de Y (ambos agujeros);
        (c2) u = agujero de α con α anidada (dentro del agujero de
             otro anillo z o de un ocupante), v = sartén o agujero.

## 2. Hechos de ensamblaje (válidos en todos los casos)

**E1 (|S| ≤ 1 nunca bloquea).** Todo σ ∈ S cumple σ < m = 1; un solo
anillo cabe en D_m (fila de uno, capacidad 1). Luego el bloqueo exige
|S| ≥ 2. [Con |S| = 0 el paso es mover m, siempre legal: D_m queda
libre y el sitio de m en u lo garantiza F.]

**E2 (esqueleto compartido).** Los anillos > m están en los mismos
contenedores en F y P; las paredes de cada plantilla solo usan los
miembros del contenedor del re-empaquetado y los recursos listados,
nunca la posición de anillos > m fuera de él.

**E3 (j ≥ 1 en el caso (a)).** El portador y tiene y ≥ 1+ω > 1: o es
ocupante de la sartén o vive dentro de uno; en ambos casos la sartén
tiene al menos un ocupante > 1.

**E4 (α ≥ máx(1+ω, S₀+ω) en los casos (b)-(c)).** El agujero de α
contiene a m (α ≥ 1+ω) y, en la rama con S dentro del agujero, a las
piezas correspondientes (tarifas del Lema DR).

## 3. El caso (a): CERRADO

Teoremas DP (perfiles par, total: j = 1 y j = 2 con toda anchura
ω > 0 incluido pivote sólido, evacuación, j ≥ 3), DP-p y DPr (perfiles
mayores salvo una celda), más la campaña corona-contra-colas:
D1 (la celda {p ≥ 4, σ₁+M ≤ 1, j ≥ 3}), D2 (pequeños extra, por
ADJUNCIÓN al perfil — resultado completo sin geometría), D3 (pivote
sólido ω ≥ 1, j ≥ 3, sin usar anchura). Etiquetas: DP/DPp/DPr son
teoremas plenos; D1/D3 son cierres computacionales con certificados
respaldados por el lema de dualidad/zigzag (`zigzag.md`), con el
asterisco de la ley de escala (j, p).

## 4. El caso (b): CERRADO al nivel áureo

Las plantillas anidadas del paper (par y trío canónicos para todo ω;
j ocupantes extra vía Ψ_j y el argumento de hoja; golden line) dan
ρ > T > φ en sus dominios, y los tres huecos declarados AL NIVEL
ÁUREO (Status, op:assembly(b)) los cierra la campaña anidada:
D4 (la puntita j = 2, ω ∈ [φ/2, 1)), D5 (k ≥ 4 fuera de la rama de
reducción, con la tricotomía y las coronas), D6 (gap lemma:
pequeños contra las paredes geométricas, por adjunción + barridos
directos). Etiquetas: las plantillas del paper son teoremas; D4-D6
son cierres computacionales adversariados (acta 2026-08-07) con la
misma maquinaria de dualidad. Residuo declarado: el lema-extensión de
la herencia (N) (C4 del acta anidada) — la rama (N) transporta el
programa del par con el polvo dentro de σ₁; su versión con carga
explícita queda enunciada y verificada en dominio, sin prueba general.

## 4bis. El lema-extensión de (N) (cierra C4 del acta anidada)

**Lema (extensión de la herencia (N)).** En la plantilla anidada con
(N): W + X_{σ₁} ≤ σ₁ − ω, las herencias geométricas del programa del
par valen verbatim: en particular la línea áurea de j = 1
(mín(φ² − (φ/2)ω, 2) > φ) y la curva canónica de j = 0, k ≥ 4,
ω > 1 − φ/2 dan ρ > φ con W y X_{σ₁} arbitrarios.

*Prueba.* Dos mecanismos.

(i) *Monolito.* Bajo (N), el conjunto W ∪ X_{σ₁} cabe como fila en el
agujero de σ₁ (capacidad σ₁ − ω; fila constructiva del Lema de fila,
suma ≤ capacidad). σ₁ con ese contenido es UNA pieza de radio σ₁: su
huella circular no cambia. Por tanto toda colocación-testigo del
programa del par para {σ₁, σ₂} se extiende a una colocación de S
(añadir W al agujero de σ₁, legal por lo anterior), y el bloqueo de S
implica el fallo de TODAS las colocaciones del par. Las paredes del
programa del par — que se derivan exactamente de esos fallos y solo
usan los radios σ₁, σ₂ y los recursos (D_m, H_m, bolsillos, disco
intrínseco) — quedan intactas a fortiori.

(ii) *Absorción por colas.* Los términos engordados por X_{σ₁} (la
B3′ del template) son masas de piezas < σ₁ del multiconjunto de
entrada: están contenidas en la cola de σ₁ (y en la de m si son
< 1), que las cotas de ρ ya contabilizan; ninguna pared usa X_{σ₁}
con signo favorable al adversario. Las conclusiones numéricas de las
dos celdas no involucran W: la línea áurea satisface
φ² − (φ/2)ω ≥ φ² − φ/2 = 1 + φ/2 > φ para todo ω ≤ 1 (identidad
exacta φ² = φ + 1), y la curva canónica está probada en el paper para
el par sin referencia a W. ∎

Con esto, las dos celdas de (N) pasan de «probadas módulo
lema-extensión» a probadas; el residuo computacional del caso (b)
queda en D4/D5/D6 con sus etiquetas.

**Lema (puerto).** Toda pared de los casos (a) y (b) usa del
contenedor del re-empaquetado únicamente que es un DISCO de capacidad
conocida con los miembros nombrados dentro. Por tanto, sustituir la
sartén (radio R) por el agujero de Y (disco de capacidad Y−ω) o el
nivel de α por el agujero de z deja cada pared VÁLIDA con la
capacidad correspondiente, y los suelos ρ > φ se heredan verbatim.

Inspección pared a pared (la lista completa, con su ingrediente):
- (D) fila en D_m: no usa el contenedor. PORTABLE.
- Tarifas de agujero (Lema DR / (Ry)): hablan del agujero del
  portador, no del contenedor. PORTABLE.
- Necesidades de par (o_i + o_ℓ ≤ cap): vienen de que los miembros
  están empaquetados EN el disco contenedor (F o P según el lado);
  en el puerto los miembros están en el agujero ⟹ misma forma con
  cap = Y−ω. PORTABLE.
- Rigidez y bolsillos (prop:S5, b, b₂, espejos): enunciados en el
  disco o₁+o₂ (o α+o), que vive dentro del contenedor por contención
  antítona (el fallo en el contenedor implica el fallo en el disco
  del par). PORTABLE.
- Coronas / zigzag / camino más largo (Lema U₄, criterio mural,
  corona-contra-colas): enunciados para un disco de capacidad c
  arbitraria. PORTABLE (es el mismo certificado con c = Y−ω).
- Colas y cascada (ρ ≤ φ): contabilidad combinatoria de tamaños, sin
  contenedor. PORTABLE.
- Evacuación / hoja / Ψ_j, Ψ_B: contabilidad de hojas y tarifas.
  PORTABLE.
- Contención monótona (fallo en R ⟹ fallo en subdisco): válida en
  cualquier disco. PORTABLE.

Único punto direccional: en (c) el re-empaquetado FALLA en el disco
pequeño directamente (ahí vive el bloqueo), así que las paredes se
derivan en el contenedor real y no hace falta transferir fallos entre
discos distintos; la contención solo se usa DENTRO del mismo caso,
como en (a) y (b).

**El mecanismo real: descenso a los discos intrínsecos.** Ninguna
pared geométrica usa el radio del contenedor como cantidad: todas se
derivan, por contención antítona (fallo en el contenedor ⟹ fallo en
todo subdisco), en el DISCO INTRÍNSECO de sus miembros (o₁+1, o₁+o₂,
α+o), que cabe en cualquier contenedor que los albergue (necesidades
de par exactas del criterio de dos círculos). Por eso los suelos son
uniformes en la capacidad y el puerto los hereda sin tocar una línea.
Bonus (no necesario): la cola del portador Y añade la cota gratuita
ρ ≥ (1+ΣS)/Y — las colas son del multiconjunto de entrada, no de la
colocación.

## 6. El teorema

**Teorema (ensamblaje).** Todo paso de intercambio bloqueado cae en
exactamente uno de los casos (a), (b), (c); en cada uno, las paredes
del caso correspondiente fuerzan ρ > φ. En consecuencia, ρ ≤ φ
implica que ningún paso de intercambio se bloquea y el greedy es
placement-oblivious: τ ≥ φ. Con τ ≤ φ < T (teorema del paper), τ = φ.

Etiquetas honestas: la parte (a)-par, (a)-evacuación, (a)-j≥3-DPr,
(b)-plantillas y (c)-puerto son teoremas; las celdas D1, D3, D4, D5,
D6 y la extensión (N) son cierres computacionales adversariados con
certificados por instancia respaldados por el lema de dualidad
(`zigzag.md`), sobre los rangos barridos, con la ley de escala (j, p,
k) como único paso numérico no convertido en prueba.

## 7. Qué verifica el script

`code/ensamblaje.py`: [A] el árbol de casos es una PARTICIÓN
(identidades de pertenencia; u ≠ v; y ≥ 1+ω ⟹ j ≥ 1; α ≥ 1+ω);
[B] contabilidad MC: instancias aleatorias de pasos de intercambio
(contenedores, portadores, perfiles, ocupantes) asignadas a casos:
0 sin caso, 0 en dos casos; [C] portabilidad: las paredes portables
evaluadas con cap = Y−ω reproducen las cotas del caso sartén en
familias aleatorias, y la ganancia del puerto es ≥ 0 (la cola de Y
solo sube ρ); [D] E1-E4 (|S| ≤ 1 nunca bloquea: barrido de
colocaciones; σ ≤ 1 cabe en D_m); [E] controles: la familia áurea del
paper vive en (a)(i) (j = 1) y la familia rígida del suelo T en (b),
con sus valores exactos.
