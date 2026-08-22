"""Comando unico de reproduccion: ejecuta todas las verificaciones del repo
y resume los verdes. Uso:  python code/run_all.py  (desde la raiz del repo).

Cada script imprime lineas [OK]/[FALLO] y un RESUMEN n/n; aqui se recogen los
resumenes y el codigo de salida es 0 solo si todo esta en verde. Scripts de
verificacion principales (con bloques [A] simbolico-exacto vs [B..] numerico):
rigido, h1, grosor, esquina, tresk, cuatrok, universal, cuadrado, corona,
ocupantes, bloqueadores, bolsillo, striple, aureo, batalla2, microcelda,
perfilp, rstar.
"""
import subprocess, sys, os, re, time

# Duracion aproximada: --full ~33 min (cuadrado.py ~10 min, perfilp.py
# ~6-8 min por las coronas de su bloque E, y rstar.py ~5-8 min por el
# barrido de la pared de corona, son los dominantes); --quick omite
# cuadrado.py, perfilp.py y rstar.py y corre en ~8 min.

SCRIPTS = [
    "rigido.py", "h1.py", "grosor.py", "esquina.py", "tresk.py",
    "cuatrok.py", "universal.py", "cuadrado.py", "corona.py",
    "ocupantes.py", "bloqueadores.py", "bolsillo.py", "striple.py",
    "aureo.py", "batalla2.py", "microcelda.py", "perfilp.py",
    "rstar.py",
]

# Scripts lentos que --quick omite.
SLOW = ("cuadrado.py", "perfilp.py", "rstar.py")

# --campaign: EL MANIFIESTO COMPLETO (peer review externo 2026-08-21,
# punto 5: run_all debia cubrir TODO el mapa de verificacion, no 18
# scripts).  Cada entrada es (script, [dict de env por invocacion]) —
# los scripts por bandas se invocan una vez por banda del mapa
# congelado de su draft.  Duracion total estimada: 3-6 h; los runs
# largos se benefician de ejecutar por tandas.
CAMPAIGN = [
    ("superinc.py", [{}]), ("test_oblivious.py", [{}]),
    ("umbral.py", [{}]), ("gemelas.py", [{}]),
    ("minima.py", [{}]), ("escala.py", [{}]),
    ("colageometrica.py", [{}]), ("arcolp.py", [{}]),
    ("compactacion.py", [{}]), ("insercion.py", [{}]),
    ("insercionanidada.py", [{}]), ("gaplemma.py", [{}]),
    ("ensamblaje.py", [{}]), ("puertocii.py", [{}]),
    ("coronacolas.py", [{}]), ("coronaagujero.py", [{}]),
    ("coronanidada.py", [{}]), ("optimizacion.py", [{}]),
    ("r2bcert.py", [{}]), ("r2bmulti.py", [{}]),
    ("areduccion.py", [{}]), ("espxy.py", [{}]),
    ("espvals.py", [{}]), ("auditcolas.py", [{}]),
    ("f3cierre.py", [{}]), ("f3vacio.py", [{}]),
    ("espkp.py", [{}]),
    ("esppesada.py", [{"CC_SS_LO": lo, "CC_SS_HI": hi}
                      for lo, hi in (("1.016", "1.025"),
                                     ("1.025", "1.05"),
                                     ("1.05", "1.1"),
                                     ("1.1", "1.2"),
                                     ("1.2", "1.4"),
                                     ("1.4", "1.62"))]),
    ("espfinal.py", [{"CC_SS_LO": lo, "CC_SS_HI": hi}
                     for lo, hi in (("1.016", "1.025"),
                                    ("1.025", "1.05"),
                                    ("1.05", "1.1"),
                                    ("1.1", "1.2"),
                                    ("1.2", "1.4"),
                                    ("1.4", "1.62"))]),
    ("espcanal.py", [{}]),
    ("espcanalp.py", [{"CC_SSLO": lo, "CC_SSHI": hi}
                      for lo, hi in (("1.0", "1.05"),
                                     ("1.05", "1.1"),
                                     ("1.1", "1.2"),
                                     ("1.2", "1.4"),
                                     ("1.4", "1.62"))]),
    ("f3converso.py", [{}]),
    ("rstarcert.py", [{}]), ("divergencia3.py", [{}]), ("gaplemmacert.py", [{}]), ("insercioncert.py", [{}]), ("goldencert.py", [{}]), ("espomegacola.py", [{}]), ("r2bcolas.py", [{}]),
]

def main():
    quick = "--quick" in sys.argv
    campaign = "--campaign" in sys.argv
    scripts = [x for x in SCRIPTS if not (quick and x in SLOW)]
    base = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(base)
    ok_all = True
    results = []
    tareas = [(name, {}) for name in scripts]
    if campaign:
        for name, envs in CAMPAIGN:
            for env in envs:
                tareas.append((name, env))
    for name, extra_env in tareas:
        path = os.path.join(base, name)
        if not os.path.exists(path):
            results.append((name, "AUSENTE", False))
            ok_all = False
            continue
        t0 = time.time()
        env_full = dict(os.environ, **extra_env)
        proc = subprocess.run([sys.executable, path], cwd=root,
                              capture_output=True, text=True,
                              env=env_full)
        out = proc.stdout + proc.stderr
        dt = time.time() - t0
        if extra_env:
            name = f"{name} {extra_env}"
        resumen = None
        for line in out.splitlines():
            if "RESUMEN" in line or "resumen" in line.lower():
                resumen = line.strip()
        # Solo el marcador [FALLO] de los scripts de verificacion cuenta como
        # fallo. El texto descriptivo de cuadrado.py ("FALLO de best fit",
        # "[FALLA]" en su control negativo) documenta el fenomeno estudiado
        # (fallos del greedy en el cuadrado), no checks en rojo; su senal de
        # error es el codigo de salida.
        fallos = len(re.findall(r"\[FALLO\]", out))
        # veredictos de texto de los scripts antiguos (cinturon y tirantes;
        # todos los scripts devuelven ademas codigo de salida != 0 al fallar)
        fallos += len(re.findall(r"HAY FALLOS|<-- REVISAR|=FALLO", out))
        verde = (proc.returncode == 0 and fallos == 0)
        ok_all &= verde
        results.append((name, resumen or f"exit={proc.returncode}, "
                        f"fallos={fallos}", verde))
        print(f"[{'OK' if verde else 'FALLO'}] {name} ({dt:.0f}s): "
              f"{resumen or ''}")
    print()
    verdes = sum(1 for _, _, v in results if v)
    print(f"TOTAL: {verdes}/{len(results)} scripts en verde")
    sys.exit(0 if ok_all else 1)

if __name__ == "__main__":
    main()
