# El suelo de Tribonacci en la subfamilia rígida: teorema sin idealización

Borrador. Resuelve el punto 1.4 de `hoja_de_ruta.md`: en la subfamilia con
`R = r₁ + r₂` (tangencia diametral exacta), el suelo `T` de la familia de
4 aros se demuestra **como teorema**, sin la idealización tangente `r₃ → r₂`
y sin límite `w → 0`. La numeración de lemas es local a este borrador
(S1–S4, Proposiciones S5–S6). Verificación: `code/rigido.py`.

**Resumen.** Las dos presiones de la construcción —el trío `{r₁, r₃, r₄}` no
empaqueta en la sartén; la pareja `{r₃, r₄}` cabe en el agujero de `r₁`—
implican `ρ > T` para **toda** instancia de la subfamilia, con grosor `w > 0`
arbitrario y `r₃ < r₂` estricto. El álgebra `t³ + t² + t < 1` sale de comparar
la cota inferior `r₃ + r₄ > r₂ + b(r₂)` (consecuencia de la infactibilidad,
Lemas S1–S4) con la cota superior `r₃ + r₄ < r₁` (el testigo), exactamente
como predecía la idealización pero sin usarla. La pieza nueva que elimina la
idealización es una reducción trigonométrica exacta: la infactibilidad del
trío equivale (en la dirección constructiva, la única que se usa) a la
desigualdad algebraica `ψ(u) + ψ(v) < τ` con `ψ(x) = √((t−x)/x)` y
`τ = t/√(1+t)`, y el mínimo de `u + v` bajo esa condición se calcula en forma
cerrada por concavidad: es `t + b(t)`, alcanzado en la esquina rígida
`u = t`, `v = b(t)`. La configuración rígida no se supone: **aparece como el
caso extremo de una optimización**. El ínfimo `T` es exacto y no se alcanza
(Proposición S6). La razón áurea reaparece como divisor de casos: para
`t ≥ 1/φ` la subfamilia es directamente vacía.

## 1. Marco y subfamilia

Modelo de `resultados.md` §1. Una instancia de 4 aros `(R, w; r₁ > r₂ > r₃ >
r₄ > 0)`, `w > 0`. Todo se normaliza por `r₁`: escribimos `t = r₂/r₁`,
`u = r₃/r₁`, `v = r₄/r₁`, `ω = w/r₁`, y el disco de la sartén tiene radio
`R/r₁`. Recordamos `ρ = máx_i (Σ_{j>i} r_j)/r_i`; en particular
`ρ ≥ ρ₂ = (u+v)/t`.

**Definición (subfamilia rígida `F`).** La instancia pertenece a `F` si

- **(F1)** `R = r₁ + r₂` — tangencia diametral exacta: la sartén queda llena
  por `{r₁, r₂}`, normalizado `R = 1 + t`;
- **(F2)** `r₃ + r₄ ≤ r₁ − w` — la pareja cabe en el agujero de `r₁`:
  `u + v ≤ 1 − ω`;
- **(F3)** el trío `{r₁, r₃, r₄}` **no** empaqueta en el disco de radio `R`:
  `{1, u, v}` no empaqueta en `1 + t`.

(F2) es la mitad del testigo del gadget de `resultados.md` §5ter (la otra
mitad, `{r₁, r₂}` en la sartén, es (F1)); (F3) es la presión de bloqueo. Las
condiciones de cierre del gadget completo (`r₄` no cabe junto a `r₂` en el
agujero de `r₁`, ni en los agujeros de `r₂, r₃`) **no se necesitan**: solo
añaden restricciones, así que todo gadget con patrón I1 y sartén rígida está
en `F` y hereda la cota del teorema. El contraejemplo `n = 4` y la gemela I1
están en `F` (verificado, `rigido.py` V8).

Constantes: `T = 1.83929…` (raíz de `x³ = x² + x + 1`), `t* = 1/T = 0.54369…`
(raíz de `t³ + t² + t = 1`), `φ = (1+√5)/2`, y el bolsillo de Descartes de la
configuración rígida `{1, t}` en `R = 1 + t`:

    b(t) = t(1+t)/(1+t+t²)

