# Estado de la sesión (2026-07-29) — punto de retoma

Sesión interrumpida por límites de cuota. Todo lo verificado está consolidado y
pusheado; este fichero documenta lo que quedó a medias y el orden de retoma.

## Hecho y consolidado (no retocar)

- **Teorema S** (suelo rígido sin idealización): `drafts/suelo_rigido.md` + `code/rigido.py`, verificado 10/10.
- **Grosor positivo**: Φ(ω) = T₍₁₊ω₎ − ω, esquina 13/7; `drafts/grosor_positivo.md` + `code/grosor.py`, 8/8 módulo H1.
- **Perfil de 3 aros**: Proposición 4 y ρ*₃(ω) con cruce exacto ω_T = 1/T − 1/2; `drafts/perfil_tres.md` + `code/tresk.py`.
- **Cuadrado**: X = 1.7110185903, b_□(X) = X−1; `drafts/cuadrado.md` + `code/cuadrado.py`.
- Consolidación en `resultados.md` §9 y notas en `reinsercion.md` §6/§9/§10.
- Actas de verificación adversaria: `drafts/VEREDICTOS.md`.

## A MEDIAS: H1 (hueco 2 de hoja_de_ruta.md §7)

Un agente atacó H1 y **encontró el resultado central antes de morir por cuota**:

    κ = √( g(s₂) / g(s₁) ),   g(s) = s³(1−s)   — identidad CERRADA en la
    frontera de bloqueo F = 2π, INDEPENDIENTE de α.

Consecuencia: κ ≥ 1 ⟺ g(s₂) ≥ g(s₁); como s₂ ≥ b(α) en la frontera y g decrece
en [3/4, 1], basta b(α) ≥ 3/4, es decir α ≥ α₀ = (√13−1)/2 ≈ 1.30278. Para
α ≤ φ el bloqueo es imposible (cota áurea), y el programa solo usa α > φ > α₀:
**H1 quedaría demostrado en toda la región que el programa necesita.**

Estado del material:
- `code/h1.py` — ESCRITO y ejecutado: bloques A (identidades sympy), B (κ contra
  diferencias finitas), C (κ ≥ 1 en frontera), E (cobertura y casos frontera) en
  verde. El bloque D marca 2 fallos que parecen de tolerancia, no matemáticos:
  D1 "estrictamente decreciente" falla con incremento máximo +0.00e+00 (empate
  exacto, probablemente comparación ≤ vs <) y D2 con error 2·10⁻⁴ ≈ la tolerancia
  de la bisección de `h_boundary`. REVISAR ambos antes de dar H1 por cerrado.
- `docs/drafts/h1.md` — NO LLEGÓ A ESCRIBIRSE. La derivación completa (por qué
  κ = √(g(s₂)/g(s₁)); sale de F_{s₁}/F_{s₂} con la identidad sin²(θ/2) = f(a)f(b)
  del Lema S1) está solo en la cabecera de h1.py y hay que reconstruirla con
  rigor: rehacer con sympy la simplificación de F_{s₁}/F_{s₂} hasta g, y escribir
  el lema con su dominio exacto.

## Orden de retoma sugerido

1. **Cerrar H1**: reconstruir la derivación en `drafts/h1.md`, arreglar
   tolerancias del bloque D de `h1.py` (D1: usar <= con margen; D2: subir
   precisión de la bisección), re-ejecutar 5/5 y someterlo a verificación
   adversaria (rehacer κ = √(g/g) en sympy sin mirar h1.py). Si sobrevive,
   quitar los "módulo H1" de grosor_positivo.md y resultados.md §9.
2. **Compacidad de S6** (rigor menor, fruta madura).
3. **ρ*₄ = ρ*₃** (fijaría ω_c = ω_T exacto).
4. **El asalto grande**: contenedores v/u genéricos (hoja_de_ruta.md §7.1).
5. Consolidar en `paper/main.tex` cuando 1–3 estén cerrados.

Lista completa priorizada con detalles: `docs/hoja_de_ruta.md` §7.
