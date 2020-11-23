import math
import random

def SA(f, init, nbr, T, alpha, maxits):
    """Simulated annealing. Assume we are minimising.
    Return the best ever x and its f-value.

    Pass in initial temperature T and decay factor alpha.

    T decays by T *= alpha at each step.
    """
    x = init() # generate an initial random solution
    fx = f(x)
    bestx = x
    bestfx = fx

    for i in range(1, maxits):
        xnew = nbr(x) # generate a neighbour of x
        fxnew = f(xnew)
        
        # "accept" xnew if it is better, OR even if worse, with a
        # small probability related to *how much worse* it is. assume
        # we are minimising, not maximising.
        if fxnew < fx or random.random() < math.exp((fx - fxnew) / T):
            x = xnew
            fx = fxnew

            # make sure we keep the best ever x also
            if fxnew < bestfx:
                bestx = x
                bestfx = fx
            
        T *= alpha # temperature decreases
        print(i, fx, T)
    return bestx, bestfx

# our standard bitstring init. use lambda: init(n) to give a function
# that takes no parameters.
def bitstring_init(n):
    return [random.randrange(2) for _ in range(n)]

# our usual bitstring nbr
def bitstring_nbr(x):
    x = x.copy()
    i = random.randrange(len(x))
    x[i] = 1 - x[i]
    return x

onemax = sum
bestx, bestfx = SA(onemax,
                   lambda: bitstring_init(1000),
                   bitstring_nbr,
                   1,
                   0.999,
                   5000)
