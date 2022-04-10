import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.F = []

    
    def set_in_cond(self, x_0, v_0, m, sila, dt, t_max):
        self.m = m
        self.dt = dt
        self.t_max = t_max
        self.sila = sila
        self.t.append(0)
        self.x.append(x_0)
        self.v.append(v_0)
        self.a.append(sila(x_0, v_0, self.dt)/self.m)


    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a.append(self.sila(self.x[-1], self.v[-1], self.t[-1])/self.m)
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.x.append(self.x[-1] + self.v[-1]*self.dt)


    def gibanje(self):
        while self.t[-1] < self.t_max:
            self.__move()
        return self.t, self.x, self.v, self.a