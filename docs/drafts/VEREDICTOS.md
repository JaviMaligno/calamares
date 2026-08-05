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
