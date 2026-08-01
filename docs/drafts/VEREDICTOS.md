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
inferior, y la salvedad de C6 (la genuinidad usa cualquier ε < δ₀ del Lema S6a(3),
existencial; la elección numérica δ²/4 se valida aparte). La separación de estatus
de §7 (demostrado / módulo criterio angular en la cota superior de H_m y mixta)
fue auditada y es honesta. 5/5 bloques.

## cuatro.md + code/cuatrok.py — PROPOSICIÓN CONFIRMADA, PRUEBA DEL COROLARIO REFUTADA Y REPARADA

ρ*₄ = ρ*₃ (Proposición 8) CONFIRMADO: oráculo independiente (calibrado contra la
Prop. 4 de perfil_tres con 0 desacuerdos en 16 800 perfiles y contra
reinserta.accepts en 11 200), malla exhaustiva de ~900 000 candidatos y búsqueda
dirigida con descenso: el mínimo sobre bloqueados coincide con ρ*₃ por arriba a
+3·10⁻⁷…+1·10⁻⁶ en 13 valores de ω, y el árbol A/B1/B2/B3 fue auditado rama a
rama (12 000 muestras × 4 ramas × 11 ω, cero violaciones; B2 es la única rama que
muerde; el certificado de B3 verificado en positivo con 340 000 perfiles).
REFUTADA la prueba del Corolario 5 tal como estaba: el cierre de k ≥ 5 invocaba
el Corolario 2 de reinsercion.md, que SOLO cubre perfiles con todos los aros en
banda — y como ρ*_{k+1} ≤ ρ*_k (polvo), k ≥ 5 podía en principio bajar el umbral.
El verificador aportó el parche, INTEGRADO como prueba principal en cuatro.md §2:
un árbol general que demuestra ρ*_k = ρ*₃ para TODO k ≥ 3 (p := #{i: s_i > s₁−ω}
≤ 3; p ≥ 3 bloquea el prefijo; p = 2 reproduce el caso (iv); p = 1 fuerza ρ ≥ 2),
con lo que el Corolario 5 (ω_c = ω_T exacto) queda demostrado y uniforme en k.
Otros arreglos: el oráculo de cuatrok.py es conservador (no «generoso») en grupos
de ≥ 4 hermanos — el sesgo correcto para [B], con la justificación reescrita — y
las familias de [D] no dependen de él (confirmado con oráculo permisivo
independiente); el bloque [C] tenía punto ciego en las ramas de contradicción
(ahora clasifica por geometría y las ejercita); aside de I₃ corregido (1/(1−ω)
para ω > 1−1/φ); el testigo con ρ = 2/(1+2ω) solo vale hasta (√5−2)/2; añadido
ω_T = T²−T−3/2 módulo la cúbica (A4b) y el mínimo de p=1 (A4c); barrido k = 5, 6
añadido ([E]). DE PROPINA auditó el Lema S6a: argumento correcto, con UN error de
extremo real, YA CORREGIDO en los tres sitios: el intervalo de propagación es
δ ∈ [0, δ₀) — en δ = δ₀ se tiene u = u_máx, que empaqueta — no (0, δ₀]; y
«δ₀ explícito» rebajado a «extremo óptimo determinado» (u_máx es un máximo, no
una fórmula). 5/5 bloques.

## universal.md + code/universal.py — NÚCLEO CONFIRMADO, ENUNCIADO DEL LEMA REFUTADO Y REPARADO

