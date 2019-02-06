from algo import *
from config import PATH_LAW_SALESMAN
from copy import deepcopy
from matplotlib import pyplot as plt
from math import sqrt


def savePlot(path):
    fichier = open(path, 'r')
    X = []
    Y = []
    Z = []
    for line in fichier:
        M = deepcopy(line.strip().split('\t'))
        X.append(float(M[0]))
        Y.append(float(M[1]))
        Z.append(0.83*sqrt(float(M[0])))

    fichier.close()
    plt.plot(X, Y, color="blue")
    plt.plot(X, Z, color="red")

    plt.xlabel('n')
    plt.ylabel('simulation de E(L_n)')
    plt.legend(('simulation', 'gamma*sqrt(n)'))
    plt.grid()
    plt.savefig(path+".png")
    plt.show()

def findGamma(path):
    fichier = open(path, 'r')
    X = []
    Y = []
    Z = []
    for line in fichier:
        M = deepcopy(line.strip().split('\t'))
        X.append(float(M[0]))
        Y.append(float(M[1])/sqrt(float(M[0])))

    fichier.close()
    plt.plot(X, Y, color="blue")
    print(Y[-1])

    plt.xlabel('n')
    plt.ylabel('simulation de E(L_n)/sqrt(n)')
    plt.ylim(0.5, 1.25)
    plt.grid()
    plt.savefig(path+"gamma.png")
    plt.show()


def MeanLaw(path="./data/solution/lawmean1.txt", nb_iter=40, nb_acquisition=200):
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

    # MeanLaw()
    # findGamma("./data/solution/lawmean.txt")
    savePlot("./data/solution/lawmean.txt")
