# El teorema de ensamblaje: todo intercambio bloqueado cae en un caso cerrado

Estado: ADVERSARIADO (2026-08-08, acta `acta_ensamblaje.md`:
CONFIRMADO CON CORRECCIONES). Script de contabilidad:
`code/ensamblaje.py`. Es la segunda de las dos piezas que faltaban
para τ = φ como teorema (módulo computacional); la primera es el lema
de dualidad/zigzag (`zigzag.md`). Correcciones mayores de la ronda:
la prueba del lema-extensión de (N) (§4bis, el monolito ingenuo era
falso; reparado vía absorción exacta) y el caso (c), que queda
partido en (c-i) α ∈ v (cerrado por porte de (b)) y (c-ii) α ∉ v
(celda abierta declarada: paredes portadas, programa pendiente).

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
        (c1) u = agujero de α, v = agujero de Y (ambos agujeros;
             α e Y a cualquier nivel);
        (c2) u = agujero de α con α anidada (su contenedor es el
             agujero de otro anillo z), v = SARTÉN.

[Corrección adversaria 2026-08-08: (c1)/(c2) redefinidos para que la
partición sea disjunta — antes (c2) decía «v = sartén o agujero» y
solapaba con (c1). La justificación de (a): u ≠ v y la sartén es
única, luego v es un agujero; su portador y cumple y ≥ 1+ω porque su
agujero admite a m = 1. Los contenedores son la sartén o agujeros de
anillos > m (el padre de m en cualquier colocación es mayor que m).
El corte de cierre REAL dentro de (c) no es (c1)/(c2) sino α ∈ v
frente a α ∉ v: véase §5.]

## 2. Hechos de ensamblaje (válidos en todos los casos)

**E1 (|S| ≤ 1 nunca bloquea).** Todo σ ∈ S cumple σ < m = 1; un solo
anillo cabe en D_m (fila de uno, capacidad 1; su carga viaja dentro).
Luego el bloqueo exige |S| ≥ 2. [Con |S| = 0 el paso es mover m,
siempre legal: D_m queda libre y m entra en u RE-COLOCANDO los
miembros directos de u según el certificado de F — los miembros > m
de u coinciden en F y P (E2) y F certificó que ese conjunto más m
empaqueta en u; las posiciones son existenciales y los subárboles
viajan rígidos, como en la prueba de thm:oblivious. No basta «el
sitio lo garantiza F» a posiciones fijas de P.]

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

*Prueba.* Dos mecanismos, con el reparto corregido tras la ronda
adversaria (2026-08-08): el monolito NO extiende las colocaciones que
usan el agujero de σ₁ como recurso, y esa familia debe tratarse por
absorción. El precedente exacto en el paper es thm:DPp(ii) (rama
anidada de la sartén) y prop:DT3j / thm:DT3-rama-1 (la carga viaja
dentro de σ₁ en cada colocación del par).

(i) *Monolito, solo para colocaciones que no usan el agujero de σ₁.*
Bajo (N), W ∪ X_{σ₁} cabe como fila en el agujero de σ₁ (capacidad
σ₁ − ω; Lema de fila, suma ≤ capacidad; el interior de σ₁ se
re-ordena libremente porque no es visible desde fuera). σ₁ con ese
contenido es UNA pieza de radio σ₁ VAYA DONDE VAYA. Las colocaciones
de los programas de las dos celdas son exactamente: fila en D_m (D),
σ₂ → H_m / fila en H_m (B1/BH, evacuación), σ₂ junto a m en u
(B2/B4), σ₂ al agujero de un nodo u hoja (Bo/Bo″), el par al
re-empaquetado de v (lem:DG, corona/F, Ry) y la legalidad del testigo
(W). NINGUNA de ellas coloca nada en el agujero de σ₁; todas se
extienden añadiendo la fila W ∪ X_{σ₁} dentro de σ₁, luego el bloqueo
de S fuerza su fallo y sus paredes valen a fortiori, verbatim.

*Contraejemplo que obliga a esta restricción* (hallazgo A4 del acta):
la colocación «σ₂ anidada en σ₁» (tercera colocación de prop:Cpair,
pared B3) NO se extiende: con ω = 0.1, σ₁ = 0.9, σ₂ = 0.7 ≤ σ₁−ω,
X = 0, W = 0.75 ≤ σ₁−ω se tiene σ₂+W+X = 1.45 > 0.8 = σ₁−ω. El
enunciado anterior («toda colocación-testigo se extiende») era falso.

