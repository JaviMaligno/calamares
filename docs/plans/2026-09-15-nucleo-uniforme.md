# Núcleo estructural del intercambio uniforme

**Goal:** demostrar criterios de recolocación independientes del número de
aros y determinar si acotan de forma universal el bosque de mayores de
un intercambio bloqueado. No afirmar tau=phi sin cerrar el residuo.

**Architecture:** usar U≤m para dividir la cola en el primer menor y el
resto. Dos discos vacantes de radio m en cualquier contenedor bastan.
Obtenerlos por una cota de área de los discos prohibidos para centros;
combinar el corte de radios con crecimiento de colas y anchura común
para acotar ramificación y cadenas del bosque residual.

**Tech Stack:** pruebas geométricas y combinatorias escritas, Lean 4.32.2
core para las desigualdades, aritmética racional exacta como control.

**Risks:** olvidar los ocupantes mayores al recomponer contenedores;
sumar áreas dentro de un disco sin restar el margen de pared; contar
ramificaciones sin incluir la raíz virtual; convertir una cota del
prefijo mayor en una cota de todos los aros; confundir un núcleo finito
de parámetros con el cierre de su factibilidad continua.

## Pasos

1. Crear `lean/Calamares/Reservoir.lean`: margen de dos discos libres
   con b≥9m y presión relajada 5/3; seis radios bajo ese corte imposibles;
   cadena unaria de seis nodos imposible si no deja holgura 2m.
2. Crear `docs/drafts/nucleo_uniforme.md` con el criterio de centros
   libres, su uso en cualquier contenedor y las cotas estructurales.
3. Compilar directamente, añadir a `lean/Calamares.lean` y ejecutar
   `lake build`. Esperado: todos los términos comprobados, sin admisiones.
4. Buscar si el residuo queda cerrado o exhibir exactamente lo que
   aún falta. Registrar fuentes consultadas, alcance formal y hashes.
   Conservar PDF, fuentes y bundle de la v2 de referencia.

## Resultado de investigación

Se han escrito los criterios de dos plazas y la reducción a dos
ramificaciones, seis hojas y 40 aros mayores; la cola sigue sin cota
de longitud. También se ha obtenido una construcción para grados
arbitrarios cuando C≤beta(a,b), mediante dos plazas de radio b/2 en
el semiplano opuesto. Los siete certificados compilan directamente.

El intercambio no queda cerrado en el dominio restante: cada
ramificación debe satisfacer 2m<b<9m y C>beta(a,b), además de las
restricciones del árbol y de los testigos F/P. No se ha encontrado
una obstrucción geométrica ni una prueba de tau=phi. La cota de 40
afecta solo al prefijo mayor; no autoriza enumerar inventarios hasta
ese tamaño como prueba de cierre. La validación final se registra
en `docs/reviews/2026-09-15-nucleo-validation.md`.
