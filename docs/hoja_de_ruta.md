# Hoja de ruta autocontenida

Cada pendiente con su estado, el esqueleto técnico de ataque y el criterio de éxito, para trabajar desde el repo sin necesidad de la conversación original.

## 1. Rigor pleno del suelo de Tribonacci (Prop. del paper, idealización tangente)

**Estado:** el ínfimo T de la familia de 4 aros está demostrado bajo la idealización "bolsillo tangente exacto". Falta el argumento sin idealizar.

**Esqueleto de la prueba rigurosa (dirección ≥, la que importa):**
1. *Lema del contrapositivo constructivo (fácil y riguroso):* si r₄ ≤ P(r₁, r₃, R), donde P es el radio del mayor tercer círculo insertable dada alguna colocación de {r₁, r₃} en el disco R, entonces el trío empaqueta (construcción explícita). Contrapositivo: todo contraejemplo de la familia (que exige el trío infactible) cumple r₄ > P(r₁, r₃, R).
2. *Cota inferior de P:* P ≥ bolsillo de Descartes de cualquier construcción tangente concreta; con holgura (r₃ < R − r₁), colocar r₃ antipodal a r₁ da huecos laterales grandes, luego P crece al alejar r₃ de la tangencia. Consecuencia: la restricción r₄ < r₃ del orden fuerza P < r₃, que empuja r₃ hacia arriba (hacia R − r₁).
3. *Función P exacta:* el "mayor tercer círculo dados dos círculos en un disco" se resuelve por análisis de casos de patrones de tangencia (a lo sumo unas pocas configuraciones candidatas: tangente a pared+ambos, pared+uno, ambos sin pared). Con P en mano, minimizar (r₃ + P(r₁, r₃, R))/r₂ sujeto a r₂ ≤ min(R − r₁, r₁ − w), P < r₃, r₃ + r₄ ≤ r₁ − w reproduce el álgebra t³ + t² + t ≤ 1 en el óptimo y da T sin idealización.
4. *Subfamilia ajustada ya rigorizable hoy:* restringiendo a R = r₁ + r₂ y r₃ en tangencia, el bolsillo es exacto (configuración rígida) y el suelo T es teorema; documentar esa versión primero.

**Éxito:** teorema "todo contraejemplo I1 cumple ρ > T" sin la palabra "idealización".

## 2. Conjetura del umbral de Tribonacci (ρ < T ⟹ irrelevancia geométrica)

**Estado:** conjetura con evidencia fuerte (0 fallos bajo T en >1000 ejecuciones; análisis de mecanismos en docs/resultados.md §5quater).

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
