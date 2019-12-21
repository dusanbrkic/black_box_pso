from pyswarm import pso
import numpy as np
import json



from ann_criterion import optimality_criterion



if __name__ == "__main__":
    w = list(np.random.uniform(-10, 10, 60))
    lb = [-10]*60
    up = [10]*60

    xopt, fopt = pso(optimality_criterion, lb, up, maxiter=20)
    f = open("rezultati.txt", "a")
    f.write(str(xopt)+"\n"+str(fopt)+"\n")
    f.close()
    print(xopt)
    print(fopt)
