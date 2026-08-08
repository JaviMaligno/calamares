# El lema de dualidad/zigzag: la construcción cíclica se auto-certifica

Estado: **script 5/5 en verde** (`code/zigzag.py`, 2026-08-08),
PRE-ADVERSARIO. Cierra el asterisco de `coronacolas.md` §4: la
conversión de la evidencia MC de los seis dominios en certificados
por-instancia con soporte de teorema, con el único residuo honesto de
la ley de escala en (j, p) (§7).

## 1. Qué cambia respecto al plan de coronacolas §4

El plan original pedía probar «en zigzag, el camino más largo = suma
consecutiva» y «el zigzag realiza el mínimo». Ambas cosas son FALSAS
en general (el script las refuta: el gap del zigzag contra el mínimo
exhaustivo llega a 0.26-0.34 según el barrido, y una pieza
sub-bolsillo rompe la igualdad camino = suma). La versión correcta es
más fuerte y más simple: **la
construcción por camino más largo se auto-certifica por maximalidad**,
y el zigzag queda como heurística de arranque sin carga de prueba.

## 2. Las piezas (todas en `code/zigzag.py`)

**Z1 (convexidad, exacta).** θ(a,b) = g(u_a + u_b) con u = log f,
f(x) = x/(R−x), g(s) = 2 asin(e^{s/2}). Sympy: g' = e^{s/2}/√(1−e^s)
y (log g')' = 1/(2(1−e^s)) > 0 en s < 0: g creciente y convexa. De la
monotonía de f: θ(a,x) crece en x — el «triángulo monótono»: si
x ≥ mín(a,b), entonces θ(a,x) + θ(x,b) ≥ θ(a,b).

**Z2 (esquina mural, exacta).** Para un par NO apilable
(R < máx + 2 mín) sin confinamiento, el máximo de
h(d_a, d_b) = (d_a²+d_b²−(a+b)²)/(2 d_a d_b) sobre la caja
[0, R−a] × [0, R−b] está en la esquina mural, y ahí
h(R−a, R−b) = 1 − 2 f(a) f(b) = cos θ_w EXACTO (identidad sympy);
las esquinas con d → 0 dan h → −∞ porque R−b < a+b y R−a < a+b
(trivial desde R < máx + 2 mín). Luego **γ_min = θ_w**: la necesidad
y la construcción usan el mismo número por par. (La monotonía por
aristas de h, con un solo cambio de signo, quedó adversariada en el
acta de coronacolas.)

**DIC (dicotomía hueco/muro).** El margen
NS-2(a,s,b) := θ(a,s) + θ(s,b) − θ(a,b) es creciente en s (Z1) y se
anula EXACTAMENTE en s = p(a,b,R), el radio del bolsillo de Descartes
del par mural tangente (a,b). Prueba geométrica: el círculo de
Descartes del par y la pared es tangente a la pared y a ambos, así que
sus ángulos murales consecutivos suman el ángulo del par:
θ(a,p) + θ(p,b) = θ(a,b); la monotonía en s da el cruce único.
Verificación: 4000 puntos aleatorios con |margen| < 1e-13 en s = p.
En consecuencia: **margen ≤ 0 ⟺ s ≤ p(a,b,R) ⟺ s cabe MURAL dentro
del hueco del par sin empujarlo**.

**ESP (espina, por maximalidad — el corazón del lema).** En la
construcción cíclica por camino más largo (posiciones α_i = camino más
largo desde el origen; `ciclo_constructivo`), sea la *espina* el
camino crítico 0 → … → k−1 más el cierre. Entonces, POR MAXIMALIDAD
(sin hipótesis sobre tamaños ni orden):

  (i)  los triples consecutivos de la espina tienen margen NS-2 ≥ 0
       (si un atajo dominara, el camino directo sería más largo y el
       del medio no estaría en el camino crítico);
  (ii) toda cadena de piezas saltadas entre dos espinas a, b suma
       ≤ θ(a,b) (el camino por las paradas sería más largo que la
       arista usada): los saltados caben murales EN ORDEN dentro del
       hueco del par, y por DIC cada saltado es sub-bolsillo de su
       par;
  (iii) total = suma cíclica de la espina en su orden inducido.

  Verificado: 4000 ciclos aleatorios (k = 4..11, órdenes zigzag y
  aleatorios), 0 fallos en (i), (ii), (iii) y 0 violaciones DIC.

**V (condición de valle — la única pieza por-dominio).** Las parejas
espina-espina NO adyacentes deben ser legales en las posiciones del
camino (la separación por el arco corto es la suma de aristas de
espina, que debe ≥ θ del par; por el arco largo, 2π − d lo cubre si
total ≤ 2π y NS del otro arco). Inducción (verificada, 1489
instancias, 0 fallos): si TODOS los triples consecutivos del ciclo
tienen margen NS-2 ≥ 0, la espina es todo el ciclo y todas las
parejas son legales.
La prueba general por división en el máximo intermedio topa con el
caso «valle puro» (todos los intermedios menores que ambos extremos),
que NO se cierra en general — por eso el chequeo de TODAS las parejas
es parte de la construcción (como en el acta DPr), y V se verifica en
cada dominio: en D1, **0 fallos de valle en 4500 instancias**.

**Z5 (dualidad).** Con lo anterior:

  - *Solidez de la construcción*: si el chequeo pasa (total ≤ 2π y
    todas las parejas), la colocación es un empaquetamiento legal
    (tangencias permitidas). Teorema — no depende de barridos.
  - *Solidez de la necesidad*: R_lb (bisección sobre certificados de
    subconjuntos con γ_min, esquina de caja, confinamiento del
    gigante) es cota inferior verdadera del radio de CUALQUIER disco
    que empaquete los círculos. Adversariado en coronacolas;
    consistencia aquí: R_construct ≥ R_lb en todas las instancias
    (violación peor: 0.00e+00).
  - *Dualidad en el dominio*: en D1 (j = 3..5, p = 4..6), la
    construcción tiene éxito EN R = R_lb con exceso 0.00e+00 (4500
    instancias): las dos fronteras coinciden. La espina nunca supera
    7 miembros: el mínimo sobre sus órdenes es exhaustivo-factible y
    es el mismo objeto que certifica la necesidad (γ = θ par a par
    por Z2 donde no hay apilables).
  - *Estrechez fuera del dominio* (informativa): en instancias
    desnudas {ocupantes, m} sin confinamiento, el hueco
    (R_construct − R_lb)/R_lb llega a 7.5e-4: viene de los pares
    apilables con m, donde γ_min = 0 < θ_w y la necesidad es
    estrictamente más débil. No afecta a la implicación que carga la
    prueba (solidez + éxito en R_lb del dominio).

## 3. El enunciado que usa la cadena de coronacolas §2

**Lema (dualidad/zigzag, versión espina).** Sea F un bloqueo con
ρ ≤ φ y sea R_lb la cota de necesidad de sus ocupantes (+m, con
confinamiento del gigante). Si el chequeo constructivo cíclico (camino
más largo, todas las parejas, granos a bolsillos de Descartes como
bins de fila) tiene éxito en R_lb para el conjunto de re-empaquetado,
entonces el intercambio se desbloquea en la sartén real (R ≥ R_lb,
contención monótona + escalado de la corona). Además el éxito del
chequeo es un CERTIFICADO con soporte de teorema: maximalidad (ESP) +
DIC + validación explícita de parejas (V) + legalidad de bins
(Descartes), y no una heurística.

La instancia áurea es el punto crítico exacto del sistema: margen
NS-2(φ, s, 1) = 0 en s = φ/2 = p(φ, 1, φ+1) (discriminante de
Descartes CERO, sympy), con cambio de signo al cruzar — el
contraejemplo del paper es la tangencia crítica del modelo, y el
chequeo jamás lo certifica (controles de coronacolas).

## 4. Qué queda (el asterisco honesto)

La ley de escala en (j, p, k): los barridos cubren j ≤ 5, p ≤ 6 (y
k de espina ≤ 7 emergente, no impuesto). Para (j, p) mayores el
argumento de monotonía de coronacolas (cada ocupante extra infla o₁
vía colas más de lo que añade en arcos) sigue siendo numérico. El lema
de arriba convierte cada celda barrida de «evidencia MC» a
«certificado con soporte de teorema»; la extensión a rangos no
barridos hereda exactamente el mismo asterisco que ya declara el
paper para los cierres computacionales.

## 5. Controles

- Áureo: margen 0 exacto en s = φ/2 (sympy y numérico), signo cambia
  al cruzar; bolsillo(φ, 1, φ+1) = φ/2 exacto.
- Negativo: s = 0.3·bolsillo en el muro rompe la igualdad
  camino = suma consecutiva (la espina lo excluye y el ciclo sigue
  legal): NS-2 es necesario para la igualdad, no para la legalidad.
- Negativo: sin cascada (ocupantes casi iguales), R_lb = 2.872 >
  o₁+o₂ = 2.55: son las colas las que permiten la corona en el par.
- El zigzag NO siempre realiza el mínimo (gap hasta ~0.3): por eso
  la prueba no se apoya en él.
