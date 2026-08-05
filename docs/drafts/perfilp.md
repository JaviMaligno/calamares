# Perfiles |S| = p ≥ 3 en el intercambio a sartén (Teorema DP-p)

Estado: **parcial** — casos (L), (N), (H1), (H2-ΨB), (H2-espejos) probados
(pendiente de acta adversaria); franja R* declarada abierta con evidencia.
Script: `code/perfilp.py`.

Notación: S = {σ₁ ≥ … ≥ σ_p}, todas < 1; W := Σ_{i≥3} σᵢ; Σ := σ₁+σ₂+W;
M := Σ hijos(m). Paredes del par (batalla2.md §1) con las variantes p
que se justifican caso a caso.

## 0. El principio de reparto

Con p piezas, cada colocación desbloqueadora reparte S entre los
depósitos: D_m (fila, capacidad 1), agujeros de piezas del perfil
(fila, capacidad σᵢ−ω), H_m (capacidad 1−ω, exige evacuar M a D_m),
bolsillos de la sartén (espejos exactos de la Prop. S5 / Lema DG), y
anidamientos. Las paredes del caso par se heredan **cuando el resto del
perfil cabe en los depósitos que la colocación par no usa**; el árbol
de abajo organiza exactamente eso.

## 1. Casos probados

**(L) Ligero: σ₁ + W ≤ 1.** Toda colocación del par «σ_i → X, la otra
→ D_m» sigue legal mandando además W a D_m: fila σ_j + W ≤ σ₁ + W ≤ 1
para j ∈ {1,2}. Se heredan VERBATIM (D_p) [Σ > 1], (G) con σ₁ y con σ₂,
(evac_p), (Ry), (Bo), y las colas solo engordan (+W). Los casos
(i)–(iv) del Teorema DP dan ρ > φ con las mismas constantes y los
mismos dominios de ω (todo ω > 0 en (i)–(ii); ω ∈ (0,1) en (iii)–(iv),
incluida la pinza del caso (iv)). Matiz de (iii): la colocación de
evacuación con p piezas es «σ₂ → H_m vaciado, σ₁+M+W → D_m», así que la
pared es (evac_p): σ₂ > 1−ω ∨ σ₁+M+W > 1; en la rama B el programa Ψ_B
usa A = σ₁+σ₂+W+M+X = (σ₁+M+W) + (σ₂+X) > 1 + q con q := σ₂+X — la
MISMA contabilidad del par con σ₁+M+W en el papel de σ₁+M. La pared en
la hoja con σ₂ es legal en (L): «σ₂ → agujero de L′, σ₁+W → D_m» con
fila σ₁+W ≤ 1.

**(N) Anidado: W ≤ σ₁ − ω − X_{σ₁}** (X_{σ₁} := contenido previo del
agujero de σ₁; la tarifa del Lema R es junto a él). El exceso W viaja
en fila dentro del agujero de σ₁ y {σ₁ con W dentro} es UNA pieza de
radio σ₁ ≤ 1: la fila {σ₁} en D_m es legal siempre, aun con σ₁+W > 1.
Cada pieza cabe individualmente porque σᵢ ≤ W ≤ capacidad.
Como W viaja dentro de σ₁ VAYA DONDE VAYA σ₁ — a D_m en (G_σ₂), (Bo) y
la evacuación; al agujero de y en (Ry); a la sartén en (G_σ₁) — todas
las colocaciones del par quedan legales: herencia de (i)–(iv) otra vez. — (L) ∪ (N) cubre W ≤ máx(1−σ₁, σ₁−ω−X_{σ₁}), cuyo mínimo sobre σ₁
(con X_{σ₁} = 0) es (1−ω)/2 en σ₁ = (1+ω)/2.

**(H1) Pesado grande: σ₁+W > 1 y σ₂ > φ−1.** Cola de m:
ρ ≥ Σ = σ₂ + (σ₁+W) > (φ−1) + 1 = φ. Todo j, todo ω > 0.

**(H2-ΨB) Pesado con σ₁+M > 1 y una hoja estricta** (existe si j ≥ 2;
también con j = 1 si el subárbol de o₁ tiene alguna hoja ≠ y). Pared
(Bo-fila) en la hoja estricta L′: la colocación «fila {σ₂,…,σ_p} al
agujero de L′ junto a X_{L′}, σ₁ → D_m» es legal (Lema R + σ₁ ≤ 1) y su
fallo da L′ < (σ₂+W) + ω + X_{L′}. Con q̃ := σ₂+W+X_{L′} > 1−ω
(L′ ≥ 1) y A := σ₁+σ₂+W+M+X_{L′} = (σ₁+M) + q̃ > 1 + q̃ (aquí entra
σ₁+M > 1): las dos colas ρ ≥ A > 1+q̃ y ρ·L′ ≥ 1+A dan
ρ > (2+q̃)/(q̃+ω) — exactamente el programa de la rama B del par, con
q̃ en el papel de s: ρ > Ψ_B(ω) > Ψ_B(1) = φ para todo ω ∈ (0,1).

**(H2-espejos) Pesado, j = 1, p = 3, σ₂ ≤ φ−1: NO HAY BLOQUEO.** La
colocación «σ₂ → bolsillo espejo 1 de {o₁, m}, σ₃ → bolsillo espejo 2,
σ₁ → D_m» siempre funciona: los espejos tienen radio b(o₁) ≥ b(1) = 2/3
> φ−1 ≥ σ₂ ≥ σ₃, son disjuntos (y₀ = 2b₂, Lema DG), y σ₁ ≤ 1. No usa ω.
Con (H1): **p = 3, j = 1 queda cerrado para todo ω > 0** (junto con
(L)/(N) para el régimen no pesado).

