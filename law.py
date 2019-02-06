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


def MeanLaw(path="./data/solution/lawmean1.txt", nb_iter=30, nb_acquisition=100):
    fichier = open(path, 'w')
    for i in range(5, nb_acquisition+5):
        print("acquisition", i)
        s = 0.
        for j in range(nb_iter):
            print("iter", j)

            g = graph.Graph()
            g.randomize(i)
            min_solution = Solution(g)


            S = SimulatedAnnealing_log(min_solution)

            min_solution = S.compute(show=False)

            s += min_solution.cost()
        del g
        del S
        del min_solution
        s = s/nb_iter
        line = str(i) + "\t" + str(s) + "\n"
        fichier.write(line)
    fichier.close()

if __name__ == "__main__":

    MeanLaw()
    # savePlot("./data/solution/lawmean.txt")
