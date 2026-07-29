# Perfiles de tres aros: caracterización exacta y fórmula cerrada de ρ*₃(ω)

Borrador. Resuelve el punto 3 de `reinsercion.md` §10: el análogo de la
Proposición 1 para `k = 3`. La numeración continúa la de `reinsercion.md`
(Proposiciones 1–3, Corolarios 1–2). Verificación: `code/tresk.py`.

**Resumen.** La caracterización de los perfiles de tres aros no reinsertables es
una disyunción de cuatro casos, tres de ellos puramente aditivos. El ínfimo
resultante **no** sigue la curva `c·(1−ω)` que sugería la búsqueda numérica, ni
involucra `2/√3 − 1`: es una hipérbola `2/(1+2ω)` que desemboca en una **meseta en
la razón áurea** y empalma después con la fórmula del par. La búsqueda de
`reinserta.py` se quedaba en un mínimo local (~0.02–0.03 por encima) en el régimen
de `ω` pequeño; con la fórmula exacta el cruce con Tribonacci baja de `ω_c ≈ 0.05`
a `ω_T = 1/T − 1/2 ≈ 0.043689`, en forma cerrada.

## 1. Marco

Como en `reinsercion.md` §3: normalizado `r_m = 1`, `ω = w/r_m ∈ (0,1)`,
`β := 1 − ω`. Los recursos del intercambio son dos nidos raíz `A = N(1)` y
`B = N(β)`, más el anidamiento recursivo dentro del propio `S` (un aro `x` cabe en
el agujero de `y` si `x ≤ y − ω`). Para hermanos en un disco de capacidad `c` la
factibilidad es: un círculo, `s ≤ c`; dos, `s + s′ ≤ c` (exacto, Lema 0 y
tangencia); tres, el criterio angular `feas3` (exacto para tres círculos en un
disco; validado en el repo contra los tres valores publicados en `resultados.md`).

`ρ_needed(S) = máx( ΣS, máx_j (Σ_{l>j} s_l)/s_j )` y
`ρ*₃(ω) = ínf { ρ_needed(S) : S = {s₁ ≥ s₂ ≥ s₃} ⊂ (0,1) no reinsertable }`.

## 2. La caracterización

**Proposición 4 (perfiles de tres aros).** Sean `s₁ ≥ s₂ ≥ s₃` en `(0,1)` y
`ω ∈ (0,1)`. `S` **no** es reinsertable en `N(1) ⊎ N(1−ω)` si y solo si se da
exactamente uno de los cuatro casos siguientes (mutuamente excluyentes por la
posición de `s₁, s₂` respecto de `β`):

| caso | región | condición de bloqueo |
|---|---|---|
| (i) | `s₂ > β` | `s₁ + s₂ > 1` (y entonces `s₃` es libre) |
| (ii) | `s₂ > β`, `s₁ + s₂ ≤ 1` | `s₃ > β` y el trío `{s₁,s₂,s₃}` no cabe en el disco unidad (`feas3`) |
| (iii) | `s₂ ≤ β < s₁` | `s₁ + s₃ > 1` y `s₂ + s₃ > β` y `s₃ > s₁ − ω` |
| (iv) | `s₁ ≤ β` | `s₂ + s₃ > 1` y `s₃ > s₁ − ω` |

El caso (ii) solo es habitable si `ω > 1/2` (de `s₁ + s₂ > 2β` y `s₁ + s₂ ≤ 1`).

*Demostración.* Primero la lista finita de colocaciones. Un padre debe exceder a
su hijo en al menos `ω`, luego los posibles bosques de anidamiento sobre
`{s₁,s₂,s₃}` son: sin aristas; una arista (`s₃` en `s₁`, `s₃` en `s₂`, `s₂` en
`s₁`); la cadena (`s₃` en `s₂` en `s₁`); y la estrella (`s₂, s₃` hermanos en el
agujero de `s₁`). Los aros de nivel superior se reparten entre `A` y `B` con las
condiciones de hermanos del §1. `S` es reinsertable si y solo si alguna de estas
combinaciones (finitas) es factible.