(ii) *Absorción exacta de la única pared del agujero de σ₁.* En los
programas de las dos celdas, el agujero de σ₁ entra solo por B3′
(σ₂ + X_σ > σ₁ − ω, Lema DR en el agujero de σ₁; app:pocket-app), y
solo en la rama B de la línea áurea (thm:DGp, cadena (I)). Bajo (N)
la pared engordada es σ₂ + X_σ + W > σ₁ − ω, y la cadena (I) es
INVARIANTE bajo X_σ ↦ X_σ + W: (I) solo usa X_σ vía esa cota inferior
y vía la cola de o₁ (y α), que recoge también a W (masa del
multiconjunto < 1 < o₁) — comprobación simbólica en el bloque F del
script: la diferencia de la cadena es e₀+e₁+e₂+e₃+2e₄ ≥ 0 en las
holguras, con W dentro de e₂. La rama A no usa B3′ (X_σ, M ≥ 0). La
esquina exceptuada de la línea áurea (rama B, hijo-nodo, ω < 1/2) va
por el programa de thm:DBpp, que tampoco usa el agujero de σ₁ (dicoto-
mía de evacuación + dos colas; las masas solo engordan) y da
ρ > Ψ_B(ω) > Ψ_B(1/2) = 2 > φ exacto: el mín(φ²−(φ/2)ω, 2) completo
se transporta. Para la curva canónica (j = 0, k ≥ 4): sus paredes
(B1-corona, B2/dicotomía, B4, BH, W; cor:DB2 y thm:DT3 rama 1) no
tocan el agujero de σ₁, luego (i) las cubre todas. Las conclusiones
numéricas no involucran W: la línea áurea satisface
φ² − (φ/2)ω ≥ φ² − φ/2 = 1 + φ/2 > φ para todo ω ≤ 1 (identidad
exacta φ² = φ + 1), y la curva canónica da ≥ 13/7 > φ para todo ω
(thm:corner). ∎

Con esto, las dos celdas de (N) pasan de «probadas módulo
lema-extensión» a probadas; el residuo computacional del caso (b)
queda en D4/D5/D6 con sus etiquetas.

**Lema (puerto, nivel pared).** Toda pared de los casos (a) y (b)
usa del contenedor del re-empaquetado únicamente que es un DISCO de
capacidad conocida con los miembros nombrados dentro. Por tanto,
sustituir la sartén (radio R) por el agujero de Y (disco de capacidad
Y−ω) o el nivel de α por el agujero de z deja cada pared VÁLIDA con
la capacidad correspondiente. [Corrección adversaria: esto NO
implica por sí solo que los SUELOS ρ > φ se hereden — un suelo es un
programa completo sobre configuraciones, y los programas tienen
hipótesis estructurales de cohabitación; véase la dicotomía
(c-i)/(c-ii) más abajo.]

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
de par exactas del criterio de dos círculos). Bonus (no necesario):
la cola del portador Y añade la cota gratuita ρ ≥ (1+ΣS)/Y — las
colas son del multiconjunto de entrada, no de la colocación.

**Corrección adversaria (2026-08-08): portabilidad de paredes ≠
cobertura de programa.** El descenso intrínseco presupone que los
miembros del disco intrínseco COHABITAN en un contenedor: o₁+1 exige
{o₁, m} juntos (en (a), m ∈ u = sartén con sus ocupantes), α+o exige
α ∈ v. Los PROGRAMAS de (a) y (b) — los árboles de casos completos
que producen el suelo φ — tienen por tanto hipótesis estructurales
que el puerto no siempre satisface: en (a), m llega al contenedor del
re-empaquetado grande (u) junto a los ocupantes, y E3 da j ≥ 1; en
(b), α es ocupante de v. El corte real dentro de (c):

- **(c-i) α ∈ v** (α miembro directo de v = agujero de Y): v es un
  disco de capacidad Y−ω con ocupantes {α} ∪ O_v ∪ {m} según P — la
  plantilla (b) VERBATIM con R ↦ Y−ω. Las necesidades de par
  (α+o ≤ cap, dos círculos exacto), lem:DG por contención al disco
  α+o₁, el criterio angular/coronas (paramétrico en la capacidad,
  lema del certificado de coronacolas §3, confinamiento
  |c| ≥ 2o₁+r−cap incluido) y las colas (libres de posición) portan
  pared a pared Y programa a programa: (c-i) hereda los suelos de (b)
  con sus mismas etiquetas (plantillas = teorema; D4–D6 = cierre
  computacional).
