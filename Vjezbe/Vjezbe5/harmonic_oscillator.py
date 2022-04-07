import matplotlib.pyplot as plt
import numpy as np
import math

class HarmonicOscillator:
    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []

    
    def set_in_cond(self, x_0, m, k, dt, t_max):
        self.t.append(0)
        self.x.append(x_0)
        self.v.append(0)
        self.a.append((-k/m)*x_0)
        self.Amp = x_0
        self.m = m
        self.k = k
        self.dt = dt
        self.t_max = t_max
        self.period_an = 2*np.pi/np.sqrt(k/m)
 

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a.append((-self.k/self.m)*self.x[-1])
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.x.append(self.x[-1] + self.v[-1]*self.dt)


    def putanja(self):
        while self.t[-1] < self.t_max:
            self.__move()
        return self.t, self.x, self.v, self.a

    
    def analitical(self):
        t_an = np.linspace(0, 10, 10000)
        for i in t_an:
            self.x.append(self.Amp*math.cos(math.sqrt(self.k/self.m)*i))
            self.v.append(-self.Amp*math.sqrt(self.k/self.m)*math.sin(math.sqrt(self.k/self.m)*i))
            self.a.append(-self.Amp*(self.k/self.m)*math.cos(math.sqrt(self.k/self.m)*i))
        del self.x[-1], self.v[-1], self.a[-1]
        return t_an, self.x, self.v, self.a
            

    def plot_trajectory(self):
        plt.plot(self.t, self.x)
        plt.xlabel("t [s]", loc='right')
        plt.ylabel("x [m]", loc='top')
        plt.grid()
        plt.show()

        plt.plot(self.t, self.v)
        plt.xlabel("t [s]", loc='right')
        plt.ylabel("v [m/s]", loc='top')
        plt.grid()
        plt.show()

        plt.plot(self.t, self.a)
        plt.xlabel("t [s]", loc='right')
        plt.ylabel("a [m/s2]", loc='top')
        plt.grid()
        plt.show()


    def period(self):
        while self.v[-1] <= 0:
            self.__move()
        while self.v[-1] > 0:
            self.__move()
        print("Period uz korak {} s je jednak {:.4f} s, analitiči period iznosi {:.4f} s. ".format(self.dt, self.t[-1], self.period_an))


