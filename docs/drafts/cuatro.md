# Perfiles de cuatro aros: ρ*₄ = ρ*₃ y el umbral combinatorio exacto

Borrador que cierra el hueco 2 de `perfil_tres.md` §5 (y el punto 3 de
`reinsercion.md` §10 para k = 4). Resultado:

**Proposición 8.** Para todo ω ∈ (0, 1),

    ρ*₄(ω) = ρ*₃(ω) = máx( 1, mín( 2(1−ω), máx( φ, 2/(1+2ω) ) ) ) .

**Corolario 5 (umbral combinatorio exacto).** ω_c = ω_T = 1/T − 1/2. Es
decir: para ω < ω_T ningún perfil de **ningún tamaño** bloquea la reinserción
con ρ < T (k ≤ 2 por la Proposición 1, k = 3 por el Corolario 3, k = 4 por la
Proposición 8, k ≥ 5 por el Corolario 2), y para ω > ω_T el testigo de tres
aros {½+ω, ½+ε, ½+ε} bloquea con ρ = 2/(1+2ω) < T. La banda
`ω_c ∈ [?, ω_T]` que dejaba abierta el Corolario 4 colapsa a un punto.

La prueba es **íntegramente aditiva** (Lema 0 + criterio exacto del par),
como la del Corolario 3: ni el caso (ii), ni `feas3`, ni geometría de
Descartes. La sorpresa es lo corta que resulta: el cuarto aro no añade casos
nuevos al ínfimo porque cada configuración con cuatro aros «activos» produce
más presión aditiva de la que produce el perfil de tres con la misma cabeza.
Verificación: `code/cuatrok.py`.

## 1. Marco

El de `perfil_tres.md` §1 con k = 4: normalizado r_m = 1, ω ∈ (0,1),
β = 1 − ω, recursos A = N(1), B = N(β) y anidamiento recursivo (x cabe en el
agujero de y si x ≤ y − ω; un grupo de hermanos cabe en capacidad c bajo los
criterios del §1). S = {s₁ ≥ s₂ ≥ s₃ ≥ s₄} ⊂ (0,1),
ρ_needed(S) = máx(ΣS, máx_j (Σ_{l>j} s_l)/s_j), y ρ*₄ el ínfimo sobre los S
no reinsertables.

Para la cota inferior solo usamos certificados **constructivos** de
colocación (si tal colocación es válida, S es reinsertable): la fila (Lema 0:
un grupo con suma ≤ c cabe en capacidad c), el criterio exacto del par, y
anidamientos simples. Que el bloqueo implique el fallo de *estas*
colocaciones concretas es todo lo que se necesita; la exactitud de criterios
de tres o más círculos no interviene.

## 2. Demostración de la Proposición 8

(≤) Es el argumento del polvo de `perfil_tres.md` §3, caso (i): toda familia
testigo de k = 3 sigue bloqueada al añadirle un cuarto aro δ → 0 (una
colocación del perfil de 4 se restringe a una del perfil de 3), y ρ_needed
converge al valor de k = 3. Luego ρ*₄ ≤ ρ*₃.

(≥) Sea S no reinsertable; probamos ρ := ρ_needed(S) ≥ ρ*₃(ω).

**Paso 0.** Si ΣS ≤ 1, la fila en A (Lema 0) reinserta: contradicción. Luego
ΣS > 1, y ρ ≥ ΣS > 1. Esto cierra ω ≥ 1/2 (allí ρ*₃ = 1). Sea ω < 1/2, y
supóngase ρ < 2(1−ω) = 2β (si no, ρ ≥ 2β ≥ ρ*₃ y listo). Como ρ ≥ ΣS:

**Paso 1 (a lo sumo un aro supera β).** Dos aros con s_i, s_j > β darían
ΣS ≥ s_i + s_j > 2β > ρ: imposible.

**Paso 2 (caso A: s₁ > β ≥ s₂).** La colocación «s₁ → A solo, {s₂, s₃, s₄} →
B en fila» debe fallar; como cada s_i ≤ β cabe solo, el fallo es la suma:
s₂ + s₃ + s₄ > β. Entonces ΣS = s₁ + (s₂+s₃+s₄) > 2β > ρ: imposible. (Es la
versión k = 4 de por qué el caso (iii) de la Proposición 4 nunca aporta el
mínimo, ahora en una línea.)

**Paso 3 (caso B: s₁ ≤ β).** Todos caben solos en B. Tres ramas según los
anidamientos disponibles:

- **B1 (s₄ > s₁ − ω).** Ningún anidamiento es posible (todo candidato x
  cumple x ≥ s₄ > s₁ − ω ≥ y − ω para todo y ∈ S). La colocación «s₁ → B,
  {s₂, s₃, s₄} → A en fila» falla: q₃ := s₂+s₃+s₄ > 1. Además
  q₃ ≥ 3s₄ > 3(s₁ − ω). Con ρ ≥ ΣS = s₁ + q₃ y ρ ≥ q₃/s₁ (cola de s₁):

      ρ > ínf { máx(s₁ + q, q/s₁) : 0 < s₁ ≤ β, q > máx(1, 3(s₁−ω)) } .

  Este programa está **contenido** en el del caso (iv) de `perfil_tres.md`
  §3 (misma función objetivo, restricción más fuerte: 3(s₁−ω) ≥ 2(s₁−ω)),
  luego su ínfimo es ≥ el de allí, que es ≥ ρ*₃(ω) en todos los tramos. (De
  hecho la rama activa da máx(φ, 3/(1+3ω)) > máx(φ, 2/(1+2ω)): el cuarto aro
  en banda *endurece* la hipérbola de 2/(1+2ω) a 3/(1+3ω).)

