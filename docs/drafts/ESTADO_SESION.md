# Estado de la sesión (2026-07-31) — traspaso para la Batalla 1

Documento de retoma para una sesión nueva. Todo lo listado como cerrado está
verificado adversarialmente, consolidado en los documentos y pusheado
(último commit: `c4d027a`). **El programa de la conjetura del umbral de
Tribonacci tiene un único hueco bloqueante: `reinsercion.md` §10.1, partido
en las Batallas 1 y 2 de abajo.**

## 1. Mapa de lo cerrado (no retocar; actas en `drafts/VEREDICTOS.md`)

| resultado | dónde | código |
|---|---|---|
| Teorema S (suelo rígido, sin idealización) + S5 + S6 + **Lema S6a** | `drafts/suelo_rigido.md` | `rigido.py` 7/7 |
| **H1**: κ = √(g(σ₂)/g(σ₁)) ∀α>1; frontera t(σ₁)+t(σ₂) = t(b(α)); cierre Tribonacci | `drafts/h1.md` | `h1.py` 5/5 |
| Grosor: Φ(ω), cota T+0.0098 | `drafts/grosor_positivo.md` | `grosor.py` 8/8 |
| **Curva exacta del grosor + Teorema de la esquina**: inf T_can = 13/7 sin módulo; ω₁ cúbica; α_m séxtica; bump (ω₁ mín local, ω_peak grado 8) | `drafts/esquina.md` | `esquina.py` 5/5 |
| Perfil k=3: ρ*₃ cerrada, meseta áurea | `drafts/perfil_tres.md` | `tresk.py` |
| **ρ*_k = ρ*₃ ∀k≥3; ω_c = ω_T = 1/T−1/2 exacto** (árbol general; ¡el Corolario 2 NO basta para k≥5!) | `drafts/cuatro.md` | `cuatrok.py` 5/5 |
| Cuadrado: X, b_□(X) = X−1 (con sus matices de acta) | `drafts/cuadrado.md` | `cuadrado.py` |
| **Lema U (frontera universal) + Teorema S con holgura (Corolario U1)** | `drafts/universal.md` | `universal.py` 5/5 |

## 2. El arsenal para las batallas (léase `drafts/universal.md` primero)

- **Lema U.** Trío {A, x, y} tangente a pared en disco R arbitrario, con
  c = R−A, T_c(x) = √((c−x)/x): infactible-angular ⟺ T_c(x)+T_c(y) ≤ c/√(AR),
  **BAJO la hipótesis A ≥ mín(x,y)** (sin ella es FALSO — ver acta; la
  dirección ⟹, la que usan las cotas inferiores, es incondicional).
- **Bolsillo general** b_R(A) = ARc/(AR+c²), creciente en R, ≤ A.
- **κ = √(g_c(y)/g_c(x))**, g_c(s) = s³(c−s); umbral afilado del κ ≥ 1:
  3c² ≤ 4AR; en la banda x,y ≤ A margen κ² ≥ 2.442.
- **G_c-identidad**: G_c = (c²/4)U′², U(z) = c/(1+z²) — monotonía de G_c ⟺
  concavidad de U; motor único de TODAS las optimizaciones del programa.
- **Cota de existencia**: bloqueo con cabeza A solo si R < (1+2/√3)A ≈ 2.1547A.
- **Lema S6a** (cierre/monotonía): propaga infactibilidades a [0, δ₀);
  con S5 hace genuinas las familias en σ₁ → 1 (sin módulo feas3).
- **Patrón de prueba de `cuatro.md` §2** (árbol general de perfiles): la
  presión aditiva es monótona en el tamaño; sospecho que la Batalla 1 tiene
  un árbol análogo en "número de ocupantes".

## 3. BATALLA 1: v genérico (ocupantes interiores) — el corazón

**Enunciado objetivo.** En el paso de intercambio, v es un disco de radio R
con ocupantes O = {o₁ ≥ … ≥ o_j} ∪ {m} empaquetados (los mayores que m
coinciden en F y en P; normalizar m = 1); m sale; S debe reinsertarse en
v ∪ H_m ∪ anidamientos. Probar: todo bloqueo tiene ρ ≥ T (ρ = colas de la
instancia completa, que INCLUYEN a los o_i).

**Plan de ataque sugerido (en orden):**
1. **Corona exacta.** Generalizar el Lema S2 a k círculos tangentes a pared:
   si la suma de arcos consecutivos (en algún orden) ≤ 2π, empaqueta —
   constructivo, misma prueba que S2 par a par. Con el Lema U cada arco es
   θ(a,b) y la infactibilidad de corona queda casi-aditiva en T_c (con
   término de orden: minimizar sobre permutaciones). Deliverable: "Lema U_k"
   para coronas.
