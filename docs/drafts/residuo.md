# El residuo honesto del programa (inventario transversal)

Estado: v2 (2026-08-18), ADVERSARIADO (acta en VEREDICTOS.md:
CONFIRMADO CON CORRECCIONES — ningún hallazgo bloqueante; nueve
hallazgos aplicados, incluido un paréntesis huérfano preexistente
en la crónica del paper). Documento de inventario, no de
resultados nuevos: clasifica TODO lo que queda vivo tras los cierres de la
campaña (hasta espfinal, commit 38bc392) y fija el criterio de
etiquetado. Fuente de cada ítem: su draft y su acta en
VEREDICTOS.md. El pasaje del paper (final de app:campaign) queda
reescrito en consecuencia: crónica separada del residuo.

## 0. Etiquetas

- **teorema**: demostración escrita en el paper.
- **exacto**: identidad en ℚ(√5) (a menudo también en Lean).
- **vacuo**: la celda no tiene instancia legal (demostrado, no
  muestreado).
- **certificado**: cerrado por subdivisión B&B con podas exactas
  sobre su caja declarada (computacional, reproducible, verifmap).
- **model-conditional (MC)**: depende de una tarifa/regla no
  derivada del modelo; se declara siempre.
- **tope de barrido**: techo de muestreo de una caja, no pared
  derivada.
- **abierto**: declarado abierto, con la evidencia disponible
  anotada.

## 1. Lo VIVO (el residuo real)

1. **Dirección j de los cierres de escala** — los certificados de
   escala barren j ≤ 9 (pan) y j ≤ 8 (nested) con dualidad
   tangente uniforme y el crecimiento geométrico exacto
   T_{k−1} ≥ φ·T_k. Las direcciones de perfil y polvo están
   cerradas EXACTAS (lema del bolsillo-φ, script escala); los
   recuentos de ocupantes de los teoremas escritos, cerrados por
   el lema de la cola geométrica. Vivo: solo el paso numérico en j
   más allá del barrido. [certificado + tope de barrido en j]

2. **Topes de barrido de las cajas certificadas** — cada
   certificado es RIGUROSO sobre su caja (no «exacto»: en el
   vocabulario del paper exacto = identidad en ℚ(√5) o LP
   totalmente unimodular); los techos de las cajas no son paredes
   derivadas:
   - ω ≤ 1.6 en toda la rama especular (ω no es polvo: la pared
     del polvo total no lo acota);
   - X_Y ≤ 3 en las cajas de coronas del motor (r2bmulti);
   - las extras coronas valen en sus rangos barridos.
   Nota: los viejos topes X_α ≤ 1.5, X_z ≤ 1 YA NO son residuo —
   la pared del polvo total (ΣS+X_m+X_α+X_z+ΣX_Y ≤ φ) los
   sustituye por paredes derivadas (espfinal). [tope de barrido]

3. **El canal ocupante ≥ r_m** — un ocupante de talla ≥ r_m dentro
   de un contenedor: la tarifa de re-empaque no está derivada del
   modelo. Todos los cierres de la celda especular son DENTRO del
   convenio (cada PIEZA extra es polvo de talla < r_m; las MASAS
   las acota la cola global ≤ φ, no r_m). Es el único épsilon
   MC que queda en la especular. [model-conditional]

4. **F3 (near-equal tops)** — la celda realista es VACUA (trío
   prohibido + sub-bolsillo forzado; residuo 1.0116 RETIRADO).
   Queda vivo:
   - los enunciados abstractos del arc-LP (lema de dualidad
     condicional; esquina sintética 1.082 sobre el dominio
     non-stackable) — válidos pero ya no anclados a instancia
     legal alguna; [teorema condicional + certificado]
   - la frontera de celda 0.9 (empírica) y el converso
     «gap ⟹ celda». [abierto; evidencia a favor: fuera de la
     celda el confinamiento sube R_lb justo donde t₃ excede el
     bolsillo]

5. **Asterisco de optimización** — para los shadow budgets está
   CERRADO (sup G ≤ 5.25 certificado, margen 0.98 rad); vive solo
   para los demás barridos bounded-family, si los hubiera con
   presupuesto no monótono. [abierto / tope; el «certificado» es
   solo la parte cerrada]

6. **Carácter computacional** — todos los «certificado» anteriores
   son computacionales (no written-proof); descansan en el
   verifmap y sus actas. La conversión a prueba escrita es
   dirección declarada, no deuda oculta. [meta]

7. **Global del programa** — el teorema de ensamblaje sigue siendo
   condicional a los cierres de celda; con las celdas cerradas
   computacionalmente, la condición se descarga en los ítems 1-5
   de esta lista. τ = φ queda con este residuo y ninguno más.

## 2. Lo CERRADO (para contraste, una línea cada uno)

- Celda especular COMPLETA dentro del convenio: ligera
  (r2bmulti + espkp) y pesada (areduccion + esppesada + espfinal),
  todas las X de polvo libres. [certificado]
- Variedad espxy (sliver x ∈ (p,1)): vacua por cola global +
  rigidez del suelo. [vacuo]
- F3 realista: vacua (0/30 legales; ~11.000 muestras sin gap).
  [vacuo; los dos lemas son teorema, la frontera de celda 0.9 es
  empírica — ver ítem 4 de §1]
- Lema de reducción 1/(4φ) con dicotomía β* = (9−√5)/8. [teorema,
  exacto]
- Trío prohibido (2·(φ/2) = φ) y sub-bolsillo forzado (cúbica
  áurea, r* = 0.963749). [teorema, exacto, Lean 42]
- Trío de raíz compartida: certificado en directa entera y corte
  X = 0 de la especular; pared de masa ΣS ≤ φ NECESARIA.
  [certificado]
- Shadow budgets: sup G ≤ 5.25. [certificado]
- Perfil y polvo de la ley de escala: bolsillo-φ. [teorema]
- 42 identidades exactas en Lean (kernel, sin axiomas extra).
  [exacto]

## 3. Consecuencia editorial

El párrafo-residuo del paper (que había crecido a ~210 líneas de
crónica) queda partido en dos: «The multipiece campaign and the
vacuity closures» (crónica, verbatim en lo esencial) y «The honest
residue» (los ítems 1-5 en cinco entradas). Nada se pierde: el
detalle técnico vive en la crónica y en el verifmap.
