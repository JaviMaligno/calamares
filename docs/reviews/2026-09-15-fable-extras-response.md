# Respuesta a la revisión de Fable de los extras

Fecha: 2026-09-15. Dictamen íntegro en
[`2026-09-15-fable-extras-review.md`](2026-09-15-fable-extras-review.md).
Modelo efectivo: `claude-fable-5-1`, revisión estática sin herramientas.
El usuario autorizó explícitamente los cuatro archivos y extractos
del manifiesto; la ejecución terminó con código 0 y resultado success.

## Decisiones sobre el dictamen

Fable acepta la cota inferior de F5, V1, captura de cola y V2.
Califica como revisión menor la justificación dimensional de la cota
superior y la identificación del agujero para el quinto aro. No señala
una refutación ni un hueco en la clasificación de padres de F5.
La revisión se contrastó con las fuentes y se atendió como sigue.

1. **Bloqueo en d≥3: incorporado.** La cota superior necesita conservar
   tanto el testigo como el fallo. La nota explica ahora que el par
   diametral es rígido en cualquier dimensión y que las restricciones
   de una tercera bola dependen de su coordenada axial y distancia al
   eje. La reducción a un plano preserva todas las distancias necesarias,
   así que sigue valiendo el bolsillo phi/2. Las exclusiones restantes
   son de una o dos bolas. Esto explicita la herencia ya usada en v2.
2. **Quinto aro: incorporado.** Se identifica el aro de radio 1, cuyo
   agujero está vacío en el testigo y tiene capacidad 1-w. La condición
   `delta<min(w,1-w,s_2)` conserva grosor común, orden y factibilidad.
   La estimación de rho no cambia.
3. **Tercer aro con N=4: corregido.** La frase ahora exige N=5 cuando
   el desacuerdo en el tercero bloquea. Con N=4 hay un solo menor y
   ya se aplica el intercambio por fila.
4. **Orden y alcance: precisados.** Se escribe p>q>t y t<q≤beta,
   y se distingue la cota suficiente phi del suelo más fuerte T que
   el paper obtiene para un subcaso de grosor común con cuatro aros.
5. **Valor superaditivo: precisado.** L alcanza el máximo; no se añade
   una afirmación de unicidad para v general bajo rho=1.
6. **Constante de área: precisada.** Para kappa>1/sqrt(2) el factor es
   un ínfimo no alcanzado entre instancias con área óptima positiva.
   Para kappa≤1/sqrt(2), el factor 1 sí se alcanza y el conjunto óptimo
   es único. No se extiende la no consecución a este segundo régimen.

La sugerencia opcional de extender el área a volumen d-dimensional se
registra para una continuación; no es necesaria para validar V2 y no
se presenta aquí como revisada o formalizada.

## Verificación y límites

Los cambios pedidos son precisiones de la prueba escrita; no cambian
las fórmulas certificadas. `lake build` y los 11 tests de grosor variable,
además de las 15 comprobaciones exactas de familias, pasan. Fable no
ejecutó esas herramientas ni recibió los nuevos módulos FiveRing y
VariableWidth; no se atribuye a su revisión su verificación mecánica.

El dictamen corresponde a los hashes de entrada de
`2026-09-15-fable-extras-metadata.json`. Las correcciones aquí descritas
son posteriores: no se afirma una segunda revisión de su texto final.

Durante la revisión se obtuvo además `docs/drafts/particion_bolsillos.md`
y tres teoremas en `PocketSplit.lean`. Amplían la alineación del segundo
y tercer aro a colas finitas y reducen el caso de seis aros a un bosque
de tres mayores en raíz. **No fueron enviados ni revisados por Fable**;
la reducción de bosques es escrita y no demuestra tau_6 ni tau universal.
Estos tres certificados elevan el total de la biblioteca de 102 a 105.