2. **Dos ocupantes en corona** (v = sartén R, O = {α, γ}, S = par): resolver
   el programa de bloqueo exacto con el Lema U_k y las paredes (B2)/(B4)/(W)
   del programa canónico (`grosor_positivo.md` §1). Conjetura fina a
   demostrar: el óptimo del adversario es γ → ausente (o γ → tangencia que
   degenera a la plantilla canónica), es decir T_gen = T_can ≥ 13/7. La
   palanca: la cola de γ, (1+σ₁+σ₂)/γ ≥ (3−2ω)/γ — γ pequeño se autocastiga
   (evidencia: `universal.py` [E], cola de γ dominante en 321/321,
   mejor ρ = 2.56); γ grande estorba menos que α (monotonías del Lema U).
3. **Ocupantes interiores → corona** (el paso duro): lema de "empujar a la
   pared": ¿el v adversarialmente óptimo tiene todos los ocupantes en
   corona? Idea: dado un bloqueo con ocupante interior, moverlo a la pared
   no puede DESBLOQUEAR (¿o sí? — explorar primero numéricamente con el
   solver físico de `sim.py`/`pack_feasible` como oráculo). Si es falso en
   general, plan B: "lema del hueco" vía densidad crítica 1/2 de
   Fekete–Keldenich–Scheffer (citada en `hoja_de_ruta.md` §2 plan): con
   ρ < T el área de S es pequeña y el hueco mayor de v−m debe absorber al
   par crítico. La pista √δ de `rigido.py` V7b (rigidez aproximada) puede
   cuantificar el hueco alrededor de D_m: al salir m, el hueco local ⊇ D_m
   más el espacio entre los ≤ 2 vecinos apretados de m — reducción a tríos
   {vecino, vecino, s} otra vez por el Lema U.
4. **k ocupantes por inducción** con el patrón de `cuatro.md` (cada ocupante
   extra paga su cola): objetivo T_gen^{(k)} ≥ T_gen^{(2)}.

**Riesgos conocidos:** (i) el criterio de corona no es exacto para ≥4
círculos (ocupantes interiores existen de verdad) — por eso el paso 3 es el
corazón; (ii) OJO con la dirección de las hipótesis del Lema U cuando la
"cabeza" del trío no sea el mayor (usar solo la dirección ⟹ o verificar
A ≥ mín); (iii) ρ de la instancia completa incluye colas de aros que no
están en v — formular con cuidado qué instancia realiza el bloqueo (véase
cómo lo hace la Proposición 3 / grosor_positivo §1).

## 4. BATALLA 2: u = sartén (después de la 1)

Si u (contenedor de m según F) es la sartén, (W) deja de ser una capacidad:
el testigo colocó S en la sartén junto a los ocupantes mayores. El análogo
de (W) es una condición de corona — lineal en T_c por el Lema U_k del paso 1
de la Batalla 1. Formulación en `universal.md` §3. Sin explorar.

## 5. Después de las batallas (en orden)

1. Ensamblar el **lema universal de reinserción** (ρ < T ⟹ el intercambio
   nunca se bloquea): combinatoria (ρ*_k = ρ*₃, ω_c = ω_T) para ω < ω_T +
   geometría (Batallas 1–2) para ω ≥ ω_T. Con él, la conjetura del umbral de
   Tribonacci queda a un paso (revisar el argumento completo del Teorema 2).
2. Rigor menor: cota ρ > √2 del cuadrado solo α ≥ 1 (hoja §7.5); exactitud
   de feas3 (§7.6, esquivable con direcciones constructivas).
3. **Consolidar `paper/main.tex`** con toda la cosecha (hoja §6): Teorema S
   + S6a, H1, esquina 13/7, ρ*_k, ω_c = ω_T, Lema U, S con holgura.

## 6. Protocolo y entorno (imprescindible)

- **Workflow por resultado**: explorar en scratchpad → `code/<nombre>.py`
  con bloques [A] simbólico / [B–D] numérico / verde total → borrador en
  `docs/drafts/<nombre>.md` con huecos declarados → **verificación
  adversaria** (agente independiente, protocolo 2 fases: Fase 1 rederivar
  SIN mirar los ficheros nuevos; Fase 2 auditar + ejecutar) → consolidar en
  resultados.md §9 / hoja_de_ruta / reinsercion + acta en VEREDICTOS.md →
  commit. **Las 4 verificaciones de esta racha cazaron errores reales**
  (hueco del Corolario 2, extremo de S6a, hipótesis del Lema U, α_peak):
  no saltarse el paso.
- sympy/mpmath SOLO en `python3.12` (el python3 por defecto no los tiene).
- Tiempos: esquina.py ~12 min, cuatrok.py ~15 min, universal.py ~4 min —
  lanzar en background.
- Si los subagentes fallan con 401 persistente: `/login`; con 529: backoff y
  reintentar (SendMessage al mismo agente retoma su transcripción).
- Scratchpads de esta racha (fuera del repo): explora_esquina.py,
  explora_cuatro.py, explora_universal.py, verif_esquina/, verif_cuatro/,
  verif_universal/ — los oráculos independientes de los verificadores son
  reutilizables.