(caso `A = 1, B = t` de la fórmula `AB(A+B)/(A²+AB+B²)` de `resultados.md`
§5bis, normalizado a `r₁ = 1`; el diccionario con el `b(α)` de
`reinsercion.md` §7 es `α = 1/t` y `b_α(α) = b(t)/t`).

## 2. Enunciado

**Teorema S (suelo rígido).** Toda instancia de `F` cumple `ρ > T`, con
desigualdad estricta y sin hipótesis adicionales sobre `w` ni sobre las
holguras. Además el suelo es exacto: `ínf { ρ(I) : I ∈ F } = T`, no
alcanzado (Proposición S6). De paso, `F` solo está habitada si `t < t*`:
si `r₂ ≥ t*·r₁` no existe ningún bloqueo del trío compatible con el testigo.

La prueba usa cuatro lemas. Ninguno invoca la exactitud del criterio angular
`feas3` ni ninguna otra afirmación no demostrada del repo: de la
factibilidad de tríos solo se usa la **dirección constructiva** (exhibir un
empaquetamiento), que es la contrapositiva correcta frente a (F3).

## 3. Lema S1: el medio ángulo

Para dos círculos de radios `a, b` **tangentes interiormente a la pared** de
un disco de radio `R` (centros a distancias `R−a`, `R−b` del centro), la
separación angular mínima `θ(a,b)` que garantiza interiores disjuntos
satisface

    sin²(θ/2) = f(a)·f(b),     f(x) := x/(R−x).

**Lema S1.** Si `a + b ≤ R`, entonces `f(a)f(b) ≤ 1`, el ángulo
`θ(a,b) = 2 arcsin √(f(a)f(b)) ∈ [0, π]` está bien definido, y dos círculos
tangentes a la pared con separación angular `γ` tienen interiores disjuntos
si y solo si `γ ≥ θ(a,b)`. Además `θ` es creciente en `a` y en `b`.

*Demostración.* Ley de cosenos entre centros: la distancia `D(γ)` cumple
`D² = (R−a)² + (R−b)² − 2(R−a)(R−b)cos γ`, creciente en `γ ∈ [0, π]`.
Interiores disjuntos ⟺ `D ≥ a + b`. En el umbral,
`1 − cos θ = [(a+b)² − ((R−a)−(R−b))²] / (2(R−a)(R−b))
= [(a+b)² − (a−b)²] / (2(R−a)(R−b)) = 2ab/((R−a)(R−b))`,
y `sin²(θ/2) = (1−cos θ)/2 = f(a)f(b)`. La condición `f(a)f(b) ≤ 1` es
`ab ≤ R² − R(a+b) + ab`, es decir `a + b ≤ R`. La monotonía es la de `f`. ∎

(`rigido.py` V1 contrasta esta forma cerrada con el `sep_angle` del repo:
coinciden a `4·10⁻¹⁵`.)

## 4. Lema S2: la construcción

**Lema S2.** Sean `v ≤ u ≤ t < 1` y `R = 1 + t`. Si

    θ(1,u) + θ(1,v) + θ(u,v) ≤ 2π,

entonces `{1, u, v}` empaqueta en el disco de radio `R`.

*Demostración.* Los tres ángulos están definidos: `1 + u ≤ R ⟺ u ≤ t`,
`1 + v ≤ R`, y `u + v ≤ 2t < R`. Colóquense los tres círculos tangentes a la
pared, con el `1` en medio: centro de `1` en ángulo `0`, centro de `u` en
`+θ(1,u)`, centro de `v` en `−θ(1,v)`. Cada círculo es interiormente
tangente a la pared, luego está contenido en el disco. Pares:

- `(1,u)` y `(1,v)`: separación angular exactamente `θ(1,u)` y `θ(1,v)`;
  disjuntos por el Lema S1 (caso frontera: tangentes).
- `(u,v)`: la diferencia de posiciones angulares es `Δ = θ(1,u) + θ(1,v)`,
  y el ángulo entre los dos radios vectores es `γ = mín(Δ, 2π − Δ) ∈ [0, π]`.
  Si `γ = Δ`: por monotonía (Lema S1, `1 ≥ u`), `θ(1,v) ≥ θ(u,v)`, luego
  `Δ ≥ θ(u,v)`. Si `γ = 2π − Δ`: la hipótesis da
  `2π − Δ ≥ θ(u,v)`. En ambos casos `γ ≥ θ(u,v)` y el par es disjunto. ∎

