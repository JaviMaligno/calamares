# Hoja de ruta autocontenida

Cada pendiente con su estado, el esqueleto técnico de ataque y el criterio de éxito, para trabajar desde el repo sin necesidad de la conversación original.

## 1. Rigor pleno del suelo de Tribonacci (Prop. del paper, idealización tangente)

**Estado: RESUELTO para la subfamilia rígida (Teorema S, `docs/drafts/suelo_rigido.md`, verificado 10/10).** Toda instancia con R = r₁+r₂, pareja en el agujero y trío infactible cumple ρ > T estricto, para todo w > 0, sin idealización; el ínfimo es T y no se alcanza. La prueba reduce la suficiencia del trío a ψ(u)+ψ(v) ≥ τ vía la identidad sin²(θ/2) = f(a)f(b), y la configuración rígida emerge como extremo por concavidad (no se supone). Queda abierta la versión con holgura R > r₁ + r₂ (el esqueleto de abajo sigue siendo el plan para esa generalización).

**Esqueleto de la prueba rigurosa (dirección ≥, la que importa):**
1. *Lema del contrapositivo constructivo (fácil y riguroso):* si r₄ ≤ P(r₁, r₃, R), donde P es el radio del mayor tercer círculo insertable dada alguna colocación de {r₁, r₃} en el disco R, entonces el trío empaqueta (construcción explícita). Contrapositivo: todo contraejemplo de la familia (que exige el trío infactible) cumple r₄ > P(r₁, r₃, R).
2. *Cota inferior de P:* P ≥ bolsillo de Descartes de cualquier construcción tangente concreta; con holgura (r₃ < R − r₁), colocar r₃ antipodal a r₁ da huecos laterales grandes, luego P crece al alejar r₃ de la tangencia. Consecuencia: la restricción r₄ < r₃ del orden fuerza P < r₃, que empuja r₃ hacia arriba (hacia R − r₁).
3. *Función P exacta:* el "mayor tercer círculo dados dos círculos en un disco" se resuelve por análisis de casos de patrones de tangencia (a lo sumo unas pocas configuraciones candidatas: tangente a pared+ambos, pared+uno, ambos sin pared). Con P en mano, minimizar (r₃ + P(r₁, r₃, R))/r₂ sujeto a r₂ ≤ min(R − r₁, r₁ − w), P < r₃, r₃ + r₄ ≤ r₁ − w reproduce el álgebra t³ + t² + t ≤ 1 en el óptimo y da T sin idealización.
4. *Subfamilia ajustada ya rigorizable hoy:* restringiendo a R = r₁ + r₂ y r₃ en tangencia, el bolsillo es exacto (configuración rígida) y el suelo T es teorema; documentar esa versión primero.

**Éxito:** teorema "todo contraejemplo I1 cumple ρ > T" sin la palabra "idealización".

## 2. Conjetura del umbral de Tribonacci (ρ < T ⟹ irrelevancia geométrica)

