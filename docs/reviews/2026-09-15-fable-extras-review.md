# Revisión independiente: cinco aros y agujeros independientes

Modelo: `claude-fable-5-1`. Revisión externa estática mediante Claude Code: no ejecutó Python ni Lean. Alcance y hashes en el manifiesto y metadata `2026-09-15-fable-extras`. El dictamen se conserva íntegro.

---

Voy a revisar estáticamente las dos notas, verificando a mano el álgebra, la geometría y la exhaustividad de casos, sin ejecutar Python ni Lean.

## Veredictos

| Enunciado | Veredicto |
|---|---|
| F5, cota inferior (todo fallo con N≤5 tiene rho>phi) | Aceptar |
| F5, cota superior en d≥3 y familia exactly-five | Revisión menor |
| V1 (rho≤1, K compacto, cualquier dimensión) | Aceptar |
| Captura de cola | Aceptar |
| V2 (constante min(1,kappa^-2-1), umbral 1/sqrt(2)) | Aceptar |

No he encontrado ningún contraejemplo de bosque a ninguna reasignación, ni ningún error de signo o de presión. Los hallazgos de revisión menor son justificaciones ausentes de afirmaciones verdaderas, no errores.

## Nota 1: cinco_aros.md

**Verificación de la geometría (§1, líneas 33-41).** Con centros `(-b,0)` y `(a,0)` en la bola de radio `a+b`, y `D=a²+ab+b²`, las tres identidades se cumplen exactamente. Usando `a+b-beta=(a+b)(a²+b²)/D`:

```
x²+y²      = (a+b)²[(a²-b²)² + 4a²b²]/D² = (a+b)²(a²+b²)²/D²   = (a+b-beta)²
(x+b)²+y²  = a²[(a+2b)²a² + 4b²(a+b)²]/D² = a²(a²+2ab+2b²)²/D² = (a+beta)²
(x-a)²+y²  simétrica bajo a<->b                                = (b+beta)²
```

El signo de x es correcto: para `a>b` el bolsillo se desplaza hacia la bola menor, situada en `(a,0)`. La distancia entre bolsillos es `4beta>2beta`. La construcción es plana y se embebe en cualquier `d≥2` y en cualquier bola mayor por traslación.

**P1 (líneas 45-54).** Correcto. Con `m=1`, `q>g(a)` fuerza `p>g(a)`, y las dos presiones `rho>2g`, `rho·a>1+2g` son exactamente las hipótesis `hr1`, `hr2` de `golden_balance` en `FourRing.lean:27-32`. He seguido esa prueba por casos `phi≤a` y `a<phi`: la primera identidad da `2g≥phi`, la segunda `1+2g≥phi·a`, y ambas concluyen `phi<rho`. La hipótesis `1<a` se cumple porque `a>m`. Las presiones solo usan cotas inferiores de las colas, así que la aplicación con aros adicionales en el inventario es legítima.

**P2 (líneas 56-69).** Correcto. He expandido la factorización de la línea 65-66 con `b0=2/phi`, `b0²+2b0=4`:

```
(A-2)²(B-1) + (A-2)(B-1)(B+4) + (B-b0)(B+b0+2)
 = A²B + AB² - A² - AB - B²  = AB(A+B) - (A²+AB+B²)
```

Las presiones dan `B>b0>1` y `A>2`, luego los tres sumandos son positivos y `beta(A,B)>m`.

**Exhaustividad de casos.** Con `N≤5`, el aro omitido i es el menor del inventario restringido y el desacuerdo m está en G. El primer aro nunca desacuerda. Si m es el cuarto, solo i es menor y el intercambio de §2 nunca bloquea. Si m es el tercero, los menores son el cuarto y el quinto, y §2 muestra que el bloqueo exige `S={p,q}`, `p+q>m`, ambos hijos inmediatos de u, luego hojas y agujero de m vacío. Si m es el segundo, §3 construye un testigo nuevo sin necesitar el análisis de S. Para el tercer aro, A y B coinciden en F y P, así que B está en la raíz (4.1) o en A (4.2). En 4.1, `u∈{raíz, A, B}` queda cubierto por los dos ítems. En 4.2 las seis parejas ordenadas se reparten: `(raíz,A),(raíz,B)` fila 1; `(A,raíz),(A,B)` fila 2; `(B,A)` fila 3; `(B,raíz)` fila 4. He rehecho cada fila enumerando los contenedores de las cinco piezas antes y después, y en todas quedan colocadas con el padre de m prescrito por F.

**Por qué la inducción preserva legalidad.** Cada paso construye un testigo P' y solo requiere que coincida con F en el prefijo hasta m. Los certificados usados son de dos tipos. Los de F (`R≥A+m`, `h_A≥B+m`, `h_B≥m`) son ciertos porque el voraz colocó m junto a exactamente los mayores que F y P asignan a u. Los de P (`R≥A+m`, `h_A≥B+m`) son ciertos porque P es un testigo. Las piezas menores que se reubican van a bolas de radio estrictamente mayor (bola vacante de m, bolsillo de radio ≥q, agujero con `h≥m>p`), y la condición de anidamiento `r_hijo≤h_padre` se hereda porque la bola destino ya estaba dentro del agujero. Los agujeros viajan con sus aros por traslación, así que trasladar B con p dentro (fila 2, `v=B`) es legal. El índice del mayor desacuerdo crece estrictamente, luego el proceso termina en como máximo tres pasos y el testigo final admite i en un contenedor cuyos ocupantes coinciden con los de F.

