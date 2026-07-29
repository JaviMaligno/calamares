# Acta de verificación adversaria de los borradores

Cada borrador de este directorio fue producido por un agente investigador y sometido
a un verificador adversario independiente que rehízo el álgebra con sympy sin mirar
la derivación, ejecutó los scripts y buscó contraejemplos dirigidos. Resumen:

## grosor_positivo.md + code/grosor.py — TODO CONFIRMADO (8/8 claims)

El verificador rederivó Φ′, la concavidad, la cúbica del cruce y la esquina racional
13/7, y coinciden al completo. La única premisa no demostrada (H1: κ ≥ 1 en la
frontera del trío) está declarada y aguantó una malla más amplia que la original.
Matiz añadido por el verificador: la dominancia de la rama σ₁+σ₂ sobre (1+σ₁+σ₂)/α
no estaba explicitada en el borrador, pero es cierta (verificada en 5 puntos).

## perfil_tres.md + code/tresk.py — CONFIRMADO con un sub-claim refutado

Proposición 4, Corolario 3 (fórmula de ρ*₃) y Corolario 4 (cruce exacto ω_T = 1/T − 1/2)
sobreviven a rederivación independiente, oráculo computacional escrito desde cero y
~6.5M de muestras sin contraejemplo. REFUTADO un detalle lateral, YA CORREGIDO en
`perfil_tres.md` §4: el perfil {0.645, 0.585, 0.585} citado como "punto crítico" ni
siquiera está bloqueado (s₃ ≤ s₁ − ω: se reinserta anidando, ρ_needed = 1.815); una
segunda pasada del investigador lo verificó por ejecución directa y reemplazó la
frase. El error no afectaba a la fórmula ni a los corolarios. Huecos declarados: exactitud de feas3 solo
para el caso (ii) con ω > 1/2; ρ*₄ abierto (evidencia de ρ*₄ = ρ*₃).

## cuadrado.md + code/cuadrado.py — CONFIRMADO con UN HUECO NO DECLARADO

Toda el álgebra exacta (cuártica de X, t*, identidad b_□(X) = X − 1, polinomios de la
escalera) rederivada por resultantes y coincide sin excepción. HUECO no declarado
detectado por el verificador: el claim «min_α b_□(α) = b_□(√2) = 1/√2 ⟹ ρ > √2
universal» está marcado "demostrado" pero solo vale para α ≥ 1; para α < 1 falta
argumento. Tratar esa cota universal como demostrada-solo-si-α ≥ 1. Nota menor: el
peldaño 2 del disco en reinsercion.md §9 (≈1.79966) difiere ligeramente del cruce
exacto de las ramas; revisar la cifra al consolidar.

## suelo_rigido.md + code/rigido.py — TODO CONFIRMADO (10/10 claims)

Teorema S: toda instancia de la subfamilia rígida F (R = r₁+r₂, pareja en el
agujero, trío infactible) cumple ρ > T estrictamente, para todo w > 0, sin
idealización tangente; el ínfimo es exactamente T y no se alcanza (Prop. S6). El
verificador rehízo las 13 identidades algebraicas en sympy antes de leer las
derivaciones, atacó los pasos delicados (rama 2π−Δ del Lema S2, equivalencia por
senos de S3, concavidad hasta (1+√13)/6 en S4) y ejecutó los 7 bloques de
rigido.py; su búsqueda adversaria con semillas propias llegó a ρ = 1.839564 dentro
de F sin bajar de T. Piezas nuevas: identidad sin²(θ/2) = f(a)f(b), reducción a
ψ(u)+ψ(v) ≥ τ, la configuración rígida emerge como extremo (no se supone), y el
bolsillo antipodal solo NO basta (óptimo relajado ρ = 1.73 con trío factible).
Matices declarados por el autor: cierre por compacidad de S6 esbozado (afecta solo
a la dirección ≤ del ínfimo) y escala √δ del umbral fuera de la esquina (numérica).
