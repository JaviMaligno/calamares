# El teorema de compactación mural: la dualidad como prueba escrita

Estado: ADVERSARIADO (2026-08-09, acta en VEREDICTOS.md):
CONFIRMADO CON CORRECCIONES — la prueba de §2 resiste; (P1)
re-derivado simbólicamente; corregidas la arista cero que faltaba y
la exclusión del origen (ahora cuantitativa); la cláusula de
bolsillos del enunciado ahora tiene su prueba en §2 (era un hueco:
§2 no la probaba).
Script: `code/compactacion.py`. Es la conversión de los cierres
computacionales en matemática escrita: elimina R_lb, los barridos y
la dirección j del programa τ = φ de un solo golpe.

## 1. El teorema

**Teorema (compactación mural).** Sea C = {c₁, …, c_k} una familia
de círculos empaquetada en el disco de radio R (interiores
disyuntos, tangencias permitidas), y supóngase que todo par de C es
NO-APILABLE en R: R < máx(a,b) + 2·mín(a,b) para todo par {a,b}.
Entonces C admite un empaquetamiento MURAL en R: existe una
colocación con todos los círculos tangentes a la pared, en el orden
cíclico del empaquetamiento original, legal (todas las parejas a
separación angular ≥ θ, con sin²(θ(a,b)/2) = f(a)f(b),
f(x) = x/(R−x)). Además, en esa colocación cada pieza «saltada» por
el camino crítico queda muralmente dentro del hueco de su par de
espina, y es sub-bolsillo de Descartes de ese par.

