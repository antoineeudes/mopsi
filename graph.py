import random
from matplotlib import pyplot as plt
import numpy as np

class Graph:
    def __init__(self, nb_vertex, width=1, height=1):
        self._nb_vertex = nb_vertex
        self._width = width
        self._height = height
        self._vertex = dict()

        for id in range(nb_vertex):
            self._vertex[id] = (random.random()*width, random.random()*height)

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
            X[id] = self[id][0]
            Y[id] = self[id][1]
        plt.scatter(X, Y)
        plt.show()

if __name__ == '__main__':
    g = Graph(100)
    g.display()
