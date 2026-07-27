# Generalizaciones del problema de los calamares

Registro completo de las generalizaciones anotadas durante la investigación, con su estado y las primeras preguntas concretas de cada una. Dos de ellas resultaron ser gratuitas (los teoremas principales las cubren sin trabajo extra); el resto es programa de investigación.

## 1. Forma del contenedor y dimensión (RESUELTA GRATIS)

Los Teoremas de selección voraz y de irrelevancia de colocación bajo superincrecencia valen para **contenedor arbitrario en cualquier dimensión**: la demostración del intercambio actúa solo dentro de la bola vacante del aro movido (Lema de fila aplicado en su interior) y la factibilidad de hermanos es un oráculo de caja negra. Cubre por tanto la plancha rectangular y los tubos/cascarones esféricos en 3D — el escenario original del RCPP — sin modificación alguna. En cambio, los resultados de afilado (transición n = 4, gemelas, suelo de Tribonacci) son específicos del disco: sus análogos en cuadrado y en R³ son abiertos. Primera pregunta: ¿cuál es la constante análoga a Tribonacci para contenedor cuadrado, donde el bolsillo de Descartes se sustituye por los huecos de esquina?

## 2. Grosor variable w_i (ABIERTA, prometedora)

Con grosores por aro, un aro grande puede tener agujero pequeño, lo que destruye el "rescate por anidamiento" que con w uniforme reconcilia casi siempre las dos métricas. Efectos esperados: la franja de divergencia área/número se ensancha drásticamente (los umbrales dejan de estar acoplados a los radios); el lema de superaditividad debe reexaminarse porque a(r, w) depende de ambos; el teorema de superincrecencia sobre la selección debería sobrevivir (la dominancia lexicográfica solo usa los radios y la monotonía/superaditividad de v), pero la constante del suelo geométrico cambiará. Primeras preguntas: ¿sigue valiendo la irrelevancia de colocación superincreciente? (revisar el paso de anidamiento del intercambio: los contenedores movidos siguen siendo agujeros de aros mayores, así que sí — comprobar formalmente); ¿cómo se deforma el diagrama de fases al liberar w?

## 3. Flexibilidad de los calamares: parámetro δ (ABIERTA)

Modelo: un aro parcialmente montado sobre otro toca la sartén en todo lo que no está solapado, salvo una rampa levantada de anchura δ alrededor de cada solape. δ = 0 es la idealización totalmente flexible (contacto = anillo menos región solapada); δ > 0 penaliza cada solape con una banda muerta proporcional a su perímetro. Esto define una relajación continua donde las colocaciones parciales intercambian contacto por cardinalidad. Primeras preguntas: con δ = 0, ¿cuándo conviene solapar en el óptimo de área (conjetura: nunca, porque solapar solo resta contacto sin liberar más superficie que retirar el aro)?; con la métrica de número redefinida ("aros con contacto positivo"), ¿la relajación es total (siempre caben todos parcialmente)? ¿Y con umbral de contacto mínimo por aro?

## 4. Inventarios infinitos y casos degenerados (ABIERTA)

Ya usada tácitamente en el diagrama de fases (pequeños ilimitados). Límites interesantes: cadenas anidadas maximales r, r−w, r−2w, …; densidad asintótica de contacto alcanzable con inventario libre (¿cuál es el sup de A/πR² sobre todos los inventarios?); configuraciones límite de tipo apolonio cuando w → 0 con anidamiento prohibido por bandas. Primera pregunta concreta: con inventario libre de radios y w fijo, ¿el sup de densidad de contacto es 1 (rellenando con discos macizos r ≤ w) y cuál es la tasa de convergencia con n aros?

## 5. Métricas alternativas (PARCIALMENTE RESUELTA)

El teorema de selección cubre toda v monótona superaditiva (área de contacto, suma de radios, suma de perímetros…). Fuera de la clase: cardinalidad (v ≡ 1) falla incluso con superincrecencia (contraejemplo explícito), y cualquier v cóncava caerá igual. Frontera exacta demostrada: la superaditividad. Abierto: aproximabilidad de la cardinalidad; métricas mixtas (área sujeta a número mínimo).

## 6. Sustituto aditivo con radios enteros (ABIERTA)

El modelo aditivo (hermanos factibles sii suma ≤ capacidad) es la capa combinatoria del problema: contiene SUBSET-SUM, su umbral de irrelevancia de colocación es exactamente 1, y es candidato natural a algoritmo pseudopolinómico con radios enteros (DP sobre capacidades con estructura de bosque; obstáculo: el acoplamiento tipo multiple-knapsack entre contenedores generados por los propios objetos).

## 7. Reglas con input completo (ABIERTA, complejidad)

Las gemelas cierran las reglas función-del-estado. Para reglas que ven todos los radios por adelantado la pregunta es de complejidad: ¿se puede alcanzar el lex-máximo con un número polinómico de consultas al oráculo de empaquetamiento de hermanos? El testigo existe siempre (seguirlo es una ejecución voraz legal); encontrarlo es lo que puede ser caro.
