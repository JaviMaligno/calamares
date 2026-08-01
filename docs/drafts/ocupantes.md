# El precio del ocupante: bloqueos con ocupantes extra en la plantilla libre

Borrador. Resuelve los **pasos 2 y 4 de la Batalla 1** (`ESTADO_SESION.md` §3)
en la plantilla de agujeros libres, y lo hace con una sorpresa: **no hace
falta geometría**. El mecanismo que el plan conjeturaba («γ pequeño se
autocastiga; cada ocupante extra paga su cola») es un teorema de cuatro
líneas una vez se observa la pared que el plan no listaba: **el agujero de
cada ocupante extra es un recurso de reinserción**, y bloquearlo obliga al
ocupante a quedarse a un grosor de m. La cola del mayor ocupante extra hace
el resto:

    bloqueo con j ocupantes extra  ⟹  ρ > (j+2)/(1+ω)      (ω ≤ j/2)

— en particular ρ > 3/(1+ω) ≥ 13/7 para ω ≤ 8/13, y > T para
ω < ω₄ := 3/T − 1 = 3T² − 3T − 4 = 0.631067…; con la cota fina de la
verificación adversaria (ρ > 4/(1+2ω) en la rama j = 1, ω ≥ 1/2), ρ > T
para todo ω < ω₅ := 2/T − 1/2 = 2T² − 2T − 5/2 = 0.587378… y ρ ≥ 13/7 para
ω ≤ 15/26. El adversario con ocupantes extra nunca baja de 2 (para
ω < 1/2), mientras que toda la curva canónica vive bajo 2: **la plantilla
canónica es estrictamente óptima para el adversario** (conjetura fina del
plan, demostrada en la plantilla). Sometido a verificación adversaria
independiente (acta en `VEREDICTOS.md`): ningún claim refutado; la cota
fina, la caracterización de exactitud del programa de paredes y la
evidencia de cierre del hueco de ω grande son del verificador.
Verificación: `code/ocupantes.py` (5/5). Numeración local: Lema V1,
Proposición V2, Corolarios V3–V4.

## 1. La plantilla

Paso de intercambio con contenedor `v` genérico (normalizado `r_m = 1`,
`ω = w/r_m`): `v` es la sartén, de radio `R`, con ocupantes
`{α} ∪ O ∪ {m}`, donde `O = {o₁ ≥ … ≥ o_j}`, `j ≥ 1`, y `o_i ≥ 1` (los
ocupantes mayores que `m` coinciden en `F` y en `P`); `u` es el agujero de
`α`, de capacidad `α − ω`, con `1 ≤ α − ω` (allí colocó `F` a `m`); el
testigo `P` colocó `S = {σ₁ ≥ σ₂}` en `u` (con `σ₁ ≤ 1`). **Plantilla
libre**: `m`, `σ₁` y los `o_i` no tienen hijos (sus agujeros están libres).
El intercambio manda `m` a `u` y debe reinsertar `S`.

Los recursos de reinserción disponibles (además del re-empaquetado completo
de la sartén) incluyen, y esto es lo que el plan del paso 2 no explotaba:

- **D_m**, el disco de radio 1 que `m` deja libre en `v` (`reinsercion.md`
  §2): cualquier σ ≤ 1 cabe ahí, y por tanto siempre hay sitio para **una**
  de las dos piezas.
- **H_m**, el agujero de `m` (capacidad `1 − ω`), que viaja con `m`.
- **`u` junto a `m`**: el par `{1, σ₂}` en el disco `α − ω` ⟺
  `1 + σ₂ ≤ α − ω` (criterio exacto del par).
- **Anidamiento** `σ₂ ⊂ σ₁` (capacidad `σ₁ − ω`).
- **Los agujeros de los ocupantes**: `σ₂ ⊂ o_k` si `σ₂ ≤ o_k − ω` (libres
  por plantilla). ← la pared nueva.

## 2. Las paredes (Lema V1)

