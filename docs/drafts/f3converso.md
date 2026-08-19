# El converso «gap ⟹ celda» del F3 (f3converso)

Estado: v2 (2026-08-19), ADVERSARIADO EN DOS RONDAS (actas en
VEREDICTOS.md). Ronda 1: REFUTADO — dos fatales: el detector
(ii) era VACUO para n ≥ 4 (consumía `arcos(n) = (inicio,
longitud)` como extremos de par: el barrido era infalsable) y el
teorema v1 tenía 4 contraejemplos reales (su (i) solo miraba
pares con t₁); el referee derivó la vía de rescate completa.
Ronda 2 (re-ronda del ciclo reparado): CONFIRMADO CON
CORRECCIONES — las 11 reparaciones verificadas, los 4
contraejemplos caen en la celda v2, y una grieta nueva quirúrgica
(H1: el gate de A3b era tautológico, `lp_ok = cajas_ok`; el
reclamo era verdadero y el gate quedó sustituido por el
contraste real contra primal_factible, 0 discrepancias en > 800
tríos realizados). Script: `code/f3converso.py` (5/5).

## 1. El problema

Tras f3vacio: la celda realista del gap de dualidad es VACUA bajo
ρ ≤ φ; el CONVERSO «gap ⟹ celda» quedó abierto con la frontera
0.9 solo empírica. Este ciclo lo cierra con una celda EXACTA.

## 2. EL TEOREMA (converso del gap, v2)

Sea F una familia mural (k ≤ 6), R* = R_arclp(F) (arc-LP exacto,
adversariado) y R_lb = R_lb_pack(F) (suma cíclica +
confinamiento, adversariado). Si R_lb < R* (GAP), el núcleo
N = pelar(F) cumple una de:

  (i′)  N contiene ALGÚN par apilable en R*: ∃ u ≥ t en N con
        R* ≥ u + 2t (γ_min del par = 0: el chico se esconde);
  (ii′) |N| ≥ 4 y una pareja NO-adyacente DOMINA en
        R_mid ∈ (R_lb, R*) sobre el orden de suma cíclica
        mínima: θ_par > min(arcos complementarios).

**Contrapositiva por tres lemas:**

- **G1 (PELADO EXACTO, teorema).** t ≤ p_∞(par mínimo del
  resto) = ab/(√a+√b)² ⟹ R_req(F) = R_req(F∖{t}). (≥)
  contención; (≤): monotonías GLOBALES simbólicas del bolsillo
  (A1, formas cerradas con residuo 0: dkp/dR > 0 y dkp/da < 0 en
  todo el dominio mural ⟹ ∂p/∂a, ∂p/∂b > 0, **∂p/∂R < 0** — la
  cota uniforme es el límite recto p_∞); el hueco crece con la
  separación (A2, denso extendido a a/R ≤ 0.75 y factores desde
  1.02, ~1500 casos, 0 violaciones); el bolsillo es MURAL
  (Descartes con kw = −1/R); la disjunción con NO-vecinos no es
  gratis (la desigualdad triangular de θ es falsa — arcolp H4)
  pero sale de t ≤ a_min: Δ(t,c) ≥ Δ(vecino,c) ≥ θ(vecino,c) ≥
  θ(t,c) por monotonía; la recursión multi-grano re-evalúa el
  par mínimo en cada paso (nunca dos granos al mismo bolsillo).
- **G2 (TRES SIN GAP, TEOREMA por cajas — A3b).** Para n = 3 el
  arc-LP se reduce a cajas: factible ⟺ Σθ ≤ 2π = la condición
  cíclica; con γ_min = θ_w para no-apilables (esquinas de
  gamma_min, cualquier dmin) y la pinza R_lb ≤ R_real ≤ R_arclp:
  igualdad EXACTA. Firma numérica: 196 tríos, ≤ 5.7e-12. El
  caso |N| = 2 es trivial (ambos lados = suelo del par).
- **G3 (re-anclado, teorema — derivación del acta).** Sin pares
  apilables, γ_min = θ_w exacto; en R_mid ∈ (R_lb, R*) el
  certificado pasa (∃ orden o con Σθ ≤ 2π) y el arc-LP falla en
  TODO orden; si toda pareja no-adyacente cumpliera θ_par ≤
  min(arcos complementarios en o), el sistema serían cajas
  d_i ≥ θ_i con Σ = 2π: factible — contradicción. Luego gap sin
  apilables ⟹ (ii′).

Complemento de (i′) ∨ (ii′) = {sin pares apilables} = G2 (núcleo
≤ 3) + G3 (≥ 4 sin dominación): sin gap. El confinamiento NUNCA
crea gap (solo sube R_lb — esquinas de gamma_min, verificado por
el acta): la dicotomía es exhaustiva.

## 3. Verificación

[A] A1 global simbólica; A2 denso extendido; A3 (196 tríos,
5.7e-12) + A3b (G2 por cajas, 4000 sistemas); A4 enunciados
completos. [B] pelado masivo con 1-3 granos (acta R8): 400/400,
discrepancia 0 (= solape de los intervalos de bisección, acta
R10). [C] el barrido: **4.000 familias, 1.266 gaps, TODOS en la
celda (i′) ∨ (ii′), 0 fuera** — anatomía: **1.266/1.266 por
(i′) apilabilidad**; la rama (ii′) NO se ejercita en la muestra
(predicción del teorema sin contraejemplo ni ejemplo: declarado;
el re-barrido del referee tampoco la vio en 147 gaps). [D] el
primer gap del stream real de C (F = [1.847, 1.738, 1.635,
1.152, 0.975], gap 8.9e-2, vía (i′)); el negativo que habría
cazado el bug vacuo (detector a radio holgado → False); trío no
apilable gap 0; pelado respeta núcleos; detector con n = 3 →
False. Banda de gaps (1e-9, 2e-6] no barrida: declarada.

## 4. Estatus

**EL CONVERSO QUEDA EN FORMA EXACTA v2**: gap ⟹ (i′) ∨ (ii′) —
la celda exacta que sustituye al 0.9 empírico. Etiquetas: G1
teorema (A1 simbólica global + A2 geométrico denso); G2 teorema
(cajas); G3 teorema re-anclado; el barrido muestreo de respaldo
(0 excepciones). ANATOMÍA REAL del gap: la vía dominante es la
APILABILIDAD de un grano no pelable — la narrativa v1 («la
pareja lejana») estaba invertida; la celda realista del F3 (≥ 3
tops ~0.9 con granos) es un caso de (i′) y ya es vacua bajo
ρ ≤ φ (f3vacio). El fenómeno del gap queda cartografiado: pelar
lo pelable, y el gap solo respira donde un grano apilable no
cabe en bolsillo o (predicción no ejercitada) donde la pareja
lejana domina.
