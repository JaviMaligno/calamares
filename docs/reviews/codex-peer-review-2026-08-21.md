# Informe de revisión

He evaluado exclusivamente el contenido matemático, expositivo y computacional; la extensión del manuscrito no interviene en mi recomendación.

## (a) Resumen del trabajo

El artículo estudia el empaquetamiento de anillos de anchura común en un disco, permitiendo anidamiento recursivo. Distingue dos objetivos —número de anillos y área de contacto— y dos nociones algorítmicas: un voraz de selección, que consulta la factibilidad del conjunto, y voraces de colocación, que insertan cada anillo en algún contenedor disponible. El primer bloque principal demuestra que, para radios supercrecientes, el conjunto lexicográficamente máximo optimiza toda función positiva, estrictamente creciente y superaditiva; además, cualquier regla de elección de contenedor produce ese mismo conjunto. El argumento de intercambio mediante la bola liberada es simple, general y válido para contenedores arbitrarios y cualquier dimensión.

El artículo demuestra después que la irrelevancia de la colocación es incondicional hasta tres anillos y falla con cuatro, incluyendo dos instancias gemelas que imposibilitan toda regla basada únicamente en el estado observable. Introduce el parámetro de colas \(\rho\), prueba que el modelo aditivo tiene umbral universal \(1\), obtiene el suelo Tribonacci exacto para una familia rígida de cuatro anillos y construye una familia áurea que falla con \(\rho\to\varphi\), refutando que el umbral geométrico global sea Tribonacci. Se conjetura que el umbral global es precisamente \(\varphi\).

Finalmente se desarrolla un programa de reinserción mediante fronteras angulares, coronas, bolsillos de Descartes, paredes de ocupantes y medias metálicas. Parte de este programa consta de argumentos escritos exactos; otra parte emplea barridos, optimización numérica, subdivisión y certificados computacionales. El propio apéndice inventaría varios residuos todavía muestreados o limitados a cajas declaradas.

## (b) Evaluación por criterios

### 1. Rigor matemático

Los resultados centrales iniciales son fuertes y, en lo esencial, correctos:

- La dominancia lexicográfica y el teorema de selección son argumentos estándar bien adaptados al modelo.
- El teorema de irrelevancia de la regla de colocación contiene una idea geométrica limpia: trasladar los elementos menores a la bola liberada por el mayor desacuerdo.
- Los contraejemplos de cuatro anillos y las instancias gemelas están adecuadamente respaldados por desigualdades geométricas explícitas.
- La familia aditiva, el suelo rígido Tribonacci y el contraejemplo áureo tienen pruebas autocontenidas sustanciales. Ejecuté `code/aureo.py` y `code/rigido.py`; terminaron respectivamente con 5/5 y 7/7 bloques verdes.
- La prueba completa del suelo rígido distingue correctamente la dirección constructiva del criterio angular de una equivalencia no demostrada. Esta cautela es excelente.
- La capa Lean es útil y está honestamente delimitada: encontré 45 declaraciones de teorema y ningún `sorry` real. Formaliza identidades algebraicas, no la geometría.

Sin embargo, hay dos problemas mayores. Primero, una afirmación de la sección de divergencia es falsa: tres anillos ya pueden separar los dos objetivos. Segundo, varios resultados llamados “theorem” o “written proof” dependen de máximos obtenidos por mallas o refinamiento en coma flotante que el propio manuscrito declara que no son aritmética de intervalos. Esto no constituye una prueba sobre un dominio continuo. La transparencia del autor es valiosa, pero no repara la clasificación epistemológica.

### 2. Legibilidad

El comienzo del artículo es muy bueno: las definiciones, la distinción selección/colocación y la progresión supercrecencia–cuatro anillos–umbrales forman un hilo claro. El título refleja bien las contribuciones principales. La introducción funciona como mapa hasta la entrada en el programa de reinserción.