La colocación es explícita; `rigido.py` V2 la construye y comprueba las seis
desigualdades geométricas directamente (distancias y contención) en ~60 000
casos, sin usar ningún criterio de factibilidad.

## 5. Lema S3: la reducción algebraica

Aquí está el paso que sustituye a la idealización. Definimos

    ψ(x) := √((t−x)/x)   (decreciente en x, ψ(t) = 0),
    τ    := t/√(1+t),

y registramos dos identidades exactas (verificadas en simbólico, `rigido.py`
V5): `ψ(b(t)) = τ` y `t/(1+τ²) = b(t)` — es decir, `ψ` y `τ` codifican el
bolsillo rígido.

**Lema S3.** Sean `v ≤ u ≤ t < 1`, `R = 1 + t`. Si `ψ(u) + ψ(v) ≥ τ`,
entonces `θ(1,u) + θ(1,v) + θ(u,v) ≤ 2π` (y por el Lema S2 el trío
empaqueta).

*Demostración.* Con `A = √(f(1)f(u))`, `B = √(f(1)f(v))`, `C = √(f(u)f(v))`
(los senos de los semiángulos, Lema S1), la conclusión es

    arcsin A + arcsin B + arcsin C ≤ π.

Caso 1: `arcsin A + arcsin B ≤ π/2`. Entonces
`π − arcsin A − arcsin B ≥ π/2 ≥ arcsin C` y no hay nada que probar.

Caso 2: `arcsin A + arcsin B > π/2`. La conclusión equivale a
`arcsin C ≤ π − arcsin A − arcsin B ∈ [0, π/2)`, y como `arcsin` es
creciente y ambos miembros viven en `[0, π/2]`, equivale a

    C ≤ sin(arcsin A + arcsin B) = A√(1−B²) + B√(1−A²).

Dividiendo por `C > 0`:

    A√(1−B²)/C = √( f(1)(1 − f(1)f(v)) / f(v) ) = √G(v),
    B√(1−A²)/C = √G(u),      con  G(x) := f(1)/f(x) − f(1)².

Con `f(1) = 1/t` y `f(x) = x/(1+t−x)` sale, en forma cerrada,

    G(x) = (1+t)(t−x) / (t²x),   es decir   √G(x) = (√(1+t)/t)·ψ(x).

(Las raíces son reales porque `f(1)f(x) ≤ 1 ⟺ x ≤ t`.) Por hipótesis,

    √G(u) + √G(v) = (√(1+t)/t)(ψ(u) + ψ(v)) ≥ (√(1+t)/t)·τ = 1,

que es exactamente la desigualdad requerida. ∎

Nótese la lectura: la condición `ψ(u)+ψ(v) ≥ τ` es una **condición
suficiente algebraica de empaquetamiento del trío**, exacta en la esquina
rígida (`u = t`: se reduce a `ψ(v) ≥ τ ⟺ v ≤ b(t)`, el bolsillo). La
contrapositiva que usaremos: **(F3) ⟹ `ψ(u) + ψ(v) < τ`.**

## 6. Lema S4: el mínimo de la suma está en la esquina rígida

**Lema S4.** Sean `0 < v ≤ u ≤ t < 1` con `ψ(u) + ψ(v) < τ`. Entonces:

1. `u > b(t)` y `v > b(t)`;
2. si `t ≥ 1/φ` (es decir `t² + t ≥ 1`): `u + v > 1`;
3. si `t < 1/φ`: `u + v > t + b(t)`.

*Demostración.* (1) Cada sumando es menor que `τ`; `ψ` es decreciente y
`ψ(b(t)) = τ`, luego `u, v > b(t)`.

(2) `u + v > 2b(t)`, y `2b(t) − 1 = (t²+t−1)/(t²+t+1) ≥ 0` exactamente
cuando `t ≥ 1/φ` (identidad V5; la raíz áurea de nuevo).