*Caso (i), suficiencia del bloqueo.* Ni `s₁` ni `s₂` caben en `B` (`> β`), y `s₂`
no puede anidar en `s₁` (`s₂ ≤ s₁ − ω < β < s₂` es imposible); ninguno tiene otro
padre posible, así que ambos son de nivel superior y ambos deben ir a `A`, pero
`s₁ + s₂ > 1` lo impide (criterio exacto del par). Bloqueado, sea cual sea `s₃`.

*Caso (i)/(ii), necesidad.* Si `s₂ > β` y `s₁ + s₂ ≤ 1` hay dos salidas: si
`s₃ ≤ β`, colóquese `{s₁, s₂}` en fila en `A` (Lema 0) y `s₃` en `B` —
reinsertable; si `s₃ > β`, los tres están en la banda `(β, 1)`: `B` es inservible,
nadie anida (`s_i − ω < 1 − ω = β < s₃`), luego los tres deben ir a `A` y la
reinsertabilidad equivale exactamente a `feas3({s₁,s₂,s₃}, 1)`. Eso es el caso
(ii), y su condición es también suficiente por el mismo argumento.

*Caso (iii).* (⇐) `s₁ > β` no cabe en `B` ni tiene padre: `s₁ ∈ A`. Nadie anida:
`s₃ > s₁ − ω ≥ s₂ − ω` mata las tres aristas (`s₂ ≥ s₃ > s₁ − ω` mata `s₂` en
`s₁`). `s₂` o `s₃` junto a `s₁` en `A` exige `s₁ + s_i ≥ s₁ + s₃ > 1`: imposible.
Luego `s₂` y `s₃` deben ir ambos a `B`, y `s₂ + s₃ > β` lo impide. (⇒) Si
`s₁ + s₃ ≤ 1`: `{s₁, s₃}` en `A`, `s₂` en `B` (`s₂ ≤ β`). Si `s₂ + s₃ ≤ β`:
`{s₂, s₃}` en `B`, `s₁` en `A`. Si `s₃ ≤ s₁ − ω`: `s₃` anidado en `s₁`, `s₁` en
`A`, `s₂` en `B`. ∎ (caso iii)

*Caso (iv).* (⇐) `s₂ + s₃ > 1` hace infactible **todo par** en cualquier
contenedor raíz (`s_i + s_j ≥ s₂ + s₃ > 1 > β`), luego cada raíz aloja a lo sumo
un aro de nivel superior: dos raíces no bastan para tres aros salvo que alguien
anide, y `s₃ > s₁ − ω` mata todas las aristas como en (iii). (⇒) Si
`s₂ + s₃ ≤ 1`: `{s₂, s₃}` en `A`, `s₁` en `B` (`s₁ ≤ β`). Si `s₃ ≤ s₁ − ω`: `s₃`
en `s₁`, `s₁` en `A`, `s₂` en `B`. ∎

**Estado.** Los casos (i), (iii), (iv) son completamente elementales (Lema 0 +
criterio del par). El caso (ii) delega en la exactitud del criterio angular para
tres círculos, con el mismo estatus que tiene en el repo (`reinserta.feas3`,
validado numéricamente contra `resultados.md`). Validación adicional:
`tresk.py` contrasta la caracterización contra `accepts()` en 12 600 perfiles
(muestreo uniforme + dirigido a las franjas críticas) sobre 14 valores de `ω`,
con **cero desacuerdos**; nótese que para `k = 3` `accepts()` es exacto (grupos de
a lo sumo tres círculos: fila, suma del par, criterio angular; el solver físico no
interviene nunca).

## 3. La fórmula cerrada

**Corolario 3.** Para todo `ω ∈ (0,1)`, con `φ = (1+√5)/2`:

    ρ*₃(ω) = máx( 1, mín( 2(1−ω), máx( φ, 2/(1+2ω) ) ) )

es decir, por tramos:

| tramo | ρ*₃(ω) | familia extremal (ε → 0⁺) |
|---|---|---|
| `0 < ω ≤ (√5−2)/2 ≈ 0.1180` | `2/(1+2ω)` | `{½+ω, ½+ε, ½+ε}` (caso iv) |
| `(√5−2)/2 ≤ ω ≤ 1−φ/2 ≈ 0.1910` | `φ` | `{1/φ, ½+ε, ½+ε}` (caso iv) |
| `1−φ/2 ≤ ω ≤ 1/2` | `2(1−ω)` | `{β+ε, β+ε, δ}` (caso i) |
| `ω ≥ 1/2` | `1` | `{½+ε, ½+ε, δ}` (caso i) |

