import random

def Graph:
    def __init__(self, nb_vertex, width=1, height=1):
        self._nb_vertex = nb_vertex
        self._width = width
        self._height = height
        self._vertex = dict()

        for id in range(nb_vertex):
            self._vertex[id] = (random.random()*width, random.random()*height))

    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    def __getitem__(self, key):
        idx = key
        if idx in self._vertex:
            return self._vertex[idx]
        else:
            raise ValueError("vertex does not exist")