(3) Cambio de variables `α = ψ(u), β = ψ(v)`, es decir `u = U(α)`,
`v = U(β)` con `U(z) = t/(1+z²)`, estrictamente decreciente; la región es
`α, β ≥ 0`, `α + β < τ`. Sea `β` fijo y auméntese `α` hasta `τ − β`: como
`U` es estrictamente decreciente,

    u + v = U(α) + U(β) > U(τ−β) + U(β) =: W(τ−β).

Ahora `U''(z) = 2t(3z²−1)/(1+z²)³ ≤ 0` para `z ≤ 1/√3`, y
`τ ≤ 1/√3 ⟺ 3t² − t − 1 ≤ 0 ⟺ t ≤ (1+√13)/6 = 0.7676…`, que cubre con
holgura el caso `t < 1/φ = 0.6180…` (identidades V5). Por tanto `U` es
cóncava en `[0, τ]`, `W(x) = U(x) + U(τ−x)` es cóncava en `[0, τ]`, y su
mínimo se alcanza en los extremos:

    W ≥ W(0) = U(0) + U(τ) = t + t/(1+τ²) = t + b(t),

usando la identidad `t/(1+τ²) = b(t)`. Luego `u + v > t + b(t)`. ∎

El contenido geométrico de (3): entre todos los perfiles `{u, v}` que un
bolsillo no logra absorber, el de **suma mínima** es el rígido —`u` pegado a
`t` y `v` pegado al bolsillo `b(t)`—, y los perfiles equilibrados
(`u ≈ v`) necesitan suma estrictamente mayor. Esto es lo que la idealización
`r₃ → r₂` afirmaba sin justificar; aquí es un cálculo de concavidad.

## 7. Demostración del Teorema S

Sea `I ∈ F`, normalizada. Por (F3) y la contrapositiva de S2+S3:

    ψ(u) + ψ(v) < τ.

Si `t ≥ 1/φ`, el Lema S4(2) da `u + v > 1`, contradiciendo (F2)
(`u + v ≤ 1 − ω < 1`). Luego `t < 1/φ`, y el Lema S4(3) da

    u + v > t + b(t).                                   (presión de bloqueo)

Encadenando con (F2):

    t + b(t) < u + v ≤ 1 − ω < 1,                       (presión del testigo)

y `t + b(t) < 1 ⟺ t(1+t) < (1−t)(1+t+t²) = 1 − t³ ⟺ t³ + t² + t < 1
⟺ t < t*` (identidad V5). Esto prueba de paso que `F` exige `t < t*`.
Finalmente

    ρ ≥ ρ₂ = (u+v)/t > (t + b(t))/t = 1 + (1+t)/(1+t+t²) =: L(t),

y `L` es estrictamente decreciente (`L′ = −(t²+2t)/(1+t+t²)² < 0`, V5) con
`L(t*) = 1/t* = T` (identidad módulo `t³+t²+t−1`, V5). Como `t < t*`:

    ρ > L(t) > L(t*) = T.   ∎

Las "dos presiones" de la hoja de ruta son exactamente las dos líneas
centradas: la infactibilidad empuja `u + v` por encima de `t + b(t)` y el
testigo lo retiene por debajo de `1`; su compatibilidad es la cúbica
`t³ + t² + t < 1`, y el cociente `ρ₂ = (u+v)/t` queda atrapado por encima de
`L(t) ≥ T`. En el diccionario `α = 1/t` del resto del repo,
`L(t) = 1 + b_α(α)`, la misma expresión de `resultados.md` §5quater y de la
Proposición 3 de `reinsercion.md` — pero ahora obtenida para todo `u < t` y
todo `ω > 0`, sin idealización tangente y sin límite de grosor.

## 8. Exactitud del suelo

### Proposición S5 (el bolsillo rígido es exacto)

**Proposición S5.** Para `0 < v ≤ t < 1`, el trío `{1, t, v}` empaqueta en
el disco de radio `R = 1 + t` si y solo si `v ≤ b(t)`.