La legibilidad se degrada en los resultados sobre contenedores genéricos y en la campaña computacional. No es un problema de extensión, sino de estructura lógica: en párrafos únicos se mezclan hipótesis, ramas, resultados exactos, resultados de subdivisión, fuzzing, historial de errores y residuos. Un lector experto no puede reconstruir con seguridad qué enunciados posteriores dependen de qué cierre numérico. Sería muy útil una tabla de dependencias con cuatro estados inequívocos: prueba escrita; certificado riguroso sobre una caja; muestreo; abierto.

El abstract da demasiado fácilmente la impresión de que toda la jerarquía de umbrales está demostrada al mismo nivel. Debería separar los teoremas principales completamente probados del programa parcial o computacional.

### 3. Reproducibilidad

Hay bastante material positivo:

- El manuscrito está asociado al tag `v1-arxiv`.
- Se citan scripts concretos y numerosos recuentos, semillas, tolerancias y techos de barrido.
- El “honest residue” distingue de manera poco habitual y encomiable los topes derivados de los topes meramente muestreados.
- Lean identifica correctamente su alcance y no pretende formalizar la geometría.

Pero la afirmación de que `python code/run_all.py` reproduce “every verification” es incorrecta. El runner contiene 18 scripts, mientras que el mapa de verificación invoca muchos otros —por ejemplo `insercion.py`, `gaplemma.py`, `r2bcert.py`, `r2bmulti.py`, `espfinal.py`, `espcanal.py` y `optimizacion.py`—. Además, `requirements.txt` no fija versiones ni versión de Python, y varios resultados dependen de NumPy/SciPy y de optimización numérica.

