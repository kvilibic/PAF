import numpy as np

G = 6.67408*10**(-11)

class Planet:
    def __init__(self, m, x0, y0, v0):
        self.m = m
        self.v0 = v0
        self.x0 = x0
        self.y0 = y0
        if self.y0 == 0:
            self.theta = 0
        else:
            self.theta = np.arctan(self.x0/self.y0)
        self.x = [self.x0]
        self.y = [self.y0]
        self.v = np.array([self.v0*np.sin(self.theta), self.v0*np.cos(self.theta)])
        self.a = np.array([0., 0.])

class Svemir:
    def __init__(self):
        self.planets = []
        self.t = 0

    def addplanet(self, Planet):
        self.planets.append(Planet)

    def __move(self):
        for promatrani in self.planets:
            F = np.array([0., 0.])
            for ostali in self.planets:
                if ostali != promatrani:
                    rx = promatrani.x[-1]-ostali.x[-1]
                    ry = promatrani.y[-1]-ostali.y[-1]
                    r = np.sqrt(rx**2 + ry**2)
                    F[0] += -G*promatrani.m*ostali.m/(r**2) * (rx/r)
                    F[1] += -G*promatrani.m*ostali.m/(r**2) * (ry/r)
            promatrani.a = np.array([F[0]/promatrani.m, F[1]/promatrani.m])
            promatrani.v = np.array([promatrani.v[0] + promatrani.a[0]*self.dt, promatrani.v[1] + promatrani.a[1]*self.dt])
            promatrani.x.append(promatrani.x[-1] + promatrani.v[0]*self.dt)
            promatrani.y.append(promatrani.y[-1] + promatrani.v[1]*self.dt)
        self.t += self.dt
    
    def evolve(self, vrijeme, dt):
        self.dt = dt
        godina = 365.242*24*60*60
        while self.t < vrijeme:
            self.__move()
            

            
                    

    