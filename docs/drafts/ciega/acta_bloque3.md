# Acta de revisión — BLOQUE 3: «The width program: profile thresholds and the 13/7 corner»

Referee externo. Objeto: `paper/main.tex` líneas 686–808 (sección) y 1556–2138 (apéndice
`app:widthproofs`). Contexto usado: resto de `main.tex` (en particular `app:rigidproof`,
líneas 1359–1554, del que este bloque importa S1/S2/S5/S6a) y `code/`. No se consultó `docs/`.

Método: (a) lectura par-a-par enunciado-vs-prueba de los 10 resultados del apéndice contra los
enunciados de la sección; (b) re-derivación independiente con sympy de todas las identidades y
polinomios del bloque (script propio `verif_bloque3.py`, 36 checks; los 3 «FAIL» iniciales fueron
artefactos del arnés propio, corregidos y re-verificados); (c) contraste numérico por fuerza bruta
del umbral de 3 anillos y del programa de bloqueo completo; (d) ejecución del script del autor
(`code/esquina.py`, 5/5 bloques OK).

## VEREDICTO GLOBAL

**Sólido. Aceptar con correcciones obligatorias menores.** Ningún hallazgo fatal. Toda la
matemática sustantiva del bloque se re-derivó y confirmó de forma independiente: la fórmula
cerrada de ρ*₃, la reducción ρ*ₖ = ρ*₃, el cruce combinatorio ω_T, la frontera cerrada en
coordenada t, la identidad κ, el cierre Tribonacci, la rama del testigo Φ, la curva de tres ramas,
el polinomio P de bigrado (6,2) con sus dos identidades de corte (coeficientes de Q5 exactos), la
esquina 13/7 con las cuatro paredes saturadas, y la estructura fina (bump 1.1·10⁻⁴ en
ω_peak = 0.0444700). Las etiquetas son honestas: la curva se declara «proved lower bound», la
igualdad solo se reclama donde la rigidez la respalda, y el 13/7 es genuinamente incondicional
(solo usa la dirección constructiva del criterio angular). Sin circularidades. Tres correcciones
obligatorias, todas de reparación trivial.

## Veredicto por sección

### Sección (686–808)
- **Convención de anchura y régimen ω≥1 (697–707)**: coherente. Verifiqué que la prueba de la
  esquina para ω ≥ 1/7 usa solo (B1)+(W) (sin H_m), como declara el paréntesis. OK.
- **Capa combinatoria (726–748)**: ρ*₂ = max(1, 2(1−ω)) — probado (Cpair, revisado caso a caso).
  ρ*₃ fórmula cerrada — probada (Ctrichar + Ctrio, revisadas rama a rama; contraste por fuerza
  bruta en 17 valores de ω: el ínfimo bruto se aproxima a la fórmula siempre por arriba, gaps
  +0.003…+0.03, consistente con ínfimo no alcanzado). ρ*ₖ = ρ*₃ — la dirección (≥) es correcta
  paso a paso; la dirección (≤) tiene el defecto O2 (polvo igual, reparable en una línea).
  ω_T = 1/T−1/2 = T²−T−3/2 = 0.0436890 — identidad verificada módulo la cúbica de Tribonacci. OK
  con O2.
- **Plantilla canónica (750–786)**: las cuatro paredes son cada una la contrapositiva de una
  colocación explícita de desbloqueo (revisé además que no faltan paredes necesarias para la
  genuinidad: σ₁ en H_m, ambos en D_m y el anidamiento σ₂⊂σ₁ están implicadas por (B2) y la
  banda). Frontera cerrada, κ, T_{1+ω}, Φ y sus propiedades: todo verificado simbólicamente.
  La distinción «lower bound probado / igualdad exacta en testigo y esquina / caveat angular en
  las otras dos ramas» es honesta; ver R1 sobre la igualdad del testigo. OK con R1.
- **Teorema 13/7 (788–802)**: correcto y verificado (ver apéndice abajo). OK.
- **Estructura fina (804–807)**: numéricamente cierta (bump +1.1047·10⁻⁴, ω_peak = raíz
  0.0444699865 del factor de grado 8 de la resultante — re-derivé la resultante y coincide). OK.

### Apéndice (1556–2138)
- **Preámbulo (1556–1579)**: modelo y ρ_needed bien definidos; exactitud de dos círculos con
  necesidad probada; «solo certificados constructivos para ≥3» — es exactamente lo que hace que
  toda cota inferior sea incondicional. OK.
- **prop:Cpair (1582–1596)**: enumeración de colocaciones completa; familia gemela correcta. OK.
- **prop:Ctrichar (1598–1643)**: casos disjuntos y exhaustivos por posición de s₁,s₂ frente a β;
  ambas direcciones revisadas colocación a colocación (incluidos cadena y estrella). Habitabilidad
  de (ii) solo con ω>1/2, correcta. OK.
