# Familia aproximante del cuadrado

Continuación autorizada mientras Fable revisa exclusivamente el bloque D.

1. Derivar la pared equilibrada G(t) y aislar su raíz t0.
2. Perturbar a=1+t+2η, b=t+η, c=t−η, w=1−t+2η.
3. Probar por continuidad todas las paredes geométricas y escribir
   explícitamente las exclusiones escalares y el valor rho=2t.
4. Certificar ejemplos racionales próximos a 2t0, con controles negativos.
5. Comprobar en Lean las identidades de G y de su polinomio normado.
   La continuidad y la interpretación euclidiana permanecen por escrito.
6. Registrar la cota, su alcance y el hecho de que este bloque nuevo
   no está incluido en el envío autorizado a Fable.

Resultado: los seis pasos están realizados. La prueba establece la cota
Y por continuidad, sin afirmar optimalidad; tres ejemplos pasan 39/39
paredes racionales. Tres tests nuevos pasan (incluido control por debajo
de la pared); las tres identidades Lean compilan y la librería completa
compila en ocho trabajos, solo con axiomas estándar en los resultados
inspeccionados. El módulo nuevo y el script están en los runners.
