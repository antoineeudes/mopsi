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


def MeanLaw(path="lawmean.txt", nb_iter=100, nb_acquisition=100):
    fichier = open(path, 'w')
    for i in range(5, nb_acquisition+5):
        s = 0.
        for j in range(nb_iter):

            g = graph.Graph()
            g.randomize(i)
            min_solution = Solution(g)


            S = SimulatedAnnealing_log(min_solution)

            time0 = time.time()

            min_solution = S.compute(show=False)

            # print("Cout final reel : {}".format(graph.real_cost(min_solution)))
            # print("Calculs de distances : {}".format(graph.nb_dist))
            # print("Temps : {}".format(time.time()-time0))

            s += min_solution.cost()
        s = s/nb_iter
        line = str(i) + "\t" + str(s) + "\n"
        fichier.write(line)
    fichier.close()

if __name__ == "__main__":

    MeanLaw()
