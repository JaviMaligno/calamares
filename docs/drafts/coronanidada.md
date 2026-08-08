# Corona-contra-colas ANIDADA: D4, D5, D6

Estado: **cerrado computacionalmente** (acta CONFIRMADO CON
CORRECCIONES, 2026-08-07, `VEREDICTOS.md`; script
`code/coronanidada.py` 5/5). La conversión a teorema pleno pende de
los MISMOS lemas que la sartén (dualidad/zigzag, `coronacolas.md` §4)
más el lema-extensión de (N) (§5, corrección C4).

## 1. La plantilla anidada y los tres resultados

Plantilla (paper §6 y app:widthproofs/app:genericproofs): u = agujero
de α (F anida m en α), v = c_P(m) = la sartén del template anidado,
que a nivel superior contiene {α, m, o₁..o_j} según P (más extras
< m). El intercambio manda m al agujero de α y libera D_m (disco
unidad) a nivel superior de v; S (el contenido del agujero de α según
P) debe reinsertarse. Normalización r_m = 1, ω = w/r_m.

**(D4) La puntita anidada j = 2, rama A, ω ∈ [φ/2, 1)** (Ψ₂ cruza φ
en φ/2 EXACTO): vacía de bloqueos con ρ ≤ φ por la corona anidada,
con dualidad exacta (déficit 0.0 uniforme, MC + esquinas
deterministas + pared activa + monotonía en R).

**(D5) Perfiles k ≥ 3 fuera de la rama de reducción**: la tricotomía
anidada (§3) primero; la celda residual {pesado σ₁+W > 1, sin
reducción W+X_σ₁ > σ₁−ω, σ₂ ≤ φ−1} más los reenvíos ('D4W', 'LW') van
a la corona, por celdas (k, j) con esquinas deterministas. Déficit
0.0 uniforme.

**(D6) Gap lemma anidado (pequeños extra en v y σ₂ minúsculo) — por
ADJUNCIÓN + barridos directos.** Todo extra e < m a nivel superior de
v se adjunta al perfil: S⁺ := S ∪ {extras} (posiciones de piezas < m
existenciales; los depósitos están en v o viajan con m; extras en
agujeros ya cuentan en las X; los aros ≥ m de v son ocupantes por
definición). La tricotomía sobre S⁺ es exhaustiva y ENRUTA a
D5 (k⁺ ≥ 3) + D4 + reenvíos; el suelo del par NO viaja (§4, C3), por
eso el residuo se barre además DIRECTAMENTE (gaps j = 0 y j = 1,
j = 2 y j = 3 en toda ω, σ₂ minúsculo), con extras engordando las
colas de forma exacta. Déficit 0.0 uniforme.

## 2. Las adaptaciones respecto a la sartén

1. **Tamaño gratis de α**: α ≥ 1+ω SIEMPRE (su agujero admite a m) y
   α ≥ σ₁+σ₂+ω (necesidad del par del testigo dentro del agujero) —
   pero véase §4: la segunda solo con el par que VIVE en u.
2. **Colas con ρ ≤ φ**: la cola de α contiene {m, S, extras,
   ocupantes menores}; cascada como en la sartén pero con α DENTRO
   del orden (se barre el rango de α entre los o_i) y con el suelo
   del punto 1.
3. **Reparto del desbloqueo (opuesto al de la sartén)**: σ₁ → v
   (miembro de la corona), σ₂ → D_m. D_m se re-crea como MIEMBRO 1.0
   de la corona: un disco unidad virtual que la corona coloca y que
   recibe una fila de suma ≤ 1 (legal por el criterio de fila).
   CONSERVADOR: el bin ocupa arco como un miembro más en vez de
   reutilizar el hueco liberado (adversariado, ataque 1 del acta).
4. **Conjuntos del certificado**: la NECESIDAD usa {α, m = 1,
   o₁..o_j} — m está a nivel superior SEGÚN P (v = c_P(m)); según F
   irá dentro de α, pero R_lb solo necesita que ALGUIEN lo empaquete.
   La SUFICIENCIA coloca {α, o₁..o_j} + bin(1.0) + piezas de
   perfil/extras. Legítimo, con el caveat de alcance de §6.
5. **Tricotomía anidada** (§3) antes de invocar coronas.
6. **D6 por adjunción** (arriba), con la corrección C3 de §4.