**Lema V1.** Si el intercambio está bloqueado en la plantilla libre,
entonces

    (B2)  σ₂ > 1 − ω                 (si no: σ₂ → H_m, σ₁ → D_m)
    (B3)  σ₂ > σ₁ − ω                (si no: σ₂ ⊂ σ₁, σ₁ → D_m)
    (B4)  σ₂ > α − ω − 1             (si no: σ₂ junto a m en u, σ₁ → D_m)
    (Bo)  σ₂ > o_k − ω  ∀k           (si no: σ₂ ⊂ o_k, σ₁ → D_m)
    (D)   σ₁ + σ₂ > 1                (si no: el par entero en D_m)
    (W)   σ₁ + σ₂ ≤ α − ω            (el testigo colocó S en u)

y además falla el re-empaquetado de la sartén (`{α} ∪ O ∪ S` no empaqueta
en `R`). En particular, por (Bo) y `σ₂ ≤ 1`:

    o_k < σ₂ + ω ≤ 1 + ω    para todo k :

**todos los ocupantes extra quedan a un grosor de m.**

*Demostración.* Cada línea es la contrapositiva de una colocación explícita:
si la desigualdad de la derecha falla, la colocación indicada es legal (las
condiciones de par y de anidamiento son los criterios exactos; el compañero
σ₁ ≤ 1 cabe en D_m, que es un disco libre de radio 1, y los dos recursos de
cada línea son disjuntos), luego el intercambio no estaba bloqueado. (W) es
la legalidad de la colocación del testigo (par en disco `α − ω`, criterio
exacto). ∎

Compárese con el programa canónico (`grosor_positivo.md` §1): (B2)–(B4) y
(W) son las mismas paredes; (Bo) es la nueva, una por ocupante — y no
requiere el criterio de coronas ni ningún oráculo.

## 3. El precio del ocupante (Proposición V2)

**Proposición V2.** Bloqueo en la plantilla libre con `j ≥ 1` ocupantes
extra ⟹

    ρ  >  2 + (j − 2ω)/o₁  ≥  (j + 2)/(1 + ω)      si ω ≤ j/2 ,

y para `j = 1`, `ω ≥ 1/2`:  `ρ > 4/(1+2ω) = (3−2ω) + (1−2ω)²/(1+2ω)`.
Las desigualdades son estrictas.

*Demostración.* La cola de `o₁` en la instancia completa contiene al menos a
`{o₂, …, o_j, m, σ₁, σ₂}` (todos menores o iguales que `o₁`; si hay empates,
en la ordenación decreciente la primera copia tiene a las demás en su cola,
y la cota vale igual). Por (Bo), `σ₁ ≥ σ₂ > o₁ − ω`, y cada `o_i ≥ 1`:

    ρ ≥ ( (j−1)·1 + 1 + σ₁ + σ₂ ) / o₁ > ( j + 2(o₁ − ω) ) / o₁ = 2 + (j − 2ω)/o₁ .

Si `ω ≤ j/2` el numerador `j − 2ω` es ≥ 0 y la expresión decrece en `o₁`;
por el Lema V1, `o₁ < 1 + ω`, luego `ρ > 2 + (j−2ω)/(1+ω) = (j+2)/(1+ω)`.
Para `j = 1 < 2ω`, úsese además la pared (D): `σ₁ + σ₂ > máx(1, 2(o₁−ω))`
y por tanto `ρ > (1 + máx(1, 2(o₁−ω)))/o₁ =: g(o₁)`. Para `o₁ ≤ 1/2 + ω`
es `g = 2/o₁ ≥ 2/(1/2+ω)`; para `o₁ ≥ 1/2 + ω`, `g = 2 + (1−2ω)/o₁` crece
en `o₁` (numerador negativo) desde el mismo valor: el ínfimo es
`g(1/2+ω) = 4/(1+2ω)`. ∎ [Rama fina aportada por la verificación
adversaria, que además comprobó que `4/(1+2ω)` es el ínfimo **exacto** del
programa de paredes en esa rama, alcanzado en `σ₁ = σ₂ → 1/2`,
`o₁ → 1/2 + ω`.]

**Observación (exactitud, del verificador).** Para `ω ≤ 1/2`, `(j+2)/(1+ω)`
es el ínfimo exacto del programa de paredes si `ω ≥ 1/(j+1)` (alcanzado en
la clausura `σ₁ = σ₂ → 1`, `o₁ → 1+ω`, `o₂, …, o_j → 1`, `α → 2+ω`); para
`ω < 1/(j+1)` la cola de `o₂` fuerza ínfimo `≥ j+1 > (j+2)/(1+ω)` — de ahí
los excesos crecientes del bloque [E]. De propina: (B4) + (W) dan
`σ₁ < 1` estricto en todo bloqueo.

