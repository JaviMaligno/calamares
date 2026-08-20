# Acta de revisión — BLOQUE 4
**Objeto:** sección «Generic containers: coronas, walls, and metallic floors» (main.tex 809–993) y apéndice «Complete proofs for generic containers» (2139–3033).
**Referee externo. Fecha: 2026-08-20.**
**Método:** lectura completa de sección y apéndice con contraste enunciado-por-enunciado; re-derivación independiente en sympy de las identidades clave (56 comprobaciones propias, script `ciega/ref_b4.py`); re-derivación a mano de las cadenas lógicas de cada prueba; ejecución de los scripts del repositorio citados por el verifmap para el bloque (`corona`, `ocupantes`, `bloqueadores`, `bolsillo`, `striple`, `batalla2`, `microcelda`, `perfilp`, `rstar` — todos en verde) con inspección de la calidad de sus gates. No se consultó `docs/`.

---

## VEREDICTO GLOBAL

**Aceptar con correcciones: 1 hallazgo OBLIGATORIO (hueco de cobertura reparable en la prueba del Teorema DP, caso j=3), 4 RECOMENDADOS, 7 MENORES.** El bloque es matemáticamente sólido en su núcleo: todas las identidades exactas que sostienen las pruebas (frontera universal, bolsillo espejo y₀=2b₂, monotonía de la línea dorada, medias metálicas y sus cruces Tribonacci, deformación dorada γ_ω, constantes de la pinza 11−4√5 y 5φ−7, rincón exacto de DPr(iv)) se re-derivaron de forma independiente y son correctas. Las cadenas de colas y paredes de los teoremas DV2, DB, DBpp, DPsij, DT3, DP(i)–(iii), DPp se verificaron paso a paso sin encontrar grietas. El único defecto de solidez es un caso no cubierto por el árbol de casos escrito de DP(iv) (j=3), para el que este referee aporta una reparación completa con las paredes ya presentes en el paper.

---

## VEREDICTO POR SUBSECCIÓN

### 1. La frontera universal y el criterio de corona (app:corona-app, 2159–2310) — SÓLIDA

- **lem:DU.** La identidad del término cruzado f(A)f(x)(1−f(A)f(y)) = AR/(R−A)²·((c−y)/y)·f(x)f(y) verificada simbólicamente; la forma seno lineal sin s = (√(AR)/c)(T_c(x)+T_c(y)) sin w verificada numéricamente a 1e−12. La lógica de dirección es correcta: (⇒) usa solo w≤π/2; (⇐) necesita s>w, que la hipótesis A≥min(x,y) provee vía monotonía. El contraejemplo R=1, A=0.01, x=y=0.45 verificado: T_c(x)+T_c(y)≤τ_R pero F<2π. T_c primitiva de −c/(2√g_c) verificada.
- **Compañeros uniformes.** b_R(A)=ARc/(AR+c²): reduce a b₂ de Descartes en R=A+B (verificado simbólicamente), creciente en R y ≤A (verificado).
- **lem:Dgaps / lem:Dsubset.** Correctos; ver F9 (admisibilidad implícita).
- **thm:Dk4.** El argumento de ciclo negativo es correcto y lo re-derivé: peso 2πU−Σθ, U=0 imposible (aristas descendentes no ciclan), U=1 exige >2 aristas y enumera exactamente los 4 tríos + el total, U=2 exigiría >4 aristas. La correspondencia ciclo-U=1 ↔ certificado de subconjunto es exacta.
- **prop:Dzigzag.** g(s)=2·arcsin(e^{s/2}): g''=e^{−s}/(2(e^{−s}−1)^{3/2})>0 verificado simbólicamente; la biyección {3 órdenes cíclicos}↔{3 emparejamientos} y la mayorización {σ₁+σ₂,σ₃+σ₄}≻ resto son correctas; Karamata cierra.
- **thm:DU4.** Dominación por pares del trío top verificada caso a caso; la linealización con hipótesis automática (A=a₁ máximo global) es correcta.
- **k=5.** El estatus del pentagrama está etiquetado con honestidad ejemplar: la redundancia geométrica se declara conjetura, «no usada», y solo se emplea la dirección incondicional de Dsubset. `corona.py` (5/5) contrasta el criterio contra un LP independiente y contra un oráculo euclídeo sin S1, con contraejemplos de slack negativo explícito (el ingenuo, el decreciente vs zigzag, el cuantificador k=5) — gates genuinamente falsables.

