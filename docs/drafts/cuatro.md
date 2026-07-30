# Perfiles de k aros: ρ*_k = ρ*₃ para todo k ≥ 3 y el umbral combinatorio exacto

Borrador que cierra el hueco 2 de `perfil_tres.md` §5 (y el punto 3 de
`reinsercion.md` §10 **para todo tamaño de perfil**). Resultado:

**Proposición 8.** Para todo ω ∈ (0, 1) y todo k ≥ 3,

    ρ*_k(ω) = ρ*₃(ω) = máx( 1, mín( 2(1−ω), máx( φ, 2/(1+2ω) ) ) ) .

**Corolario 5 (umbral combinatorio exacto).** ω_c = ω_T = 1/T − 1/2. Es
decir: para ω < ω_T ningún perfil de **ningún tamaño** bloquea la reinserción
con ρ < T (k ≤ 2 por la Proposición 1, k ≥ 3 por la Proposición 8), y para
ω ∈ (ω_T, (√5−2)/2] el testigo de tres aros {½+ω, ½+ε, ½+ε} bloquea con
ρ = 2/(1+2ω) < T. La banda `ω_c ∈ [?, ω_T]` que dejaba abierta el
Corolario 4 colapsa a un punto — y ya sin invocar el Corolario 2, que solo
cubre perfiles con todos los aros en banda y no bastaba (véase §4).

La prueba es **íntegramente aditiva** (Lema 0 + criterio exacto del par +
anidamientos simples), como la del Corolario 3: ni el caso (ii), ni `feas3`,
ni geometría de Descartes. Historia: la primera versión de este borrador
demostraba solo k = 4 (árbol A/B1/B2/B3, §3) y cerraba k ≥ 5 con el
Corolario 2; la verificación adversaria refutó ese cierre (el Corolario 2 no
aplica a perfiles con polvo) y aportó el árbol general de §2, más corto, que
cubre todo k ≥ 3 de una vez. Verificación: `code/cuatrok.py` y el acta en
`VEREDICTOS.md`.

## 1. Marco

El de `perfil_tres.md` §1 con k arbitrario: normalizado r_m = 1, ω ∈ (0,1),
β = 1 − ω, recursos A = N(1), B = N(β) y anidamiento recursivo (x cabe en el
agujero de y si x ≤ y − ω; un grupo de hermanos con suma ≤ c cabe en
capacidad c — la fila del Lema 0). S = {s₁ ≥ … ≥ s_k} ⊂ (0,1),
ρ_needed(S) = máx(ΣS, máx_j (Σ_{l>j} s_l)/s_j), y ρ*_k el ínfimo sobre los S
no reinsertables.

Para la cota inferior solo usamos certificados **constructivos** de
colocación (si tal colocación es válida, S es reinsertable): fila, criterio
exacto del par, anidamientos simples. Que el bloqueo implique el fallo de
*estas* colocaciones concretas es todo lo que se necesita. Dos hechos
elementales que se usan sin mención: ρ_needed es monótono al añadir aros
menores (la suma y todas las colas crecen), y si un subconjunto «prefijo»
{s₁,…,s_j} ya es no reinsertable, S entero lo es (toda colocación se
restringe).

## 2. Demostración de la Proposición 8 (árbol general, todo k ≥ 3)

(≤) Argumento del polvo de `perfil_tres.md` §3: toda familia testigo de
k = 3 sigue bloqueada al añadirle k−3 aros δ → 0, y ρ_needed converge al
valor de k = 3. Luego ρ*_k ≤ ρ*₃.

(≥) Sea S no reinsertable con k aros; probamos ρ := ρ_needed(S) ≥ ρ*₃(ω).

**Paso 0.** La fila de todos en A falla: ΣS > 1, luego ρ > 1. Esto cierra
ω ≥ 1/2 (ρ*₃ = 1). Sea ω < 1/2, y supóngase ρ < 2β (si no, ρ ≥ 2β ≥ ρ*₃).

**Paso 1 (s₁ ≤ β).** Dos aros > β darían Σ > 2β ≥ ρ ≥ Σ. Y si solo s₁ > β:
«s₁ → A solo, resto → B en fila» falla, y como cada s_i ≤ β cabe solo, el
fallo es la suma: Σ − s₁ > β, luego Σ > 2β: imposible. Queda s₁ ≤ β.

