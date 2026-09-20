# ¿Es ajustado el suelo de Tribonacci?

Nota conceptual, escrita a raíz de una pregunta externa recibida por correo:
«is the tribonacci floor tight, or the best your current argument gives?».
Respuesta corta: **las dos cosas, en ámbitos distintos** — es exacto en la
familia rígida, estrictamente flojo con grosor positivo, y falso como umbral
universal. Todo lo que sigue ya está probado en `paper/v2/main.tex`; esta nota
sólo lo reúne en una página.

## 1. Es ajustado en la familia rígida

`thm:rigidfloor` (`paper/v2/main.tex:559`, prueba completa en `app:rigidproof`)
y `prop:S6`:

- **≥** ρ > T estricto para toda instancia de 𝓕, con ω > 0 arbitrario y radios
  estrictos — sin la idealización r₃ → r₂, w → 0 de la versión anterior.
- **≤** familia aproximante explícita I_t = (1, t, t−δ, q_t) dentro de 𝓕, con
  ρ(I_t) → T cuando t → t\* = 1/T.

Luego ínf = T, no alcanzado: no es «lo mejor que da el argumento», son las dos
direcciones.

Y no es un artefacto de la parametrización: **la configuración rígida no se
supone, emerge**. En las coordenadas ψ(x) = √((t−x)/x) la suma p+q es
U(α)+U(β) con U(z) = t/(1+z²), cóncava en [0, τ_t] exactamente cuando
t ≤ (1+√13)/6 = 0.7676…, que cubre el rango relevante con holgura; por
concavidad el ínfimo cae en la esquina del cierre, p = t, q = b(t), con b el
bolsillo de Descartes. La cúbica no se ajusta a nada: es la condición de
compatibilidad entre las dos presiones,

    t + b(t) < p + q ≤ 1 − ω < 1   ⟺   t³ + t² + t < 1.

## 2. Es flojo, y cuantificadamente, con grosor positivo

En ω = 0 el programa de bloqueo de la plantilla canónica es **vacío**
(`docs/drafts/grosor_positivo.md` §1): T es el ínfimo del programa *relajado*,
el que usa sólo (B1) y (W). Con ω > 0, `thm:corner` (`paper/v2/main.tex:995`):

    T_can(ω) ≥ 13/7 = T + 0.017856…

uniforme en ω, con igualdad sólo en el límite de la esquina racional
(ω, α, σ₂) = (1/7, 2, 6/7), donde saturan las cuatro paredes a la vez. La curva
ni siquiera es monótona: bache de altura 1.1·10⁻⁴ en ω ≈ 0.0445, raíz de un
polinomio explícito de grado 8. El objeto natural del régimen con grosor es el
Tribonacci deformado T₍₁₊ω₎.

## 3. Escondía algo como umbral universal

La conjetura τ = T es **falsa**, y la refutó el propio flujo adversario del
proyecto (`docs/respuesta_revision.md`, desarrollo posterior al primer
dictamen). La familia áurea — sartén R = φ+1, radios {φ, 1, φ/2+2ε, φ/2+ε} —
rompe la placement obliviousness en ρ = φ+3ε < T (`thm:golden`).

El mecanismo explica *por qué* T parecía tan estructurado: la pared de capacidad
Σ S ≤ cap(u), que sube el suelo de φ a T, existe sólo cuando el contenedor del
aro pivote es un **agujero** (intercambio anidado). Cuando es la **sartén**, esa
pared no está, el suelo cae al primer peldaño de la escalera —el bolsillo de
Descartes— y aparece φ. La variable oculta era qué contenedor ocupa el pivote,
no la aritmética de la cúbica. El umbral global es τ = φ (`thm:golden-global`),
con ínfimo no alcanzado, para cualquier inventario finito en el disco, incluso
con agujeros independientes; y τ₄ = φ en contenedores esféricos de cualquier
d ≥ 2.

## 4. Lo que sigue abierto

T como suelo **universal del anidado** es conjetura. Lo probado es una jerarquía
de plantillas anidadas cuyos suelos exceden todos a T: las medias metálicas
Ψ(ω) = (1−ω)+√((1−ω)²+1) (plata 1+√2 en ω = 0, cruce en (T−1)²/2), la segunda
media metálica raíz de u² − (2−ω)u − 1 (cruce en (T−1)²), la línea áurea del
doble bolsillo y la esquina hermana 17/7. Detalle bonito: la identidad que
certifica ese cruce **es** el polinomio de Tribonacci,

    (T−1)²·T − (2T − T² + 1) = T³ − T² − T − 1.

Quedan huecos de anchura (j = 1 con ω ≥ 0.9626, etc.) y está registrado como
`op:assembly`: determinar los suelos afilados de las familias de intercambio
anidado especializadas más allá de la rígida, cuyo suelo es exactamente T.

## Resumen en una línea

T es exactamente el ínfimo de la familia rígida (probado en las dos
direcciones, con la esquina rígida derivada y no supuesta); es flojo por
13/7 − T con grosor positivo; y no es el umbral universal, que es φ, porque la
pared que lo sostiene desaparece cuando el pivote vive en la sartén.
