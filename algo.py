from graph import *
from math import exp
from matplotlib import pyplot as plt

def indice_min(liste):
    mini = float('inf')
    n = len(liste)
    indice = 0
    for i in range(n):
        if liste[i]<mini:
            mini = liste[i]
            indice = i

    return indice, mini

class SimulatedAnnealing:
    def __init__(self, alpha, T):
        self._temperature = T
        self._alpha = alpha
        self.solutions = []
        self.costs = []

    @property
    def temperature(self):
        return self._temperature
    @property
    def alpha(self):
        return self._alpha

    def __getitem__(self, key):
        return self.solutions[key]

    def compute(self, grid, previous_solution):

        T = self.temperature
        first_solution = Solution(previous_solution)
        self.solutions.append(first_solution)
        self.costs.append(first_solution.cost())

        while T>1:
            new_solution = self[i-1].disturb(grid)
            new_cost = new_solution.cost()
            if new_cost < self.costs[i-1]:
                print("Good Permutation", new_cost)
                self.solutions.append(new_solution)
                self.costs.append(new_cost)
            else:
                p = random.random()
                if p < exp(-(new_cost-self.costs[i-1])/T):
                    self.solutions.append(new_solution)
                    self.costs.append(new_cost)
                else:
                    self.solutions.append(self[i-1])
                    self.costs[i] = self.costs[i-1]
            T = self.alpha*T
        ind_min, min = indice_min(self.costs)
        return (min, self[ind_min])

    # def multiple_compute(self):
    #
    #     for i in range(100):


if __name__ == '__main__':
    S = SimulatedAnnealing(0.98, 100)

    g = Graph(100)
    first_solution = []
    for i in range(g.nb_vertex):
        first_solution.append(g[i])
    first_solution = Solution(first_solution)

    solutions = []
    costs = []
    for i in range(100):
        cost, first_solution = S.compute(g, first_solution.vertex)
        costs.append(cost)
        solutions.append(first_solution)
        print(cost)

    ind_sol, cost = indice_min(costs)
    solution = solutions[ind_sol]

    print(str(cost) + '\n')
    print(solution)
    X = []
    Y = []
    for vertex in solution:
        X.append(vertex.x)
        Y.append(vertex.y)
    plt.plot(X, Y)
    g.display()
