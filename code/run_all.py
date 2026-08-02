"""Comando unico de reproduccion: ejecuta todas las verificaciones del repo
y resume los verdes. Uso:  python code/run_all.py  (desde la raiz del repo).

Cada script imprime lineas [OK]/[FALLO] y un RESUMEN n/n; aqui se recogen los
resumenes y el codigo de salida es 0 solo si todo esta en verde. Scripts de
verificacion principales (con bloques [A] simbolico-exacto vs [B..] numerico):
rigido, h1, grosor, esquina, tresk, cuatrok, universal, cuadrado, corona,
ocupantes, bloqueadores, bolsillo.
"""
import subprocess, sys, os, re, time

SCRIPTS = [
    "rigido.py", "h1.py", "grosor.py", "esquina.py", "tresk.py",
    "cuatrok.py", "universal.py", "cuadrado.py", "corona.py",
    "ocupantes.py", "bloqueadores.py", "bolsillo.py",
]

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(base)
    ok_all = True
    results = []
    for name in SCRIPTS:
        path = os.path.join(base, name)
        if not os.path.exists(path):
            results.append((name, "AUSENTE", False))
            ok_all = False
            continue
        t0 = time.time()
        proc = subprocess.run([sys.executable, path], cwd=root,
                              capture_output=True, text=True)
        out = proc.stdout + proc.stderr
        dt = time.time() - t0
        resumen = None
        for line in out.splitlines():
            if "RESUMEN" in line or "resumen" in line.lower():
                resumen = line.strip()
        fallos = len(re.findall(r"\[FALLO\]|FALLO\b", out))
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