Nótese qué NO se ha usado: ni el re-empaquetado de la sartén (la pared
geométrica), ni el criterio de coronas, ni `feas3`, ni siquiera (B2), (B4),
(D) o (W). La cota es puramente combinatoria: **cada ocupante extra paga
1/(1+ω) de cola** — el «árbol en número de ocupantes» que el plan
conjeturaba, sin inducción.

## 4. Corolarios

**Corolario V3 (cruces exactos, j = 1).** `ρ > 3/(1+ω)` para ω ≤ 1/2, con

    3/(1+ω) ≥ 13/7  ⟺  ω ≤ 8/13 = 0.6154…   (todo el tramo ω ≤ 1/2 cumple)
    3/(1+ω) > T     ⟺  ω < ω₄ := 3/T − 1 = 3T² − 3T − 4 = 0.6310675…

(la segunda igualdad es la identidad `T·(3T²−3T−4) = 3 − T` módulo
`T³ = T²+T+1`, verificada en simbólico). Combinando con la rama fina
`4/(1+2ω)` (que domina a `3−2ω` por la identidad
`4/(1+2ω) − (3−2ω) = (1−2ω)²/(1+2ω)`): el bloqueo con un ocupante extra
exige `ρ > T` para todo `ω < ω₅ := 2/T − 1/2 = 2T² − 2T − 5/2 =
0.5873784…` (identidad `T·(2T²−2T−5/2) = 2 − T/2`, exacta ya antes de
reducir módulo la cúbica), y `ρ ≥ 13/7` para todo `ω ≤ 15/26 = 0.5769…`.
Para `j ≥ 2`: `ρ > 4/(1+ω) > 2 > T` para **todo** `ω < 1`.

**Corolario V4 (conjetura fina del plan, en la plantilla).** Para ω < 1/2,
todo bloqueo con ocupantes extra tiene `ρ > 3/(1+ω) > 2`. En cambio la curva
canónica (sin ocupantes extra) vive estrictamente bajo 2: la rama del
testigo cumple `Φ(ω) < 2` para **todo** ω por la identidad exacta

    (2+ω)³ − (1+ω)·((2+ω)² + (2+ω) + 1) = 1  > 0   ⟹   T₍₁₊ω₎ < 2 + ω ,

la rama H_m es `2(1−ω) < 2` y la mixta no pasa de `1.9174`
(`esquina.md` §5); y el ínfimo global `13/7` es genuino (Teorema de la
esquina, sin módulo). Luego

    inf { ρ : bloqueo con ocupantes extra }  ≥  2  >  13/7  =  inf T_can :

**añadir ocupantes es estrictamente subóptimo para el adversario; el `v`
óptimo es la plantilla canónica.** (Comparación puntual: `3/(1+ω) > 2 >
máx(2(1−ω), Φ(ω))` para todo ω < 1/2, exacta sobre las cotas inferiores
canónicas demostradas.)

**Observación (encaje con la evidencia previa).** `universal.py` [E]
muestreó tres ocupantes `{α, γ, 1}` con caja `ω ≤ 0.25` y encontró mejor
bloqueo-proxy `ρ = 2.5617` con la cola de γ dominante en 321/321 casos. La
cota exige `ρ > 3/(1+ω) ≥ 2.4` en esa caja, y el mínimo del programa de
paredes está en `3/(1+ω) + O(exceso)` (bloque [C]: exceso `+0.003`–`+0.009`):
la evidencia queda explicada cuantitativamente.

## 5. Dónde queda la geometría