**La hipótesis es tight (ronda hostil 2026-08-09).** No puede
suprimirse: la familia anillo (central c + corona de n círculos r
tangentes a la pared en R = c + 2r, todos los pares apilables) es un
empaquetamiento real explícito con Σθ_adyacentes > 2π en todo orden
cíclico — ningún empaquetamiento mural existe. Y no puede rebajarse
a «no-apilable respecto del mayor»: L = 2 mural + 7 círculos 0.76
murales + 1 interior en R = 3.51 empaqueta de verdad, tiene todos
los pares (L, s) no-apilables (3.51 < 3.52) y los (s, s) apilables,
y Σθ_ady = 6.519 > 2π: sin mural (controles (a')/(a'') del script).

## 2. La prueba (proyección mural: tres líneas)

**Colocación:** empújese cada círculo a la pared EN EL ÁNGULO REAL
de su centro: c_i ↦ posición mural (R − r_i) · (cos ψ_i, sin ψ_i),
con ψ_i el ángulo del centro real. [Ningún centro está en el origen,
cuantitativamente: para todo par no-apilable {a, b} (a ≥ b),
d_b ≤ R − b y |c_a − c_b| ≤ d_a + d_b fuerzan
d_a ≥ (a+b) − (R−b) = a + 2b − R > 0, y simétricamente
d_b ≥ 2a + b − R ≥ a + 2b − R > 0: los centros viven en un anillo
con margen positivo. (La versión cualitativa: un centro en el origen
exige R ≥ a + 2c para todo otro c, que es apilable si c ≤ a y, si
c > a, a + 2c ≥ c + 2a lo da a fortiori.) k = 1 es trivial:
cualquier ángulo mural sirve. Y dos círculos no comparten ángulo:
γ_real ≥ θ > 0 por (P1).]

**Legalidad:** la separación angular de cada par NO cambia (es la
real, γ_real). Por (P1), γ_real(a,b) ≥ θ(a,b) para todo par
no-apilable, y θ(a,b) es por definición (lem:S1) el ángulo mural
mínimo de disyunción: dos círculos murales a separación ≥ θ(a,b)
tienen centros a distancia ≥ a+b. Luego todos los pares son
disyuntos. ∎

**La cláusula de bolsillos (el «además» del enunciado).** Sobre el
orden cíclico real σ defínase el θ-DP (camino más largo con pesos
θ): es combinatoria pura sobre los θ, independiente de dónde estén
los círculos. Si la arista de espina (a, b) salta la pieza s,
entonces (i) ψ_s está estrictamente entre ψ_a y ψ_b (la espina
respeta el orden de σ = el orden angular real); (ii) la legalidad ya
probada de TODAS las parejas proyectadas deja a s mural dentro del
hueco de a y b; (iii) por maximalidad del DP,
θ(a,s) + θ(s,b) ≤ θ(a,b) (ESP-individual, acta de zigzag: tres
líneas, α[s] ≥ α[a] + θ(a,s), α[b] ≥ α[s] + θ(s,b),
α[b] = α[a] + θ(a,b)), y por DIC, s ≤ p(a, b, R): sub-bolsillo de
Descartes de su par de espina. Nada de esto usa el wrap. ∎

No hace falta el camino más largo, ni orden alguno: la proyección
preserva el orden cíclico real automáticamente. (P2) queda como
COROLARIO con contenido propio — el presupuesto del certificado — y
(P1) es el único ingrediente con prueba no trivial.

## 2b. Los ingredientes en detalle

Sea σ = (v₀, v₁, …, v_{k−1}) el orden cíclico de los centros del
empaquetamiento real (ángulos crecientes) y γ_real(a,b) la
separación angular real de cada par.

**(P1) θ ≤ γ_real par a par.** Sea {a, b} un par del
empaquetamiento, a ≥ b. Primero, θ(a,b) está bien definida:
a+b ≤ |c_a−c_b| ≤ d_a + d_b ≤ (R−a) + (R−b) da a + b ≤ R, luego
f(a)f(b) ≤ 1. Por la ley de cosenos y la disyunción
|c_a − c_b| ≥ a+b: cos γ_real ≤ h(d_a, d_b) =
(d_a² + d_b² − (a+b)²)/(2 d_a d_b) (necesita d_a, d_b > 0: dado por
la cota del anillo de §2). El máximo de h sobre la caja
(0, R−a] × (0, R−b] se alcanza en una esquina:
∂h/∂d_a = (d_a² − d_b² + (a+b)²)/(2 d_a² d_b) es > 0 en toda la
arista si d_b ≤ a+b, y si d_b > a+b cambia de signo una sola vez
− → + (mínimo interior); en ambos casos el máximo por arista está en
los extremos (adversariado en el acta de coronacolas y re-derivado
con sympy en esta ronda). Para un par NO-APILABLE las tres esquinas
con algún d → 0 dan h → −∞, porque AMBAS coordenadas quedan bajo
a+b en toda la caja: d_b ≤ R−b < a+b ⟺ R < a+2b (= máx+2mín,
la definición), y d_a ≤ R−a < a+b ⟺ R < 2a+b, que se sigue de
a ≥ b (a+2b ≤ 2a+b); la esquina (0,0) da −∞ por cualquier
dirección de entrada. La esquina mural da
h(R−a, R−b) = 1 − 2 f(a) f(b) = cos θ exacto (identidad
polinómica). Con γ_real, θ ∈ [0, π] y cos decreciente ahí:
γ_real(a,b) ≥ θ(a,b) para TODO par, adyacente o no. ∎(P1)

**(P2) El camino más largo está acotado por 2π.** La construcción
mural coloca por camino más largo sobre el orden σ: posiciones
α_i = máx sobre subsecuencias 0 = w₀ < w₁ < … < w_t = i de
Σ θ(w_s, w_{s+1}), y total = α_{k−1} + θ(v_{k−1}, v₀). Para
CUALQUIER subsecuencia con su cierre: las separaciones reales
consecutivas-en-subsecuencia, medidas consistentemente en el sentido
del orden, PARTICIONAN el círculo real:

    Σ_s γ_real→(w_s, w_{s+1}) = 2π  (exacto),

donde γ_real→ es la distancia angular en el sentido de recorrido
(≥ γ_real, la separación mínima). Por (P1),
θ(w_s, w_{s+1}) ≤ γ_real(w_s, w_{s+1}) ≤ γ_real→(w_s, w_{s+1}),
luego Σ_s θ ≤ 2π para TODA subsecuencia cerrada, y en particular
para la crítica: total ≤ 2π. ∎(P2)

**(P3) Solidez de la colocación.** Con total ≤ 2π, la colocación
por camino más largo es legal: (i) por definición del DP,
α_j − α_i ≥ θ(i, j) para todo i < j (DP-adelante), así que solo el
arco de cierre (wrap) podría fallar; (ii) el fallo del wrap para el
par (i, j) significa (α_j − α_i) + θ(i,j) > 2π; pero
α_j − α_i ≤ α_j ≤ camino crítico hasta j, y el camino de j a i por
el cierre forma una subsecuencia cerrada cuya suma excedería 2π,
contradicción con (P2) aplicado a la subsecuencia
(camino crítico hasta i) ∪ {j}: en detalle, α_i ≥ θ-camino de 0 a i
y la subsecuencia 0 → … → i (crítica de i), j, cierre a 0 tiene suma
α_i + θ(i, j) + θ(j, 0)... el par (i,j) con i < j: la subsecuencia
crítica de j seguida del cierre j → 0 da α_j + θ(j,0) ≤ 2π (P2);
como α_j ≥ α_i + θ(i,j), se tiene α_j − α_i ≤ 2π − θ(j,0) − α_i +
(α_j − α_j)… la forma limpia: para el par (i,j),
(α_j − α_i) + θ(i,j) ≤ α_j + θ(i,j) − θ-camino(0→i)… y la
subsecuencia (crítica de i) ∪ {j} cerrada da
α_i + θ(i,j) + θ(j,0)-camino-de-vuelta ≤ 2π con la vuelta ≥ 0…
[REDACCIÓN FINA PENDIENTE — el mecanismo es: todo candidato a fallo
del wrap induce una subsecuencia cerrada que excedería 2π; el
chequeo explícito de parejas del algoritmo lo hace incondicional:
si el chequeo pasa, la colocación es legal (solidez del acta de
zigzag), y (P2) garantiza que el TOTAL nunca lo impide.]
(iii) cada saltado s entre espinas a, b cumple
θ(a,s) + θ(s,b) ≤ θ(a,b) por maximalidad (acta de zigzag, ESP
fortalecido) y por DIC es sub-bolsillo de su par: queda mural dentro
del hueco. ∎

**Nota sobre el estatus (revisada).** El teorema completo se prueba
en §2 por proyección mural, con (P1) como único ingrediente no
trivial: NO queda redacción pendiente. (P2) y (P3) se conservan
porque tienen contenido adicional: (P2) acota el presupuesto de
CUALQUIER subsecuencia (la versión certificado de la dualidad) y
(P3) describe la variante por camino más largo (que produce además
la estructura de espina/bolsillos usada por el reparto); su intento
de prueba del wrap vía (P2) NO cierra en general (los intentos
directos dan la desigualdad al revés) y queda documentado como
abierto SIN carga: la proyección de §2 lo esquiva por completo, y
para el reparto la holgura de la proyección (huecos ≥ tangencia)
basta.

## 3. Qué cambia en el programa τ = φ

La cadena corona-contra-colas queda: bloqueo ⟹ F empaqueta
C = {ocupantes, m} en la sartén real R (caso sartén: los ocupantes
están a nivel superior por definición y «F places m at top level»,
app:pan-app del paper) ⟹ (compactación, si todos
los pares son no-apilables) C se compacta MURALMENTE en R con
bolsillos de Descartes explícitos ⟹ el reparto (σ₁ → D_m, perfil y
polvo a los bolsillos/carteras, lema del bolsillo-φ) desbloquea:
contradicción. SIN R_lb, SIN biseccion, SIN barridos en j: vale
para todo j, p, k de una vez.

Las piezas que quedan para el teorema pleno por dominio:
1. NO-APILABILIDAD de los pares del muro en R (por dominio): para
   pares de ocupantes con cascada — álgebra de esquinas; los pares
   apilables (piezas chicas vs R grande) van al reparto de bolsillos
   directamente (una pieza apilable respecto del gigante cabe tras
   él: R ≥ o₁ + 2b ⟹ b cabe en la cartera trasera — tratar por
   casos).
2. El REPARTO: capacidades de los bolsillos flanqueantes de o₁ +
   D_m + H_m ≥ masas (esquinas exactas; el bolsillo-φ ya da la
   versión (o₁, o₂) adyacentes y las carteras flanqueantes dan
   ≥ 0.764 ≥ φ−1 ≥ σ₂ en el mínimo de la cascada — certificar).
3. La versión anidada y el puerto: mismas piezas con el disco
   contenedor correspondiente (portables: ya inspeccionado).

Con 1-3 escritos, los cierres computacionales D1/D3/D4-D6/(c-i)/
(c-ii)/R2b se convierten en teoremas con el estándar del paper
(esquinas exactas + certificados de una variable), y el asterisco
numérico desaparece por completo.
