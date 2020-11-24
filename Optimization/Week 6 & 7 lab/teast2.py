from deap import benchmarks
import numpy as np
# # import pyswarms as ps
# # from pyswarms.utils.functions import single_obj as fx
# # from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
# import matplotlib.pyplot as plt
# import random
# # def schaffer(x):
# #     a = 0.25
# #     b = 0.10
# #     np.sum((((x[1:]**2.0) + (x[:-1]**2.0))**a)  * ((np.sin( 50 * (x[1:]**2.0) +((x[:-1]**2.0)**b))) + 1))
# #     return benchmarks.schaffer(x)[0]


# # Set-up optimizer
# # for i in range(0,4):
# #     random.seed(i)
# options = {'c1':1, 'c2':2, 'w':0.5}
# optimizer = ps.single.GlobalBestPSO(n_particles = 6, dimensions = 2,options=options)
# optimizer.optimize(fx.schaffer2, iters=50000)
# # Plot the cost
# plot_cost_history(optimizer.cost_history)
# plt.show()

from opfunu.cec_basic.cec2014_nobias import *
from mealpy.swarm_based.PSO import BasePSO,PPSO,PSO_W,HPSO_TVA
from mealpy.swarm_based.GWO import BaseGWO, RW_GWO
from mealpy.swarm_based.WOA import BaseWOA
import matplotlib.pyplot as plt
def schaffer(x):
    # a = 0.25
    # b = 0.10
    # np.sum((((x[1:]**2.0) + (x[:-1]**2.0))**a)  * ((np.sin( 50 * (x[1:]**2.0) +((x[:-1]**2.0)**b))) + 1))
    return benchmarks.schaffer(x)[0]

obj_func = schaffer
lb = [-100]
ub = [100]

problem_size = 6
batch_size = 2
verbose = True
epoch = 500
pop_size = 100
res = []

md1 = BasePSO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
#print(md1.solution[0])
print(md1.solution[1])
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("pso_1.pdf")
plt.close()


md1 = PPSO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
print(md1.solution[1])
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("pso_1.pdf")
plt.close()


md1 = PSO_W(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
print(md1.solution[1])
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("pso_1.pdf")
plt.close()


md1 = HPSO_TVA(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
print(md1.solution[1])
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("pso_1.pdf")
plt.close()

md1 = BaseGWO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
print(md1.solution[1])
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("pso_1.pdf")
plt.close()

md1 = RW_GWO(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
print(md1.solution[1])
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("pso_1.pdf")
plt.close()

md1 = BaseWOA(obj_func, lb, ub, problem_size, batch_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
print(md1.solution[1])
for i in range(0,epoch):
    res.append([i,md1.loss_train[i]])
res = np.array(res)
plt.plot(res[:, 0], res[:, 1])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig("pso_1.pdf")
plt.close()