**Hallazgo 1 (revisión menor). Línea 166-167.** Se afirma que la familia áurea da el ínfimo "en todas las dimensiones d≥2", pero el paper (`main.tex:677-696`) solo prueba el fallo del voraz en el disco. El testigo se embebe en un plano, y el bloqueo de `s_1,s_2` en la sartén depende de que el bolsillo del par diametral `{phi,1}` siga siendo `phi/2` en `d≥3`. Es cierto, pero hay que decirlo: la rigidez del par vale por desigualdad triangular en cualquier dimensión, y para una tercera bola las restricciones `|c|≤R-q`, `|c-c_phi|≥phi+q`, `|c-c_1|≥1+q` dependen de c solo a través de su proyección sobre el eje y su distancia al eje, luego el problema se reduce al plano que contiene c y el eje, donde se aplica `prop:S5` reescalada. Los demás contenedores son de una o dos bolas y no dependen de d. Reparación mínima: añadir esa frase en §5.

**Hallazgo 2 (revisión menor). Línea 169-172.** "El agujero vacío del pivote del testigo" no identifica el aro. En el testigo el único agujero vacío con capacidad conocida es el del aro 1 (radio `1-w`), y la condición `delta<1-w` es exactamente la que garantiza que quepa. Nombrarlo. La cota `rho_5≤rho_4+delta/s_2` es correcta: los divisores de las colas antiguas son `phi,1,s_1`, todos mayores que `s_2`, y la cola nueva de `s_2` vale `delta/s_2`.

**Editorial.**
- Línea 95-97: "en este último caso hay exactamente dos aros menores" es falso para N=4, donde el tercer aro solo tiene a i por debajo y nunca bloquea. Decir "cuando bloquea, N=5".
- Línea 104: `p≥q≥t` debería ser estricto, como exige el teorema.
- Línea 108: para t basta `t≤q≤beta(A,m)`; no hace falta una segunda aplicación de P1.
- §3 cubre también N=4 y da una prueba del caso "voraz anida 1 en A" de `thm:fourfloor` que solo obtiene `rho>phi`, mientras el paper obtiene `rho>T`. Conviene anotar que es más débil pero suficiente, para que un lector no vea una contradicción.

## Nota 2: grosor_variable.md

**V1 (líneas 19-34).** Correcto. La clausura hacia abajo se mantiene porque cada hijo de un aro retirado tiene radio `≤h_i<r_i` y queda dentro de la bola exterior liberada, luego dentro del agujero del nuevo padre. El intercambio traslada los hijos inmediatos menores de u con sus subárboles; su suma de radios es a lo sumo `T_m≤rho·r_m≤r_m`, y el lema de fila los aloja en la bola vacante. La igualdad `rho=1` no rompe nada. La extensión de `prop:n3` con `r_3<r_2≤h_1` sustituye correctamente a `r_1-w` en `main.tex:428`.

**Captura de cola (líneas 47-55).** Correcta. El agujero de i está vacío en el testigo del prefijo, `r_j≤T_i≤h_i` da la legalidad de anidamiento de cada j, y la clausura hacia abajo certifica cada admisión sucesiva.

**V2 (líneas 59-90).** Correcta. El primer índice diferente está en L por clausura hacia abajo de S. En la rama `h_i<T_i` la cadena es estricta en el primer paso y `T_i>0` está garantizado, pues `T_i=0` cae en la rama de captura. `B≤T_i²` usa positividad e inclusión en la cola. La conclusión `A(L)≥C+a_i>C+cB≥c(C+B)` es válida porque `0<c≤1` y `C≥0`. Para `kappa≤1/sqrt(2)` la desigualdad es estricta frente a todo `S≠L`, lo que da unicidad, incluido `kappa=1/sqrt(2)`.

**Ejemplo de dos aros (líneas 94-115).** Geometría exacta: `r_1=1` llena la sartén, `1+kappa>1` impide hermandad, `kappa>kappa-epsilon` impide anidar, `rho=kappa`. La condición `1-(kappa-epsilon)²<kappa²` equivale a `epsilon<kappa-sqrt(1-kappa²)`, positiva exactamente cuando `kappa>1/sqrt(2)`. La razón es

```
kappa^-2 - 1 + (epsilon/kappa)(2 - epsilon/kappa)  ->  kappa^-2 - 1  desde arriba
```

Grosores `1-kappa+epsilon` y `kappa`, ambos positivos. El ejemplo superincreciente con `e<1/4` da razón `4e<1` y `rho=1/(1+e)`. Todo correcto.

**Editorial.**
- Línea 41-43: `lem:lexdom` del paper supone superincrecencia estricta. Con `rho=1` el argumento sigue dando que L alcanza el máximo de `sum v(r_i)`, pero puede no ser el único maximizador. Precisar "alcanza el máximo".
- Línea 66-67: "la mejor posible" es como ínfimo; el propio argumento muestra que la razón es estrictamente mayor que `c(kappa)`, así que no se alcanza.
- Línea 59: V1 vale en R^d, y la misma prueba con potencias d-ésimas daría `c=min(1,kappa^-d-1)` y umbral `2^(-1/d)`. Es una sugerencia opcional, no un defecto.

## Alcance

He verificado `FourRing.lean` como dependencia leyendo la prueba de `golden_balance`; sus dos identidades polinómicas coinciden con las de `main.tex:793-799`. No dispongo de `FiveRing.lean` ni `VariableWidth.lean`, así que no afirmo nada sobre esos certificados. No afirmo `tau=phi` universal ni novedad bibliográfica.