- **B2 (s₄ ≤ s₁ − ω < s₃).** La colocación «s₄ anidado en s₁, s₁ → B,
  {s₂, s₃} → A en fila» falla; el anidamiento y las capacidades son válidos,
  luego el fallo es q₂ := s₂ + s₃ > 1. Además s₂ ≥ s₃ > s₁ − ω da
  q₂ > 2(s₁ − ω). Con ρ ≥ ΣS > s₁ + q₂ y ρ ≥ (q₂ + s₄)/s₁ > q₂/s₁:

      ρ > ínf { máx(s₁ + q, q/s₁) : 0 < s₁ ≤ β, q > máx(1, 2(s₁−ω)) } ,

  **exactamente** el programa del caso (iv) de `perfil_tres.md`, cuyo ínfimo
  es 2/(1+2ω), φ o 1/(1−ω) según el tramo, siempre ≥ ρ*₃(ω) (Corolario 3).
  Este es el caso que muerde: el polvo del argumento (≤) vive aquí.

- **B3 (s₃ ≤ s₁ − ω y s₄ ≤ s₁ − ω).** Si además s₄ ≤ s₂ − ω, la colocación
  «s₃ en s₁, s₄ en s₂, s₁ → A, s₂ → B» es válida: contradice el bloqueo.
  Luego s₄ > s₂ − ω. Ahora fallan las dos colocaciones «s₄ en s₁, s₁ → B,
  {s₂, s₃} → A» y «s₃ en s₁, s₁ → B, {s₂, s₄} → A», es decir s₂ + s₃ > 1 y
  s₂ + s₄ > 1. Entonces s₃ > 1 − s₂ y s₄ > 1 − s₂, y

      ΣS > s₁ + s₂ + 2(1 − s₂) = 2 + (s₁ − s₂) ≥ 2 > 2β > ρ :

  imposible. (B3 es vacío bajo ρ < 2β.)

En todas las ramas ρ ≥ ρ*₃(ω) o contradicción. ∎

## 3. Lectura

- **Por qué el cuarto aro no baja el umbral.** El ínfimo de k = 3 vive en el
  caso (iv): cabeza s₁ y una cola q = s₂ + s₃ > máx(1, 2(s₁−ω)). Un cuarto
  aro solo puede (a) quedarse en banda —y entonces engorda la cola a
  q₃ > máx(1, 3(s₁−ω)), subiendo la hipérbola a 3/(1+3ω)—, (b) anidar en s₁
  sin tocar la estructura —y entonces el perfil efectivo es el de tres, rama
  B2, mismo ínfimo—, o (c) permitir dos anidamientos, que reabren la
  reinserción salvo a costa de dos pares por encima de 1 (Σ > 2). No hay
  cuarta opción: la presión aditiva es monótona en el tamaño del perfil una
  vez fijada la cabeza.
- **El patrón k general.** Los pasos 0–2 y B1/B3 no usan k = 4: sugieren que
  ρ*_k = ρ*₃ para todo k ≥ 3 por inducción (la rama «s_k anida en s₁ y el
  resto es un perfil de k−1» reduciría a k−1). No se hace aquí: para el
  programa solo hacía falta k = 4 (el Corolario 2 ya excluye k ≥ 5 bajo T);
  queda anotado como extensión natural.
- **ω_c cerrado.** Con el Corolario 5, la garantía combinatoria de
  `reinsercion.md` §6 queda exacta: reinserción asegurada (sin geometría)
  para todo perfil si y solo si ω < ω_T = 1/T − 1/2 = T² − T − 3/2
  ≈ 0.0436891. Nótese la coincidencia notable con la juntura ω₁ ≈ 0.0413570
  de la curva del grosor (`drafts/esquina.md`): son objetos distintos
  (cúbicas distintas), pero ambos viven en la misma ventana ω ≈ 0.04, la
  «zona de riesgo» real del programa.

## 4. Huecos declarados

1. **Ninguno en la cadena de la Proposición 8**: la prueba usa solo Lema 0,
   el criterio exacto del par y anidamientos simples (certificados
   constructivos); ni feas3 ni el caso (ii) de la Proposición 4 intervienen.
2. **ρ*_k para k ≥ 5** por encima de T sigue sin fórmula (irrelevante para
   el programa: Corolario 2). La inducción esbozada en §3 queda sin hacer.
3. **Ínfimo no alcanzado**, como en todo el programa (condiciones de bloqueo
   abiertas).

## Mapa de verificación

`code/cuatrok.py`, cuatro bloques: **[A]** identidades en sympy exacto
(dominación 3/(1+3ω) − 2/(1+2ω) = 1/((1+3ω)(1+2ω)) > 0, el álgebra de B3
Σ > 2 + (s₁−s₂), el punto fijo áureo, el cruce ω_T = 1/T − 1/2 como
identidad, y el cruce hipérbola/2(1−ω)); **[B]** búsqueda adversaria con
oráculo generoso de reinserción (todos los bosques de anidamiento con
agujeros de contenido múltiple, repartos A/B con fila + par exacto + feas3):
ningún perfil bloqueado por debajo de ρ*₃ en 13 valores de ω sobre los
cuatro tramos con muestreo dirigido a las familias críticas con polvo;
**[C]** validación mecánica del árbol de la prueba: sobre miles de perfiles
bloqueados muestreados, la clasificación (paso 0/1/2, B1/B2/B3) asigna rama,
las condiciones forzadas se cumplen y la cota de la rama vale ≥ ρ*₃;
**[D]** familias de polvo por tramo (bloqueadas según el oráculo, con
ρ_needed a < 10⁻³ de ρ*₃) y el Corolario 5.
