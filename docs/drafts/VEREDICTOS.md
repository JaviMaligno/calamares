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

## h1.md + code/h1.py — TODO CONFIRMADO (6/6 claims), con mejoras del verificador integradas

H1 (κ = −∂h/∂σ₁ ≥ 1 en la frontera de bloqueo del trío) queda demostrado. El
verificador rederivó la identidad κ = √(g(σ₂)/g(σ₁)) desde cero por una ruta
distinta (reducción a t = √((1−s)/s) en vez de λ·tan), la validó en aritmética
racional EXACTA (30/30 puntos, α ∈ [9/7, 24999.5]; la factorización simbólica
muestra que el factor que anula κ² − g/g es exactamente la ecuación de frontera),
en mpmath dps=50 contra diferencias finitas (err ≤ 1.25·10⁻²⁹, α hasta 10⁶) y en
mallas adversarias de ~10M de puntos (α hasta 10¹⁵) sin contraejemplo. Cero
refutaciones. Hallazgos del verificador, INTEGRADOS en la revisión de h1.md:
(1) forma cerrada de la frontera t(σ₁) + t(σ₂) = t(b(α)) — h explícita; (2) la
hipótesis α ≥ α₀ del borrador era un artefacto de coordenadas: κ ≥ 1 vale para
todo α > 1 (en el caso restante κ² > 6); (3) el cierre áureo (φ) era subóptimo:
con 1 + b(α) ≥ α el cierre llega exactamente a T (Tribonacci), coherente con la
Proposición 3. Menores corregidos: no-op en h1.py (filtro muerto), cifra de la
tasa Θ(√d) (~2·10⁻⁴, no 3·10⁻⁴), «alcanzado EN σ₁ = 1» (conjunto cerrado), (W)
definida en el texto. Las piezas nuevas del verificador quedaron re-verificadas
en simbólico en h1.py A8–A14 y en malla (C2, C4, E1–E2); 5/5 bloques.
Consecuencia: los «módulo H1» de grosor_positivo.md, resultados.md §9,
reinsercion.md §10 y hoja_de_ruta.md quedan retirados.

## esquina.md + code/esquina.py — TODO CONFIRMADO (6/6 claims), 1 error numérico corregido

Curva exacta del grosor y Teorema de la esquina (inf T_can = 13/7). El verificador
rederivó el mínimo condicionado desde cero y reconstruyó la curva con dos motores
independientes (frontera cerrada y criterio angular puro): coincidencia en 22+14
valores de ω (≤ 3·10⁻¹² y ≤ 4·10⁻⁴ unilateral). P(α,ω) rederivado por doble
cuadratura (cociente exacto −1); añadió la IRREDUCIBILIDAD de P sobre ℚ[α,ω] (y
ℚ(ω)[α]), la identidad de juntura P(2−ω,ω) = (ω−1)³·cúbica, y la parametrización
x = t(α−1) que hace transparente el alcance de la rama mixta (x ≥ 0 ⟺ ω ≤ 1/7).
Ataques: 30 000 valores de ω, ~4·10⁶ muestras con 206 866 bloqueos genuinos
(mínimo 1.860387 > 13/7), extremos ω ∈ [10⁻⁹, 0.9], σ₁ = 1−10⁻¹²: cero
violaciones. Estructura fina confirmada en exacto: V′(ω₁⁺) = +0.07213803 (signos
por polinomio mínimo módulo la cúbica), resultante = −2¹⁸(ω−1)¹⁰R₈, ω_peak único
(máximo, 2ª diferencia < 0), bump +1.10473·10⁻⁴; la monotonía de grosor_positivo
§4 es efectivamente FALSA y quedó corregida allí. REFUTADO un dato lateral, YA
CORREGIDO: α_peak es 1.9618665, no 1.9614700 (§6; ahora se verifica en D1d).
Precisiones incorporadas: exclusión α > 2+ω estricta (en α = 2+ω hay un candidato
con S = 2), caso (c) en (2, 2+ω), el descarte completo de α < T₍₁₊ω₎ en el tramo
del testigo, unicidad de la esquina explícita, alcance ω > 0.30 de la cota
inferior, y la salvedad de C6 (la genuinidad usa cualquier ε ≤ δ₀ del Lema S6a(3),
existencial; la elección numérica δ²/4 se valida aparte). La separación de estatus
de §7 (demostrado / módulo criterio angular en la cota superior de H_m y mixta)
fue auditada y es honesta. 5/5 bloques.

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