El ínfimo no se alcanza (las condiciones de bloqueo son abiertas), igual que en la
Proposición 1. La fórmula es continua: en `ω₁ = (√5−2)/2 = 1/φ − 1/2` vale
`2/(1+2ω₁) = 2/(√5−1) = φ`, y en `ω₂ = 1 − φ/2` vale `2(1−ω₂) = φ`.

*Demostración.* Se calcula el ínfimo de `ρ_needed` en cada caso de la
Proposición 4 y se toma el mínimo.

**Caso (i).** `ρ ≥ Σ ≥ s₁ + s₂ > máx(1, 2β)` (la suma del par supera `1` por
hipótesis y `2β` porque ambos superan `β`). La familia
`s₁ = s₂ = máx(β, ½) + ε`, `s₃ = δ → 0` está bloqueada y su `ρ_needed` tiende a
`máx(1, 2β)`: los cocientes de cola tienden a `1` y a `0`. Ínfimo:
`máx(1, 2(1−ω))` — exactamente `ρ*₂(ω)`. (Es el "par de la Proposición 1 más
polvo": muestra en particular `ρ*₃ ≤ ρ*₂` para todo `ω`, y con el mismo argumento
`ρ*_{k+1} ≤ ρ*_k`.)

**Caso (ii)** (solo `ω > 1/2`). Todo perfil bloqueado tiene `Σ > 1` (si `Σ ≤ 1` el
Lema 0 lo mete en fila en `A`, contradiciendo la infactibilidad del trío), luego
su ínfimo es `≥ 1`, que es el valor de la fórmula en `ω ≥ 1/2`. No baja el mínimo.

**Caso (iii).** `s₃ > máx(1 − s₁, s₁ − ω)` y `s₂ ≥ s₃` dan
`Σ ≥ s₁ + 2·máx(1 − s₁, s₁ − ω) =: g(s₁)`, con `g` decreciente hasta
`s₁ = (1+ω)/2` y creciente después; su mínimo es `g((1+ω)/2) = (3−ω)/2`, pero
además `s₁ > β`. Si `ω ≤ 1/3` entonces `β ≥ (1+ω)/2` y
`Σ > g(β) = 3 − 5ω ≥ 2 − 2ω`; si `ω ∈ (1/3, 1/2)`, `Σ > (3−ω)/2 ≥ 2 − 2ω`; si
`ω ≥ 1/2`, `Σ ≥ s₁ + s₃ > 1`. En los tres rangos el caso (iii) queda dominado por
el valor de la fórmula (que es `≤ 2(1−ω)` y `≤ 1` respectivamente): nunca aporta
el mínimo.

**Caso (iv).** Sea `q = s₂ + s₃`. Las cotas de `ρ_needed` relevantes son
`ρ ≥ s₁ + q` y `ρ ≥ q/s₁`, y las restricciones de bloqueo implican `q > 1` y
`q ≥ 2s₃ > 2(s₁ − ω)`, con `s₁ ≤ β`. Por tanto

    ínf caso (iv) ≥ ínf { máx(s₁ + q, q/s₁) : 0 < s₁ ≤ β, q > máx(1, 2(s₁−ω)) }.

Para `s₁` fijo ambas cotas crecen con `q`, así que `q → Q(s₁) := máx(1, 2(s₁−ω))`.

- Rama `s₁ ≥ ½ + ω` (`Q = 2(s₁−ω)`): `máx(3s₁ − 2ω, 2 − 2ω/s₁)`, ambas crecientes
  en `s₁`; mínimo en el extremo izquierdo, `máx(3/2 + ω, 2/(1+2ω))`.
- Rama `s₁ ≤ ½ + ω` (`Q = 1`): `h(s₁) = máx(s₁ + 1, 1/s₁)`, decreciente hasta el
  cruce `s₁² + s₁ = 1`, es decir `s₁ = 1/φ`, donde vale `1 + 1/φ = φ`, y creciente
  después. El mínimo de la rama está en `s₁* = mín(β, ½+ω, 1/φ)`.

