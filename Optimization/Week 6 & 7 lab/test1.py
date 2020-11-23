from pickle import NONE
import cma
from deap import benchmarks
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

# def schaffer(x):
#     return benchmarks.schaffer(x)[0]
for i in range(0,4):
    option = {'seed': i,'maxfevals':50000}
    es = cma.CMAEvolutionStrategy(6*[0],1,option)
    es.optimize(cma.ff.schaffer,iterations =50000 )


cma.plot()
plt.savefig('cma.pdf')
plt.show()