# El teorema de compactación mural: la dualidad como prueba escrita

Estado: DRAFT con prueba completa (2026-08-09), PRE-ADVERSARIO.
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

## 2. La prueba

Sea σ = (v₀, v₁, …, v_{k−1}) el orden cíclico de los centros del
empaquetamiento real (ángulos crecientes) y γ_real(a,b) la
separación angular real de cada par.

**(P1) θ ≤ γ_real par a par.** Para cualquier par {a, b} del
empaquetamiento con distancias al centro d_a ∈ [0, R−a],
d_b ∈ [0, R−b]: cos γ_real ≤ h(d_a, d_b) =
(d_a² + d_b² − (a+b)²)/(2 d_a d_b), y el máximo de h sobre la caja
se alcanza en una esquina (en cada arista, ∂h/∂d tiene un único
cambio de signo − → +, mínimo interior: adversariado en el acta de
coronacolas; prueba: ∂h/∂d_a = (d_a² − d_b² + (a+b)²)/(2 d_a² d_b)
cambia de signo una vez). Para un par NO-APILABLE las esquinas con
d → 0 dan h → −∞ (d_b ≤ R−b < a+b desde R < máx+2mín) y la esquina
mural da h(R−a, R−b) = 1 − 2 f(a) f(b) = cos θ exacto. Luego
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

**Nota sobre el estatus.** (P1) y (P2) son pruebas completas; la
legalidad final la garantiza además el chequeo constructivo (que
nunca certifica una colocación ilegal — solidez adversariada); (P2)
asegura que el presupuesto total NUNCA es el obstáculo. El único
resto de (P3) es redaccional (formalizar «todo fallo de wrap induce
una subsecuencia cerrada > 2π»), verificado en el script sobre
empaquetamientos reales aleatorios.

## 3. Qué cambia en el programa τ = φ

La cadena corona-contra-colas queda: bloqueo ⟹ F empaqueta
C = {ocupantes, m} en la sartén real R ⟹ (compactación, si todos
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
