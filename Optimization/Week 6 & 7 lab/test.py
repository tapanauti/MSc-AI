import random
import numpy as np
import matplotlib.pyplot as plt
from deap import benchmarks

def schaffer(x):
    return benchmarks.schaffer(x)[0]   # Inbuilt fucntion available for use from deap library's benchmark functions

# Can use this also , based on the equation from ' https://deap.readthedocs.io/en/master/api/benchmarks.html#deap.benchmarks.schaffer'
# constructed this one for use.
def my_function(x):
      return np.sum((x**2+x1**2)**0.25 * ((np.sin(50*(x**2+x1**2)**0.1))**2+1.0) for x, x1 in zip(x[1:], x[:-1]))   


# function to perform (a very crude) optimization
# bounds = lower and upper bounds for each decision variable (2D list)
# NFE = number of function evaluations to perform
# f = the function to be optimized
# this function is used from 'https://gist.github.com/jdherman/6e7b9d588c57380bc3e7' did some changes to functionality for using it for schaffer and desired output.
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
    history.append((i,best_f)) # append the iteration and the objective function for it.

  return best_x,np.array(history)

bounds = [[-100,100], [-100,100 ],[-100,100 ],[-100,100 ],[-100,100 ],[-100,100 ]] # setting the bounds for 6 decision variables.

its = 50000 # no of iterations
#running this for 4 runs and ploting the factorial design.
for i in range (0,5):
    random.seed(i)  
    x,history =optimize(bounds, its,schaffer)
plt.plot(history[:, 0], history[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("Random_plot.pdf")
plt.close()

# getting the mean and standard deviation for results and comparison.
for i in range(0,its):
      mu = np.sum(np.mean(history[:,1])) # mean
      sigma = np.sum(np.var(history[:,1])) # stnadard deviation
print(sigma)
