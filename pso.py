import numpy as np

class Paricle():
    def __init__(self, lb, ub, dim):
        self.pozicija = np.random.uniform(low=lb, high=ub, size=dim)
        self.vektor = np.full(dim, 0, dtype=float)
        self.y = np.Inf
        self.najbolji_X = self.pozicija
        self.najbolji_y = self.y





def particle_swarm_optimisation(funkcija, lowerb, upperb, maxiter=20, npart = 50, dim=60):

    w = 1
    dmp = 0.99
    c1 = 2
    c2 = 2
    #Inicijalizacija
    particles = []
    globalno_najbolji_X = "Neka najbolji pobedi"
    globalno_najbolji_y = np.Inf
    for k in range(dim):
        p = Paricle(lowerb, upperb, dim)
        p.y = funkcija(p.pozicija)
        particles.append(p)
        if p.y<globalno_najbolji_y:
            globalno_najbolji_X = p.pozicija
            globalno_najbolji_y = p.y

    #glavna petlja

    for i in range(maxiter):
        for j in range(len(particles)):
            particles[j].vektor = w*particles[j].vektor + c1*np.random.uniform(size=dim)*(particles[j].najbolji_X - particles[j].pozicija)+c2*np.random.uniform(size=dim)*(globalno_najbolji_X-particles[j].pozicija)

            particles[j].pozicija = particles[j].pozicija + particles[j].vektor

            particles[j].y = funkcija(particles[j].pozicija)

            if particles[j].y < particles[j].najbolji_y:
                particles[j].najbolji_X = particles[j].pozicija
                particles[j].najbolji_y = particles[j].y
                if particles[j].y < globalno_najbolji_y:
                    globalno_najbolji_X = particles[j].pozicija
                    globalno_najbolji_y = particles[j].y
            w = w*dmp
    return globalno_najbolji_X
