from pso import particle_swarm_optimisation
from ann_criterion import optimality_criterion
from time import time


def H(X):
    if 78<=X[0]<=102 and 33<=X[1]<=45 and 27<=X[2]<=45 and 27<=X[3]<=45 and 27<=X[4]<=45:
        return True
    else:
        return False


def himmelblau(X):
    if G(X) and H(X):
        return 5.3578547 * X[2] * X[2] + 0.8356891 * X[0] * X[4] + 37.293239 * X[0] - 40792.141
    else:
        return 1000000


def g1(X):
    return 85.334407 + 0.0056858 * X[1] * X[4] + 0.0006262 * X[0] * X[3] - 0.0022053 * X[2] * X[4]


def g2(X):
    return 80.51249 + 0.0071317 * X[1] * X[4] + 0.0029955 * X[0] * X[1] - 0.0021813 * X[2] * X[2]


def g3(X):
    return 9.300961 + 0.0047026 * X[2] * X[4] + 0.0012547 * X[0] * X[2] + 0.0019085 * X[2] * X[3]


def G1(X):
    res = g1(X)
    if 0 <= res <= 92:
        return True
    else:
        return False


def G2(X):
    res = g2(X)
    if 90 <= res <= 110:
        return True
    else:
        return False


def G3(X):
    res = g3(X)
    if 20 <= res <= 25:
        return True
    else:
        return False


def G(X):
    if G1(X) and G2(X) and G3(X):
        return True
    else:
        return False


if __name__ == "__main__":
    t1 = time()
    X = particle_swarm_optimisation(himmelblau, 0, 100, maxiter=200, npart=1000, printData=True, dim=5)
    y = himmelblau(X)
    t2 = time()
    print(X)
    print(y)
    print("Potrebno vreme: " + str(t2 - t1))
    print("Ogranicenje g1: " + str(g1(X)))
    print("Ogranicenje g2: " + str(g2(X)))
    print("Ogranicenje g3: " + str(g3(X)))
