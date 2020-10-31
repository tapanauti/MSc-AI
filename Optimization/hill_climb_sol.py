import numpy as np
import random
import matplotlib.pyplot as plt

# the simplest metaheuristic search algorithm
def hill_climb(f, init, nbr, its=10000, stop=None):
    """
    f: objective function X -> R (where X is the search space)
    init: function giving random element of X
    nbr: function X -> X which gives a neighbour of the input x
    its: number of iterations, ie fitness evaluation budget
    stop: termination criterion (X, R) -> bool
    return: best ever x
    
    In this version, we store and return a history of
    best objective values; we avoid wasting objective evaluations;
    we allow a termination criterion.
    """
    history = [] # create history
    x = init()
    fx = f(x) # fx stores f of current best point
    for i in range(its):
        xnew = nbr(x)
        fxnew = f(xnew) # avoid re-calculating f
        if fxnew > fx: # we maximise, not minimise
            x = xnew
            fx = fxnew
        history.append((i, fx)) # save history
        if stop is not None and stop(x, fx): # a termination condition
            break
    return x, np.array(history) # return history

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
    return np.random.random()
def real_nbr(x):
    delta = 0.3
    x = x.copy()
    i = random.randrange(n)
    # add a small real constant in range [-delta, delta]
    x[i] = x[i] + (2 * delta * np.random.random() - delta)
    return x

# some test objective functions for real vectors
def sphere(x):
    return np.sum(x**2)
def rastrigin(x):
    # https://en.wikipedia.org/wiki/Rastrigin_function
    n = len(x)
    return np.sum(x*x - n*np.cos(2*np.pi*x)) + n*np.size(x)

def run_sphere():
    # optimise the "sphere" function for n = 2
    n = 2
    f = lambda x: -sphere(x) # we use -sphere because we minimise
    stop = lambda i, fx: abs(fx) < 0.00001
    print(hill_climb(real_init, real_nbr, f, its=10000, stop=stop))

def run_onemax_and_plot():
    # optimise the "onemax" function
    n = 8
    onemax = sum # a common (easy) test problem
    onemax_stop = lambda x, fx: fx == len(x)
    x, history = hill_climb(onemax,
                            lambda: bitstring_init(n),
                            bitstring_nbr,
                            its=2000,
                            stop=onemax_stop)

    plt.plot(history[:, 0], history[:, 1])
    plt.xlabel("Iteration"); plt.ylabel("Objective")
    plt.savefig("hill_climb_plot.pdf")
    plt.close()

def run_onemax_and_test_scalability():
    ns = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    its = 2000
    bestfxs = []
    onemax = sum
    onemax_stop = lambda x, fx: fx == len(x)
    for n in ns:
        x, history = hill_climb(onemax,
                                lambda: bitstring_init(n),
                                bitstring_nbr,
                                its=its,
                                stop=onemax_stop)
        bestfx = history[-1][1] # best ever objective value
        bestfxs.append((n, bestfx))
    bestfxs = np.array(bestfxs)
    plt.plot(bestfxs[:, 0], bestfxs[:, 1])
    plt.xlabel("Size"); plt.ylabel("Objective")
    plt.savefig("hill_climb_scalability_plot.pdf")
    plt.close()
    
        
def needle_in_haystack(x):
    # this is a "needle in a haystack": the optimum is [1, 1, .. 1],
    # with objective value 1, and every other point has objective 0.
    f = 1
    for xi in x:
        f *= xi
    return f

def medium_difficulty(x):
    # this is more difficult than onemax, because there are some
    # interactions between decision variables (onemax has no
    # interactions, in fact it is linear), but not as difficult as the
    # needle in a haystack because there are not as many interactions.
    # the optimum is [1, 1, .., 1] with objective value n-1.
    x1 = x[1:] # all but the first element
    x2 = x[:-1] # all but the last element
    f = sum(x1i * x2i for x1i, x2i in zip(x1, x2))
    return f

def guessing_game(x):
    """During undergrad, you probably programmed a guessing game where the
    computer thinks of a number and the human tries to guess it.
    Here, the human thinks of a bitstring and the computer tries to guess
    it."""
    print("Think of a bitstring and I will guess. Press Ctrl-D to stop.")
    f = lambda x: float(input(f"Here is my guess: {x}. How many are right? "))
    hill_climb(f, lambda: bitstring_init(8), bitstring_nbr, its=20,
               stop=lambda x, fx: fx == len(x))

