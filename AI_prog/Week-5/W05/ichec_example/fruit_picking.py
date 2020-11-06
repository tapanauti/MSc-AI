# Solving a *facility location* problem using CMA-ES.

# Usage: python fruit_picking.py <data filename> <m> <seed>

# We have many small flying robots, picking fruit from trees in a
# large square field (the unit square).

# There are n trees. Tree i is in location T_i. The amount of fruit to
# be picked from tree i is w_i. There are m bins for the fruit to be
# delivered to, of unlimited capacity. Each robot picks one fruit from
# a tree and then delivers it to the nearest bin, and then goes back
# to the same tree.

# We want to avoid having to recharge the robots' batteries often, so
# we want to minimise the total flying distance by placing the bins
# in good positions. Thus, we have to choose 2m real numbers.

import sys
import cma # pip install cma
import numpy as np
import matplotlib.pyplot as plt



def plot(x, i):
    # make a plot to show T, w and x
    plt.xlim((0, 1))
    plt.ylim((0, 1))
    # plot the tree locations and use w to indicate amount of fruit
    plt.scatter(T[:, 0], T[:, 1], s=100.0*w, c="g")
    bins = x.reshape((m, 2))
    # plot the bin locations as squares
    plt.scatter(bins[:, 0], bins[:, 1], marker="s", c="r")
    plt.axes().set_aspect('equal')
    plt.savefig("fruit_picking_%s.png" % str(i).zfill(5))
    plt.close()


def dist(a, b):
    # Euclidean distance
    return np.sqrt(np.sum((a - b) ** 2))

def f(x):
    # objective: minimise weighted distance to nearest bin, summed
    # across trees.
    bins = x.reshape((m, 2))
    total_dist = 0.0
    for t in range(n):
        tree = T[t]
        nearest = min(dist(tree, b) for b in bins)
        total_dist += w[t] * nearest
    return total_dist

filename = sys.argv[1]
m = int(sys.argv[2]) # number of bins
seed = int(sys.argv[3]) # NB do not set CMA seed to 0, it treats that as "no seed"!

np.random.seed(seed)
data = np.genfromtxt(filename)
T = data[:, 0:2] # x, y locations of trees
w = data[:, 2] # amount of fruit per tree
n = T.shape[0]
initial = np.random.random(m * 2) # initial x, y locations of bins
maxits = 200 * (2 * m) # search effort increases with problem dimension
sigma = 0.5

es = cma.CMAEvolutionStrategy(initial,
                              sigma,
                              {'bounds': [0.0, 1.0],
                               'seed': seed})
i = 0
while not es.stop() and i < maxits / es.popsize:
   X = es.ask()
   if i % 10 == 0:
       current_x = X[0] # use this for plotting
       plot(current_x, i)
   es.tell(X, [f(x) for x in X])
   es.disp()
   i += 1

# The above code uses the "ask-tell" interface.
# A much simpler interface is available, but doesn't
# allow us to inspect x during the evolution:

# es.optimize(f, iterations=maxits / es.popsize)   

xbest, fbest, evals_best, evaluations, iterations, xfavorite, stds, stop = es.result
print("xbest")
print(xbest)