- **(c-ii) α ∉ v** (incluye TODO (c2), donde α está anidada y
  v = sartén, y los (c1) con α fuera del agujero de Y): las paredes
  portan (W, B2/B4 en u; D y (Ry) en v; Bo en todo nodo de la
  configuración; colas), pero NINGÚN programa probado las ensambla:
  thm:DP exige m ∈ sartén, thm:DGp/lem:DG exigen α ∈ v, y Ψ_j con
  j′ = ocupantes reales de la sartén no cubre ω ≥ 1/2 con j′ = 1.
  [ACTUALIZACIÓN 2026-08-08: PROGRAMADA Y CERRADA en la campaña
  `puertocii.md` / `code/puertocii.py` (5/5): pinzas exactas I1–I4
  (ligereza automática, ω\* = 3/(2φ), esquina (3/(2φ), 1/2)) +
  coronas con dualidad tangente; el residuo delimitado R2 se vació
  con el recurso que faltaba en la lista: el REPACK DE LA SARTÉN
  (legal: factibilidad por contenedor + acuerdo solo de contenedores
  en ≥ m; precedente: el pan repack de thm:DP), vía la pinza exacta
  α > 2, T > √5−1 ⟹ b₂(α,T) > b₂(2,√5−1) = 1 > σ₂ — la misma
  esquina áurea del muro espejo. Pendiente su ronda hostil.]

## 6. El teorema

**Teorema (ensamblaje, CONDICIONAL tras la ronda adversaria).** Todo
paso de intercambio bloqueado cae en exactamente uno de los casos
(a), (b), (c) — la partición es un teorema (definicional: contenedor
= sartén única o agujero de un anillo > m). En (a), (b) y (c-i) los
programas correspondientes fuerzan ρ > φ (con las etiquetas de
abajo). En (c-ii) (α ∉ v) las paredes están portadas pero el programa
que las ensambla queda POR ESCRIBIR: el ensamblaje da τ = φ MÓDULO
esa celda además de los residuos computacionales. Si (c-ii) se
cierra, ρ ≤ φ implica que ningún paso se bloquea y el greedy es
placement-oblivious: τ ≥ φ; con τ ≤ φ < T (teorema del paper), τ = φ.

Etiquetas honestas: la partición (a)/(b)/(c), E1–E4, el lema-puerto a
nivel pared, el lema-extensión de (N) (con la prueba corregida de
§4bis) y la herencia (c-i) ⟵ (b) son teoremas; (a)-par,
(a)-evacuación, (a)-j≥3-DPr y (b)-plantillas son teoremas del paper;
las celdas D1, D3, D4, D5, D6 son cierres computacionales
adversariados con certificados por instancia respaldados por el lema
de dualidad (`zigzag.md`), sobre los rangos barridos, con la ley de
escala (j, p, k) como paso numérico no convertido en prueba; y
(c-ii) es una CELDA ABIERTA declarada (paredes portadas, programa
pendiente, sondeos de cierre favorables).

## 7. Qué verifica el script

`code/ensamblaje.py` (alcance re-etiquetado tras la ronda adversaria;
los checks marcados [ENUNCIADO] en el script registran afirmaciones
cuya prueba vive en este draft/el paper, no verificaciones):
[A] identidades exactas (sympy) + E3/E4 como enunciados;
[B] la partición sobre los flags derivados de la definición
(re-etiquetado: es DEFINICIONAL, no un test MC con contenido — la
exhaustividad viene de «contenedor = sartén única o agujero», no del
muestreo) + el conteo del corte (c-i)/(c-ii);
[C] construcción geométrica de la fila de dos círculos (criterio
exacto) y el bonus de la cola de Y [ENUNCIADO en su mitad];
[D] E1 (|S| = 1 con criterio exacto de un círculo; |S| = 0 como
enunciado con la re-colocación de F);
[E] controles (identidades áurea/Tribonacci, (D) como puerta);
[F] el lema-extensión REPARADO: identidad de la línea áurea,
contraejemplo que refuta el monolito ingenuo (la colocación B3 no se
extiende), invariancia simbólica de la cadena (I) de thm:DGp bajo
X_σ ↦ X_σ + W (holguras e₀+e₁+e₂+e₃+2e₄ ≥ 0), Ψ_B(1/2) = 2 exacto
(transporte de la esquina del mín(·,2)) y el monolito MC restringido
a colocaciones que no usan el agujero de σ₁.
