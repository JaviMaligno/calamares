# El lema de la cola geométrica: presupuestos uniformes en n

Estado: DRAFT con pruebas (2026-08-09), PRE-ADVERSARIO. Script:
`code/colageometrica.py` (5/5). Quita los topes de ocupantes de los
presupuestos de sombras de los teoremas escritos: thm:nestedwritten
(j ≤ 6 certificado → todo j), coronaagujero ramas 1 y 2 (k ≤ 14/12
→ todo k), y el tramo de sombras de thm:D1written. Las direcciones
j/k de los teoremas ESCRITOS dejan de ser asteriscos numéricos.

## 1. El enunciado

**Lema.** Sea T = {t₁ ≥ t₂ ≥ … ≥ t_n} una familia de cascada con
ρ ≤ φ (colas globales: cada tᵢ contiene en su cola a m, a la masa
suelta Σ y a las piezas menores), R ≥ t₁+t₂, y s con 2s < t₂
(régimen). Entonces el presupuesto de sombras de insertar s sobre
T ∪ {D_m} ∪ extras está dominado, PARA TODO n, por el mayorante
explícito G_u de §2 con u = S₃ (el sufijo de la cola), y

    sup G = 5.2115 < 2π − 0.05,

alcanzado en la esquina crítica (t₂ = 1+Σ, Σ → 1, u = φt₂,
t₁ = 2φ, w* = 1/φ con s′ = 1/2) — exactamente la misma esquina
5.2115 de los barridos de los teoremas: el lema demuestra que
AQUELLA esquina es el peor caso de TODOS los n a la vez.

## 2. El mayorante y sus cuatro ingredientes exactos

Sufijos S_i := tᵢ + t_{i+1} + … + 1 + Σ.

**(S) Decaimiento geométrico.** La cascada tᵢ ≥ S_{i+1}/φ da
S_i ≥ (1+1/φ)S_{i+1} = φS_{i+1} (identidad 1+1/φ = φ): los sufijos
decaen con razón 1/φ. En particular S₃ ≤ φt₂ y S_{3+r} ≤ S₃/φ^r.

**(M) Tres cotas por término de la cola.** Para la pieza real de
rango 3+r (orden decreciente):
- t_{3+r} ≤ t₂ (orden);
- t_{3+r} ≤ S_{3+r} − 1 − Σ ≤ u/φ^r − (1+Σ) (la pieza cabe en su
  propio sufijo tras descontar m y Σ);
- t_{3+r} ≤ (u−1−Σ)/(r+1) (hay r+1 piezas de cola ≥ ella).
El dominante es d_r = mín de las tres: dominación TÉRMINO A
TÉRMINO (asin creciente en la pieza).

**(N) Corte de existencia.** La pieza de rango 3+r arrastra sufijo
≥ 1+Σ+p_min (p_min = máx(1, (1+Σ)/φ)): r ≤ log_φ(u/(1+Σ+p_min)).
El número de términos es FINITO (logarítmico); sin el corte la
serie diverge (control E(a): 500 fantasmas ya cuestan 184 ≫ 2π).
La frontera de igualdad (t₃ = p_min con t₂ en su suelo) se INCLUYE
con tolerancia — es una instancia real (la encontró el bloque B).

**(V) El vínculo de cascada de t₁.** t₁ ≥ máx(t₂, (t₂+u)/φ) — la
cola de t₁ contiene a t₂, a la cola entera, a m y a Σ. Cola pesada
fuerza t₁ grande. NO es decorativo: sin el vínculo, t₁ = t₂ = 2
con cola llena daría 6.3734 > 2π (control E(d)) — pero esa
combinación es conjuntamente INFEASIBLE (con u = φt₂ el suelo es
t₁ ≥ 2φ, y ahí G = 5.2115). Este es el trade-off central del lema:
el adversario no puede tener a la vez el par apretado y la cola
llena.

Sobre t₁ el mayorante es la bañera exacta (`insercion.md`, bloque
G): máximo en el suelo o en el límite π (t₁ → ∞ mata las demás
sombras vía R).

## 3. La maximización certificada

G_u evaluado sobre la caja compacta (t₂ hasta 10⁶ en malla log,
Σ ∈ (1, φ], u ∈ [1+Σ, φt₂], t₁ en el suelo del vínculo × malla ×
límite π; tres modos de inserción: s′ en el tope, w* = 1/φ con s′,
y σ₂ ≤ 0.999 con la ligadura Σ ≥ 2σ₂): **sup = 5.2115**, en la
esquina crítica. Límites por fórmula: t₂ → ∞ (serie límite
explícita 5.5237 < 2π−0.4: par superior → 4asin(1/2) = 2π/3 y cola
geométrica de razón 1/φ; puntos 10⁴, 10⁶ dan 4.71); t₁ → ∞ (→ π,
margen π).

**Dominación verificada** (bloque B): 14 976 familias reales de
cascada con n hasta 40, holguras expovariate, tres modos: G ≥
presupuesto real SIEMPRE (0 violaciones; peor gap −0.000000 — la
instancia frontera t₃ = p_min con igualdad exacta, incluida).

**Controles de necesidad**: sin cascada (5 piezas iguales) la
dominación es FALSA (real 8.84 > G 4.07) — ρ ≤ φ es hipótesis
necesaria; sin régimen revienta; sin corte de existencia diverge;
sin vínculo de t₁ supera 2π.

## 4. Consecuencia

**Teorema (presupuestos uniformes).** En los teoremas escritos cuyo
paso mural es un presupuesto de sombras sobre una familia de
cascada — thm:nestedwritten (j ≥ 2), las dos ramas de agujero
(k ≥ 3), thm:D1written (j ≥ 3) — la cobertura vale para TODO
número de ocupantes: el presupuesto real está dominado por G, y
sup G = 5.2115 < 2π − 0.05 sobre toda la caja. ∎

Los topes j ≤ 6 / k ≤ 14 / k ≤ 12 de los barridos dejan de ser
parte del enunciado: pasan a ser redundancia empírica. La dirección
j de los CIERRES COMPUTACIONALES (dualidad/escala: coronas R_lb,
otro criterio) NO está cubierta por este lema y conserva su
asterisco propio (j ≤ 9/8 con crecimiento geométrico).

## 5. Estatus

Exacto (teorema): el decaimiento de sufijos (φ² = 1+φ), las tres
cotas por término, el corte de existencia, el vínculo de cascada de
t₁, la dominación término a término, el límite t₁ → ∞ (π), la
hipótesis de cascada (necesaria: control). Numérico-certificado: el
sup de G sobre la caja compacta (malla + esquinas deterministas +
serie límite por fórmula en t₂ → ∞) — la MISMA maximización
certificada única que el resto del programa (el lema de
optimización pendiente la cerraría; estándar thm:DPr). La banda de
t₁ entre el suelo y el límite se muestrea (bañera con hombro
posible): mismo estatus.
