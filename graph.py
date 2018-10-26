import random
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt
from math import exp

class Vertex:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __str__(self):
        return '<{}, {}>'.format(self._x, self._y)
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def next_vertex(self):
        return self._next_vertex


    def dist(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Graph:
    def __init__(self, nb_vertex, width=1, height=1):
        self._nb_vertex = nb_vertex
        self._width = width
        self._height = height
        self._vertex = list()

        for id in range(nb_vertex):
            x = random.random()*width
            y = random.random()*height
            self._vertex.append(Vertex(x, y))

        self.relative_dist = []

        for i in range(nb_vertex):
            temp = []
            for j in range(nb_vertex):
                temp.append(j)
            # self[i].dist(self[j])
            temp.sort(key=(lambda j, i0=i, vertex=self._vertex:vertex[i0].dist(vertex[j])))
            self.relative_dist.append(temp)
            # print(self._vertex[i].dist(self._vertex[temp[1]]))

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
        # idx = key
        # if idx in self._vertex:
        return self._vertex[key]
        # else:
        #     raise ValueError("vertex does not exist")

    def display(self):
        X = np.zeros(self.nb_vertex)
        Y = np.zeros(self.nb_vertex)

        for id in range(self.nb_vertex):
            X[id] = self[id].x
            Y[id] = self[id].y
        plt.scatter(X, Y)
        plt.show()

    def get_nearest_vertex(id_vertex):
        pass



class Solution:
    def __init__(self, graph, path_index = None):
        # La liste de vertex n'est jamais modifiée
        self.graph = graph
        self.vertex = self.graph._vertex
        self.len = len(self.vertex)

        self.path_index = path_index
        if path_index == None:
            self.path_index = list(range(self.len))
            # self.path_index[self.len-1] = 0


    def __getitem__(self, key):
        # if(key > self.len):
        #     raise IndexError()

        if(key == self.len):
            return self.vertex[self.path_index[0]]
        return self.vertex[self.path_index[key]]

    def __setitem__(self, key, val):
        self.vertex[key] = val

    def __str__(self):
        string = ''
        for id in self.path_index:
            string += self.vertex[id].__str__() + '\n'
        return string

    def __copy__(self):
        return Solution(self.graph, self.path_index[:])

    def get_most_distant_vertices_id(self):
        max_dist = -1
        i_max = None
        for i in range(1, self.len):
            new_dist = self[i].dist(self[i+1])
            if new_dist > max_dist:
                max_dist = new_dist
                i_max = i
        return i_max

    def swap(self, i, j):
        self.path_index[i], self.path_index[j] = self.path_index[j], self.path_index[i]
        # self[i], self[j] = self[j], self[i]

    def reverse(self, i, j):
        if i>self.len or j>self.len or i<-1 or j<-1:
            raise IndexError("Indice en dehors des bornes")

        i, j = min(i,j), max(i,j)
        if j-i > self.len-(j-i):
            i, j = j+1, i+self.len-1

        for k in range((j+1-i)//2):
            i1, i2 = (i+k)%self.len, (j-k)%self.len
            self.path_index[i1], self.path_index[i2] = self.path_index[i2], self.path_index[i1]


    def get_edges_dist(self):
        Dist = []
        for i in range(self.len):
            Dist.append(self[i].dist(self[i+1]))
        return Dist

    def cost(self):
        s = 0
        for i in range(len(self.vertex)):
            s += self[i].dist(self[i+1])
        return s

    def randomize_solution(self, grid):
        for i in range(grid.nb_vertex):
            self[i] = grid[i]


if __name__ == '__main__':
    g = Graph(100)
    V = Vertex(2, 4)
    print(V)
    #g.display()
    list_of_vertex = []
    for i in range(g.nb_vertex):
        list_of_vertex.append(g[i])
    sol = Solution(g)
    print(sol)
    print(sol.cost())
    sol2 = sol.disturb(g)
    print(sol2.cost())
    sol3 = sol2.disturb(g)
    print(sol3.cost())
    sol4 = sol3.disturb(g)
    print(sol4.cost())
