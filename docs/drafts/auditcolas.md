# Auditoría de colas globales

Estado: v2 (2026-08-10), ADVERSARIADO (acta en VEREDICTOS.md:
REFUTADO el v1 — cometía el error que auditaba: cola parcial en un
reclamo de existencia; reparaciones 1-5 aplicadas y el resultado
principal INVERTIDO a más fuerte). Script: `code/auditcolas.py`
(5/5, v2).

## 1. El criterio (v2)

- **Suficiencia sobre superconjunto = SOUND**: omitir paredes solo
  agranda el dominio certificado. Sin reparación.
- **Existencia/residuo = legalidad ENTERA.** Colas inevitables
  (granularidad-independientes): las de TODA pieza ≥ m — cuentan
  las tracked menores MÁS la masa total del polvo. Bajo m: el
  pigeonhole de masa (X agregada < 1 = polvo forzoso) y el
  confinamiento (X_m ≤ 1−ω) cierran los escapes; una masa X ≥ 1
  puede ser anillo único y sale de cola(m) (banda declarada).
- **Lema del trío prohibido** (exacto): tres piezas a ≥ b ≥ c con
  b, c ≥ (φ/2)·a violan ρ ≤ φ — cola(a) ≥ b+c ≥ 2(φ/2)a = φa. El
  umbral de comparabilidad es OTRA VEZ φ/2.

## 2. El F3 real: candidato fuerte a VACUIDAD

Re-escaneo con legalidad entera (36.384 instancias válidas, 30 con
gap viejo, semilla del acta de f3cierre): **sobreviven 0/30** (peor
cola de top 2.89-3.60 vs φ; el «2/3» del v1 era artefacto de
muestra de 3 con cola parcial). Mecanismo estructural: el gap de
dualidad exige ≥ 3 tops de ratio 0.9 > φ/2 = 0.809, y el trío
prohibido los mata (cola del top mayor ≥ 1.8 > φ) — **el gap de
dualidad y ρ ≤ φ son incompatibles en el generador F3**. La misma
vacuidad de espvals, un nivel más arriba. Consecuencias: errata a
f3cierre §3-4 y al pasaje del paper («the 1.0116 residue stands»);
el supremo sintético 1.0816 queda como enunciado ABSTRACTO del
arc-LP (su esquina también viola el trío prohibido como
instancia). El cierre formal (gap ⟹ ≥ 3 tops comparables ⟹
ilegal) merece ciclo propio — declarado.

## 3. El caso índice y la clasificación

espxy/espvals: caso índice (variedad vacía, errata registrada).
Suficiencia sound: B&B de r2bcert/r2bmulti/areduccion/bolsillos/
optimizacion, barridos G de puertocii, fuzzing de actas. Restos de
existencia: residuo R2/B1b de puertocii = pre-cierre (celdas hoy
cerradas por repack/[G]; las 581 instancias no viven en el paper);
núcleo de espvals v1 muerto; esquinas representativas =
ilustrativas.

## 4. Impactos

Todo generador de legalidad de adversario futuro impone la
legalidad entera (todas las colas, con la banda de las X ≥ 1); el
criterio suficiencia-vs-existencia y el trío prohibido entran en
los criterios de rigor de la ronda final ciega. Tres actas con
errata en este hilo: espxy, espvals v1, f3cierre (parcial — su
teorema condicional y su dualidad exacta SOBREVIVEN; muere el
«residuo que permanece»).
