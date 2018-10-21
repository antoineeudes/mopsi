from graph import *
from math import exp

class SimulatedAnnealing:
    def __init__(self, nb_iteration, alpha, T):
        self._temperature = T
        self._alpha = alpha
        self._nb_iteration = nb_iteration
        self.solutions = []
        self.costs = np.zeros(nb_iteration+1)

    @property
    def temperature(self):
        return self._temperature
    @property
    def nb_iteration(self):
        return self._nb_iteration
    @property
    def alpha(self):
        return self._alpha

    def __getitem__(self, key):
        return self.solutions[key]

    def compute(self, grid):

        T = self.temperature
        first_solution = Solution(grid)
        self.solutions.append(first_solution)
        self.costs[0] = first_solution.cost()

        for i in range(1, self.nb_iteration+1):
            print(i)
            new_solution = self[i-1].disturb(grid)
            new_cost = new_solution.cost()
            if new_cost < self.costs[i-1]:
                self.solutions.append(new_solution)
                self.costs[i] = new_cost
            else:
                p = random.random()
                if p < exp(-(new_cost-self.costs[i-1])/T):
                    self.solutions.append(new_solution)
                    self.costs[i] = new_cost
                else:
                    self.solutions.append(self[i-1])
                    self.costs[i] = self.costs[i-1]
            T = self.alpha*T
        return (min(self.costs))

if __name__ == '__main__':
    S = SimulatedAnnealing(100, 0.9, 1000)
    cost = S.compute(Graph(100))
    print(cost)