Conservadurismo (dirección segura, como en la sartén): masas
opcionales (M, X's, hijos) OMITIDAS de las colas — cotas inferiores
más débiles ⟹ ocupantes menores ⟹ corona más difícil; los extras de
D6 SÍ entran en las colas (son piezas conocidas de la instancia); el
mínimo sobre órdenes y repartos es cota superior del mínimo
verdadero.

## 3. La tricotomía anidada y las herencias (correcciones C1/C2)

Sobre el perfil (σ₁, σ₂, W = resto, X_σ₁): **(L)** ligero σ₁+W ≤ 1 y
**(N)** anidado W+X_σ₁ ≤ σ₁−ω heredan el programa del par; **(H1)**
σ₂ > φ−1 da ρ ≥ Σ > φ por la cola de m; el resto va a la corona.

**C1 — (L) solo hereda las paredes COMBINATORIAS.** Las geométricas
(lem:DG/B1) reempaquetan v entero y destruyen la fila de D_m donde
(L) aparca W — el mismo mecanismo por el que cor:DS excluye a lem:DG.
Como Ψ₁ < φ en ω ≥ 1/2 y ρ*₃ muere en ω > 1−φ/2, las celdas
{(L), j = 1, ω ∈ [1/2,1)} y {(L), j = 0, k ≥ 4, ω > 1−φ/2} se
REENVÍAN a la corona ('LW', gemelo del reenvío 'D4W' de j = 2 con
ω ≥ φ/2), salvo si además anidan: entonces van por (N). Suelos que
(L) sí hereda (combinatorios): Ψ₁ (ω < 1/2), Ψ₂ (ω < φ/2), la
escalera Ψ_j ≥ √3 > φ (j ≥ 3), thm:DT3/cor:DB2 (j = 0, k = 3) y ρ*₃
(j = 0, k ≥ 4, ω ≤ 1−φ/2).

**C2 — la franja {W ≤ σ₁−ω < W+X_σ₁} se barre.** La celda de corona
es W+X_σ₁ > σ₁−ω; el generador solo salta con W+X ≤ σ₁−ω (antes
saltaba con W ≤ σ₁−ω y la franja con X_σ₁ > 0 quedaba sin barrer ni
heredar). 669 sondas del atacante con déficit 0.0.

## 4. La legitimidad de D6 (corrección C3)

La reducción D6 → D5 + D4 es de ENRUTADO combinatorio. El suelo
α ≥ σ₁+σ₂+ω NO viaja con el par de S⁺: las piezas extra viven en v,
no en u, y la pared (W) solo vale para el par que SÍ vive en el
agujero de α. En las celdas alcanzables desde D6 el suelo legítimo es
max(1+ω, par verdadero de u + ω); el bloque D2 del script barre D6
directamente con af tomado del par de u (los extras solo engordan
colas y corona), en j = 0..3 y en el régimen de σ₂ minúsculo.

## 5. El lema-extensión pendiente (corrección C4)

Las herencias GEOMÉTRICAS de (N) — j = 1 la línea áurea
min(φ²−(φ/2)ω, 2) > φ, y j = 0, k ≥ 4, ω > 1−φ/2 la curva canónica —
requieren un lema aún POR REDACTAR, con este argumento de carga: σ₁
con W dentro de su agujero es UNA pieza (mismo radio σ₁), luego la
pared (W) queda intacta a fortiori, y la B3′ engordada por X_σ₁ la
absorbe la cola. Hasta redactarlo, esas dos celdas de (N) cuentan
como «probadas módulo lema-extensión», no más.

## 6. Caveat de alcance (para el ensamblaje)

Toda la campaña presupone **v = sartén con α ∈ v a nivel superior**:
el conjunto de la necesidad {α, m, o₁..o_j} y el reparto de la
suficiencia usan que P empaqueta a α y a m a nivel superior de v.
Los casos **v = agujero** (de algún aro mayor) y **α anidada más
arriba (α ∉ v)** tienen otros conjuntos de certificado y son asunto
del ENSAMBLAJE, no de esta campaña.

## 7. Controles

- **La esquina rígida nunca se certifica**: en
  {α = 1/t, σ₁ = 1, σ₂ = b(t)/t}, R = α+1, el ciclo es tangente 2π
  EXACTO (sympy independiente del atacante: fórmula del coseno y
  Descartes propios) y con σ₂ mayor el ciclo no cabe y la maquinaria
  no certifica; además ρ ≥ 1+b(t)/t > φ (fuera del dominio ρ ≤ φ),
  consistente con el suelo T.
- **Sin colas la pared no es vacua**: con α = 1+ω y ocupantes en su
  mínimo 1, la corona NO cabe en R_lb; son las colas de ρ ≤ φ las
  que la vacían.
- **Fronteras exactas** (sympy): Ψ₂(φ/2) = φ, Ψ₁(1/2) = φ,
  Ψ₃(1) = √3, la rama B en ω = 1 es el polinomio áureo, la línea
  áurea en ω = 1 vale 1−φ/2 > 0, la meseta áurea de ρ*₃ y la
  autoconsistencia de la pinza de D4; la cascada mínima j = 2 con
  Σ → 1 da o₂ = 2/φ, o₁ = 2 y α = 2φ exactos (las mismas esquinas de
  la sartén).
- **Pared activa y monotonía**: al 90% de R_lb la corona falla; subir
  R nunca pierde el certificado.
- **No prueba de más**: búsqueda adversaria de familias bloqueadas
  certificables — ninguna (acta, ataque 4).

## 8. Limitación y qué falta

B, C2 y D2 son barridos MC con dualidad tangente en R = R_lb
(evidencia computacional, no prueba sobre j, k arbitrarios): el
cierre formal pende del MISMO lema de dualidad/zigzag de la sartén
(`coronacolas.md` §4), con la ley de escala en (j, k) como lema, MÁS
el lema-extensión de §5. Con la sartén (D1–D3) y esta campaña
(D4–D6), quedan: redactar esos dos lemas y el ENSAMBLAJE (§6).
