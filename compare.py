import algo
import graph
from graph import Solution
from algo import SimulatedAnnealing_log, SimulatedAnnealing_repeated, SimulatedAnnealing_step
import time
from matplotlib import pyplot as plt
import copy
import numpy as np


if __name__ == '__main__':

    X_log = []
    Y_log = []
    X_repeated = []
    Y_repeated = []
    X_step = []
    Y_step = []

    X_log_mean = []
    Y_log_mean = []
    X_repeated_mean = []
    Y_repeated_mean = []
    X_step_mean = []
    Y_step_mean = []

    for n in range(10, 251, 10):
        # X.append(n)

        for nb_graph in range(1, 10):
            g = graph.Graph()
            g.randomize(n)
            start_solution = Solution(g)

            #Décroissance log
            print("LOG")
            min_solution = copy.copy(start_solution)

            S = SimulatedAnnealing_log(min_solution, T=0.1)

            time0 = time.time()

            min_solution = S.compute(show=False)

            print("Cout final reel : {}".format(graph.real_cost(min_solution)))
            print("Calculs de distances : {}".format(graph.nb_dist))
            print("Temps : {}".format(time.time()-time0))
            X_log.append(time.time()-time0)
            Y_log.append(graph.real_cost(start_solution)-graph.real_cost(min_solution))
            # Y_log.append((graph.real_cost(start_solution)-graph.real_cost(min_solution))/(time.time()-time0))

            # Décroissance exp répétée
            print("REPEATED")
            min_solution = copy.copy(start_solution)

            S = SimulatedAnnealing_repeated(min_solution, 0.1, 0.9, 100000)

            time0 = time.time()

            min_solution = S.compute(show=False)

            print("Cout final reel : {}".format(graph.real_cost(min_solution)))
            print("Calculs de distances : {}".format(graph.nb_dist))
            print("Temps : {}".format(time.time()-time0))
            X_repeated.append(time.time()-time0)
            Y_repeated.append(graph.real_cost(start_solution)-graph.real_cost(min_solution))
            # Y_repeated.append((graph.real_cost(start_solution)-graph.real_cost(min_solution))/(time.time()-time0))

            # Décroissance par paliers
            print("STEPS")
            min_solution = copy.copy(start_solution)

            S = SimulatedAnnealing_step(min_solution, 0.1, 200, 0.9)

            time0 = time.time()

            min_solution = S.compute(show=False)

            print("Cout final reel : {}".format(graph.real_cost(min_solution)))
            print("Calculs de distances : {}".format(graph.nb_dist))
            print("Temps : {}".format(time.time()-time0))
            X_step.append(time.time()-time0)
            Y_step.append(graph.real_cost(start_solution)-graph.real_cost(min_solution))
            # Y_step.append((graph.real_cost(start_solution)-graph.real_cost(min_solution))/(time.time()-time0))

        X_log_mean.append(np.mean(X_log))
        Y_log_mean.append(np.mean(Y_log))
        X_repeated_mean.append(np.mean(X_repeated))
        Y_repeated_mean.append(np.mean(Y_repeated))
        X_step_mean.append(np.mean(X_step))
        Y_step_mean.append(np.mean(Y_step))
        X_log = []
        Y_log = []
        X_repeated = []
        Y_repeated = []
        X_step = []
        Y_step = []

    # plt.plot(X, Y_log, label='log')
    # plt.plot(X, Y_repeated, label='repeated')
    # plt.plot(X, Y_step, label='step')
    # plt.legend()
    # plt.show()

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter(X_log_mean, Y_log_mean, s=10, c='b', marker="s", label='Log')
    ax1.scatter(X_repeated_mean, Y_repeated_mean, s=10, c='r', marker="o", label='Exp répétée')
    ax1.scatter(X_step_mean, Y_step_mean, s=10, c='g', marker="o", label='Exp par paliers')
    plt.legend(loc='upper left');
    plt.show()
