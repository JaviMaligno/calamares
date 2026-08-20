# Acta de revisión — BLOQUE 6 (ronda ciega)

Referee externo. Objeto: apéndice «Complete proof of Theorem thm:rigidfloor»
(`paper/main.tex` líneas 1359–1555) y apéndice «Verification details for
Theorem thm:twins» (líneas 3775–3815), contrastados con los enunciados
(thm:rigidfloor, líneas 485–497 + rem:slack 531–539; thm:twins, líneas
413–439). Metodología: re-derivación completa a mano de cada lema, y
verificación en aritmética exacta (sympy, racionales) de V1–V4 y de todas las
identidades algebraicas del suelo rígido (script del referee
`ref_bloque6.py` en este directorio). Ejecutados además los dos scripts del
repo: `code/gemelas.py` (reproduce) y `code/rigido.py` (7/7 bloques OK).
`docs/` no consultado.

---

## Veredicto por apéndice

**Apéndice `app:rigidproof` (thm:rigidfloor): ACEPTAR con correcciones
menores.** La prueba es completa, autocontenida y honesta. Cada identidad
algebraica que declara «exacta» lo es (todas re-derivadas independientemente
por el referee, no solo confiadas al bloque V5 del script). Los dominios
reclamados coinciden con los probados; el único uso del criterio angular es
la dirección constructiva, tal como la nota de la línea 1434 declara — no hay
exactitud escondida ni circularidad. Enunciado = prueba en todas las ramas.

**Apéndice `app:verif` (thm:twins): ACEPTAR con UNA corrección obligatoria.**
V1, V2 y V4 son correctos en aritmética exacta con todos los redondeos del
lado seguro. V3 — la única feasibilidad positiva no dos-círculos, y pieza
imprescindible del teorema — presenta un testigo explícito que, tal como está
impreso, **viola dos restricciones** (solapes de ~3–5·10⁻⁴): los ángulos
fueron redondeados hacia el lado inseguro. La afirmación V3 es VERDADERA y la
reparación es local y limpia (abajo), pero el testigo impreso no verifica.

---

## Hallazgos

### Apéndice twins (app:verif)

**[OBLIGATORIA] T1 — El testigo de V3 impreso es infeasible (redondeo del
lado inseguro).** Líneas 3802–3810. Con los ángulos impresos 30.77° y 32.02°
(evaluación a 40 dígitos):

- |c_A−c_X| = 14.75948967… **< 14.76** (déficit 5.1·10⁻⁴)
- |c_A−c_Y| = 14.73968625… **< 14.74** (déficit 3.1·10⁻⁴)

Los ángulos de tangencia exacta son cos θ_X = 88/102.4 = **55/64**
(θ_X* = 30.7535°) y cos θ_Y = 87/102.6 = **145/171** (θ_Y* = 32.0103°);
aumentar el ángulo acerca el círculo al 10, de modo que 30.77° > θ_X* y
32.02° > θ_Y* producen solape. Los valores impresos ni siquiera son el
redondeo correcto de los exactos (serían 30.75° y 32.01°). El paréntesis
«(exact tangencies, chosen via the boundary angles)» es falso tal cual.
**Corrección** (verificada exacta por el referee): dar el testigo racional
c_A = (−5,0), c_X = (8.8, √27.4176), c_Y = (8.7, −√29.5776) — nótese
10.24·(55/64) = 8.8 y 10.26·(145/171) = 8.7 exactos. Entonces
|c_A−c_X|² = 13.8² + 27.4176 = 217.8576 = 14.76² **exacto**,
|c_A−c_Y|² = 13.7² + 29.5776 = 217.2676 = 14.74² **exacto**,
|c_X| = 10.24, |c_Y| = 10.26 (frontera), y
|c_X−c_Y|² = 0.01 + (√27.4176+√29.5776)² ≈ 113.96 > 9.5² = 90.25 con margen
enorme. Alternativa: redondear los ángulos HACIA ABAJO (p.ej. 30.70° y
31.95°), que da todas las desigualdades estrictas. Nota: `gemelas.py` no
contiene este testigo (usa un solver numérico y el criterio de suma angular),
así que el texto impreso es el único certificado de V3 — de ahí la severidad.