### 2. Paredes de ocupantes y suelos metálicos (app:walls-app + app:blockers-app, 2312–2462) — SÓLIDA

- **lem:DV1.** Cada pared es contrapositiva de una colocación explícita con recursos disjuntos y criterios exactos (par-exacto para (B4): correcto, dos círculos en disco ⟺ suma ≤ capacidad; la fila para (D)).
- **prop:DV2.** Re-derivada entera: la cadena de la cola de o₁, la monotonía en o₁ para ω≤j/2, y el ínfimo 4/(1+2ω) en o₁=½+ω para j=1<2ω (verificado por barrido: el mínimo del programa coincide). La convención de primera copia se introduce aquí y es consistente (ρ es un máximo sobre índices).
- **cor:DV34.** Los cruces 3/T−1=3T²−3T−4=0.6310 y 2/T−½=2T²−2T−5/2=0.5873 verificados (usando 1/T=T²−T−1); 13/7 para ω≤15/26 verificado por ambas ramas; la identidad (2+ω)³−(1+ω)((2+ω)²+(2+ω)+1)=1 es exacta (es (a−1)(a²+a+1)=a³−1) y da Φ<2 correctamente.
- **lem:DR.** Construcción correcta (tangencias verificadas); la reducción «si un hijo excede σ₂, la desigualdad es la misma» es cierta (misma suma total).
- **lem:DBo.** Correcto; la legalidad («positions are re-eligible») descansa en el convenio existencial de posiciones declarado en el preámbulo — consistente.
- **thm:DB.** El programa min-max re-derivado: cruce u²−(1+σ−ω)u−1=0, raíz creciente en σ, mínimo en σ=1−ω → Ψ(ω). El caso «cruce en X<0» está bien tratado (2σ excede la raíz por definición del cruce; el paréntesis algebraico Q(2σ)=2P_σ(2σ)+j≥j es exacto — lo comprobé). El nodo mínimo tiene hijos <1 por minimalidad: correcto.
- **thm:DBpp.** La dicotomía de evacuación es una colocación legal (fila σ₁+M en D_m + σ₂ en H_m vaciado); rama B re-derivada: s>1−ω por Bo''+y*≥1, dos colas → u²−(2−ω)u−1, cruce interior garantizado (Ψ_B>2−ω). Ψ_B≥Ψ por monotonía de la raíz en el coeficiente lineal: correcto. **Los cruces Tribonacci verificados exactamente**: Ψ=T en ω=(T−1)²/2 (la identidad 1−(T²−1)/(2T)=(T−1)²/2 mód T³−T²−T−1 la re-derivé — es exacta, no aproximada), Ψ_B=T en (T−1)² («el doble»), y (T−1)²T−(2T−T²+1)=T³−T²−T−1 literal. Ψ(0)=1+√2, Ψ(¼)=2, Ψ_B(½)=2, Ψ_B(1)=φ, Ψ₂(φ/2)=φ: todos exactos.
- `ocupantes.py` (5/5) y `bloqueadores.py` (6/6): contrastes por optimización/muestreo con márgenes reportados, no tautológicos.

### 3. El doble bolsillo, la línea dorada y Ψ_j (app:pocket-app, 2464–2650) — SÓLIDA con reservas de etiquetado (F3, F5, F6)