- **thm:Ctrio (1645–1708)**: las cuatro ramas de la minimización revisadas; los cruces exactos
  ((√5−2)/2 = φ−3/2 y ω ≤ 1−φ/2) verificados; las familias extremales satisfacen las condiciones
  de bloqueo con margen (comprobado). La observación de que ni el caso (ii) ni geometría alguna
  entra es cierta. **Colisión de notación ω₁** (O1). OK con O1.
- **prop:Callk (1710–1768)**: dirección (≥) impecable (Steps 0–3 revisados; p=1 da
  ((1+ω)+√((1+ω)²+8))/2 ≥ 2, verificado). Dirección (≤): O2. OK con O2.
- **cor:Comegac (1770–1775)**: consecuencia directa; matiz de redacción M1. OK.
- **lem:CF (1793–1844)**: la identidad de frontera re-derivada (la factorización de
  (sin A cos B)² comprobada) y contrastada numéricamente contra F = 2π (error máx 6·10⁻¹⁵ en 40
  pares (α,σ₁) aleatorios); s* y el rango de h correctos. OK.
- **thm:Ckappa (1846–1877)**: t′ = −1/(2√g), G′ y G(1/√2) = 8/81 verificados; el argumento por
  casos con σ < 1/√2 es correcto y la holgura κ² > 6 real. OK.
- **cor:Cmin (1879–1904)**: mínimo en (1, b(α)) confirmado numéricamente para 5 α; identidades
  polinómicas de signo verificadas; compacidad implícita correcta (F(σ₁,0⁺) < 2π mantiene la
  región lejos de σ₂ = 0). OK.
- **prop:Cwitness (1925–1953)**: Φ′ re-derivada por diferenciación implícita: coincide; la
  reducción del denominador a 7T²+4T+3 módulo la cúbica, verificada; concavidad y cuerda-tangente
  correctas; T_{8/7} = 2 exacto. La «attainment in the limit» requiere genuinidad no escrita (R1).
  OK con R1.
- **lem:CE1 (1970–2007)**: la linealización de (B1) en coordenada t es legítima en toda la banda
  (equivalencia de niveles por monotonía, comprobada); los tres casos y las monotonías en α
  (incluido el caso c₄ móvil con el G-lema) revisados. OK.
- **prop:Ccurve (2009–2071)**: rama H_m — la juntura s*(2−ω) = 1−ω da exactamente la cúbica
  4ω³−20ω²+25ω−1 (numerador re-derivado, coincide signo incluido; derivada (5−2ω)(5−6ω)
  verificada); rama mixta — la equivalencia (W) ⟺ Ξ(α) ≥ t(1−ω) es correcta, pero la monotonía
  estricta de Ξ se afirma sin prueba (R2; la verifiqué: se reduce a un polinomio sin raíces en
  (1,2)); rama del testigo — correcta, con la observación de que el argumento vía Cmin ya mata
  todos los α < T_{1+ω} de una vez. El polinomio P: **re-derivado desde cero** elevando al
  cuadrado dos veces; es exactamente el factor irreducible de bigrado (6,2) y las dos identidades
  de juntura/corte del paper salen con constante 1 (misma normalización). Contraste global: mi
  programa numérico coincide con las tres ramas en 13 valores de ω (desvío máx 2.5·10⁻⁵, malla).
  El tope 0.30 no se explica (M3). OK con R2, M3.
- **Prueba de thm:corner (2073–2122)**: cobertura completa de ω > 0 por el split α ≥ 2 / α < 2
  (verificada); la factorización P(13/7+ω, ω) = 4(7ω−1)Q5/7⁶ **confirmada coeficiente a
  coeficiente**, y Q5 tiene única raíz positiva 0.00072543, ninguna en [1/25, 1/7] (aislamiento
  reproducido con raíces reales exactas de sympy); V(ω₁) − 13/7 = 1/7 − 2ω₁ > 0 y 2(1−ω) > 13/7
  ⟺ ω < 1/14, exactos. Genuinidad de la familia: la cita «Corollary Cmin gives σ₂ > b(α)» es
  elíptica (lo que se usa es la identidad de signo de su prueba: α > T_{1+ω} ⟹ b(α) < c₄ ≤
  σ₂ − ε/2), pero válida; la elección ε = δ²/4 frente al radio de propagación de S6a(3) es M2.
  Verifiqué la saturación simultánea de las cuatro paredes en (1/7, 2, 1, 6/7). OK con M2.
- **rem:Cbump (2124–2137)**: contenido numéricamente cierto (todo reproducido: resultante de P y
  P_α+P_ω factoriza en (lineal)·(grado 8); raíz 0.0444699865; altura +1.1047·10⁻⁴;
  V′(ω₁⁺) = +0.07214). Pero c₀ y r′ no están definidos (O3) y la «exact coincidence» es una
  sustitución trivial (M4). OK con O3, M4.

