# initial setup required for the programm run.
# for pso algorithm implementations - 'pip install mealpy'
# for cma algorithm implementation - 'pip install cma'
# for use of inbuilt benchmark function  - 'pip install deap' 
# The optimisation problem used here is the benchmark function - 'schaffer'
# more information of this function can be found at  - 'https://deap.readthedocs.io/en/master/api/benchmarks.html#deap.benchmarks.schaffer'
# 'https://www.sfu.ca/~ssurjano/schaffer2.html'  and  'http://benchmarkfcns.xyz/benchmarkfcns/schaffern1fcn.html'

import random
import numpy as np
import matplotlib.pyplot as plt
import cma # for cma implementation
from opfunu.cec_basic.cec2014_nobias import * # requirement for mealpy
from mealpy.swarm_based.PSO import BasePSO,PPSO,PSO_W,HPSO_TVA # mealpy implementation of PSO
from mealpy.swarm_based.GWO import BaseGWO, RW_GWO # mealpy Implementation of GWO
from deap import benchmarks # inbulit function(optimisation problem) for usage in all algorithms


def schaffer(x):
      return benchmarks.schaffer(x)[0]   # Inbuilt fucntion available for use from deap library's benchmark functions

# Can use this also , based on the equation from ' https://deap.readthedocs.io/en/master/api/benchmarks.html#deap.benchmarks.schaffer'
# constructed this one for use.
def _schaffer_(x):
      return np.sum((x**2+x1**2)**0.25 * ((np.sin(50*(x**2+x1**2)**0.1))**2+1.0) for x, x1 in zip(x[1:], x[:-1]))   


#-------------------------------------------------------------------------------- RANDOM SEARCH -----------------------------------------------------------------------------------------


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
      np.random.seed(i)  
      x,history =optimize(bounds, its,schaffer)
