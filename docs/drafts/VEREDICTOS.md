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

## ocupantes.md + code/ocupantes.py — TODO CONFIRMADO (V1–V4), con cota fina del verificador integrada

El precio del ocupante (pasos 2 y 4 de la Batalla 1 en la plantilla libre). El
verificador rederivó a ciegas las seis paredes y el argumento de cola y llegó
EXACTAMENTE al mismo resultado antes de leer el borrador, incluida la pared
nueva (Bo) de los agujeros de los ocupantes. Auditó la legalidad de cada
colocación desbloqueante contra el marco de reinsercion.md §2 (D_m, recursos
disjuntos, solo se mueven aros menores que m), los empates (o₁ = 1 = m
exactos), la partición de monotonía y las identidades (todas reproducidas en
sympy independiente: 8/13, ω₄ = 3/T−1 = 3T²−3T−4, la identidad del 2 que da
Φ < 2 para todo ω, la esquina genuina como ancla de la comparación V4).
Ejecutó ocupantes.py (5/5 a la primera) y atacó con SLSQP multi-arranque y
barridos de 60k por ω sin hallar ningún bloqueo bajo la cota (~10⁶ instancias).
NINGÚN CLAIM REFUTADO. Hallazgos del verificador INTEGRADOS: (1) **cota fina**
en la rama j = 1, ω ≥ 1/2 — usando además la pared (D), ρ > 4/(1+2ω), ínfimo
exacto del programa de paredes (alcanzado en σ₁ = σ₂ → 1/2, o₁ → 1/2+ω), que
extiende ρ > T hasta ω₅ = 2/T − 1/2 = 2T²−2T−5/2 = 0.587378 y ρ ≥ 13/7 hasta
15/26; (2) caracterización de exactitud: (j+2)/(1+ω) es el ínfimo exacto del
programa de paredes sii ω ≥ 1/(j+1), y si no la cola de o₂ fuerza ≥ j+1 (esto
explica los excesos del bloque [E]); (3) σ₁ < 1 estricto en todo bloqueo (por
(B4)+(W)); (4) evidencia de cierre del hueco de ω grande: en ω ∈ [0.5, 0.63]
las 2000 instancias bloqueadas-por-paredes de menor ρ admiten TODAS corona en
R̄ = α+o₁ (estaban desbloqueadas de verdad): la pared geométrica sube el ínfimo
real muy por encima de la combinatoria. Matices de código corregidos: el
muestreo de [B] no llegaba a ω < 0.25 (ahora condicionado, 324 instancias con
ω < 0.20), test cuasi-tautológico de [B](i) re-etiquetado como consistencia,
código muerto de [D] convertido en la aserción real de la cadena de V4, y el
check trivial de [C] re-etiquetado como medición. 5/5 tras las correcciones.

## bloqueadores.md + code/bloqueadores.py — NÚCLEO CONFIRMADO, §5 REFUTADO Y REESCRITO

Agujeros ocupados a profundidad arbitraria (paso 3a de la Batalla 1). El
verificador rederivó a ciegas TODO el núcleo antes de leer el borrador — disco
opuesto, tarifa del bloqueo, nodo mínimo, dos colas, Ψ(ω) = (1−ω)+√((1−ω)²+1),
cruce en (T−1)²/2 — coincidencia exacta. Confirmados: Lema R (tangencia exacta
del disco opuesto; σ ≤ c hipotetizado y automático en las aplicaciones), pared
Bo″ (el caso «un hijo supera σ₂» reduce literalmente a la misma desigualdad;
legalidad de recolocación correcta: solo σ₂ cambia de contenedor), Teorema B
(optimización verificada; y* ≥ 1 sin pérdida; empates bien) y Corolario B1
(identidades reproducidas en sympy independiente). REFUTADA la §5 antigua («la
fuga»): la familia con H_m relleno que "demostraba" que la hipótesis m-sin-hijos
era necesaria NI SIQUIERA ESTABA BLOQUEADA — la desbloquea la propia evacuación
(σ₁ + hijos de m en fila en D_m, σ₂ en el H_m vaciado), y para δ ≥ (1−2ω)/2
además cae la pared (D); y la dicotomía enunciada olvidaba colocar a σ₁: la
correcta es bloqueo ⟹ σ₂ > 1−ω ∨ σ₁ + Σhijos(m) > 1 (contraejemplo del
verificador a la versión sin σ₁: ω = 0.1, σ = (0.9, 0.81), hijo de m 0.85,
o₁ = 1 con hijo 0.81, α = 1.81, bloqueado con ρ = 4.37 — sin amenaza para el
Teorema B). Con ello cae el único overclaim del borrador («m sin hijos se queda
por una razón demostrable»): la evidencia adversaria apunta a lo CONTRARIO —
en búsquedas amplias con H_m ocupado (hasta 6 hijos, Σ > capacidad incluida,
evacuaciones exhaustivas) el mínimo quedó en 2.44–2.96, siempre ≥ Ψ, y el
verificador conjetura que el Teorema B se extiende a m-con-hijos por
combinatoria pura. TODO INTEGRADO: §5 reescrita (evacuación corregida +
conjetura), matiz de notación del paso 3 (σ = σ₂ variable, no 1−ω fija — la
lectura literal antigua habría invalidado el paso), nota de degeneración en
ω = 0 de la minimalidad, Ψ < 3/(1+ω) afilada a estricta global (5ω²−2ω+2 > 0,
disc −36), cota fina vía (B4)+cola de α anotada (≈ Ψ+0.05, explica las
holguras de [D]), y el bloque [E] sustituido por la validación constructiva de
la evacuación (20 000 casos, 0 fallos). 5/5 tras las correcciones.

**Segunda ronda (Teorema B″, m con hijos): CONFIRMADO.** La conjetura del
verificador quedó demostrada y él mismo la auditó: rama A correcta (H_m solo
entra por (B2); D_m íntegro porque m viaja con sus hijos), rama B correcta (el
paso de doble sustitución (1+A)/y* > (2+s)/(s+ω) es sano — numerador y
denominador no comparten variable —, el cruce s²+sω = 2−ω cae estrictamente
dentro de la región, estrictos bien), dominancia Ψ_B ≥ Ψ correcta (raíz
metálica creciente en b, igualdad solo en ω = 0), Corolario B2 cotejado contra
las fuentes (la curva T_can solo usa σ₂ > 1−ω; la Proposición 4 no usa (B2) ni
(B4)). Su ataque ampliado (200k configs × 6 ω, adversario con agujeros de σ₁,
σ₂ y de los hijos de m rellenables, empaquetados h > 1−ω, evacuaciones a 6
destinos) no encontró nada bajo Ψ_B (mínimos 2.34–2.69). Correcciones
integradas: la definición de nodo debe excluir explícitamente a m (sin ello
y* = m rompería el paso 3 de B y duplicaría masa en B″ — matiz que afecta a
ambos teoremas, arreglado); errata decimal (T−1)² = 0.70440226 (no 0.7044045);
el hallazgo de que (T−1)²·T − (2T−T²+1) ES el polinomio de Tribonacci
(identidad exacta, no solo resto 0); «Φ > T ∀ω» precisado a ω > 0; mapa
actualizado a 6/6 y tautología del check 2·ω₆ eliminada. 6/6 tras las
correcciones.

## bolsillo.md + code/bolsillo.py — TODO CONFIRMADO (asalto geométrico), con la disyunción de bolsillos demostrada por el verificador

La pared del bolsillo doble y el cierre en ω (j = 1 hasta 0.9505). El
verificador rederivó a ciegas TODO: la pared σ₁ > b₂(α,o₁) vía contención en
R̄ y S5 reescalada, la cuadrática N²+(1+σ₁)N−σ₁(1+σ₁)² = 0, el rincón dorado
(α = 2, o₁ = √5−1, X = √5−2, b₂(2,√5−1) = 1) con la curva φ²−(φ/2)ω y el
cruce 0.962585, Ψ_j con sus umbrales, y la limitación del Lema G frente a
pequeños — coincidencia total, y su SLSQP independiente reproduce la curva a
<10⁻⁴. NINGÚN CLAIM REFUTADO. Aportaciones del verificador INTEGRADAS:
(1) la disyunción de los dos bolsillos espejo, que el borrador solo asertaba,
DEMOSTRADA con la identidad exacta y₀² − b₂² = 3b₂² (y₀ = 2b₂: los círculos
espejo distan 4b₂), ahora en el lema y verificada en simbólico con las
tangencias; (2) hueco de demostración REAL en Ψ_j: si algún hijo del mayor
ocupante es un nodo ≥ 1, la prueba escrita no aplica (la cola de m solo
recoge hijos < 1) — el enunciado sobrevivió a sus ataques dirigidos (los
nodos anidados se autodestruyen: mínimos 2.732 vs Ψ₂ = 2.000) y queda
declarado como caso con parche pendiente (asteriscos en la tabla §7);
(3) matiz de alcance del Corolario S ("compatible con la plantilla de cada
teorema": un pequeño en el agujero de un o_i manda la instancia de V2 a B″);
(4) forma alternativa ω_A = 2(φ²−T)(φ−1) vía φ³ = 2φ+1; (5) la puntita
[0.9505, 0.9626) parece cerrable: su numérica indica que la rama B exacta
nunca baja de la curva A (en ω = 0.98 el programa completo da 1.8252). Su
verificación de coherencia con los resultados previos: los mínimos 2.32-2.14
de bloqueadores.py [D] quedan BAJO la curva dorada ⟹ aquellas instancias con
paredes combinatorias en pie estaban realmente desbloqueadas por el
re-empaquetado (la geometría sube el suelo), y el proxy 2.5617 de
universal.py [E] queda sobre la curva (2.416 en su caja) ✓. Detalles de
código anotados (checks decorativos en [B]/[E], [D] de profundidad 1,
cola de α sin imponer α ≥ o₁ — inocuo). 5/5 tras las correcciones.

**Tercera ronda (Teorema G′, el remate de la rama B): ENUNCIADO SOBREVIVE,
PRUEBA REPARADA.** El verificador auditó su propia observación convertida en
teorema y cazó un error real: la cadena (II) — la cola de α — solo vale si
α ≥ o₁, hipótesis que la plantilla no da (¡los ocupantes pueden superar a α!);
como A_máx(3/2) = 3/2 exacto, para o₁ > 3/2 el caso α ≥ o₁ es VACÍO y la
«dominación trivial o₁ > 2» de la primera redacción hablaba de un conjunto
vacío mientras las instancias reales quedaban sin cubrir. Confirmó todo lo
demás con re-verificación independiente: cadenas y signos, B3′ en rama B, las
dos factorizaciones exactas, el caso o₁ ∈ (g, õ] (con la tangencia benigna
c₁₀′(g⁺) = φ — otra aparición áurea — y la autodualidad A_máx(g) = 2,
A_máx(2) = g), los certificados univariantes (sus mallas de 40 000 coinciden),
y las erratas õ = 1.29558 y los primeros eslabones «≥». REPARACIÓN integrada
(el enunciado ρ > T para ω < ω_A queda SIN asteriscos): el caso α < o₁ solo
existe para ω < 1/2 (N₁(1/2) = 3/2 exacto) y ahí (a) con hijos de o₁ menores
que m valen dos cotas α-libres — 1+o₁−ω por la cola de m, y
1+(2−ω+2b₂(1+ω,o₁))/o₁ por la cola de o₁ que ahora CONTIENE a α (Bo″+B3′+W
cancelan α) — cuyo máximo supera la curva dorada con margen +0.31 (certificado
del verificador, reproducido en [F]); (b) con hijo-nodo en o₁, la rama B da
ρ > Ψ_B(ω) > Ψ_B(1/2) = 2 > T exacto (la forma fuerte de la curva hereda ahí
el asterisco de recursión de Ψ_j; numéricamente ≥ 3.1). El modelo SLSQP de
min_programa tenía las dos colas sobre-restringidas justo en la región del
hueco (cola de α incondicional y cola de m con X entera): arreglado imponiendo
α ≥ o₁ (la sub-rama donde el modelo es válido) y cubriendo α < o₁ con el
parche. 6/6 tras las correcciones.

**Cuarta ronda (Lema de las hojas — Ψ_j sin asteriscos): CONFIRMADO,
PRUEBA REPARADA EN LA RAMA B.** Verificador independiente, protocolo de dos
fases; su rederivación a ciegas coincidió con §4 en existencia de las j
hojas (anidamiento estricto ⟹ bosque finito; subárboles disjuntos), hecho 1
(L nunca es α ni m: la definición de nodo ya los excluye), hecho 2 (empates
por primera copia; misma W en ambos lados legítima — en el denominador solo
debilita), la optimización de la rama A (cruce exacto en sympy, mínimo en
σ = 1−ω, W* > 0) y la dominancia de la rama B. Dos hallazgos integrados:
(1) el paso ESCRITO de la rama B contaba M dos veces (σ₁+M > 1 ya consume
M; contraejemplo del paso tal cual: σ₁ = 0.7, M = 0.5, σ₂ = 0.3, W = 0.9 da
cola garantizada 1.9 < 2.2 afirmado) — reparado con la variable
s = σ₂ + X_L (X_L y M disjuntos): sale la MISMA metálica u² − (2−ω)u − j,
el resultado no cambia; (2) la esquina del cruce en W < 0 (ω > 1/2, j = 1,
σ → 1), no discutida: allí 2σ satisface (2σ)² − 2(1−ω)(2σ) − j ≥ j > 0 ⟹
2σ > Ψ_j, sin fuga. Además exigió enunciar la cola de m como hecho 3
explícito de la rama A (el término 2σ+W lo necesita). Su ataque con árboles
reales (~3000 instancias legales + minimización dirigida sobre
torres-cadena, hojas verdaderas, Bo″ por nodo, ambas ramas, 24 casos): 0
violaciones, min ρ = 1.61–4.92 siempre ≥ Ψ_j con holgura ≥ 0.35, y el
adversario óptimo elige siempre torres de altura 1 — exactamente lo que el
lema afirma. Umbrales de la escalera exactos a 10⁻¹². Sobre el bloque [D]
de bolsillo.py: el proxy «j menores nodos» es condición necesaria del
bloqueo (conservador, correcto); limitación anotada: solo muestrea rama A
(su ataque cubrió rama B y j = 1 sin hallazgos). VEREDICTO: la Proposición
Ψ_j vale sin asteriscos para todo j y toda ocupación; correcciones
editoriales aplicadas a bolsillo.md §4 y al Apéndice D del paper.

## Acta: striple.md (Teorema T3 — S de tres piezas en la canónica)

**Veredicto: CONFIRMADO en todos los sub-claims; enunciado REFORZADO por el
verificador.** Protocolo de dos fases; la rederivación a ciegas coincidió en
colocaciones, paredes, incompatibilidades (corona de v ↮ D_m/evacuación), la
cadena del zigzag (rangos A, B < π/2; sentido de f(σ₁) ≤ 1/α; identidad
σ₂ > b(α)), la herencia de las 4 paredes en la Rama 1 y la tricotomía. Sus
ataques: oráculo independiente reescrito desde cero (0 discrepancias en 140k
configuraciones), 2M muestras del zigzag (0 violaciones; pared AJUSTADA,
margen mínimo 2.8·10⁻⁵ en σ₃ = σ₂, σ₁ → 1), barrido de bordes en 11 valores
de ω (~85k bloqueos en régimen fiel, 0 fallos de cadena, 0 violaciones de
ρ > Φ; mínimos por rama R1A ≥ 2.14, R1B ≥ 1.99, 2A ≥ 2.50, 2B ≥ 2.64).
Cuatro aportaciones integradas: (1) la pared **(BH)** «σ₁(σ₃) → D_m;
σ₂ + M fila en H_m» ⟹ σ₂ + M > 1 − ω, que en la rama 1B da
ρ > 1 + σ₁ ≥ 1 + Φ/2 ≥ 1 + T/2 = 1.9196 y ELIMINA la excepción de rama:
ρ > máx(Φ, 13/7) en TODAS las ramas; (2) el suelo de la rama 2B es exacto
y racional: el cruce de las dos cotas es γ = 2 en ω = 2/7 (identidad
8 = 4 + 2 + 2 en la cúbica de la deformación áurea) con valor **17/7** —
corrige el 2.4291 de rejilla (artefacto del paso i/200); (3) la línea
B1+W ⟹ σ₁+σ₂ ≥ 1+b(α) ≥ Φ añadida a la rama 1A (tal como estaba escrita
solo daba 13/7, insuficiente para ρ > Φ con ω > 1/7); (4) artefacto del
oráculo en M > 1−ω (capH < 0 rechazaba asignaciones que ni tocaban H_m;
contraejemplo concreto con M = 1.036) — la prueba era válida ahí, era
hueco de cobertura del código; arreglado (H_m solo restringe si se usa) y
la rama 1B ejercitada en [C] con M > 0. Estrictitud menor anotada e
integrada: el > estricto de la rama 1B usa σ₃ > ω. 5/5 bloques en verde
tras las correcciones.

## Acta: umbral_aureo.md (Teorema A1 — contraejemplo a la conjetura de T)

**Veredicto: CONFIRMADO — la conjetura del umbral de Tribonacci queda
refutada.** Verificación con mandato explícito de DESTRUIR el
contraejemplo, por siete vías; resistió todas. El verificador: (1)
rederivó en simbólico desde cero el bolsillo por curvaturas de Descartes
(k₀k₁+k₁k₂+k₂k₀ = 0 ⟹ b₂ = AB(A+B)/(A²+AB+B²)), b₂(φ,1) = φ/2,
(1+φ)/φ = φ, la factorización de la necesidad S5 y el punto fijo
2b(A)·A = 1+2b(A) con única raíz positiva A = φ; (2) optimización
numérica propia SIN asumir rigidez (3 centros libres, multistart):
v_máx = φ/2 a 1.8e−13, v = φ/2+10⁻³ infactible; (3) contraste con el
solver físico del repo (`sim.pack_feasible`, independiente): {φ,1,s} NO
empaqueta en R = φ+1, {φ,s,s} SÍ, {s,s} NO cabe en el agujero de φ —
también con radios estrictos; (4) semántica del modelo auditada contra
paper y código: tangencias legales (par sum ≤ R, como en n=4 y gemelas),
regla del agujero r ≤ r'−w, worst fit = capacidad estática máxima ⟹
elige la sartén, obliviousness = TODAS las reglas (basta una ejecución
legal que falle); (5) el árbol exhaustivo de aureo.py [B] auditado: la
única rama de bolsillo que decide es la rígida exacta, la rama corona
(suficiente-solo) nunca bloquea en el subárbol m→sartén, best[True]=3
acota toda regla; (6) ρ recalculada en simbólico y la Conjecture
contradicha LITERALMENTE tal como está en paper/main.tex:479 y
resultados.md §5quater. Hallazgos integrados: radios ESTRICTOS
{φ, 1, φ/2+2ε, φ/2+ε} (ρ = φ+3ε) para respetar la convención r₁ > … >
r_n del paper; assert en la rama bolsillo de pan_ok; Conjetura A2
reformulada directamente sobre obliviousness; el modelo del paper debe
decir «interiores disjuntos» (la lectura literal «pairwise-disjoint»
mataría también n=4 y las gemelas); el teorema exacto vive en δ = 0
(tangencia diametral, codimensión 1) con ventanas abiertas en ω y ε, y
la robustez δ < δ* = 0.0248 es evidencia angular. T queda
recaracterizado: suelo del intercambio anidado (Batalla 1 intacta), no
umbral global. aureo.py 5/5 tras las correcciones.

## Acta: batalla2.md (Teorema P — el suelo áureo de la Batalla 2, S par)

**Veredicto: CONFIRMADO en todos los sub-claims matemáticos; rincón
correctamente declarado NO DECIDIDO; un bug del aparato numérico hallado y
corregido.** Dos fases. Fase 1 (a ciegas): rederivación idéntica de las
cinco paredes con el punto crítico de la legalidad de (G) resuelto (D_m
viaja dentro del ocupante que el re-empaquetado mueve: las posiciones son
existenciales por contenedor, sin incompatibilidad corona↮D_m porque los
recursos viven en contenedores distintos); el caso j = 1 con dos
aportaciones exactas: el numerador de g′ es −(3A⁴+6A³+3A²+2A+1) y el
cruce 2b = g factoriza como (A²−A−1)(2A+1) = 0 — raíz positiva única φ;
la hoja estricta (agujero ≠ agujero de y) identificada como exactamente lo
que evita el doble conteo de m; Ψ_B(1) = φ, Ψ₁(1/2) = φ, Ψ₂(φ/2) = φ,
Ψ₃(1) = √3 verificadas en sympy; el Lema Z rederivado SIN U₄ (identidad
sin²(θ/2) = ab/((R−a)(R−b))) con la observación de que la admisibilidad de
θ(o₁,1) ES el par de F, y contrastado con un LP exacto de coronas propio:
0 violaciones en 35 000 tests. Fase 2 (ataques, ~1.25M iteraciones con
generador propio de profundidad 4): 0 violaciones de φ y de cadenas;
campaña reveladora: sin la pared (G) el mínimo j = 2 cae a 1.6555 con
instancias que violan o₂ < 1+1/o₁ — el Lema Z es exactamente la pared que
las mata. HALLAZGO (código): corona_ok con k ≥ 5 devolvía True, que en el
generador DESCARTA candidatos (no conservador): la evidencia j = 3 del
bloque [D] era vacía (n = 0 enmascarado por «n == 0 or»). Corregido
(k ≥ 5 → no imponer (G); n > 0 exigido): j = 3 puebla con n ≈ 12–13k y
mín ρ ≥ 2.24. Matices integrados: la rama B es vacía para ω ≥ 1/2 bajo
S ⊂ (ω,1) (Ψ_B(1) = φ es cierre estético; margen real ≥ 2−φ en la región
poblada); márgenes del rincón actualizados (φ+0.41 / φ+0.62); nota
cosmética en §2. 5/5 tras las correcciones.

## Acta (2ª ronda): batalla2.md — el cierre del rincón y la corrección σ>ω

**Delta verificado: W₂ y j = 2 CONFIRMADOS; árbol j = 3 con resultado
confirmado y dos pasos escritos REFUTADOS y reparados; y una CORRECCIÓN DE
PLANTILLA descubierta al integrar.** (1) Pared W₂ (bolsillos espejo):
el SII del cuarteto en o₁+o₂ confirmado (rigidez del par por sus propias
restricciones; necesidad S5 por círculo válida para ambos a la vez;
suficiencia por colocación espejo con y₀ = 2b₂ resuelto en sympy y 4 000
muestras geométricas); cruce áureo o₂* = √(1+2o₁)−1 con o₂*(3/2) = 1,
b₂(o₁,o₂*) < 1 en (3/2,2) e igualdad exacta en o₁ = 2; mín-máx numérico
1.618312 con argmin el rincón dorado (2, 1.236): ínfimo φ, nunca
alcanzado. Nit integrado: Ā < 1+1/o₁ solo para o₁ ≥ el número plástico
(certificado (o₁³−o₁−1)/(o₁⁴+o₁³+2o₁²+2o₁+1)). (2) Árbol j = 3: casos
1, 2 y polvo confirmados; Slip A («cola de m ≥ s+X₁» ilegal con nodos en
X₁; contraejemplo con paredes en pie) reparado enrutando y = o₁ por la
dicotomía nodo→jj=3/polvo→cola-de-m; Slip B («nodo z ⟹ tercera hoja
estricta» falso con hijo-nodo único; contraejemplo jj = 2) reparado con
Ψ₂ (ω < φ/2) y ρ > 2ω (ω ≥ φ/2, σ₂ > ω). (3) CORRECCIÓN: la premisa
«S ⊂ (ω,1)» que la reparación y una nota usaban NO es una necesidad del
modelo (los discos sólidos r ≤ w son piezas legales, y las familias de
polvo del repo los usan): rastro corregido en striple.md (el refuerzo
13/7-en-1B de T3 queda condicionado a σ₃ > ω; carve-out {rama 1B,
σ₃ ≤ ω} con cota Φ(ω) > T restaurado) y en batalla2.md (nota de rama B
reformulada; la sub-celda {j = 3, rama A, y hoja, ω ≥ φ/2, σ₂ ≤ ω,
o₁ ≥ 3, o₂ ≥ 3/φ} queda DECLARADA con el argumento de la torre esbozado
— tricotomía por niveles: polvo total > φ−1 ⟹ cola de m; dos hijos-nodo
⟹ jj = 3; torre de nodo único ⟹ suma cuadrática en la cola de o₁,
mín ≈ 1.93 — y la evidencia del verificador: 240 000 muestras dirigidas
con y sin σ > ω, mín ρ = 2.37, 0 violaciones). Teorema P: j = 1 y j = 2
completos toda ω; j ≥ 4 completo; j = 3 completo salvo la sub-celda
declarada. batalla2.py 6/6 tras las correcciones.

## Acta (2026-08-04): microcelda.md — cierre de la micro-celda de j = 3 (pinza sobre v*)

**Veredicto: CONFIRMADO. La sub-celda declarada en el acta anterior queda
CERRADA; el Teorema P pasa a ser TOTAL para perfiles de pares.** Objeto:
el Teorema M de `drafts/microcelda.md` (`microcelda.py` 5/5) — la pinza
sobre v*, el nodo más pequeño del subárbol de o₁ cuya cola contiene a o₂
y o₃: (Bo) más la cola dan a la vez `v* > φ(3φ − s)` y
`v* < φ²(2s + φ − 4)` con `s := σ₂ + ω`, incompatibles mientras
`s ≤ (6φ−1)/(2φ+1) = 11 − 4√5 = 15 − 8φ = 2.0557`, y aquí `s < 2` porque
σ₂ ≤ 1 y ω < 1. No usa σ₂ ≤ ω, ni ω ≥ φ/2, ni o₁ ≥ 3: cierra las ramas
3b–3e enteras y hace innecesario el esbozo de la torre con suma
cuadrática.

**Los ocho frentes del verificador hostil** (todos superados): (1) doble
conteo en las colas — o₂, o₃, m, σ₁, σ₂ son ajenas al subárbol de v*
(ocupantes de nivel superior; m en el agujero de y o en la sartén; el
par lo coloca P en la sartén); (2) legalidad de (Bo) en profundidad —
vale en todo nodo cuyo agujero no sea el de y, y v* lo cumple;
(3) conteo de hojas estrictas en la rama de dos hijos-nodo — las dos
hojas son estrictas porque y está fuera del subárbol de o₁, y el
ocupante de {o₂,o₃} que no contiene a y aporta la tercera: jj = 3;
(4) minimalidad de v* con empate o₁ = o₂ — obliga a definir V por «su
cola contiene o₂ y o₃» (véase reserva 2); (5) dirección de la cota del
polvo — D < φ−1 sale de la cola de m, no al revés; (6) estrictas vs no
estrictas en toda la cadena; (7) ¿prueba de más? — contraste con el
contraejemplo áureo (`thm:golden`), que vive en j = 1 y por tanto no
tiene los tres ocupantes que la cadena necesita, y además cumple
ρ = φ+3ε > φ: compatible; (8) auditoría del script bloque a bloque.

**Ataque numérico independiente.** El verificador montó un generador
propio, más estricto que el del borrador: impone y, (Ry) y (Bo) en
TODOS los nodos, el anidamiento y la rama A. Resultado: **29 310
configuraciones, mín ρ = 2.9795, sin contraejemplo**.

**Seis reservas de redacción**, todas señaladas por el verificador y ya
aplicadas en el paper y en `microcelda.md`: (1) D es el polvo
*distinto del par* (σ₁, σ₂ no cuentan como polvo en la cola de m);
(2) V se define por «su cola contiene o₂ y o₃», no por «v > o₂» — con el
empate o₁ = o₂ la segunda formulación dejaría fuera a o₁; (3) hay que
citar la rama A/B explícitamente en el paso de las dos hojas estrictas
(la rama B es el caso ya cerrado del Teorema DP); (4) «nodo del subárbol
de o₁» incluye a o₁ mismo; (5) (Bo) en profundidad presupone σ₁ ≤ 1 y
que el agujero en cuestión no es el de y; (6) el alcance del argumento
es la rama A. Ninguna afecta al resultado.

Nota de alcance (control negativo del bloque [D], no reserva): para
`s > s* = 2.0557` la cadena NO cierra. El régimen de **pivote sólido
ω ≥ 1 con j ≥ 3** queda por tanto fuera de este argumento y sigue
abierto, como ya declaraba el convenio de anchura de `batalla2.md` §1.

## Acta (2026-08-05): perfilp.md — Teorema DP-p, perfiles |S| ≥ 3 a sartén (parcial)

**Veredicto: REFUTADO tal como estaba escrito → REPARADO.** Los casos
(L), (N), (H1), (H2-ΨB) y (H2-espejos) CONFIRMADOS tras auditoría
analítica caso por caso contra thm:DP / thm:DBpp / lem:DR / lem:DBo /
lem:DG; (H2-swap) REFUTADO para j ≥ 3 y confirmado para j = 2; la
exhaustividad de la partición REFUTADA con dos celdas omitidas. Todas
las reparaciones ya aplicadas en `perfilp.md` y `code/perfilp.py` (5/5).

**Los ocho ataques:**

1. **Herencia (L) caso por caso — CONFIRMADA.** Cada colocación del par
   sigue legal mandando además W a D_m (fila σ_j + W ≤ σ₁ + W ≤ 1 para
   j ∈ {1,2}); los casos (i)–(iv) del Teorema DP portan con las mismas
   constantes y los mismos dominios de ω. El matiz de (evac_p)
   CONFIRMADO correcto: la colocación de evacuación con p piezas es
   «σ₂ → H_m vaciado, σ₁+M+W → D_m», la pared es σ₂ > 1−ω ∨ σ₁+M+W > 1,
   y en la rama B el programa Ψ_B usa la MISMA contabilidad del par con
   σ₁+M+W en el papel de σ₁+M.
2. **(N) con la tarifa X_σ₁ — CONFIRMADO con una imprecisión reparada.**
   El umbral correcto es W ≤ σ₁ − ω − X_σ₁ (la tarifa del Lema R junto
   al contenido previo del agujero de σ₁). El borrador tenía un
   paréntesis impreciso sobre a dónde va σ₁; lo correcto (ya escrito):
   W viaja dentro del agujero de σ₁ VAYA DONDE VAYA σ₁ — a D_m en
   (G_σ₂), (Bo) y la evacuación; al agujero de y en (Ry); a la sartén en
   (G_σ₁) — y por eso todas las colocaciones del par quedan legales.
3. **Geometría de espejos — CONFIRMADA numéricamente.** y₀ = 2b₂ exacto,
   tangencias con residuo ~1e-11; los espejos tienen radio
   b(o₁) ≥ b(1) = 2/3 > φ−1 ≥ σ₂ ≥ σ₃ y son disjuntos (Lema DG).
4. **Contrapositiva de la fila con pieza individual — CONFIRMADA.**
   {σ₁ con W dentro} es UNA pieza de radio σ₁ ≤ 1: la fila {σ₁} en D_m
   es legal siempre, aun con σ₁ + W > 1, y cada pieza de W cabe
   individualmente porque σᵢ ≤ W ≤ capacidad.
5. **(H2-swap) — REFUTADO para j ≥ 3, confirmado para j = 2.** La
   no-empaquetabilidad NO es hereditaria hacia subconjuntos: que
   {O, m, σ₃} falle con j ≥ 3 no implica que {o₁, o₂, m, σ₃} falle en
   el disco o₁+o₂ — el mismo motivo por el que el caso (ii) del par es
   j = 2 (j ≥ 3 fue por la escalera). Reparación: el caso queda
   restringido a j = 2 y nace la cuarta celda de R*
   ({p = 3, j ≥ 3, σ₁+M ≤ 1}).
6. **¿Prueba de más? — NO.** La familia áurea con polvo añadido
   (S = {φ/2+2ε, φ/2+ε, δ}) cae en (L) (σ₁+W = φ/2+2ε+δ ≤ 1), donde el
   suelo sigue siendo φ y la familia lo realiza: consistente. El
   contraejemplo áureo (p = 2) no entra en ningún caso nuevo.
7. **Exhaustividad — REFUTADA, dos celdas omitidas** (ambas incorporadas
   a R*): **(A)** {pesado, no-anida, σ₂ ≤ φ−1, σ₁+M > 1, j = 1,
   subárbol de o₁ = cadena hasta y (sin hoja estricta), p ≥ 4} — existe
   porque (H2-ΨB) necesita una hoja estricta que la cadena hasta y no
   tiene; es el pariente p ≥ 4 de la vieja micro-celda, hoy sin pinza
   porque no hay o₂ que atrapar. El verificador la barrió con 18 452
   muestras y 0 bloqueos supervivientes. **(B)** {p = 3, j ≥ 3, pesado,
   σ₁+M ≤ 1, σ₂ ≤ φ−1} — consecuencia directa de restringir el swap a
   j = 2 (ataque 5).
8. **Auditoría del script — superada tras una reparación.**
   `perfilp.py` 5/5 en verde; el bloque E ahora muestrea M > 0 (antes
   no ejercitaba la pared σ₁+M). Evidencia de R*: 236 685
   configuraciones examinadas con todas las paredes y coronas
   impuestas, 15 bloqueos supervivientes, mín ρ = 3.15 (margen 1.53
   sobre φ).

**Reparaciones aplicadas** (todas ya en `perfilp.md` y
`code/perfilp.py`): (1) (H2-swap) restringido a j = 2; (2) R* ampliada
de dos a cuatro celdas con las dos omitidas; (3) el paréntesis de (N)
reescrito — W viaja dentro de σ₁ vaya donde vaya σ₁; (4) el bloque E
muestrea M > 0. Estado final del Teorema DP-p: **parcial** — p = 3 con
j = 1 cerrado para todo ω > 0; (L)/(N)/(H1)/(H2-ΨB)/(H2-espejos)/
(H2-swap j = 2) probados; R* declarada abierta con evidencia.

## Acta (2026-08-06): rstar.md — cierre de la región R* (Teorema DPr)

**Veredicto: REFUTADO → REPARADO. CONFIRMADO CON CORRECCIONES salvo una
celda REFUTADA, que queda declarada abierta.** Objeto: el cierre de la
región R* del Teorema DP-p — el nuevo **Teorema DPr** (`paper/main.tex`
thm:DPr, `drafts/rstar.md`, `code/rstar.py` 6/6). Resultado neto tras
la ronda: **R* = {p ≥ 4, σ₁+M ≤ 1, j ≥ 3}** — una sola celda. Cerradas:
C4 = {p = 3, j ≥ 3} (pinza-con-Σ), C3 = {p = 3, j = 2} entera
(espejos-par / Ψ-programa / corona-vacía con margen 0.494), C1 j = 1
(coronas, márgenes 0.54–0.86), C1 j = 2 (análisis de frontera con la
esquina π), y C2 = {p ≥ 4, σ₁+M > 1, cadena} entera (j = 1 por
definición de la celda).

**Los ocho puntos de la ronda:**

1. **Suficiencia del criterio de camino más largo — CONFIRMADA
   constructivamente.** La colocación mural (círculos tangentes a pared
   con el par {o₁, o₂} diametral) es factible ⟺ el camino más largo
   sobre subsecuencias (TODAS las parejas separadas ≥ θ, no solo las
   adyacentes) es ≤ π. El verificador construyó 3 071 colocaciones
   explícitas y las contrastó con distancias euclidianas: 0 inválidas.
   El criterio ingenuo (suma de arcos adyacentes) es el que refuta el
   **pentagrama**; ese fallo fue detectado y corregido ANTES de la
   ronda por el hilo principal, y la ronda confirmó la corrección.
2. **REFUTADO: la corona de C1 para j ≥ 3 no recolocaba a o₃.** La
   contención al disco o₁+o₂ no es legal con tres o más ocupantes: o₃
   tiene que ir a alguna parte. La reparación numérica con o₃ inserto
   en la cadena da camino más largo 4.86–4.93 ≫ π: la colocación NO
   existe. La celda **{p ≥ 4, σ₁+M ≤ 1, j ≥ 3} queda ABIERTA** (única
   superviviente de R*).
3. **El margen 0.038–0.042 de p ≥ 4, j = 2 era ARTEFACTO de malla.**
   El sup real del camino más largo es **π EXACTO**, alcanzado solo en
   la esquina de frontera {σ₁ = 1, W = 0}: allí o₂ = 2/φ, o₁ = 2,
   R̄ = 2φ, con las identidades exactas
   sin²(θ(o₂,m)/2) = 1/2 − √5/10, sin²(θ(m,o₁)/2) = 1/2 + √5/10 (suman
   1 ⟹ θ(o₂,m) + θ(m,o₁) = π) y f(o₁)f(o₂) = 1 (par diametral). La
   esquina está EXCLUIDA del dominio (el perfil es < 1 estricto y
   pesado exige σ₁+W > 1): el cierre de j = 2 sobrevive **por análisis
   de frontera, no por malla** (~10⁶ muestras interiores sin ningún
   punto ≥ π). Bloque [A2] de `rstar.py` incorporado.
4. **Pinza-con-Σ rederivada desde cero — CONFIRMADA.** Frontera exacta
   de C2' contra C4': s' = (φ−1)Σ + (16−9φ); sup del dominio de
   s' − (φ−1)Σ = 5φ−7; margen **23 − 14φ = 16 − 7√5 = 0.3475 > 0**;
   degeneración exacta a 11 − 4√5 = 15 − 8φ (Teorema M) en Σ = 1.
   Monte Carlo 500k sin violación.
5. **Rama (b) de C4 (dos hijos-nodo ⟹ jj = 3): mínimo real 2.000363**
   (el 2.0058 del barrido era de malla; multistart del verificador),
   sigue > φ con margen ~0.382.
6. **C3.1 y C3.2 — CONFIRMADOS con matices.** C3.1: el ínfimo es
   exactamente φ en el rincón áureo (o₁, o₂) = (2, √5−1), que queda
   FUERA de la pared (b₂(2, √5−1) = 1 exacto); estricto porque las
   colas llevan 1+Σ > 2+σ₂. C3.2: el argmin es interior, en el cruce
   q* = √(1+(1−ω)²) (errata del mensaje de la ronda, corregida), con
   Ψ(1/2) = φ exacto y empalme √3 en ω = 1 − 1/√3.
7. **Colateral: `corona_cabe` de `perfilp.py` usaba el criterio
   ingenuo** (suma de arcos adyacentes). Ya PORTADO al camino más largo
   por el hilo principal y `perfilp.py` re-ejecutado (5/5; la
   evidencia del bloque E no cambia de veredicto).
8. **Controles negativos informativos** (bloque [E] de `rstar.py`):
   (a) sin las colas o₂ ≥ (1+Σ)/φ, o₁ ≥ (o₂+1+Σ)/φ la corona NO cabe
   (mín sobre órdenes 5.46 > π): la pared no es vacua, la vacían las
   colas; (b) quitando Σ de las colas la frontera vuelve a ser el
   11 − 4√5 del Teorema M, y la pinza SIN Σ no cierra C4 (s' alcanza
   2.226 > s* = 2.0557); (c) Ψ(0.6) = 1.477 < φ: el programa de C3.2
   no cubre ω > 1/2, por eso C3.3 necesita la pared de corona.

**Auditoría numérica independiente:** ~2M de puntos Monte Carlo +
multistart sobre las cuatro celdas (scripts `audit1.py`/`audit2.py` del
scratchpad del verificador), sin contraejemplo fuera del punto 2.
Estado final: el Teorema DPr cierra R* entera salvo la celda
{p ≥ 4, σ₁+M ≤ 1, j ≥ 3}; la vía identificada para ella es la corona
cíclica a nivel de sartén (pared R ≥ R_corona(O ∪ {m})).
`rstar.py` 6/6 tras las reparaciones.

---

## Acta 2026-08-07 — Campaña corona-contra-colas (sartén): D1, D2, D3

**Objeto**: `code/coronacolas.py` — cierre computacional de los tres
dominios residuales de la sartén: D1 = {p≥4, σ₁+M≤1, j≥3}, D2 =
pequeños extra (por adjunción al perfil), D3 = pivote sólido ω≥1 j≥3.

**Veredicto hostil: CONFIRMADO CON CORRECCIONES.** Los ocho eslabones
resistieron: (1) colas en cascada exactas (el max dentro del generador;
cierre del dominio visitado; 4 284 esquinas deterministas sin fallo);
(2) el lema del certificado angular para empaquetamientos ARBITRARIOS
verificado con cálculo propio (∂h/∂d con un solo cambio de signo ⟹
máximo de caja en esquina; 400 cajas × grid 150², 0 violaciones), el
confinamiento por triángulo, la necesidad cíclica por subconjuntos
(limitarse a los 6 mayores es conservador); (3) la suficiencia cíclica
constructiva validada EUCLIDIANAMENTE (1 500/1 500 colocaciones con
coordenadas explícitas, 0 solapes; identidad de bolsillo
θ(a,p)+θ(p,b) = θ(a,b) con error 7e-15); (4) la tangencia es legal
(interiores disjuntos); (5) legalidad del desbloqueo y dirección de
monotonía correctas; (6) D2 por adjunción con el barrido de 200k
cubriendo la partición; (7) D3 sin anchura en ningún paso; (8) NO
prueba de más: la instancia áurea nunca se certifica (en ε = 0 es la
realización tangente exacta, con sin²(θ(φ,σ)/2) = (φ+1)/(φ+2) y
sin²(θ(1,σ)/2) = 1/(φ+2) sumando 1).

**Reparado tras el acta** (6 ítems): guarda a+b ≤ R en el ciclo (bug
latente no explotable), muro de tamaño < 2 (el KeyError hacía
inalcanzable el return False), bisección devuelve el extremo seguro
`lo`, checks tautológicos convertidos en enunciados, `stackable` muerto
eliminado, y el carácter MC de B/D declarado en el resumen.

**Historia interna de la campaña** (refutaciones previas al acta, todas
del hilo principal): el pentagrama (arcos adyacentes ⟹ camino más
largo), el teletransporte de m (⟹ certificados por subconjuntos), el
clamp de la cascada (cuasi-empates exigen o ≥ φ(1+Σ)), el ancla
diametral de la suficiencia (⟹ corona cíclica en zigzag), el polvo en
la pared (⟹ bolsillos de Descartes como bins de fila).

**Limitación declarada**: B y D son evidencia computacional
(MC + esquinas + dualidad exacta déficit 0.0 uniforme), no una prueba
sobre j, p arbitrarios; el cierre formal exige redactar el argumento de
dualidad (necesidad y suficiencia usan los mismos certificados) con la
ley de escala en (j, p) como lema. ESE es el siguiente paso antes de
integrar al paper, junto con la versión anidada (D4-D6) y el
ensamblaje.

---

## Acta 2026-08-07 — Campaña anidada D4-D6

**Objeto**: `code/coronanidada.py` (+ `drafts/coronanidada.md`) — la
versión ANIDADA de corona-contra-colas: D4 = puntita j = 2
(ω ∈ [φ/2, 1)), D5 = perfiles k ≥ 3 fuera de la rama de reducción,
D6 = gap lemma (pequeños extra en v y σ₂ minúsculo), sobre la
plantilla u = agujero de α, v = c_P(m), con el intercambio que manda
m al agujero de α y re-crea D_m a nivel superior de v.

**Veredicto hostil: CONFIRMADO CON CORRECCIONES.** Verificador
independiente con script propio (sympy propio, fórmula del coseno y
Descartes rederivados, generadores adversarios). Los ocho ataques:

1. **El D_m mural — CONSERVADOR, explicado.** Re-crear D_m como
   MIEMBRO 1.0 de la corona (un disco unidad virtual que la propia
   corona coloca, con fila de suma ≤ 1, legal por el criterio de
   fila) solo puede endurecer el certificado de suficiencia: el bin
   ocupa arco como un miembro más en vez de reutilizar el hueco que
   el intercambio libera. Dirección segura; resistió.
2. **El conjunto de la necesidad {α, m = 1, o₁..o_j} — LEGÍTIMO, con
   caveat de alcance.** P empaqueta ese conjunto a nivel superior de
   v porque v = c_P(m) y m está a nivel superior SEGÚN P (según F irá
   dentro de α, pero R_lb solo necesita que ALGUIEN lo empaquete).
   Caveat anotado en el draft: esto presupone α ∈ v a nivel superior
   (v = sartén). Cuando v es un agujero y α queda anidada más arriba
   (α ∉ v), el conjunto de la necesidad es otro: ese caso es del
   ENSAMBLAJE, no de esta campaña.
3. **La esquina rígida — tangencia 2π EXACTA, verificada con sympy
   independiente.** En {α = 1/t, σ₁ = 1, σ₂ = b(t)/t}, R = α+1
   (t = 0.52): θ(α,1)+θ(1,σ₂)+θ(σ₂,α) − 2π = 0 exacto con fórmula
   del coseno propia, y b(t)/t coincide con el bolsillo de Descartes
   rederivado por curvaturas. Con σ₂ un factor 1.001–1.3 mayor el
   ciclo excede 2π y la maquinaria completa NO certifica (déficits
   positivos crecientes). En la tangente exacta sí cabe: frontera
   legal (interiores disjuntos).
4. **Familias bloqueadas contradictorias — AUSENTES.** La búsqueda de
   instancias genuinamente bloqueadas que la maquinaria certificara
   (prueba-de-más) no encontró ninguna; la única certificación en
   frontera es la tangente exacta del punto 3, y la esquina rígida
   vive además fuera del dominio (ρ ≥ 1+b(t)/t > φ).
5. **C1 (grave, enrutado) — REFUTADA la herencia geométrica de (L),
   REPARADA por reenvío.** La celda ligera (L) NO hereda las paredes
   geométricas del par: lem:DG/B1 reempaquetan v entero y destruyen
   la fila de D_m donde (L) aparca W — el mismo mecanismo por el que
   cor:DS excluye a lem:DG. Como Ψ₁(ω) < φ para ω ≥ 1/2 y ρ*₃ muere
   en ω > 1−φ/2, las celdas {(L), j = 1, ω ∈ [1/2,1)} y {(L), j = 0,
   k ≥ 4, ω > 1−φ/2} quedaban descubiertas. Reparación (gemela del
   reenvío D4W): se reenvían a la corona ('LW'), salvo si además
   anidan (W+X ≤ σ₁−ω), que van por (N). El atacante verificó
   2 779 + 2 652 coronas de las dos celdas con déficit 0.0; el
   reenvío quedó integrado en la tricotomía (`caso_anidado`) y en los
   barridos de C2.
6. **C2 (cobertura) — la franja {W ≤ σ₁−ω < W+X_σ₁} no se barría.**
   El generador de la celda de corona saltaba con W ≤ σ₁−ω, pero la
   celda es W+X_σ₁ > σ₁−ω: la franja con X_σ₁ > 0 ni se barría ni se
   heredaba. Reparación: se muestrea X_σ₁ y se salta SOLO con
   W+X ≤ σ₁−ω. El atacante verificó 669 sondas de la franja con
   déficit 0.0.
7. **C3 (legitimidad de D6) — el suelo del par no viaja con S⁺.** La
   reducción D6 → D5 + D4 transportaba el suelo α ≥ σ₁+σ₂+ω con el
   par de S⁺, que puede contener extras que NO viven en u — y la
   pared (W) solo vale para el par que sí vive en el agujero de α.
   Reparación: en las celdas alcanzables desde D6 el suelo legítimo
   es max(1+ω, par verdadero de u + ω), y el bloque D2 barre D6
   DIRECTAMENTE (gaps j = 0/j = 1, barridos nuevos j = 2 y j = 3 en
   toda ω, σ₂ minúsculo) con af tomado del par de u y los extras solo
   engordando colas y corona. Déficit 0.0 en todos los barridos.
8. **C4 (redacción) — las herencias geométricas de (N) necesitan un
   lema-extensión explícito.** (N) j = 1 (línea áurea) y (N) j = 0
   k ≥ 4 (curva canónica) usan paredes geométricas del par con W
   dentro del agujero de σ₁; el argumento de carga es: σ₁ con W
   dentro es UNA pieza (mismo radio σ₁), luego (W) queda intacta a
   fortiori, y la B3′ engordada por X_σ₁ la absorbe la cola. El lema
   está PENDIENTE DE REDACCIÓN y el docstring lo declara: esas dos
   celdas cuentan como «probadas módulo lema-extensión», sin
   sobre-reclamar.

**Reparaciones aplicadas** (todas en `code/coronanidada.py`): C1
(reenvío 'LW' en la tricotomía + muestreo de las celdas reenviadas en
los barridos de D5), C2 (salto solo con W+X ≤ σ₁−ω), C3 (barridos
directos j = 2/j = 3 con af del par verdadero de u; enunciado de la
reducción rebajado a enrutado), C4 (docstring). Re-ejecución completa
`CC_ITER=60000`: **5/5 bloques en verde**, con las celdas reenviadas
cerrando por corona con déficit 0.00 y la partición
L/N/H1/D4W/LW/corona verificada sobre 150 000 + 150 000 perfiles
(0 sin caso, 0 violaciones de contrato).

**Limitación compartida con la sartén**: B, C2 y D2 son evidencia
computacional (MC + esquinas + dualidad tangente en R_lb); el cierre
formal pende del MISMO lema de dualidad/zigzag de
`coronacolas.md` §4, con la ley de escala en (j, k) como lema, MÁS el
lema-extensión de C4. **Caveat de alcance** (punto 2): esta campaña
cubre v = sartén con α ∈ v a nivel superior; v = agujero con α
anidada es del ensamblaje.

---

## Acta: lema de dualidad/zigzag (ronda hostil) — 2026-08-08

Objeto: `code/zigzag.py` (certificados Z1/Z2/DIC/ESP/V/Z5) y
`docs/drafts/zigzag.md` (el draft del lema), el puente
evidencia → teorema de la campaña corona-contra-colas.

### VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES

El núcleo del lema resiste el asalto: solidez de la construcción
(chequeo pasa ⟹ empaquetamiento legal), solidez de la necesidad
(R_construct ≥ R_lb, 0 violaciones), DIC (identidad de tangencia
verificada de forma independiente a 50-190 dígitos en régimen mucho
más amplio que el del script), ESP por maximalidad (y más fuerte de
lo enunciado), y la dualidad exacta en D1 (déficit 0.00e+00, ahora
con un contador sin agujeros). Dos piezas de la periferia NO
resistieron: la «inducción NS-2» del draft queda REFUTADA como
implicación general (era un artefacto del generador) y el enunciado
(i) de ESP sobrevendía los triples del cierre. Ninguna de las dos
carga la prueba: se retiran/precisan y el lema queda en pie con
enunciado honesto. 8 hallazgos: 2 ALTA, 2 MEDIA, 4 BAJA. Script
reparado: **5/5 en verde** con CC_ITER=60000 y con CC_ITER=100000.

### Hallazgos

1. **ALTA — La «inducción NS-2» es FALSA como implicación general
   (check de generador sesgado) — REFUTADA y retirada del lema.**
   El draft afirmaba: «si TODOS los triples consecutivos del ciclo
   tienen margen NS-2 ≥ 0, la espina es todo el ciclo y todas las
   parejas son legales. Inducción (verificada, 1489 instancias,
   0 fallos)». Los 0 fallos eran un artefacto del generador
   (tamaños U(0.5, 3.0), ratio ≤ 6, solo orden zigzag — que nunca
   pone dos grandes consecutivos). Contraejemplo (verificado a mano,
   α y θ recomputados): orden = [0.1007, 3.007, 3.0048, 3.0142,
   0.1004], R = 6.288959 — márgenes cíclicos todos ≥ 0.032, espina =
   todo el ciclo, total = 5.161 ≤ 2π, y la pareja de grandes NO
   adyacentes (3.007, 3.0142) es ilegal por el arco LARGO (arco
   corto disponible 1.645 < θ = 2.328, déficit 0.683). Con
   generador hostil (bimodal 0.1/3.0, k ≤ 15, órdenes aleatorios):
   165 992 instancias con la premisa, 9 058 con espina propia y 907
   con parejas ilegales. CRÍTICO PARA EL VEREDICTO: en el 100% de
   los casos el chequeo constructivo RECHAZA la instancia ilegal
   (ok = False) — la solidez no depende de la inducción; muere el
   metateorema, no el certificado. Reparación: el check del bloque B
   se invirtió a control negativo (contraejemplo fijo + barrido
   hostil con zigzag Y barajas + verificación «0 certificaciones
   ilegales»); el draft reescribe V sin la inducción y documenta el
   contraejemplo.

2. **ALTA — ESP (i) sobrevendido: los triples de la espina que
   cruzan el CIERRE no están cubiertos por la maximalidad y SON
   negativos con frecuencia.** El draft decía «los triples
   consecutivos de la espina tienen margen NS-2 ≥ 0» sin excluir el
   cierre k−1 → 0, y el código solo verificaba los internos
   (`range(len(esp) - 2)`): la afirmación, leída sobre el ciclo de
   la espina, es falsa — en 19 951 ciclos adversariales, el triple
   (esp[−2], esp[−1], esp[0]) viola NS-2 en 1 570 casos (peor
   −1.73) y (esp[−1], esp[0], esp[1]) en 1 219 (peor −1.94). La
   maximalidad del camino 0 → k−1 no dice nada de la arista de
   cierre. El lema NO usa esos triples (el cierre solo entra en el
   total y en el chequeo de parejas), así que es sobreventa, no
   refutación. Reparación: enunciado precisado a «triples con centro
   INTERNO del camino crítico» (docstring, texto del check y draft)
   y los triples del cierre se reportan como control honesto
   ([info]: 532 negativos de 4000 ciclos).

3. **MEDIA — corona_instr declaraba éxito ignorando los granos
   (solidez latente rota respecto a corona_suf).** Para el split t,
   corona_suf exige que los granos asc[:t] quepan en los bolsillos
   de Descartes de la corona (bins de fila); corona_instr los
   descartaba sin chequeo: un «éxito» con t > 0 habría certificado
   un empaquetamiento que omite piezas, y la bisección de
   R_construct del bloque D habría podido subestimar. Verificado
   por replay fiel (mismo RNG compartido entre t): en los barridos
   ACTUALES nunca se dispara (0 éxitos con t > 0 en las 4 500 de D1
   y las 150 del bloque D: siempre gana t = 0), luego los datos
   publicados no estaban contaminados — pero el agujero era real.
   Reparación: corona_instr coloca los granos en los bolsillos
   exactamente como corona_suf (first-fit descendente con resta de
   capacidad) y solo declara éxito si caben todos.

4. **MEDIA — fallos invisibles en el contador del bloque C: el
   «exceso» ignoraba las parejas.** El conteo de fallos usaba
   exceso = max(0, total − 2π): un orden con total ≤ 2π pero parejas
   ilegales aparecía con exceso 0.00 y NO contaba como fallo — el
   camino exacto por el que un «exceso 0.00e+00 sospechosamente
   perfecto» podría mentir. Verificado por replay: en el barrido
   actual no hay ninguno (el 0.00e+00 era genuino). Reparación:
   ciclo_instr ahora devuelve el déficit real (máximo del exceso de
   cierre y el peor déficit de parejas, fiel al defc de
   ciclo_constructivo) y corona_instr/bloque C cuentan fallos sobre
   ese déficit («incluye parejas y granos» en el texto del check).

5. **BAJA (fortalecimiento) — el comentario «el triple individual
   puede ser positivo» era FALSO: cada saltado individual es
   sub-bolsillo por maximalidad.** Por definición del DP:
   α[t] ≥ α[i] + θ(a, s_t), α[j] ≥ α[t] + θ(s_t, b) y
   α[j] = α[i] + θ(a, b) (arista de espina) ⟹
   θ(a, s_t) + θ(s_t, b) ≤ θ(a, b) para CADA saltado, no solo la
   cadena entera; con DIC, s_t ≤ p(a, b, R). Verificado: 37 888
   saltados en 30 000 ciclos, 0 violaciones (margen peor −5.0e-06),
   0 casos s > p. El check del bloque B estaba debilitado a la
   conjunción «margen < 0 Y s > p»; ahora exige margen ≤ 0 y s ≤ p
   por separado (check «ESP fuerte»), y el draft enuncia el teorema
   con su prueba de tres líneas.

6. **BAJA (fortalecimiento) — DP-adelante: el fallo de parejas solo
   puede venir del wrap (teorema nuevo en el enunciado).** Por
   construcción del DP, α[j] − α[i] ≥ θ(i, j) para TODO i < j: el
   arco corto hacia adelante está garantizado para todas las
   parejas, y el único modo de fallo del chequeo es el arco largo
   (2π − (α[j] − α[i]) < θ(i, j)). Verificado: 20 000 ciclos, 0
   violaciones hacia adelante (49 413 pares con wrap potencial). El
   contraejemplo del hallazgo 1 falla exactamente así. Añadido como
   check (bloque B) y al draft como ESP (iv): V queda reducida a la
   condición de arco largo.

7. **BAJA — check(True) tautológico en Z2 y la duda del capado
   θ = π, resueltos con identidades exactas.** El check «no
   apilable ⟹ R − b < a + b» era un check(True) documentativo; se
   sustituyó por la identidad (2a+b) − (a+2b) = a − b (sympy) que
   cierra la cadena con a ≥ b. Y la duda de A8 («¿el capado θ = π
   rompe la monotonía/convexidad usada?») se disuelve con
   (R−a)(R−b) − ab = R(R−a−b) exacto: f(a)f(b) ≥ 1 ⟺ R ≤ a + b,
   luego en el disco el capado vive SOLO en la frontera de
   tangencia diametral (el punto áureo es exactamente esa
   frontera); además capar solo puede subir el margen, luego
   margen ≤ 0 sigue implicando s ≤ p. Ambas identidades añadidas al
   bloque A y al draft.

8. **BAJA — cifras del draft desincronizadas con barridos mayores.**
   El gap del zigzag contra el mínimo exhaustivo llega a 0.459 con
   CC_ITER=100000 (el draft decía 0.26-0.34/«~0.3»); corregido a
   0.25-0.46/«~0.46 observado». El resto de cifras del draft
   (3.24e-14, 4 500, 7.45e-04, exceso 0.00e+00) cuadran con la
   salida real; la mención «1489 instancias» de la inducción se
   retiró junto con la inducción.

### Verificaciones independientes del atacante

- **DIC en régimen amplio (A1)**: mpmath a 50 dígitos, 3 000
  puntos con ratios a/b hasta 100× y R hasta ~6(a+b) (el script
  solo prueba R ≤ 1.4(a+b)): peor |margen(p)| = 1.7e-47; p < mín(a,b)
  en el 100% de los casos con R > a+b. Más 5 identidades DIC en
  puntos racionales evaluadas con sympy a 60 dígitos: |margen| ≤
  2e-190. La prueba geométrica (el círculo de Descartes es
  mural-tangente a ambos y los ángulos murales suman) queda
  respaldada: requiere el par (a, b) mural TANGENTE — que es
  exactamente el par de la arista tangente que la construcción usa.
- **Z1 (A8)**: re-derivación por g'' con sympy: g'' =
  e^{−s}/(2(e^{−s}−1)^{3/2}) > 0 en s < 0 (comprobado también en
  malla); el argumento del script ((log g')' > 0 con g' > 0 ⟹
  g'' > 0) es correcto y está bien enunciado.
- **Fidelidad del generador D1 (A4)**: cotejado línea a línea con
  bloque_B de coronacolas.py — mismos rangos (s2 ∈ (0.01, φ−1),
  piezas ≤ s2, s1 con σ₁+M > 1, holguras expovariate(3), 30% sin
  holgura), misma cascada (máximo DENTRO antes de la holgura),
  mismo confinamiento (R_lb_pack con confinado_por = o₁): réplica
  fiel; difieren solo semilla y nº de instancias por celda.
- **Replays de solidez (A4/A5)**: reproducción externa de
  corona_instr (RNG compartido entre splits, fiel al break) sobre
  las 4 500 instancias de D1 y las 150 del bloque D: 0 éxitos con
  t > 0, 0 fallos invisibles. La comparación R_construct vs R_lb es
  coherente (mismos conjuntos desnudos {ocupantes, m}, ambos sin
  confinamiento en el bloque D).
- **Inducción hostil (A3)**: 400 000 intentos, 4 modos (uniforme,
  empates al 0.1%, bimodal 0.1/3.0, colas geométricas), k ≤ 15,
  R hasta 1.6×: 165 992 con premisa → 9 058 espinas propias, 907
  parejas ilegales, 0 certificadas. Contraejemplo mínimo verificado
  a mano (hallazgo 1).
- **Ejecuciones (A7)**: base 5/5 reproducido; tras reparaciones,
  5/5 con CC_ITER=60000 y 5/5 con CC_ITER=100000 (D1 a 7 497
  instancias, déficit máx 0.00e+00; solidez en 250 instancias,
  violación 0.00e+00; la refutación de la inducción se reproduce:
  459 espinas propias, 47 ilegales, 0 certificadas).

### Reparaciones aplicadas

En `code/zigzag.py`: ciclo_instr devuelve déficit real y α
(hallazgos 4, 6); corona_instr coloca granos en bolsillos y usa el
déficit (3, 4); bloque A con las dos identidades nuevas (7); bloque
B con checks endurecidos (5), DP-adelante (6), triples internos +
[info] del cierre (2), y la inducción invertida a refutación con
contraejemplo fijo + barrido hostil (1); docstring del módulo
actualizado (1, 2, 5, 6). En `docs/drafts/zigzag.md`: estado
ADVERSARIADO, ESP reescrito con (i) internos, (ii) individual,
(iv) DP-adelante, V sin inducción y con el contraejemplo, nota del
capado en Z1, controles negativos nuevos y cifras sincronizadas
(1, 2, 5, 6, 7, 8).

**Qué es teorema y qué no, tras la ronda**: Z1, Z2, DIC, ESP
(i)-interno/(ii)-individual/(iii)/(iv) y las dos solideces son
teoremas (identidades sympy + argumentos de maximalidad de tres
líneas); V y la dualidad exacta en R_lb son verificación por
dominio (D1: 4 500-7 497 instancias, déficit y fallos 0 con el
contador sin agujeros); la ley de escala (j, p) sigue siendo el
asterisco declarado. La inducción NS-2 ya no forma parte del lema.

---

# Acta: teorema de ensamblaje y lema-extensión (N) (ronda hostil)

Fecha: 2026-08-08. Adversario sobre `docs/drafts/ensamblaje.md` y
`code/ensamblaje.py` (6/6 en verde, CC_ITER=60000 al inicio).
Fuentes contrastadas: `paper/main.tex` (thm:oblivious §~303-341,
localización §~677-712, lem:row §219, prop:Cpair §1451, lem:DV1
§2183 (paredes B2/B3/B4/Bo/D/W), cor:DB2 §2325, thm:DBpp §2301,
app:pocket-app §2333 (B3′, thm:DGp), thm:DT3 §2535, prop:DT3j §2604,
thm:DPp §2778 (caso (ii) anidado), app:pan-app §2618, thm:DP §2638,
sec:generic §797-927), `coronacolas.md`, `coronanidada.md` (§5 C4,
§6 caveat de alcance). NO se tocaron `zigzag.py`, `zigzag.md` ni
`VEREDICTOS.md`.

## VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES

La partición (a)/(b)/(c) es correcta (definicional) y los hechos
E1–E4 sobreviven. El lema-extensión de (N) es CIERTO pero su prueba
(i) era FALSA tal como estaba escrita (contraejemplo explícito);
reparada con la división correcta monolito/absorción, anclada en los
mecanismos que el propio paper usa (thm:DPp(ii), prop:DT3j, thm:DT3
rama 1). La corrección mayor: el caso (c) vendido como «teorema» por
portabilidad NO estaba probado — la portabilidad pared a pared es
real, pero no implica cobertura de PROGRAMA; (c) queda partido en
(c-i) α ∈ v (cerrado de verdad, herencia verbatim de (b)) y (c-ii)
α ∉ v (celda abierta declarada). El teorema de ensamblaje pasa a
CONDICIONAL módulo (c-ii) además de los residuos computacionales ya
declarados.

## Hallazgos

### ALTA

**H1. El «teorema» del caso (c) era un salto lógico (A2/A7).**
El draft afirmaba que los suelos ρ > φ «se heredan verbatim» en el
puerto porque ninguna pared usa el radio del contenedor. La
inspección pared a pared es correcta a NIVEL PARED (verificado contra
el paper: criterio angular y confinamiento del gigante paramétricos
en la capacidad — coronacolas §3, |c| ≥ 2o₁+r−cap es desigualdad
triangular en cualquier disco; b_R, T_c, κ uniformes en R — sec:
generic §809-819; necesidades de par exactas por dos-círculos;
colas libres de posición). Pero un SUELO es un programa completo, y
los programas tienen hipótesis estructurales de COHABITACIÓN que el
puerto no siempre satisface:
- el programa (a) (thm:DP) usa m ∈ sartén = u (repack {o₁, m, σ}:
  la rigidez del par {o₁, m} en el disco o₁+1 exige que cohabiten) y
  E3 (j ≥ 1) usa que la sartén contiene TODO — en (c), u es un
  agujero que puede no tener ningún miembro > 1, y el portador Y no
  vive en u;
- el programa (b) (lem:DG, thm:DGp, coronas D4–D6) exige α ∈ v
  («v is a pan with occupants {α}∪O∪{m}», sec:generic §803;
  coronanidada §6 lo declara explícitamente fuera de su alcance);
- Ψ_j con j′ = ocupantes reales de la sartén no cubre j′ = 1,
  ω ≥ 1/2 (Ψ₁ ≤ φ ahí) — exactamente el hueco que en (b) tapaba la
  línea áurea, que necesita α ∈ v.
Configuración concreta sin programa: u = agujero de α sin miembros
> 1, v = agujero de Y, α ∉ v, todo anidado en una torre única de la
sartén, ω ≥ 1/2. REPARACIÓN: dicotomía (c-i)/(c-ii) en el draft;
(c-i) α ∈ v hereda (b) programa a programa (v es un disco de
capacidad Y−ω con ocupantes {α}∪O_v∪{m} según P: plantilla (b) con
R ↦ Y−ω, con las mismas etiquetas); (c-ii) queda como CELDA ABIERTA
declarada con las paredes portadas listadas y un sondeo de cierre
(con X_Y^rest = 0, las colas de α e Y con (Ry) fuerzan
σ₂ ≥ (φ−1)(1+ω) y ΣS > φ: contradicción; el caso torres/X_Y > 0
queda por programar). §6 re-etiquetado como teorema CONDICIONAL.

**H2. La prueba (i) del lema-extensión era falsa tal como estaba
(A4, el ataque central).** Afirmaba «toda colocación-testigo del
programa del par se extiende» añadiendo W al agujero de σ₁. Falso:
la colocación «σ₂ anidada en σ₁» (tercera colocación de prop:Cpair;
pared B3 de lem:DV1, placement «σ₂ ⊂ σ₁ → D_m») USA el agujero de
σ₁, y con él cargado no se extiende. Contraejemplo (ahora en el
bloque F del script): ω = 0.1, σ₁ = 0.9, σ₂ = 0.7 ≤ σ₁−ω = 0.8,
X = 0, W = 0.75 (cumple (N): W+X ≤ 0.8), pero σ₂+W+X = 1.45 > 0.8.
El LEMA sobrevive porque los programas de las dos celdas de (N) no
usan esa colocación como pared:
- j = 1 línea áurea (thm:DGp): la rama A usa Bo″, lem:DG, (W) y la
  cadena (*) con M, X_σ ≥ 0 — sin agujero de σ₁; la rama B usa B3′
  (σ₂+X_σ > σ₁−ω, YA tarifada, app:pocket-app §2338), que bajo (N)
  engorda a σ₂+X_σ+W > σ₁−ω, y la cadena (I) es INVARIANTE bajo
  X_σ ↦ X_σ+W: solo usa X_σ por esa cota inferior y por la cola de
  o₁/α, que también recogen W (masa del multiconjunto). Verificado
  simbólicamente (sympy): LHS − RHS = e₀+e₁+e₂+e₃+2e₄ en las
  holguras de {rama B, Bo″, B3′+W, (W), lem:DG}, con W dentro de e₂.
- j = 0, k ≥ 4 curva canónica: las paredes del programa (B1-corona,
  B2/dicotomía, B4, BH, W — thm:DT3 rama 1, cor:DB2) no tocan el
  agujero de σ₁; el monolito (fila W∪X_σ₁ por el lema de fila, σ₁
  una pieza de radio σ₁ vaya donde vaya) las porta todas — el
  precedente textual es thm:DPp(ii) del propio paper.
REPARACIÓN aplicada en §4bis del draft (prueba reescrita con el
reparto correcto y el contraejemplo) y en el bloque F del script
(contraejemplo + invariancia simbólica + Ψ_B(1/2) = 2 exacto para la
esquina del mín(·,2), que el draft ni mencionaba — thm:DBpp tampoco
usa el agujero de σ₁, sus masas solo engordan).

### MEDIA

**H3. El bloque B era un check tautológico (A1/A6).** Muestreaba
flags booleanos con u_pan ⟹ ¬v_pan CABLEADO («u != v y u es LA
sarten») y luego «verificaba» la partición sobre los mismos flags:
cero contenido. La exhaustividad real es DEFINICIONAL (contenedor =
sartén única o agujero de un anillo > m — esto último probado en
thm:oblivious: el padre de m es mayor que m; u = v = sartén excluido
por unicidad). REPARACIÓN: flags primitivos independientes con la
exclusión derivada y etiquetada [ENUNCIADO], predicados corregidos,
y conteo del corte (c-i)/(c-ii). Sigue siendo definicional y así se
declara en la salida.

**H4. (c1)/(c2) del draft se solapaban (A1).** (c2) decía «v =
sartén o agujero»: la configuración {u = agujero de α anidada,
v = agujero de Y} caía en (c1) Y en (c2). El script ya resolvía con
prioridad implícita; el draft no. REPARACIÓN: (c1) = ambos agujeros
(α a cualquier nivel), (c2) = v sartén con α anidada; y nota de que
el corte de cierre real es α ∈ v / α ∉ v, transversal a (c1)/(c2).
Respuestas al resto de A1: u = v = agujero del mismo anillo es
imposible (un anillo, un agujero, u ≠ v); v = agujero de Y cubre Y a
cualquier nivel (solo entra al programa vía (Ry)/colas, libres de
nivel); m a nivel superior en v con u agujero es (b) o (c2) según α;
contenedores de anillos ≤ m no existen (padre > m).

**H5. El bloque C era tautológico y no versaba sobre lo que decía
versar (A6).** Muestreaba pares con o₂ ≤ cap−o₁ y comprobaba
o₁+o₂ ≤ cap (tautología), y llamaba a eso «descenso a discos
intrínsecos». No refuta la portabilidad (que queda establecida a
nivel pared por la inspección manual contra el paper, hallazgo H1),
pero el acta debe registrar que el script NO la verificaba.
REPARACIÓN: el check ahora construye la fila diametral y valida
contención y disyunción numéricas (dirección constructiva real del
criterio exacto), y la contención antítona + lema-puerto quedan como
[ENUNCIADO] con remisión al draft. Ídem el «bonus» de la cola de Y
(semi-tautológico, etiquetado). El check análogo del bloque E ((D)
es puerta) tenía la misma tautología y se reparó igual.

**H6. Cinco checks eran check(True) sin distinguir enunciado de
verificación (A6).** E3, E4, |S| = 0, «consecuencia» del bloque F, y
la exclusión de u = v = sartén. REPARACIÓN: etiqueta [ENUNCIADO]
sistemática en script y draft §7; la «consecuencia» además corregida
en contenido (H2).

### BAJA

**H7. E1 con |S| = 0 estaba mal justificado (A3).** «El sitio de m
en u lo garantiza F» es falso a posiciones fijas de P: P puede tener
los miembros de u en otra disposición. Lo que vale (y es lo que hace
la prueba de thm:oblivious): los miembros > m de u coinciden en F y
P por maximalidad de m, las posiciones son existenciales, y P′
re-coloca u por dentro según el certificado de F con los subárboles
viajando rígidos. Con |S| = 1, añadido que la carga de σ viaja
dentro. REPARACIÓN: redactado en E1 y en el check [ENUNCIADO].

**H8. Alineación con el acta anidada C4 (A5): correcta.** Las dos
celdas del lema-extensión coinciden con coronanidada §5 (j = 1 línea
áurea mín(φ²−(φ/2)ω, 2) y j = 0, k ≥ 4, ω > 1−φ/2 curva canónica), y
la identidad φ²−φ/2 = 1+φ/2 > φ es exacta y suficiente para todo
ω ≤ 1 (el draft ya lo tenía bien). El único hueco era el transporte
de la esquina «2» (rama B con hijo-nodo, ω < 1/2), no argumentado en
el draft: cerrado vía thm:DBpp (H2, con Ψ_B(1/2) = 2 verificado
exacto). La curva canónica da ≥ 13/7 > φ para todo ω (thm:corner),
más de lo que la celda necesita.

**H9. E3 y E4 son correctos.** E3: y ≥ 1+ω porque su agujero admite
m = 1 (capacidad y−ω ≥ 1+X ≥ 1, lem:DR), y su raíz es un ocupante
> 1 de la sartén — el análogo en el puerto NO existe para u (puede
no tener miembros > 1), y eso es parte de H1, pero sí existe para la
sartén global (siempre hay un ocupante > 1 si hay portador o α
anidada). E4 vale en (b) y (c) con el matiz ya recogido en
coronanidada C3 (el suelo S₀+ω solo con el par que vive en u).

## Reparaciones aplicadas

1. `docs/drafts/ensamblaje.md`: cabecera de estado; (c1)/(c2)
   disjuntos + justificación de (a) y de «contenedor = sartén o
   agujero de anillo > m»; E1 reescrito (H7); §4bis prueba del
   lema-extensión reescrita (H2: monolito restringido +
   contraejemplo + absorción exacta de B3′ + esquina Ψ_B); lema-
   puerto rebajado a nivel pared; nueva sección de la dicotomía
   (c-i)/(c-ii) (H1); §6 teorema re-etiquetado CONDICIONAL con
   etiquetas honestas; §7 realineado con el script.
2. `code/ensamblaje.py`: bloque B reescrito (H3, H4); bloques C y E
   des-tautologizados (H5); etiquetas [ENUNCIADO] (H6); bloque F
   ampliado con el contraejemplo, la invariancia simbólica de (I) y
   Ψ_B(1/2) = 2 (H2); docstring actualizado.

## Verificaciones independientes

- Lectura dirigida del paper en todos los puntos citados (lista
  arriba); en particular: prop:Cpair enumera la colocación B3 —
  base del contraejemplo H2; lem:DV1 la deriva de «σ₂ ⊂ σ₁ → D_m»;
  thm:DGp usa B3′ SOLO en la rama B; cor:DB2 confirma que el
  programa canónico usa (B1)/(B2)/(W) sin agujero de σ₁; thm:DPp(ii)
  y prop:DT3j son el precedente exacto del monolito bien enunciado;
  sec:generic §803 confirma la hipótesis α ∈ v de TODA la plantilla
  anidada (base de H1); coronanidada §6 ya advertía el alcance.
- Re-derivación a mano de la cadena (I) de thm:DGp (con σ₁+M > 1,
  Bo″, B3′, (W), σ₁ > b₂ dos veces) y de su invariancia bajo
  X_σ ↦ X_σ+W; después codificada en sympy (bloque F).
- Sondeo de cierre de (c-ii) en el subcaso X_Y^rest = 0: (Ry) ⟹
  Y < S₀+ω ≤ α ⟹ la cola de α contiene a Y, m y S ⟹
  ρ ≥ (Y+1+S₀)/α con α < 1+ω+σ₂ ⟹ σ₂ ≥ (φ−1)(1+ω) ⟹ ΣS ≥
  2(φ−1)(1+ω) > φ para ω > (2−φ)/(2φ−2)... > 0.236; junto a
  ρ*₃ > φ en ω pequeño el subcaso parece cerrable — NO es prueba,
  queda documentado como sondeo.
- Script: 6/6 con CC_ITER=60000 y CC_ITER=200000; harness de
  semillas (scratchpad `semillas.py`): 4 desplazamientos × bloques
  B–F, todo OK. El verde no depende de la semilla cableada.

## Estado final

- `code/ensamblaje.py`: 6/6 en verde (60k y 200k; semillas OK), con
  contenido real añadido y tautologías etiquetadas o eliminadas.
- `docs/drafts/ensamblaje.md`: corregido; el teorema de ensamblaje
  queda CONDICIONAL: (a), (b), (c-i) cerrados con sus etiquetas
  (teoremas del paper + D1–D6 computacionales + lema-extensión (N)
  ahora probado); (c-ii) (α ∉ v) es la celda abierta declarada del
  ensamblaje, junto con la ley de escala (j, p, k) y los lemas de
  dualidad/zigzag ya conocidos.

# Acta: campaña (c-ii) y cierre de R2 (ronda hostil)

Fecha: 2026-08-08. Adversario hostil sobre `code/puertocii.py`
(bloques A–F), `docs/drafts/puertocii.md` y la ACTUALIZACIÓN de
`docs/drafts/ensamblaje.md` §5 que declaraba (c-ii) cerrada.
Corridas: baseline 6/6 con CC_ITER = 60000; tras las reparaciones,
6/6 con CC_ITER = 60000 (oficial) y 6/6 con CC_ITER = 150000 y
semillas alteradas (77260808/377/77260809/997/131, copia en
scratchpad). Sondeos adversarios independientes en scratchpad
(rama pesada, rama Y ≥ α, sub-celda de raíz compartida).

## VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES Y RECORTES

El recurso central del bloque [F] — el repack de la sartén — es
LEGAL (A1 confirmado contra la definición del paper). Pero el
«cierre de R2» tal como estaba enunciado era FALSO en dos frentes
(H1, H2): la pinza del par no cubre la sub-celda de raíz compartida
y la reducción por «ligereza automática I1» era errónea para
perfiles con W > 0. Tras 6 reparaciones el estado honesto es:
(c-ii) cerrada SALVO la sub-celda R2b (raíz compartida), que queda
computacional-declarada, más el [ENUNCIADO] de legalidad del repack
y el gap-dualidad de F3 delimitado. La frase «la celda (c-ii) deja
de ser residuo del ensamblaje» se RETIRA.

## A1 (la línea que decidía): legalidad del repack — CONFIRMADA

- La definición de placement del paper (Sección 2, «Rings and
  placements») dice literalmente: «Feasibility is a property of the
  assignment (siblings may be rearranged freely inside their
  container)». La factibilidad ES por contenedor y existencial en
  posiciones; las posiciones no forman parte del dato.
- La iteración de thm:oblivious solo requiere que P′ sea un testigo
  factible que COINCIDA EN CONTENEDOR con F en los anillos ≥ m
  («agreeing with F on all rings of radius ≥ r_m: the first
  disagreement strictly shrinks»). Las frases «they touch nothing
  else in v» y «rings larger than m, which do not move» pertenecen
  al certificado CONSTRUCTIVO del caso superincreciente (así se
  exhibe la factibilidad de ese P′ concreto sin re-empaquetar), no
  a la noción de paso admisible. Un P′ que reordena posiciones
  dentro de la sartén sin cambiar ningún contenedor es un testigo
  válido de la misma iteración.
- Precedentes en el propio paper y del MISMO paso de intercambio
  bloqueado: lem:DG («full repacking is a legal resource: children
  travel inside their parents, positions are existential»; cor:DS
  lo reconoce como «the global repacking of the pan») y
  thm:DP/app:pan-app (recursos: «…and the pan repack»). En (c-ii-2)
  la sartén es un contenedor TERCERO (ni u ni v): sigue siendo
  legal por la definición — mover σ₂ (< m) a la sartén y reordenar
  posiciones no toca ningún contenedor de anillos ≥ m.
- Matiz que el bloque F ya respeta tras la reparación: el repack
  debe RE-ALOJAR a todos los miembros top-level de la sartén
  (extras incluidos), no solo al par. F3 lo hace; F1e/F1f se
  enuncian con la sartén = {par} y extras vía F3.
- ETIQUETA: sigue siendo [ENUNCIADO] (la prueba formal del lema
  «bloqueo ⟹ fallo de la colocación re-empaquetada» vive en el
  draft/paper, no en el script). Correcto declararlo así.

## Hallazgos

**H1 (ALTA — REFUTA el enunciado original de [F]): sub-celda de
raíz compartida (R2b).** F afirmaba «la sartén contiene a α y al
tope T de la torre de Y (top-level, compartidos)». FALSO si la
torre de Y tiene raíz α (Y — o su ancestro z — miembro directo del
agujero de α; también en la variante especular α bajo la torre de
Y). Es una configuración de (c-ii-2) legítima (u = agujero de α,
v = agujero de Y ⊂ u, α ∉ v) y CONSISTENTE con todas las paredes:
verificado con instancia concreta (ω = 1, σ = {0.75, 0.72},
Y = 2 ∈ u, X_α = Y, α = 4.5: E4, B2u, RY, BH, D, colas y ρ ≤ φ
todos satisfechos; sondeo del scratchpad). Ahí el par {α, T}
degenera (T = α), la sartén puede ser {α} sola con R = α, y las
pinzas F1e/F1f NO aplican. Además el barrido B2 con X_α ≤ 1.5 no
podía ni rozar la sub-celda (exige X_α ≥ Y ≥ 1+ω ≈ 2).
REPARACIÓN: bloque F5 nuevo (barrido estructural con Y o z dentro
de u, d = 1..2, partición + corona-Y + corona-z + corona-α con la
pieza grande dentro, en la peor capacidad α = lb(α)): 31 304
instancias consistentes con semillas alteradas, 0 residuo — las
coronas cierran porque E4 con Y ∈ u infla la capacidad
(α−ω ≥ ΣS+X_α ≥ ΣS+Y). PERO el cierre es SOLO computacional y con
alcance declarado: R2b queda ABIERTA como celda exacta y vuelve al
residuo del ensamblaje. X_α en B2 ampliada a 3.0.

**H2 (ALTA — REFUTA la «ligereza automática»): rama pesada y
puerta (D).** I1 («E4+B2u ⟹ todo perfil de (c-ii) es ligero») es
falsa como reducción: B2u es una rama de la DISYUNCIÓN «fila en u
falla ∨ fila en D_m falla». En la rama pesada (ΣS ≥ 1+σ₂, solo
W > 0) E4 hace CABER la fila {m, σ₂} en u y el atasco pasa a
{σ₁} ∪ W: el script la despachaba como cierre ('I1-ligereza' en
B2/C/D) — ERROR. Además la puerta «(D): S₀ > 1» estaba cableada en
TODOS los muestreos; la pared limpia es ΣS > 1 (la forma S₀ > 1
exige W alojada) y S₀ ≤ 1 < ΣS es perfil legítimo del bloqueo.
Sondeo adversario: 12 021 perfiles pesados consistentes, 278
sobreviven al reparto ingenuo. CONSECUENCIA CUANTITATIVA: la caja
pesada R2W NO respeta la esquina áurea — malla B1b: supervivientes
de la partición desde ω ≈ 0.525, MUY por debajo de ω* = 3/(2φ); el
enunciado «el residuo vive en ω > ω*» solo vale para el perfil
ligero. REPARACIÓN: (i) recurso de PARTICIÓN exacta A⊎B = S
(subconjuntos; fila A en u junto a m, fila B ≤ 1 en D_m) con techo
generalizado ub(α) = 1+ω+X_α+(ΣS−B*) — subsume el B2u clásico;
(ii) muestreos sin S₀ > 1 cableado y con pesados incluidos
(B1b/B2/C/D); (iii) pinza EXACTA nueva F1f para R2W-raíz-distinta:
BH + pesado ⟹ N ≥ 4 ⟹ α ≥ 4/φ, T > 2/φ, y b₂(4/φ, 2/φ) =
12/(7φ) > 1 (⟺ 289 > 245, sympy): σ₁ y σ₂ a los DOS bolsillos
espejo (y₀ = 2b₂) y W ≤ 1 a D_m; (iv) C1 evalúa pesados en la
corona (C1W = 0 residuo); (v) E(c) reescrito (la «expulsión de la
rígida por I1» era vacua: σ₁ < m estricto; su límite es pesado).
R2W delimitada: 193 instancias en 150k, ω ∈ [0.578, 1.349], todas
con F1f aplicable.

**H3 (MEDIA — anticonservador): techo de Y con S₀.** `survive_c2`
usaba lbY < S₀+X_Y+ω y F3 muestreaba ubY = S₀+X_Y+ω, pero la pared
(RY) es la fila de TODO S: el techo correcto es ΣS+X_Y+ω. La forma
S₀ cerraba de más (el par {σ₁,σ₂} a v exige W alojada, que no es
automática) y abría un agujero de muestreo en F3 (Y ∈ [S₀+X_Y+ω,
ΣS+X_Y+ω) sin barrer). REPARADO en ambos sitios y en la caja de
`puertocii.md` §5. El cierre algebraico I3 bajo ω* no dependía del
techo (B1 ligero sigue con 0 violaciones).

**H4 (MEDIA — la rama Y ≥ α no es «vacía»).** I2 la vacía solo si
X_Y+ω ≤ φ; con X_Y+ω > φ la rama RESPIRA (22 403 supervivientes de
la condición necesaria en el sondeo con X_Y ≤ 2) y la afirmación
del mapa «donde la cierra la pinza I3 vía ω_ef» era INCORRECTA (I3
es la rama Y < α). Su cierre real es corona-Y, computacional y solo
sobre los rangos barridos (X_Y ≤ 1–2, ω ≤ 1.35). En el sondeo el
bolsillo del par sale b₂ > 1 en toda la muestra, pero no hay pinza
exacta (con X_m grande y ω chico el suelo α > 1+ω no basta).
REPARADO el texto (script y draft); la rama queda etiquetada
computacional.

**H5 (MEDIA — F3 no barría su caja).** X_m ≡ 0, X_α ≤ 0.5,
X_Y ≤ 0.1 frente a un residuo B2 con X_α hasta 1.5 y X_Y hasta
1.0; más el ubY de H3; más la línea muerta
`s1 = rng.uniform(s2, min(1.0, 1 + s2 - s2))` (el min es
idénticamente 1.0 — no era intencional: dejaba s1 ∈ [s₂, 1) sin
imponer S₀ > 1, lo cual resultó CORRECTO tras H2, pero por
accidente). REPARADO: rangos ampliados (X_α ≤ 1.5, X_Y ≤ 1.0,
X_m ≤ 0.5 muestreado), ubY con ΣS, línea limpiada, modo pesado
añadido (647 instancias pesadas en 150k), d = 0 mantiene el tope
mínimo T = Y.

**H6 (MEDIA — gap de dualidad en F3, aflorado por las semillas
alteradas).** Con ≥ 3 tops casi iguales (p. ej. {3.08, 3.07, 2.95,
1.53}) el certificado angular de `R_lb_pack` no ve los bolsillos y
subestima el radio real mínimo de los PROPIOS tops: la corona con
la carga falla en R = R_lb (3/4535 instancias, semillas alteradas)
aunque a ese radio los tops tampoco caben de verdad. No es un
contraejemplo del cierre: es el hueco necesidad-angular vs radio
real ya conocido de las campañas. REPARADO honestamente: bisección
de R_fit y delimitación del cociente (peor observado R_fit/R_lb =
1.0116; umbral declarado 1.15); las instancias quedan DELIMITADAS
con el estatus de la ley de escala, no maquilladas.

**H7 (BAJA — verificaciones que pasaron).** F1c re-derivada a mano:
N = 2+ΣS+X_m+X_α+2X_Y+ω con ω = ω_ef−X_α+φ(2X_Y+X_m) da
N = 2+ΣS+ω_ef+(1+φ)X_m+(2+2φ)X_Y (X_α se cancela exactamente,
coeficientes positivos) > 3+ω*, y (3+ω*)/φ > 2 ⟺ 2φ > 1: OK. El
suelo α ≥ N/φ viene de cola(α) con {m, S, X_m, X_α, Y, X_Y} y
Y ≥ 1+X_Y+ω, válido también con Y anidada bajo α (la cola es del
multiconjunto). Contención monótona del par diametral: R ≥ suma
del par por el criterio exacto de dos círculos (la sartén los
contiene), y el subdisco concéntrico hereda: OK. Controles E:
(a)/(b)/(d)/(e) muerden ((e): 58/58 fallos al 90% de R_lb). B3
esquina (3/(2φ), 1/2) exacta: OK (solo perfil ligero, ahora
declarado). Los docs decían «5/5» con 6 bloques: corregido.

## Reparaciones aplicadas

1. `code/puertocii.py`: `survive_c2` reescrita (piezas explícitas,
   partición u/D_m con B*, techo de Y con ΣS, sin cierre
   'I1-ligereza'; devuelve la clase ligero/pesado); helper
   `b_star`; `torre_c1` con techo generalizado por partición.
2. Malla B1 partida en ligera (claim exacto intacto: 0
   supervivientes bajo ω*) + B1b pesada (delimitación, pinza
   F-pesada verificada nodo a nodo); B2/C/D sin S₀ > 1 cableado,
   con X_α ≤ 3.0, y con rutas/cajas nuevas R2W y C1W.
3. Bloque F: F2 re-enunciado (cita de la definición de placement +
   restricción de raíz distinta); F1e restringida; F1f nueva
   (12/(7φ) > 1 exacto); F3 reparado (H5) + gap-dualidad (H6); F5
   nuevo (R2b, H1); F4 intacto.
4. `docs/drafts/puertocii.md`: cabecera, §1 (paredes corregidas),
   §2 (I1 condicional, I2 con rama respirante), §3 (B1b, R2W), §5
   (caja R2 corregida, R2W y R2b nuevas), §6 y §8 reescritos al
   estado honesto.
5. `docs/drafts/ensamblaje.md` §5: bloque de ACTUALIZACIÓN
   reescrito — (c-ii) NO desaparece del residuo: quedan R2b
   (computacional-declarada), el [ENUNCIADO] del repack y el
   gap-dualidad; la nota «pendiente ronda hostil» sustituida por la
   referencia a esta acta.
6. Copia con semillas alteradas en scratchpad (verde 6/6 a 150k):
   el verde no depende de la semilla cableada.

## Estado del script

`code/puertocii.py`: 6/6 en verde. Corrida oficial CC_ITER = 60000:
B1 1 088 541 nodos ligeros (0 bajo ω*), B1b 306 357 nodos pesados
(5621 sobreviven, 4683 bajo ω*, 0 sin pinza F), B2 150 088
instancias (residuo R2 = 552, 0 fuera de caja; R2W = 69, 0 sin
pinza), C1 18 388 coronas (déficit ligero 0.0, C1W = 0), D 17 574
enrutadas con 0 sin caso, F3 1790 con 0 gaps, F5 12 505 con 0
residuo. Semillas alteradas CC_ITER = 150000: 6/6; B2 375 154
(R2 = 1335, R2W = 193), C1 46 086, D 44 146, F3 4535 con 3 gaps
≤ 1.0116, F5 31 304 con 0 residuo. Los números de residuo son
DELIMITACIONES declaradas, no fallos.

## Qué queda abierto tras esta ronda (recorte honesto)

1. R2b (raíz compartida) como celda exacta: solo barrido F5
   (d = 1..2; profundidades mayores y variante especular declaradas
   sin barrido propio).
2. El [ENUNCIADO] F2 (legalidad del repack como lema formal).
3. La rama Y ≥ α con X_Y+ω > φ y las coronas: computacionales sobre
   rangos (X ≤ 1–3, ω ≤ 1.35, k ≤ 5, j ≤ 3, d ≤ 3).
4. El gap-dualidad de F3 (≥ 3 tops casi iguales) — mismo estatus
   que la ley de escala.


---

# Acta: bloque G (R2b) y ley de escala (ronda hostil)

Fecha: 2026-08-08 (2ª ronda hostil del día). Piezas atacadas:
`code/puertocii.py` bloque [G] + sección R2b de
`docs/drafts/puertocii.md`, y `code/escala.py` +
`docs/drafts/escala.md`.

## Veredicto global

**CONFIRMADO CON CORRECCIONES en ambas piezas.** Ningún resultado
central refutado: la esquina certificada de R2b
(π + 4·asin(1/√3) < 2π) y el lema del bolsillo-φ
(p(2φ, 2, 2φ+2) = φ) sobreviven todos los ataques. PERO una
justificación del bloque G estaba REFUTADA (la «herencia por
monotonía» de d ≥ 2/espejo: falsa por sympy), la orientación
especular no tenía tarifa derivada, la rama pesada y la rama X′ > 0
tenían agujeros de barrido, y la plantilla anidada de escala era
anticonservadora. Todo reparado y re-ejecutado hasta verde
(oficial 60k + semillas alteradas 60k/150k).

## Hallazgos — PIEZA 1 (bloque G, R2b)

**GH1 (ALTA — justificación REFUTADA, cierre reparado): la
«monotonía» de G-f era falsa y la especular no estaba derivada.**
G-f comparaba (Y, c) → (Y+ω, c+ω) y de su delta ≤ 0 muestral
concluía «subir nivel no agranda la suma: d ≥ 2 y el espejo heredan
por monotonía». Sympy la refuta como monotonía: con c − z = ΣS
constante (la forma real del nivel: z = Y+t, c = ΣS+z),
d/dt[f_z·f_m]·ΣS(c−1)² = ΣS−1 > 0 y
d/dt[f_z·f_{σ₂}]·ΣS(c−σ₂)²/σ₂ = ΣS−σ₂ > 0: DOS de los tres
productos CRECEN al subir el nivel; el delta ≤ 0 observado era un
hecho neto no certificado (y el θ capado en π lo enmascara en la
esquina). Peor: la orientación ESPECULAR (α bajo la torre de Y) ni
siquiera tiene esa forma — en ella m baja a u DENTRO de la torre de
Y y el trío {Y, m, σ₂} no existe en ningún disco común; la tarifa
del ataque inicial (sin derivar) daba 28 748 «fallos» por par
imposible hasta derivar la legalidad que faltaba: **m y z conviven
en v según P ⟹ Y ≥ 1 + z + ω** (dos círculos), que es load-bearing.
REPARACIÓN: (i) G-f0 nuevo: certificado sympy de la refutación;
(ii) G-f reescrito como BARRIDO DIRECTO de d ≥ 2 (z en su caja
legal [Y+X_z+ω, Y+X_z+σ₂+ω) por (Rz), c = ΣS+z+X′) más la pieza
grande LIBRE (domina todos los niveles): sup 4.97–5.11 < 2π, margen
≥ 1.06; (iii) G-g NUEVO: especular con tarifa derivada (legalidad
Y ≥ 1+z+ω, suelo de Y por cola(Y) = (1+ΣS+X_m+α+X′+z+X_z+X_Y)/φ,
techo (RY-esp) Y < ΣS+z+X_Y+ω; corona {z, D_m, σ₂} ligera /
{z, D_m} ∪ A pesada en c′ = Y−ω, peor capacidad Y mínimo): 7k–18k
instancias, 0 fallos. Las profundidades especulares mayores quedan
cubiertas por el patrón relativo + pieza libre de G-f.

**GH2 (MEDIA — agujero de barrido en la rama pesada).** G-e fijaba
el cuarteto {Y, σ₂, m, σ₁} con W MONOPIEZA ≤ 1 y Y solo en su
techo. La celda pesada admite W multipieza y W > 1 (ΣS ≤ φ deja
W hasta ≈ 1.5 con σ₁, σ₂ chicos), donde B* puede contener a σ₂ y
el resto A tener varias piezas: ni la colocación ni el barrido
cubrían eso. REPARACIÓN: partición EXACTA B*/A por enumeración
(B* → D_m, mural {Y, m} ∪ A por corona_suf), Y en todo su rango,
muestreo dirigido a W > 1 (160 instancias en 60k): déficit 0.

**GH3 (MEDIA — la rama X′ > 0 no se colocaba).** El argumento «X′
sube c: conservador» solo vale para el trío PELADO; las piezas X′
viven en u y también hay que colocarlas. REPARACIÓN: G-b′ nuevo con
X′ explícito (1..3 piezas, hasta tamaño Y) en la corona
{Y, m, σ₂} ∪ X′ con c = ΣS+Y+ΣX′: 21 815 instancias, 0 fallos.
(El techo de la ventana de α usado es correcto: X_Y viaja DENTRO de
Y en la fila de u — el techo B2u-fila es 1+σ₂+Y+X′+ω sin X_Y — y
el suelo por cola omite X_m/X′: conservador.)

**GH4 (BAJA — dirección de esquina imprecisa).** «La suma crece al
subir Y y σ₂» es falsa en Y: el peor Y es a menudo el SUELO (malla
adversaria: sup 5.554 con Y = suelo vs 5.5914 del G-c previo); el
sup global vive en la esquina DEGENERADA suelo = techo (ω → 0,
ΣS → 1⁺), que ambos barridos tocan. La monotonía decreciente en ΣS
con Y en frontera sí se verifica (0/20 000), y con σ₂ > 1/2 el
mínimo ΣS = 2σ₂ (s₁ = s₂) está barrido. REPARACIÓN: G-c barre Y en
suelo Y techo; texto de G-c y doc corregidos.

**GH5 (BAJA — verificaciones que PASARON).** (i) Suficiencia del
trío: «Σθ ≤ 2π» a secas NO es suficiente para 3 murales en general
— hace falta θ ≤ π por par (reparto de holgura al par opuesto) y
que cada par quepa (a+b ≤ c). Aquí ambas valen: theta_w capa en π y
los tres pares caben vía (D) (Y+1 ≤ c ⟺ ΣS ≥ 1; σ₂+Y ≤ c ⟺
σ₂ ≤ ΣS; 1+σ₂ ≤ c trivial). Cross-check trío vs ciclo_constructivo:
29 071 casos, 0 discrepancias. Docstring reparado con el argumento.
(ii) σ₂ ≤ 1/2 en la esquina: correcto (Y → 1 exige ΣS → 1; ligera +
σ₁ ≥ σ₂ ⟹ σ₂ ≤ 1/2); lejos de la esquina σ₂ llega a 0.999 con
ΣS = 2σ₂, barrido y con margen. (iii) W = 0 domina la ligera
(σ₂ ≤ (ΣS−W)/2: W > 0 solo estrecha). (iv) Rama pesada W ≤ 1 a D_m
comprobada como B* (σ₁+W < 1 en la ligera por definición). (v) La
malla G-b sin filtro ΣS+X_m ≤ φ es un superconjunto: conservador.

**GH6 (BAJA — doc inconsistente).** `puertocii.md` decía en
cabecera «R2b cerrada por [G]» y en §5/§6/§8 «ABIERTA como celda
exacta / cierre SOLO computacional (F5)». REPARADO: §5/§6/§8
reescritos al estado real (cerrada al nivel
computacional-con-esquina-exacta por [G], alcance de rangos
declarado) y la cabecera con las correcciones de esta ronda.

## Hallazgos — PIEZA 2 (ley de escala)

**EH1 (MEDIA — plantilla anidada anticonservadora).** El generador
de [C] usaba `cascada(None, S0+af, j)`: mete α_f en la cola de
TODOS los ocupantes, también los MENORES que α_f, que en la
plantilla real (`cascada_anidada` de coronanidada, rank de α en la
secuencia) no lo llevan. Medido: o_min inflado hasta +1.65
(instancias más fáciles que las reales). REPARACIÓN: [C] usa
`cascada_anidada` VERBATIM con rank muestreado y holguras; re-verde
con déficit 0.0 uniforme j = 1..8 (6 400 instancias del ataque +
corridas oficiales).

**EH2 (MEDIA — hueco enunciado-barrido del lema).** El lema promete
la colocación «perfil+polvo en fila a UN bolsillo del par (o₁, o₂)
ADYACENTES», pero los barridos usaban corona_suf con la carga
REPARTIDA (bolsillos genéricos, par no necesariamente adyacente):
demostraban otra colocación. REPARACIÓN: check nuevo en [B] que
realiza el lema TAL CUAL: corona de SOLO ocupantes+m con o₁, o₂
adyacentes (camino más largo, todas las parejas validadas), disco
de Descartes del par colocado GEOMÉTRICAMENTE (tangencia a o₁ y
pared) con holgura ≥ 0 frente a todos los demás murales, y
bolsillo ≥ masa: 687–2k instancias, 0 fallos / 0 invasiones /
0 violaciones. El doc precisa qué es [ENUNCIADO] (lem:row,
verificado en paper: «radii ≤ C pack inside a ball of radius C»)
y qué es numérico (la colocación adyacente + bolsillo libre).

**EH3 (BAJA — precisión de empates y bordes).** «Toda pieza < m»
→ «≤ m»: las piezas EMPATADAS con m (= 1) entran en cola(m) por el
convenio de primera copia, luego la cota masa ≤ φ cubre σ₁ = 1; en
el borde masa = φ = bolsillo la fila aún cabe (lem:row es ≤).
E3 verificado: el mínimo de la cascada es Σ → 1⁺ y crece en Σ
(dirección buena con Σ > 1 estricto); en D3 (pivote sólido) la
cascada es idéntica (no usa ω). Docs actualizados.

**E6/G6 (corridas).** Oficial CC_ITER = 60 000: `puertocii.py` 7/7
(G-b 43 368, G-b′ 21 815, G-e 4 301 con 160 W > 1, G-f 18 380
margen 1.32, G-g 7 351, todo déficit 0), `escala.py` 5/5. Semillas
alteradas (+7 en todos los Random): 150 000: 7/7 y 5/5 (G-f margen
1.17, G-g 18 051 con 0 fallos); 60 000: 7/7 y 5/5. El verde no
depende de la semilla.

## Reparaciones aplicadas

1. `code/puertocii.py` [G]: G-b′ nuevo (X′ explícito); G-c con Y en
   suelo y techo; G-e por partición exacta B*/A con W multipieza y
   muestreo dirigido W > 1; G-f0 nuevo (refutación sympy de la
   monotonía); G-f reescrito (barrido directo d ≥ 2 + pieza libre);
   G-g nuevo (especular con tarifa derivada Y ≥ 1+z+ω); docstring
   de trio_suma con la suficiencia k = 3 completa; helper
   b_star_particion.
2. `code/escala.py`: [C] con `cascada_anidada` real (rank + holgura);
   [B] check nuevo del lema tal cual (par adyacente + no-invasión
   del bolsillo + bolsillo ≥ masa, helpers _coloca_ciclo y
   _holgura_bolsillo); [A](vi) empates ≤ m por primera copia.
3. `docs/drafts/puertocii.md`: cabecera R2b reescrita (correcciones
   de esta ronda), §5 R2b, §6 y §8 coherentes con [G] y con la
   etiqueta honesta (computacional-con-esquina-exacta).
4. `docs/drafts/escala.md`: estado adversariado; prueba del lema con
   empates y cita lem:row; nota de lo que el barrido demuestra
   (colocación tal cual); corrección de la plantilla anidada; §3
   etiquetas actualizadas.
5. Copias con semillas alteradas en scratchpad (verdes 60k y 150k).

## Estado de los scripts

`code/puertocii.py`: **7/7 en verde** (oficial 60k; alteradas
60k/150k). `code/escala.py`: **5/5 en verde** (oficial 60k;
alteradas 60k/150k). Sin commits (según encargo).

## Qué queda abierto (recorte honesto)

1. R2b sigue siendo computacional-con-esquina-exacta: EXACTO son la
   esquina G-d, la monotonía en c, la suficiencia del trío k = 3 y
   la refutación G-f0; el sup del interior, la pesada, d ≥ 2 y la
   especular son barridos MC/frontera sobre rangos (ω ≤ 1.6,
   X ≤ 1–3, W ≤ 8 piezas). No hay monotonía de nivel que los
   sustituya (G-f0 la refuta).
2. El lema del bolsillo-φ: p/k exactos MODULO (i) lem:row
   [ENUNCIADO del paper] y (ii) la colocación
   adyacente-con-bolsillo-libre, que es numérica (0 invasiones en
   los barridos) — un lema geométrico de no-invasión del bolsillo
   de Descartes del par mayor la haría exacta.
3. La dirección j sigue numérica (dualidad tangente en rangos
   j ≤ 9 / j ≤ 8).

---

# Acta: teorema de compactación mural (ronda hostil) — 2026-08-09

Objeto: `docs/drafts/compactacion.md` (teorema + prueba §2 por
proyección) y `code/compactacion.py` (bloques A–E). La pieza que
convierte los cierres computacionales del programa τ = φ en prueba
escrita.

## VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES

La prueba de §2 (proyección mural) RESISTE: es correcta, corta y no
depende del wrap. (P1) fue re-derivado íntegramente con sympy por el
atacante — todas las identidades dan 0 exacto — y el único
ingrediente no trivial queda como teorema. Pero el draft afirmaba
«prueba completa» con un hueco real: la cláusula de bolsillos del
enunciado («además, cada saltada…») no estaba probada por §2, y la
prueba escrita de (P1) omitía una de las dos aristas cero de la
caja, la buena definición de θ y la exclusión cuantitativa del
origen. Todo reparable con piezas ya adversariadas — reparado. La
hipótesis se demostró TIGHT en dos direcciones (no se puede
suprimir NI rebajar a «no-apilable respecto del mayor»: dos
contraejemplos deterministas nuevos, uno de ellos construido en
esta ronda). 8 hallazgos: 1 ALTA, 4 MEDIA, 3 BAJA. Script: 5/5 en
verde en las cuatro corridas (60000 base, 60000 semilla+777,
150000 semilla+13, 60000 final).

## Hallazgos

### ALTA

1. **La cláusula «además» del enunciado (saltadas/sub-bolsillos) NO
   estaba probada — el ∎ de §2 solo cerraba la legalidad.** El
   enunciado promete que cada pieza saltada por el camino crítico
   queda muralmente dentro del hueco de su par de espina y es
   sub-bolsillo de Descartes; pero la proyección de §2 no define
   espina ni camino crítico (coloca a ángulos reales), y (P3) — la
   única sección que hablaba de saltadas — está documentada como
   variante SIN carga con el wrap abierto. El estatus «NO queda
   redacción pendiente» era falso para esa cláusula. NO refuta: la
   cláusula es demostrable con piezas ya adversariadas y ninguna
   depende del wrap: el θ-DP sobre el orden cíclico real es
   combinatoria pura sobre los θ; ESP-individual (acta de zigzag,
   maximalidad en tres líneas) da θ(a,s) + θ(s,b) ≤ θ(a,b) para
   cada saltada; DIC da s ≤ p(a,b,R); y la legalidad ya probada de
   la proyección deja a s mural dentro del hueco (ψ_s está entre
   ψ_a y ψ_b porque la espina respeta el orden angular). REPARADO:
   párrafo «La cláusula de bolsillos» añadido a §2 con esa prueba.

### MEDIA

2. **(P1): la prueba escrita solo cubría UNA de las dos aristas
   cero.** «d_b ≤ R−b < a+b desde R < máx+2mín» justifica h → −∞
   solo en la esquina d_a → 0; la esquina d_b → 0 necesita
   d_a ≤ R−a < a+b ⟺ R < 2a+b, que se sigue de a ≥ b
   (a+2b ≤ 2a+b, identidad (2a+b)−(a+2b) = a−b) pero NO estaba
   escrito; tampoco la esquina (0,0) (h → −∞ por cualquier
   dirección: verificado con sympy, límite direccional uniforme).
   Además faltaba la buena definición de θ: para un par empaquetado
   a+b ≤ |c_a−c_b| ≤ d_a+d_b ≤ 2R−a−b da a+b ≤ R (f(a)f(b) ≤ 1)
   automáticamente — sin esa línea θ(a,b) podría no existir.
   REPARADO: (P1) reescrito con las cuatro esquinas, la buena
   definición y el rango [0, π] de ambos ángulos explícito.

3. **La exclusión del origen era cualitativa y vaga («miembros
   relevantes»); la verdad es cuantitativa y más fuerte.** La
   afirmación del corchete es CIERTA (verificada: un centro en el
   origen exige R ≥ a+2c para todo otro c; si c ≤ a eso es
   apilable por definición; si c > a, a+2c ≥ c+2a lo da a
   fortiori — dirección que el draft no derivaba), pero lo que
   realmente vale es la cota del anillo: en todo par no-apilable,
   d_a ≥ a+2b−R > 0 y d_b ≥ 2a+b−R > 0 (de d_b ≤ R−b y
   |c_a−c_b| ≤ d_a+d_b). Ningún centro puede estar en el origen NI
   cerca — con margen positivo explícito, que es además lo que
   (P1) necesita para dividir por d_a d_b. El caso k = 1 (sin
   pares: la hipótesis es vacua y el centro SÍ puede estar en el
   origen, con ψ indefinido) no estaba cubierto: trivial (cualquier
   ángulo mural sirve), ahora explícito. REPARADO en draft +
   check dirigido de infactibilidad bajo la cota (0 violaciones).

4. **Precisión falsa en la cita del máximo por esquinas: «un único
   cambio de signo − → +, mínimo interior» no es el caso general.**
   ∂h/∂d_a = (d_a² − d_b² + (a+b)²)/(2 d_a² d_b) (re-derivada:
   numerador d_a² − (d_b² − (a+b)²)): si d_b ≤ a+b la derivada es
   > 0 en TODA la arista (no hay extremo interior); solo si
   d_b > a+b hay el cambio − → + con mínimo interior. La
   conclusión (máximo por arista en los extremos ⟹ máximo de caja
   en esquina) vale igual en ambos casos. REPARADO con la
   dicotomía escrita.

5. **El control de necesidad de la hipótesis era débil (1
   contraejemplo MC en 25) y la tightness no estaba explorada.**
   REPARADO con dos controles deterministas nuevos: (a') tres
   familias anillo (central c + corona de n círculos r murales en
   R = c+2r, coordenadas explícitas, todos los pares apilables) sin
   NINGÚN empaquetamiento mural — en cualquier colocación mural los
   huecos consecutivos suman 2π y cada uno es ≥ θ del par
   adyacente (lem:S1), y aquí Σθ_ady > 2π en TODO orden cíclico
   (peor margen 1.188): argumento de imposibilidad exacto, no MC;
   (a'') la relajación «no-apilable respecto del mayor» NO basta:
   contraejemplo construido en esta ronda, L = 2 mural + 7 círculos
   0.76 murales + 1 interior en R = 3.51 — empaquetamiento real
   explícito (holgura mínima 0.0026), pares (L,s) no-apilables
   (3.51 < 3.52), pares (s,s) apilables, y Σθ_ady − 2π = 0.236 > 0:
   sin mural. El enunciado es tight en ambas direcciones; ambos
   contraejemplos documentados en §1 del draft.

### BAJA

6. **El muestreo por rechazo nunca visita la frontera de (P1).**
   Peor holgura observada en E: 0.011–0.036; tangencias exactas y
   empates de radios ausentes por construcción (medida cero).
   REPARADO: dirigido de pares TANGENTES exactos en A (~33k–83k
   casos por corrida, esquinas d mínimas/murales + empates a = b):
   peor margen −7.6e-15 — toca la esquina mural γ = θ EXACTA, que
   es donde (P1) es igualdad; y muestreadores con empates exactos
   (prob. 0.3) y k hasta 7 en A/B/C/E.

7. **(A5) Consistencia del wrap en el repo — CONFIRMADA, sin
   dependencia oculta.** Nadie usa el wrap-por-camino-más-largo
   como teorema: rstar.md/perfilp.md usan la dualidad de cadena
   ABIERTA a₀ → a_{k+1} (scheduling estándar, sin wrap — eso SÍ es
   teorema); zigzag/escala/coronacolas usan el ciclo SIEMPRE con el
   chequeo explícito de todas las parejas (solidez condicional del
   acta de zigzag). El texto de (P3) es honesto: intento de wrap
   documentado como abierto SIN carga. Sin cambios de carga.

8. **(A7) El esqueleto de §3 es correcto; menudencias de
   trazabilidad.** La cadena bloqueo ⟹ F empaqueta C = {ocupantes,
   m} en R ⟹ compactación ⟹ reparto ⟹ contradicción cuadra con el
   paper: en el caso sartén «F places m at top level»
   (app:pan-app, verificado textualmente) y los ocupantes son nivel
   superior por definición: C está genuinamente empaquetado por F.
   El draft declara con claridad que la no-apilabilidad de ESE C es
   hipótesis por probar (pieza 1, por dominio) y que los pares
   apilables van al reparto por casos. Añadida la cita textual de
   app:pan-app en §3. Restos menores no tocados: rama muerta
   `t > 1` en bloque B (t ≥ 2 siempre) y guarda d < 1e-9 en bloque
   A inalcanzable bajo la cota del anillo (documentativos, sin
   efecto).

## Verificaciones independientes del atacante

- **(P1) completo con sympy** (scratchpad `p1_sympy.py`, 8 salidas
  exactas): cos γ = (d_a²+d_b²−L²)/(2d_a d_b) decreciente en L ⟹
  cos γ ≤ h con L ≥ a+b (h − cos γ|_tangencia = 0); numerador de
  ∂h/∂d_a = d_a² − (d_b²−(a+b)²) con raíz única solo si d_b > a+b;
  límites −∞ en las tres esquinas con d → 0 (incluida (0,0) por
  dirección arbitraria); identidad h(R−a,R−b) − (1−2f(a)f(b)) = 0;
  y la equivalencia mural (A2): dist²(γ=θ) − (a+b)² = 0 exacto —
  γ ≥ θ es EXACTAMENTE la disyunción proyectada, y lem:S1 del
  paper da el «iff» con la tangencia legal (interiores disyuntos).
- **(A3) degenerados**: tangencias reales dan γ = θ alcanzable y la
  proyección da distancia = a+b exacta — legal (tangencia
  permitida en hipótesis y conclusión); círculos al mismo ángulo
  imposibles (γ ≥ θ > 0 estricto: f(a)f(b) > 0); k = 1 trivial,
  k = 2 cubierto por la prueba general (la proyección no tiene
  wrap).
- **(A4)**: contraejemplo (a'') construido y verificado
  euclidianamente (holgura par a par, contención, apilabilidades y
  Σθ_ady — todo explícito en el script; scratchpad `a4_det.py`).
- **(P2)**: la partición dirigida es exacta para ángulos distintos
  (garantizados por γ > 0); verificada en 425 empaquetamientos con
  subsecuencias aleatorias, 0 fallos.

## Reparaciones aplicadas

En `docs/drafts/compactacion.md`: estado → ADVERSARIADO; párrafo de
tightness en §1 (hallazgo 5); corchete del origen cuantitativo +
k = 1 en §2 (3); prueba de la cláusula de bolsillos en §2 (1); (P1)
reescrito completo en §2b (2, 4); cita de app:pan-app en §3 (8).
En `code/compactacion.py`: dirigido de tangencias exactas + cota
del anillo en bloque A (6, 3); controles deterministas (a') y (a'')
en bloque D (5); empates exactos y k ≤ 7 en los muestreadores (6);
CC_SEED para corridas con semillas alteradas; docstring
actualizado.

## Estado del script

5/5 en verde en las cuatro corridas: CC_ITER=60000 base (pre y post
reparaciones), CC_ITER=60000 CC_SEED=777, CC_ITER=150000
CC_SEED=13, y la corrida final por defecto. Cifras representativas
(150k): (P1) 426 empaquetamientos / 1365 pares + 82 737 tangentes
dirigidos, 0 violaciones, peor margen −7.6e-15; (P2) 425, 0 fallos;
(P3) 437, 0 fallos; controles (a) 2/29 MC, (a') margen 1.188,
(a'') holgura 0.0026 / margen 0.236; (E) 428 proyecciones, 0
violaciones.

## Qué queda abierto tras esta ronda (recorte honesto)

1. El wrap de la variante (P3) sigue abierto — y sigue SIN carga:
   la proyección de §2 lo esquiva y nadie en el repo lo usa como
   teorema.
2. Las piezas 1–3 de §3 (no-apilabilidad del C del muro por
   dominio, capacidades del reparto, versión anidada) son las
   hipótesis del programa, no de este teorema; el draft las declara
   correctamente como pendientes.

---

## Acta 2026-08-09 — Lema de inserción y teorema D1-escrito (ronda hostil)

**Objeto**: `docs/drafts/insercion.md` (Lema A + Lema B + Teorema
D1-escrito) y `code/insercion.py`. Ataque con cálculo propio (sympy
independiente, optimización dirigida sobre el politopo de cascada,
contraejemplos construidos) sobre las líneas A1–A8.

**Veredicto hostil: REFUTADO EL ENUNCIADO, CONFIRMADA LA PRUEBA —
REPARADO.** El enunciado del Lema A tal como estaba escrito era
falso; su prueba, el presupuesto y el teorema eran correctos. Se
detectó además un hueco de hipótesis en la rama D3 (σ₂ ≤ φ−1 no
disponible) y se cerró. El «sup por esquinas» del Lema B vendía como
monotonía lo que no lo es; queda delimitado con piezas exactas
nuevas y un residuo numérico declarado. Script 7/7 tras las
reparaciones (dos bloques nuevos).

### Hallazgos ALTA

1. **El enunciado del Lema A era FALSO (refutación con n = 1).** El
   draft enunciaba la hipótesis como Σ 2·θ_R(s, x_i) < 2π con θ_R el
   ángulo MURAL de lem:S1 — pero la prueba solo soporta la SOMBRA
   Θ_i = arcsin((s+x_i)/(R−s)) bajo el régimen R > 2s+x_i, que el
   enunciado ni mencionaba. Contraejemplo: R = 3, x = 2.2 a
   profundidad d = 0.1, s = 0.5: par no apilable, Σ 2θ_R = 3.34 < 2π
   y sin embargo (R−s)+d = 2.6 < s+x = 2.7 — todo ángulo mural en
   conflicto, inserción imposible (bloque A6 nuevo). Es exactamente
   la «versión ingenua» que el propio control A4 del draft refuta:
   el enunciado contradecía su prueba. REPARADO: enunciado con
   sombras + régimen por pieza; Θ ≥ θ_R anotado como consecuencia
   del mínimo global de h.
2. **Hueco de hipótesis en D3: σ₂ ≤ φ−1 no está disponible.** En la
   celda D1 la cota σ₂ ≤ φ−1 es legítima (heredada de la región de
   thm:DPr; la rama σ₂ > φ−1 heavy la cierra thm:DPp(iii) por masa,
   la light/anidada la cierran DPp(i)-(ii) con los dominios ω < 1 de
   DP(iv)) — pero el teorema reclamaba también D3 = {ω ≥ 1, j ≥ 3},
   donde light con σ₂ > φ−1 NO está cerrada por nadie (DP(iv) exige
   ω < 1) y el presupuesto con s = σ₂ → 1 REVIENTA en el mínimo de
   cascada de D1 (6.81 > 2π: el quiebre está en s ≈ 0.955). CERRADO
   en dos pasos exactos+numéricos (bloque F nuevo): (i) σ₂ > φ/2 es
   VACÍA por masa (cola(m) ≥ σ₁+σ₂ ≥ 2σ₂ > φ, exacto); (ii) en
   σ₂ ∈ (φ−1, φ/2] la ligadura Σ ≥ 2σ₂ engorda la cascada
   (o₂ ≥ 1+Σ ≥ 1+2s, identidad exacta φ² = 1+φ) y el presupuesto
   paramétrico cierra: sup 4.61/4.93 < 2π, máximo en la esquina
   s = φ/2, Σ = φ, o = (φ³, φ², φ), margen ≥ 1.36.

### Hallazgos MEDIA

3. **El «sup por esquinas» no era un argumento: la monotonía en o₁
   es FALSA.** El presupuesto con R = o₁+o₂ acoplado NO decrece al
   crecer o₁: es bañera (decrece y luego CRECE hacia el límite π).
   Delimitado con piezas exactas nuevas (bloque D): dirección R
   exacta (sombra decrece en R); dirección o₂ exacta (el término
   propio (u−w₂)/√(u²−w₂²) queda dominado solo por el de o₁, pues
   u−w₂ = o₁−2s < o₁+s = w₁ y w₂ ≤ w₁); dirección o₁ bañera exacta
   (N_i²/P² estrictamente decreciente: numerador
   2w²(s²−o₁²−o₁o₂−o₂s−w²) < 0, denominador (o₂−2s)(u²−w²)² > 0 ⟹
   a lo sumo un cambio de signo − → + del gradiente) con límite
   o₁ → ∞ igual a π < 2π exacto. Direcciones restantes (o₃.., Σ, j):
   el presupuesto CRECE en o_k con k ≥ 3 (el sup vive en caras de la
   cascada, no en el mínimo «per se»); queda NUMÉRICO-CERTIFICADO
   por optimización dirigida sobre el politopo (coordinate ascent
   proyectado, multistart, j ≤ 8): sup 4.7214 ≤ esquina 4.7225 y
   5.2241 ≤ 5.2644 (bloque G nuevo). El draft ahora declara el
   estatus por dirección; el cierre formal del sup es un lema de
   optimización pendiente y así queda dicho.
4. **La esquina del bloque C mezcla extremos incompatibles — en la
   dirección conservadora.** (Σ → 1, s = φ−1) es infactible como
   punto del dominio (σ₂ = φ−1 fuerza Σ ≥ 2σ₂ = 2/φ > 1); como el
   presupuesto se evalúa en el mayorante desacoplado (s por encima,
   Σ por debajo), la cota solo sobra. Anotado; sin cambio de valor.
5. **Contabilidad de W' afinada (A3).** cola(m) recoge TODAS las
   piezas < 1 — perfil, polvo, extras, M y los X de los agujeros —
   así que W' ≤ φ − σ₁ − σ₂ − (M+X's) ≤ φ − 1 = 1/φ con los
   descuentos ≥ 0 explícitos. El draft lo decía a medias; ahora
   entero. Con ello σ₁+M ≤ 1 NO se usa en la construcción (M viaja
   dentro de m) y el teorema cubre de hecho {j ≥ 3, σ₂ ≤ φ−1,
   heavy} para toda p y todo ω: anotado como holgura del enunciado.

### Hallazgos BAJA

6. **v\* fuera de rango (A1-ii).** Si v\* = √(u²−w²) > R−x_i el
   mínimo interior cae fuera de las profundidades admisibles; la
   cota sigue válida (mínimo global minora el rango restringido) y
   el arco real máximo es el mural θ < Θ. Aclarado en la prueba.
7. **Generadores (A7).** El muestreador de B nunca tocaba
   R = o₁+o₂ EXACTO (el peor R, con o₁-o₂ diametrales forzosos):
   añadido G3 — esquinas euclidianas deterministas con murales
   apiñados adversarialmente (25 configuraciones, j = 3..6, Σ hasta
   φ, incluida la esquina D3 (φ³, φ², φ)): σ₂ y w* entran siempre,
   validación euclidiana directa. El «gigante profundo» queda fuera
   del dominio por (b') y su fenómeno está capturado por el control
   A4.
8. **F4 v1 evaluaba un punto infactible** (s = φ/2 con Σ < φ,
   violando Σ ≥ 2s): cota conservadora pero mensaje impreciso;
   corregido con la guarda de ligadura.

### Verificaciones que resistieron

- Ley de cosenos y dirección del signo del conflicto: identidad
  exacta w² − |c_s−c_i|² = 2uv(cos γ − h) (sympy propio, A1).
- h mural = cos θ_R de lem:S1 exacto; sombra ≥ θ_R (consecuencia
  del mínimo global; verificado además en malla 20k, mínimo ≥ 0).
- Capado: el régimen u > w da (s+x)/(R−s) < 1 — sin capar arcsin.
- Legalidad de la colocación testigo (A4): contrastada con
  thm:oblivious — contenedores de F y P coinciden, subárboles
  rígidos dentro de portadores, D_m vacante por lem:row (2ª parte),
  posiciones existenciales; σ₂/w* murales disjuntos de contenidos
  automáticamente. El círculo-fila w* cumple lem:row con hipótesis
  exacta (Σ radios ≤ w* ⟹ fila dentro del disco virtual).
- Las dos inserciones: la sombra de σ₂ está contada en el
  presupuesto de w* (bloques C y G).
- A8 (D3): ningún paso usa ω ni H_m; D_m existe con ω ≥ 1; j = 3
  con Σ → φ da presupuesto 4.13 < esquina (la masa ayuda).
- Robustez: 7/7 con CC_SEED=777/CC_ITER=60000 y
  CC_SEED=31337/CC_ITER=150000 (8 589 empaquetamientos en B, 0
  fallos de inserción, 0 solapes euclidianos).

### Reparaciones aplicadas

- `docs/drafts/insercion.md`: Lema A re-enunciado (sombras +
  régimen); control A6 (refutación del enunciado mural) añadido;
  Lema B con procedencia de σ₂ ≤ φ−1, contabilidad completa de W',
  estatus por dirección del sup y rama (d) para D3; Teorema con la
  construcción paso a paso (subárboles rígidos, X_y^rest, rama
  light de D3) y párrafo de estatus epistémico.
- `code/insercion.py`: bloques A6 (contraejemplo del enunciado),
  D-monotonías exactas (o₂ y bañera de o₁, sympy), F (rama D3
  paramétrica: vacuidad, o₂ ≥ 1+Σ, curva, optimización con
  ligadura) y G (sup por optimización dirigida + esquinas
  euclidianas deterministas R = o₁+o₂). 7/7.

**Límite declarado**: el sup del presupuesto sobre las direcciones
no cubiertas por las piezas exactas (o₃.., Σ, j y la rama (d)) es
evidencia numérica fuerte (esquinas de alta precisión +
optimización dirigida + deterministas euclidianas; margen mínimo
1.02), no teorema. El lema de optimización que lo cierre en
general es el análogo del lema del bolsillo-φ y queda como
siguiente pieza.

---

## Acta 2026-08-09 — Inserción anidada j ≥ 2 (ronda hostil)

**Objeto**: `docs/drafts/insercionanidada.md` (teorema
anidado-escrito, inserción por sombras en la plantilla anidada) y
`code/insercionanidada.py`. Ataque sobre las líneas A1–A7 con
cálculo propio (sympy independiente, sonda de ascenso coordinado
sobre el politopo de cascada, análisis de casos del régimen).

**Veredicto hostil: REFUTADA LA COBERTURA TAL COMO ESTABA ESCRITA —
REPARADA Y FORTALECIDA.** El teorema v1 era a la vez incorrecto en
un flanco (vendía j = 2, ω ≤ φ−1 hasta σ₂ ≈ 0.95 con un régimen
declarado (1+ω)/2 que no lo soportaba, apoyado en la premisa falsa
o₁ ≥ 1+ω) y débil en otro (la franja declarada
{j = 2, ω ≤ φ−1, σ₂ ∈ [0.95, 1)} es VACÍA por masa). Tenía además
dos huecos de reparto (σ₁+σ₂ ≤ 1 < Σ sin cota 1/φ; s′ = extra sin
pared ni régimen). Tras las reparaciones el teorema queda MÁS
FUERTE: j ≥ 2 COMPLETO (todo ω, todo σ₂, todo perfil, extras
incluidos); la única franja declarada es {j ≤ 1}. Script 5/5 en
todas las corridas.

### Hallazgos ALTA

1. **El régimen del enunciado descansaba en la premisa injustificada
   o₁ ≥ 1+ω.** Los ocupantes no tienen relación alguna con la pared
   de α (solo α admite a m en su agujero: α ≥ 1+ω). Con la premisa
   caída, el techo declarado s < (1+ω)/2 quedaba sin soporte, y el
   teorema afirmaba cubrir j = 2, ω ≤ φ−1 hasta σ₂ ≈ 0.95 — por
   encima de su propio techo (1+ω)/2 ≤ φ/2 < 0.95: inconsistencia
   interna (bloque A v1 lo daba por [ENUNCIADO] sin verificar).
   REPARADO con un lema exacto MÁS FUERTE (régimen automático,
   j ≥ 2): con |T| = j+1 ≥ 3 piezas top-level {α, o₁..o_j}, la
   cascada (convenio de primera copia, heredado de la sartén) da
   t₃ ≥ (1+Σ)/φ y t₂ ≥ (t₃+1+Σ)/φ ≥ (1+Σ)(1+φ)/φ² = 1+Σ ≥ 2
   (identidad φ² = 1+φ, sympy); el par de P da R ≥ t₁+t₂, luego
   R − x ≥ t₂ ≥ 2 > φ ≥ 2s′ y 2 > 2/φ = 2w* para TODA pieza del
   presupuesto: ambos regímenes estrictos con margen 2−φ, uniformes
   en ω, sin usar siquiera α ≥ σ₁+σ₂+ω. Validado además en el
   muestreo (0 fallos en ~17k instancias j ≥ 2).
2. **Hueco de reparto: σ₁+σ₂ ≤ 1 < Σ.** El testigo v1 (σ₁ → D_m,
   σ₂ mural) solo daba W′ < 1/φ vía (D) σ₁+σ₂ > 1; si el par cabe
   en D_m pero Σ > 1, la cota 1/φ del círculo-fila no salía y el
   teorema no cerraba esa rama. REPARADO: LLENADO GREEDY de D_m
   (fila decreciente hasta la primera pieza que no cabe, s′); por
   construcción fila + s′ > 1 y cola(m) ≤ φ dan W″ < φ−1 = 1/φ
   EXACTO; (D) pasa de hipótesis a peor caso (s′ = σ₂), y el
   presupuesto de s′ ≤ σ₂ queda cubierto por monotonía en s.
3. **Hueco de reparto: s′ puede ser un EXTRA de la sartén.** El
   draft v1 barría polvo/extras a w* pero presupuestaba solo σ₂ con
   la cota (α−ω)/2 del par del agujero — que NO vale para extras
   (viven en v, no en u). Un extra grande como primer no-cabe del
   greedy quedaba sin pared, sin régimen y fuera del objetivo
   medido. REPARADO: tope EXACTO uniforme s′ ≤ ℓ₂ ≤ min(Σ/2, φ/2)
   (ℓ₁ entra primero; ℓ₁+ℓ₂ ≤ Σ y ℓ₁+ℓ₂ ≤ cola(m) ≤ φ), válido
   para piezas de S y extras por igual; el régimen automático del
   hallazgo 1 cubre 2s′ ≤ φ < 2 sin distinguir procedencia; el
   bloque B mide la cobertura hasta ese tope por instancia.

### Hallazgos MEDIA

4. **La esquina-masa estaba mal atribuida y la franja mal
   delimitada.** σ₂ > φ/2 (en general s′ > min(Σ/2, φ/2)) es vacía
   SIN condición en ω: 2σ₂ > φ ≥ cola(m), exacto. El draft la
   condicionaba a ω > φ−1 (vía 2σ₂ ≥ 1+ω) y por eso declaraba la
   franja {j = 2, ω ≤ φ−1, σ₂ ∈ [0.95, 1)} — VACÍA por masa
   (φ/2 < 0.95): se declaraba como pendiente una región que no
   existe, mientras el hueco real del viejo régimen (σ₂ ∈
   ((1+ω)/2, φ/2]) quedaba sin nombrar. Con los hallazgos 1 y 3,
   j = 2 queda COMPLETO para todo ω y la franja declarada se reduce
   a {j ≤ 1}. D4 y D5 subsumidas; el borde ω = φ−1 desaparece del
   enunciado (el tope tight es ahora s′ = φ/2 con cola(m) = φ
   exacta, cubierto con margen 2−φ).
5. **Generador del bloque B con suelo espurio α ≥ Σ+ω.** No es una
   necesidad (la suma de radios de un empaquetamiento no está
   acotada por el radio del disco): excluía instancias legales con
   1+ω ≤ α < Σ+ω, en dirección NO conservadora (la sombra de α
   crece con α pero R = par también: ambiguo). REPARADO: suelo
   honesto α ≥ 1+ω (la cola de α la pone `cascada_anidada`);
   esquinas deterministas añadidas (holgura 1 exacta con empates de
   cascada, Σ → 1⁺, Σ = φ, ranks extremos de α, ω hasta 0.05 y
   0.999; 816 configuraciones); cobertura POR INSTANCIA hasta el
   tope (17 359 instancias j ≥ 2, 0 fallos) en vez de solo la celda
   D4.
6. **Paso (1) impreciso: «sin mover nada salvo m».** Los anillos
   > m del agujero de α SÍ se recolocan (interior del agujero,
   según el certificado de F — posiciones de F ≠ posiciones de P), y
   polvo/extras top-level < m de la sartén también se mueven (a
   D_m/w*). La legalidad en sí RESISTIÓ el contraste con
   thm:oblivious (~303-341): m es el mayor discrepante ⟹ cuando F
   colocó m nada < m estaba colocado y los ocupantes > m del
   agujero coinciden en F y P por maximalidad; F certificó ese
   conjunto + m; subárboles rígidos; el interior no toca la sartén.
   Redacción reparada en draft y docstring.

### Hallazgos BAJA

7. **Bloque C con cascada local inflada** (suelo 1+ω en ocupantes,
   heredando la premisa falsa del hallazgo 1) y rango de s2 del
   viejo régimen; además contaba como obligatorias inserciones
   fuera del presupuesto del Lema A. REPARADO: suelo 1.0, s2 hasta
   el tope min(Σ/2, φ/2), guardas de régimen Y de presupuesto
   (2 090 empaquetamientos, 0 fallos en ambas inserciones).
8. **La navaja j = 1 se verificó y es EXACTA y más limpia de lo
   vendido**: con o₁ = 2/φ y R = α+o₁, la razón de la sombra de α
   para w* = 1/φ es (α+1/φ)/(α+2/φ−1/φ) = 1 IDÉNTICA en α (sympy):
   el régimen falla con igualdad en el límite Σ → 1 y la sola α
   come π. La franja {j ≤ 1} está bien declarada y no se vende de
   más (el teorema exige j ≥ 2); anotado que muere por PRESUPUESTO
   (para Σ > 1 el régimen estricto sobrevive con margen (Σ−1)/φ,
   pero el presupuesto revienta cerca de la esquina). E(a) se
   mantiene como control de dirección (sin el par, la sombra de α
   incluye π); E(b) actualizado al tope nuevo.

### Verificaciones que resistieron

- Legalidad del intercambio (A1): certificado de F + maximalidad de
  m + orden decreciente, contrastado línea a línea con
  thm:oblivious; S sale entera; X_α^{>m} compartido; m coexiste con
  ellos por el certificado; M viaja dentro de m; D_m queda vacante
  top-level per P.
- Presupuesto de σ₂ (A2): posiciones reales de P; D_m contado
  entero (radio 1) es conservador (cubre a σ₁ y a la fila); la cota
  de sombra es uniforme en la profundidad (Lema A); R ≥ α+máx(o₁,1)
  y R ≥ o₁+o₂ son necesidades de par exactas (dos círculos).
- La segunda inserción comprueba su régimen y suma la sombra de s′
  (bisección y cobertura, bloque B; euclidiano, bloque C).
- s_cap medidos estables: j = 2 ≥ 0.949, j ≥ 3 = 0.999, en las
  tres semillas; sonda hostil independiente (ascenso coordinado
  sobre holguras/Σ/ω/rank, multistart): sup del presupuesto en el
  objetivo 5.2115 (j = 2) y 4.5649 (j = 3), margen ≥ 1.07 sobre 2π.
- D5: k y p no aparecen (W″ < 1/φ como un solo círculo-fila): masa,
  no cantidad.

### Reparaciones aplicadas

- `docs/drafts/insercionanidada.md`: reescrito — reparto con
  llenado greedy y extras; §2 con las dos paredes exactas (tope
  min(Σ/2, φ/2) y régimen automático t₂ ≥ 1+Σ); teorema j ≥ 2 para
  todo ω/σ₂/perfil/extras; franja reducida a {j ≤ 1}; estatus
  exacto vs numérico actualizado.
- `code/insercionanidada.py`: bloque A con las identidades nuevas
  (tope, cadena t₂ ≥ 1+Σ, W″ < 1/φ del greedy, navaja con razón
  idéntica 1); bloque B con suelo honesto, objetivo por instancia,
  esquinas deterministas y validación del lema de régimen; bloque C
  con dominio corregido y guardas; bloques D-E actualizados. 5/5.

### Estado del script

5/5 en verde en las cuatro corridas: CC_ITER=60000 por defecto
(seed 20260811), CC_ITER=60000 CC_SEED=777, CC_ITER=150000
CC_SEED=31337 y la corrida final por defecto. Cifras (150k): 50 816
instancias en B (42 461 j ≥ 2, 0 fallos de presupuesto, 0 fallos de
régimen), 5 300 empaquetamientos euclidianos en C con 0 fallos.

**Límite declarado**: los presupuestos < 2π sobre el dominio
(bisección por instancia + esquinas deterministas + sonda hostil,
margen ≥ 0.05 en cobertura y ≥ 1.07 en la sonda) son
numérico-certificados, no teorema; el cierre formal del sup es el
mismo lema de optimización pendiente que en `insercion.md`. La
franja {j ≤ 1} queda para pinza dedicada (candidatos en el draft),
cubierta computacionalmente por `coronanidada`.

---

## Acta: gap lemma j ≤ 1 (ronda hostil)

Fecha: 2026-08-09. Objetivo: `docs/drafts/gaplemma.md` +
`code/gaplemma.py` (corona directa ≤ 5 piezas, necesidad del trío,
suelos y ligaduras de masa). Líneas A1–A7 del encargo, todas
ejecutadas.

### Veredicto

**CONFIRMADO CON CORRECCIONES.** El mecanismo central (corona
directa k ≤ 5 exacta por instancia + necesidad del trío por P1 +
partición) sobrevive. Dos agujeros reales en la instrumentación
—el suelo E4 con Σ total (anticonservador) y la no-apilabilidad
afirmada sin check— reparados; con las reparaciones el barrido
sigue en 0 fallos y aparece una estructura exacta nueva (el punto
áureo del trío). 5/5 en verde tras reparar, estrés incluido.

### Hallazgos ALTA

- **A2 — Suelo E4 anticonservador (generador v1)**: el suelo
  α ≥ Σ_S+X_α+ω usa la masa DEL AGUJERO (Σ_S), pero el generador
  metía Σ total (S + extras + polvo). Los extras top-level de la
  sartén no están en el agujero: el suelo real es MENOR y el
  barrido v1 nunca visitaba α ∈ [máx(1+ω, (1+Σ+X)/φ), Σ+X+ω).
  Reparado: Σ_S ∈ [0, Σ] independiente en B y C + esquinas con
  Σ_S ∈ {0, Σ/2, Σ} + suelo mínimo absoluto α = (1+Σ)/φ con
  trade-off s′/w*. Rebarrido: 0 fallos (la región nueva aguanta,
  pero el margen real es más fino — ver MEDIA).
- **A1 — No-apilabilidad sin verificar**: el draft decía «R₃ <
  máx+2mín: verificado en el barrido» y el script NO lo
  verificaba. Peor: fuera del dominio es FALSO (ej. α = 2.6,
  o₁ = 1: R₃ = 3.628 > M = 3.0; con o₁ < 2/φ hay violaciones
  reales). Reparado doble: (i) cota BLINDADA incondicional
  R ≥ máx(pares, mín(R₃, M)) con M = mín par (máx+2mín)
  (dicotomía: par apilable a R_real ⟹ R_real ≥ M), el teorema ya
  no depende de la afirmación; (ii) CHECK explícito en bloque C:
  en las instancias con trío activo (R₃ > pares; 346–908 por
  corrida), R₃ ≤ M con 0 violaciones ⟹ mín(R₃, M) = R₃ en el
  dominio.

### Hallazgos MEDIA

- **El punto áureo del trío (estructura exacta nueva)**: el margen
  M − R₃ se anula EXACTAMENTE en (α, o₁) = (2, 2/φ): pr(α,o₁) = 1
  y pr(α,m)+pr(o₁,m) = 1 (sympy; o₁ = 2/φ raíz de o₁²+2o₁−4 = 0),
  suma del trío = 2π exacta en R = o₁+2, y además α+o₁ = o₁+2 =
  1+√5: pares = R₃ = M colapsan (el intervalo peligroso [M, R₃)
  es vacío justo donde el margen muere). El suelo o₁ ≥ (1+Σ)/φ >
  2/φ es lo que mantiene R₃ ≤ M en el dominio: el check no es
  decorativo. Documentado en §3 y check simbólico en bloque A.
- **Margen del núcleo j = 0 sobrestimado**: el 0.021 del v1 venía
  del suelo inflado Σ+ω. Con el suelo honesto mínimo
  α = máx(1+ω, (1+Σ)/φ) el margen real es ≥ 0.0073 — positivo
  pero fino. Draft y check corregidos sin maquillar.
- **A7 — Estatus inflado**: «maximización certificada ∎» sin
  distinguir el criterio exacto por instancia del sup muestreado.
  Añadido §6: exacto = reparto/P1/cota blindada/punto
  áureo/ligaduras/k ≤ 5 por instancia/límite α → ∞; el sup sobre
  la caja es barrido + esquinas con el MISMO lema de optimización
  pendiente que insercion/insercionanidada. La frase «la
  plantilla anidada queda ENTERA» se mantiene con el asterisco
  del estándar (j ∈ {0,1} ∪ j ≥ 2 sin hueco; extras en Σ ✓).

### Hallazgos BAJA

- **Límite α → ∞ solo 3 puntos y sin argumento**: añadida la
  fórmula límite (θ(α,x) → 2 asin √x; el π diametral (α,1)
  absorbe θ(α,s′) ≈ 2.24 < π por camino largo; total π +
  2 asin √(1/φ) = 4.951 < 2π, margen 1.33) + α = 10⁴ en j = 0 y
  j = 1 (navaja y holgura). [En la ronda, la primera cota burda
  del adversario sumaba los dos θ de α y daba 7.19 > 2π: la
  absorción por el camino largo es necesaria en el argumento.]
- **W″ en esquinas j = 1**: faltaba el término Σ−1 en la ligadura
  (solo Σ−2s′); añadido mín(1/φ, Σ−1, Σ−2s′) (draft §2 ya lo
  enuncia completo). Las esquinas v1 eran conservadoras (w* más
  grande), no un fallo.
- **ω y o₁ poco barridos**: ω hasta 3.0 en los generadores (antes
  1.4) y ω ∈ {2, 3} en esquinas; o₁ con holgura determinista
  hasta 20 (monotonía cubierta por puntos, no supuesta); doble
  suelo α = o₁ = (1+Σ)/φ (la esquina que el generador v1 casi no
  tocaba). A4 verificado: 24 permutaciones ⊇ 12 órdenes cíclicos
  de 5 piezas, exhaustivo; ciclos de 3–4 piezas idem; k ≤ 2
  trivial por suma. A1(ii): 3 piezas = ciclo único ✓. A1(iii):
  R₃ cota del R real de P (P empaqueta el trío top-level; θ
  decrece en R) ✓; j = 0 sin trío: cierra con R = α+1 ✓.

### Reparaciones aplicadas

- `code/gaplemma.py`: generadores B/C con Σ_S ∈ [0, Σ] honesta y
  ω ≤ 3; `M_apilable` + `R_trio_blindada` (cota incondicional);
  check explícito de no-apilabilidad (0 violaciones en activas);
  check simbólico del punto áureo (bloque A, sympy); esquinas
  nuevas (Σ_S ∈ {0, Σ/2, Σ}, suelo mínimo con trade-off s′/w*,
  doble suelo, o₁ hasta 20, α = 10⁴, ω hasta 3); límite α → ∞
  por fórmula y también en j = 1; margen del núcleo con suelo
  honesto; ligadura W″ completa en esquinas.
- `docs/drafts/gaplemma.md`: §2 con Σ_S separada y ligadura W″
  completa; §3 con la cota blindada, el check y el punto áureo;
  §4 con el barrido honesto y el margen fino; §5 sin hueco entre
  teoremas; §6 de estatus (exacto vs numérico-certificado).

### Estado del script

5/5 en verde en tres corridas: CC_ITER=60000 por defecto (seed
20260812), CC_ITER=150000 CC_SEED=777 (50 000 instancias j = 0 +
25 000 j = 1, 908 tríos activos, 0 violaciones, 0 fallos),
CC_ITER=60000 CC_SEED=31337. Sonda del adversario (scratchpad):
40k j = 0 + 30k j = 1 con suelo honesto, 0 fallos; malla fina en
dominio 6 746 tríos activos con R₃ ≤ M siempre (margen mínimo
0.0039 en (α, o₁) → (2, 2/φ), el punto áureo).

**Límite declarado**: la corona cabe en todo el dominio es
numérico-certificado (sup muestreado + esquinas), no teorema; el
cierre formal es el lema de optimización pendiente común. La cota
del trío, en cambio, queda blindada como teorema incondicional.

---

## Acta: ronda hostil del puerto escrito (`puertoescrito.md`) — 2026-08-09

Adversario sobre el draft del puerto ((c-ii) como teoremas), con
lectura con lupa de los dos teoremas anidados, `puertocii.md`,
`ensamblaje.md`, los tres scripts y sonda numérica propia
(4 866 nodos, holgura de t hasta 10⁴, ω hasta 1.35, doble inflado).

### VEREDICTO: CONFIRMADO CON CORRECCIONES

El núcleo de §1 RESISTE: la lista de 4 ingredientes agota lo que
usan thm:nestedwritten y thm:gapwritten (búsqueda con lupa: el tope
s′ y W″ son masa pura; el régimen automático solo usa |T| ≥ 3; la
cota (α−ω)/2 no se usa; el trío de gaplemma vale con t verbatim y
la blindada es incondicional por instancia; E4 entra con Σ_S libre;
sin mezcla F/P). Los suelos «solo suben» son álgebra de dos líneas
(verificado sympy).

### Hallazgos y reparaciones

1. **[GRAVE] «Holguras libres y límite α → ∞» era FALSO para
   `insercionanidada`**: holgura expovariate (~≤ 6×), sin límite
   t → ∞ — justo lo que (c-ii-1) tensiona (t inflada por la torre).
   La sonda del adversario: 0 fallos, máximo 5.2115 EN EL SUELO
   h = 1 (inflar solo ayuda; límite → π). REPARADO: bloque F en
   `insercionanidada.py` (6/6) — F0 suelo t ≥ Σ_S+ω por dos ramas
   sympy; F1 régimen bajo holgura arbitraria (9 088 instancias,
   h ≤ 10⁴, ω ≤ 1.35, dobles infladas, 0 fallos); F2 peor
   presupuesto 5.2115 en el suelo; F3 límite t → ∞ por fórmula
   (→ π, margen π). §1 reescrito distinguiendo los dos dominios.
2. **[GRAVE] El «módulo §3» de §2 omitía hojas**: los barridos del
   bloque G de R2b (computacional-con-esquina-exacta, no pinzas),
   [ENUNCIADO] F2 (legalidad del repack, del que dependen F1e/F1f),
   el gap-dualidad de F3 y los rangos de las coronas. REPARADO: §3
   ampliado a lista completa (2 ramas abiertas + 4 asteriscos
   heredados).
3. **[MENOR] Etiquetas infladas**: «COROLARIO»/«TEOREMA» heredan el
   estándar §6 (numérico-certificado en el sup). REPARADO: estándar
   heredado explícito en el corolario y el teorema.
4. **[MENOR] ω ≥ 1 no barrido en insercionanidada** (≤ 0.999 vs
   1.35 de puertocii). REPARADO: bloque F barre ω hasta 1.35 (ω
   entra solo vía el suelo 1+ω; línea en el draft).
5. **[MENOR] Redacción de suelos**: lo que hace falta (y VALE) es
   que t y los o_i satisfacen los suelos POR RANGO; t ≥ Σ_S+ω sale
   automático (dos ramas: ω ≥ φ−1 vía 1+2ω; ω < φ−1 vía cascada
   con Σ+ω ≤ 2φ−1 < 2φ). REPARADO en §1 + F0.
6. [NOTA] Script exigido y especificado — es el bloque F (el
   esqueleto fue la sonda del adversario).
7. [RESISTE] Ingredientes completos, sin mezcla F/P (ver arriba).
8. [NOTA] Las dos ramas residuales coinciden con H4 y B2u-fila de
   las actas: bien delimitadas.

### Estado tras reparación

`insercionanidada.py` 6/6 en verde (bloque F nuevo);
`insercionanidada.md` actualizado (§3 holgura grande + límite, §5
estatus); `puertoescrito.md` reescrito (dominios distinguidos,
estándar heredado, residuo completo §3.1-6).

---

## Acta: ronda hostil de las dos ramas de agujero (`coronaagujero.md`) — 2026-08-09

Adversario sobre el cierre de las dos ramas residuales del puerto
(rama respirante Y ≥ α y corona-α), con reproducción del 5/5,
55 000 instancias adversarias con semilla independiente (trade-off
s′/w* completo, mallas sesgadas a fronteras) y sondas dedicadas
(pseudo-contraejemplos k = 0 con polvo, banda k = 1 excluida,
dirección k hasta 14).

### VEREDICTO: CONFIRMADO CON CORRECCIONES

El esqueleto resiste (plantilla anidada dentro del agujero,
dicotomía k ≥ 3 / k ≤ 2, ventana exacta de c). **0 contraejemplos**
bajo fuego. Dos hallazgos graves con reparación exacta:

1. **[GRAVE] «k = 0 vacío porque las piezas son ≥ 1» era FALSO**:
   X_Y en el convenio real (compon_masa, acta 2026-08-08) INCLUYE
   polvo < m del agujero de Y. REPARADO con el **lema de
   respiración fuerte** (exacto, verificado en sonda): I2 COMPLETA
   ((φ−1)(X_Y+ω) > 1+(2−φ)ΣS+X_m+X_α) + pared (D) (ΣS > 1) ⟹
   X_Y+ω > φ(3−φ) = 2φ−1 = √5; polvo ≤ φ−ΣS < φ−1 por cola(m) ≤ φ;
   masa > m: X_{>m}+ω > √5−(φ−1) = φ EXACTO ⟹ k ≥ 1. El filtro del
   script queda justificado sin cambio de código; los
   pseudo-contraejemplos k = 0 con polvo VIOLAN la I2 completa (no
   son del dominio); la banda k = 1 excluida además pasa la corona
   (redundancia). Reescritos cabecera, A(3) y E(c) con las
   identidades sympy φ(3−φ) = 2φ−1 = √5 y √5−(φ−1) = φ.
2. **[GRAVE] Alcance k no declarado**: el certificado cubría
   k ≤ 7/6 sin decirlo. REPARADO: barridos extendidos a k ≤ 14
   (rama 1) / k ≤ 12 (rama 2) con la traza del peor presupuesto
   DECRECIENTE (5.212 → 3.382; 3.114 → 3.106) y la dirección k
   declarada como asterisco (análogo exacto de la dirección j de la
   ley de escala; cola geométrica de razón φ detrás).
3. **[MENOR] Trade-off s′/w* solo en esquina** (bloque B). REPARADO
   con el MAYORANTE DESACOPLADO: s′ = tope Y w* = 1/φ simultáneos
   (monotonía en ambos tamaños); peor sube a 5.2115 — exactamente
   el suelo crítico del teorema anidado — y sigue < 2π−0.05.
4. [NOTA] En rama 2 el suelo E4 domina siempre (ΣS+X_α ≥ 1+x₁+x₂ >
   pares, M): ventana efectiva [ΣS+X_α, 1+σ₂+X_α) a secas. Anotado.
5. [NOTA] Checks vacuos A(3)/E(c) reescritos con la sustancia.
6. [NOTA a favor] Σ ≤ 1 imposible en la celda (pared (D)): el
   barrido Σ ∈ (1, φ] no es restricción. Anotado.

RESISTEN: la cola es GLOBAL (convención del paper, líneas 202-203:
la cadena x₂ ≥ 1+Σ vale en ambos agujeros); pares y blindada
legítimos (rama 1: P empaqueta {x's, m}; rama 2: F empaquetó
{x's, m} simultáneos al colocar m, los > m coinciden por
maximalidad); extras de v → Σ; X_m viaja dentro de m; régimen rama
2 incluye m (c−1 > 2σ₂ con margen); suelos conservadores (peor c,
holguras sobreyectivas, en rama 2 usar ΣS en la cascada debilita:
dirección buena); E4 sin el bug Σ_S/Σ del gap lemma; el lema de
inserción usado agnóstico a posiciones; exhaustividad de la
partición por ramas (las exclusiones tienen cierre exacto propio).

### Estado tras reparación

`coronaagujero.py` 5/5 (mayorante, k extendido, lema de respiración
fuerte en A(3)/E(c)); `coronaagujero.md` reescrito (§2 lema fuerte,
§3 ventana efectiva, §4 alcance k explícito, §5 estatus completo).
**Las dos ramas de `puertoescrito.md` §3.1-2 quedan CERRADAS al
estándar del programa** (exacto en ligaduras/regímenes/ventanas/
respiración; numérico-certificado en sups; dirección k asterisco
decreciente).

---

## Acta: ronda hostil del lema de la cola geométrica (`colageometrica.md`) — 2026-08-09

Adversario con reproducción del 5/5, ~31 600 familias adversarias
propias (28 809 de los generadores REALES de los teoremas), malla
fina del sup (~2·10⁶ evaluaciones de G) y contraejemplos dirigidos.

### VEREDICTO: CONFIRMADO CON CORRECCIONES

La maquinaria (S)/(M)/(N)/(V) es correcta; la dominación resiste
TODO el fuego (0 violaciones en ~45k familias: holguras 10⁴ en
posiciones elegidas, empates exactos, Σ = φ, frontera t₃ = p_min,
las tres cascadas reales). La esquina 5.2115 es EXACTA (G = real,
gap 0: identidad de familia {2φ, 2, 2/φ}+D_m con los barridos de
insercionanidada F y coronaagujero B).

1. **[GRAVE] El enunciado omitía t₂ ≥ 1+Σ**: solo es teorema para
   n ≥ 3 (cadena φ² = 1+φ); con n = 2 hay contraejemplo EXPLÍCITO
   dentro de las hipótesis declaradas (Σ → 1, t₂ = (1+Σ)/φ,
   t₁ = vínculo en su suelo = 1+Σ, w* = 1/φ: presupuesto 6.93 >
   2π) — es LA NAVAJA ÁUREA j ≤ 1: la frontera del lema coincide
   exactamente con la frontera conocida de los teoremas de
   sombras. REPARADO: hipótesis en §1 + control E(e); los tres
   teoremas consumidores la garantizan — la Consecuencia §4
   sobrevive sin cambios.
2. [MENOR] «sup G = 5.2115» como igualdad global descansaba en
   interpolación en la banda t₂ > 10⁶. REPARADO: §1 enuncia
   sup < 2π−0.05 con la banda acotada por fórmula (5.5237 <
   2π−0.4); la malla del acta hasta 10⁸ converge a 4.71.
3. [MENOR] La NOTA del bloque C decía «gap ~0.3»: el gap en la
   esquina es 0 EXACTO (identidad de familia). REPARADO.
4. [MENOR] La dominación solo se verificaba sobre el generador
   propio. REPARADO: bloque B ampliado a cascada_anidada
   (j ≤ 6, suelo 1+ω, rank barrido) y cascada_agujero (k ≤ 14),
   0 violaciones — los suelos extra solo inflan y toda cota
   sobrevive al inflado.
5. [NOTA] Tolerancia del corte en frontera: con u real nunca se
   excluye una pieza existente (cap ≥ t ≥ p_min sin tolerancia);
   la exclusión solo ocurre en nodos de barrido infactibles.
   Anotado en docstring.
6. [RESISTE] (V) y los empates: el convenio de primera copia hace
   del empate el punto de CONTACTO del vínculo ((t₂+t₂/φ)/φ = t₂
   exacto); 0 violaciones con t₁ = t₂ y cola máxima.
7. [RESISTE] El sup sobre la caja legítima: malla fina sin hombro
   entre nodos; máximo 5.2115.
8. [RESISTE] (M)/(N), extras por modo, ligadura Σ ≥ 2σ₂, alcance
   §4 bien delimitado (solo quita topes donde hay sombras; la
   dirección j de dualidad/escala conserva su asterisco).

### Estado tras reparación

`colageometrica.py` 5/5 (hipótesis, E(e), NOTA corregida, bloque B
ampliado); `colageometrica.md` reescrito (§1 hipótesis + frontera
navaja, §2 empates, §3 dominación ampliada, §5 estatus). **Los
topes j ≤ 6 / k ≤ 14 / k ≤ 12 de los teoremas escritos pasan a
redundancia empírica: los presupuestos de sombras son uniformes en
el número de ocupantes.**

---

## Acta: ronda hostil del lema de optimización (`optimizacion.md`) — 2026-08-09

Adversario con reproducción del 5/5, instrumentación del B&B,
fuzzing de la cota de caja (64 840 puntos reales contra cajas
aleatorias), contraejemplos a la forma normalizada, análisis del
resto analítico hasta t₂ = 10¹⁰⁰ y objetivos intermedios.

### VEREDICTO: CONFIRMADO CON CORRECCIONES

El resultado (sup G < 2π − 0.05) es verdadero y el B&B principal es
sólido (cota de caja válida coordenada a coordenada, podas sin
fugas — 0 violaciones en el fuzzing, peor gap +2.3·10⁻⁸ —,
terminación temprana correcta por max-heap). Tres reparaciones:

1. **[GRAVE] El suelo del vínculo normalizado del bloque C no era
   cota superior**: usaba (a_lo+u′_lo)/φ en vez de (1+u′_lo)/φ (el
   «t₂» del vínculo se normaliza a 1 exacto) — déficit de hasta
   0.47 rad en cajas con a_lo > 1. El certificado v1 sobrevivió
   solo porque ninguna caja evaluada activaba el bug (instrumentado:
   0 cajas activas en la corrida real). REPARADO (una línea) +
   control E(c) que demuestra la violación de la versión rota.
2. **[GRAVE] El «40» del resto analítico no estaba justificado** (y
   la fórmula escrita fallaría desde t₂ ≈ 10²⁰ con σ uniforme): la
   justificación real es el acoplamiento σ_real·(N−60) ≤
   (φ/2)·log_φ(φt₂/3)/t₂ < 10⁻¹³, decreciente en t₂ (el conteo es
   log pero σ decae como 1/t₂). REPARADO en docstring y draft;
   verificado por el acta hasta t₂ = 10¹⁰⁰ (suma real ≤ 9.3·10⁻¹³).
3. **[GRAVE en redacción] La frase de flotantes era falsa**: el
   margen de la decisión de parada era 5·10⁻⁵ (no «≥ 0.9 rad, 12
   órdenes») por la terminación temprana. REPARADO subiendo la
   caja principal al objetivo FUERTE 5.25 (4 495/5 126 cajas,
   verificado viable por el propio adversario): ahora TODA caja
   final tiene cota ≤ máx(5.25, 6.0408) y el margen real frente a
   2π−0.05 es 0.19-0.98 rad, > 12 órdenes de verdad.
4. [MENOR] El guard r > 200 truncaba en silencio (subestimación
   potencial fuera del dominio). REPARADO: raise.

RESISTEN: la cota de esquina del B&B principal (la mezcla Σ_hi/Σ_lo
es válida — ningún factor usa Σ en direcciones opuestas); las tres
podas (sin fugas, verificado con esquinas); la terminación temprana
(invariante de heap); la reducción de modos (contra los tres
consumidores reales: el patrón es siempre «una inserción, luego w*
con la insertada como pieza» — no existe presupuesto con σ₂ y s′
simultáneos bajo w*); objetivos intermedios coherentes (5.25/5.5/
6.0 certifican; 5.20 se atasca en 5.2115 exacto); T₂ = 1000 no es
frágil (con 10⁴ también certifica); el alcance §4 es honesto.

### Estado tras reparación

`optimizacion.py` 5/5 (vínculo normalizado reparado, objetivo
fuerte 5.25, raise en el guard, control E(c));
`optimizacion.md` reescrito (§2 reparaciones, §3 certificado
fuerte, flotantes honestos). **Los sups de presupuestos de sombras
de los teoremas escritos quedan CERTIFICADOS por subdivisión
exhaustiva** (≤ 5.25 en la caja principal, < 2π−0.05 globalmente):
el «lema de optimización pendiente» de los teoremas de sombras está
cerrado; conservan etiqueta propia los dominios de coronas acotadas
y los cierres computacionales.

---

## Acta: ronda hostil del lema de realización y repack (F2, `repack.md`) — 2026-08-09

Adversario con reproducción del 5/5, sondeos deterministas
(tangencias exactas, sólidos r ≤ w, micro-agujeros 0.05, gemelos de
igual radio, rotaciones/reflexiones de subárboles) y verificación de
la equivalencia del chequeo (argumento del punto extremo + criterio
analítico por arcos, 3 000 pares, 0 discrepancias).

### VEREDICTO: CONFIRMADO CON CORRECCIONES

El núcleo — (a) realización global por composición raíz-hoja, (b)
repack con subárboles rígidos — es correcto y cierra el [ENUNCIADO]
F2. Hallazgos:

1. **[GRAVE] (c) mislabelaba re-asignaciones como instancias de
   (b)**: el propio paso de intercambio y las coronas de agujero
   CAMBIAN el bosque (m se muda; los menores se recolocan) — eso no
   es «mismas bolas, otra colocación»: es un bosque nuevo cuya
   legalidad la cargan los certificados por contenedor (F, fila,
   corona, bolsillo), con (a) como paso de composición. REPARADO:
   (c) reescrito — testigo = asignación bosque-factible +
   colocación por contenedor con su recurso; (b) queda como caso
   particular (pan repack, bolsillo espejo con el mismo conjunto).
2. **[GRAVE→MENOR] Deslinde con el lema de inserción**: la
   construcción del testigo consume posiciones reales de P (la bola
   vacante de m, la inserción mural «sin mover nada») — posiciones
   EXISTENCIALES: se toma una realización y se modifica contenedor
   a contenedor; recursos posicionales y de conjunto son
   complementarios y ambos desembocan en (a). REPARADO en (c).
3. [MENOR] La hipótesis inductiva de (a) no estaba enunciada y
   «disjuntos» debía ser «interiores disjuntos» (tangencias
   legales). REPARADO: invariante explícito
   material(subárbol) ⊂ bola, material(descendientes) ⊂
   bola-agujero; los tres tipos de par verificados por el acta.
4. [MENOR] Bloque A decorativo. RE-ETIQUETADO como transcripción.
5. [MENOR] El generador filtraba r < 3w (sólidos jamás
   ejercitados) y sin tangencias exactas. REPARADO: sólidos en el
   generador + sub-bloque determinista (los casos del acta).
6. [MENOR] Comentario muerto en D(1) (bisección no implementada);
   la fórmula del bolsillo verificada por el acta (Descartes
   degenerado exacto en R = α+o₁). LIMPIADO; D declarado
   ilustrativo.
7. [NOTA] ρ depende SOLO del multiconjunto (ni siquiera del
   bosque); N, A del conjunto colocado. Separado en (b).
8. [NOTA] Traslaciones bastan; isometrías de una colocación son
   otras colocaciones (regiones rotacionalmente simétricas).
   Frase añadida; rotación/reflexión verificadas (0 violaciones).
9. [NOTA] «bit a bit» → módulo permutación de radios iguales.
10. [NOTA] K arbitraria y dimensión d: el argumento vale verbatim
    (solo la raíz cambia). Frase añadida — F2 cubre lo que
    thm:oblivious reclama.

RESISTE: la equivalencia del chequeo con la disyunción de
interiores (no es «más fuerte»: imposibilidad del solape parcial
sin cruce de circunferencias, punto extremo); tangencias exactas,
sólidos, micro-agujeros, profundidad 4 real, gemelos: 0 violaciones
en todos los sondeos.

### Estado tras reparación

`repack.py` 5/5 (sólidos en el generador, sub-bloque determinista
con isometrías, bloque A re-etiquetado, D limpiado); `repack.md`
reescrito ((a) con hipótesis inductiva e interiores, (b) con
invariantes finos, (c) completo con el deslinde). **El [ENUNCIADO]
F2 queda cerrado como lema probado desde la definición.**

---

## Acta: ronda hostil de R2b certificada (`r2bcert.md`) — 2026-08-09

Adversario con reproducción del 5/5 (148/41 948 cajas exactas),
fuzzing de la cota DR (200k cajas con puntos reales, X hasta 3, T
hasta 10¹⁰), MC de cobertura ESP (800k tiros) y verificación de
tarifas contra el código de [G].

### VEREDICTO: CONFIRMADO CON CORRECCIONES

**La rama DR es un certificado genuino y sólido**: superconjunto
legítimo de G-b/G-c/G-f (tarifas verificadas en código), cotas de
caja válidas (0 violaciones, 0 podas de puntos reales), cola T → ∞
correcta, podas sin pérdida (fronteras compartidas), certifica SIN
la pared de masa. Hallazgos:

1. **[GRAVE] El alcance ESP era falso como enunciado**: certificaba
   el corte X = 0 sobre la caja del barrido, no «las cajas legales
   ENTERAS» — con X > 0 los TECHOS de ventana se desplazan (X = 0
   solo es el peor para el suelo de cola(Y)): 54k configuraciones
   legales del MC quedaban fuera del corte; y ω > 1.6 sin techo
   legal. Sin contraejemplo (sup MC con X > 0, ω ≤ 3: 5.7379 <
   objetivo). REPARADO: alcance reescrito; ESP fuera del corte al
   FUERA.
2. **[GRAVE, compartido con G-g] Las X_Y de la ESP viven en v** (la
   corona real tiene > 3 piezas; k = 3 no aplica): el análogo
   especular de G-b′, sin argumento escrito. REPARADO: al FUERA.
3. [MENOR] La narrativa de E(d) acusaba en falso a G-g: G-g SÍ
   imponía la pared (`SS+Xm > φ: continue`, ligera incluida).
   REPARADO: el aporte real del B&B es demostrar que la pared es
   NECESARIA para el trío ESP (la esquina σ₂ → 1 sin pared es
   legal y la corona no cabe: par diametral exacto, disc = 0,
   bolsillo 0.958 < σ₂) — la DR no la necesita.
4. [MENOR] «> 13 órdenes» falso otra vez (la lección de
   optimización): el delta de parada real es DR 5.6·10⁻³ / ESP
   1.9·10⁻⁵ (~10 órdenes sobre float). REPARADO.
5. [NOTA] La fórmula de bolsillo sin raíz coincide en el punto
   (disc = 0) y en general mayora: a fortiori. Documentado.

RESISTEN: dominación DR (A1), cota de caja (A2, fuzzing), cola
T → ∞ (A3), validez de c′_lo ESP incluso con X > 0 (A4 — el
problema era cobertura, no cota), certificado DR sin pared (A5),
podas/partición sin pérdida y honestidad del objetivo (A6), pares
cabiendo en ambas ramas (A7), FUERA de la DR bien rebajado (A8).

### Estado tras reparación

`r2bcert.py` 5/5 (E(d) y docstring corregidos); `r2bcert.md`
reescrito (§3 corte X = 0, §4 lema con alcance honesto, §5 deltas
de parada). **G-b/G-c/G-f certificados sobre el dominio legal
entero; G-g ligera certificada en el corte X = 0; el resto de [G]
permanece como barrido declarado.**

---

## Acta: ronda hostil de bolsillos fase 1 (`bolsillos.md`) — 2026-08-09

Adversario con reproducción del 3/3, verificación simbólica
independiente, 40 000 realizaciones del cuarteto (0 violaciones,
peor margen −4·10⁻¹⁶ = redondeo de tangencia), esquinas (Σ → 1⁺,
Σ = φ exacto, ω = 10⁶, holgura 10⁴, Σ_S = Σ) y 260k tuplas contra
`_lp4`.

### VEREDICTO: CONFIRMADO CON CORRECCIONES (con mejoras)

La fase 1 resiste el asalto completo y sale REFORZADA:

1. **[MENOR→MEJORA] El certificado queda 100% algebraico**:
   r(u) = φu² + 2(φ−1)u + (φ−1) — tres coeficientes POSITIVOS
   (r > 0 sin malla); g estrictamente decreciente (g′ = p′ − φ,
   sup p′ = p′(2/φ) < φ) con mínimo EXACTO g(φ) = (3−√5)/4 =
   φ/2 − 1/φ. APLICADO al script y draft.
2. [MENOR] El check «p creciente» era vacuo (disyunto falso +
   fallback trivial). REPARADO: p′·D² = 2u+1 exacto.
3. **[MENOR, relevante] El «margen 0.003» del punto peligroso
   j = 1 era ESPURIO**: con w* = 1/φ exacto el 4-ciclo suma 2π
   EXACTO (consecuencia de la identidad d2) — la variedad es
   exactamente tangente en el cierre, no «casi». REESCRITO.
4. **[GRAVE, fase 2] `_lp4` sin los caps de wrap** (d_i ≤ 2π−θ_i
   de los pares consecutivos): sin contraejemplo en 260k tuplas
   pero sin prueba; y el modo k = 4 del B&B no valida el par
   (otro, m) por el lado de chico. DOCUMENTADO como supersedido:
   el lema del LP de arcos (arcolp.py) INCLUYE los wraps (arcos de
   longitud n−1). El «sii» de _lp4 para las diagonales solas es
   CORRECTO (verificado con construcción explícita + 200k vértices).
5. [NOTA] Dos ramas en α explicitadas (u ≤ φ: q, g; α > φ:
   p(α) > p(φ) = φ/2 > topes). APLICADO (check con p(φ) = φ/2).
6. [NOTA] Menudencias (check(5) narrativo, parrilla R desde
   2/φ+1 exacto). APLICADAS.

**MEJORA MAYOR: la identidad d2 DEMOSTRADA en ℚ(√5)** (álgebra de
senos): √(x₁x₂(1−x₁)(1−x₂)) = (7√5−15)/5 es cuadrado exacto y
x₁(1−x₂)+x₂(1−x₁)+2(7√5−15)/5 = 1−x₃, con sin(A+B) = cos(C) sin
problemas de rama: θ(φ,1/φ)+θ(1/φ,1)+θ(1,φ) = π en R = 2φ es
TEOREMA. Añadido a Lean como (39) golden_pi_trio (kernel).

RESISTEN: la realización completa de los 6 pares (construcción
explícita, 40k instancias); la DIC en el par diametral SIN importar
zigzag (f(s)(f(α)+f(1)) = 1 en s = p, disc ≡ 0); dominio sin techos
de α; ligaduras conservadoras; extensión R > R_test (márgenes
crecen, ningún uso del bolsillo fuera de R_test); las esquinas
todas; el WIP de fase 2 vendido honestamente (salvo el 0.003).

### Estado tras reparación

`bolsillos.py` 3/3 (checks exactificados); `bolsillos.md`
reescrito (certificado algebraico completo, dos ramas, tangencia
exacta en §3); Lean 39. **El dominio j = 0 de thm:gapwritten es
TEOREMA ALGEBRAICO con tangencia áurea.**

---

## Acta: ronda hostil del lema del LP de arcos (`arcolp.md`) — 2026-08-09

Adversario con reproducción del 5/5, contraejemplos ejecutados,
clasificación completa de los «101 casos», contraejemplo LP puro a
la dualidad, verificación FD del gradiente y sondeo del LP completo
en V.

### VEREDICTO: REFUTADO EN SU ENUNCIADO — núcleo reparado (v2)

1. **[FATAL, H1] La π-gorra como REQUISITO aceptaba órdenes
   físicamente imposibles**: pr ≥ 1 ⟺ a+b ≥ R, y con a+b > R
   estricto el requisito real es +∞ (dos murales no son disyuntas a
   ninguna separación). Contraejemplos: [1.5, 1.5, 0.1] en R = 2
   (dual y primal True, corona_k5 False, solape material −2.0).
   REPARADO: precondición «pares caben» (a_i+a_j ≤ R, igualdad
   permitida — el caso áureo) como guarda en dual/primal/corona.
2. **[FATAL, H2] «Estrictamente más fuerte que corona_k5 en
   101/3000» era 100% artefacto de H1**: los 101 tenían pares
   imposibles; tras reparar, equivalentes 3000/3000. RETRACTADO:
   el valor del arc-LP es la caracterización SII con desigualdades
   cerradas + la forma LP, no potencia.
3. **[GRAVE, H3] La «dualidad LP estándar de matrices de
   intervalos» era argumento inválido**: los arcos CIRCULARES no
   son matriz de intervalos ni TU — contraejemplo puro (n = 3, tres
   arcos de longitud 2 con r = 1.5π: infactible por cobertura
   doble, invisible a familias disjuntas). REPARADO: el criterio
   oficial es el PRIMAL EXACTO por enumeración de bases; el dual
   queda como poda necesaria (coincide empíricamente en 9500+
   instancias bajo la estructura geométrica, sin prueba —
   declarado).
4. **[GRAVE, H4] El certificado de entorno tenía hueco lógico**:
   σ ≤ 0 no cubre las diagonales del 4-ciclo y la desigualdad
   triangular de θ es FALSA en parte de V (margen −0.098).
   REPARADO: el LP COMPLETO del 4-ciclo (primal exacto) sobre
   malla 13³ de V, 0 infactibles.
5. [MENOR, H5] El check del gradiente era True hardcodeado.
   REPARADO: los tres signos exigidos.
6. [RESISTE, H6] Gradiente verificado por FD (10⁻⁴); contabilidad
   de σ correcta (θ(α,o₁) = π por frontera legal, no fantasma);
   C/D/E no contaminados por H1 (el único par con suma = R es
   (φ,φ), igualdad exacta legal); tolerancias de tangencia bien
   puestas (10⁻¹² adverso rompe, m−ε mantiene); cobertura de
   órdenes correcta (12 = 4!/2); la necesidad sin el agujero de H1
   (en una corona genuina los pares caben automáticamente); el uso
   con cotas de esquina queda conservador TRAS la reparación (par
   inflado que no cabe ⟹ infactible, sin testigo en falso); paso
   de malla razonable (rugosidad ~1.55, cambio entre nodos ~0.01
   vs márgenes 0.42+).

### Estado tras reparación

`arcolp.py` 5/5 (guarda de pares, primal oficial, LP completo en
E, signos exigidos en D, bloque B como equivalencia);
`arcolp.md` v2 reescrito. **El lema v2 con precondición es
caracterización exacta; la lección para fase 2: las cotas de
esquina con la guarda son conservadoras — sin ella habrían
certificado en falso.**

---

## Acta: ronda hostil de bolsillos fase 2 (`bolsillos.md` §3) — 2026-08-09

Adversario con reproducción íntegra (números de caja exactos), 5
sondas (F cerrado vs LP exacto en 40k tuplas + 18 961 testigos;
grid 400² de R₃ vs M; colas; 9 000 instancias reales; malla
desplazada de V).

### VEREDICTO: CONFIRMADO CON CORRECCIONES

La maquinaria central RESISTE: F cerrado es caracterización sii
verificada sin una discrepancia (wraps de la lección H4 incluidos,
punto tangente F = 0 exacto); la unión bolsillo/ciclo sin hueco
(75k puntos); dominio_pares_ok legítimo (la π-gorra en esquinas
solo SUBE requisitos); 0 contradicciones en todos los muestreos.
Pero «dominios ENTEROS» era falso tal cual:

1. **[GRAVE] Colas del bloque E inexistentes** (piezas > 30 sin
   certificado). REPARADO: rama 1 verbatim de D; rama 2 con
   R = 1+x₁+x₂ y mejor bolsillo ≥ 1.1505 > φ/2 (9 esquinas, dos
   escalas), trío por suma de máximos 4.97 < 2π.
2. **[GRAVE] `trio_ok = True` hardcodeado**: la salvaguarda
   prometida era ficción y el «check exhaustivo» heredado es
   MUESTREO. REPARADO: v2-check ∨ guard R₃(hi) ≤ M(lo) en la banda
   ∨ exclusión W₂ del punto áureo del trío (2, 2/φ, Σ→1) Y SU
   ESPEJO (donde pares = R₃ = M colapsan y disc ≡ 0 da p₁₂ = 1
   exacto — la salvaguarda por esquinas nunca decide ahí);
   «exhaustivo» → «muestreado + grid 400²» en draft. El grid del
   acta confirma el hecho con margen muriendo solo en el punto
   áureo, y las violaciones REALES bajo el suelo o₁ < 2/φ.
3. **[GRAVE] Cola de D en la esquina FAVORABLE** (patrón E2): el
   bolsillo (g1,m) decrece vía R — ínfimo real 0.715 (no 0.968);
   sobrevive por +0.097. REPARADO (ínfimo en R → ∞, crecimiento en
   g1 verificado, simetría (α, o₁) escrita).
4. **[GRAVE draft] «Reducción GLOBAL de s′» falsa en la banda R₃**
   (el bolsillo real con −2√disc cae bajo φ/2 en una región; el
   código nunca la usaba — gate numérica correcta). REPARADO el
   §3.
5. [MENOR] «+0.1 = o(1)» injustificado → suma de máximos 5.74.
6. [MENOR] sup_ok/super-bolsillos de s′ ahora exigidos en todas
   las ramas.
7. [MENOR] El asterisco malla/tolerancias viaja con el enunciado.
8. [NOTA] R3_necesidad devuelve el extremo infactible (~1e-16,
   documentar); herencia k = 1 mecanizada; rama j = 0 muerta en
   _bnb_hibrido; el LP de la rama rara prueba un solo orden
   (completitud, no corrección).

RESISTE (verificado): la derivación de F (d₁ = π FORZADO, no
óptimo; diagonales correctas; wraps satisfechos — 40k tuplas, 0
discrepancias); la unión en w* (dicotomía puntual + esquinas
válidas sin monotonía); dominio_pares_ok y en_V; el hecho R₃ ≤ M
en dominio (rompe bajo el suelo: coherente con gaplemma); 9 000
instancias reales sin fallo; la venta honesta salvo «ENTEROS».

### Estado tras reparación

`bolsillos.py` 5/5 con salvaguardas reales, W₂ (+espejo), colas de
E, cola de D correcta, gates H6; `bolsillos.md` §3 v4. Los B&B
re-verificados con las salvaguardas: rama 1 k = 2 en 274k cajas,
rama 2 en 7.9k; j = 1 en curso con tope ampliado (la salvaguarda
honesta encarece la banda áurea).

---

## Acta: ronda hostil de la re-delimitación F3 (`f3cierre.md`) — 2026-08-10

VEREDICTO GLOBAL: REFUTADO como «cierre», rescatado como lema
condicional con dominio honesto.

Referee hostil sobre `f3cierre.py` v1 (4/4) + `f3cierre.md` v1.
Evidencia ejecutada (ataque reproducible, semillas 20260818/20260814).

### Derribos

1. **[GRAVE] Transferencia al dominio real FALSA**: el generador
   real del F3 (puertocii) produce instancias de gap cuyos tops
   tienen parejas APILABLES al radio exacto (3/3 medidas) — la
   hipótesis de no-apilabilidad del teorema falla en el 100% de las
   instancias reales de gap: «R_real ≥ R_arcLP(tops) es TEOREMA»
   NO cubre la celda F3 real. El «60/60 no apilables» era artefacto
   del generador sintético (ratio 0.9-1.0).
2. **[GRAVE] «≤ 1.030» refutado por la esquina del propio dominio**:
   4 tops 0.9 + 2 granos 0.55 da ratio 1.0816 (cadena diametral
   top-grano-top = 2.35 exacto); 3×0.9+2×0.55 da 1.0603. El gate
   1.05 del bloque B fallaba en la esquina de su propio dominio; 60
   muestras uniformes no la pisaron. Supremo real ≥ 8.2%.
3. **[GRAVE] Narrativa «1.0116 = dos cotas flojas» sin soporte**: en
   el dominio sintético las dos cotas viejas son TENSAS (R_lb sobre
   tops = radio exacto; R_fit = radio exacto 25/25); el check D(a)
   era True hardcodeado y lo medido (0/25 sobrestimaciones)
   contradecía su propio texto. El 1.0116 vive en el dominio real —
   donde el teorema no llega.
4. **[MEDIO] Justificación de granos falsa**: «un grano siempre es
   apilable tras un top» — contraejemplo: top 0.9 + grano 0.55 ⟹
   top+2·grano = 2.0 > R_ex = 1.939. La irrelevancia real es por
   borrado monótono.
5. **[MEDIO] Disciplina de lados/tolerancias**: enunciados de
   necesidad citaban el lado hi (suficiencia); banda ~1e-9 del
   primal con signo favorable-a-factible sin declarar (medida:
   True en R₃*−1e-10, False desde 1e-9); el déficit «~1e-10» del
   bloque D(c) está DENTRO de la banda.
6. **[MEDIO] n = 6 fuera del acta del arc-LP** (validado k = 3..5);
   deriva de definición del R_lb viejo (sobre carga, no sobre tops
   como puertocii); granos escalan por t0 (cociente hasta 0.61, no
   0.55).

RESISTE: la composición compactación∘arc-LP (dirección correcta:
orden heredado ⟹ mín sobre órdenes; monotonía en R), la sanity
clásica genuina (1+2/√3, 1+√2 en tangencia), la precondición
pares-caben en toda la bisección, la resolución 2⁻⁴² de la
bisección, la lógica de la dicotomía por instancia (R_ex vs M con
el lado seguro).

### Estado tras reparación (v2, 5/5)

Lema CONDICIONAL con dominio honesto: malla determinista de 16
esquinas (supremo 1.0816 certificado como esquina), R_lb viejo con
la definición de puertocii + vigilancia de ambos lados (tenso
60/60), D(a) con condición real (sobre == 0: narrativa retirada),
lados lo/hi separados + banda del primal declarada y medida en A,
bloque E nuevo: (e1) generador real reproducido — 3/3 instancias de
gap con tops apilables, el residuo 1.0116 PERMANECE con dos vías
declaradas; (e2) acta del arc-LP extendida a k = 6 (dual-y-primal
vs LP directo HiGHS, 60 sistemas 31/29, 0 discrepancias).

---

## Acta: ronda hostil de la multipieza R2b (`r2bmulti.md`) — 2026-08-10

VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES. La matemática entera
resiste (1460 tests dirigidos + end-to-end, 0 grietas de solidez);
las grietas son de enunciado y dominio.

### Derribos

1. **[OBLIGATORIA] El «dominio legal» de G-b′ era falso**: el techo
   Y ≤ 6.6 descansa en el tope de MUESTREO X_Y ≤ 3 de puertocii, no
   en una pared derivada — instancia legal exhibida con X_Y = 4,
   Y = 7.0 que pasa todas las paredes declaradas; y s2 = 0.9995
   legal fuera de la raíz [0, 0.999]. El draft vendía
   «superconjunto del dominio legal... TODO el dominio». REPARADO:
   s2 < 1 ENTERA (pared real, re-certificado 59/87/139 cajas) y
   enunciado reescrito como caja del barrido MC con X_Y > 3 y
   ω > 1.6 declarados FUERA.
2. **[OBLIGATORIA] «MARGEN = 1e-7 ≫ precisión ~1e-9 de HiGHS» era
   falso en la cifra**: la banda ~1e-9 es la del primal-por-bases;
   el error del objetivo de HiGHS en el max-t llega a +2.5e-8
   (medido: t_true = 5e-8 → reporta 7.5e-8) y 1e-7 es exactamente
   su tolerancia de factibilidad por defecto. REPARADO: la d
   devuelta se verifica en FLOAT PURO (_verifica_d: holgura ≥ 5e-8
   por arco, Σd = 2π, d ≥ 0; error float ~1e-15) — el certificado
   ya no descansa en el solver.
3. **[MENOR] Cita imprecisa**: f3cierre [E] validó el LP de
   FACTIBILIDAD, no el max-t. REPARADO en textos.
4. **[MENOR] Carga mal atribuida**: «habilitado por la validación
   k = 6» sugería depender de la caracterización k = 6; los
   certificados usan solo la SUFICIENCIA del arc-LP (válida para
   todo k). REPARADO en draft y docstrings.

### RESISTE (verificado por el referee)

Motor por término (monotonía acoplada verificada por tipo de par;
m fuera de la capacidad correcto en la tarifa DR; clamp s2_p sup
exacto; 400 cajas-punto sin violación; π-gorra inofensiva por
álgebra de pares). Criterio antipodal (exclusión de (Y,m) legítima
— ambos lados a π exacto con θ < π estricto por álgebra; sub-camino
≤ π automático; TU de intervalos aplica a max(Σθ_consec, θ_ext);
400 sistemas de camino vs LP, 0 discrepancias; end-to-end con
colocaciones construidas, 0 pares mal separados). Las dos UB de la
ESP (UB1 acoplada válida eslabón a eslabón; UB2 con cola clampada
válida; 6 podas exactas, 600 controles sin podas de puntos reales).
El aterrizaje ESP es limpio, no al límite: re-ejecutado a 2π−0.35
CERTIFICA (1863 cajas, cota 5.9331). Sin circularidad con r2bcert.
Controles negativos reales.

### Estado tras reparación (v2, 5/5)

G-b′ j ≤ 3 certificada sobre la caja del barrido con s2 < 1 entera
(59/87/139 cajas); ESP X > 0 (X_Y = 0) certificada (948 cajas, y
1863 a margen 0.35); verificación float de toda d certificante;
alcance honesto con los cuatro FUERA declarados.

---

## Acta: ronda hostil del lema de reducción de |A| (`areduccion.md`) — 2026-08-10

VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES. Cero grietas de
solidez: ningún camino por el que el certificado apruebe algo falso
(mayorantes verificados par a par en dirección pesimista;
colocaciones físicas construidas; ninguna poda traga puntos reales
— 600 puntos G-e + 400 G-g, 0 podados; dominios MC contenidos —
6553 instancias G-e + 5822 G-g pesada X=0, 100% dentro de las
raíces).

### Confirmado por el referee

El LEMA entero rehecho a mano (dicotomía en β* con estrictos
correctos; b_star_particion da exactamente la maximalidad usada;
a ≤ φ/2; 1312 perfiles adversarios en los umbrales, 0 violaciones).
El bloque de polvo (convexidad en la dirección correcta, igualdad
solo en la diagonal; cota independiente del orden; embedding
atómico sound; colocación física de una cadena de 14 piezas). El
antipodal de dos lados (tangencia θ(z,m) ≡ π en c′ = 1+z legítima
con desigualdades cerradas; pares cruzados entre semicírculos
dominados por los extremos). Los criterios de caja (podas exactas
una a una; cota acoplada con signo x(1−x) ≥ 0; clamps de masa
fantasma con los suelos correctos).

### Derribos/correcciones

1. **[OBLIGATORIA] Lado degenerado de _peor_camino**: con cadena
   vacía, el arco completo de un solo gap reintroducía el par
   antipodal «excluido» y exigía θ(0,1) ≤ π−margen — en la
   tangencia de G-g eso era False irresoluble, y el verde de D
   dependía del ACCIDENTE de que la bisección nunca anula un slot
   (89/400 puntos reales tangentes daban False estructural).
   REPARADO: cadena vacía ⟹ presupuesto 0 (el lado degenerado ES
   el par excluido).
2. **[REDACCIÓN] §5 sobrevendía G-g**: solo la rebanada X = 0 del
   MC pesado queda sustituida. REPARADO.
3. **[REDACCIÓN] «cajas» → «cajas vistas (certificadas + podas)».
   REPARADO.
4. **[RECOMENDADA] El orden MONÓTONO del polvo es carga real del
   argumento** (contraejemplo no-monótono [t₀, ε, t₀] viola pares
   saltados: sep 0.023 < θ 0.147) y solo vivía en un check.
   REPARADO en §2.
5. **[REFUERZO hallado por el referee] 4t₀ = φ−1 EXACTO ⟹
   |A_big| = 4 y polvo INCOMPATIBLES** (μ < 1−β < toda pieza de
   polvo): el mural real es ≤ 6 nodos. AÑADIDO al lema (iv) y como
   poda exacta en ambos B&B.

### Estado tras reparación (v2, 5/5)

Lema (i)-(iv) exacto en ℚ(√5) (candidato a Lean); bloque de polvo
con el orden monótono explícito; lado degenerado correcto sin
dependencia del accidente; G-e 501 cajas vistas / 109 certificadas;
G-g pesada X=0 re-verificada tras las reparaciones.

---

## Acta: ronda hostil de la variedad ESP X_Y > 0 (`espxy.md`) — 2026-08-10

VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES. El hallazgo central
sobrevive al asalto: álgebra exacta verificada A MANO (las seis
identidades), refutación sound y robusta (déficit 0.51 rad, no
marginal), región legal (réplica exacta de semilla + paredes
omitidas comprobadas post-hoc: 0 violaciones), protección áurea de
σ₂ real con margen (min z = 2.84 ≫ φ; 2M muestras, 0 puntos con
σ₂ > x*). La trampa gorda del encargo (fila de D_m vs (BH)) se
disuelve: D_m (hueco unidad en v, cap 1) y H_m (agujero propio de
m, cap 1−ω−X_m) son recursos distintos.

### Regalos del referee

- **x*(φ) = φ/2 EXACTO** — el mecanismo de la protección de σ₂:
  z > φ ⟺ x*(z) > φ/2 ≥ σ₂ (no el umbral difuso «z ≥ 1.9»).
- φ(3−φ) = √5 (el umbral de no-rescate en x = 0 es la constante
  de respiración fuerte).
- Barrido con ω libre: min z = 2.84, min ω = 0.906 en la zona sin
  rescate; la caja ω ∈ [0.9, 1.6] del generador era esencialmente
  exacta por casualidad.

### Correcciones exigidas (aplicadas)

1. (BH) y (Bσ₁) son paredes del BLOQUEO y el generador no las
   comprobaba (se cumplían por suerte estructural de la caja, 0/300
   violadas): añadidas por construcción.
2. C(c) era TAUTOLOGÍA (2z+2+2x > 2c′ ⟺ x > 0 con c′ = 1+z por
   construcción — gate que no puede fallar, E2 disfrazado):
   eliminado y reetiquetado como corolario trivial; texto roto de
   C(b) arreglado.
3. El «4/300» del draft era cifra huérfana (el script no lo mide):
   retirado; «300/300» anotado como dependiente de semilla (gate
   > 80%).
4. x*(φ) = φ/2 enunciado como el mecanismo (reparación 4).
5. Lado x ≥ 1 rebajado a MODEL-CONDITIONAL (pieza ≥ r_m fuera del
   convenio de X_Y = polvo < m; tarifa de cola sin derivar; banda
   finísima: 0.005 en z = 4).
6. Código muerto retirado (cabe_trio, rama xs ≥ 1); D-1 reetiquetado
   como malla orientativa sin gate ficticio.
7. Nota de alcance: la parte ω ≥ 1 de la variedad cae en régimen de
   pivote sólido (posible cobertura por DPr j ≥ 3, pendiente —
   reduciría la variedad a ω ∈ (0.9, 1)).

### Estado tras reparación (v2, 5/5)

La celda ESP X_Y > 0 pasa de «declarada fuera» a variedad peligrosa
DELIMITADA con frontera exacta: x* = p(z,1;1+z) = z(z+1)/(z²+z+1)
(el bolsillo del par diametral), anchura 1/(z²+z+1) (= 1/(2φ²) en
z = φ), no-rescate z+ω ≥ φ(3+x−φ) (= 3φ−1 en x = 1). Tres rutas de
cierre declaradas (simetría m↔x la más prometedora), nada hecho.

### Adenda al acta de espxy (2026-08-10, mismo día): la nota 7 resuelta

La «posible cobertura por pivote sólido/DPr» de la reparación 7
queda RESUELTA EN NEGATIVO (análisis con citas, agente lector):
D3 («pivote sólido ω ≥ 1, j ≥ 3») es una celda del CASO (a) —
intercambio de sartén — con j = ocupantes de la cascada de sartén
y m EN la sartén (coronacolas D3, líneas 575-602); el solid-pivot
del paper cuelga de thm:DP/thm:D1written (pan exchange) y de la
curva canónica (caso (b)); la partición (a)/(b)/(c) es disjunta y
DEFINICIONAL (ensamblaje: «exactamente uno») y la portabilidad de
programas de sartén está explícitamente prohibida (ensamblaje:
«portabilidad de paredes ≠ cobertura de programa» — el descenso
intrínseco exige cohabitación {o₁, m} en la sartén). En (c-ii),
ω ≥ 1 es donde VIVE el residuo (R2 con X = 0: ω ∈ (0.927, 1) ∪
[1, ∞)) — nunca se delegó. El pivote sólido además ayuda al
adversario: mata H_m (X_m = 0) y la colocación BH, con D_m
intacto. La variedad completa ω ∈ (0.906, 1.6] queda ABIERTA.
Colateral: la variedad es el corazón de la rama I2 «que respira»
(X_Y+ω > φ, cierre que era solo-computacional — coherente con que
espxy la rompa); herramientas portables para la ruta m↔x:
lem:compact/lem:insert (disco arbitrario) y el precedente
corona-α; el receptor natural de x es la SARTÉN vía el lema F2 de
realización-y-repack (u = agujero de α no puede: su techo de
bloqueo α < 1+σ₂+X_α+ω no admite m+x ≈ 2).

---

## Acta: ronda hostil del vals de las bolas vacantes (`espvals.md` v1) — 2026-08-10

VEREDICTO GLOBAL: REFUTADO, con tres derribos independientes y una
ERRATA al acta archivada de espxy.

1. **[FATAL] El vals no está licenciado por F2**: el lema da por
   contenedor O el recurso posicional (bolas vacantes sobre la
   realización de P) O el certificado fresco (fila/corona que la
   SUSTITUYE) — el vals exigía ambos en v (x → D_m + σ₁ → bola de x
   + trío fresco): en modo certificado la bola de x muere con el
   repack (σ₁ sin casa: x+σ₁ > 1.41 > 1 siempre); en modo
   posicional σ₂ necesita inserción con presupuesto de sombras sin
   derivar. La propia silla (iii) del draft enunciaba el principio
   que lo mata.
2. **[FATAL] La variedad entera es ILEGAL bajo ρ ≤ φ**: la cola
   GLOBAL de m incluye las X_Y (ΣS+X_m+ΣX_Y ≤ φ); la variedad
   exigía ΣS > 1 y x > 0.91: ΣS+x > 1.91 > φ. Medido: 400/400
   (espvals B), 250/250 (núcleo) y **300/300 del acta de espxy**
   (mínimo 1.96). ERRATA: los «300 puntos legales» de espxy no lo
   eran; su referee dirigido comprobó las paredes listadas y nadie
   miró cola(m) — evidencia directa para la ronda final ciega.
3. **[FATAL] Rigidez del suelo**: en c′ = 1+z el par (z,m) es
   tangente rígido y el hueco máximo de v es exactamente x*: P
   mismo es infactible con x > x* en v — la obligación «corona con
   x» era fantasma (cp = 1+z exacto en el 100% de lo muestreado).
4. [MENOR] ω ∈ [1.003, 1.6] del núcleo era artefacto de semilla
   (ω_min = 0.970 con 2000 puntos); la atribución del
   estrangulamiento a cola(z) sola, incorrecta (~0.60 analítico);
   sillas (vi)-(viii) sin listar; «97%» y rango de ω sin gate.

### Estado tras el acta (v2, 5/5)

`espvals.py`/`espvals.md` REESCRITOS como el documento de la
VACUIDAD: la pared cola(m) global (incompatibilidad exacta
ΣS+x > 1.91 > φ), la rigidez del suelo (tangencias numéricas a
1e-8 confirman hueco = x*), y la CONSECUENCIA POSITIVA: toda X_Y
legal ≤ φ−ΣS < 0.618 < x*(z) en todo el dominio — sub-bolsillo
universal: la celda ESP X_Y > 0 ligera se cierra por vacuidad +
inserción (certificación k-piezas pendiente declarada). El álgebra
de espxy sobrevive como geometría (Lean 40-41). Lecciones: colas
globales en toda legalidad de adversario; existencia de P en los
suelos rígidos; los dos modos de F2 no se mezclan.

---

## Acta: ronda hostil de la auditoría de colas globales (`auditcolas.md` v1) — 2026-08-10

VEREDICTO GLOBAL: REFUTADO — la meta-auditoría cometía el error que
auditaba (cola PARCIAL en reclamos de existencia). Aplicado su
propio estándar completo, el resultado principal se INVIERTE a más
fuerte.

1. **[FATAL] «La cota inevitable es cola(m)» era falso**: toda cola
   de pieza ≥ m es igual de inevitable (tracked menores + masa
   total del polvo) y son las DOMINANTES: matan 30/30 gaps del F3
   real donde cola(m) mataba 15/30. Además la banda de X ≥ 1
   (anillo único fuera de cola(m); GAP#25 exhibido) y los dos
   cierres del escape de granularidad bajo m (pigeonhole de masa,
   confinamiento) faltaban.
2. **[FATAL] El F3 real: 0/30 testigos legales** bajo legalidad
   entera (peor cola de top 2.89-3.60 vs φ; el «2/3» del v1 era
   artefacto de muestra 3 — la misma enfermedad que el «≤ 1.030»
   ya refutado en el acta de f3cierre). MECANISMO ESTRUCTURAL (el
   trío prohibido): tres piezas con las dos siguientes ≥ (φ/2)·
   mayor violan ρ ≤ φ (2·(φ/2) = φ exacto); el gap de dualidad
   exige ≥ 3 tops de ratio 0.9 > 0.809: gap y ρ ≤ φ incompatibles
   en el generador. EL RESIDUO F3 REAL ES CANDIDATO FUERTE A
   VACUIDAD → errata a f3cierre §3-4 y al pasaje del paper; el
   1.0816 sintético queda como enunciado abstracto del arc-LP.
3. [MEDIO] Titular infalsable (gate gap_total ≥ 3 no gateaba la
   conclusión — patrón E2); 6/7 checks [ENUNCIADO] con True;
   banda de X_α sin declarar (coronaagujero L105: contexto).
4. RESISTE: la clasificación suficiencia-vs-existencia (G-b′ sound
   confirmado; R2/B1b pre-cierre confirmado, las 581 instancias no
   viven en el paper; ω es anchura, no pieza).

### Estado tras reparación (v2, 5/5)

Criterio v2 con las colas de piezas ≥ m + pigeonhole +
confinamiento + banda X ≥ 1; lema del trío prohibido (φ/2 otra
vez); B re-ejecutado a 30 gaps con legalidad entera: 0/30
(reproducido: 36.384 instancias, peor exceso 1.75) con gate
gap_legal == 0; consecuencias y deuda declaradas (el cierre formal
de la vacuidad F3 = ciclo propio).

---

## Acta: ronda hostil de la vacuidad F3 (`f3vacio.md`) — 2026-08-10

VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES. El núcleo sobrevive
todos los ataques ejecutados (~11.000 instancias adversarias),
incluidos los dos críticos del encargo: el CONFINAMIENTO no sube
R_lb sobre pares EN la celda (100% de 5.300+ instancias, suma
cíclica confinada máx 4.02 < 2π; γ₁₂ = π exacto por la esquina
h = −1), y las terceras piezas < m dan 0 gaps (1.500 instancias).
El álgebra es exacta (disc = 0 en R = a+b; p(a,ra;(1+r)a) = q(r)a;
q = r·x*(1/r); cúbica áurea con r* = 0.963749; identidad
θ₁₃+θ₂₃ = π a 3.6e-15).

### Derribos/correcciones (aplicadas)

1. **[GORDA] El dominio declarado «α ≤ ~5.1» era FALSO**: el techo
   real del generador es α ≤ 6.64 (réplica del loop de puertocii,
   12.112 instancias; ub_a con ω inflada por X_Y). No rompe el
   lema (techo 23 > 6.64) pero sí el alcance y el margen (3.46×,
   no «> 4×»). REPARADO en todos los textos.
2. El bloque C cubría la mitad del rango (t₁ ∈ [4.57, 5.10] de
   facto) y no muestreaba t₃ < m ni 4 tops. REPARADO: t₁ hasta
   6.7, modo chico (232/600), 4 tops (19/600); 0 gaps en todo.
3. El argumento de t₄ del bloque D usaba la premisa falsa (5.1):
   la pared que realmente fuerza polvo es cola(t₃): t₄ ≤
   φt₃−1−ΣS, válida a toda escala. REPARADO.
4. r* = 0.963749 (el comentario decía 0.9639); tolerancia
   apretada a 1e-5. REPARADO.
5. **La frontera 0.9 de la celda es EMPÍRICA** y el converso
   «gap ⟹ celda» queda ABIERTO — con la evidencia a favor: fuera
   de la celda (r₂ ∈ 0.60-0.90) hay t₃ legales sobre el bolsillo
   (hasta 1.24×) pero ahí el confinamiento SUBE R_lb (hasta
   1.0126) y corona_suf cabe en el R_lb subido: 0 gaps en 5.100
   instancias. DECLARADO en §3.
6. Gates: el bloque B ahora exige techo > 6.64; C gatea los modos.
7. El retiro del 1.0116 se sostiene TRAS aplicar 1-6 con esta
   acta. APLICADO (paper actualizado).
8. Colateral: clamp del disc en bolsillo_descartes de coronacolas
   (devolvía 0.0 en ~38% de pares diametrales exactos, conservador
   pero infiel). REPARADO; humo de coronacolas en verde.

### Estado tras reparación (v2, 5/5)

La celda F3 es ρ-VACÍA por las dos pinzas (trío prohibido +
sub-bolsillo forzado con techo 23 vs dominio real 6.64); el
residuo 1.0116 RETIRADO del programa; convenio de alcance honesto
(0.9 empírico, converso abierto, bandas fuera de vía declaradas).

---

## Acta: ronda hostil de la certificación k-piezas (`espkp.md`) — 2026-08-10

VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES. Cero grietas de
solidez dentro del convenio X_Y = polvo < m: podas exactas
(verificadas una a una), mayorantes en dirección pesimista, cota
acoplada con el signo correcto (d/dz ∝ x(1−x) ≥ 0 con la fórmula
real; el ruido float ~6.7e-8 en x = 1 es inocuo: thmat[0][1] es
entrada muerta del par antipodal excluido), bloque de polvo
CAP-GENÉRICO re-fuzzeado con el tope grande (cap = μ ≤ 0.618:
0/6000; el contraejemplo no-monótono reescalado sigue violando: el
orden monótono sigue siendo carga real), B&B convergente y
reproducible (1329/483 exactos), sanity robusto a semilla (3 ×
250/250; ~23% por corona_suf con dirección solo-suficiente
correcta; 0 piezas sobre-bolsillo en 750). Ventanas idénticas a
r2bmulti bloque D (adversariado) con μ como única novedad.

### Correcciones exigidas (aplicadas)

1. **[OBLIGATORIA, declarativa] El convenio no estaba declarado**:
   el cierre es cierre-DENTRO-del-convenio X_Y = polvo < m; el
   canal «ocupante ≥ r_m en v» es MODEL-CONDITIONAL con tarifa sin
   derivar (acta espxy corr. 5, banda X ≥ 1 de auditcolas) y el
   «queda CERRADA» en plano sobrevendía un epsilon. REPARADO en
   bloques A/E y draft.
2. **[RECOMENDADA] Control negativo del CERTIFICADOR** (no solo de
   la poda): añadido — bloque con D = 4 > π → False y matriz
   estrangulada (θ ≡ 2.5) → False.
3. **[RECOMENDADA] Orden monótono heredado + derivación
   cap-genérica**: explicitados en A y draft con el fuzz del acta.
4. **[MENOR] Código muerto**: CC_ITER sin uso en espkp (retirado);
   `talla()` con T0 hardcodeado en areduccion._peor_camino —
   TRAMPA LATENTE si se reviviera con topes ≠ t₀ (retirada; humo
   de areduccion A/C en verde).
5. **[MENOR] Redacción**: «EXACTAMENTE el mural de areduccion» →
   «comparte la forma»; término redundante z+μ+ω retirado de lo_Y.

### Estado tras reparación (v2, 5/5)

LA CELDA ESP X_Y > 0 LIGERA CERRADA DENTRO DEL CONVENIO (vacuidad
de espvals + certificado k-piezas con k libre); el canal ≥ r_m y
la pesada con X_Y > 0 declarados como residuo con vía.

---

## Acta: ronda hostil de la pesada especular con X_Y > 0 (`esppesada.md`) — 2026-08-16

VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES. Cero grietas de
solidez: las direcciones pesimistas de los tramos (crédito del
suelo/techo del tramo, pinza vacua EXACTA), la fusión de bloques
(cadena por masa cap-genérica), el pliegue con OR de variantes y
la pared pesada verificadas a mano; 5/6 bandas re-ejecutadas con
recuentos EXACTOS (la sexta, verde por el coordinador, 19809/3535);
400 cajas-punto de instancias reales: True 400, None/False 0; el
sanity REPARADO (con A-polvo) no destapa nada (2×200/200).

### Hallazgo del referee

**La frontera ΣS = 1+σ₂ exacta es VACUA**: S∖{σ₂} suma exactamente
1 ⟹ b_star_particion da β = 1 ⟹ ventana de α = [ΣS+ω, ΣS+ω) = ∅ —
la unión espkp (ligera, ΣS < 1+σ₂) ∪ esppesada (pesada, poda
SSh < 1+s2l) cubre la especular con X_Y sin hueco: la frontera no
tiene puntos.

### Correcciones exigidas (aplicadas)

1. **[OBLIGATORIA, fidelidad] bloque_C**: muA era código muerto —
   la carga del sanity NO llevaba el A-polvo que la puerta
   anunciaba. REPARADO (apolvo en la carga; verde).
2. **[OBLIGATORIA, texto] «4 tramos» → «8 tramos»** en el
   comentario del criterio y la puerta de bloque A (K = 8 en el
   código). REPARADO.
3. **[RECOMENDADA] bloque_D al estándar espkp**: añadidos la
   matriz estrangulada y el negativo de la poda pesada (caja
   ligera → None). REPARADO.
4. **[RECOMENDADA, draft]** clip ΣS ≤ φ−0.02 del generador
   declarado; la vacuidad de la frontera anotada. REPARADO.
5. **[MENOR]** D(b) computado en vez de enunciado; tolerancia
   1e-15 del pliegue inocua frente a MARGEN (documentada aquí).

### Estado tras reparación (v2, 5/5 con B por unión de bandas)

LA CELDA ESPECULAR ENTERA cerrada dentro del convenio en sus
cortes/cajas declarados: ligera X_Y = 0 (r2bmulti), ligera
X_Y > 0 (espkp), pesada X = 0 (areduccion), pesada X_Y > 0 (este,
corte X_α = X_z = X_m = 0). Residuo especular: pesada con
X_α/X_z/X_m > 0 (solo-MC), canal ocupante ≥ r_m
(model-conditional), topes del barrido. Lecciones de ingeniería
del ciclo: renuncia POR TRAMOS (la total crea tangencias fantasma
donde la cola del parámetro renunciado era el rescate), pliegue
con OR (plegar piezas medianas duplica su coste), y la pared del
sub-caso como poda (no re-certificar caro lo que otro certificado
ya cubre).

---

## Acta: ronda hostil de espfinal (la especular completa) — 2026-08-18

VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES. Una grieta de
solidez real y ACOTADA, una regresión de fidelidad conservadora y
discrepancias declarativas; el resto del criterio v5 verificado en
dirección pesimista término a término. Evidencia: F a tres ε₀
(85/43, 83/42, 75/38), 4/6 bandas B re-ejecutadas con recuentos
EXACTOS (DFS determinista), fuzz del greedy partible 20.000
multiconjuntos (0 violaciones), fuzz de β con σ₁ bajos que el
oficial no cubría (0/4000, peor 0.9964), contraejemplo DP del cap,
negativos del motor nuevo.

### La grieta (R1, reparada)

**El cap del bloque F**: «piezas de A ≤ σ₂ ≤ ε₀» era FALSO — σ₁
puede quedar EXCLUIDA de B* y caer en A con ε₀ < σ₁ ≤ ΣA ≤ 2ε₀
(contraejemplo DP exacto del referee: 66×0.015 + 0.008 + σ₁ =
0.0171, el óptimo único deja σ₁ fuera). cap = max(ε₀, μ_Y)
sub-mayoraba. REPARADO: cap = max(2ε₀, μ_Y) — impacto numérico
NULO (B&B idéntico 85/43, verificado por el referee antes de
exigirlo).

### Confirmado

Pared del polvo total (X_α/X_z en la cola de m dentro del
convenio; podas con suelos = mínimos). Bloque partible: el greedy
|m₁−m₂| ≤ cap es TEOREMA (invariante d′ ≤ cap por inducción);
sub-bloques M/2+cap/2 mayoran; dos bloques en un lado sound.
X_m/X_z sin dimensión (monotonías verificadas). β ≥ 1−ε₀ TEOREMA.
Holguras ε₀ pesimistas (a_hi con un ε₀ de sobra). Empalme exacto
F∪B en 1.016 (IEEE). Mapa sin huecos. Sanity 200/200.

### Correcciones (R2-R5, aplicadas)

R2: «K = 8»/«KZ = 4» de los textos vs K = 4/KZ = 2 del código (la
enfermedad de esppesada corr. 2, invertida). R3: negativos del
motor nuevo _antipodal2 añadidos al bloque D (D = 10 → False,
estrangulada → False). R4: clip ΣS ≤ φ−0.05 del sanity declarado;
el lado vacío de _peor_camino2 documentado como CONSERVADOR
DELIBERADO (no porta la guarda de areduccion — solo endurece — y
portarla invalidaría los recuentos del mapa). R5: _THMAT global
documentada (uso interno, se asigna antes de todo uso, sin
threads; smell de la clase talla(), no agujero); constancia
0.004 → 75 cajas (el 63 histórico era de una versión previa).

### Estado tras reparación (v2)

LA CELDA ESPECULAR COMPLETA CERRADA DENTRO DEL CONVENIO: ligera
(r2bmulti + espkp) y pesada (areduccion + esppesada + espfinal)
con todas las X de polvo en todo su rango legal — la pared del
polvo total retira los topes de muestreo X_α ≤ 1.5 / X_z ≤ 1.
Mapa: F (1, 1.016] × TODO en 85 cajas (reducción de degeneración,
14 dims → 4) + seis bandas B ~32.100 cajas. Residuo especular: el
canal ocupante ≥ r_m (model-conditional) y ω ≤ 1.6 (tope de
barrido). Técnicas exportables: pared del polvo total, dimensiones
eliminadas por monotonía/tramos con crédito, bloque de polvo
partible (pesos por nodo), reducción de degeneración.

## Acta: revisión de la cirugía del párrafo-residuo (`residuo.md` + paper) — 2026-08-18

**Veredicto: CONFIRMADO CON CORRECCIONES** (ningún hallazgo
bloqueante). Ciclo editorial, no matemático: el párrafo-residuo de
app:campaign (~210 líneas de crónica con el residuo enterrado) se
parte en «The multipiece campaign and the vacuity closures»
(crónica) y «The honest residue» (inventario de cinco ítems);
draft transversal nuevo `residuo.md`. El revisor trabajó con
criterios de rigor sin líneas de ataque dirigidas (ensayo del
formato de la ronda final ciega).

### Hallazgos (aplicados)

1. (corrección) El residuo perdía el ítem del carácter
   computacional (written-proof pendiente), que op:assembly sí
   mantiene → cláusula final añadida con \ref{op:assembly}.
2. (corrección) «exact over its declared box» sobredeclarado
   (exacto = ℚ(√5)/TU en el vocabulario del paper) → «rigorous»;
   ídem en el draft.
3. (corrección) Ítem (iii) confundía talla con masa: el convenio
   es POR PIEZA (< r_m); las masas las acota la cola global →
   reescrito en paper y draft.
4. (corrección, PREEXISTENTE de 38bc392) Paréntesis huérfano en la
   crónica: «over their sweep boxes (the direct one entirely;…»
   nunca cerraba (verificado por balance programático de toda la
   región) → «(» sustituido por «--».
5. (cosmético) Costura de los topes colgaba de la frase de la
   celda X_Y > 0 → «the caps of the sweep boxes themselves remain
   sampling ceilings».
6. (cosmético) Fragmento sin verbo en la costura de los scripts F3
   → «The scripts … passed adversarial rounds».
7. (cosmético) «a vacuity under the global tail» sobre-específico
   (hay vacuidades por β = 1, por trío prohibido, geométricas) →
   «a vacuity» a secas.
8. (anotado, deliberado) «substantially certified» → «are
   certified»: el único cambio de fuerza real; justificado porque
   todo lo que cubría el «substantially» vive ahora como ítems
   (ii)-(iv) del residuo.
9. (cosmético, draft) Etiqueta del asterisco → [abierto / tope];
   nota de frontera empírica 0.9 en la entrada F3 de §2.

### Verificaciones positivas del acta

Barrido de la crónica por hedges: todo sampled/MC/open/empirical
aterriza en algún ítem (i)-(v). El residuo pesado pre-espfinal ya
no es residuo (espfinal lo cerró; el diff lo confirma commiteado).
\ref{app:verifmap} resuelve; números idénticos al texto viejo y
consistentes con op:assembly y el verifmap. Paréntesis de toda la
región editada balancean a cero tras la reparación 4.

### Estado tras reparación (v2)

El inventario vivo del programa entero, en cinco ítems: (i) la
dirección j de la escala (j ≤ 9 pan / j ≤ 8 nested); (ii) los
topes de barrido (ω ≤ 1.6 especular, X_Y ≤ 3 del motor, extras
coronas en sus rangos); (iii) el canal ocupante ≥ r_m
(model-conditional, único épsilon MC de la especular); (iv) los
enunciados abstractos del arc-LP de F3 + frontera 0.9 empírica +
converso abierto; (v) el asterisco de optimización fuera de los
shadow budgets. Más la dirección declarada: sustituir los
certificados computacionales por pruebas escritas (op:assembly).
Paper 50 pp, 0 referencias sin resolver.

## Acta: ronda hostil del canal ocupante ≥ r_m (`espcanal.md`) — 2026-08-18

**VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES** — cero grietas
de solidez en lo certificado, y EL HALLAZGO DEL REFEREE INVIRTIÓ
EL RESIDUO: la «lámina del gemelo» V* que el ciclo declaraba
como residuo es VACÍA, y el reclamo honesto resultó MÁS fuerte
que el del draft. Referee con criterios de rigor sin líneas de
ataque (formato de la ronda ciega). Recuentos re-ejecutados
EXACTOS (banda alta 79.277/19.977/0; sanity; controles), sondas
propias del referee (negativos de los certificadores nuevos,
auditoría de wrap del creciente: 39.919 llamadas, 0
certificaciones con span > π).

### El hallazgo central (R1, aplicado)

**LA VACUIDAD DEL GEMELO**: el convenio de primera copia hace lo
contrario de lo que el v1 le atribuía — «the tail of a ring
collects all later copies»: con x = r_m exacto, la cola de la
PRIMERA copia recoge a la otra copia MÁS S y el polvo:
1+ΣS+X > 2 > φ con la pared D. Bloqueo + ρ ≤ φ excluyen el
empate ⟹ V* = ∅ y la banda muerta es [1, 2/φ) CERRADA (pinza
unificada). El mismo movimiento del hecho (2) de thm:DBpp y
cor:DV34. Los 22 puntos «de la lámina» del sanity v1 eran
instancias ρ-ilegales (el generador no imponía la cola del
gemelo): la «auto-confirmación» era artefacto — reescrito como
CONTROL de la vacuidad (98/98 violan).

### Lo verificado sin hallazgo (positivo)

Las dos paredes del nodo son TEOREMAS (desbloqueos completos
movimiento a movimiento contra lem:DR/lem:row/lem:DG/
thm:oblivious; greedy pesado con σ₁ ∈ A y partición completa);
pinza de la cola de x conservadora; pooling 27 exhaustivo con
huecos simultáneos (contenedores disjuntos) y atomicidad
conservadora; necesidad del creciente con monotonías en la
dirección correcta y memoización a la baja legal; suelo_trio
cota inferior genuina (clava 1+2/√3 a 1.1e-13); podas del B&B
paredes verdaderas con esquinas pesimistas; acoplo
th(x,b,z_lo+x_eff) cubierto por A5; cobertura sin huecos entre
bandas (solapes 1.05 < 1.236, 3.227 > 3.217); Z_MAX cubre el
techo Rz+x por álgebra ajustada (z < 1+σ₂+3ω+φ ≤ 8.227).

### Correcciones (aplicadas)

R1: la vacuidad del gemelo (pinza extendida al empate en ambos
criterios; A9 reescrita: CANAL LIGERO CERRADO ENTERO; sanity
con control 98/98; D(c) empalme por vacuidad; draft/docstring/E
sin lámina). R2: «bloque B2» inexistente y contradicción
A6-vs-A7 (la pesada SÍ tiene pared derivada) — alineados. R3:
«x-en-z entera» era solo PROFUNDIDAD 1: la banda [1.236, techo)
en torres d ≥ 2 queda DECLARADA (pinza y pared del nodo son
posición-independientes). R4: guard de wrap en _creciente_cabe
(la cuerda crece con el ángulo solo hasta π; empíricamente
gratis). R5: negativos de los certificadores nuevos añadidos a
D. R6: comentario de la pinza sobredimensionado corregido. R7:
X_INF retirado; álgebra de Z_MAX anotada. R8: conteos del draft
y nota del muestreo del sanity.

### Estado tras reparación (v2, 5/5)

LA TARIFA DEL CANAL DERIVADA (dos paredes del nodo, teoremas) y
EL CANAL LIGERO x-EN-v Y x-EN-z (d = 1) CERRADO ENTERO, SIN
RESIDUO — el candidato a lámina resultó otra vacuidad de
frontera. Declarado: pesada con x (pared A7 derivada;
certificado = fusión con espfinal), banda [1.236, techo) en
d ≥ 2, x-en-u (exclusión estructural), k ≥ 2, ω ≤ 1.6. Técnicas
exportables: pared del nodo, pooling del polvo, lema del
creciente (nec+suf), pinza de la cola de x con empate.

## Acta: ronda hostil de la pesada del canal (`espcanalp.md`) — 2026-08-19

**VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES** — cero grietas
de solidez en lo certificado; dos hallazgos obligatorios de
inventario/fidelidad, ambos aplicados (H1 se resolvió CERRANDO lo
que faltaba, no declarándolo). Referee con criterios de rigor sin
líneas de ataque; recuentos re-ejecutados EXACTOS ([1.2, 1.4]:
26.125/8.644 del mapa v1); sondas propias del referee: fuzz del
teorema de reducción 0/20.000 (peor β = 0.5095 — la poda β > 1/2
es ajustada de verdad), monotonía de la cota acoplada de x
0/4.000, no-tautología (criterio(raíz) = False), 40/40
cajas-punto legales.

### Lo verificado sin hallazgo (positivo)

LA REDUCCIÓN DE DIMENSIÓN ES TEOREMA: toda pieza de A ≤
min(β, φ/2) — β ≥ σ₁ ≥ max(A) INCLUSO con σ₁ ∈ A (la duda de
espfinal R1: {σ₁} es candidato a B* con σ₁ < 1), y a ≤ φ/2 por
maximalidad (β+a > 1) + ΣS ≤ φ (ΣS ≥ β+a ≥ 2a). Esquinas
pesimistas en los tres usos del cap; el bloque fusionado A+μ_Y
mayora ambas familias; el greedy partible cap-genérico. Poda
β > 1/2 exacta. Pared pesada del nodo con esquinas correctas.
Ventanas y colas pesimistas término a término; suelo del trío
cota inferior legítima; frontera ΣS = 1+σ₂ sin hueco con
espcanal (el empate lo cubre este script). Cota acoplada de x
con zl (más pesimista que z_lo: cuesta fuerza, nunca solidez).
Sanity con gate real.

### Hallazgos (aplicados)

H1 [OBLIG]: la pesada x-EN-z (d = 1) no estaba ni certificada ni
declarada (espcanal la cerró solo en ligera; este script solo en
v) → CERTIFICADA: criterio_pesada_z nuevo (corona de v sin x — x
viaja dentro de z —, ventanas de z corridas, cola de Y con x):
15.571 cajas, dominio entero, 0 sin resolver. H2 [OBLIG]: la
banda alta del mapa etiquetada [1.4, φ] pero barrida con techo
1.62 (10.921/2.255 reproduce con 1.62, no con φ) → etiqueta real
[1.40, 1.62] en draft. H3 [REC]: negativo dirigido del
certificador nuevo (no-tautología: raíz de banda → False) + la
derivación del creciente con cap < masa anotada. H4 [MENOR]:
«suelo fino» 1−bh es más débil que el teorema β > 1/2 — 
terminología corregida; el clamp se conserva (recuentos). H5
[MENOR]: el sanity generaba X_z DESPUÉS de x (la pinza no veía
todo el polvo) → X_z antes. H6 [MENOR]: Xzh muerto (herencia de
espfinal) — anotado.

COLATERAL de la reparación H1: al certificar la pesada-z apareció
una región atascada (β ≈ 0.81, masa_A ≈ 0.26: el cap min(β, φ/2)
= 0.809 era pesimista de más) → EL CAP FINO min(β, φ/2, ΣA)
(exacto: una pieza no excede la masa de su multiconjunto), que la
disolvió; mapa v RE-BARRIDO CONGELADO v2 entero con el criterio
final: [1.0, 1.05] 51.713/11.924; [1.05, 1.1] 38.173/8.656;
[1.1, 1.2] 20.377/7.339; [1.2, 1.4] 23.169/7.822; [1.4, 1.62]
10.905/2.248 — total 144.337 + 15.571 (z), todo 0 sin resolver.

### Estado tras reparación (v2, 5/5)

EL CANAL OCUPANTE ≥ r_m CERRADO EN EL CONTENEDOR DE Y (v y torre
d = 1) EN AMBOS PERFILES. Declarado: banda [2/φ, techo) en torres
d ≥ 2, x-en-u (exclusión estructural), k ≥ 2, ω ≤ 1.6. Técnicas
exportables: reducción de dimensión por pago-por-masa de la
partición entera (β sola, cap = min(β, φ/2, ΣA)), poda β > 1/2.

## Acta: ronda hostil del converso «gap ⟹ celda» (`f3converso.md` v1) — 2026-08-19

**VEREDICTO GLOBAL: REFUTADO** (como «cierre en forma exacta»),
por dos vías independientes del referee (criterios de rigor sin
líneas de ataque):

1. **[FATAL] El detector de la vía (ii) era VACUO para n ≥ 4**:
   consumía `arcos(n)` = (inicio, LONGITUD) como extremos (i, j);
   la tupla (1,1) daba θ(x, x) > tol siempre ⟹ True. El barrido
   central «1.266/1.266 TODAS en la celda» era INFALSABLE (y el
   único negativo del detector usaba n = 3 — el único caso donde
   el bug podía devolver False).
2. **[FATAL] El teorema v1 era FALSO tal cual**: su (i) solo
   miraba pares apilables con t₁, pero el complemento que G2/G3
   necesitan es «NINGÚN par apilable». 4 contraejemplos reales
   del propio generador (re-barrido honesto del referee, 500
   familias/147 gaps): F = [1.1203, 0.9373, 0.7599, 0.5355,
   0.5182] (gap 2.21e-2; (0.9373, 0.5182) apilable),
   [2.2706, 1.6876, 1.3831, 1.3029, 0.949] (1.6e-2),
   [1.2382, 0.7896, 0.7487, 0.7301, 0.7277, 0.5954] (1.1e-2),
   [1.5402, 0.8766, 0.7555, 0.6356, 0.6135, 0.5667] (1.1e-3).
3. [FATAL, consecuencia] Los reclamos de [C]/[E]/§4 caían; la
   ANATOMÍA estaba invertida (la dominante es la APILABILIDAD —
   143/147 vía t₁ + 4 vía par no-top — no «la pareja lejana»).
4. G3/(ii) mal anclados: deben vivir en R_mid ∈ (R_lb, R*) sobre
   el orden de suma cíclica mínima — y ASÍ SON DEMOSTRABLES
   (derivación del referee: sin apilables γ_min = θ_w exacto;
   sin dominación el sistema son cajas factibles: contradicción).
5. G2 promovible a TEOREMA por cajas (n = 3: factible ⟺ Σθ ≤ 2π).
6. A1 «simbólica» era puntual (5 puntos); las formas cerradas
   globales existen (residuo 0).
7. A2 fuera de su dominio muestreado (a/R hasta 0.75 requerido) y
   a A4 le faltaba la disjunción con no-vecinos (sale de
   t ≤ a_min; la desigualdad triangular de θ es falsa — arcolp
   H4) y la muralidad del bolsillo.
8-11. B sin pelado múltiple; D(a) con otro generador y NameError
   latente; «discrepancia 0.00» sobreleída y banda (1e-9, 2e-6]
   sin declarar; caso |N| = 2 sin cubrir.

**Lo que sobrevivió**: la solidez direccional (R_lb ≤ R_real ≤
R_arclp; el confinamiento nunca crea gap — esquinas de gamma_min:
para no-apilables γ_min = θ_w con CUALQUIER dmin); la definición
de apilable (= vacuidad γ = 0); G1 por contención; y LA VÍA DE
RESCATE derivada por el propio referee: celda (i′) ∃ par apilable
CUALQUIERA ∨ (ii′) dominación en R_mid — 147/147 gaps del
re-barrido en (i′). Nota de proceso: el 5/5 en verde era
estructuralmente incapaz de detectar los fatales — el gate de
(ii) no podía fallar.

## Acta: RE-RONDA del converso (`f3converso.md` v2) — 2026-08-19

**VEREDICTO GLOBAL: CONFIRMADO CON CORRECCIONES.** Las 11
reparaciones aplicadas de verdad y sin regresiones: detector
reparado (extremos reales, dos arcos complementarios, orden de
suma mínima, R_mid; False en radio holgado, True en el positivo
construido [1.0, 0.15, 1.0, 0.15] a R = 2.05); los 4
contraejemplos de la v1 caen en la celda v2 (ejecutado); A1
re-derivada independiente (residuo 0); verificación ANALÍTICA
extra del ancla de G3 (h creciente en la caja ⟺ a+2b > R = 
no-apilable ⟹ γ_min = θ_w para cualquier dmin); re-barrido
CC_ITER=800: 250/250 en celda, anatomía 100% (i′), consistente
con el oficial 1266/4000.

**H1 [MAYOR, aplicada]**: el gate de A3b era TAUTOLÓGICO
(lp_ok = cajas_ok; el import de primal_factible muerto) — el
reclamo era VERDADERO (contraste real del referee: 1.500 tríos,
0 discrepancias; álgebra de cajas re-derivada: caps
s_k ≤ 2π−2θ_k ≥ 0 suman ≥ 2π−Σθ) → gate sustituido por la
comparación real contra primal_factible (n3b > 800, 0
discrepancias). **H2 [aplicada]**: actas persistidas (esta
entrada). **H3 [aplicada]**: R_lb obligatorio en en_celda.
H4-H5 [notas]: tol = 1e-7 del detector sin margen cuantificado
(empíricamente irrelevante); etiquetas honestas (G1 con la pata
A2 densa declarada; la rama (ii′) predicción no ejercitada,
declarada).

### Estado tras la re-ronda (v2, 5/5)

EL CONVERSO EN FORMA EXACTA v2: gap ⟹ (i′) algún par apilable
del núcleo en R* ∨ (ii′) dominación no-adyacente en R_mid — la
celda exacta que sustituye al 0.9 empírico. G1 teorema (A1
global simbólica + A2 denso extendido + no-vecinos por
t ≤ a_min); G2 TEOREMA (cajas, contraste real); G3 teorema
re-anclado; barrido 4.000/1.266/1.266 todos (i′). La anatomía
real del gap es la apilabilidad; la celda realista del F3 es un
caso de (i′) y ya es vacua bajo ρ ≤ φ. El fenómeno queda
cartografiado.

## Acta: LA RONDA FINAL CIEGA (paper entero, 7 bloques + meta) — 2026-08-20/21

**El compromiso cumplido** (memoria ronda-final-ciega, feedback de
Javi 2026-08-10): siete referees independientes, uno por bloque
temático del paper, CIEGOS — sin VEREDICTOS.md, sin drafts, sin
líneas de ataque; solo el paper, el código y los 7 criterios de
rigor genéricos (etiquetas honestas, dominios vs topes,
direcciones de tolerancia, gates infalsables, circularidad,
enunciado-vs-prueba, re-derivación propia). Más un META-REFEREE
de consistencia transversal sobre las 7 actas. Actas completas
archivadas (scratchpad de la sesión, ciega/acta_bloque1..7.md +
acta_meta.md).

**VEREDICTO GLOBAL: PUBLICABLE TRAS CORRECCIONES — CERO FATALES**
en los 7 bloques y en el meta. Recuento consolidado deduplicado:
0 FATALES · 11 OBLIGATORIAS · 17 RECOMENDADAS · 33 MENORES = 61
ítems. Circularidad inter-secciones LIMPIA (barrido de \ref
completo: cada apéndice importa solo de apéndices anteriores).
Los siete referees re-derivaron independientemente la matemática
sustantiva de sus bloques (sympy, racionales exactos, walkthroughs)
y la encontraron correcta.

### Los hallazgos con contenido matemático (ambos con reparación
derivada dentro de la propia ronda)

- **O2 (bloque 4)**: la prueba de thm:DP(iv) j=3 no cubría «y
  hoja estrictamente dentro del subárbol de o₁» (la ruta Ψ₃
  invocada es falsa si el subárbol es una cadena que termina en
  y). Reparación del referee, verificada: (b′) dos hijos-nodo ⟹
  hoja que evita a y ⟹ Ψ₃; (c′) cadena: la pinza corre verbatim
  con m contado vía T_{v*} ≥ X_{v*}+1 si v* ≠ y; si v* = y,
  contradicción y > 3 (cola de y) vs y < φ+ω < φ² (Ry + cola de
  m). El enunciado no cambia. APLICADA + gate falsable en
  batalla2.py (el viejo max(Ψ₃,Ψ_B) > φ era independiente de la
  instancia).
- **O3 (bloque 1)**: la clausura hacia abajo de la factibilidad
  se afirmaba sin prueba. Lema de tres líneas añadido (el disco
  del anillo retirado queda libre; los hijos no se mueven y se
  re-parentan). APLICADA.

### Convergencias entre referees independientes

V3 de las gemelas infactible tal como estaba impreso (bloques 2
Y 6: mismos déficits ~4e-4, mismos ángulos exactos 30.7535°/
32.0103°) → sustituido por el testigo RACIONAL EXACTO
(c_X = (8.8, √27.4176), c_Y = (8.7, −√29.5776); 14.76²/14.74²
exactos; abscisas 10.24·55/64 y 10.26·145/171). También: 5.37→
5.38, la cota general z > 30/7, d = 0 en S5, DSpan (B5+B7).

### Patrones sistémicos detectados (nota del meta)

(a) testigos/constantes impresos con redondeo inseguro — siempre
con el enunciado verdadero detrás; (b) punteros/recuentos del
aparato de verificación desincronizados (espfinal 6/6, Lean 45
teoremas, rigido/tresk/cuatrok, cifras de informe no trazables —
todo corregido o etiquetado); (c) gates que no pueden fallar —
tercer y cuarto ejemplares del patrón ya cazado en f3converso/
espcanalp: batalla2 (rama j=3 interior) y coronacolas C (el
«200.000 muestras, cero sin caso» era el complemento booleano de
su propia cascada de continues) → AMBOS sustituidos: batalla2
con el techo (c′) por instancia (6/6 verde), coronacolas con la
enumeración LÓGICA exhaustiva del retículo de 12 celdas
(falsable; el residuo es exactamente la celda D1; bloque C
verde). La exhaustividad de DSpan en el paper reescrita como la
tricotomía lógica (O10).

### Aplicación

61/61 ítems aplicados (O1-O3 y los gates por el autor; el resto
editorial por agente aplicador con verificación de compilación):
3 pasadas de pdflatex, 0 referencias sin resolver, 52 pp. Diff:
348 líneas en main.tex + los dos gates. Ajustes al lado seguro
en dos cifras (η < 0.049; õ = 1.29556…).

### Estatus del programa tras la ronda

El paper queda con: la matemática re-derivada por siete pares de
ojos sin anclar, cero fatales, los dos únicos huecos de prueba
reparados, el aparato de verificación sincronizado y los cuatro
gates-infalsables del proyecto cazados y sustituidos. La
honestidad de etiquetado sale REFORZADA (verificada punto a
punto por los referees 5 y 7; única sobredeclaración real: el
«is exactly» de op:assembly, corregida). Pendiente de decisión:
envío a arXiv (endorsement math.MG pendiente — memoria
paper-arxiv-estado).

## Acta: el peer review externo (codex) y su ciclo de reparación — 2026-08-21

**El encargo de Javi**: peer review externo por otro modelo (codex
CLI, sandbox de solo lectura), con la instrucción de no penalizar
longitud y centrarse en rigor, legibilidad, reproducibilidad y
novedad. **Veredicto del reviewer: REVISIONES MAYORES** (no
rechazo: «resultados originales, elegantes y potencialmente
publicables»). Informe completo en
docs/reviews/codex-peer-review-2026-08-21.md.

### Los dos cargos mayores y su resolución

1. **«Three never diverge» ERA FALSO** — el reviewer exhibió la
   divergencia con TRES anillos (R = 10, w = 9/2,
   {8, 101/20, 99/20}: el par diametral cabe, nada convive con el
   8, y a(8) = 207π/4 > 198π/4): verificado EXACTO en racionales.
   Un hallazgo que ni las rondas dirigidas ni la ronda ciega de 7
   referees vieron (anchura grande, fuera de las retículas).
   REPARADO: lema «dos nunca divergen» (exhaustivo lógico) +
   contraejemplo exacto + la instancia de 4 re-etiquetada como la
   mínima DEL MECANISMO DEL AGUJERO (el régimen w = 1 del diagrama
   de fases, ahora con su dominio declarado y franja.py citado)
   — script nuevo divergencia3.py (5/5), con la cartografía
   muestreada del umbral de anchura (aparece desde w/R ≈ 0.26).
2. **Las «certified maximization» por malla no prueban un sup
   continuo** — ENDURECIDO donde más importa: la maximización
   CENTRAL (la pared de corona de C3.3, el sup que cierra el
   régimen pesado de thm:DPr) subida a certificado por
   subdivisión: mayorante de esquina EXACTO (cada f-factor
   monótono por coordenadas; los productos contra f_o1 capados
   por sus límites monótonos x/o₂ — sin tope de barrido) + B&B:
   sup g < π sobre el dominio continuo NO ACOTADO en 71 cajas +
   dos regímenes de cola analítica — script rstarcert.py (5/5;
   el mayorante coincide con g en cajas-punto: ajustado; margen
   0.79). Las maximizaciones restantes (gaplemma, insercion)
   RE-ETIQUETADAS honestamente como grid-based con el asterisco
   de optimización, y su endurecimiento al estilo rstarcert
   declarado como continuación natural.

### El resto aplicado

Reproducibilidad: run_all.py con el perfil --campaign (el
manifiesto COMPLETO del verifmap, bandas incluidas — el reviewer
cazó que los 18 scripts del runner no cubrían la campaña y la
nota del autor prometía «every verification»); requirements.txt
con versiones fijadas (Python 3.13.7, numpy 2.2.6, scipy 1.16.3,
sympy 1.14.0, matplotlib 3.10.7) y la nota del solver
(linprog/HiGHS siempre re-verificado en float); READMEs de Lean
sincronizados (45 teoremas; el raíz decía 22 y lean/README 32).
Bibliografía: Chen-Tang-Song-Zeng-Peng-Liu (CIE 2018, greedy de
círculos iguales; autores verificados contra Semantic Scholar) +
el párrafo de la intro distinguiendo heurísticas de garantías.
Ccurve renombrada «lower-bound curve; exact on the witness
branch»; el pentagrama k = 5 con su script citado como
comprobación; la reducción NP racionalizada (dividir por π);
la frase del abstract separando niveles epistémicos; el verbo
«verified as a theorem by fuzz» → «re-derived independently and
probed by fuzz».

### Declarado como continuación

Endurecimiento de gaplemma/insercion al estilo rstarcert;
auditoría exhaustiva de verbos río abajo (punto 4 del review;
parcialmente cubierta por la ciega y esta tanda); lemas de
dominio adicionales en DGp/DP (punto 7; parcialmente cubierto
por R7 de la ciega).


## gaplemmacert.py — NOTA DE CICLO (contraste, sin acta): el endurecimiento pedido YA EXISTIA

Fecha: 2026-08-21. El «endurecimiento 2/3» del peer review externo
(subir gaplemma.py a certificado de caja) se ejecuto COMPLETO —
cuarteto j = 0 analitico via h(alpha) = x*(alpha) - (phi alpha - 1)/2
con raiz real unica alpha = phi; quinteto j = 1 por B&B fuera de la
banda de la variedad F(alpha, o1) = alpha o1 (alpha+o1-1) - alpha^2
- o1^2 = 0; colas en 1 caja por el cap del limite monotono
(estable donde R - o pierde precision float); 5/5 — y AL TERMINAR
se descubrio que el endurecimiento ya existia: la campana de
bolsillos (2dff09c/13630f5/4b0fede, tres rondas adversariales,
Lean 39) habia cerrado exactamente esa celda, con la MISMA
matematica (q(u) = (phi-u) r(u) equivale a h; la banda F es la
curva tangente del trio de fase 2, alli CERTIFICADA por
construccion — mas fuerte que declararla). Cadena del error: el
ciclo del peer review (1e34fe9), con el contexto comprimido, puso
a thm:gapwritten el asterisco de optimizacion CONTRADICIENDO el
parrafo siguiente del propio paper («For j=0 the domain sweep has
since been upgraded...»). REPARACION: paper corregido (el teorema
remite a los pocket certificates, sin asterisco; el unico portador
del asterisco queda nombrado: la maximizacion del budget de
thm:D1written / insercion); gaplemmacert.py se conserva como
CONTRASTE INDEPENDIENTE (dos convergencias por tecnicas distintas
sobre la misma celda), docstring y bloque E re-anclados, sin claim
propio en el paper y por eso sin ronda adversarial propia. El
referee lanzado para este ciclo se cancelo al descubrir la
redundancia. LECCION OPERATIVA (5o caso del patron de contexto):
antes de re-etiquetar un teorema o abrir un «endurecimiento»,
grep del paper ENTERO por la celda y git log de los scripts que
la tocan — el resumen de sesion no es el repositorio.


## insercioncert.py — CONFIRMADO CON CORRECCIONES (ronda adversarial, cero grietas de solidez)

Fecha: 2026-08-21. El endurecimiento 3/3 del peer review: el
presupuesto de sombras de thm:D1written (ambas inserciones) sube de
maximizacion dirigida (insercion.py bloque G, asterisco) a
CERTIFICADO POR SUBDIVISION sobre el politopo cascada COMPLETO —
todos los j >= 3 a la vez via la reduccion masa+cuerda (n <= m y la
cuerda de convexidad de asin), 4 variables agregadas (Sigma, m, o2,
o1), B&B principal 149/173 cajas + 7 celdas de cola por caps de
limite (sin tope de barrido). El referee re-derivo la reduccion, los
mayorantes y la rama homogenea de forma independiente, ejecuto 5/5 y
corrio 5 sondas propias (~21.000 comparaciones, j hasta 30, m hasta
3000, y un conjunto MAS ANCHO que el politopo real con o_k libres:
0 violaciones; sup real por ascenso = 4.7225/5.2644 EXACTAMENTE las
esquinas historicas j = 3).

HALLAZGOS: H1 (MAYOR, reparado): la esquina de t1 en la rama
homogenea (l2b = l2_lo con suelo1 creciente en lambda2) no estaba
cubierta por los gates A5/A7 — es correcta por una MONOTONIA
ACOPLADA a lo largo de v2 que el referee derivo (dz1/d rho < 0 en
ambos regimenes del max del suelo), y la esquina esta TENSA (holgura
-2.7e-15 en 4000 celdas: el sup real la toca). Reparacion: gate A8
con las dos derivadas acopladas simbolicas, verde. H2 (MENOR,
aplicado): paper sincronizado — thm:D1written con el certificado,
el residuo (v) cerrado entero, verifmap con los tres scripts nuevos,
op:assembly actualizado. H3 (NOTA): float sin intervalos, estandar
rstarcert, margen >> error libm. H4 (NOTA, aplicado): assert de
booleano estricto en el criterio (el motor descarta None en
silencio) y docstring de la masa corregido a (1+s) m_hi/u_lo.
H5-H6: re-derivaciones punto por punto y sondas, todas confirmadas.


## goldencert.py — CONFIRMADO CON CORRECCIONES (1 FATAL en el certificado embarcado, reparado y re-verificado)

Fecha: 2026-08-21. Los tres parches de malla de la rama B de thm:DGp
(bolsillo.py bloque F) suben a exacto/certificado: L1 (c10 >= 0 en
[g, o*], c20 >= 0 en [o~, 3/2]) por racionalizacion del radical +
Sturm racional exacto sobre el conjugado en Q[o] — o* = 1.59556948 y
o~ = 1.29556359 pasan de estimaciones de malla a RAICES ALGEBRAICAS
EXACTAS; L2 (f1a >= 0 en [g, q*] x [0, 1], contacto unico en (g, 1)
con gradiente (1/4, -sqrt5/4)) por B&B con el contacto tratado por
monotonia local; L3 (el parche del hueco alpha < o1) por B&B +
cierre elemental m1.

HALLAZGOS: H1 (FATAL, reparado): el minorante del bloque C
transcribia 1 - w donde el numerador real es 1 - 2w + 2b2 — NO era
minorante (exceso +w/o), las 16 cajas aceptadas no estaban
justificadas y el tratamiento del contacto era CODIGO MUERTO (nunca
se invocaba); el referee verifico la reparacion de un token: 529
cajas, 0 sin resolver, 1 caja via contacto con holguras amplias.
El enunciado L2 en si era verdadero (malla de control del referee
251x201 sin negativos). SEXTO caso del patron certificado-que-no-
certifica: un typo en el mayorante puede validar un B&B entero —
el control es SIEMPRE contrastar el mayorante contra la funcion en
cajas-punto (el bloque D de insercioncert lo hace; goldencert C no
lo hacia). H2 (MAYOR, reparado): «superset [o~, 3.5] x [0, 1/2]»
era falso — N1(w) -> inf con w -> 0 (N1(1/100) = 9.61); anadido
L3b: para o >= 3.5 la propia m1 da 4 > curva + 1/4; paper con la
clausula. H3 (MAYOR, reparado): el margen «Lipschitz» muestreado
x1.5 sustituido por la cota rigurosa del referee (B <= 12.31 por
esquinas de racionales, margen B h/2; la caja de contacto pasa con
mo - Bh/2 = +0.044). H4 (MENOR, reparado): signo_exacto sin
nsimplify/evalf — sp.sign sobre el valor algebraico exacto con
assert. H5 (MENOR, reparado): literales de o*/o~ corregidos
(1e-8). H6: la artilleria que NO perforo — direccion segura de la
racionalizacion, denominadores positivos globales (nuevo gate B1b),
A_max rama correcta y autodual, b2 creciente en ambos argumentos,
c21 = phi/2 - 1/A_max >= 0 sii A_max >= g (elemental de verdad),
sondas de 100k/50k puntos limpias. Re-run tras reparaciones: 5/5.


## espomegacola.py — CONFIRMADO (0 fatales, 0 mayores; 2 menores aplicados)

Fecha: 2026-08-22. La cola de anchura omega > 1.6 de la celda PESADA
ESPECULAR certificada ENTERA: el tope de barrido omega <= 1.6 del
residuo (ii) deja de ser tope en esta celda.  Arquitectura: las
ventanas de espfinal son omega-lineales (alpha >= max(1, SS+Xp) +
omega, z >= ... + 2 omega), el contenedor cumple c >= 1 + z (teorema
del par {z, m}), y cada termino se mayora UNIFORME en omega — el
rapido por el cap del limite th(z, x, c) <= 2 asin(sqrt x) (p =
zx/(1+z-x) crece en z hacia x, para x <= 1), los lentos con
c_floor = 1 + z_min(W0), el polvo con X_m = 0 exacto (omega > 1) y
un solo tramo pesimista.  B&B de 9 dims lentas: 23 cajas.  El par
(z, m) asintoticamente diametral se codifica thmat[0][1] = 0
(tangencia legal no estricta — la MISMA reparacion ya adversariada
de areduccion._peor_camino, que espfinal decidio no portar por
conservadurismo).

El referee re-derivo los seis flancos (ventanas, teorema del par,
caps, el 0 del par linea a linea en _peor_camino2, conservadurismo
del tramo unico, cobertura de perfil identica a espfinal) y corrio
600 cajas-punto x 4 anchuras con corona exacta + 20.000 puntos del
cap (peor holgura +2.4e-6: el cap es el limite, ajustado) + busqueda
dirigida del margen (0.0073 rad > 0 en el rincon SS -> 1 con polvo
maximo).  0 violaciones.  MENORES aplicados: el recuento de
dimensiones (9, no 10) y try/finally en el negativo D; typo del
docstring.  NOTA para el paper: citar el cap como LIMITE (holgura
asintotica 0), no como cota holgada.


## r2bcolas.py — CONFIRMADO (cero grietas de solidez; 2 deudas del motor y 2 notas, aplicadas)

Fecha: 2026-08-22. La cola Y > 6.6 de G-b' (el tope de muestreo
X_Y <= 3 del residuo (ii)) certificada ENTERA en DOS REGIMENES: la
parametrizacion homogenea rho = x/Y NO separa las saturaciones (con
x finito el par (Y, m) va diametral; con x ~ Y lo hace (Y, x): dos
pi excluyentes que un solo mayorante mezcla — el primer B&B se atasco
exactamente ahi).  Regimen I (todas las x <= 6.6): caps uniformes en
Y (p(Y, lenta) crece hacia k/(SS+Sx); (Y, x) <= x/(SS+Sx) via
c - x >= Y; lentos con c(Y1)), B&B con los motores de r2bmulti
(117/791/3329 cajas por j; la saturacion SS -> 1 la absorbe el par
analitico de banda_matriz, que NO lee thmat[0][1] — verificado linea
a linea).  Regimen II (x_max > 6.6 => Y >= x_max > 6.6): UNA
comprobacion cerrada por j con caps constantes (cruzados <= 1/2 y
1/4 — la cota (x_i, x_l) <= 1/4 es TENSA: 1.0466 vs pi/3 — y
lentas < 1/(1+6.6)), par (Y, x_max) antipodal con tangencia
asintotica legal.

Sondas del referee: ~29.000 comparaciones (60.931 puntos interiores
del regimen I con holgura minima 2.6e-4; 24.000 del regimen II
incluyendo x_max = Y exacto y j = 3 con las tres x = Y, holgura
0.0099; colocacion explicita del testigo verificada; 5.500
instancias adversariales de corona real: siempre cabe), 0
violaciones.  DEUDAS APLICADAS: H1 el lado vacio de _antipodal_cola
era imposible por diseno (req = pi del par) — exencion del par
antipodal anadida (conservador-ruidoso, no unsound); H2 gate
CRUZADO de lados anadido (la solidez que el referee demostro fuera
del codigo: sep(u, v) >= min-extremo(u) + min-extremo(v)); H4 el
conteo j <= 3 declarado en E como dominio heredado del MC (no
derivado); H7 contraste de caps del regimen II anadido al bloque C
(8000 puntos).  H5: la exclusion analitica del par (Y, m) de
banda_matriz sigue valida con caps (theta real < pi sii SS+Sx > 1,
independiente de la matriz).  Sin agujero j = 0 (rama DR de r2bcert
con T libre).  Re-run tras reparaciones: 5/5.


## esptorre.py — CONFIRMADO CON CORRECCIONES (certificado solido; el control y el alcance reparados)

Fecha: 2026-08-22. La banda media del canal ocupante a profundidad
de torre d >= 2 (residuo (iii)) cerrada para el PERFIL LIGERO y
torres-CADENA, dentro del convenio.  La reduccion ingenua a d = 1
con ocupante t_1 FALLA (los children de t_1 contienen x >= r_m, no
polvo: el techo del nodo y el de la ventana de z se rompen — la
grieta se cazo en el diseno, antes de la ronda); el cierre correcto
certifica d >= 2 DIRECTO: la torre como masa M >= x + omega solo en
suelos favorables (tres apariciones auditadas), t_1 >= x + omega en
la convivencia, y la ventana de z SIN TECHO cubierta por B&B finito
[1, 40] + cola z >= 40 por caps de limite (2asin(sqrt pieza) via
c >= 1 + z).  Ambas ramas certifican en 1 caja — y el referee
verifico que las 1-caja son REALES: thmat de la raiz reconstruido a
mano (reparto {sigma2}|{polvo} con margen 0.39 rad; el reparto de
un solo lado FALLA: el motor discrimina), falsable (piezas x2 ->
False), 500 torres en-celda con corona exacta y 0 violaciones,
200k comprobaciones de caps.  H3: la pinza RY es correcta (el RHS
es el techo de la ventana de Y por children — la torre son
descendientes de z y no suma; el LHS cuenta toda la cola por la
first-copy convention).

CORRECCIONES APLICADAS: H1 el control D(a) era casi vacuo (196/200
None: pinza de x no respetada, z pegado al suelo con ventana de Y
vacia — patron control-que-no-controla) -> regenerado EN-CELDA
(alpha en su ventana con holgura < 1+s2-SS, x sobre su pinza, z
sobre el umbral RY, SS <= phi por la pared global, un tercio en la
cola z; None sobre punto legal cuenta como violacion): 300/300.
H2 el alcance del bloque E estaba inflado -> la PESADA (espcanalp)
rebajada a continuacion declarada (su criterio conserva el techo
d = 1; la cirugia de torre no esta implementada alli) y
restaurados los residuos omitidos: omega <= 1.6 de esta celda
(la tecnica de espomegacola no aplicada aqui) y torres con RAMAS
(bajo el k >= 2 no-anidados de espcanal A6).  H5: docstring de
cajas-no-puntos y x_eff muerta eliminada.


## esptorrep.py — CONFIRMADO (cero grietas; 2 menores del control aplicados)

Fecha: 2026-08-22. LA TORRE PROFUNDA PESADA: la banda media del
canal a d >= 2 en el perfil pesado, cerrada con la cirugia de torre
de esptorre sobre espcanalp.criterio_pesada_z.  El referee verifico
la FIDELIDAD de la cirugia linea a linea (el diff es exactamente lo
declarado: M_lo en las dos colas, convivencia via t_1, techo de z
retirado con sus x_hi_z/x_eff que solo lo alimentaban, rama de cola
con caps; ninguna pieza retirada de mas), la pared pesada del nodo
sobre el x del fondo (children = polvo, valida a toda profundidad;
omitir z/alpha/torre de la cola global solo SOBRE-estima X_x:
conservador), la pinza RY (RHS por children — la torre no suma;
LHS suelo valido con +x+M por first-copy; en la cola la pinza se
desactiva: nunca reclama vacuidad), las direcciones de M (todas
suelos legitimos; mu_y_max sin restar x/M es correcto-conservador:
x y los t no son polvo), los caps de la corona pesada (<= 1
siempre; exceso del cap numerico 0.0 exacto en malla z hasta 1e7),
la no-vacuidad de los B&B (la 1-caja de la cola: los 8 tramos
kz x kseg reconstruidos a mano — la variante de UN bloque falla en
los 8 y la de DOS certifica: el motor discrimina; falsable por
masa x2, c estrangulado y th x1.6; censo: 393/440 por motor, 47
por vacuidad sana de ventanas), la cobertura de la raiz (X_TOP =
3.227 > 3.218 el techo puntual; A_MAX cubre; s2 <= 0.618 real en
la pesada), y el empalme sin huecos (el empate SS = 1 + s2 lo
cubre este script; las bandas de x muertas a toda profundidad por
pinza/pared).  Sondas: 400 puntos con S REAL construida
(b_star_particion) y X > 0 en 318, 150 coronas fisicas verificadas
(arc-LP/corona_suf/creciente): 0 violaciones.

MENORES APLICADOS: H1 el generador del bloque C muestreaba beta
abstracta -> S real via b_star_particion (como espcanalp C); H2 el
bloque C no ejercitaba X > 0 -> X's aleatorias bajo el presupuesto
global (y el suelo de alpha corregido con +Xp, que el replay del
fix destapo); H5 cosmetico del enunciado A3 (el cap fino).  Con
esptorre (ligera) + esto (pesada): LA BANDA MEDIA DEL CANAL A
d >= 2 CERRADA EN AMBOS PERFILES para torres-cadena, dentro del
convenio.


## r2bpool.py — NOTA DE CICLO (exploracion sin claim): j >= 4 en G-b' colinda con el lema de |A|

Fecha: 2026-08-22. Intento de cerrar el ultimo tope de conteo del
residuo (ii) (G-b' con j <= 3) por POOLING: las piezas X' plegadas
en bloques por masa con un peso NUEVO mas fino — LA CUERDA DE FILA:
una fila de piezas <= cap en capacidad c consume arco <=
[2 asin(z)/z] * m/(c - cap) con z = cap/(c-cap) (por arco(r) <=
2 asin(r/(c-r)), la desigualdad del semi-angulo theta(a,b) <=
asin f_a + asin f_b y la cuerda de convexidad de asin) — lema
exportable que mejora el pi m/(c-cap) historico en ~35% con cap
moderado.  Funcionan: los caps uniformes en Y, el refinamiento
th(Y_hi, a, c_lo) para Y acotado, y los regimenes con piezas
pequenas o resto diminuto.

EL OBSTACULO ESTRUCTURAL (resultado negativo informativo): la
banda POCAS-GRANDES (Mr ~ x_1 repartido en 1-3 piezas comparables
a x_1) no se certifica ni con bloques (cap ~ x_1 => theta(Y, B) ~
pi/2 y peso ~ 1: los lados exceden pi aunque la corona real quepa
holgada) ni con explicitas (el numero de grandes no esta acotado).
Es EXACTAMENTE el «lema de reduccion de |A|» que r2bmulti [E]
declaro faltante para G-e/G-g pesadas.  CONCLUSION: el tope j <= 3
de G-b' no es un tope trivial — colinda con ese abierto declarado;
su cierre es un ciclo mayor (jerarquia explicitas <= K +
cadena-cuerda + fila con la banda de transicion).  El paper ya
declara j <= 3 como eleccion del MC: nada que cambiar.  El script
queda como exploracion (gates A verdes; B&B parciales con las
cajas de la banda documentadas), sin ronda (no soporta claim).


## espomegacanal.py — REFUTADO EN PRIMERA RONDA -> REPARADO -> RE-RONDA CONFIRMADO CON CORRECCIONES

Fecha: 2026-08-22. LA COLA DE LA ANCHURA omega > 1.6 DE LAS SEIS
CELDAS DEL CANAL (el ultimo tope de barrido heredado, dentro del
convenio): tramo medio [1.6, 40] re-ejecutando los criterios
existentes (la afirmacion central — son OMEGA-GENERICOS, el 1.6
vivia solo en los roots — CONFIRMADA por ambas rondas con auditoria
linea a linea) + cola omega >= 40 por argumentos autonomos de caps.

PRIMERA RONDA (REFUTADO como cierre; la matematica sobrevive): H1
FATAL — el techo del root de z en las celdas x-EN-z copiaba la
formula historica 2 omega cuando la ventana legal lleva +x_eff ~
omega (escala 3 omega): puntos en-celda con omega >= 27.6 jamas
visitados (evidencia ejecutada: omega = 35, z = 91.5 > 85.5, True);
H2 FATAL — las torres perdian z > Z1 = 40 del tramo medio (sus
crit_cola nunca re-ejecutados con omega > 1.6; evidencia: omega =
2, z = 45, True); H3 caps del resto de C(a) no mayorantes; H4 C(b)
apelaba a certificados inexistentes; H5 C(c) sin gate.  OCTAVO
caso del patron de agujeros de cobertura: al extender un root,
recomputar los techos LEGALES de las ventanas (no copiar las
formulas del root historico).

REPARACIONES: Z_MAXZ = 127.13 a escala 3 omega (b: 1 caja; d: 293);
celdas g/h = las colas z de las torres con omega en [1.6, 40] (1
caja cada); bloque C reescrito con los caps correctos (1/z_lo) y
gates computados.  RE-RONDA (CONFIRMADO CON CORRECCIONES): el
techo puntual derivado independientemente (125.85/125.35 <
127.13), las dimensiones de los roots g/h verificadas contra los
unpacks (20 valores exactos, con controles de sensibilidad que
descartan el certifica-basura), la cobertura del plano (omega, z)
sin hueco, los caps de C re-derivados, y 1000 sondas en las
franjas de los agujeros (500 en z [85, 121] con omega [25, 40];
500 torres con z [40, 90]): todo verde.  Menores aplicados:
recuentos del docstring (293, g/h), el estatus E sin apelaciones
(margenes reales 0.397/0.82/0.62), y las peores esquinas
LITERALES en C(b)/C(c) (cap <= phi/2, masa <= phi - 1/2, dos
lentas por lado: 2.322 y 2.525 — los valores que el referee midio).
Agregado final: (a) 1.62M cajas; (b) 1; (c) ~3.3M en 11 bandas
eps 1e-2; (d) 293; (e) 1; (f) 31; (g) 1; (h) 1 — todas 0 sin
resolver.  Manifiesto campaign con las 17 invocaciones.


## lemaA.py (fase 1 del lema de |A|) — REFUTADO (dos agujeros de solidez del ESLABON FINAL; la matematica nueva sobrevive; hallazgo transversal sobre _antipodal2)

Fecha: 2026-08-23. EL VEREDICTO: el motor corona_slots certifica
coronas DEMOSTRABLEMENTE infeasibles.  Contraejemplo reproducible:
corona_slots(P=[74.2, 0.1], M=51, cap=25.5, c=100) = True, pero el
A legal {25.5, 25.5} da una corona INFEASIBLE con prueba exacta
(la ventana opuesta a P0 mide 0.501 rad y el par de 25.5 exige
0.699; el sistema de arcos es infactible por LP en TODOS los
ordenes).  No aislado: el barrido hostil del referee encontro
violaciones a razon ~1/60 certificadas en la region P0 ~ 0.7c.

H1 (FATAL, LA CAUSA RAIZ — HALLAZGO TRANSVERSAL): _antipodal2
(espfinal) verifica caminos POR LADO entre los polos (0, 1) y
cubre los pares CRUZADOS solo si vale theta(u,v) <= theta(u,polo)
+ theta(polo,v) — cierto SOLO cuando el polo mayora en f a los
intermedios.  PRECONDICION IMPLICITA bajo la que el motor fue
adversariado: en espfinal/esppesada/esptorre(p)/espomegacola/
espomegacanal los intermedios son polvo/piezas < 1 <= polos
(auditoria de usos: todas las coronas historicas la cumplen; en
r2bcolas el gate CRUZADO de su acta H2 la cubre explicitamente).
El lema de slots la VIOLA por construccion (slots hasta cap
grandes con polo m = 1): tercer bug del estilo
representacion-que-no-representa.  H2 (GRAVE, independiente): la
pi-gorra de th tapa pares de P imposibles (f f >= 1) cuando ambos
lados son no vacios: corona_slots(P=[2, 2], M=0.5, cap=0.25,
c=3.9) = True con el par (2, 2) incapaz de coexistir — el motor
generico necesita el gate de factibilidad de pares que
criterio_gbp si declaraba en su celda.  H3 (GRAVE): el enunciado
A1 «M < c en toda corona» es FALSO como teorema (3000 piezas de
0.01 en c = 10: M = 30, colocacion legal; el maximo real escala
~ pi c): el gate operativo es conservador pero el claim de
completitud cae — el regimen M in [c, ~pi c) queda fuera y debe
declararse.  H4 (GRAVE): el tope M <= 13.2 de la aplicacion C(a)
era un TOPE DE BARRIDO con justificacion espuria («M < c» es
vacia en G-b': c = SS+Y+M), mas un suelo M >= 0.05 silencioso; y
el «extiende r2bmulti» sobrevendia (r2bmulti llegaba a M = 19.8
en j <= 3).  H5: el control B(d) no muestreaba la region hostil
(NOVENO caso del patron control-que-no-controla — los controles
deben muestrear ADVERSARIALMENTE la region donde el mecanismo
nuevo puede fallar, no distribuciones comodas).  H6: codigo
muerto crit_slots_YG.

LO QUE SOBREVIVE (verificado a mano por el referee, sin
objecion): los SLOTS ESCALONADOS (r_i <= (M-(g-i)t)/i, asignacion
ordenada mayorando entrada a entrada), la CUERDA DE FILA entera,
el greedy-halving, los radios-nodo ligados a masa, la fila Y de
la aplicacion y la estructura AND-sobre-g / OR-de-colocaciones —
la matematica nueva es correcta; lo roto es ENTREGARLA a
_antipodal2 fuera de su precondicion.  REPARACION (fase 1-bis,
pendiente): motor de dos lados con pares cruzados explicitos
(extender el _antipodal_cola de r2bcolas, que ya los gatea) +
gate de factibilidad f f < 1 + A1 como condicion operativa +
topes de C(a) declarados o derivados + control B(d) hostil.
lemaA.py queda como BORRADOR REFUTADO-EN-REPARACION, sin claim.


## lemaA.py fase 1-bis — RE-RONDA: el MOTOR NUEVO CONFIRMADO; C(a) refutada otra vez (motor viejo olvidado) y reparada segun prescripcion

Fecha: 2026-08-23. LA RE-RONDA confirmo el motor de colocacion
(_coloca_y_verifica + _motor_dos_lados: suficiencia constructiva
completa) con artilleria seria: unit-test de sep() (3000 pares,
error max 4.4e-16), barrido de la region hostil (120 coronas x
1112 instancias con ORACULO LP EXACTO calibrado sobre los
contraejemplos de la primera acta), 3 piezas P, pares casi-pi,
bloques pesados y 150 casos-borde por biseccion en c: CERO
contraejemplos nuevos (peor margen +0.018).  Los tres negativos
del acta caen.  A1 operativo honesto; topes de C(a) declarados;
B(d) hostil correcto; spot-check transversal: espfinal._certifica
y esptorrep._certifica_z cumplen la precondicion (intermedios
< 1 <= polos).

PERO C(a) SEGUIA USANDO EL MOTOR VIEJO (_corona_slots_capY llamaba
a _antipodal2 — negligencia de la reparacion): el referee
re-ejecuto el B&B real y encontro 5 cajas certificadas SIN
respaldo (oraculo LP: t* = -0.015 a -0.050; el triangulo {Y,
slot 6.6, slot 4.66} consume 5.75 de 6.28 rad y el resto no cabe
— el par cruzado (slot, slot) jamas mirado).  El claim en si
sobrevive (105.560 instancias reales oraculadas: peor t* = +0.50).
REPARADO segun la prescripcion del acta: _corona_slots_capY
decidida por _motor_dos_lados con dos colocaciones OR ((Y, m) y
(Y, slot_1) con la exencion EN-CELDA pr(Y, x1) < 1 — el parametro
`exento` deja de ser codigo muerto), el B&B re-subdivide las
cajas antes irrecuperables y pasa; E retitulado (fase 1-bis,
«complementa»).  Run final 5/5 con el motor confirmado decidiendo
TODO.  LECCION (segunda del ciclo): al reparar un motor, grep de
TODOS los llamadores del viejo — la funcion especializada quedo
sin migrar y el docstring afirmaba lo que el codigo no hacia.

================================================================
ACTA — FASE 2 DEL LEMA DE |A|: G-b' COMPLETO (lemaA2.py + motor
compartido lemaA.py) — RONDA CONFIRMADA CON CORRECCIONES +
VERIFICACION DIRIGIDA CONFIRMADA (R1 aplicado)
================================================================

Fecha: 2026-08-23. EL CLAIM: G-b' certificado para todo Y >= 1,
toda masa M > 0, todo cardinal (j >= 1; j = 0 es el baseline
r2bmulti) — el conteo j <= 3 del residuo (ii) DEJA DE SER TOPE.
Composicion: fase 1-bis (Y <= 6.6, M in [0.05, 13.2]) + R-I
(Y >= 6.6, piezas <= 6.6; fila por limites, M de 0 a la cola)
+ R-II (x_max > 6.6; B&B (s2, SS, uq, uv)) + R-III (flecos
M < 0.05 y M > 13.2 de Y <= 6.6).

DOS UNSOUND AUTOCAZADOS ANTES DE LA RONDA (declarados): (1) el
"factor cuadratico" p_GB = mq/(1+q_lo)^2 era ANTICONSERVADOR
(grande/(c-cap) solo <= 1 cuando Y >> x; el cap sound es lineal)
— 53 cajas certificadas con el descartadas; (2) la colocacion
CICLO SIMPLE (nueva en el motor: _coloca_ciclo, para coronas
holgadas donde el par antipodal desperdicia) corria con pares
exentos leyendo thmat[0][1] = 0 como requisito real — guard
`exento is None`. De paso el ciclo descubrio que el negativo
B(c) historico de lemaA era FACTIBLE de verdad (el motor viejo
lo rechazaba por limitacion): sustituido por un infeasible
probado ({1.5 x2} + A(3, 1.5) en c = 3.55: suma ciclica 6.57 >
2pi, sin pares imposibles, los 3 ordenes ciclicos equivalentes).

LA CLAVE DE R-II: la dimension v = Y/x_max. Sin ella los caps
grande-resto no bajan de mq/(1+q_lo) (tight en Y >> x) y q ~ 2
no cabe; con ella todos los pares usan p = [a/(c-b)][b/(c-a)]
con las paredes c - x >= x(v+q), c - cap >= x(v+q+1-mq), c - Y
>= SS + x(1+q) — nueve cotas re-derivadas por el referee, todas
correctas, mezcla de esquinas conservadora. El par (Y, x_max)
lleva su theta REAL (ciclo disponible) salvo clamp (q_lo ~ 0:
exencion antipodal del gate A2, estricta SIN apelar al clamp).
Slots por VARIANTES AND EN g (masa de bloques <= Mr - g t2) con
D = min(cuerda mq con ratio <= 1/2 uniforme, cuerda t2 con z =
1/(K-1)).

RONDA 1 (CONFIRMADO CON CORRECCIONES): 0 certificados falsos —
~1500 coronas reales (300 banda dura v in [1,3] x q in [1,4] +
555 muestreadas DENTRO de 100 cajas certificadas + 31
infeasibles probados contra el ciclo): 0 violaciones. H1 MAYOR:
hueco real M in (0, 1e-3) en R-I (fila con M_lo subestima el
sup para M_real < M_lo — deficit 1e-5 >> tol). H2 MAYOR: la
soundness de _corona_capY sin el gate M < c descansaba en tres
argumentos NO ESCRITOS que el referee derivo: (i) K-copias
(c_real > K p => f_real < 1/(K-1)), (ii) ratio 1/2 de cola
exige c_lo >= 6.72 (condicion de regimen: R-I 7.6, R-III gordo
15.2), (iii) mayorizacion no-cola = 36 l^2 - 59 l + 25 >= 0
(disc -119 < 0). H3: etiqueta E(b) no describia el test. H4:
M-uniformidad de la cola descansaba en saturacion de facto.
H5: M_lo = 1e-6 de R-III chico sound solo por Y <= 6.6. H6:
j = 0 fuera del dominio, declarar.

REPARACIONES + LO QUE DESTAPARON: M_lo = 0 en la banda inferior
(fila a/SS sup uniforme) CLAMPA el par (Y, m) a pi en la esquina
SS -> 1 — cerrado con la EXENCION (Y, m) NUEVA (gate: ff =
Y/((SS+M)(SS+Y+M-1)) < 1 ESTRICTO en todo G-b' porque SS+M > 1 y
SS+Y+M-1 > Y), colocacion OR de respaldo en _corona_capY. Los
flags cola_inf (M-uniforme, exige saturacion H4 o cap_hi <= t
ESTRUCTURAL) y via_cola (peso ratio-uniforme, gate 6.72)
separados — el gate H4 ingenuo (n_g = K-1 siempre) rechazaba
las colas con cap_hi < t legitimas. E(c) nuevo: falsabilidad
real de crit_RII (caja dura q ~ 2, v ~ 1 certifica; thetas x2
rechaza).

VERIFICACION DIRIGIDA (CONFIRMADO + R1 OBLIGATORIO): la
exencion (Y, m) atacada sin exito — convencion del modelo
verificada en r2bmulti.criterio_gbp (c = SS + Y + M con m y s2
DENTRO de SS... sus aportes a c son via SS; c - 1 y c - Y
exactos), expansion simbolica (Y+u)(u+1) - Y = Yu + u^2 + u > 0,
barrido hostil sup ff = 1 - 1e-12, sonda 300 coronas esquina
dura (SS - 1 <= 2e-3, M <= 1e-3, Y hasta 100): 0 violaciones,
theta(Y, m) max 3.117 < pi. R1 (MAYOR, LATENTE): borde x cola en
crit_RI daba M_hi = 0.0 (certificado degenerado True demostrado
sobre caja artificial); NO EXPLOTADO en el B&B ejecutado (las
1243 cajas instrumentadas: 0 borde+cola — proteccion accidental
por orden de particion) — gate aplicado (False, no None: la
caja tiene puntos legales). El peso literal de la banda M_lo=0
es sound sin monotonia (mayora masa <= M_hi; nota R3 comentada).

RUN FINAL: lemaA2 6/6 (R-I 1243/535, R-II 1789/797, R-III 53/23
+ 355/148), lemaA 5/5 (motor con ciclo + guard). LECCIONES
(novena y decima del patron): al anhadir una via al motor
(ciclo), auditar que las CONVENCIONES de las vias existentes
(exencion = thmat 0) no se filtran; los gates de uniformidad
(H4) deben distinguir el caso estructural (cap <= t) del
censado (saturacion) — el gate ingenuo mata certificados sanos.

================================================================
ACTA — FASE 3a DEL LEMA DE |A|: G-e / G-g PESADAS (lemaA3.py) —
PRIMERA RONDA REFUTADO EL CIERRE EJECUTADO -> REPARADO -> RE-RONDA
DE FIDELIDAD CONFIRMADA (cero grietas residuales)
================================================================

Fecha: 2026-08-23. EL CLAIM: las celdas pesadas G-e y G-g del
ensamblaje (declaradas FUERA en r2bmulti, cubiertas solo por el
MC de puertocii (e)/(g)) certificadas por B&B: el mural {Y, m} U A
(c = SS + Y) y {z, D_m} U A (c' >= 1 + z) con |A| SIN COTA, y
Y/z SIN TECHO (los techos del MC heredaban w <= 1.6; aqui colas
por fila de limites).

LA MATEMATICA NUEVA (ambas piezas CONFIRMADAS por el referee con
derivacion propia): (1) EL GATE DE LA PARTICION — con A no vacio,
b = masa(B*) > 1/2, toda pieza a de A cumple a <= min(b, SS - b)
<= SS/2 <= phi/2 y masa(A) = SS - b (derivado de la maximalidad
de B*; 450 particiones adversariales estructuradas, B* sin la
pieza mayor incluido: 0 violaciones); b COMO DIMENSION del B&B
(el acoplamiento b/|A|/masa/cap: el conservador plano no
cierra).  (2) EL LEMA DE LA CADENA DORADA — el lado {a} entre z
y m con c' = 1 + z cabe sii asin sqrt(p1) + asin sqrt(p2) <=
pi/2 sii p1 + p2 <= 1 (x^2 + y^2 <= 1) sii (1-a)(z^2+z) >= a;
con a <= SS/2 y z >= SS (pared E4-esp real, verificada) se
reduce a SS^2 - SS - 1 <= 0, es decir SS <= PHI EXACTO: la
pared de la familia ES el caso de tangencia (SS = phi, a =
phi/2, z = phi, tangencia exacta legal).  LEMA POR PUNTO: las
cotas van atadas al MISMO SS de cada punto real — la variante
k = 1 no evalua nada por caja (la evaluacion por esquinas
mezcla a_max con z_min y rompe la tangencia por epsilon: ese
fue el atasco de diseno, resuelto al reconocer el lema).
(3) ESCALONES POR MASA: la pieza i-esima de k piezas de suma M
es <= M/i (variantes AND por |A| = k).

LA PRIMERA RONDA REFUTO EL CIERRE EJECUTADO (H1 FATAL): en la
variante k >= 6, cap_b = min(cap_k, masa_A/6) — pero masa_A/6
solo acota la pieza SEXTA: las cinco mayores solo estan
acotadas por cap_6 = masa_A - 5(1-b).  Contraejemplo legal del
referee: S = {0.95, 0.4, 5 x 0.0501} (b = 0.95, |A| = 6, pieza
0.4 modelada a cap ~0.11) EN HOJA CERTIFICADA de ambos B&B —
la banda b > 0.876 que es exactamente el punto de venta del
claim (|A| sin cota).  La VERDAD no fue refutada (0 violaciones
de corona_suf en ~1640 contrastes, banda incluida).  REPARACION
DE UNA LINEA: cap_b = cap_k.  H2 MENOR: docstring de crit_Gg
contradecia el codigo (decia "verificado numericamente por
caja" del k = 1 analitico) — corregido.  H3/H4 NOTAS
consignadas (falsabilidad solo via _asin2; rama masa <= 0 vacua
en la pesada).

LA RE-RONDA DE FIDELIDAD: diff cotejado linea a linea (solo lo
prescrito), el contraejemplo H1 ahora en hojas con cap_6 =
0.743/0.524 >= 0.4, runs identicos (G-e 877/421, G-g 6645/3034),
200 instancias dirigidas |A| = 6..10 en b > 0.876 localizadas
end-to-end en hojas certificadas con corona_suf verde (400
coronas, 0 violaciones).  VEREDICTO FINAL: CONFIRMADO.

Lo que ademas AGUANTO en la primera ronda: la exencion (Y, m) de
G-e (ff crece hacia 1/SS < 1), las filas por limites con sus
colas (crit_Ge no lee uyh — cola Y genuinamente uniforme,
verificado programaticamente), la cobertura (roots
superconjunto, coincidencia exacta con el objeto barrido de
puertocii: c = SS + Y y cp >= 1 + z), y 800 puntos end-to-end
sobre 69 hojas certificadas distintas.

PAPER: el item "extras coronas on swept ranges" del residuo (ii)
reescrito — los murales pesados quedan certificados sin techos
(queda solo la ESP especular del engine en sus rangos); verifmap
con lemaA3; la seccion del ensamblaje menciona la
re-certificacion.  LECCION (undecima del patron): un cap "por
posicion" (masa/i) solo mayora la pieza de ESA posicion — al
agregarlo a un bloque, el cap del bloque es el de la PRIMERA
pieza que puede caer en el, no el de la ultima.

================================================================
ACTA — FASE 3b DEL LEMA DE |A|: K >= 2 ANILLOS DEL CANAL LIGERO
(lemaA4.py) — TRES VUELTAS ADVERSARIALES: CONFIRMADO CON
CORRECCIONES tras DOS REFUTADOS intermedios
================================================================

Fecha: 2026-08-26. EL CLAIM FINAL (tras el ciclo de rondas): la
ESP ligera con k >= 2 anillos extra >= r_m en el contenedor de Y
queda CERTIFICADA por B&B en OMEGA IN [0, 1.05] con extras de v
HOJA (children = polvo) y Wz <= 34 (anidados en z, torres
incluidas); RESIDUOS DECLARADOS Y SONDADOS (~1450 sondas
corona_suf en total, 0 violaciones): la banda omega in [1.05,
1.6] entera, los extras-PADRE (anidados dentro de extras de v),
la cola Wz > 34 (por dominio del root), la cola omega > 1.6
(patron espomegacanal) y la pesada (pared A7).

EL APARATO: 11 dims (w, s2, SS, Xp, Xz, Xm, a, z, mu, Wv, Wz)
con masas de extras como dimensiones; x_floor = (1+SS+X+mu)/phi
(pinza de la cola de x, posicion-independiente) y T = s2+w+X_x
(pared del nodo para hojas) acotan cada extra; variantes AND por
j_v con escalones por masa y sub-bandas adaptativas de x_2
ligadas (el techo de x_1 baja con la banda de x_2 — sin el
ligamiento el par (z, x_1) clampaba espuriamente); j >= 6 por
BLOQUES PUROS (cap = min(T, Wv - 5 x_floor): la PRIMERA pieza
que puede caer, leccion 11); cola Wv W-uniforme con peso C max(
phi/2, r(W_0)) (H5: el sup del ratio NO es el limite); LA COTA
ACOPLADA POR EXTREMOS (gate A6, nueva): con c(z) = (K+z)/phi -
omega, log p solo tiene minimos interiores (S' = 2 beta gamma /
((c-a)(c-z)) > 0 en todo punto critico) — el sup de p esta en
los extremos de z, y para pares (z, extra) tambien en los del
extra (4 esquinas, min de familias); EL MINI-MOTOR _motor_rapido
para coronas n >= 8 (ciclo + repartos greedy: el pleno con 2^n
masks x perms costaba segundos/caja — probar menos colocaciones
solo pierde suficiencia).

LAS TRES VUELTAS (la historia integra):
VUELTA 1 (REFUTADO): H1 FATAL — la banda declarada con `wh >=
1.4` (TECHO de caja) tragaba enteras las 4 bandas del manifiesto
con techo 1.4 (verdes vacuas: "1 caja, 0 certificadas"); H2
FATAL — el techo T solo se deriva para extras HOJA (espcanal A3:
children del minimal = polvo): un extra PADRE tiene X_x >= 1 y
excede T; contraejemplo exacto (T = 1.518, padre 2.34 con
anidado 1.35) en caja podada por FALSA VACUIDAD (j_min > j_max).
VUELTA 2 (REFUTADO): mi reparacion R3 de la cola Wz usaba
box-test por TECHO (`Wzh >= 34 -> None`) y el ROOT [0, 34] lo
cumplia: LAS 18 BANDAS REPORTADAS VERDES ERAN VACUAS (el mismo
patron techo-vs-suelo de H1, cometido por mi al reparar) — el
referee lo cazo cotejando que el run reportado era imposible
con el codigo en disco.  H4: con T_ext = T + Wz honesto, el
rincon cola-Wv con padres no cerraba; H5: el peso de cola
asumia sup = limite.
DECISIONES FINALES: (a) el claim EXCLUYE los padres (la opcion
alternativa que el propio referee prescribio en R2) — todo
extra de v es hoja y T es correcto; (b) el corte estable en
omega puro 1.05 (la "lamina" de saturacion diametral — par
(z, x_1) al piso de capacidad con bolsillos reales de
centesimas — reaparecio en 15+ iteraciones de delimitacion a
CADA j como extras-contra-el-techo con z chico: box congelado,
caracterizacion estructural, version-padre y apretura multi-j
derivaron todas; el corte por suelo wl es el unico estable);
(c) la variante j >= 6 reescrita a bloques puros (la de
5-escalones + bloques doble-contaba ~1.5 Wv).
VUELTA 3 (CONFIRMADO CON CORRECCIONES): la variante de bloques
puros verificada sound (cap mayora x_1 para todo j >= 6 hoja);
H3 por dominio verificado (el root de z 42.698 cubre exacto el
techo Rz con Wz <= 34); H4 regresion certificada; H5 sound en
el manifiesto (el caso kink exige z_lo > 18.9 y alli r < phi/2
— nota en el codigo); la vacuidad j_min > j_max ahora legitima
(sin configs hoja); 5 bandas reproducidas con conteos + A 6/6,
C 3/3, D.  Correcciones aplicadas: guard de _cuerda en la rama
no-cola (peso negativo alcanzable solo fuera del manifiesto),
textos A2/A5/header/check-B alineados al claim final.

MANIFIESTO FINAL (12 bandas, todas verdes con el codigo final):
Wv {[0,4],[4,8],[8,12]} x omega {[0,0.4],[0.4,0.8],[0.8,1.05]}
(9) + Wv [12,34] x omega {[0,0.8],[0.8,1.05]} (2) + la banda
declarada [0,34] x [1.05,1.6] (1).  Conteos del referee:
[0,4]x[0,0.4] 1463/476; [4,8]x[0.4,0.8] 4707/1659;
[8,12]x[0.8,1.05] 24071/7305; [12,34]x[0,0.8] 843/265;
[12,34]x[0.8,1.05] 1089/364.

LECCIONES (12-15 del patron): (12) el box-test de una
declaracion SIEMPRE por SUELO — el techo dispara sobre el root
(cometido DOS veces en el mismo ciclo, la segunda al reparar la
primera); (13) una pared derivada para el caso minimal (T con
children-polvo) NO se hereda al caso anidado — auditar la
precondicion de cada pared al extender el dominio; (14) mezclar
escalones-al-techo con bloques de masa residual doble-cuenta;
(15) el coste del motor pleno explota con n >= 8 nodos y un
mini-motor greedy es sound por perdida-de-suficiencia.  El
patron transversal de la campana (verdes-vacuos) suma su caso
mas instructivo: NUNCA reportar bandas verdes sin mirar el
conteo de certificadas.

================================================================
ACTA — CICLO 3c DEL LEMA DE |A|: EL MOTOR-BOLSILLO Y LA SUBIDA
DEL CORTE A OMEGA <= 1.15 (lemaA4.py) — CONFIRMADO CON
CORRECCIONES (con una leccion de atribucion)
================================================================

Fecha: 2026-08-26. OBJETIVO: encoger la banda declarada omega
[1.05, 1.6] de la fase 3b con la carencia que sus tres vueltas
identificaron — las colocaciones de BOLSILLO (m al hueco de
Descartes entre murales, lo que corona_suf hace y el motor
mural no representaba).

LO CONSTRUIDO: _bolsillo_inf(a_lo, b_lo) = 1/(1/sqrt(a) +
1/sqrt(b))^2 — cota inferior del bolsillo de Descartes valida
para TODO R y toda separacion (tres monotonias: dkp/dkw = 1 +
(ka+kb)/sqrt(disc) > 0 con kw = -1/R => el infimo es R -> oo;
crece en los radios murales => suelos; la tangencia minora toda
separacion >= theta — re-derivada por el referee: sep(grano, q)
>= theta_w(bolsillo, q)); _prueba_bolsillo (granos {m, s2}/{m} a
techo, muro por ciclo tolerando el par saturado, bolsillos de
los pares consecutivos con el esquema de resta de corona_suf);
gate A7 con sympy.

EL RESULTADO MEDIDO: el corte de la banda declarada sube de
1.05 a 1.15 (4 bandas nuevas verdes: Wv {[0,4],[4,8],[8,12],
[12,34]} x omega [1.05,1.15]; ademas [1.05,1.25] cierra salvo
Wv [8,12], donde la familia multi-j reaparece en [1.15,1.25];
la franja [1.25,1.4] es coste puro de maquina — 12.8k cajas/
400s sin fugas, kills sistematicos).

LA LECCION DE LA RONDA (hallazgo central del referee, MAYOR de
honestidad): la atribucion era FALSA — instrumento la via
bolsillo y NO DECIDIO NI UNA CAJA (0 exitos en ~52k llamadas;
contrafactual con la via deshabilitada: conteos IDENTICOS).
La franja [1.05, 1.15] cierra con LA MAQUINARIA DE LA FASE 3b
(bloques puros, cotas por extremos), que nunca se habia
re-testado ahi tras la tercera vuelta — el corte 1.05 era un
artefacto historico.  Diagnostico de la inercia: el grano
m = 1 exige 1/sqrt(z_lo) + 1/sqrt(x1_lo) <= 1, imposible en
las ventanas que fallan (haria falta z_lo >= 40).  EL MOTOR SE
QUEDA (sound, auditado a fondo: monotonias re-derivadas,
disyuncion del grano con murales no adyacentes probada en el
limite half-plane, resta multigrano justificada via fila
diametral dentro del disco-bolsillo, falsabilidad unitaria
verde) como via documentada-inerte.  Correcciones aplicadas:
la atribucion honesta en header/D/_en_lamina, el check B con
W_CORTE interpolado, el gate A7.

Reproduccion del referee: 4 bandas nuevas con conteos
(6479/1866, 3509/959, 23305/6864, 905/301) + declarada (1
caja) + A/C/D verdes; 150 sondas de verdad en la franja nueva
(0 violaciones).  LECCION 16 del patron: al mejorar la
maquinaria, RE-TESTAR los recortes declarados antiguos (el
corte era un artefacto); LECCION 17: toda atribucion causal de
un cierre a un mecanismo nuevo se INSTRUMENTA (0 decisiones =
narrativa falsa aunque el resultado sea verdadero).

================================================================
ACTA — CICLO 3d DEL LEMA DE |A|: EL RE-TEST DE LOS PADRES Y EL
CLAIM DUAL (lemaA4.py) — CONFIRMADO CON CORRECCIONES (un FATAL
posicional refutado, reparado en una linea y cotejado)
================================================================

Fecha: 2026-08-28. OBJETIVO: atacar los residuos declarados del
ciclo 3c aplicando la LECCION 16 (al mejorar la maquinaria,
re-testar los recortes declarados antiguos). El candidato: los
extras-PADRE (extras anidados en extras de v), declarados desde
la segunda vuelta de la fase 3b (opcion b del referee: claim de
hojas). La maquinaria del 3b/3c (T_ext = T + Wz de la segunda
vuelta, variantes por conteo, bloques puros) nunca se habia
re-apuntado a ellos.

LO CONSTRUIDO (modo CC_PADRES=1, aditivo, hojas intactas):
- La lamina de declaracion cambia a (omega > 1.05 O Wv > 8):
  el claim-padres vive en omega <= 1.05 y Wv <= 8 (Wz <= 34
  por dominio del root, como en hojas).
- techo_esc(i) = T_ext si i <= n_padres sino T, con
  n_padres = floor(Wz_hi / x_floor): las primeras posiciones
  pueden ser padres (cota T_ext), las demas son hojas (T).
- j_min por acumulacion de techo_esc; variantes j imposibles
  por conteo -> VACUIDAD (continue), no fallo.
- j >= 6: padres-nodo explicitos (hasta n_p6 = min(n_padres, 3))
  + bloques de hojas.
- Bloque C(a) con 30% de configs padre; ~400 sondas de verdad
  padre del referee (claim + residuos), 0 violaciones.

LA RONDA (quinta de lemaA4; dos caidas de sesion del referee —
limite de gasto y reinicio del proceso — documentadas; sus notas
integras en el scratchpad sobrevivieron ambas):

H1 FATAL (REFUTADO -> REPARADO -> COTEJADO): en j >= 6 con
n_padres > n_p6 = 3, la pieza (n_p6+1)-esima puede ser un PADRE
(> T), pero el resto tras los padres-nodo se capaba con
cap_f = min(T, ...): el mayorante no cubria. Exhibit del referee
(probe7): caja certificada del dominio del claim con config real
legal de 6 padres ~1.31 > cap_f = 1.068 (anidados legales,
Wz en caja, verdad corona_suf verificada). ES LA LECCION 11
APLICADA A PADRES: un cap por posicion solo mayora la pieza de
ESA posicion — y "posicion de hoja" no mayora un padre.
REPARACION (prescripcion del referee, una linea):
cap_f = min(techo_esc(n_p6 + 1), max(x_floor, Wv_hi/(n_p6+1)
si n_p6 sino Wv_hi - 5 x_floor)). ARGUMENTO POSICIONAL (el
referee lo hizo suyo): p_4 <= Wv/4 (cuarta en orden decreciente,
incondicional) y p_4 <= techo_esc(4) (si p_4 > T hay 4 padres,
luego techo_esc(4) = T_ext) — min de dos mayorantes, sound.
COTEJO: probe7b (el rincon del exhibit contra el criterio en
disco: cierra n=55 cert=20, tainted-check contra el cap nuevo =
0 — el referee precisa que ese 0 es garantia ANALITICA del cap
nuevo, test de regresion y no evidencia independiente); el
exhibit exacto certifica ahora con cap 2.0 >= 1.36; busqueda
adversarial propia del referee 200k cajas x configs j = 6..9
con bordes n_p6 = 3 y n_padres = 4: exceso maximo de pieza
sobre cap_f = 0.000000; rincon extremo Wz [28,34]
(n_padres ~ 27) cierra.

CONFIRMADOS SIN CORRECCION: las vacuidades por conteo y el j_min
por acumulacion (derivacion posicional propia del referee); la
invariancia de hojas (con PADRES=0 el fix es un no-op
demostrable: n_p6 = 0 fuerza la rama antigua; bandas de control
[12,34]x[1.05,1.15] 905/301 y [0,4]x[1.05,1.15] 6479/1866
IDENTICAS al 3c, verificadas por el referee y el coordinador);
los textos B/D del claim dual (dominio honesto, la atribucion
del 3c preservada).

RUN FINAL (codigo final, las 6 bandas del manifiesto padres,
todas verdes): [0,4]x[0,0.4] 2355/849; [0,4]x[0.4,0.8]
4133/1400; [0,4]x[0.8,1.05] 5073/1469; [4,8]x[0,0.4]
46033/18729 (la banda del exhibit, re-corrida tras el fix);
[4,8]x[0.4,0.8] 37113/13911; [4,8]x[0.8,1.05] 24651/8956.
Las bandas fuera del rincon del fix conservan sus conteos
pre-fix (no-op verificado por conteo identico). A 7/7, C 3/3
(con 30% padres), D verde.

VEREDICTO DEL REFEREE: CONFIRMADO CON CORRECCIONES. El claim
dual queda: HOJAS omega <= 1.15 / Wz <= 34 (16 bandas, sin
cambio) + PADRES omega <= 1.05 y Wv <= 8 y Wz <= 34 (6 bandas
nuevas). RESIDUOS DECLARADOS Y SONDADOS: padres con Wv > 8 u
omega > 1.05; la banda omega [1.15, 1.6]; Wz > 34; omega > 1.6;
la pesada.

LECCIONES: la 16 RINDE (el residuo-padres era en gran parte un
artefacto de no re-apuntar T_ext); la 11 tiene una variante de
TIPO, no solo de posicion (un cap "de hoja" en una posicion que
puede ocupar un padre es el mismo error); los conteos identicos
pre/post-fix fuera del rincon son la verificacion barata de que
un fix es local.

================================================================
ACTA — CICLO 3e DEL LEMA DE |A|: LA COLA Wz > 34 CERTIFICADA
(lemaA4.py, modo CC_COLAZ=1) — CONFIRMADO (sin correcciones
obligatorias; un cosmetico aplicado)
================================================================

Fecha: 2026-08-29. OBJETIVO: el residuo del OCTAVO PATRON (acta
R3 de la fase 3b): la cola Wz > 34 quedaba declarada porque el
techo Rz de z crece 1:1 con Wz y el root de z no la cubre.

LA MATEMATICA NUEVA:
- LA PALANCA (del propio repo, espcanal x-en-z): Wz es masa
  ANIDADA EN z => cuenta en cola(z), y con rho <= phi:
  (i) suelo de cola(z): z >= (resto + Wz)/phi;
  (ii) vacuidad rho: Wz + resto > phi z es ILEGAL — esto mata
  TODO el sector Wz > phi Z2 con z <= Z2 (cobertura por
  vacuidad);
  (iii) el techo Rz acopla al reves: z <= C0 + Wz (C0 = a_hi +
  Xz + s2 + omega <= 8.698).
- LA C A TROZOS (la pieza central): en las cajas z-cola el
  minorante de c'(z) es lineal a trozos — tramo inferior
  (Wz >= Wz_lo, pendiente 1/phi; A6: criticos minimos, sup en
  extremos) y tramo superior (Wz >= z - C0, pendiente
  2/phi > 1) donde los criticos de log p son MAXIMOS (S' =
  -2(cp-1)cp/((c-z)(c-v)) < 0 — el signo OPUESTO a A6: la
  identidad -(A+B)^2 + A^2 + B^2 = -2AB) con el critico en
  forma cerrada z*^2 = Dp(Dp - v)/(cp(cp - 1)) y limite p -> 0
  en z -> oo.  GATE A8 nuevo (sympy: la identidad de S', el
  cuadrado, el numerador de S = (6 + 2 sqrt 5)[Dp(Dp - v) -
  cp(cp-1) z^2], el limite).  Candidatos del sup: z_lo,
  min(z_hi, z_kink), z_kink, z* (si cae en el tramo), z_hi si
  finito.  SIN la c a trozos, la esquina z -> oo del tramo
  inferior tiene c - z < 0 y clampa a pi: nada certificaria.
- COLAS POR TECHO-DE-ROOT (el patron cola_v aplicado a z y Wz):
  root [1, Z2 = 42.698] x [34, phi Z2 = 69.087]; la caja que
  toca el techo del root certifica el rayo (z_hi/Wz_hi = INF).
  Cobertura del complemento {Wz > 34}: el rectangulo + las
  cajas-cola (los puntos z > Z2 tienen Wz >= z - C0: la
  ventana z_hi = min(zh_eff, C0 + Wz_hi) los liga) + la
  vacuidad rho (Wz > phi Z2 con z <= Z2).
- t_ac/t_gl = pi si z_hi >= INF/2 (piso_z degenera en float:
  1e18 + x == 1e18) — la acoplada t_c decide sola.

ATRIBUCION INSTRUMENTADA DESDE EL ARRANQUE (leccion 17):
- SUPZ_N: el sup del par (z, v) se alcanza en el codo z_kink
  en el 100% de las llamadas (75/75 por banda) — la c a trozos
  ES el mecanismo.
- El suelo de cola(z) resulto INERTE (contrafactual
  CC_3E_OFFSUELO=1: bandas identicas) — queda activo y
  documentado como refuerzo inerte en header/D.  La leccion
  17 rinde: la palanca anunciada (el suelo) no decide; decide
  la c a trozos + la cola de Y con Wz_lo (c' >= 36.75).

LA RONDA (sexta de lemaA4; la sesion del referee se atasco
—watchdog 600s— TRAS escribir el veredicto en sus notas):
- A 8/8 y C 4/4 (con (a3): 300 sondas de verdad en la cola,
  rho-legales, 0 violaciones de corona_suf) reproducidos.
- Las 5 bandas reproducidas EXACTAS: omega {[0,0.4],[0.4,0.8],
  [0.8,1.05],[1.05,1.15]} = 1 caja / 1 certificada (el ROOT
  ENTERO certifica de una: la cola es holgada — z_lo >= 22.9,
  c' >= 36.75, theta_peor ~ 0.75 rad en el codo, verificado A
  MANO por el referee: el 1-caja es creible, no vacuo — el
  True es de motor, j = 0 siempre pasa por _prueba);
  [1.15, 1.6] = 1 caja / 0 certificadas con LAMINA_N = 1 (la
  unica caja esta EN L de verdad: declarada limpia).
- VALIDACION BRUTA de _sup_pz: 4000 escenarios aleatorios
  (z_hi finito e infinito, kink dentro/fuera del intervalo,
  K/v/omega variados) x grid denso de 4000 puntos por
  escenario: 0 fallos — los candidatos son completos.
- Verdad en los bordes de cobertura (z > Z2 o Wz > phi Z2):
  120 sondas propias del referee + 60 doble-cola del
  coordinador (probe3e) + 300 de C(a3): 0 violaciones.
- Regresion hojas [12,34]x[1.05,1.15] con COLAZ=0: 905/301
  IDENTICA (el modo es no-op fuera de si mismo) y el assert
  COLAZ ^ PADRES funciona.
- El MENOR autodeclarado (caja degenerada Wzl > Wzh devolvia
  True) NO se reprodujo en la forma del referee (dio None);
  cosmetico — bnb no genera degeneradas.  Guard anadido de
  todos modos tras el veredicto (crit_k2 devuelve None).

VEREDICTO DEL REFEREE: CONFIRMADO (sin correcciones
obligatorias).  EL CLAIM QUEDA: k >= 2 HOJAS con Wz > 34
certificado para omega <= 1.15 y Wv completo (con su cola
W-uniforme); la lamina [1.15, 1.6] declarada como en hojas.
RESIDUOS DECLARADOS Y SONDADOS: los padres fuera de su dominio
3d (Wv > 8 u omega > 1.05 u Wz > 34), la banda omega
[1.15, 1.6], la cola omega > 1.6, la pesada.

LECCION 18: cuando el residuo es "el root no cubre", mirar si
una LIGADURA del modelo (aqui rho <= phi via cola(z)) acota el
sector no cubierto — la cobertura puede completarse por
vacuidad + acople sin agrandar el barrido; y el sup de una
cota lineal A TROZOS exige re-derivar el argumento de extremos
POR TRAMO (el signo de S' se invierte con la pendiente > 1:
los criticos pasan de minimos a maximos y aparece z*).

----------------------------------------------------------------
NOTA DE EXPERIMENTO (post-3e, leccion 16 aplicada otra vez): el
flag CC_TROZOS=1 activa la C A TROZOS del 3e en modo HOJAS (el
acople Wz >= z - C0 del techo Rz vale en TODO punto real).
Re-test del corte: la banda [8,12] x omega [1.15,1.25] (la que
fallaba en el 3c) NO cierra tampoco con la c a trozos — la caja
sin resolver (omega ~ 1.24, z ~ 4.05, Wv ~ 8.5, Wz ~ 0) es la
familia diametral-saturada de la lamina, donde z_hi ~ C0 y el
tramo superior casi no existe.  CONFIRMA la historia del 3b: la
franja [1.15, 1.6] es estructural/coste de maquina, no carencia
de la maquinaria nueva.  El flag queda documentado (default 0:
los conteos del manifiesto no cambian; sound — auditado como
parte del 3e, donde TROZOS = COLAZ).
----------------------------------------------------------------

================================================================
ACTA — CICLO 3g DEL LEMA DE |A|: EL TRAMO OMEGA > 1.6 DE k >= 2
(lemaA4.py, modo CC_OMEGA=1) — PROVISIONAL: claim parcial verde
con el cotejo del coordinador; EL SELLO ADVERSARIAL PENDIENTE
(el referee cayo por limite semanal de gasto, reset 2026-09-02)
================================================================

Fecha: 2026-08-29. OBJETIVO: el residuo omega > 1.6 del canal
k >= 2 (el patron espomegacanal como esperanza heredada).

EL CLAIM (PROVISIONAL hasta el sello): k >= 2 HOJAS con omega
in [1.6, 2], j_v <= 1 (Wv < 2 x_floor - 0.1; el resto de la
masa k >= 2 anidado en z via Wz <= 34), certificado por bandas:
[1.6, 1.75] x Wv [0, 4] eps 3e-2 = 149575/15294; [1.75, 2] x
Wv [0, 4] x s2 {[0.45, 1), [0, 0.45]} eps 4e-2 = 340027/75593
y 398697/59617; Wv [4, 34] x [1.6, 2] = 1 caja TODA EN L (con
x_floor <= (1+phi)/phi = 1.618, Wvl >= 3.14 es siempre lamina:
la cobertura de Wv alto y su cola es la declaracion).
Sobre-verificacion no reclamada: [2, 2.3] x s2 [0.45, 1) verde
1255241/347710.

LOS DOS HALLAZGOS (el valor central del ciclo):
1. LA LAMINA ES OMEGA-INVARIANTE: la caja mala de CADA banda
   omega > 1.6 es la MISMA familia x_2 -> x_1 con c' al suelo
   z + x_1 del tramo [1.15, 1.6] (diagnostico probe3g +
   asintotica z ~ 2w, x_i ~ T ~ w: el ratio del par -> 1
   exacto).  EL RESIDUO SE UNIFICA: j_v >= 2 es UNA lamina
   para todo omega > 1.15, no dos residuos.  El patron
   espomegacanal NO porta a k >= 2 (en k <= 1 el unico extra
   es el par exento; con dos, el segundo par diametral no
   tiene donde ir).
2. EN EL TRAMO ALTO EL SUELO-PAR ES IRREALIZABLE en parte del
   dominio: 67/228 sondas j_v >= 2 con Y al suelo-par NO caben
   por corona_suf (todas caben con holgura 1.2; 0 violaciones
   de verdad).  El suelo real de Y es la capacidad c* del
   CONJUNTO {z, x_1, x_2, m, s2} — una pared de NECESIDAD
   (min sobre ordenes circulares de sum theta_w consecutivos
   > 2 pi => la corona no cabe => c' real mayor) que el
   criterio no conoce.  ES LA CONTINUACION NATURAL: la pared
   c* cerraria la lamina unificada donde muerde.

LA CONSTRUCCION: roots escalados con w_hi (a_top = 2 + XP_MAX
+ w_hi, z_top = a_top + XZ_MAX + 1 + w_hi + wz_hi — la clase
de gap "3 omega" que la primera ronda de espomegacanal cazo);
crit_k2 omega-generico (auditado: X_m clampada, ventanas +w,
techo_nodo, c_lo — nada asume w <= 1.6); lamina por SUELO
Wvl >= 2 x_floor - 0.1 (margen 0.1: la frontera es movil; las
cajas con Wvh < 2 x_floor certifican por vacuidad de conteo
del j = 2 — sin huecos de cobertura); y LA EXENCION MOVIL del
motor (cambio global): el clamp UNICO de la fila 0 se exenta
sea cual sea el nodo (la antipodal es legal por convivencia
c' >= z + x para todo circulo de v, c' >= 1 + z para m — la
misma justificacion del par (0,1); swap del nodo al indice 1
porque la colocacion antipodal del motor es (0,1) fija); DOS
clamps = False honesto (dos antipodales del mismo z se
solapan); bloques excluidos; bolsillo omitido con swap.

LA RONDA (interrumpida): el referee verifico la REGRESION
COLAZ intacta y lanzo la reproduccion de la banda-claim antes
de caer por el limite semanal de gasto de la cuenta (tercera
caida de la campana; esta no recuperable hasta 2026-09-02).
EL COTEJO DEL COORDINADOR (documentado, pendiente de sello):
- El FATAL-potencial (la exencion movil es cambio de motor
  global: conteos del manifiesto stale?): 4 bandas de
  regresion IDENTICAS — hojas [12,34]x[1.05,1.15] 905/301,
  [0,4]x[1.05,1.15] 6479/1866, [4,8]x[1.05,1.15] 3509/959
  (las duras del corte, donde mas dispararia) + COLAZ por el
  referee.  El manifiesto NO esta stale.
- Soundness de la exencion movil: el indice 0 es z en toda
  variante; los nodos exentables (extras, m, s2, escalones
  padre) conviven todos con z en v; bloques excluidos por
  jj not in Ds; el swap intercambia filas Y columnas
  (simetria preservada).
- Cobertura de la lamina por suelo: declarar por suelo nunca
  deja huecos (toda hoja del arbol o declara o certifica).
- Roots: a <= 1 + s2 + Xp + w <= a_top; z <= a + Xz + s2 + w
  + Wz <= z_top.  Re-derivados.
RESIDUOS DECLARADOS Y SONDADOS (a4: 0 violaciones de verdad):
la lamina j_v >= 2 UNIFICADA (todo omega > 1.15), omega > 2
con j_v <= 1 (coste de maquina), el cruzado omega > 1.6 con
Wz > 34, los padres fuera de su dominio, la pesada.

PENDIENTE AL RESET (2026-09-02): el sello del referee sobre
(1) la exencion movil (abuso de swap, convivencia), (2) la
reproduccion de bandas, (3) el hallazgo c* con generador
propio.  EL PAPER Y EL TAG v1-arxiv NO SE TOCAN hasta el
sello — el bundle arXiv queda en el estado sellado del 3e.

LECCION 19: un residuo heredado con nombre de patron
("espomegacanal") no es un plan — el patron puede NO portar
(k <= 1 vs k >= 2 difieren en un par diametral); y cuando dos
residuos comparten la caja mala, unificarlos es mas valioso
que cerrar un tramo mas.

================================================================
ACTA — CICLO 3h DEL LEMA DE |A|: K >= 2 DEL CANAL PESADO
(lemaA5.py) — PROVISIONAL: 16 bandas verdes con el
auto-contraste del coordinador; EL SELLO ADVERSARIAL PENDIENTE
(mismo bloqueo que el 3g: limite semanal, reset 2026-09-02)
================================================================

Fecha: 2026-08-29. OBJETIVO: el ultimo residuo de CELDA del
canal — la ESP PESADA (SS >= 1 + s2) con k >= 2 extras
(espcanalp certifico k <= 1; k >= 2 estaba declarado con la
pinza de colas).

EL CLAIM (PROVISIONAL): k >= 2 PESADA certificada en omega in
[0, 1.15] (lamina [1.15, 1.6] declarada POR SUELO, 1 caja en L
limpia), extras HOJA, Wz <= 34 por dominio, Wv completo con su
cola W-uniforme.  16/16 bandas verdes (omega {[0,0.4],
[0.4,0.8], [0.8,1.05], [1.05,1.15]} x Wv {[0,4], [4,8],
[8,12], [12,34]}): 12997/4124, 22301/8044, 18149/6149,
31359/10735; 22481/6763, 45673/14576, 34481/10597,
73939/23835; 23871/7102, 58357/17621, 32723/9883, 82467/26459;
20489/5608, 43989/12617, 20705/6173, 56731/17741.
NOTABLE: la pesada pasa [1.05, 1.15] LIMPIA a la primera — mas
docil que la ligera (cuyo corte costo dos ciclos): T_p es
generoso y z es chico (Z_MAX_P ~ 8.2 sin Wz).

LA CONSTRUCCION (lemaA5.py, 12 dims: w, s2, SS, b, Xp, Xz, Xm,
a, z, mu, Wv, Wz):
- LA PARED PESADA POR-EXTRA (el enunciado A1p, la pieza a
  adversariar): la derivacion A7 de espcanal (greedy A/B hacia
  el agujero de x) aplica A CADA extra por separado — el
  desbloqueo mueve solo B, children(x_i) y A (en fila a D_m,
  lem:row), los demas extras no se tocan: todo extra HOJA
  cumple x_i < T_p = omega + SS - 1 + min(b, 1) + X_x.  El
  analogo exacto del techo T ligero (A2iii, por-extra).
- La particion colapsada a beta (espcanalp adversariado):
  b > 1/2, piezas de A <= min(b, phi/2), A por MASA como
  bloques partibles en la corona; bl = max(bl, 1 - bh); la
  corona pesada NO lleva nodo s2 (sigma2 vive en la particion;
  B* <= 1 al agujero de D_m, patron k = 1).
- Ventanas pesadas (a_hi = 1 + (SS - b) + Xp + omega) + el
  aparato de lemaA4 entero (variantes AND j_v, escalones con
  T_p, cola Wv W-uniforme, cota acoplada A6, exencion movil
  del 3g).
- LA PIEZA NUEVA DEL CICLO — ESCALONES EXACTOS HASTA J_ESC = 8:
  el bloque j >= 6 por cuerda de lemaA4 NO cabe en la pesada
  (T_p ~ 2.4 vs T ligero ~ 1.4: cap del bloque alto, la cuerda
  paga Wv entera al cap y la banda [0.4,0.8] x [8,12] se
  atascaba en 795k cajas); con j_max <= 8, cada j real va con
  su fila AND de escalones exactos (sound: la variante j cubre
  j_real = j; sin doble conteo — escalones PUROS por variante,
  no escalones+bloques) y el centinela 99 (bloques por cuerda)
  solo si j_max > 8 (cola Wv).  La banda atascada paso a
  34481/10597 — mas barata ademas.

AUTO-CONTRASTE DEL COORDINADOR (pendiente de sello):
- C(a): 300 coronas pesadas reales (la familia S con ocupantes
  W extra — SS = s1 + s2 + sum(W) >= 1 + s2, alcanzable solo
  asi: el primer generador con S = {s1, s2} producia 0
  instancias, corregido —, la PARTICION REAL greedy B* <= 1
  con b > 1/2, extras repartidos v/anidados, piezas de A
  explicitas): corona_suf 0 violaciones.
- Verdad j_v = 6..8 (el camino nuevo de escalones): 150
  sondas, 0 violaciones.
- El borde b -> 0.5 decide (False conservador, sin colgarse);
  la caja cola_v (j_max = 1e6, j = 99 activo) certifica.
- La banda declarada [1.15, 1.6]: 1 caja, toda en L, 0
  certificadas — declaracion limpia.
- A 4/4 (enunciados A1p/A2p/A3p/A4p), C 2/2, D verde.

RESIDUOS DECLARADOS: la lamina [1.15, 1.6] (por suelo; la
misma familia omega-invariante del 3g se espera aqui), omega >
1.6 (hallazgo 3g: espomegacanal no porta a k >= 2), padres
(anidados en extras), Wz > 34 (sin el modo cola-z portado), y
las continuaciones de la ligera.

PENDIENTE AL RESET (2026-09-02), ronda adversarial completa:
(1) LA PARED A1p por-extra (la derivacion A7 con k >= 2:
atacar la independencia del desbloqueo respecto de los demas
extras — es EL enunciado nuevo del ciclo); (2) los escalones
exactos j <= 8 (sound por variante-AND? el j real = 7 con la
fila de 7 escalones); (3) la corona sin nodo s2 y B* al
agujero de D_m (portado de k = 1: re-derivar); (4) el
generador C (la particion greedy = la real?); (5) bandas con
conteos.  EL PAPER Y EL TAG v1-arxiv SIGUEN CONGELADOS (estado
3e) hasta los sellos de 3g y 3h.

================================================================
ACTA — CICLO 3i DEL LEMA DE |A|: LA PARED c* DE NECESIDAD Y LA
SUBIDA DEL CORTE A OMEGA <= 1.25 (lemaA4.py, CC_CSTAR=1) —
PROVISIONAL (sello pendiente del 2026-09-02, con 3g y 3h)
================================================================

Fecha: 2026-08-29. OBJETIVO: la continuacion identificada en el
3g — la pared c* del conjunto — contra la lamina j_v >= 2.

LA PARED c* (la matematica nueva): los circulos {z, x_1..x_j,
m} (y s2 si su suelo es real) DEBEN convivir en la corona de v
del ocupante.  Con los radios a SUELO: si NINGUN orden circular
admite sum theta_w(consecutivos; c) <= 2 pi, la corona no cabe
en capacidad c y c' real > c.  TRES MONOTONIAS la hacen sound:
(i) toda colocacion valida induce un orden con separaciones
consecutivas >= theta_w y suma 2 pi (condicion NECESARIA — la
suficiencia no se usa); (ii) radios reales >= suelos =>
theta_w reales mayores; (iii) theta_w decrece en c => el test
es monotono y la BISECCION da c* (subestimarlo es sound: 22
pasos).  El test: n <= 6 el min EXACTO por permutaciones
((n-1)!/2 <= 60, con poda temprana); n > 6 la cota inferior
TSP-half (sum_i dos-menores-de-la-fila-i / 2 <= min sobre
ordenes).  DOBLE USO: la VACUIDAD (si refuta en el TECHO de c'
— la pinza RY — la variante j no tiene puntos reales: la
corona de un ocupante real siempre cabe; el reverso
constructivo del hallazgo 67/228 del 3g) y el RESCATE (si la
variante falla en c_lo se re-prueba en c*: los theta del
mayorante en c* siguen mayorando porque c' real >= c* y
theta/cuerdas decrecen/mayoran en c).  Los suelos del
conjunto: z_lo, max(x1_lo, x2a), x2a, x_floor x (j-2), 1.0,
y s2l SOLO si > 1e-3 (inflar un suelo romperia la necesidad:
se omite — omitir afloja, sound).
+ LOS ESCALONES EXACTOS J_ESC = 8 portados del 3h BAJO CSTAR
(el bloque-cuerda j >= 6 era el fallo de la caja historica del
corte; cada j real <= 8 con su fila AND; el centinela 9 por
bloques solo con cola Wv).  CON CSTAR=0 EL CAMINO SELLADO
QUEDA INTACTO: regresion 905/301 y 6479/1866 IDENTICAS.

EL RESULTADO: EL CORTE DE HOJAS SUBE DE 1.15 A 1.25 — la
franja [1.15, 1.25] ENTERA verde (CC_CSTAR=1 CC_WCORTE=1.25):
[8,12] 2771/877; [4,8] 6529/1784; [12,34] 2323/736; [0,4] en
tres tramos de s2 ([0.45,1) 6159/2041, [0.22,0.45] 5283/1733,
[0,0.22] 1447/417).  Quince delimitaciones fallidas (3b), el
3c y el 3f no la habian movido de 1.15.  SOBRE-VERIFICACION
no reclamada: [1.25,1.4] x {[8,12] 5071/1481, [12,34]
5613/1652} verdes; [1.25,1.4] x Wv bajas no caben en el
presupuesto de maquina (el corte se queda en 1.25 —
declaracion por suelo con CC_WCORTE, como siempre).

LA ATRIBUCION (leccion 17, instrumentada de serie — CSTAR_N):
- LOS ESCALONES EXACTOS deciden la mayor parte: [8,12]
  2771/877 con CERO llamadas al rescate (la caja historica
  del corte caia por el bloque-cuerda, no por c*).
- LA PARED c* decide en las Wv BAJAS: [0,4] con 34-36
  rescates exitosos (~700 intentados) en s2 altos y 29 en s2
  bajos — sin ella esas bandas no cierran.
- En [4,8]: 126 rescates intentados, 0 exitosos, y cierra por
  otras vias — c* muerde pero no decide alli.
- El coste del c* es sensible: moverlo a ultima-oportunidad
  ROMPIO la banda buena (el rescate temprano evita miles de
  sub-bandas); quedo temprano con biseccion abaratada.

AUTO-CONTRASTE (pendiente de sello, con la lista 3g/3h):
regresion sellada intacta; la vacuidad-techo no disparo en
ningun run (0 en todos los contadores: la pared vacia esta
ahi para el referee, no reclamada); sondas de la lamina (a2,
[1.05, 1.6]) siguen verdes en C.  PUNTOS DE ATAQUE para el
referee: (1) la necesidad del min-orden (el argumento de que
toda colocacion induce un orden — con BLOQUES en la corona el
conjunto c* NO los incluye: omitidos, sound); (2) el rescate
re-evalua _prueba con c_st — verificar que TODAS las piezas
del mayorante (cuerdas de bloques incluidas) mayoran en c_st;
(3) la poda de reflexion en permutaciones (perm[0] >
perm[-1]); (4) reproduccion de la franja.

RESIDUO NUEVO DEL CORTE: [1.25, 1.6] (antes [1.15, 1.6]) — y
la lamina unificada j_v >= 2 de omega > 1.6 sigue (la pared
c* NO la cierra alli: los conflictos del tramo alto son de
presupuesto con c al suelo del trio, no del conjunto-suelo).
PAPER Y TAG CONGELADOS (estado 3e) hasta los sellos.

================================================================
ACTA DE SELLOS — LA RONDA TRIPLE (3g, 3h, 3i): LOS TRES CICLOS
CONFIRMADOS; EL 3i CON SELLO PLENO TRAS LAS CORRECCIONES
================================================================

Fecha: 2026-08-30 (la ronda pedida al reset adelantado del
limite).  El referee verifico HEAD 43d18f2 (arbol limpio por
md5/diff) y despues el re-cotejo sobre el codigo corregido.

CICLO 3g — CONFIRMADO (sello): la EXENCION MOVIL es SOUND
(permutacion del swap coherente; legalidad por tipo de nodo;
>= 2 clamps = False conservador; SPY sobre 11261 cajas: 12099
llamadas, 9105 exenciones, 0 matrices asimetricas); la
regresion sellada reproducida por el referee EN HEAD (905/301,
3509/959, 6479/1866 + COLAZ); el claim [1.6, 2] j_v <= 1 con
[1.6,1.75] reproducida exacta y la lamina Wv >= 3.14 derivada
por el referee; la omega-invariancia RE-DERIVADA (p = 1 exacto
en c = z + x_1, scale-free) y el c*-irrealizable reproducido
con SU generador (11/250 — la tasa depende del generador, el
fenomeno es robusto).

CICLO 3h — CONFIRMADO (sello): A1p (pared por-extra) con la
estructura thm:oblivious de la ligera; T_p mayora la
reconstruccion del referee del desbloqueo; B* <= 1 al disco
D_m re-derivado; cap_A resuelto POR EL REFEREE con margen
(toda pieza de A <= sigma2 <= phi - 1 < phi/2); escalones
J_ESC = 8 sin huecos y centinela 99 correcto (el codigo hace
lo sound; el texto del commit era impreciso); tres bandas
reproducidas exactas (incluida la atascada 34481/10597); su
sonda j 6..9 con particion real 160/0.  EL MENOR (A_MAX_P):
APLICADO — MASA_A_MAX = 1.079 con la derivacion del referee
(masa_A <= 2 phi/3, extremo en b = phi/3 con |A| = 2; el
techo viejo 0.999 cubria el claim solo por el slack
W_MAX - W_CORTE); el manifiesto pesada 16/16 RE-CORRIDO con
la constante (12923/4099, 22231/8007, 18003/6099,
31049/10606, 22185/6640, 45105/14312, 33915/10314,
72113/23030, 23439/6931, 56321/16738, 31485/9404,
79269/25131, 20367/5558, 42083/12081, 19193/5643,
53495/16830) — banda 1 verificada por el referee.

CICLO 3i — SELLO PLENO tras dos correcciones MAYORES:
- C1 (derivacion): el test por theta_w consecutivas era FALSO
  como lema general — el APILAMIENTO RADIAL (c >= r1 + 2 r2)
  da gamma real 0.  Sin bite empirico (50k tests sinteticos +
  el replay de la banda de rescates: 4349 refutaciones
  reales, 0 divergencias con cabe_algun_orden — los
  certificados estaban sanos), pero la derivacion se corrigio
  DELEGANDO la refutacion en el aparato adversariado del repo
  (cabe_algun_orden de coronacolas: gamma_min con apilamiento
  + subconjuntos + confinamiento del gigante), con el GATE A9
  nuevo (el caso apilable [3,1,1] certifica; la monotonia en
  c de la biseccion verificada) y una PRE-CRIBA de coste
  cuya unica salida activa es no-refutar (solo-ahorro,
  verificado por el referee).  La franja [1.15, 1.25] ENTERA
  re-corrida con el codigo final y REPRODUCIDA 8/8 por el
  referee: 2771/877, 6529/1784, 2323/736, 1447/417,
  5283/1733, 7153/1997, 10339/3191, 4903/1078.
- C2 (acta): un tramo del acta provisional no reproducia
  (transcripcion/invocacion no documentada) — el acta queda
  sustituida por los conteos del binario final (arriba).
- EL MENOR DEL RE-COTEJO (atribucion, tercera aparicion del
  patron): los contadores de rescate del mensaje del
  coordinador eran de la variante sin pre-criba.  DEL BINARIO
  FINAL: [0,4] x s2 [0, 0.22] = 672 rescates / 29 exitosos
  (identico al pre-fix: criba INTERSECCION confirmador = las
  refutaciones viejas, coherente con el replay 4349/0);
  s2 [0.45, 1) x omega [1.15, 1.2] = CERO rescates (la
  biseccion interna de x_2 salva las mismas sub-bandas);
  [4, 8] = 126/0.  Los conteos de CAJAS son identicos en los
  tres casos: el arbol externo es robusto al mecanismo
  interno.  LA ATRIBUCION HONESTA FINAL: la pared c* decide
  en [0,4] x s2-bajos (29 exitosos, sin ella no cierra); en
  el resto deciden los escalones J_ESC = 8 y la biseccion.
LECCION 20 (de la prescripcion del referee): los contadores
de atribucion se regeneran EN EL MISMO RUN que produce los
conteos sellados — nunca de runs intermedios.

CLAIMS SELLADOS TRAS LA RONDA TRIPLE: (1) hojas ligeras
k >= 2 con OMEGA <= 1.25 (Wv completo con cola, Wz completo
via 3e), lamina [1.25, 1.6] declarada; (2) omega in [1.6, 2]
con j_v <= 1; (3) la PESADA k >= 2 completa en omega <= 1.15
(hojas, Wz <= 34, Wv completo).  RESIDUOS: [1.25, 1.6] y la
lamina unificada j_v >= 2 en omega > 1.6; omega > 2 (j_v <=
1); los padres fuera de su dominio; los cruzados de Wz-cola;
la pesada fuera de su dominio.
