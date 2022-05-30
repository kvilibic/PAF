import numpy as np

class Particle:
    def __init__(self, Q, m, v, E, B):
        self.Q = Q
        self.m = m
        self.v = v
        self.E = E
        self.B = B
        self.x = [0.]
        self.y = [0.]
        self.z = [0.]
        self.t = [0.]
    
    def reset(self):
        self.x = [0.]
        self.y = [0.]
        self.z = [0.]
        self.t = [0.]

    def RK4_a(self, v):
        return self.Q/self.m*(self.E + np.cross(self.v, self.B(self.t)))

    def __RK4_move(self):
        k1v = self.RK4_a(self.v) * self.dt
        k1xyz = self.v * self.dt 
        k2v = self.RK4_a(self.v + k1v/2) * self.dt
        k2xyz = (self.v + k2v/2) * self.dt
        k3v = self.RK4_a(self.v + k2v/2) * self.dt
        k3xyz = (self.v + k2v/2) * self.dt
        k4v = self.RK4_a(self.v + k3v) * self.dt
        k4xyz = (self.v + k3v) * self.dt

        self.x.append(self.x[-1] + (k1xyz[0] + 2*k2xyz[0] + 2*k3xyz[0] + k4xyz[0])/6)
        self.y.append(self.y[-1] + (k1xyz[1] + 2*k2xyz[1] + 2*k3xyz[1] + k4xyz[1])/6)
        self.z.append(self.z[-1] + (k1xyz[2] + 2*k2xyz[2] + 2*k3xyz[2] + k4xyz[2])/6)
        self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
        self.t.append(self.t[-1]+self.dt)

    def RK4_gibanje(self, dt):
        self.dt = dt
        while self.t[-1] < 10:
            self.__RK4_move()