**Paso 2 (la cola supera 1).** «s₁ → B, resto → A en fila» falla:
Q := Σ − s₁ > 1. Con ρ ≥ Σ = s₁ + Q y ρ ≥ Q/s₁ (cola de s₁):
ρ ≥ mín_{s ≤ β} máx(1+s, 1/s), que vale φ si β ≥ 1/φ y 1/β si no. Eso da
ρ ≥ ρ*₃ para todo ω ≥ (√5−2)/2 = 0.1180… (el arranque de la meseta áurea:
allí ρ*₃ ≤ φ, y para ω ≥ 1 − φ/2 se compara con 2β y 1/β como en
`perfil_tres.md`). Sea pues ω < (√5−2)/2, donde ρ*₃ = 2/(1+2ω); hacia
contradicción, supóngase ρ < 2/(1+2ω). De ρ ≥ Q/s₁ > 1/s₁ sale
s₁ > (1+2ω)/2 = ½ + ω, en particular **s₁ − ω > ½**.

**Paso 3 (cuántos aros quedan por encima del agujero de s₁).** Sea
p := #{i : s_i > s₁ − ω}. Todos esos aros superan ½, y Σ ≤ ρ < 2 permite a
lo sumo tres: p ∈ {1, 2, 3} (p ≥ 1 porque cuenta a s₁).

- **p ≥ 3**: s₁, s₂, s₃ > s₁ − ω > ½. Ningún par cabe junto en una raíz
  (sumas > 1 > β, criterio exacto del par) y nadie anida en nadie
  (s_j ≤ s_i − ω ≤ s₁ − ω < s_j es imposible, y no hay aros mayores donde
  anidar). Tres aros de nivel superior con dos raíces: el **prefijo
  {s₁, s₂, s₃} ya es no reinsertable**, luego
  ρ ≥ ρ_needed({s₁,s₂,s₃}) ≥ ρ*₃.

- **p = 2**: s₃, …, s_k ≤ s₁ − ω. La colocación «{s₃,…,s_k} en fila dentro
  del agujero de s₁ (capacidad s₁ − ω), s₁ → A, s₂ → B» falla; todas sus
  piezas son válidas salvo, a lo sumo, la fila del agujero: R := Σ_{i≥3} s_i
  > s₁ − ω. Con s₂ > s₁ − ω (p = 2), la cola Q = s₂ + R > 2(s₁ − ω), y
  Q > 1 (Paso 2): exactamente el programa del caso (iv) de
  `perfil_tres.md`,

      ρ ≥ ínf { máx(s₁ + q, q/s₁) : 0 < s₁ ≤ β, q > máx(1, 2(s₁−ω)) } =: I₂(ω),

  cuyo valor es 2/(1+2ω) / φ / 1/(1−ω) por tramos, siempre ≥ ρ*₃
  (Corolario 3). **Esta es la única rama que muerde**: el polvo de (≤) vive
  aquí.

- **p = 1**: s₂ ≤ s₁ − ω. La colocación «s₂ en el agujero de s₁, s₁ → B,
  {s₃,…,s_k} → A en fila» falla: R′ := Σ_{i≥3} s_i > 1. Entonces
  Σ = s₁ + s₂ + R′ > (s₂ + ω) + s₂ + 1 = 1 + 2s₂ + ω, y la cola de s₂ da
  ρ ≥ R′/s₂ > 1/s₂. Luego

      ρ ≥ mín_s máx(1 + 2s + ω, 1/s) = [ (1+ω) + √((1+ω)² + 8) ] / 2 ≥ 2

  (el valor en ω = 0 es 2 y crece con ω): contradice ρ < 2β < 2. (Para
  k = 3 esta rama es directamente vacía: R′ = s₃ < 1.)

En todas las ramas, ρ ≥ ρ*₃(ω) o contradicción. ∎

El árbol es del verificador adversario (véase el acta); sustituye al cierre
ilegítimo por el Corolario 2 y de paso hace el resultado uniforme en k.

## 3. La prueba original de k = 4 (se conserva: está validada por rama)

La primera versión demostraba k = 4 con un árbol más fino que sigue siendo
correcto (auditado y validado mecánicamente rama a rama): tras los pasos
0–1 de §2, con todos los aros ≤ β,

- **B1** (s₄ > s₁−ω, sin anidamientos): q₃ := s₂+s₃+s₄ > 1 por la fila en A,
  y q₃ ≥ 3s₄ > 3(s₁−ω): programa contenido en el del caso (iv)
  (3(s₁−ω) ≥ 2(s₁−ω)), luego ρ ≥ I₂(ω) ≥ ρ*₃; de hecho la rama activa
  endurece la hipérbola a 3/(1+3ω) mientras 3(s₁−ω) manda (ω ≤ 1−1/φ; para
  ω mayores I₃ = 1/(1−ω), igual que I₂).
- **B2** (s₄ ≤ s₁−ω < s₃): «s₄⊂s₁, s₁→B, {s₂,s₃}→A» falla ⟹ q₂ := s₂+s₃ > 1
  y q₂ > 2(s₁−ω): el caso (iv) exacto. Es el análogo k=4 de la rama p=2.