*Demostración.* **Rigidez.** En cualquier empaquetamiento, los centros
cumplen `|c₁| ≤ R − 1 = t`, `|c_t| ≤ R − t = 1` y `|c₁ − c_t| ≥ 1 + t`. La
desigualdad triangular da `1 + t ≤ |c₁ − c_t| ≤ |c₁| + |c_t| ≤ t + 1`:
igualdad en todo. Luego `c₁` y `c_t` son antipodales con `|c₁| = t`,
`|c_t| = 1`; salvo rotación, `c₁ = (−t, 0)`, `c_t = (1, 0)`.

**Suficiencia.** El círculo del bolsillo, tangente a la pared, al `1` y al
`t`, tiene radio `b(t)` (su centro se obtiene resolviendo el sistema de
tangencias; `rigido.py` V6 verifica los residuos a `10⁻⁹`); cualquier
`v ≤ b(t)` colocado concéntrico dentro de él es disjunto de ambos y queda en
el disco.

**Necesidad.** Sea `X` el centro del círculo `v`, `d = |X|`, y `γ` el ángulo
entre `X` y `(1,0)`. Si `d = 0`, `|X − c₁| = t < 1 + v`: imposible; luego
`d > 0`. Las condiciones de disyunción son

    d² + t² + 2dt·cos γ ≥ (1+v)²   y   d² + 1 − 2d·cos γ ≥ (t+v)²,

que acotan `cos γ` por abajo y por arriba; su compatibilidad exige

    (1+t)·d² ≥ (1+v)² + t(t+v)² − t(1+t),

y con `d ≤ R − v = 1 + t − v`:

    (1+t)(1+t−v)² − (1+v)² − t(t+v)² + t(1+t) ≥ 0.

El miembro izquierdo factoriza **exactamente** (simbólico, V5) como

    4·[ t(t+1) − v(t²+t+1) ]  =  4(t²+t+1)·(b(t) − v),

luego `v ≤ b(t)`. ∎

Obsérvese que esta es la única pieza de la prueba donde la configuración
rígida se usa como tal, y su papel es solo la **exactitud** del suelo (la
dirección `≤` del ínfimo); el Teorema S no la necesita.

### Lema S6a (cierre y monotonía de la factibilidad)

Formalizamos el ingrediente topológico que la Proposición S6 necesita. Sea
`D := {(t, u, v) : 0 < v ≤ u ≤ t < 1}` y, para `p = (t, u, v) ∈ D`, dígase
que `p` **empaqueta** si existen centros `c₁, c₂, c₃ ∈ ℝ²` con

    |c₁| ≤ t ,   |c₂| ≤ 1 + t − u ,   |c₃| ≤ 1 + t − v ,
    |c₁ − c₂| ≥ 1 + u ,   |c₁ − c₃| ≥ 1 + v ,   |c₂ − c₃| ≥ u + v

(contención en el disco `R = 1 + t` y disyunción de interiores; es la misma
noción usada en todo el documento). Sea `E ⊆ D` el conjunto de los `p` que
empaquetan.

**Lema S6a.**

1. **(monotonía)** Si `(t, u, v) ∈ E`, `u′ ≤ u`, `v′ ≤ v` y
   `(t, u′, v′) ∈ D`, entonces `(t, u′, v′) ∈ E`.
2. **(cierre)** `E` es cerrado en `D`.
3. **(apertura cuantificada de la infactibilidad)** Para `t, v` fijos, el
   conjunto `U := {u ∈ [v, t] : (t, u, v) ∈ E}` es vacío o un intervalo
   cerrado `[v, u_máx]` con el máximo **alcanzado**. En particular, si
   `(t, t, v) ∉ E`, entonces `(t, u, v) ∉ E` para todo `u ∈ (u_máx, t]`:
   la infactibilidad de la esquina rígida se propaga a un intervalo
   explícito `δ ∈ (0, δ₀]`, `δ₀ := t − u_máx > 0` (y a todo `[v, t]` si
   `U = ∅`).

*Demostración.* (1) Los mismos centros son testigo: cada cota de contención
se relaja (`1 + t − u ≤ 1 + t − u′`) y cada cota de separación también
(`1 + u ≥ 1 + u′`, `u + v ≥ u′ + v′`).