La distinción entre “certified maximization” y certificado riguroso es explícita, pero la terminología sigue siendo peligrosa: una malla dirigida con refinamiento no certifica un máximo continuo. Como comparación, trabajos de empaquetamiento que delegan una parte matemática automática emplean aritmética de intervalos para convertir la cobertura computacional en prueba; por ejemplo, Fekete–Keldenich–Scheffer lo declaran expresamente en su resultado de densidad crítica [Packing Disks into Disks with Optimal Worst-Case Density](https://arxiv.org/abs/1903.07908).

### 4. Novedad y significancia

Las contribuciones principales son interesantes y, hasta donde permite una búsqueda selectiva, parecen genuinamente novedosas:

- La irrelevancia de la regla de colocación bajo supercrecencia es conceptualmente atractiva y sorprendentemente general.
- La transición exacta \(n=3/4\) y las instancias gemelas son resultados limpios.
- La separación entre umbral aditivo \(1\), familia rígida Tribonacci y contraejemplo áureo es el aspecto más fuerte del trabajo.
- El programa de umbrales ofrece ideas geométricas reutilizables, incluso allí donde todavía no alcanza un cierre universal.

El trabajo sí justifica potencialmente una publicación. No obstante, la contextualización bibliográfica es demasiado estrecha para las afirmaciones generales sobre algoritmos voraces. La literatura RCPP ya incluye procedimientos GRASP y referencias a algoritmos voraces para círculos desiguales [Recursive circle packing problems](https://onlinelibrary.wiley.com/doi/10.1111/itor.12107), y existen algoritmos voraces específicos para círculos en contenedores circulares [Greedy heuristic algorithm for packing equal circles into a circular container](https://doi.org/10.1016/j.cie.2018.03.030). Estos trabajos no parecen anticipar el teorema estructural del manuscrito, pero deben discutirse para precisar la novedad: aquí no se propone otra heurística, sino una garantía de independencia respecto de la regla de colocación.

## (c) Puntos concretos

### Puntos mayores

1. **La afirmación “cuatro anillos; tres nunca divergen” es falsa.**  
   Localización: [main.tex, sección 9](C:/Users/Usuario/Github/calamares/paper/main.tex:1030), especialmente líneas 1035–1040.

   Considérese
   \[
   R=10,\qquad w=4.5,\qquad r=\{8,5.05,4.95\}.
   \]
   Los dos pequeños caben exactamente en el disco porque \(5.05+4.95=10\), pero ninguno cabe junto al de radio \(8\), ni en su agujero de capacidad \(3.5\), ni uno dentro del otro. Sus áreas son
   \[
   a(8)=51.75\pi,\qquad a(5.05)+a(4.95)=49.5\pi.
   \]
   Por tanto, el óptimo de área es el anillo de radio \(8\), con cardinalidad \(1\), y el óptimo de cardinalidad es el par pequeño, con cardinalidad \(2\). Esto afecta a la minimalidad anunciada y obliga a rehacer el correspondiente diagrama de fases o a añadir una hipótesis que excluya este ejemplo.

2. **Una malla más refinamiento no prueba un máximo sobre un dominio continuo.**  
   Localizaciones principales: [Theorem DPr](C:/Users/Usuario/Github/calamares/paper/main.tex:3099), [definición de “certified maximization”](C:/Users/Usuario/Github/calamares/paper/main.tex:3146) y [Theorem D1written](C:/Users/Usuario/Github/calamares/paper/main.tex:3293).

   El manuscrito reconoce en líneas 3157–3161 que “certified maximization” no usa aritmética de intervalos. `rstar.py` confirma que se emplean `linspace`, mallas logarítmicas y máximos observados. En consecuencia, las partes (ii)–(iv) de DPr y los teoremas posteriores que heredan ese estándar no están demostrados como enunciados universales.

   Debe hacerse una de estas dos cosas:

   - proporcionar cotas de intervalo/racionales, con cobertura verificable de las cajas y control explícito del redondeo; o
   - reclasificar esos enunciados como resultados computacionales o conjeturales sobre los dominios barridos.

3. **La clasificación epistemológica es internamente inconsistente.**  
   Localizaciones: [Agradecimientos](C:/Users/Usuario/Github/calamares/paper/main.tex:1259), [campaña computacional](C:/Users/Usuario/Github/calamares/paper/main.tex:3146), [nestedwritten](C:/Users/Usuario/Github/calamares/paper/main.tex:3327) y [gapwritten](C:/Users/Usuario/Github/calamares/paper/main.tex:3371).

   El texto afirma que “theorem” significa prueba escrita, pero varios de esos teoremas contienen sólo un “proof sketch” y una “certified maximization” no rigurosa. Frases como “verified the reduction as a theorem by 20,000-instance fuzz” son especialmente problemáticas: el fuzzing puede descubrir errores, pero no demostrar el enunciado.

4. **Las consecuencias de esos cierres computacionales deben auditarse aguas abajo.**  
   El abstract, Conjecture 12, la sección “Status”, Open Problem 14 y las afirmaciones de que “the entire nested template” tiene pruebas escritas dependen de resultados que todavía llevan el asterisco de optimización. Se necesita un grafo de dependencias y una revisión sistemática de verbos: “prove”, “certify”, “sample”, “support” y “conjecture” no deben intercambiarse.

5. **El comando único de reproducción no reproduce el mapa anunciado.**  
   Localizaciones: [nota del autor](C:/Users/Usuario/Github/calamares/paper/main.tex:24), [mapa de verificación](C:/Users/Usuario/Github/calamares/paper/main.tex:1272) y `code/run_all.py`.

   `run_all.py` contiene 18 scripts y omite buena parte de la campaña citada. Debe existir un manifiesto ejecutable que incluya todos los scripts que respaldan afirmaciones del manuscrito, con perfiles `quick/full`, parámetros, semillas, techos de cajas, tiempos esperados y recuentos esperados. Los números procedentes sólo de informes adversariales también deberían tener un comando reproducible.

6. **La sección del diagrama de fases necesita enunciados y pruebas, no sólo una descripción y una figura.**  
   Además de corregir el punto 1, deben definirse formalmente las regiones del diagrama, dar las desigualdades que determinan cada escalón, precisar qué umbrales de círculos iguales están demostrados y enlazar los scripts que generan la figura. Actualmente no es posible reconstruir el diagrama desde el artículo.

7. **Los teoremas DP y de la línea áurea contienen ramas demasiado comprimidas para verificar exhaustividad.**  
   Localizaciones: [Theorem DGp](C:/Users/Usuario/Github/calamares/paper/main.tex:2579) y [Theorem DP](C:/Users/Usuario/Github/calamares/paper/main.tex:2860).

   En particular, las isolaciones univariantes, el parche “certified on a grid”, la transición entre órdenes \(\alpha,o_1\) y el árbol \(j=3\) necesitan lemas formales que declaren dominios y cobertura. No basta remitir al historial de rondas adversariales.

### Puntos menores

8. **Error de notación en la propiedad de clausura descendente.**  
   En [línea 211](C:/Users/Usuario/Github/calamares/paper/main.tex:208) aparece \(r-\omega\), aunque en esa sección la anchura se denomina \(w\).

9. **“Exact curve” es una denominación demasiado fuerte.**  
   [Proposition Ccurve](C:/Users/Usuario/Github/calamares/paper/main.tex:2077) demuestra explícitamente una cota inferior y reconoce que dos ramas no tienen cota superior incondicional. El título y el resumen deberían decir “proved lower-bound curve”, salvo en las ramas donde se acredita igualdad.

10. **El criterio \(k=5\) de la corona requiere mejor respaldo.**  
    En [líneas 2381–2390](C:/Users/Usuario/Github/calamares/paper/main.tex:2381) se afirma que basta añadir exactamente el pentagrama tras enumerar 84 ciclos, pero no se proporciona la enumeración como lema/proposición verificable. Aunque no se use en las cotas principales, debe demostrarse o etiquetarse como comprobación computacional.

11. **Documentación Lean desincronizada.**  
    El manuscrito dice correctamente 45 teoremas, pero `lean/README.md` ofrece una tabla numerada sólo hasta 32, y el README raíz todavía habla de 22. Deben sincronizarse y explicar qué enunciado geométrico usa cada identidad formalizada.

12. **Entorno computacional insuficientemente congelado.**  
    `requirements.txt` sólo enumera paquetes. Deben añadirse versiones de Python, NumPy, SciPy, SymPy y Matplotlib, además de plataforma y, si interviene un solver, versión y tolerancias. Para certificados rigurosos no debe confiarse únicamente en comparaciones `float`.

13. **La revisión bibliográfica debería distinguir garantías de heurísticas.**  
    Recomiendo ampliar la introducción con algoritmos voraces y constructivos para empaquetamiento circular, explicando por qué no implican irrelevancia de la regla ni optimalidad estructural. La novedad parece plausible, pero actualmente se sostiene más por ausencia declarada que por una comparación documentada.

14. **Abstract y mapa de resultados.**  
    El abstract es fiel a la familia áurea, al suelo Tribonacci y a la conjetura global, pero no al grado de cierre del programa genérico. Recomiendo añadir una frase explícita que separe los teoremas completos de las coberturas por subdivisión y de los residuos muestreados.

15. **Codificación de la reducción de complejidad.**  
    En Proposition 13 convendría especificar cómo se representa el umbral que contiene \(\pi\), o dividir la desigualdad por \(\pi\) y formular la instancia con datos racionales. Esto haría completamente formal la reducción de NP-dificultad débil.

## (d) Recomendación editorial

**Revisiones mayores.**

No recomiendo rechazo porque el núcleo del artículo contiene resultados originales, elegantes y potencialmente publicables: el teorema de irrelevancia de colocación, la transición a cuatro anillos, las instancias gemelas, el umbral aditivo, el suelo rígido Tribonacci y el contraejemplo áureo constituyen una contribución significativa.

La revisión mayor es necesaria por dos razones objetivas: existe al menos una afirmación matemática falsa en la sección de divergencia, y varias afirmaciones presentadas como teoremas universales dependen de optimizaciones por malla que no son certificados rigurosos. Antes de la publicación deben corregirse el diagrama de fases, la jerarquía epistemológica y la infraestructura de reproducción. Una vez realizadas esas correcciones —incluso si parte del programa genérico se reclasifica honestamente como evidencia computacional— el trabajo merecería una nueva evaluación favorable.


