from deap import benchmarks
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
import matplotlib.pyplot as plt
import random
def schaffer(x):
    return benchmarks.schaffer(x)[0]


# Set-up optimizer
for i in range(0,4):
    random.seed(i)
    options = {'c1':2.05, 'c2':2.05, 'w':0.6}
    optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
    optimizer.optimize(fx.schaffer2, iters=50000)
# Plot the cost
plot_cost_history(optimizer.cost_history)
plt.show()