La pared geométrica (el re-empaquetado de `{α} ∪ O ∪ S` falla en `R`) quedó
sin usar. Sigue disponible, y el criterio de coronas (`corona.md`) la vuelve
algebraica: bloqueo ⟹ sin corona en `R̄ = α + o₁` (por `R ≥ α + o₁`, pares en
la sartén, y la monotonía de θ en R — `d/dR[f·f] < 0`, bloque [A]) ⟹ trío
top falla o zigzag falla (Lema U₄). El bloque [C] mide su efecto: en
ω ≥ 0.25 sube el mínimo del programa por encima de la cota combinatoria
(p. ej. `2.51` vs `2.40` en ω = 0.25; `2.40` vs `2.14` en ω = 0.40). Se
necesitará para el único tramo abierto (`j = 1`, ω grande, §6.2) y para el
paso 3.

## 6. Huecos declarados

1. **Agujeros ocupados (el corazón, paso 3 de la Batalla 1).** Si los
   agujeros de los `o_i` (o de `σ₁`, o de `m`) están ocupados, la pared (Bo)
   se debilita a «σ₂ no empaqueta junto a los ocupantes del agujero», que es
   recursiva. La dicotomía es clara — o σ₂ cabe (desbloqueado) o el ocupante
   del agujero es grande y paga su propia cola — pero el análisis recursivo
   no está hecho. Igualmente quedan fuera los ocupantes de `v` **menores**
   que `m`.
2. **`j = 1` con `ω ≥ ω₅ = 0.5874`.** La cota combinatoria (incluida la
   fina) cae por debajo de T. Plan: rama del testigo deformada con el
   Lema U₄ en `R̄` (la pared geométrica, §5), que en el canónico da
   `Φ(ω) > T` para todo ω. Evidencia del verificador de que se cierra así:
   en `ω ∈ [0.5, 0.63]`, las 2 000 instancias bloqueadas-por-paredes de
   menor ρ admiten **todas** una corona en `R̄ = α + o₁` — es decir, estaban
   realmente desbloqueadas y el ínfimo real con la pared geométrica queda
   muy por encima de la cota combinatoria.
3. La cota `(j+2)/(1+ω)` es un mínimo del programa de paredes casi exacto
   (excesos `+0.002`–`+0.11`, bloques [C] y [E]) pero **no** es el ínfimo
   exacto de ρ sobre los bloqueos reales: la pared geométrica lo sube (§5).
   No se necesita más para la conjetura (basta `> T`).
4. La comparación V4 usa las cotas inferiores canónicas demostradas y la
   esquina genuina; los valores exactos de `T_can` en las ramas H_m/mixta
   heredan el módulo habitual de exactitud del criterio angular
   (`esquina.md` §7), irrelevante aquí porque la separación es `> 2` contra
   `< 2`.

## Mapa de verificación

`code/ocupantes.py`, cinco bloques (5/5 OK):

- **[A]** simbólico: 8/13; `ω₄ = 3/T − 1 = 3T²−3T−4` módulo la cúbica; la
  identidad del 2 (`Φ < 2` para todo ω); la rama fina (`4/(1+2ω)` domina a
  `3−2ω`; cruce 15/26; `ω₅ = 2/T − 1/2 = 2T²−2T−5/2`); `3/(1+ω) > 2(1−ω)`
  siempre; monotonía de θ en R.
- **[B]** paredes: 18 129 casos con pared caída ⟹ colocación desbloqueante
  consistente (los criterios son exactos; el contenido está en la dicotomía
  de V1); 9 503 instancias con paredes en pie (muestreo condicionado que
  cubre también ω < 0.20, matiz del verificador) ⟹ `ρ >` cota V2 y `ρ >`
  cota fina (0 violaciones); `o₁ ≤ 1+ω` en 101/101.
- **[C]** ajuste: el mínimo del programa de paredes pega con `(j+2)/(1+ω)`
  (exceso `+0.003`–`+0.009` en ω ≤ 0.15) y la pared geométrica (no-corona en
  `R̄`, vía `corona.py`) lo sube en ω ≥ 0.25.
- **[D]** la cadena de V4 en malla (`3/(1+ω) > 2 > máx(2(1−ω), Φ(ω))` en
  (0, 0.30]) + cruces de V3 + margen `+0.45` sobre 13/7 en ω = 0.30.
- **[E]** escalado en j: mínimos `2.61, 3.52, 4.40, 5.33` para
  `j = 1..4` en ω = 0.15, contra `(j+2)/(1+ω) = 2.61, 3.48, 4.35, 5.22`.