## Hallazgos

**[OBLIGATORIA] O1 — Colisión de notación ω₁.** Línea 1692 (prueba de thm:Ctrio):
«ω₁ := (√5−2)/2» ≈ 0.118; líneas 783 y 2020 (sección y prop:Ccurve): ω₁ = 0.0413570…, raíz de
4ω³−20ω²+25ω−1. El mismo símbolo con dos valores distintos dentro del mismo apéndice.
*Corrección*: renombrar el local de Ctrio (p.ej. ω_φ).

**[OBLIGATORIA] O2 — Polvo igual rompe la dirección (≤) de prop:Callk.** Línea 1715: «Dust:
append k−3 rings δ→0». Con k−3 anillos de polvo IGUALES, la cola del primero vale k−4, de modo
que ρ_needed del perfil aumentado es ≥ k−4 > ρ*₃ para k ≥ 6: la dirección (≤) falla tal como está
escrita. *Corrección* (una línea): polvo superdecreciente δ, δ², …, δ^{k−3} — todas las colas de
polvo tienden a 0 y ρ_needed → ρ_needed(testigo). (El paréntesis análogo de Ctrio caso (i), con
un solo anillo de polvo, sí es correcto.)

**[OBLIGATORIA] O3 — Símbolos indefinidos en rem:Cbump.** Línea 2129: «V′(ω₁⁺) = c₀/(r′−c₀)»
con c₀ y r′ sin definir en ninguna parte del paper. El valor numérico (+0.0721) es correcto (lo
reproduje: +0.07214), pero la fórmula es ilegible. *Corrección*: definir c₀ y r′, o sustituir por
el enunciado numérico con su certificado.

**[RECOMENDADA] R1 — Igualdad en la rama del testigo sin prueba de genuinidad escrita.** La
sección (777–778) y prop:Ccurve afirman «equality holds on the witness branch», y prop:Cwitness
«attained in the limit», pero la familia σ₁ = 1−ε, σ₂ = b(α)+ε′ solo es un bloqueo genuino si el
trío es realmente no-empaquetable; el argumento (rigidez de prop:S5 en σ₁ = 1 + propagación de
lem:S6a(3)) está escrito únicamente para la esquina ω = 1/7. Las mismas dos líneas valen verbatim
en α = T_{1+ω} para todo ω ∈ [1/7, 0.30] (α ≥ 2 mantiene el disco diametralmente lleno).
*Corrección*: añadirlas o remitir explícitamente desde Cwitness/Ccurve al argumento de la esquina.

**[RECOMENDADA] R2 — Monotonía de Ξ afirmada sin prueba.** Línea 2050: «Ξ strictly increasing on
(1,2]» sostiene la buena definición de α_m y la forma del conjunto admisible [α_m, 2]. Se reduce
a (α(α+1))³ > (2α+1)²(α−1)³(2−α) en (1,2), que verifiqué (polinomio sin raíces en (1,2), margen
enorme). *Corrección*: media línea con esta reducción.

**[RECOMENDADA] R3 — Sin puntero a los scripts del bloque.** Las afirmaciones computacionales
(aislamiento exacto de raíces de Q5, factor de grado 8 de la resultante, altura del bump) están
respaldadas por `code/esquina.py` (5/5, lo ejecuté) y `code/grosor.py`, pero el apéndice no los
cita — a diferencia de app:rigidproof, que cita `code/rigido.py` (V5) en línea 1366.
*Corrección*: añadir la cita.

**[MENOR] M1 — cor:Comegac**: «blocks with ρ = 2/(1+2ω) < T» — la familia con ε tiene ρ
estrictamente mayor; escribir «with ρ arbitrarily close to 2/(1+2ω)».

**[MENOR] M2 — Familia de la esquina**: ε = δ²/4 no se justifica frente al radio de propagación
δ₀ de lem:S6a(3); cualquier ε menor sirve y ρ → 13/7 igualmente — basta «shrinking ε if needed».

**[MENOR] M3 — El tope ω ≤ 0.30** de prop:Ccurve y de la rama del testigo no se explica en el
bloque; nada del programa se rompe ahí (comprobé que T_{1+ω} < 2+ω idénticamente: la diferencia
de cubos es la constante 1). Indicar de dónde viene el corte.

**[MENOR] M4 — rem:Cbump**: «the exact coincidence of the leading terms ((α−1)³(2−α) =
(1−ω₁)³ω₁ at α = 2−ω₁)» es la sustitución trivial α = 2−ω₁, no una coincidencia; reformular.

## Verificado en positivo (re-derivación propia, sympy + numérico)

