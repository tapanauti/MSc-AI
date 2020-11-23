import random
import numpy as np
import math
import matplotlib.pyplot as plt
from deap import benchmarks
# function to optimize: takes in a list of decision variables, returns an objective value
# this is the Rosenbrock function: http://en.wikipedia.org/wiki/Rosenbrock_function
# the global minimum is located at x = (1,1) where f(x) = 0
def my_function(x):
    # a = 0.25
    # b = 0.10
    # np.array(x)
    # return np.sum((((x[1:]**2.0) + (x[:-1]**2.0))**a)  * ((np.sin( 50 * (x[1:]**2.0) +((x[:-1]**2.0)**b))) + 1))
    return np.sum((x**2+x1**2)**0.25 * ((np.sin(50*(x**2+x1**2)**0.1))**2+1.0) for x, x1 in zip(x[1:], x[:-1]))
    #return np.sum(x[1:]*np.sin(math.sqrt(x[1:])))
def rosenbrock(x): # test problem, hard
    # from https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.rosen.html
    return np.sum((100.0*(x - x1**2.0)**2.0 + (1 - x1)**2.0) for x,x1 in zip(x[1:],x[:-1]))

def schaffer(x):
    return benchmarks.schaffer(x)[0]

def schwefel(sol):
    return benchmarks.schwefel(sol)[0]
# function to perform (a very crude, stupid) optimization
# bounds = lower and upper bounds for each decision variable (2D list)
# NFE = number of function evaluations to perform
# f = the function to be optimized
def optimize(bounds, NFE, f):
  D = len(bounds) # number of decision variables
  best_f = 9999.0 # initialize the "best found" - both the function value and the x values
  best_x = [None]*D
  history = []
  for i in range(NFE):
    # use an "operator" to generate a new candidate solution
    # this is "uniform mutation" in MOEA lingo
    new_x = [bounds[d][0] + random.random()*(bounds[d][1] - bounds[d][0]) for d in range(D)]
    
    #print(new_x)
    new_f = f(new_x)
    if new_f < best_f: # see if it's an improvement -- in multiobjective, this is the Pareto sort
      best_f = new_f
      best_x = new_x
    history.append((i,best_f))

  return best_x,np.array(history)

#result = []
# now let's try it...
# (the Rosenbrock problem technically doesn't have "bounds", but we'll make some up..)
bounds = [[-500,500],[-500,500],[-500,500],[-500,500],[-500,500],[-500,500]]
#bounds = [[-1,5],[-1,5],[-1,5],[-1,5],[-1,5],[-1,5]]
its = 50000
for i in range (0,5):
    random.seed(i)  
    x,history =optimize(bounds, its,schwefel)
# print(history[-1][1])
plt.plot(history[:, 0], history[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("Random_plot.pdf")
plt.close()
#x,history = optimize(bounds, 50000,schaffer)
for i in range(0,its):
    mu = np.sum(np.mean(history[i][1]))
    sigma = np.sum(np.var(history[i][1]))


# it should be near best_f = 0.0 and best_x = [1,1], hopefully