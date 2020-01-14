from pyswarm import pso
import numpy as np
import json
from pso import particle_swarm_optimisation



from ann_criterion import optimality_criterion



if __name__ == "__main__":
    X = particle_swarm_optimisation(optimality_criterion, -10, 10)
    y = optimality_criterion(X)
    print(y)
