from pso import particle_swarm_optimisation
from ann_criterion import optimality_criterion
from time import time

if __name__ == "__main__":
    t1 = time()
    X = particle_swarm_optimisation(optimality_criterion, -10, 10, maxiter=100, npart=240, printData=True)
    y = optimality_criterion(X)
    t2 = time()
    print(X)
    print(y)
    print("Potrebno vreme: " + str(t2-t1))
