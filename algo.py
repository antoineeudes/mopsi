import graph
import random
from graph import Solution
from math import exp
from math import log
from matplotlib import pyplot as plt
import copy

def indice_min(liste):
    mini = float('inf')
    n = len(liste)
    indice = 0
    for i in range(n):
        if liste[i]<mini:
            mini = liste[i]
            indice = i

    return indice, mini


def disturb(sol):
    s2 = copy.copy(sol)
    id1 = random.randint(0, sol.len-1)
    id2 = random.randint(0, sol.len-1)
    s2.swap(id1, id2)
    return s2

def disturb2(sol):
    s2 = copy.copy(sol)
    id1 = random.randint(0, sol.len-1)
    i_max = sol.get_most_distant_vertices_id()
    s2.swap(i_max, id1)

    return s2

def disturb3(sol):
    s2 = copy.copy(sol)
    id1 = random.randint(0, sol.len-1)

    Dist = sol.get_edges_dist()
    # max_dist = max(Dist)
    for i in range(sol.len):
        p = random.random()
        if p < 1-exp(-Dist[i]/3):
            s2.swap(i, id1)
            # print("Trouvé")
            return s2
        # print("Pas pris")

    print("Permutation aléatoire")
    id2 = random.randint(0, sol.len-1)
    s2.swap(id1, id2)
    return s2

def disturb4(sol):
    s2 = copy.copy(sol)
    i_max = sol.get_most_distant_vertices_id()
    # s2.path_index[2]=5
    return s2

def disturb_reverse(sol):
    s2 = copy.copy(sol)
    id1 = random.randint(0, sol.len-1)
    id2 = random.randint(0, sol.len-1)
    s2.reverse(id1, id2)
    return s2




class SimulatedAnnealing:
    def __init__(self, alpha, T, grid, disturb_function):
        self._temperature = T
        self._alpha = alpha
        self.solutions = []
        self.costs = []

        self.disturb_function = disturb_function

        self.min_solution = Solution(grid)

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


    def compute(self, start_solution = None):

        if(start_solution != None):
            self.min_solution = start_solution
        T = self.temperature
        current_solution = self.min_solution
        i = 2
        while T>10:
            # print(T)
            current_cost = current_solution.cost()
            new_solution = self.disturb_function(current_solution)
            new_cost = new_solution.cost()
            p = random.random()

            if p < exp(-max(0,new_cost-current_cost)/T):
                current_solution = new_solution
                if current_solution.cost() < self.min_solution.cost():
                    self.min_solution = current_solution

            T = self.alpha*T
            # T = 100/log(i)
            i += 1

        return self.min_solution

if __name__ == '__main__':
    g = graph.Graph(100)
    S = SimulatedAnnealing(0.8, 100, g, disturb_reverse)
    min_solution = S.compute()

    for i in range(50000):
        solution = S.compute()
        print(min_solution.cost())
        if(solution.cost() < min_solution.cost()):
            min_solution = solution


    print(str(min_solution.cost()) + '\n')
    # print(min_solution)
    X = []
    Y = []
    print(graph.nb_dist)
    for vertex in min_solution:
        X.append(vertex.x)
        Y.append(vertex.y)
    plt.plot(X, Y)
    g.display()