**Estado:** conjetura con evidencia fuerte (0 fallos bajo T en >1000 ejecuciones; análisis de mecanismos en docs/resultados.md §5quater). **Avance: ver `docs/reinsercion.md`.** El paso de intercambio queda partido en dos. La parte combinatoria está cerrada: con los recursos que libera el intercambio (disco vacante, agujero de m que viaja con él, anidamiento) el perfil de dos aros tiene umbral exacto max(1, 2(1−ω)) con ω = w/r_m, ningún bloqueo con ≥5 aros en banda es compatible con ρ < T, y el mínimo sobre perfiles cruza T en ω_c ≈ 0.05: para w ≲ r_m/20 la reinserción está garantizada sin geometría. La parte geométrica queda aislada y cuantificada: la cota que da el bolsillo de Descartes por sí solo se minimiza en α = φ con valor exactamente φ ≈ 1.618, luego el bolsillo NO basta para llegar a T y hace falta la infactibilidad del trío completo. Consecuencia práctica: la ventana de riesgo es α ≈ φ con ω > ω_c. **Segundo avance (Proposición 3, `docs/reinsercion.md` §9):** en la plantilla canónica el ínfimo con los tres ingredientes —infactibilidad del trío + colocación del testigo (S cabe en u)— es exactamente T, alcanzado en α = T, σ₂ = T − 1 (identidad exacta b(T) = T − 1). La condición del trío sola se queda en 1.7990559 (raíz de 2α³ = α²+2α+2): el lema necesita los tres ingredientes. Falta: v y u genéricos, grosor positivo, bloqueos de 3 aros. **Tercer avance (workflow verificado, borradores en `docs/drafts/`):** (a) *grosor positivo cerrado en la plantilla*: Φ(ω) = T₍₁₊ω₎ − ω con T₍₁₊ω₎ raíz del Tribonacci deformado α³ = (1+ω)(α²+α+1); cota uniforme T_can(ω) ≥ T + 0.00985 para todo ω ∈ (0, 0.3] — "el grosor solo lo sube" confirmado con holgura (H1, κ ≥ 1 en la frontera del trío, DEMOSTRADO en `drafts/h1.md` vía la identidad cerrada κ = √(g(σ₂)/g(σ₁))); la curva no es monótona y su mínimo conjeturado es la esquina racional exacta (ω, α, σ₂, ρ) = (1/7, 2, 6/7, 13/7). (b) *Perfil de 3 aros cerrado*: Proposición 4 con fórmula ρ*₃(ω) = max(1, min(2(1−ω), max(φ, 2/(1+2ω)))) y cruce exacto con T en ω_T = 1/T − 1/2 ≈ 0.0437 (sustituye al ω_c ≈ 0.05 numérico). (c) *Cuadrado*: constante hermana X = 1.7110186 (cuártica 17x⁴−4x³−62x²+4x+49), bolsillo de esquina (√s−√a)², identidad b_□(X) = X−1 análoga a b(T) = T−1; el umbral del cuadrado es estrictamente menor que X (instancia con ρ = 1.685 < X que ya falla). La pista A culminó en el Teorema S (ver punto 1). Estado consolidado en `resultados.md` §9; huecos activos priorizados en la sección final de este documento.

**Plan de ataque:** convertir el rescate de bolsillos en un *lema universal de reinserción*: en el paso de intercambio de la prueba de irrelevancia (Teorema 2 del paper), cuando los aros menores que m alojados en u suman más que r_m, demostrar que con ρ < T siempre existe reinserción alternativa combinando (a) el Lema de fila (suma ≤ r_m), (b) la densidad crítica 1/2 de Fekete–Keldenich–Scheffer (área ≤ π r_m²/2) y (c) los bolsillos de Descartes del contenedor v tras retirar m. El caso crítico identificado: pocos aros medianos con suma > r_m y área > mitad — cuantificar que ese perfil exige ρ ≥ T (la misma álgebra del suelo). Riesgo: mecanismos de bloqueo aún no imaginados con n ≥ 6; mitigación: barridos estructurados por debajo de T con nuevas plantillas antes de invertir en la prueba.

## 3. Reglas con input completo (complejidad)

**Estado:** abierto. Las gemelas cierran las reglas función-del-estado; seguir al testigo siempre funciona pero exige conocer el lex-máximo.

**Formulación precisa recomendada:** modelo de oráculo — la regla ve todos los radios y puede consultar "¿empaqueta este multiconjunto en un disco de capacidad C?" (oráculo de hermanos). Pregunta: ¿bastan poly(n) consultas para colocar el lex-máximo? Observaciones de partida: el voraz de selección usa n consultas de *factibilidad de conjunto* (no de hermanos); reducir conjunto→hermanos parece exigir explorar mapas de padres (exponenciales). Candidato a resultado negativo: cota inferior de consultas por adversario que responda consistentemente con dos bosques distintos. Candidato positivo: con radios enteros y DP sobre capacidades, poly-pseudo consultas.

## 4. Afilados en cuadrado y en R³

