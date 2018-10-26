from graph import *
from algo import *
import numpy as np
from matplotlib import pyplot as plt


g = Graph(100)
costs = np.zeros(9)
j = 0
for alpha in np.linspace(0.7, 0.95, 3):

    for T in np.linspace(100, 1000, 3):
        print('alpha = '+ str(alpha))
        print('T = ' + str(T))
        S = SimulatedAnnealing(alpha, T, g)
        min_solution = S.compute()

        for i in range(1000):
            solution = S.compute()
            print(min_solution.cost())
            if(solution.cost() < min_solution.cost()):
                min_solution = solution

        costs[j] = min_solution.cost()
        j += 1

print(costs)

x=np.unique(np.linspace(0.7, 0.95, 3))
y=np.unique(np.linspace(100, 1000, 3))
X,Y = np.meshgrid(x,y)

Z=costs.reshape(len(y),len(x))
print(Z)

plt.pcolormesh(X,Y,Z)

plt.show()
