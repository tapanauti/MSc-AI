import cma
import numpy as np
import matplotlib.pyplot as plt
from deap import benchmarks

def schaffer(x):
    return benchmarks.schaffer(x)[0]

# Basic cma -es but changes in hyperparameters like the initial mean being  a randomised value between bounds and difference of bounds and the sigma being 2/5 of bound.
for i in range(1,5):
    option = {'seed': i}
    mean = (-100 + (np.random.rand() * 200))
    es = cma.CMAEvolutionStrategy(6*[mean],40,option) # for eavery decision variable initialsing the same value of mean.
    es.optimize(cma.ff.schaffer,iterations =50000 )
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

# The original basic cma impleentation with initial mean as 0 and sigma as 1.
for i in range(1,5):
    option = {'seed': i}
    es = cma.CMAEvolutionStrategy(6*[0],1,option)
    es.optimize(cma.ff.schaffer,iterations =100 )
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
for i in range(1,5):
    options = {'seed':i, 'verb_time':0, 'ftarget': 1e-8}
    res = cma.fmin(schaffer, '2. * np.random.rand(3) - 1', 0.5,options, bipop=True)
data=[]
with open (r"C:\\Users\\CS-Guest-2\\Desktop\\Nuig\\MSc_AI\\outcmaes\\fit.dat") as f:
    next(f)
    data = np.loadtxt(f)
plt.plot(data[:, 0], data[:, 4])
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.savefig('bipopcma.pdf')
plt.show()