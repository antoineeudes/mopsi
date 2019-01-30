from algo import *
from config import PATH_LAW_SALESMAN
from copy import deepcopy
from matplotlib import pyplot as plt


def savePlot(path):
    fichier = open(path, 'r')
    X = []
    Y = []
    for line in fichier:
        M = deepcopy(line.strip().split('\t'))
        X.append(float(M[0]))
        Y.append(float(M[1]))

    fichier.close()
    plt.plot(X, Y)
    plt.grid()
    plt.savefig(path+".png")
    plt.show()


def MeanLaw(path):
    return
        # string = line.strip().split('\t')

if __name__ == "__main__":

    # savePlot("./data/solution/law.txt")
    for i in range(10, 2000, 2):
        g = graph.Graph()
        g.randomize(i)
        min_solution = Solution(g)

        # S = SimulatedAnnealing_exp(min_solution, 0.1, 0.99999)
        # S = SimulatedAnnealing_exp(min_solution)
        S = SimulatedAnnealing_log(min_solution)
        # S = SimulatedAnnealing_repeated(min_solution, 100, 0.9, 10000)

        # X, Y = [], []
        # print(graph.nb_dist)
        # for vertex in min_solution:
        #     X.append(vertex.x)
        #     Y.append(vertex.y)
        # plt.plot(X, Y)
        # g.display()

        time0 = time.time()

        min_solution = S.compute()

        print("Cout final reel : {}".format(graph.real_cost(min_solution)))
        print("Calculs de distances : {}".format(graph.nb_dist))
        print("Temps : {}".format(time.time()-time0))

        # X, Y = [], []
        # for vertex in min_solution:
        #     X.append(vertex.x)
        #     Y.append(vertex.y)
        # plt.plot(X, Y)
        # g.display()

        min_solution.write()
