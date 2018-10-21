import random
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt

class Vertex:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

class Graph:
    def __init__(self, nb_vertex, width=1, height=1):
        self._nb_vertex = nb_vertex
        self._width = width
        self._height = height
        self._vertex = dict()

        for id in range(nb_vertex):
            x = random.random()*width
            y = random.random()*height
            self._vertex[id] = Vertex(x, y)

    @property
    def width(self):
        return self._width
    @property
    def nb_vertex(self):
        return self._nb_vertex
    @property
    def height(self):
        return self._height
    def __getitem__(self, key):
        idx = key
        if idx in self._vertex:
            return self._vertex[idx]
        else:
            raise ValueError("vertex does not exist")

    def display(self):
        X = np.zeros(self.nb_vertex)
        Y = np.zeros(self.nb_vertex)

        for id in range(self.nb_vertex):
            X[id] = self[id].x
            Y[id] = self[id].y
        plt.scatter(X, Y)
        plt.show()


class Solution:
    def __init__(self, list_of_vertex):
        self.vertex = list_of_vertex

    def __getitem__(self, key):
        id = key
        return self.vertex[id]

    def disturb(self):
        nb_vertex = len(self.vertex)
        id1 = random.randint(0, nb_vertex-1)
        id2 = random.randint(0, nb_vertex-1)
        self.vertex[id1], self.vertex[id2] = self[id2], self[id1]


    def cost(self):
        s = 0
        for i in range(len(self.vertex)-1):
            s += sqrt((self[i+1].x - self[i].x)**2 + (self[i+1].y - self[i].y)**2)
        s += sqrt((self[-1].x - self[0].x)**2 + (self[-1].y - self[0].y)**2)
        return s

    def randomize_solution(self, grid):
        for i in range(grid.nb_vertex):
            self[i] = grid[i]


if __name__ == '__main__':
    g = Graph(100)
    #g.display()
    list_of_vertex = []
    for i in range(g.nb_vertex):
        list_of_vertex.append(g[i])
    sol = Solution(list_of_vertex)
    print(sol.cost())
    sol.disturb()
    print(sol.cost())
    sol.disturb()
    print(sol.cost())
    sol.disturb()
    print(sol.cost())
    sol.disturb()
    print(sol.cost())