**[MENOR] T2 — Errata de redondeo en el sketch del cuerpo (línea 432).**
«√(204.86−20·8.8) ≤ 5.37»: √28.86 = 5.3722 > 5.37. El apéndice (línea 3800)
tiene el valor correcto 5.38. Corregir 5.37 → 5.38 en el cuerpo (la
conclusión < 9.76 no se ve afectada).

**[MENOR] T3 — El cuerpo cita más de lo que el apéndice prueba.** Línea
430–431: «no third circle of radius ≥ 4.7 fits», pero V2 solo prueba
z ∈ {4.74, 4.76}. La afirmación general es cierta y de una línea con el mismo
método (|c_z−c_B|² ≤ 3(15−z)²−2(10+z)²+150 = z²−130z+625 < (5+z)² ⟺
z > 30/7 ≈ 4.286), y además no es portante: los dos valores probados bastan
para I₂, y el walkthrough de I₁ no necesita el bloqueo de sartén de 4.99/4.50
(ambas sub-ramas de «5 a la sartén» colocan los cuatro aros — verificado por
el referee). Restringir la frase o añadir la línea general.

**[RECOMENDADA] T4 — Los cuatro recorridos greedy quedan al lector.** Ni el
cuerpo (etiquetado honestamente «Proof ingredients») ni el apéndice derivan
explícitamente «best fit falla en I₁ / worst fit falla en I₂» desde V1–V4 +
hechos dos-círculos. El referee cerró el walkthrough completo y es correcto y
rutinario: tras la decisión sobre el 5, TODOS los pasos posteriores son
forzados (un solo contenedor factible o ninguno) en las cuatro ejecuciones,
lo cual es además lo que sostiene la cota 1/2 aleatorizada (la única
aleatoriedad relevante es la elección binaria del paso decisivo). Una tabla
de cuatro líneas con las ejecuciones haría el teorema autocontenido.

**Verificado en positivo (twins):**
- V1 exacto: 14.99²−10.01² = 249/2 = 124.5 y 14.5²−10.5² = 100 exactos;
  cotas decrecientes en a, evaluación en a = 5 legítima (a ≤ 5); transversas
  √(1497/1250) = 1.09435 ≤ 1.095 y √54 = 7.34847 ≤ 7.349 (lado seguro);
  |c_X−c_Y|² ≤ 77.29441 ≤ 77.30, √77.30 = 8.7920 ≤ 8.80 < 9.49. Todas las
  direcciones de redondeo seguras. El paso Cauchy–Schwarz transverso correcto.
- V2 exacto: rigidez diametral por desigualdad triangular (15 ≤ a+b ≤ 15);
  c_z·u ≥ 44/5 y 87/10 exactos; el doble uso de |c_z|² ≤ (15−z)² es legítimo
  (la cota compuesta 3s−2(10+z)²+150 es creciente en s); |c_z−c_B|² ≤
  28.8576 y 31.2676 exactos, √ = 5.3719 ≤ 5.38 < 9.76 y 5.5917 ≤ 5.60 < 9.74.
- V4 exacto: agujero 9.495; 9.49 ≤ 9.495; 9.50 > 9.495 (dos veces).
- Estado idéntico en el paso decisivo: cierto (prefijo {10,5} compartido,
  colocación del 10 forzada, mismos contenedores/capacidades/ocupantes/aro).
- Dicotomía verificada: anidar el 5 ⟹ falla I₁ (4.99 forzado a sartén,
  4.50 bloqueado por V1+V4+capacidades), acierta I₂ (V3); sartén ⟹ acierta
  I₁, falla I₂ (V2+V4). Lex-max = los cuatro aros en ambas (testigos: worst
  fit en I₁, best fit en I₂). Cota aleatorizada 1/2 correcta.