(2) Sean `p_k = (t_k, u_k, v_k) ∈ E` con `p_k → p ∈ D`, y `(c₁ᵏ, c₂ᵏ, c₃ᵏ)`
testigos. Todos los centros viven en la bola `|c| ≤ 1 + t_k ≤ 2`, luego la
sucesión de testigos vive en un compacto de `(ℝ²)³ ≅ ℝ⁶` y una subsucesión
converge a `(c₁, c₂, c₃)`. Las seis restricciones son de la forma
`g(c₁, c₂, c₃; t, u, v) ≥ 0` con `g` continua, y valen a lo largo de la
subsucesión; pasando al límite valen en `(c₁, c₂, c₃; p)`. Luego `p ∈ E`.

(3) Por (1), `U` es decreciente-cerrado (si contiene `u`, contiene
`[v, u]`); por (2) es cerrado en `[v, t]`; luego es `∅` o `[v, u_máx]` con
`u_máx ∈ U`. Si `(t, t, v) ∉ E` entonces `u_máx < t`, y todo
`u ∈ (u_máx, t]` queda fuera de `E`. ∎

Nada aquí usa geometría fina: es el argumento estándar de que un sistema de
desigualdades **no estrictas** con testigos en un compacto define un conjunto
cerrado, más la observación de que encoger radios nunca rompe un
empaquetamiento. El punto (3) es la única forma en que la Proposición S6 lo
usa; de propina, hace **explícito** el `δ₀` que antes era existencial.

### Proposición S6 (el ínfimo es T y no se alcanza)

**Proposición S6.** `ínf { ρ(I) : I ∈ F } = T`, y el ínfimo no se alcanza.

*Demostración.* `≥` y no-alcance: Teorema S (estricto). `≤`: hace falta una
familia en `F` con `ρ → T`. Dos ingredientes:

*Cierre de la factibilidad.* Lema S6a(3): si `(t, t, v)` es infactible,
existe `δ₀ > 0` (a saber, `t − u_máx`) tal que `(t, t−δ, v)` es infactible
para todo `δ ≤ δ₀`.

*La familia.* Fijo `t < t*`, sea `ε_t := (1 − t − b(t))/2 > 0` y
`v_t := b(t) + mín(ε_t, (t − b(t))/2)`. Por la Proposición S5, `(t, t, v_t)`
es infactible; por apertura existe `δ ∈ (0, t − v_t)` con `(t, t−δ, v_t)`
infactible. La instancia `I_t = (1, t, t−δ, v_t)` con
`ω := 1 − (t − δ + v_t) > ε_t − δ > 0` (tomando `δ < ε_t`) cumple (F1)–(F3)
y los órdenes estrictos: `I_t ∈ F`. Su `ρ`:

    ρ₂ = (t − δ + v_t)/t ≤ (t + b(t) + ε_t)/t = L(t) + ε_t/t,

`ρ₁ = t + u + v < 3t < 1.7 < T` y `ρ₃ = v/u < 1`, luego
`ρ(I_t) = ρ₂ → L(t*) = T` cuando `t → t*` (pues `ε_t → 0`). ∎

`rigido.py` V7b materializa la familia con `δ` concreto (bisección del
umbral bloqueante con `feas3` como oráculo *numérico*, solo para elegir el
parámetro): `ρ − T = +9.5·10⁻², +3.7·10⁻², +1.2·10⁻², +3.9·10⁻³, +1.2·10⁻³`
para `δ = 10⁻², …, 10⁻⁶`, siempre dentro de `F`. Un dato empírico
interesante que la prueba no necesita: el umbral bloqueante crece como
`b(t) + Θ(√δ)` al separar `u = t − δ` de la esquina rígida — la protección
del bolsillo mejora en raíz cuadrada, no linealmente, al ganar holgura
(evidencia numérica, V7b).

## 9. Relación con el resto del programa y lectura

- **La escalera de `reinsercion.md` §9 se cierra por arriba.** La
  Proposición 3 de allí (plantilla canónica, `w → 0`, ínfimo `T`) queda
  subsumida: el Teorema S da la misma constante como cota inferior estricta
  válida para todo `w > 0` y sin tangencias supuestas, y la Proposición S6
  la declara óptima. La identidad `b(T) = T − 1` del repo es, en el
  diccionario `α = 1/t`, la igualdad `b(t*) = 1 − t*` que hace coincidir las
  dos presiones en `t*` (verificada en simbólico módulo ambas cúbicas, V5).
