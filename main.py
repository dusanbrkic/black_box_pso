from pyswarm import pso
import numpy as np



from ann_criterion import optimality_criterion



if __name__ == "__main__":
    w = list(np.random.uniform(-10, 10, 60))
    lb = [-10]*60
    up = [10]*60

    xopt, fopt = pso(optimality_criterion, lb, up, maxiter=20)
    print(xopt)
    print(fopt)
