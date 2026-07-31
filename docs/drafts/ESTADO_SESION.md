# Estado de la sesión (2026-07-30) — punto de retoma

Sesión de cierre masivo: H1, S6a, esquina 13/7 y ρ*_k = ρ*₃, todos con
verificación adversaria completada y consolidados. **El programa queda con un
único hueco bloqueante: contenedores v/u genéricos (hoja_de_ruta §7.1).**

## Cerrado y consolidado (no retocar)

- **H1** (`drafts/h1.md` + `code/h1.py` 5/5, acta 6/6): κ = √(g(σ₂)/g(σ₁))
  para todo α > 1; frontera cerrada t(σ₁)+t(σ₂) = t(b(α)); cierre Tribonacci.
- **Lema S6a** (`drafts/suelo_rigido.md` §8, auditado en el acta de cuatro):
  cierre por compacidad de la Prop. S6; intervalo de propagación [0, δ₀)
  (¡abierto por la derecha!), δ₀ = t − u_máx el extremo óptimo.
- **Esquina 13/7** (`drafts/esquina.md` + `code/esquina.py` 5/5, acta 6/6):
  curva exacta de T_can (2(1−ω) | α_m(ω)−ω | Φ(ω)); ω₁ raíz de
  4ω³−20ω²+25ω−1; α_m séxtica P irreducible; TEOREMA: inf T_can = 13/7 sin
  módulo del criterio angular; bump: ω₁ mínimo local, ω_peak ≈ 0.04447 (R₈,
  grado 8), α_peak = 1.9618665; corregida la monotonía de grosor_positivo §4.
- **ρ*_k = ρ*₃ para todo k ≥ 3** (`drafts/cuatro.md` + `code/cuatrok.py` 5/5):
  Proposición 8 con el árbol general (p ≤ 3 sobre el agujero de s₁; p≥3
  prefijo bloqueado, p=2 caso (iv), p=1 ρ ≥ 2) — aportado por la verificación
  adversaria tras REFUTAR el cierre vía Corolario 2 (solo cubre perfiles en
  banda; ρ*_k es no creciente y no bastaba). Corolario 5: **ω_c = ω_T =
  1/T − 1/2 exacto**. El árbol k=4 original (A/B1/B2/B3) se conserva validado.
- Actas de TODO en `VEREDICTOS.md` (7 borradores). Teorema S, grosor,
  perfil_tres, cuadrado: como antes.

## El asalto (§7.1): fase 1 CERRADA, batallas 2 y 3 abiertas

- **Fase 1 hecha** (`drafts/universal.md` + `code/universal.py` 5/5, acta en
  VEREDICTOS con refutación del enunciado original REPARADA): **Lema U**
  (frontera lineal del trío en disco R arbitrario, CON la hipótesis
  A ≥ mín(x,y) — sin ella es falso, contraejemplo en el acta), bolsillo
  general b_R(A) = ARc/(AR+c²) creciente en R, κ uniforme en R con umbral
  afilado 3c² ≤ 4AR, G_c-identidad G_c = (c²/4)U′² (h1 §4 ≡ S4(3)), cota de
  existencia R < 2.1547·A, y **Teorema S con holgura** (Corolario U1) —
  cierra la extensión de hoja_de_ruta §1.
- **Batalla 1 (v con ocupantes interiores)**: formulada en universal.md §3;
  exploración a favor (3 ocupantes, proxy angular: mejor bloqueo ρ = 2.56 >>
  13/7, la cola del ocupante extra γ es la dominante en 321/321). Falta el
  «lema del hueco» (cota inferior del mayor hueco en función de la capacidad
  libre) para ocupantes interiores; para coronas de tangentes a pared el
  Lema U ya da la aditividad en T_c.
- **Batalla 2 (u = sartén)**: formulada, sin explorar. El análogo de (W) es
  una condición de corona, lineal en T_c por el Lema U.
- Rigor menor pendiente: cota ρ > √2 del cuadrado solo α ≥ 1 (hoja §7.5);
  exactitud de feas3 (§7.6, esquivable con direcciones constructivas).
- Consolidar `paper/main.tex` con todo lo nuevo (§6 de la hoja de ruta).

## Notas de entorno

- sympy solo en `python3.12`. esquina.py ~12 min; cuatrok.py ~15 min.
- Verificadores adversarios: protocolo 2 fases (rederivar sin mirar → auditar
  y ejecutar); si la API da 401 persistente, `/login`.
- Scratchpad con las exploraciones: explora_esquina.py, explora_cuatro.py,
  verif_esquina/ y verif_cuatro/ (oráculos independientes de los agentes).
