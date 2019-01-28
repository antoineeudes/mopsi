from algo import *
from config import PATH_LAW_SALESMAN


if __name__ == "__main__":

    for i in range(10, 500, 2):
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
