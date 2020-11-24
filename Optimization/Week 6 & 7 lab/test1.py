from pickle import NONE
import cma
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

# def schaffer(x):
#     return benchmarks.schaffer(x)[0]
for i in range(0,4):
    option = {'seed': i,'maxfevals':50000}
    es = cma.CMAEvolutionStrategy(6*[0],1,option)
    es.optimize(cma.ff.schaffer,iterations =50000 )


cma.plot()
data=[]
with open (r"C:\\Users\\CS-Guest-2\\Desktop\\Nuig\\MSc_AI\\outcmaes\\fit.dat") as f:
    next(f)
    data = np.loadtxt(f)
plt.plot(data[:, 0], data[:, 4])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig('cma.pdf')
plt.show()