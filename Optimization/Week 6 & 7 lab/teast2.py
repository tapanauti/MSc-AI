from deap import benchmarks
import random
import numpy as np
from opfunu.cec_basic.cec2014_nobias import *
from mealpy.swarm_based.PSO import BasePSO,PPSO,PSO_W,HPSO_TVA
from mealpy.swarm_based.GWO import BaseGWO, RW_GWO
import matplotlib.pyplot as plt

# def schaffer(x):
#     return benchmarks.schaffer(x)[0]

# obj_func = schaffer
# lb = [-100]
# ub = [100]
# problem_size = 6 # decision variables
# batch_size = 2
# verbose = True
# # these being population based algorithms here total iterations are gen * population size , so epoch * pop_size gives 50000 iterations - confirmed the setting from all algorithms source code available at -
# # 'https://github.com/thieu1995/mealpy '
# epoch = 500
# pop_size = 100
# res = []

# # The original version of particle swarm optimisation
# for i in range (1,5):
#     random.seed(i)        
#     md1 = BasePSO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
#     best_pos1, best_fit1, list_loss1 = md1.train()
# print(md1.solution[1]) # prints the optimal solution
# for i in range(0,epoch):
#     res.append([i,md1.loss_train[i]])
# res = np.array(res)
# plt.plot(res[:, 0], res[:, 1])
# plt.xlabel("Iteration"); plt.ylabel("Objective")
# plt.savefig("basepso.pdf")
# plt.close()

# # Simple and effective variant of PSO: Phaser Partcle Swarm Optimisation -  in this while creating list instead of uniform nature we take many multipe random geometric constants and add them to the best positions form the list.
# # the source code for all these variants  is availbale at ' https://github.com/thieu1995/mealpy/blob/master/mealpy/swarm_based/PSO.py'
# for i in range (1,5):
#     random.seed(i) 
#     md1 = PPSO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
#     best_pos1, best_fit1, list_loss1 = md1.train()
# print(md1.solution[1])
# for i in range(0,epoch):
#     res.append([i,md1.loss_train[i]])
# res = np.array(res)
# plt.plot(res[:, 0], res[:, 1])
# plt.xlabel("Iteration"); plt.ylabel("Objective")
# plt.savefig("ppso.pdf")
# plt.close()

# # Another interesting variant of Phaser PSO where for the initial list another temporary variant is taken and that is multiplied with each element list to get the final list.
# # source code for the same avialable in the previously mentioned lin.
# for i in range (1,5):
#     random.seed(i) 
#     md1 = PSO_W(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
#     best_pos1, best_fit1, list_loss1 = md1.train()
# print(md1.solution[1])
# for i in range(0,epoch):
#     res.append([i,md1.loss_train[i]])
# res = np.array(res)
# plt.plot(res[:, 0], res[:, 1])
# plt.xlabel("Iteration"); plt.ylabel("Objective")
# plt.savefig("ppso_w.pdf")
# plt.close()

# # This one was by far the most iteresting implementation for PSO , it is a hierarchical PSO with junping time- varying accelerations,
# #  (such a fancy name: but is it really that worth of variant, chcek the answer and plot to find out ), in this algorithm the acceleration coefficients take the absolute value with the inertia weights and then this is 
# # multiplied with uniform list intials to form a new list which is the mean of acceleration constants. ( Didn't get what i'm trying to say check the source code(mentioned above link above) for a peek at this algorithm.)
# for i in range (1,5):
#     random.seed(i) 
#     md1 = HPSO_TVA(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
#     best_pos1, best_fit1, list_loss1 = md1.train()
# print(md1.solution[1])
# for i in range(0,epoch):
#     res.append([i,md1.loss_train[i]])
# res = np.array(res)
# plt.plot(res[:, 0], res[:, 1])
# plt.xlabel("Iteration"); plt.ylabel("Objective")
# plt.savefig("hpso_tva.pdf")
# plt.close()

# # This the basic random grey wolf optimisation.
# for i in range (1,5):
#     random.seed(i) 
#     md1 = BaseGWO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
#     best_pos1, best_fit1, list_loss1 = md1.train()
# print(md1.solution[1])
# for i in range(0,epoch):
#     res.append([i,md1.loss_train[i]])
# res = np.array(res)
# plt.plot(res[:, 0], res[:, 1])
# plt.xlabel("Iteration"); plt.ylabel("Objective")
# plt.savefig("gwo.pdf")
# plt.close()

# # this is novel  random walk grey wolf optimsation variant which is speculated to give less optimised results than that of GWO, let's check result to find the truth.
# for i in range (1,5):
#     random.seed(i) 
#     md1 = RW_GWO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
#     best_pos1, best_fit1, list_loss1 = md1.train()
# print(md1.solution[1])
# for i in range(0,epoch):
#     res.append([i,md1.loss_train[i]])
# res = np.array(res)
# plt.plot(res[:, 0], res[:, 1])
# plt.xlabel("Iteration"); plt.ylabel("Objective")
# plt.savefig("rw_gwo.pdf")
# plt.close()

std_deviation=[3.593276070468794e-13, 5.067408066524548e-18, 2.668094881251309e-18, 5.471293048464291e-18, 9.237734312316854e-12, 2.5604029196684186e-12] 
std_deviation = np.mean(std_deviation)
print(std_deviation)