- «All feasibilities … except three facts»: recuento honesto (V4 es
  dos-círculos-exacto).
- `gemelas.py` reproduce (solver numérico; etiquetado como reproducción, no
  como prueba — honesto).

### Apéndice rigidfloor (app:rigidproof)

**[MENOR] R1 — Prop. S5 (necesidad): el caso d = 0 no se descarta.** Línea
1494 fija «d = |X| > 0» sin justificación. Es trivial (d = 0 da
|X−c₁| = t < 1+q, infeasible), pero la prueba debería decirlo en media línea:
tal como está, la cota inferior de cos γ divide por d.

**[MENOR] R2 — Lema S6a(3): p_max y δ₀ presuponen no-vacuidad.** Línea
1514–1518: «empty or a closed interval [q, p_max]» seguido de una frase que
usa p_max y δ₀ = t−p_max sin la salvedad del caso vacío. El uso en Prop. S6
es correcto en ambos casos (si el intervalo es vacío, todo p es infeasible y
cualquier δ sirve), pero conviene la coletilla «if nonempty».

**Verificado en positivo (rigidfloor) — todo re-derivado por el referee:**
- **S1**: ley de cosenos ⟹ 1−cos θ = 2ab/((R−a)(R−b)) ⟹ sin²(θ/2) = f(a)f(b)
  exacto (sympy: residuo 0); buena definición ⟺ a+b ≤ R exacto; monotonía de
  f en [0,R) correcta; el «iff» de disyunción por D(γ) creciente en [0,π].
- **S2**: dominios de los tres θ correctos (1+p ≤ 1+t ⟺ p ≤ t; p+q ≤ 2t <
  1+t ⟺ t < 1); el case-split del wrap (γ = Δ vs 2π−Δ) cubre ambas ramas, y
  la rama γ = Δ usa correctamente θ(1,q) ≥ θ(p,q) por 1 ≥ p.
- **S3**: la equivalencia arcsin A+arcsin B+arcsin C ≤ π ⟺ C ≤ sin(arcsin A+
  arcsin B) es válida en el caso no trivial (ambos lados en [0,π/2]); los
  radicales reales ⟺ x ≤ t; G(x) = (1+t)(t−x)/(t²x) confirmado simbólicamente
  con f(1) = 1/t, f(x) = x/(1+t−x); √G = (√(1+t)/t)ψ y el remate
  (√(1+t)/t)τ_t = 1 exactos. Solo se usa la dirección suficiente (nota 1434
  honesta): sin circularidad con S5.
- **S4**: ψ(b(t)) = τ_t y t/(1+τ_t²) = b(t) confirmados (sympy residuo 0);
  2b−1 = (t²+t−1)/(t²+t+1) exacto y su signo en t = 1/φ; U″ =
  2t(3z²−1)/(1+z²)³ confirmado; dominio de concavidad τ_t ≤ 1/√3 ⟺
  t ≤ (1+√13)/6 = 0.76759…, que cubre t < 1/φ = 0.61803… con holgura, tal
  como se declara; el argumento de esquina (subir α a τ_t−β, W cóncava,
  mínimo en extremos, ambos = t+b(t)) correcto y estricto.
- **Suelo estricto**: la cadena t+b(t) < 1 ⟺ t³+t²+t < 1 ⟺ t < t* exacta
  ((1−t)(1+t+t²) = 1−t³ verificado); ρ ≥ ρ₂ = (p+q)/t legítimo (ρ es el
  máximo de las colas); L′ = −(t²+2t)/(1+t+t²)² confirmado; L(t*) = 1/t* = T
  verificado módulo T³−T²−T−1 (residuo polinómico 0). La prueba demuestra de
  paso «F fuerza t < t*», tal como el enunciado reclama.