Comparando (verificado en simbólico, `tresk.py` §1): si `ω ≤ ω₁ = (√5−2)/2`,
`s₁* = ½ + ω` y el ínfimo es `2/(1+2ω)` (que domina a `3/2 + ω` exactamente en ese
rango: el cruce `2/(1+2ω) = 3/2 + ω` es `2ω² + 4ω − ½ = 0`, de raíz positiva
`(√5−2)/2`); si `ω₁ ≤ ω ≤ 1 − 1/φ = (3−√5)/2 ≈ 0.382`, `s₁* = 1/φ` y el ínfimo es
`φ`; si `(3−√5)/2 ≤ ω < 1/2`, `s₁* = β` y el ínfimo es
`máx(2−ω, 1/(1−ω)) = 1/(1−ω)` (cruce en `(2−ω)(1−ω) = 1`, raíz `(3−√5)/2`),
que supera `2(1−ω)` en ese rango: dominado por el caso (i). Para `ω ≥ 1/2` el caso
(iv) es vacío (`s₂ + s₃ ≤ 2s₁ ≤ 2β < 1`).

La cota inferior se aproxima: la familia `s₂ = s₃ = q/2` con `s₁` en el mínimo de
cada rama satisface todas las restricciones de bloqueo con holgura `ε` (en el
tramo 1, `s₁ = ½+ω`, `s₂ = s₃ = ½+ε`: `s₂+s₃ = 1+2ε > 1` y
`s₃ = ½+ε > ½ = s₁−ω`; análogo en la meseta). Luego el ínfimo del caso (iv) es
exactamente `2/(1+2ω)`, `φ`, `1/(1−ω)` en sus tres tramos.

**Mínimo global.** `2/(1+2ω) < 2(1−ω)` en `(0, ½)` (equivale a `ω(1−2ω) > 0`), y
`φ ≤ 2(1−ω) ⟺ ω ≤ ω₂`: el mínimo entre casos es el enunciado. ∎

**Estado: demostrado.** La prueba del Corolario 3 no usa el caso (ii) ni `feas3`:
es íntegramente aditiva (Lema 0 + criterio exacto del par). En el ínfimo de `k=3`
no hay geometría de Descartes en absoluto. Verificación numérica (`tresk.py`):
las familias testigo con `ε = 10⁻⁵` están bloqueadas según `accepts()` y su
`ρ_needed` dista `< 4·10⁻⁵` de la fórmula en 15 valores de `ω`; la búsqueda por
descenso multi-arranque sobre la región bloqueada no encuentra nada por debajo de
la fórmula (diferencias entre `+3·10⁻⁷` y `+3·10⁻⁴`, todas positivas, como
corresponde a un ínfimo no alcanzado); los flips de frontera (relajar una sola
desigualdad) reactivan la reinserción en todos los casos.

## 4. Consecuencias

**Corolario 4 (cruce con Tribonacci en forma cerrada).** `ρ*₃(ω) = T` exactamente
en

    ω_T = 1/T − 1/2 = T² − T − 3/2 ≈ 0.043689

(la segunda identidad módulo `T³ = T² + T + 1`; verificada en simbólico). Para
`ω < ω_T` ningún perfil de dos **ni de tres** aros bloquea con `ρ < T`; para
`ω > ω_T` el testigo `{½+ω, ½+ε, ½+ε}` bloquea con `ρ = 2/(1+2ω) < T`. Como
`ρ*₃ ≤ ρ*₂` en todo punto, la garantía combinatoria de reinserción con `ρ < T`
para perfiles de hasta 3 aros vale exactamente hasta `ω_T`, que sustituye (y
rebaja) la estimación `ω_c ≈ 0.05` de `reinsercion.md` §6. Por el Corolario 2 el
único tamaño de perfil que podría rebajar aún más el umbral es `k = 4`: queda
`ω_c ∈ [algo ≤ ω_T que fije k=4, ω_T]`, con la evidencia numérica de §6
(columna `k=4` ≈ columna `k=3` tras corregir el mínimo local) sugiriendo
`ρ*₄ = ρ*₃`, es decir `ω_c = ω_T`. Abierto.