- **lem:DG.** Rigidez del par por desigualdad triangular: correcta. **y₀=2b₂ verificado simbólicamente** resolviendo el sistema de tangencias (la solución tiene y₀=±2b₂ exacto). La herencia por contención (no empaqueta en R ⟹ no en el disco α+o₁≤R) es la dirección correcta.
- **thm:DGp, rama A.** Re-derivada entera: (W)+σ₂≥1−ω → α≥1+σ₁; N(σ₁) resuelve b₂(1+σ₁,N)=σ₁ (verificado); h decreciente ⟸ (1+4σ₁)−(1+2σ₁−2σ₁²)²=4σ₁³(2−σ₁) (verificado, exacta); N(1)=√5−1, 1/g=φ/2, y ρ>φ²−(φ/2)ω. La cadena (*) con Bo'' en o₁ verificada línea a línea.
- **thm:DGp, rama B.** Las dos piezas exactas verificadas simbólicamente: ∂²b₂/∂α²=−6αo³(α+o)/D³ y D²−αo²(o+2α)=(α+o)(α³+α²o+o³) — el numerador de o−α·∂b₂/∂α factoriza exactamente así (lo comprobé), de donde f₂ decreciente. La cadena (I) re-derivada término a término (Bo'', B3', (W), DG). Autodualidad A_max(g)=2, A_max(2)=g, A_max(3/2)=3/2 verificada. La región α<o₁ exige ω<½ (o₁>1+ω≥3/2≥N₁(ω)): correcto, con N₁(½)=3/2 exacto (b₂(3/2,3/2)=1 verificado). El parche del hueco (dos cotas α-libres, verificadas ambas cadenas) y el subcaso hijo-nodo → Ψ_B(ω)>2 correcto. La celda excepcional del enunciado coincide con la de la prueba. Reservas: F3 (certificados numéricos sin etiquetar), F5 (constantes o*, õ), F6 (errata notacional c20+ωc21).
- **prop:DPsij (argumento de hojas).** Re-derivado completo: j hojas disjuntas, la mayor recoge j−1+m+σ's+W, pared Bo'' en la hoja, cruce u²+(ω−σ−1)u−j, mínimo en σ=1−ω → Ψ_j; el caso W<0 correcto (misma álgebra que DB); rama B → raíz de u²−(2−ω)u−j que domina. Cruces 0.3522/0.6240/0.8959 verificados. La nota honesta sobre ω>1 (Ψ_j cae bajo √j) es correcta y valiosa.
- **cor:DS.** El argumento de localidad es correcto para la lista dada (DV2, DB, DBpp, DPsij: solo usan D_m, H_m, agujeros de nodos/σ₁); la exclusión explícita de lem:DG («the gap lemma left open», remitido a app:campaign) es honesta. La masa en agujeros ya está contada en las X; «compatible with each theorem's template» excluye correctamente pequeños dentro de agujeros libres de DV1/DV2.
- `bolsillo.py` (6/6): contrastes SLSQP genuinos con contacto a 1e−13; el certificado simbólico f₁≡curva en o=g; controles con contacto exacto en (g,ω→1) — coherentes con mi barrido propio (peor caso 0.0094 en (g, 0.983)).

### 4. Perfiles de tres piezas (app:triple-app, 2652–2747) — SÓLIDA (F2, F4)

- **thm:DT3.** Verificado rama a rama. Rama 1: las cinco paredes son colocaciones legales con recursos compatibles (σ₃ cabalga en σ₁; el corona repack no usa D_m — consistente con el preámbulo); (B1)+(W)+cor:Cmin → ρ>Φ>T correcto en ambas ramas de la dicotomía; el subcaso σ₁+M>1 usa σ₃>ω de forma esencial (F2) y da 1+σ₁≥1+T/2=1.9196>13/7 ✓. Rama 2A: la cota (3/2)Φ−ω≥2.64 en (0,1/7] verificada numéricamente con la cota cuerda; para ω≥1/7, Φ≥13/7 por monotonía ✓. Rama 2B: **la tercera ruta al bolsillo re-derivada entera**: U₄ hacia atrás → zigzag falla → 2[θ(α,σ₂)+θ(σ₁,σ₂)]>2π → sin²A+sin²B>1 → f(σ₂)(α+1/α)>1 ⟺ σ₂>b(α) — el álgebra es exacta (f(α)=α y f(σ₁)≤1/α ⟺ σ₁≤1 en el pan R=α+1, lo comprobé). γ_ω: γ₀=φ y γ_{2/7}=2 verificados en la cúbica; 1−2b'>0 en α≥1 y 1<γ'<2 verificados (implícita numérica); el cruce de las dos colas en (γ,ω)=(2,2/7) con valor 17/7 exacto. Monotonías de las dos cotas correctas.
- **prop:DT3j.** El transporte de las paredes del par con carga anidada es correcto (la carga viaja dentro de σ₁, las colas solo crecen).
- `striple.py` (5/5) con ramas pobladas y k=4 como «hueco declarado» — etiquetado honesto.

### 5. Suelo dorado del intercambio a sartén (app:pan-app, 2749–3033) — SÓLIDA SALVO F1

- **thm:DP (i), j=1.** Re-derivado: σ_i>b(o₁) por contención+S5 para ambos i; el certificado de g decreciente (3A²+3A+1)(A²+A+1)−2A(2A+1) **es exactamente el numerador de −g'** (verificado; coeficientes 3,6,3,2,1>0); la factorización del cruce 2b(A)A=1+2b(A) ⟺ (A²−A−1)(2A+1)=0 verificada; 2b(φ)=φ y g(φ)=φ exactos. Sin uso de anchura: la extensión a ω≥1 es legítima.
- **thm:DP (ii), j=2.** La pared de bolsillos espejo re-derivada: el «iff» del cuádruple es correcto (necesidad por S5 por círculo; si b₂≥1 empaqueta, luego el fallo fuerza b₂<1); Ā(2)=√5−1 y Ā(3/2)=3/2 verificados; el cruce o₂*=√(1+2o₁)−1 es interior en (3/2,2) con igualdad exacta en o₁=2 (verificado); cobertura de los tres tramos de o₁ completa; 2/(√5−1)=φ.
- **thm:DP (iii).** El programa Ψ_B en la hoja estricta re-derivado; Ψ_B(1)=φ exacto y decreciente.
- **thm:DP (iv), j≥4.** k≥j−1≥3 hojas estrictas → Ψ₃>√3>φ: correcto sea cual sea la posición de y.
- **thm:DP (iv), j=3.** Las ramas o₂<3/φ y o₁<3 verificadas ((3/φ+3)/φ=3 exacto); y=o₁ con nodo/polvo correcta; y en el subárbol de OTRO ocupante correcta. **La pinza re-derivada símbolicamente al completo**: (C1)–(C4) exactas, umbral (6φ−1)/(2φ+1)=11−4√5=15−8φ (verificado), extremos φ+3 y φ³=2φ+1, el hijo-nodo de v* forzado para s≤6−2φ=(2φ+4)/φ² (verificado). El argumento es ajustado y correcto **en su dominio declarado (y hoja fuera del subárbol de o₁)**. → **F1: la configuración «y hoja estrictamente dentro del subárbol de o₁» no está cubierta por ninguna rama escrita** (ver hallazgo).
- **thm:DPp.** (i) el porte con W en la fila es legal (σ_j+W≤1) y las colas engordan; (ii) correcto vía DR; (iii) trivialmente correcto (Σ>φ); (iv) programa Ψ_B correcto con q̃>1−ω; (v) verificado: φ−1<2/3=b(1)≤b(o₁), bolsillos disjuntos, bloqueo imposible; (vi) el caso mixto está comprimido pero la matemática cierra (F10), y la astilla fuerza ω>2−φ usando la hipótesis pesada Σ>1+σ₂ correctamente.
- **thm:DPr.** Etiquetado con honestidad («Proof sketch and verification», «computer-assisted»); el criterio mural es correcto en la dirección usada (suficiencia; camino más largo en el DAG de restricciones de diferencia = enunciado exacto) y la corrección del pentagrama frente a arcos adyacentes está bien traída. **Re-derivé exactamente dos de sus afirmaciones**: sup(s'−(φ−1)Σ)=5φ−7 (alcanzado en σ₁=σ₂=σ₃=φ−1, ω→1; margen 23−14φ) y el rincón de (iv): con o₂=2/φ, o₁=2, R̄=2φ, sin²(θ(o₂,m)/2)=½−√5/10 y sin²(θ(m,o₁)/2)=½+√5/10 suman 1 (verificado simbólicamente). La degeneración de la frontera de (i) a 11−4√5 en Σ=1 es aritméticamente consistente. La celda abierta {p≥4, σ₁+M≤1, j≥3} declarada sin ambigüedad.
- `batalla2.py` (6/6), `microcelda.py` (5/5, con controles negativos genuinos: la pinza NO cierra sobre s*=2.0557 — la constante es la justa), `perfilp.py` (5/5), `rstar.py` (6/6, con controles negativos: sin colas la pared mural no es vacua; sin Σ la pinza no cierra C4).

### 6. Contraste sección ↔ apéndice (809–993 vs apéndice)

Todos los enunciados de la sección se corresponden con teoremas del apéndice y los valores citados (0.5874, 0.6310, 15/26, (T−1)²/2=0.3522, (T−1)²=0.7044, ω_A=2−2(T−1)(φ−1)=0.962585 — re-derivado en forma cerrada 2(φ²−T)(φ−1) usando (φ−1)φ... (φ²−1)(φ−1)=1, correcto —, 0.624, 0.896, √3, φ²−φ/2=1.809, 17/7, 2/7) son exactos. Excepciones de higiene: F2 (hipótesis de DT3), F9 (retórica del contraejemplo). El párrafo «Status» es honesto: los huecos residuales están listados y remitidos con etiqueta correcta a app:campaign.

### 7. Criterios transversales

1. **Etiquetas:** honestas en general (conjetura del pentagrama, sketch de DPr, celda excepcional de DGp, hueco k=4 de striple declarado). Déficit puntual en DGp (F3).
2. **Dominios:** los declarados coinciden con los probados salvo F1 y las constantes F5.
3. **Tolerancias:** los guards de los scripts (1e−9) van en la dirección permisiva pero los márgenes reportados son órdenes de magnitud mayores; los contactos exactos (0 esperado) se distinguen de los positivos.
4. **Gates infalibles:** dos detectados (F1-bis en batalla2.py: `max(Psij(3,w),PsiB(w))>PHI` es independiente de la instancia; «añadir pequeños nunca baja rho» en bolsillo.py es cuasi-trivial). El resto de gates contrasta contra LP/SLSQP/oráculos independientes con controles negativos.
5. **Circularidad:** barrida la DAG completa de dependencias del bloque (DU→DU4; DR→DBo→DB→DBpp; S5→DG→DGp; Cmin/Cwitness/corner desde app:widthproofs, anterior). Ninguna.
6. **Enunciado = prueba:** salvo F1, F2, F4, sí.
7. **Re-derivación propia:** 56 comprobaciones sympy/numéricas propias, todas conformes salvo la constante o* (F5).

---

## HALLAZGOS

### [OBLIGATORIA]

**F1. thm:DP(iv), j=3: el árbol de casos no cubre «y hoja estrictamente dentro del subárbol de o₁» (líneas 2827–2843).**
El texto enumera: y=o₁ (dicotomía nodo/polvo); «y lies in **another** occupant's subtree» (no-hoja → Ψ₃; hoja → Ψ₂/2ω/pinza); y la pinza se enuncia y demuestra «closes y a leaf **outside** o₁'s subtree» (2844), usando esa hipótesis dos veces ((b): el ocupante de {o₂,o₃} que no contiene a y; (c): (Bo) vale en todo nodo del subárbol de o₁ «as y lies outside»). Si y está anidado estrictamente dentro de o₁ y es hoja, y el subárbol de o₁ es una cadena que termina en y, solo hay **dos** hojas estrictas (las de o₂ y o₃): la ruta Ψ₃ invocada por la frase «a node makes y's subtree or o₁'s contribute a third strict leaf» (2833–2834) es falsa en esa configuración, y la pinza escrita no aplica. El script `batalla2.py` reproduce el mismo hueco: su rama `y_en_o1 ∧ tiene_nodo_o1` descarga en el gate `max(Psij(3,w),PsiB(w))>PHI`, que es **independiente de la instancia** (no puede fallar); la única protección es el chequeo muestral final `r>φ`. `microcelda.py` declara su celda explícitamente «y hoja FUERA del subárbol de o₁».
**Reparación (verificada por este referee, solo con paredes ya presentes):** para y ∈ subárbol de o₁, y≠o₁, en rama A con ρ≤φ, o₂≥3/φ, o₁≥3:
(b') si algún nodo del subárbol de o₁ tiene dos hijos-nodo, uno de sus dos subárboles evita a y y aporta hoja estricta; o₂ y o₃ aportan las otras dos (ninguno contiene a y) → Ψ₃. 
(c') si es cadena o₁⊃v₁⊃…⊃y: V se define igual; si v*≠y, la pinza corre **textualmente** (y∉V, luego el hijo de v* ∉V y ≤o₂; (Bo) vale en v*≠y; m∈subárbol de v* cuenta aparte de X_{v*} al no ser hijo directo — (C1)–(C4) intactas). Si v*=y: la cola de y da φy>o₂+3≥3φ ⟹ **y>3**; y (Ry) más la cola de m dan y−ω<σ₁+σ₂+X_y^rest≤ρ≤φ ⟹ **y<φ+ω<φ²=2.618<3**. Contradicción. 
Con esto el enunciado de DP(iv) queda como está; debe añadirse el caso al texto (y, idealmente, un gate falsable al script).

### [RECOMENDADA]

**F2. thm:DT3: la hipótesis S⊂(ω,1) vive solo en el preámbulo del apéndice (2657) y falta en la sección (941–961) y en el enunciado del teorema (2666–2669).**
El modelo admite anillos con r≤ω (discos sólidos, línea 182–183), luego σ₃≤ω es una instancia legítima. σ₃>ω es esencial para la mitad 13/7 del subcaso «σ₁+M>1» de la rama 1 (2688–2690): sin ella la cadena da solo ρ>σ₁+1−ω, que no alcanza 13/7 para ω grande. La mitad ρ>Φ>T sobrevive sin la hipótesis ((B1)+(W) no usan σ₃). Corrección: subir S⊂(ω,1) al enunciado del teorema y a la frase de la sección, o anotar que el caso σ₃≤ω se remite al gap lemma de app:campaign.

**F3. thm:DGp: los certificados numéricos internos no están etiquetados como asistidos por ordenador (2553–2565).**
c₁₀≥0 en [g,o*] y c₂₀≥0, c₂₁≥0 se afirman sin método (a diferencia del parche +0.307, que sí dice «certified on a grid with symbolic endpoints», y de thm:DPr, que declara «computer-assisted»). Son funciones algebraicas de una variable: certificables exactamente (Sturm/resultantes) o, como mínimo, etiquetar la asistencia. Una rejilla con extremos simbólicos no es una certificación de continuo; el estándar de honestidad del propio paper (DPr) pide la etiqueta.

**F4. thm:DT3, rama 1: «the program … is exactly that of Theorem corner, whose lower bound gives σ₁+σ₂>13/7» (2686–2688).**
thm:corner acota ρ=max(S₀,(1+S₀)/α)≥13/7, no S₀ a solas. La conclusión ρ≥13/7 se obtiene igual (ρ≥max(S₀,(1+S₀+σ₃)/α)≥max(S₀,(1+S₀)/α)≥T_can≥13/7), pero la frase atribuye al corner una cota que su enunciado no da. Reformular sobre ρ.

**F5. Constantes o* y õ imprecisas (2553, 2559).**
La raíz de c₁₀ es 1.59557 (c₁₀(1.5958)=−1.3·10⁻⁴<0): la afirmación «c₁₀≥0 en [g, o*=1.5958]» es falsa en la constante literal; `bolsillo.py` imprime o*=1.5957. La raíz de c₂₀ es 1.295564, no «õ=1.29558…» (el «…» reclama dígitos exactos que no lo son); el script imprime 1.2957. La cobertura no se ve afectada (solo se usa (g,õ] ⊂ [g,1.5955…], con margen c₁₀(õ)=0.063, y c₂₀(1.29558)>0), pero las constantes deben corregirse o definirse como «la raíz de …».

### [MENOR]

**F6. thm:DGp (2563–2564): «f₂ ≥ f₂(A_max) = c₂₀(o₁)+ω c₂₁(o₁)».** Debe ser f₂(A_max)−curva = c₂₀+ω c₂₁ (con c₂₁=φ/2−1/A_max, coherente con «c₂₁≥0 para o₁≤2», que verifiqué); tal como está escrito, la no-negatividad de c₂₀,c₂₁ no diría nada sobre la curva.

**F7. op:assembly(a) (1150) describe la ruta j=3 de thm:DP con «a U₄-based wall (o₂<1+1/o₁)» que no aparece en la prueba actual de thm:DP** (que usa (Ry), hojas, colas y la pinza). Deriva de descripción; actualizar.

**F8. lem:Dgaps (2199–2208) no enuncia la admisibilidad a_i+a_j≤R** necesaria para que θ_ij esté definida (thm:DU4 sí la dice: «all pairs admissible»).

**F9. Sección 829–831: «an explicit counterexample pins the failure region exactly»** — el apéndice da un contraejemplo puntual, no una caracterización de la región de fallo; rebajar la frase (o remitir al script, que sí barre la región).

**F10. thm:DPp(vi) (2955–2963):** la disyunción comprimida omite el caso mixto ({o₁,o₂,m,σ₃} empaqueta pero {o₁,o₂,m,σ₂} no); aterriza en la misma pared espejo (σ₂≤1 fuerza b₂<1), pero merece una cláusula.

**F11. La convención de primera copia** se introduce entre paréntesis dentro de la prueba de DV2 (2350–2352) y hace trabajo real en varias pruebas posteriores (colas de DB/DPsij, o₁∈V en la pinza aun con o₁=o₂, empates α=o₁ en la cola (II) de DGp). Promoverla al preámbulo del apéndice.

**F12. Cosmético:** thm:DU4 se titula «Lemma U₄» siendo Theorem; «jj=3» (2834, 2838) es jerga de script filtrada al paper.

---

## VERIFICADO EN POSITIVO (resumen)

1. **56 comprobaciones sympy/numéricas propias** (script del referee): identidad del término cruzado de DU y su contraejemplo; T_c'=−c/(2√g_c); b_R↗R, b_R≤A, b_R|_{R=A+B}=b₂; g''>0 del zigzag; **y₀=2b₂ resolviendo el sistema de tangencias**; N(σ₁) y la identidad (1+4σ₁)−(1+2σ₁−2σ₁²)²=4σ₁³(2−σ₁); ∂²b₂/∂α² y la factorización (α+o)(α³+α²o+o³) del numerador de o−αb₂'; el certificado de coeficientes positivos de −g' en DP(i) y la factorización (A²−A−1)(2A+1); 2b(φ)=φ; las tres identidades Tribonacci (cruce de Ψ, cruce de Ψ_B, polinomio literal); las cinco constantes de la pinza y su umbral 11−4√5 resuelto simbólicamente; γ₀=φ, γ_{2/7}=2, 1<γ'<2; b₂(2,√5−1)=1, b₂(3/2,3/2)=1, cruce interior en (3/2,2); autodualidad de A_max; N₁(½)=3/2; f₁(1+ω)≥curva con contacto en (g,ω→1); el rincón exacto de DPr(iv); Ψ(¼)=2, Ψ(½)=φ, Ψ_B(½)=2, Ψ_B(1)=φ, Ψ₂(φ/2)=φ; cruces 0.3522/0.6240/0.8959; ω_A=0.962585; ínfimo 4/(1+2ω) de DV2; (3/2)Φ−ω≥2.64; **sup(s'−(φ−1)Σ)=5φ−7 de DPr(i) re-derivado exactamente a mano** (alcanzado en σ₁=σ₂=σ₃=φ−1, ω→1).
2. **Cadenas lógicas re-derivadas a mano:** DV1–DV34 completas; DR/DBo/DB/DBpp con sus programas min-max y casos de borde; el argumento de hojas de DPsij (incluido el paréntesis W<0, que es álgebra exacta); DT3 rama a rama con la tercera ruta al bolsillo sin²A+sin²B>1 ⟺ σ₂>b(α); DP(i)–(iii) completos; la pinza (C1)–(C4); DPp(i)–(vi); el criterio mural (dirección de suficiencia, la usada).
3. **Circularidad:** ninguna (DAG de dependencias barrida; todo lo citado se prueba antes o en apéndices anteriores).
4. **Scripts del verifmap ejecutados en verde** con contrastes independientes (LP, SLSQP, oráculo euclídeo) y controles negativos genuinos (la pinza no cierra sobre s*; la pared mural no es vacua sin colas; contraejemplos de slack negativo del criterio ingenuo y del orden decreciente).