- **S5**: rigidez del par {1,t} por desigualdad triangular correcta;
  suficiencia: el círculo de Descartes tangente a pared y a ambos tiene radio
  exactamente b(t) (resuelto por el referee: r = (t²+t)/(t²+t+1), centro real
  con Y² = 4t²(1+t)²/(1+t+t²)² > 0); necesidad: las dos cotas de cos γ y su
  compatibilidad re-derivadas; la factorización del lado izquierdo como
  4(t²+t+1)(b(t)−q) verificada a mano (los términos q² se cancelan: coef.
  (1+t)−1−t = 0; lineal −4(1+t+t²); constante 4t(1+t)) y en sympy.
- **S6a**: (1) las seis restricciones relajan al bajar (p,q) — correcto;
  (2) compacidad de testigos (|c_i| ≤ 1+t ≤ 2) y paso al límite en
  restricciones no estrictas — correcto, cerrado relativo a D;
  (3) segmento inicial cerrado — correcto (módulo R2).
- **S6**: ε_t > 0 ⟺ t < t*; q_t ∈ (b(t), t) bien definido (b(t) < t ⟺
  t² > 0); infeasibilidad de (t,t,q_t) por S5; δ existe por S6a(3);
  ω = 1−(t−δ+q_t) ≥ ε_t+δ > 0 (q_t ≤ b+ε_t ⟹ t+q_t ≤ 1−ε_t); órdenes
  estrictos (δ < t−q_t); F2 con igualdad (permitido, F2 es «≤»); ρ = ρ₂
  porque ρ₂ > T > 3t*(=1.631) > ρ₁ y ρ₃ < 1; ρ₂ ≤ L(t)+ε_t/t → T
  (comprobación numérica del referee: t = t*−10⁻³ da ρ₂ ≤ 1.84119, T =
  1.83929). Inf = T y no-atención (suelo estricto) — enunciado = prueba.
- **rem:slack**: antitonía del contenedor por traslación concéntrica
  correcta; F2 no depende de R; la familia aproximante tiene R = r₁+r₂,
  admisible — el ínfimo no cambia. Correcto.
- **Membresías reclamadas por el enunciado** (no probadas en el apéndice,
  verificadas exactas por el referee): n=4: p+q = 0.97 ≤ 1−ω = 0.97
  (igualdad, F2 es «≤»), F3 = lem:cap escalado, R = 15 = 10+5;
  gemela I₁: 0.949 ≤ 0.9495, F3 = V1 escalado. Coincide con el bloque V8 de
  `rigido.py` (en F = True ambas).
- **Etiquetas honestas**: «All exact algebraic identities … additionally
  verified in code» — el «additionally» es veraz: la prueba se sostiene sola.
  Los gates de los scripts no son tautológicos (V5 compara expresiones
  simbólicas independientes; V6 contrasta contra un solver primal).
- `rigido.py` ejecutado: 7/7 bloques OK, sin fallos.

---

## Resumen de severidades

| # | Sev. | Dónde | Qué |
|---|------|-------|-----|
| T1 | OBLIGATORIA | app:verif V3 (3802–3810) | Testigo impreso infeasible (solapes ~4·10⁻⁴); sustituir por el testigo racional exacto (8.8, √27.4176)/(8.7, −√29.5776) o ángulos redondeados hacia abajo |
| T2 | MENOR | cuerpo 432 | 5.37 → 5.38 (√28.86 = 5.372) |
| T3 | MENOR | cuerpo 430–431 | «≥ 4.7» excede lo probado en V2; restringir o añadir la línea general |
| T4 | RECOMENDADA | thm:twins/app:verif | Tabla explícita de las cuatro ejecuciones greedy (todo forzado tras el paso decisivo) |
| R1 | MENOR | Prop S5 (1494) | Descartar d = 0 en media línea |
| R2 | MENOR | Lema S6a(3) (1514–1518) | «if nonempty» para p_max/δ₀ |

Ningún hallazgo FATAL. thm:rigidfloor: prueba correcta tal cual.
thm:twins: teorema verdadero; V3 exige la reparación local T1 antes de
publicación.
