"""Redraw the existing paper figures with legible English labels.

Geometry and phase classes follow code/figrefuta.py, viz.py and franja.py.
The divergence witness uses explicit centers instead of a packing solver.
Only figures in paper/v2 are written; the historical assets are preserved.
"""

import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Annulus, Circle, Patch
import numpy as np

OUT = Path(__file__).resolve().parent / 'v2/figures'
COLORS = ['#c96b30', '#287db2', '#419345', '#8753a3']
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})


def pan(ax, radius):
    ax.add_patch(Circle((0, 0), radius, fc='#f3f3f3', ec='#222222', lw=1.2))
    ax.set(xlim=(-1.06*radius, 1.06*radius), ylim=(-1.06*radius, 1.06*radius),
           aspect='equal')
    ax.axis('off')


def ring(ax, center, radius, width, index, label):
    ax.add_patch(Annulus(center, radius, width, fc=COLORS[index], ec='#333333', lw=.5))
    ax.text(*center, label, ha='center', va='center', fontsize=11)


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / name, dpi=240, bbox_inches='tight', pad_inches=.08)
    plt.close(fig)


def counterexample():
    fig, axes = plt.subplots(1, 2, figsize=(7, 3.7), layout='constrained')
    for ax in axes:
        pan(ax, 15)
    left, right = axes
    ring(left, (-5, 0), 10, .3, 0, '')
    left.text(-5, 7, '10', ha='center')
    ring(left, (-5, 0), 5, .3, 1, '5')
    ring(left, (10.1, 0), 4.9, .3, 2, '4.9')
    left.set_title('Best fit: 3 rings\n4.8 cannot be inserted', fontsize=12, pad=9)
    ring(right, (-5, 0), 10, .3, 0, '')
    right.text(-5, 7, '10', ha='center')
    ring(right, (10, 0), 5, .3, 1, '5')
    ring(right, (-9.8, 0), 4.9, .3, 2, '4.9')
    ring(right, (-.1, 0), 4.8, .3, 3, '4.8')
    right.set_title('Worst fit: 4 rings\n4.9 and 4.8 share the hole', fontsize=12, pad=9)
    save(fig, 'contraejemplo_n4.png')


def divergence():
    fig, axes = plt.subplots(1, 2, figsize=(7, 3.7), layout='constrained')
    for ax in axes:
        pan(ax, 10)
    left, right = axes
    ring(left, (0, 0), 9, 1, 0, '')
    left.text(0, 6.6, '9', ha='center')
    ring(left, (0, 0), 4.2, 1, 1, '4.2')
    left.set_title(f'Maximum area\n2 rings; area = {24.4*math.pi:.1f}', fontsize=12, pad=9)
    circumradius = 8.4 / math.sqrt(3)
    centers = [(circumradius*math.cos(t), circumradius*math.sin(t))
               for t in (math.pi/6, 5*math.pi/6, 3*math.pi/2)]
    assert circumradius + 4.2 < 10
    for i, center in enumerate(centers):
        for other in centers[:i]:
            assert math.dist(center, other) >= 8.4 - 1e-12
        ring(right, center, 4.2, 1, i+1, '4.2')
    right.set_title(f'Maximum cardinality\n3 rings; area = {22.2*math.pi:.1f}', fontsize=12, pad=9)
    save(fig, 'divergencia_calamares.png')


def phase_diagram():
    # Same grid and thresholds as code/franja.py; this is a figure, not a proof.
    thresholds = {1: 1., 2: .5}
    for k in range(3, 7):
        thresholds[k] = 1 / (1 + 1/math.sin(math.pi/k))
    thresholds.update({7: thresholds[6], 8: 1/(1+1/math.sin(math.pi/7)),
                       9: 1/(1+1/math.sin(math.pi/8)), 10: .262258924})
    small = np.arange(2.65, 5.201, .01)
    big = np.arange(4.80, 9.801, .01)
    p, b = np.meshgrid(small, big)

    def maxfit(ratio):
        result = np.zeros_like(ratio, dtype=int)
        for n, threshold in thresholds.items():
            result = np.where(ratio <= threshold + 1e-12, n, result)
        return result

    n_pan, n_hole = maxfit(p/10), maxfit(p/(b-1))
    with_count, without_count = 1+n_hole, n_pan
    with_area = (2*b-1) + n_hole*(2*p-1)
    without_area = n_pan*(2*p-1)
    grid = np.zeros_like(n_pan)
    grid[(with_area >= without_area) & (with_count >= without_count)] = 1
    grid[(without_count > with_count) & (with_area > without_area)] = 2
    grid[(with_count > without_count) & (without_area > with_area)] = 3
    colors = ['#c7d9ec', '#f2c9a1', '#c0392b', '#7d3c98']
    fig, ax = plt.subplots(figsize=(7, 4.5), layout='constrained')
    ax.imshow(grid, origin='lower', aspect='auto', cmap=ListedColormap(colors),
              vmin=0, vmax=3, extent=[small[0], small[-1], big[0], big[-1]])
    ax.plot(4.2, 9, 'k*', ms=11, mec='white')
    ax.annotate('Example above\n(4.2, 9.0)', (4.2, 9), xytext=(12, -28),
                textcoords='offset points', fontsize=10)
    ax.set_xlabel(r'Small-ring radius $\rho$')
    ax.set_ylabel(r'Large-ring radius $b$')
    labels = ['Both prefer omitting the large ring', 'Both prefer the large ring',
              'Area prefers it; cardinality omits it', 'Reverse divergence']
    ax.legend(handles=[Patch(fc=c, label=s) for c, s in zip(colors, labels)],
              loc='lower left', fontsize=9, framealpha=.96)
    save(fig, 'franja_divergencia.png')


if __name__ == '__main__':
    counterexample()
    divergence()
    phase_diagram()
    print('Three v2 figures regenerated.')
