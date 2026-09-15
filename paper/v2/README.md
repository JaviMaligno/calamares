# Integrated v2

This directory is the current English manuscript. The parent directory's
`main.tex` and `generalizations_v2.tex` preserve the September 14 reference.

From the repository root, run:

```text
python paper/build_v2.py --verify-bundle
```

This writes `output/pdf/calamares_v2_integrada.pdf` and
`paper/arxiv-v2-integrada.tar.gz`, then compiles the archive in a fresh
temporary directory to check that it contains every required source.
It requires `pdflatex` and the LaTeX packages listed in `main.tex`.
Inside the extracted archive, compile `main.tex` until references stabilize.

The bundled PNG figures are sufficient for compilation. To regenerate them
from the repository, run `python paper/render_v2_figures.py` with Matplotlib
and NumPy installed. The historical figure assets are not changed.

The global golden proof and the dimensional and variable-area extensions
are based on the independently reviewed source proofs recorded in
`docs/reviews/`. The integrated English manuscript received a local
editorial and rendering review. Lean checks algebraic and Cartesian
certificates; the complete geometric forest argument is a written proof.
