import glob
import numpy as np
import matplotlib.pyplot as plt
a =[]
for i in glob.glob('*.dat'):
    a.append(i)
b= []
c= []
for i in a:
    x,y = np.loadtxt(fname = i,unpack = True)
    b.extend(x.tolist())
    c.extend(y.tolist())

plt.xlim((0, 8))
plt.ylim((0, 3000))
plt.figure(figsize=(10,8))
plt.xlabel('Dimension')
plt.ylabel('Distance from origin')
plt.scatter(b,c)
plt.savefig('rw_results.png')

