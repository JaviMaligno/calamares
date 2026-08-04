# Cierre de la micro-celda de j = 3 (intercambio a sartén)

Estado: **cerrada**, acta adversaria CONFIRMADO (`VEREDICTOS.md`, 2026-08-04:
ocho frentes atacados, generador independiente con 29 310 bloqueos y
mín ρ = 2.9795, sin contraejemplo).
Script: `code/microcelda.py` (5/5). Sustituye al esbozo de la torre de
`batalla2.md` §4ter, que no hacía falta.

## 0. Lo que estaba abierto

El Teorema DP (perfiles de pares) cerraba j = 3 salvo la celda

    { σ₂ ≤ ω (disco sólido), ω ≥ φ/2, y hoja fuera del subárbol de o₁,
      o₁ ≥ 3, o₂ ≥ 3/φ }

con evidencia dirigida (240 k muestras, mín ρ = 2.37) pero sin prueba. El
esbozo pendiente era una torre con suma cuadrática de nodos anidados.

## 1. Enunciado

**Teorema M.** En el intercambio a sartén con j = 3, perfil de pares, y
hoja fuera del subárbol de o₁ y o₂ ≥ 3/φ, el bloqueo implica ρ > φ
siempre que

    σ₂ + ω  ≤  11 − 4√5  =  15 − 8φ  =  2.05572…

En particular para todo ω < 1 (convenio de anchura) y todo σ₂ ≤ 1 (el par
va detrás del pivote), en la **rama A** de la dicotomía de evacuación (la
rama B es el caso (iii), cerrado aparte), lo que cubre la micro-celda entera: **σ₂ ≤ ω, ω ≥ φ/2
y o₁ ≥ 3 no se usan**.

## 2. Prueba

Por reducción al absurdo: supongamos ρ ≤ φ. Escribimos s := σ₂ + ω,
S₀ := σ₁+σ₂ (> 1 por (D)), D := polvo distinto del par (piezas de radio < 1 que no son σ₁ ni σ₂) y, para
un nodo v, X_v = radio total del contenido de su agujero y T_v = radio
total de todo su subárbol (T_v ≥ X_v).

**(a) El polvo es escaso.** La cola de m recoge σ₁, σ₂ y todo el polvo,
piezas todas de radio < 1 = r_m y distintas entre sí. Luego
ρ ≥ S₀ + D > 1 + D. Si D ≥ φ−1 saldría ρ > φ. Por tanto **D < φ−1**.

**(b) Ningún nodo de {o₁} ∪ subárbol de o₁ tiene dos hijos-nodo.** Si los
tuviera, cada hijo aporta una hoja de su propio subárbol, y son dos hojas
distintas; ambas son *estrictas* porque y está fuera del subárbol de o₁.
El ocupante de {o₂, o₃} que no contiene a y aporta una tercera. Con
jj = 3 la escalera da ρ > Ψ₃(ω) > Ψ₃(1) = √3 > φ (Ψ₃ decreciente) en la
**rama A**; la rama B es el caso (iii) del Teorema DP, ya cerrado.

**(c) La cadena.** Por (b) el subárbol de o₁ es una cadena (torre)
o₁ ⊃ z₁ ⊃ z₂ ⊃ … Sea

    V := { v ∈ {o₁} ∪ torre : la cola de v contiene a o₂ y a o₃ }

(o₁ ∈ V incluso si o₁ = o₂, por el convenio de primera copia: definirlo
como «v > o₂» dejaría fuera el empate.)

y v* := mín V. Nótese que o₂, o₃, m, σ₁, σ₂ son piezas **ajenas** al
subárbol de v*: o₂ y o₃ son ocupantes de nivel superior; m está en el
agujero de y (según P) o en la sartén (según F), y y no está en el
subárbol de o₁; y el par lo coloca P en la sartén. No hay doble conteo.

- **[C1]** La cola de v* contiene o₂, o₃, m = 1, σ₁, σ₂ y todo T_{v*}.
  Con (Bo) en v* (legítima: el agujero de v* no es el de y, y σ₁ ≤ 1), T_{v*} ≥
  X_{v*} > v* − s. Con o₃ > 1, S₀ > 1 y ρ ≤ φ:

      o₂ + 3 + (v* − s)  <  φ·v*      ⟹   o₂ < (φ−1)v* − 3 + s

- **[C2]** Con o₂ ≥ 3/φ y la identidad `3/φ + 3 = 3φ`:

      v*  >  φ(3φ − s)

- **[C3]** v* tiene un hijo-nodo. Si no, X_{v*} sería polvo puro < φ−1 y
  (Bo) daría v* < s + φ−1, incompatible con [C2] mientras
  s ≤ (2φ+4)/φ² = 2.7639. Sea w ese hijo; por minimalidad de v*,
  w ≤ o₂, luego X_{v*} ≤ w + (polvo del nivel) < o₂ + (φ−1) y (Bo) da

      o₂  >  v* − s − (φ−1)

- **[C4]** [C1] y [C3] juntas, usando `1/(2−φ) = φ²`:

      v*(2−φ) < 2s + φ − 4      ⟹   v* < φ²(2s + φ − 4)

[C2] y [C4] son incompatibles exactamente cuando

    φ(3φ − s) ≥ φ²(2s + φ − 4)  ⟺  6φ − 1 ≥ s(2φ + 1)
                                ⟺  s ≤ (6φ−1)/(2φ+1) = 11 − 4√5

y s = σ₂ + ω < 2 < 11 − 4√5. Contradicción. ∎

En el peor caso admisible s → 2 las dos cotas son exactamente
`φ+3 = 4.618…` (inferior) y `φ³ = 2φ+1 = 4.236…` (superior): el margen es
`φ + 3 − φ³ = 2 − φ = 0.382`, no marginal.

## 3. Por qué no prueba de más

- **No contradice el contraejemplo áureo** (`thm:golden`): aquella familia
  vive en j = 1 (el propio paper la sitúa «inside case (i)»), y esta
  cadena necesita tres ocupantes — o₂ y o₃ en las colas, y la tercera hoja
  estricta en (b). Además concluye ρ > φ, y la familia áurea tiene
  ρ = φ+3ε > φ: compatible.
- **La rama o₂ < 3/φ no la toca** (se cierra aparte, por la cola de o₂),
  y [C2] la necesita: con o₂ → 1 la cota inferior cae por debajo de [C4]
  (control negativo del bloque D).
- **La constante es ajustada**: para s > 11−4√5 la cadena NO cierra
  (control negativo). O sea, si el pivote fuese sólido con ω grande
  (σ₂+ω > 2.0557) este argumento no bastaría — coherente con que el
  régimen ω ≥ 1 esté abierto salvo donde se declara.

## 4. Qué queda abierto después

La micro-celda era lo único que faltaba de **j = 3**; el Teorema DP pasa a
ser total para perfiles de pares. Siguen abiertos, y no dependían de
ella: perfiles |S| ≥ 3, anillos pequeños extra, y el ensamblaje del lema
universal de reinserción con umbral φ. La Conjetura áurea sigue siendo
conjetura: exige *todos* los perfiles, no solo los de pares.
