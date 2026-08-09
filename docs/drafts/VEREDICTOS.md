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