Los teoremas de superincrecencia ya cubren cualquier contenedor y dimensión (paper, Teoremas 1–2). Abierto: análogos de n=4/gemelas/suelo. Para el cuadrado, el papel del bolsillo de Descartes lo juegan los huecos de esquina (círculo inscrito en esquina entre lado y círculo: radio con fórmula cerrada); repetir el álgebra del suelo con esa fórmula debería dar la constante análoga a T. Para R³ (esferas), el par deja de ser aditivo-exacto (¡dos esferas en una bola: sí sigue siendo r_a + r_b ≤ C!) — de hecho el par ES exacto en toda dimensión; los tríos cambian (empaquetamientos de 3 esferas), rehacer el criterio.

## 5. Contenido secundario pendiente

- Caracterización exacta de la franja de divergencia (hoy: diagrama numérico + borde superior demostrado 0.4641R).
- Aproximabilidad de la métrica de número (¿PTAS con oráculo? ¿APX-dura?).
- Pseudopolinómico para el sustituto aditivo con radios enteros.
- Generalizaciones de docs/generalizaciones.md (grosor variable y δ-flexibilidad las más jugosas).

## 6. Publicación

- Pulir paper/main.tex: nombres, agradecimientos, revisar redacción del abstract, decidir si el apéndice de verificación crece con (V-extra) para el contraejemplo n=4 de la sección de fases.
- Recomprobar cada cita contra su fuente primaria (los datos bibliográficos vienen de la revisión documentada en docs/resultados.md §7).
- Destino primario: Operations Research Letters o Discrete Applied Mathematics; preprint arXiv (math.CO / cs.CG cruzado).
- Al subir, enlazar el repo como material suplementario (el mapa de verificación del README cubre cada afirmación numérica).

## 7. Huecos activos, por prioridad (tras la consolidación de resultados.md §9)

**Bloqueantes de la conjetura principal:**
1. **Contenedores v/u genéricos** — EL hueco. Todo lo demostrado vive en la plantilla canónica (v rígido con un vecino grande, S un par, u el agujero de α). Hace falta: cota inferior universal del mayor hueco de un empaquetamiento en función de la capacidad libre, y la restricción del testigo cuando u es la sartén (empaquetabilidad junto a ocupantes mayores, no capacidad simple). Pista útil ya medida: el umbral bloqueante crece como b(t) + Θ(√δ) fuera de la esquina rígida (rigido.py V7b).
2. **H1 — RESUELTO en `drafts/h1.md` (acta en `VEREDICTOS.md`; `code/h1.py` 5/5).** La corazonada Schur era una identidad cerrada: κ = √(g(σ₂)/g(σ₁)) con g(s) = s³(1−s), independiente de α, y κ ≥ 1 para todo α > 1. De propina: la frontera de bloqueo del trío tiene forma cerrada t(σ₁) + t(σ₂) = t(b(α)) con t(s) = √((1−s)/s), y el cierre por abajo del programa es exactamente α ≤ T (Tribonacci), no la cota áurea. Los "módulo H1" del bloque de grosor quedan retirados.
3. **ρ*₄ = ρ*₃** — conjeturado; k ≥ 5 excluido (Corolario 2), así que k = 4 es lo único que podría rebajar ω_T. Cerrarlo fija ω_c = ω_T exacto.

**De rigor menor:**
4. Compacidad en la Prop. S6 (esbozada; solo afecta a la dirección ≤ del ínfimo).
5. Cota ρ > √2 del cuadrado: válida solo para α ≥ 1; falta el caso α < 1 o restringir el enunciado.
6. Exactitud del criterio angular feas3: usada como exacta, sin prueba en el repo; afecta al caso (ii) de la Proposición 4 (ω > 1/2). El Teorema S la esquiva usando solo direcciones constructivas — mismo truco aplicable donde reaparezca.

**Extensiones naturales:** holgura R > r₁ + r₂ en el Teorema S; escalera completa y familia de 4 aros del cuadrado; ¿comparten mecanismo la meseta φ de ρ*₃ y el suelo φ del bolsillo (Prop. 2)?; optimalidad de la rama mixta y de la esquina 13/7 del grosor (hoy numéricas).