Frontera universal del trío en disco R arbitrario. El verificador rederivó la
factorización desde cero (exacta, 40/40 casos racionales) y confirmó T_c, τ_R, el
bolsillo b_R(A) (también por geometría directa de tangencias, residuo 6.2·10⁻¹¹),
κ = √(g_c/g_c) (contra diferencias finitas a 40 dígitos: 8.5·10⁻⁴⁰) y el Corolario
U1 (Teorema S con holgura): leyó la prueba del Teorema S con lupa sin hallar usos
ocultos de R = r₁+r₂, verificó la monotonía en R (500 000 casos) y barrió 2·10⁶
sorteos de la familia con holgura: ρ_min = 1.8553 > T, cero contraejemplos.
REFUTADO el ENUNCIADO del Lema U tal como estaba: la equivalencia ⟸ es FALSA sin
la hipótesis A ≥ mín(x,y) (contraejemplo R = 1, A = 0.01, x = y = 0.45: la forma
lineal predice bloqueo y el trío empaqueta con F = 2.28 << 2π; caracterización
exacta: falla exactamente en la región s ≤ w). La existencia de la frontera venía
gratis de la banda en h1.md y se soltó al generalizar; h1 y suelo_rigido quedan a
salvo (allí A es el máximo), y el Corolario U1 también (solo usa la dirección ⟹,
incondicional). YA REPARADO: hipótesis añadida al enunciado, prueba reescrita
(sin s ≤ sin w y s > w desde la hipótesis), contraejemplo citado. Más hallazgos
del verificador, INTEGRADOS: la G_c-IDENTIDAD G_c = (c²/4)U′² (κ ≥ 1 de h1 y la
concavidad de S4(3) son el mismo hecho en dos coordenadas — la «coincidencia» de
(1+√13)/6 es una identidad); el umbral AFILADO del κ ≥ 1 en R general
(τ_R ≤ 2/√3 ⟺ 3c² ≤ 4AR; justo encima κ_min = 0.9785, fuera de la hipótesis);
la cota de existencia del bloqueo R < (1+2/√3)A = 2.1547A (que sustituye al
«aviso de la rama del par», vacío bajo la hipótesis: x+y < R sale gratis), con
margen κ² ≥ 2.442 en la banda de uso; y b_R(A) ≤ A. Errores menores corregidos:
la cola dominante de la exploración [E] es la de γ en 321/321 (no la de α); (F2)
estricta en D2; test INVERSO añadido al bloque B (el original solo comprobaba ⟹
y era ciego a la refutación: 55/2991 fallos en su propia malla fuera de la
hipótesis). 5/5 bloques tras las correcciones.

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

## corona.md + code/corona.py — TODO CONFIRMADO (C1–C7 + contraejemplos), con mejoras del verificador integradas

Criterio de coronas (paso 1 de la Batalla 1). El verificador rederivó a ciegas
(Fase 1, sin mirar los ficheros) el sistema de huecos, el contraejemplo al
enunciado ingenuo del plan, el criterio exacto k=4, el orden zigzag, el patrón
del pentagrama en k=5 y el contraejemplo del cuantificador — coincidencia total
con el borrador antes de leerlo. En Fase 2 auditó las pruebas línea a línea
(C4: ciclos simples bastan, conteo #aristas > 2U, enumeración U=1 reproducida;
C6: mayorización y anchuras verificadas, g′ rederivada a mano) y ejecutó
baterías propias: 4 000 aleatorias + 2 344 comparaciones en frontera (bisección
a slack ≈ 0) + 3 000 con radios hasta 0.9 + 622 con a₁+a₂ = R exacto (θ = π):
0 discrepancias; sanity clásico x = √2−1 para 4 iguales clavado a 3.6e−15; en
frontera el trío activa 652 veces y el zigzag 520 (ninguna condición
redundante); oráculo EUCLÍDEO propio (sin S1) concordante. NINGÚN CLAIM
REFUTADO. Errores menores corregidos: dos constantes del §3 (2·arcsin(9/11) =
1.9165, no 1.914; 3θ(0.47,0.47) = 6.5421, no 6.456), la redacción del censo
U=2 omitía los 10 patrones de 3 aristas (30 por conteo + 10 por LP + 1
pentagrama), y el «máximo geométrico 7.311» del pentagrama era un mínimo local
de una búsqueda capada a radios < R/2 — el récord real del verificador es
Σ_D = 7.5560 estricto (frontera 7.5742, con un radio > R/2), aún lejísimos del
4π necesario. Hallazgos del verificador INTEGRADOS: **Corolario C5′** (el trío
top domina a los otros tres: el Lema U₄ son DOS desigualdades), **Teorema C7**
(k=5 exacto para θ arbitrarias: subconjuntos + pentagrama ⟺ LP, contrastado en
30 000 matrices), la Conjetura C8 reformulada como redundancia geométrica del
pentagrama, prueba constructiva alternativa de C4, contraejemplo global k=5
propio con margen −0.099, y la dirección de polígonos estrella {m/q} para el
censo k ≥ 6. Sesgo de muestreo del código corregido (radios > R/2 y pares
tangentes ahora cubiertos). 5/5 bloques tras las correcciones.