plt.plot(history[:, 0], history[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("Random_plot.pdf")
plt.close()

# getting the mean and standard deviation for results and comparison.
for i in range(0,its):
      mu = np.sum(np.mean(history[:,1])) # mean
      sigma = np.sum(np.var(history[:,1])) # stnadard deviation
print(mu,sigma)


#------------------------------------------------------------------------------------- CMA -------------------------------------------------------------------------------- 


# Basic cma -es but changes in hyperparameters like the initial mean being  a randomised value between bounds and difference of bounds and the sigma being 2/5 of bound.
for i in range(1,5):
      np.random.seed(i)
      option = {'seed': i} # to hide console print every run use 'verb_disp':0 inside this option.
      mean = (-100 + (np.random.rand() * 200))
      es = cma.CMAEvolutionStrategy(6*[mean],40,option) # for eavery decision variable initialsing the same value of mean.
      es.optimize(cma.ff.schaffer,iterations =50000 ) # cma has inbulit birary of function (ff), schaffer function is taken from it and used 
      print(es.result_pretty())
#the cms stores all the genrated reports in a .dat file, so using one of the 'fit.dat' file for factorial design experiment.
data=[]
with open (r"C:\\Users\\CS-Guest-2\\Desktop\\Nuig\\MSc_AI\\outcmaes\\fit.dat") as f:
  next(f)
  data = np.loadtxt(f)
plt.plot(data[:, 0], data[:, 4])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig('cma_variant.pdf')
plt.show()

# The original basic cma implementation with initial mean as 0 and sigma as 1.
for i in range(1,5):
      np.random.seed(i)
      option = {'seed': i}
      es = cma.CMAEvolutionStrategy(6*[0],1,option)
      es.optimize(cma.ff.schaffer,iterations =50000 )
      print(es.result_pretty())
data=[]
with open (r"C:\\Users\\CS-Guest-2\\Desktop\\Nuig\\MSc_AI\\outcmaes\\fit.dat") as f:
  next(f)
  data = np.loadtxt(f)
plt.plot(data[:, 0], data[:, 4])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig('basecma.pdf')
plt.show()

# The cma variation using bipop strategy  which progressively increments the population , here i'm taking restarts as 1 as i dont want many runs for the function.(as 4 runs already taking place due to seed.)
for i in range(1,10):
      np.random.seed(i)
      options = {'seed':i, 'verb_time':0, 'ftarget': 1e-8, 'maxfevals': 5e4}
      res = cma.fmin(schaffer, '2. * np.random.rand(6) - 1', 0.5,options, bipop=True)
      print(res[1])
data=[]
with open (r"C:\\Users\\CS-Guest-2\\Desktop\\Nuig\\MSc_AI\\outcmaes\\fit.dat") as f:
  next(f)
  data = np.loadtxt(f)
plt.plot(data[:, 0], data[:, 4])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig('bipopcma.pdf')
plt.show()


# -------------------------------------------------------------------------------------- PSO -------------------------------------------------------------------------------------


obj_func = schaffer # using  the defined schaffer function
lb = [-100]
ub = [100]
problem_size = 6 # decision variables
batch_size = 2
verbose = False # Make true if you want to display each iteration on console
# these being population based algorithms here total iterations are gen * population size , so epoch * pop_size gives 50000 iterations - confirmed the setting from all algorithms source code available at -
# 'https://github.com/thieu1995/mealpy '
epoch = 500
pop_size = 100
res = []

# The original version of particle swarm optimisation
for i in range (1,5):
    np.random.seed(i)        
    md1 = BasePSO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1 = md1.train()
    print(md1.solution[1]) # prints the optimal solution
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
# sd = np.sum(np.var(md1.loss_train)) # uncomment if you want or print the sigma
# print(sd)
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("basepso.pdf")
plt.close()

#Simple and effective variant of PSO: Phaser Partcle Swarm Optimisation -  in this while creating list instead of uniform nature we take many multipe random geometric constants and add them to the best positions form the list.
#the source code for all these variants  is availbale at ' https://github.com/thieu1995/mealpy/blob/master/mealpy/swarm_based/PSO.py'
for i in range (1,5):
    np.random.seed(i) 
    md1 = PPSO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1 = md1.train()
    print(md1.solution[1]) # prints the optimal solution
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
# sd = np.sum(np.var(md1.loss_train)) # uncomment if you want or print the sigma
# print(sd)
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("ppso.pdf")
plt.close()

# Another interesting variant of Phaser PSO where for the initial list another temporary variant is taken and that is multiplied with each element list to get the final list.
# source code for the same avialable in the previously mentioned link.
for i in range (1,5):
    np.random.seed(i) 
    md1 = PSO_W(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1 = md1.train()
    print(md1.solution[1]) # prints the optimal solution
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
# sd = np.sum(np.var(md1.loss_train)) # uncomment if you want or print the sigma
# print(sd)
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("ppso_w_demo.pdf")
plt.close()

# This one was by far the most iteresting implementation for PSO , it is a hierarchical PSO with junping time- varying accelerations,
#  (such a fancy name: but is it really that worth of variant, chcek the answer and plot to find out ), in this algorithm the acceleration coefficients take the absolute value with the inertia weights and then this is 
# multiplied with uniform list intials to form a new list which is the mean of acceleration constants. ( Didn't get what i'm trying to say check the source code(mentioned above link above) for a peek at this algorithm.)
for i in range (1,10):
    np.random.seed(i) 
    md1 = HPSO_TVA(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1 = md1.train()
    print(md1.solution[1]) # prints the optimal solution
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
# sd = np.sum(np.var(md1.loss_train)) # uncomment if you want or print the sigma
# print(sd)
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("hpso_tva.pdf")
plt.close()

# This the basic random grey wolf optimisation.
for i in range (1,5):
    np.random.seed(i) 
    md1 = BaseGWO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1 = md1.train()
    print(md1.solution[1]) # prints the optimal solution
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
# sd = np.sum(np.var(md1.loss_train)) # uncomment if you want or print the sigma
# print(sd)
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("gwo.pdf")
plt.close()

# this is novel  random walk grey wolf optimsation variant which is speculated to give less optimised results than that of GWO, let's check result to find the truth.
for i in range (1,5):
    np.random.seed(i) 
    md1 = RW_GWO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1 = md1.train()
    print(md1.solution[1]) # prints the optimal solution
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
sd = np.sum(np.var(md1.loss_train)) # uncomment if you want or print the sigma
print(sd)
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("rw_gwo.pdf")
plt.close()


#----------------------------------------------------------------------------------------------------------- END -----------------------------------------------------------------------------------------