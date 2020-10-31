import numpy as np
import random
import matplotlib.pyplot as plt

# the simplest metaheuristic search algorithm
def hill_climb(f, init, nbr, its=10000):
    """
    f: objective function X -> R (where X is the search space)
    init: function giving random element of X
    nbr: function X -> X which gives a neighbour of the input x
    its: number of iterations, ie fitness evaluation budget
    return: best ever x
    """
    x = init() # make a random point
    for i in range(its):
        xnew = nbr(x) # make a new point by changing x
        if f(xnew) > f(x): # if it's better
            x = xnew # step to the new point
    return x

# operators for bitstrings
def bitstring_init(n):
    # uniform sampling from X
    return [random.randrange(2) for i in range(n)]
def bitstring_nbr(x):
    # "blind mutation" -- does not assume anything about the
    # objective, eg we do not know that 1s are good and 0s bad.
    x = x.copy() # otherwise we would change x itself
    i = random.randrange(len(x))
    x[i] = 1 - x[i]
    return x

# operators for real vectors
def real_init(n):
    return [random.random() for i in range(n)]
def real_nbr(x):
    x = x.copy()
    i = random.randrange(n)
    # add a small real constant in range [-delta, delta]
    delta = 0.3
    x[i] = x[i] + random.random() * 2 * delta - delta
    return x

# some test objective functions for real vectors
def sphere(x):
    return np.sum(x**2)
def rastrigin(x):
    # https://en.wikipedia.org/wiki/Rastrigin_function
    n = len(x)
    return np.sum(x*x - n*np.cos(2*np.pi*x)) + n*np.size(x)


onemax = sum
bestx = hill_climb(onemax, lambda: bitstring_init(16), bitstring_nbr)
print(bestx)