- **Dónde vive cada constante.** `φ` aparece dos veces con papeles nuevos:
  `t ≥ 1/φ ⟹ F` vacía (Lema S4(2): dos bolsillos ya desbordan el agujero), y
  la concavidad que fuerza el mínimo en la esquina rígida vale hasta
  `t = (1+√13)/6 ≈ 0.7676 > 1/φ`, con margen. `T` aparece una única vez, al
  final, como `L(t*)`: todo el resto de la prueba es geometría de bolsillos.
- **Qué añade sobre la idealización.** La idealización afirmaba dos cosas:
  que el peor perfil es el rígido y que el bolsillo rígido es exacto. La
  primera es ahora el Lema S4 (concavidad); la segunda, la Proposición S5
  (rigidez + factorización). Ninguna era falsa — pero la primera no era
  obvia: el umbral real de bloqueo con `u < t` crece como `√(t−u)`, así que
  los perfiles no rígidos son *mucho* más caros de bloquear, y el ínfimo se
  concentra en la esquina.
- **Lo que este teorema no da.** La subfamilia exige `R = r₁ + r₂` exacto.
  Para sartenes con holgura (`R > r₁ + r₂`) el bloqueo del trío involucra a
  `r₂` móvil y el análisis de `v` genérico de `reinsercion.md` §10.1 sigue
  abierto; la conjetura del umbral (ρ < T ⟹ irrelevancia, para toda
  instancia) no queda demostrada por esto.

## 10. Huecos declarados

Ninguno en la cadena principal: los Lemas S1–S4, el Teorema S y las
Proposiciones S5–S6 son demostraciones completas (las identidades algebraicas
delegadas a sympy están todas en `rigido.py` V5, 10/10). Matices de estatus:

1. **Cierre de la factibilidad** (Proposición S6) — **RESUELTO**: el antiguo
   esbozo de compacidad es ahora el Lema S6a (monotonía + cierre + apertura
   cuantificada de la infactibilidad, con `δ₀ = t − u_máx` explícito). Solo
   afectaba a la dirección `≤` del ínfimo.
2. **`feas3` no interviene en ninguna prueba.** Se usa únicamente como
   oráculo numérico en las verificaciones (V7, V8) y para elegir parámetros
   concretos en la familia aproximante. El estatus de exactitud de `feas3`
   (hueco declarado en `perfil_tres.md` §5) es irrelevante aquí.

## Mapa de verificación

`code/rigido.py` (7/7 bloques OK):

- **V1** identidad del medio ángulo contra `reinserta.sep_angle` (err `4·10⁻¹⁵`).
- **V2+V3** `ψ(u)+ψ(v) ≥ τ ⟹` construcción explícita válida: ~60 000 casos,
  0 fallos angulares, 0 geométricos (distancias verificadas directamente).
- **V4** `ψ(u)+ψ(v) < τ ⟹ u+v > t+b(t)` (o `> 1` si `t ≥ 1/φ`): ~2000 casos
  en la región, 0 fallos; V4b: el mínimo de `U(α)+U(τ−α)` está en los
  extremos y vale `t + b(t)` (exceso `0.0`).
- **V5** 10 identidades simbólicas en sympy (incluye la factorización de la
  necesidad, `L(t*) = T` y `b(T) = T−1` módulo las cúbicas).
- **V6** Proposición S5 contra geometría directa: tangencias del bolsillo a
  `10⁻⁹`, colocaciones concéntricas válidas, y barrido de 160 000 centros
  candidatos sin posición válida para `v > b(t)`. (El solver físico
  `pack_feasible` no sirve de oráculo aquí: la configuración rígida es de
  medida nula y no la encuentra — coherente con la lección de
  `resultados.md` §5ter sobre el muestreo aleatorio.)
- **V7a** malla aleatoria de `F` (oráculo `feas3`): 153 instancias, todas
  con `ρ ≥ 1.898 > T`. **V7b** familia aproximante: `ρ → T` por encima,
  dentro de `F`.
- **V8** contraejemplo `n = 4` (`ρ = 1.940`) y gemela I1 (`ρ = 1.898`)
  pertenecen a `F`.
