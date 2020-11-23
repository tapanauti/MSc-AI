from re import VERBOSE
from deap import benchmarks
import matplotlib.pyplot 
import numpy as np

# # def schaffer(x):
# #     return benchmarks.schaffer(x)[0]
# for i in range(0,5):
#     option = {'seed': i,'maxfevals':50000}
#     # res = cma.fmin(cma.ff.schaffer,6 * [0.5],0.3,option)
#     es = cma.CMAEvolutionStrategy(6*[0],1,option)
#     es.optimize(cma.ff.schaffer,iterations =1000  )

# # res = es.result_pretty()
# es.logger.plot()

from pymoo.algorithms.so_cmaes import CMAES
from pymoo.factory import get_problem
from pymoo.optimize import minimize

problem = get_problem("schwefel")

algorithm = CMAES()

res = minimize(problem,algorithm,('n_eval',50000),seed = 1,verbose=True )

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))