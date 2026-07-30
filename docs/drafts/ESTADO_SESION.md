# Estado de la sesión (2026-07-29, noche) — punto de retoma

Sesión con inestabilidad de API (529/401 intermitentes en subagentes). Todo el
trabajo está consolidado en ficheros y commiteado; lo ÚNICO pendiente es la
verificación adversaria de los dos borradores nuevos y su consolidación.

## Hecho y verificado (sesiones anteriores + hoy)

- **H1 CERRADO y consolidado** (commit 9e7ff2c): `drafts/h1.md` + `code/h1.py`
  5/5, acta TODO CONFIRMADO en `VEREDICTOS.md`. κ = √(g(σ₂)/g(σ₁)) para todo
  α > 1; frontera cerrada t(σ₁)+t(σ₂) = t(b(α)); cierre Tribonacci.
- **Teorema S, grosor, perfil 3, cuadrado**: como antes (actas en VEREDICTOS).

## Hecho HOY, pendiente de verificación adversaria

1. **Lema S6a** (`drafts/suelo_rigido.md` §8): formaliza el cierre por
   compacidad de la Prop. S6 (monotonía + cierre + apertura cuantificada,
   δ₀ = t − u_máx explícito). Hueco §10.1 marcado RESUELTO. Consolidado en
   resultados.md §9 y hoja_de_ruta.md §7.4. Riesgo bajo (argumento estándar).
2. **Esquina 13/7 y curva exacta del grosor** (`drafts/esquina.md` +
   `code/esquina.py`, 5/5): cierra H2 de grosor_positivo.md.
   - Curva exacta: 2(1−ω) en (0,ω₁]; α_m(ω)−ω en [ω₁,1/7]; Φ(ω) después.
   - ω₁ = raíz de 4ω³−20ω²+25ω−1 (cúbica, antes sin forma cerrada).
   - α_m: sextica P(α,ω) explícita (bigrado (6,2)).
   - TEOREMA: inf T_can = 13/7, SIN módulo feas3 (familia genuina α = 2+δ,
     ε = δ²/4, vía Prop. S5 + Lema S6a; en α = 2 exacto NO hay familia).
   - Clave: q(ω) = P(13/7+ω,ω) = 4(7ω−1)Q₅/7⁶, Q₅ sin raíces en [1/25,1/7].
   - BUMP nuevo: ω₁ es MÍNIMO local; máximo local en ω_peak ≈ 0.04447 (raíz
     de R₈, grado 8); altura +1.1e-4. Corrige el «decrece en (0,1/7]» de
     grosor_positivo §4 (era interpolación, los valores medidos eran buenos).
3. **ρ*₄ = ρ*₃** (`drafts/cuatro.md` + `code/cuatrok.py`, 4/4): Proposición 8
   (prueba puramente aditiva, árbol A/B1/B2/B3 en una página) y Corolario 5:
   **ω_c = ω_T = 1/T − 1/2 exacto**. Cierra el hueco 2 de perfil_tres §5 y
   el punto 3 de reinsercion §10 para k = 4.

## Pendiente inmediato (en orden)

1. **Verificación adversaria de esquina.md** — protocolo 2 fases (el prompt
   completo está en la transcripción; reconstruir si hace falta: Fase 1 sin
   mirar esquina.md/esquina.py, rederivar curva + P + q + R₈ + atacar; Fase 2
   auditar y ejecutar). El agente `verificador-esquina` cayó repetidamente
   por 529/401; si persiste el 401: `/login`.
2. **Verificación adversaria de cuatro.md** — mismo protocolo (Fase 1:
   rederivar el mínimo condicionado k=4 y buscar bloqueos bajo ρ*₃ con
   oráculo propio; Fase 2: auditar el árbol A/B1/B2/B3 y ejecutar cuatrok).
   Pedirle también auditar el Lema S6a (3 puntos, rápido).
3. **Consolidar si sobreviven**: retirar H2 de grosor_positivo.md §6 (y
   corregir su §4 con el bump), actualizar resultados.md §9 (grosor pasa a
   «curva exacta demostrada, ínfimo global 13/7»; perfil pasa a «ω_c = ω_T
   exacto, k=4 cerrado»), hoja_de_ruta.md §7 (huecos 2 y 3 → RESUELTOS),
   perfil_tres.md §4-§5 (Corolario 4 sin banda, hueco 2 → resuelto),
   reinsercion.md §10.3, actas en VEREDICTOS.md, y este fichero.
4. Después: **el asalto grande** (contenedores v/u genéricos, hoja_de_ruta
   §7.1) — único hueco bloqueante restante de la conjetura.

Notas de entorno: sympy solo en `python3.12`; esquina.py tarda ~12 min
(bloque C); cuatrok.py ~13 min (oráculo de bosques). Scratchpad de la
exploración: explora_esquina.py, explora_cuatro.py (P, q, R₈ ya reproducidos
ahí).
