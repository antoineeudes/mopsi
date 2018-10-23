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
    def __init__(self, alpha, T, grid):
        self._temperature = T
        self._alpha = alpha
        self.solutions = []
        self.costs = []

        first_solution = []
        for i in range(grid.nb_vertex):
            first_solution.append(grid[i])
        self.min_solution = Solution(first_solution)

    @property
    def temperature(self):
        return self._temperature
    @property
    def alpha(self):
        return self._alpha
    @property
    def cost(self):
        return self.cost

    # @property
    # def min_solution(self):
    #     return self._min_solution
    # @min_solution.setter
    # def min_solution(self, sol):
    #     self._cost = sol.cost()
    #     self._solution = sol

    def __getitem__(self, key):
        return self.solutions[key]

    def compute(self, grid, previous_solution):

        T = self.temperature
        first_solution = Solution(previous_solution)
        self.solutions.append(first_solution)
        self.costs.append(first_solution.cost())
        i = 0
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
            i += 1
        ind_min, min = indice_min(self.costs)
        return (min, self[ind_min])

    def compute2(self, start_solution = None):

        if(start_solution != None):
            self.min_solution = start_solution
        T = self.temperature
        current_solution = self.min_solution

        while T>0.1:
            new_solution = current_solution.disturb2()
            new_cost, current_cost = new_solution.cost(), current_solution.cost()
            p = random.random()

            if p < exp(-max(0,new_cost-current_cost)/T):
                current_solution = new_solution
            if current_solution.cost() < self.min_solution.cost():
                self.min_solution = current_solution

            T = self.alpha*T

        return self.min_solution

    # def multiple_compute(self):
    #
    #     for i in range(100):


if __name__ == '__main__':
    g = Graph(100)
    S = SimulatedAnnealing(0.4, 100, g)
    min_solution = S.compute2()

    for i in range(1000):
        solution = S.compute2()
        print(min_solution.cost())
        if(solution.cost() < min_solution.cost()):
            min_solution = solution


    print(str(min_solution.cost()) + '\n')
    print(min_solution)
    X = []
    Y = []
    for vertex in min_solution:
        X.append(vertex.x)
        Y.append(vertex.y)
    plt.plot(X, Y)
    g.display()