**La conjetura de la curva era falsa.** Ni `c·(1−ω)` con `c < 2` ni `2/√3 − 1`:
el tramo dominante es la hipérbola `2/(1+2ω)`, que sobre el rango muestreado
`ω ∈ [0.03, 0.08]` se ajusta casualmente bien a una recta de pendiente ≈ `−2c` —
de ahí la impresión numérica. El umbral `2√3 − 3` (tres círculos iguales) no
aparece porque el perfil extremal nunca pone los tres aros en la banda: pone
**dos gemelos en ½** y un mayor en `½ + ω`, y toda la infactibilidad es de pares.

**La meseta áurea.** En `ω ∈ [ω₁, ω₂]` el ínfimo es constante `= φ`, procedente
de `mín_s máx(1+s, 1/s) = φ` en `s = 1/φ`: la razón áurea reaparece por tercera
vía, ahora sin bolsillos de Descartes — puro equilibrio entre la presión de la
suma (`1 + s₁`) y la presión de la cola (`1/s₁`) del perfil `{s₁, ½, ½}`. Nótese
que `ρ*₃ > φ` para `ω < ω₁`: la protección combinatoria de tres aros nunca baja
de `φ` antes de la meseta, el mismo suelo que el bolsillo de Descartes da por vía
geométrica en la Proposición 2. Si es coincidencia o no, queda abierto.

**Corrección a la tabla de `reinsercion.md` §6.** Los valores de la columna
`k=3` para `ω ≤ 0.08` eran mínimos locales del descenso por coordenadas
(quedaban ~0.02–0.03 por encima del ínfimo real; p. ej. `ω = 0.05`: tabla
`1.846`, real `1.8182`; el perfil hallado `{0.645, 0.585, 0.585}` es un punto
crítico de la esquina `Σ = cola`, no el óptimo `{0.55, 0.5, 0.5}`). Las columnas
con `ω ≥ 0.12` sí coinciden con la fórmula (`1.618 = φ`, `1.601 ≈ 2(1−ω)+δ`,
`1.101 ≈ 2(1−ω)+δ`). La conclusión cualitativa de §6 no cambia (por debajo de
`ω_c` la combinatoria cierra), pero `ω_c` pasa de `≈ 0.05` medido a `≤ 0.043689`
demostrado (con igualdad si `ρ*₄ = ρ*₃`).

## 5. Huecos declarados

1. **Caso (ii) y `feas3`.** La exactitud del criterio angular para tres círculos
   en un disco se usa tal cual la usa el repo (validada numéricamente, no
   demostrada aquí). Afecta solo a la caracterización en `ω > 1/2`, no a la
   fórmula de ρ*₃.
2. **`ρ*₄`.** La fórmula cerrada para perfiles de cuatro aros sigue abierta; el
   argumento del polvo da `ρ*₄ ≤ ρ*₃` y el Corolario 2 excluye `k ≥ 5` bajo `T`,
   pero no hay prueba de `ρ*₄ = ρ*₃` (solo la evidencia numérica de §6).
3. **Infimo vs. mínimo.** ρ*₃ es un ínfimo no alcanzado; las instancias reales
   con `ρ` cerca del ínfimo requieren tangencias casi exactas, como en todo el
   resto del programa.

## Mapa de verificación

- `code/tresk.py` — (1) identidades simbólicas en sympy (cruces `ω₁`, `ω₂`,
  mínimo áureo de `máx(1+s, 1/s)`, `ω_T` módulo el polinomio de Tribonacci);
  (2) caracterización contra `accepts()` de `reinserta.py`, 12 600 perfiles,
  0 desacuerdos; (3) familias testigo bloqueadas con `ρ_needed` a `< 4·10⁻⁵` de
  la fórmula; (4) flips de frontera; (5) descenso multi-arranque sobre la región
  bloqueada: nada por debajo de la fórmula; (6) contraste con la tabla de
  `reinsercion.md` §6 (la fórmula es ≤ tabla en todo punto, como corresponde a
  una tabla de cotas superiores).
