
import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from time import perf_counter

"""
A way to calculate compound interest, using
some cool Python technologies and other methods
to play around with a common implementation.
"""

# This algorithm is as fast as the Numpy version, but,
# when the Numpy version is JIT'd, that version is 8x faster
# at that computation. Fun to build a basic `nth_root` algorithm!
@jit(nopython=True, fastmath=True)
def nth_root(x, n=2, prec=0.0001):
    prec = prec # percentage terms
    b = 2 # breakdown
    e = x / b # expected
    while True:
        # make current.
        curr = e**n # current resolve

        # check if good to leave.
        diff = abs(curr - x) # guess difference
        perc_off = diff/x # percentage from x
        if perc_off < prec: # done!
            break

        # move the needle
        b += 1
        move = 1 / b
        e *= 1 + (move * (-1 if curr > x else 1))
    return e

# An extremely fast `nth_root` implementation using JIT
# compilation.
@jit(nopython=True, fastmath=True)
def nth_root_numpy(x, n=2):
    return np.power(x, (1 / n))

# Calculating the base weekly rates from yearly.
yearly_apy = 1.06 # conservative.
weekly_apy = nth_root(yearly_apy, 52, prec=0.000001)

# Configurables.
weekly_deposit = 500
value = 0 # running value
contributions = 0
years = 10
weeks = years*52

# Plot information.
plot_contributions = [[], []] # running contributions
plot_value = [[], []] # running value of fund

# Simulate.
for i in range(weeks):
    # Run through weekly actions. Apply interest first.
    value *= weekly_apy
    contributions += weekly_deposit
    value += weekly_deposit

    # Add plottable values.
    plot_contributions[0].append(i)
    plot_contributions[1].append(contributions)
    plot_value[0].append(i)
    plot_value[1].append(value)

# Plot contributions and values.
plt.plot(*plot_contributions)
plt.plot(*plot_value)
plt.show()
