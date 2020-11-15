import numpy as np

import random
import matplotlib.pyplot as plt

# this GA is for minimisation
def GA(f, init, nbr, crossover, select, popsize, ngens, pmut):
    history = []
    # make initial population, evaluate fitness, print stats
    pop = [init() for _ in range(popsize)]
    popfit = [f(x) for x in pop]
    history.append(stats(0, popfit))
    for gen in range(1, ngens):
        # make an empty new population
        newpop = []
        # elitism
        bestidx = min(range(popsize), key=lambda i: popfit[i])
        best = pop[bestidx]
        newpop.append(best)
        while len(newpop) < popsize:
            # select and crossover
            p1 = select(pop, popfit)
            p2 = select(pop, popfit)
            c1, c2 = crossover(p1, p2)
            # apply mutation to only a fraction of individuals
            if random.random() < pmut:
                c1 = nbr(c1)
            if random.random() < pmut:
                c2 = nbr(c2)
            # add the new individuals to the population
            newpop.append(c1)
            # ensure we don't make newpop of size (popsize+1) - 
            # elitism could cause this since it copies 1
            if len(newpop) < popsize:
                newpop.append(c2)
        # overwrite old population with new, evaluate, do stats
        pop = newpop
        popfit = [f(x) for x in pop]
        history.append(stats(gen, popfit))
    bestidx = np.argmin(popfit)
    return popfit[bestidx], pop[bestidx], history

def stats(gen, popfit):
    # let's return the generation number and the number
    # of individuals which have been evaluated
    return gen, (gen+1) * len(popfit), np.min(popfit), np.mean(popfit), np.median(popfit), np.max(popfit), np.std(popfit)
    
def tournament_select(pop, popfit, size):
    # To avoid re-calculating f for same individual multiple times, we
    # put fitness evaluation in the main loop and store the result in
    # popfit. We pass that in here.  Now the candidates are just
    # indices, representing individuals in the population.
    candidates = random.sample(list(range(len(pop))), size)
    # The winner is the index of the individual with min fitness.
    winner = min(candidates, key=lambda c: popfit[c])
    return pop[winner]

def real_init(n):
    return np.random.normal(size=n)

def real_nbr(x):
    delta = 0.1
    x = x.copy()
    # draw from a Gaussian
    x = x + delta * np.random.randn(len(x))
    return x

def uniform_crossover(p1, p2):
    c1, c2 = [], []
    for i in range(len(p1)):
        if random.random() < 0.5:
            c1.append(p1[i]); c2.append(p2[i])
        else:
            c1.append(p2[i]); c2.append(p1[i])
    return np.array(c1), np.array(c2)

def rastrigin(x):
    # https://en.wikipedia.org/wiki/Rastrigin_function
    n = len(x)
    return np.sum(x*x - n*np.cos(2*np.pi*x)) + n*np.size(x)

n = 6
f = rastrigin
popsize = 100
ngens = 100
pmut = 0.1
tsize = 2
bestf, best, h = GA(f,
                    lambda: real_init(n),
                    real_nbr,
                    uniform_crossover,
                    lambda pop, popfit: tournament_select(pop, popfit, tsize),
                    popsize,
                    ngens,
                    pmut
)

h = np.array(h)

# plot min fit against number of individuals so far. we see fast
# improvements, then a sense of "plateau".
plt.plot(h[:, 1], h[:, 2])
plt.xlabel("Iterations")
plt.ylabel("Fitness")
plt.show()
plt.close()

# plot std fit against number of individuals so far.  we see that the
# SD becomes very small after only about 1/5th of the run... but it
# remains non-zero, so the population is not fully converged.
plt.plot(h[:, 1], h[:, -1])
plt.xlabel("Iterations")
plt.ylabel("SD(fitness)")
plt.show()
plt.close()