Identidades exactas (todas simbólicas, coinciden):
- t(b(α)) = 1/√(α(α+1)); s* = 4α(α+1)/(2α+1)² con t(s*) = σ/2; t′(s) = −1/(2√(s³(1−s)));
  κ = √(g(σ₂)/g(σ₁)); G′(t) = 2t(1−3t²)/(1+t²)⁵; G(1/√2) = 8/81; holgura κ² > 6 del caso alto.
- 1+b(α)−α = −(α³−α²−α−1)/(α²+α+1) y su deformación con T_{1+ω}.
- Φ′(ω) = (2α+1)/(α²(α²+2α+3)) por diferenciación implícita (numerador reducido a 2α+1);
  Φ′(0) = (2T+1)/(7T²+4T+3) = 0.1374516 módulo la cúbica; concavidad (d/dα log Φ′ < 0);
  T_{8/7} = 2; Φ(1/7) = 13/7; cuerda-tangente en [0,1/7].
- ω_T = 1/T − 1/2 = T² − T − 3/2 = 0.0436890; 13/7 − T = 0.0178561; 2(1−ω) > 13/7 ⟺ ω < 1/14.
- Numerador de (1−ω) − s*(2−ω) = −(4ω³−20ω²+25ω−1); derivada (5−2ω)(5−6ω);
  ω₁ = 0.0413570035 ∈ (1/25, 1/14). Cruce hiperbola/aditivo en (√5−2)/2 = φ − 3/2.
- T_{1+ω} = 2−ω ⟺ 2ω³−10ω²+14ω−1 = 0; ω_× = 0.0754315; suelo uniforme 2(1−ω_×) = T + 0.0098503.
- **P re-derivado desde la ecuación de α_m**: factor irreducible de bigrado (6,2) exacto;
  P(2−ω, ω) = (ω−1)³(4ω³−20ω²+25ω−1) con constante 1; P(2, 1/7) = 0;
  P(13/7+ω, ω) = 4(7ω−1)Q5(ω)/7⁶ con los cinco coeficientes de Q5 idénticos a los impresos;
  raíces reales de Q5: {−2.5177, −2.1712, +0.00072543} — ninguna en [1/25, 1/7].
- Resultante(P, P_α+P_ω) = (lineal)·(factor de grado 8); única raíz del factor en (ω₁, 1/7):
  0.0444699865 = ω_peak.

Contrastes numéricos:
- Frontera cerrada vs criterio angular F = 2π: error máx 6·10⁻¹⁵ (40 pares aleatorios).
- cor:Cmin: min(σ₁+σ₂) = 1+b(α) en α ∈ {1.2, 1.7, 2, 2.5, 3}.
- ρ*₃: chequeador de reinsertabilidad exacto (ω < 1/2) por enumeración de bosques y colocaciones;
  en 17 valores de ω el ínfimo por fuerza bruta se aproxima a la fórmula desde arriba
  (gaps +0.003…+0.03; con polvo: +0.004…+0.008). Ningún perfil bloqueado por debajo de la fórmula.
- Programa de bloqueo completo vs curva de tres ramas: 13 valores de ω, desvío máx 2.5·10⁻⁵
  (resolución de malla); ínfimo global de la curva = 13/7 en ω = 1/7; V > 13/7 en (ω₁, 1/7).
- Estructura fina: V(ω₁) = 2−2ω₁ (juntura exacta); bump +1.1047·10⁻⁴ en 0.04447;
  V′(ω₁⁺) = +0.07214.
- Familia de la esquina: paredes (B2)(B4)(W) + banda + margen σ₂ > b(α) + infactibilidad angular
  en σ₁ = 1−ε para δ ∈ {10⁻¹…10⁻⁴}; ρ ↓ 13/7. Saturación simultánea de las cuatro paredes en
  (1/7, 2, 1, 6/7).
- Script del autor `code/esquina.py`: 5/5 bloques OK (incluye contraste angular sin coordenada t).

Estructura lógica:
- Sin circularidad: CF→Ckappa→Cmin→{Cwitness, CE1}→Ccurve→corner; S1/S2/S5/S6a importadas de
  app:rigidproof (independiente). El G-lema se usa en tres sitios siempre en el mismo sentido.
- Dirección de tolerancias: solo se usa la dirección constructiva del criterio angular
  (F ≤ 2π ⟹ empaqueta), así que la región relajada contiene todos los bloqueos y toda cota
  inferior es incondicional — el error siempre perjudica, nunca favorece, la conclusión.
- Gates falsables: mi fuerza bruta podía haber encontrado perfiles bloqueados por debajo de las
  fórmulas y no los encontró; el chequeador de reinsertabilidad es exacto en el rango usado.
- Dominios: la cobertura de ω > 0 del teorema de la esquina es completa (split verificado);
  el paréntesis del régimen sólido ω ≥ 1 es consistente con lo que la prueba usa.
