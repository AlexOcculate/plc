import prettyplotlib as ppl
import numpy as np
from prettyplotlib import plt

fig, ax = plt.subplots(1)

np.random.seed(14)

# 'y' for make a grid based on where the major ticks are on the y-axis
ppl.bar(ax, np.arange(10), np.abs(np.random.randn(10)), grid='y')
fig.savefig('bar_prettyplotlib_grid.png')