**(H2-swap) Pesado, σ₁+M ≤ 1, j = 2, p = 3.** (Solo j = 2: la
no-empaquetabilidad de {O, m, σ₃} NO es hereditaria hacia el
subconjunto {o₁,o₂,m,σ₃} cuando j ≥ 3 — mismo motivo por el que el
caso (ii) del par es j = 2 y j ≥ 3 fue por la escalera.) Dicotomía del
intercambio con H_m: «σ₂ → H_m, σ₁+M → D_m (fila ≤ 1 ✓), σ₃ → bolsillo
de la sartén». Su fallo fuerza σ₂ > 1−ω **o** σ₁+M > 1 (excluido por hipótesis) **o**
{O, m, σ₃} no re-empaqueta — y esto último, por contención al disco
o₁+o₂ y S5, obliga a que m = 1 y σ₃ quepan en los dos espejos: fallo ⟹
máx(m, σ₃) = 1 > b₂, o sea b₂ < 1 directamente. Esa rama resucita la
pared de espejos del caso (ii) del par (o₂ < Ā(o₁)) y su optimización,
con colas engordadas
(1+Σ > 2+σ₂ > 2): ρ > φ como en el par. La primera rama, junto con la
simétrica en σ₃ («σ₃ → H_m, σ₂ → bolsillo»), fuerza σ₃ > 1−ω, y
entonces ρ ≥ Σ > σ₁ + 2(1−ω); con la cola 1+σ₂ > 2−ω esto cierra
ω < 2−φ. **Queda la franja** ω ≥ 2−φ con σ₂, σ₃ ∈ (1−ω, φ−1].

## 2. La región declarada abierta R*

    R* := { σ₁+W > 1,  W+X_{σ₁} > σ₁−ω,  σ₂ ≤ φ−1 } ∩
          [ { p ≥ 4, σ₁+M ≤ 1 }
          ∪ { p ≥ 4, σ₁+M > 1, j = 1, subárbol de o₁ = cadena hasta
              la hoja y (sin hoja estricta) }
          ∪ { p = 3, j = 2, σ₁+M ≤ 1, σ₂ > 1−ω, σ₃ > 1−ω }
          ∪ { p = 3, j ≥ 3, σ₁+M ≤ 1 } ]

(el tercer miembro implica ω > 2−φ; para p = 3 con j = 1 los espejos
cierran siempre; para p = 3, j = 2, con alguna σᵢ ≤ 1−ω cierra el
swap; y el
segundo miembro existe porque (H2-ΨB) necesita una hoja estricta, que
la cadena hasta y no tiene — es el pariente p ≥ 4 de la vieja
micro-celda, hoy sin pinza porque no hay o₂ que atrapar; la cuarta
celda existe porque el swap solo vale para j = 2). La partición
(L)∪(N)∪(H1)∪(H2-ΨB)∪(H2-espejos)∪(H2-swap)∪R* es exhaustiva — la
enumeración fue verificada adversariamente, que encontró y corrigió dos
celdas omitidas en la primera versión (acta en VEREDICTOS.md). Con
p ≥ 4 quedan fuera todos los j en la rama σ₁+M ≤ 1 porque el swap y los
espejos solo alojan dos piezas más allá de σ₁ (los espejos son dos, y m
compite por ellos cuando j ≥ 2). Para {p=3, j≥3, σ₁+M≤1} el programa
crudo de la escalera con σ̂ := σ₂+W roza φ sin superarlo (mín numérico
≈ 1.616 < φ): se necesita una pared más fina, no un empujón. Evidencia
dirigida (`perfilp.py` bloque E, con M > 0 muestreado): los bloqueos
ahí casi no existen — 11 configuraciones bloqueadas de 236 016
examinadas con todas las paredes y coronas impuestas, mín ρ = 3.01
(margen 1.39 sobre φ); el verificador hostil añadió un barrido propio
de la celda con σ₁+M > 1 (18 452 muestras, 0 bloqueos supervivientes).
La maquinaria
identificada para cerrarla: la pared de intercambio de coronas
(P empaqueta {O} ∪ S en R y el re-empaquetado {O, m} ∪ (S∖A) debe
fallar en el mismo R: el canje σ₁ ↔ m da una pared cuantitativa) y la
cascada de bolsillos (escalera).

## 3. Por qué no prueba de más

- El contraejemplo áureo (p = 2) no entra en ningún caso nuevo: (L)/(N)
  reproducen el teorema del par tal cual, y la familia áurea con polvo
  añadido (S = {φ/2+2ε, φ/2+ε, δ}) cae en (L) (σ₁+W = φ/2+2ε+δ ≤ 1),
  donde el suelo sigue siendo φ y la familia lo realiza: consistente.
- (H2-espejos) usa σ₂ ≤ φ−1 < 2/3 = b(1): el control negativo del
  script comprueba que con σ₂ > 2/3 y o₁ = 1 el bolsillo NO basta.
- (H2-ΨB) exige σ₁+M > 1: sin eso A > 1+q̃ falla (contabilidad
  explícita en el script) — por eso R* lleva σ₁+M ≤ 1.

## 4. Qué implica

El suelo áureo del intercambio a sartén queda probado para **perfiles
de 3 piezas con j = 1 en todo ω > 0**, y para perfiles arbitrarios en
los regímenes ligero, anidado, pesado-grande y pesado-ΨB. La Conjetura
áurea (τ = φ) sigue abierta: falta R*, los pequeños extra y el
ensamblaje. El ínfimo sobre los casos cerrados sigue siendo φ
(familia áurea, ahora también con polvo: cor:goldencover se extiende).