- **B3** (s₃, s₄ ≤ s₁−ω): si s₄ ≤ s₂−ω, «s₃⊂s₁→A, s₄⊂s₂→B» reinserta
  (contra); luego s₄ > s₂−ω, y de «s₄⊂s₁→B, {s₂,s₃}→A» y «s₃⊂s₁→B,
  {s₂,s₄}→A» salen s₂+s₃ > 1 y s₂+s₄ > 1, de donde
  Σ > 2 + (s₁−s₂) ≥ 2 > 2β: imposible.

Nótese que B3 usa dos anidamientos separados y es genuinamente k = 4 (con
k > 4 dejaría aros huérfanos); el árbol general de §2 lo evita con la fila
dentro del agujero de s₁.

## 4. Lectura

- **Por qué ningún k baja el umbral.** El ínfimo de k = 3 vive en el caso
  (iv): cabeza s₁ y cola q > máx(1, 2(s₁−ω)). Con más aros, la cola por
  encima del agujero de s₁ solo puede engordar (p ≥ 3 bloquea ya el
  prefijo; p = 1 exige cola > 1 dentro de A y dispara ρ ≥ 2), y la única
  configuración ajustada es p = 2: la misma cabeza, la misma cota, el mismo
  ínfimo. La presión aditiva es monótona en el tamaño del perfil una vez
  fijada la cabeza.
- **Sobre el Corolario 2 de `reinsercion.md`.** Solo cubre perfiles con los
  k aros **todos en la banda** (1−ω, 1); como ρ*_{k+1} ≤ ρ*_k (polvo), no
  podía cerrar k ≥ 5 por sí solo — el hueco que detectó la verificación.
  Con la Proposición 8 el papel del Corolario 2 en el programa queda
  reducido a lo que siempre fue: excluir bloqueos de muchos aros en banda.
- **ω_c cerrado.** La garantía combinatoria de `reinsercion.md` §6 queda
  exacta: reinserción asegurada (sin geometría) para todo perfil si y solo
  si ω < ω_T = 1/T − 1/2 = T² − T − 3/2 ≈ 0.0436890. Nótese la cercanía —
  son objetos distintos, cúbicas distintas — con la juntura de la curva del
  grosor de `drafts/esquina.md` (la raíz 0.0413570 de 4ω³−20ω²+25ω−1):
  ambas viven en la ventana ω ≈ 0.04, la «zona de riesgo» real del programa.

## 5. Huecos declarados

1. **Ninguno en la cadena de la Proposición 8**: solo Lema 0, criterio
   exacto del par y anidamientos simples; ni feas3 ni el caso (ii) de la
   Proposición 4 intervienen. El antiguo apoyo en el Corolario 2 está
   retirado.
2. **ρ*_k para k ≤ 2**: Proposición 1 (`reinsercion.md`), ya cerrada;
   ρ*₂ = máx(1, 2(1−ω)) ≥ ρ*₃ como debe.
3. **Ínfimo no alcanzado**, como en todo el programa.
4. Confirmación numérica pendiente de bajo valor: barrido dirigido k = 5–7
   (el verificador lo dejó escrito pero sin ejecutar por la caída del
   tooling); el bloque [E] de `cuatrok.py` lo cubre para k = 5 y 6.

## Mapa de verificación

`code/cuatrok.py`, cinco bloques: **[A]** identidades en sympy exacto
(dominación 3/(1+3ω) − 2/(1+2ω) = 1/((1+3ω)(1+2ω)) > 0, el álgebra de B3 y
del paso p = 1 (mínimo [(1+ω)+√((1+ω)²+8)]/2 ≥ 2), el punto fijo áureo, el
cruce ω_T = T² − T − 3/2 **módulo la cúbica de Tribonacci**, y el cruce
hipérbola/2(1−ω)); **[B]** búsqueda adversaria con oráculo de reinserción
**conservador en grupos de ≥ 4 hermanos** (bosques de anidamiento completos,
repartos A/B con fila + par exacto + feas3; el sesgo bloqueante es el sesgo
seguro aquí: sobredeclarar bloqueos solo puede crear falsos candidatos por
debajo de ρ*₃, y no aparece ninguno) en 13 valores de ω; **[C]** validación
mecánica de los DOS árboles con muestreadores dedicados por rama (paso 1,
B1, B2, B3, p = 1, p = 2, p ≥ 3), incluyendo las ramas que cierran por
contradicción (se comprueba Σ > 2β o Σ > 2 explícitamente, no por
descarte); **[D]** familias de polvo por tramo — su bloqueo genuino no
descansa en el sesgo del oráculo: ninguna requiere grupos de ≥ 4 hermanos
(las sumas de pares ya fallan), y la verificación adversaria lo confirmó
con un oráculo permisivo independiente con solver — y el Corolario 5;
**[E]** barrido k = 5 y k = 6: sin bloqueos bajo ρ*₃.
