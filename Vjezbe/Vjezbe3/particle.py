import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.v_y = []
        self.v_x = []
        self.a_x = []
        self.a_y = []

    
    def set_in_cond(self, v_0, theta, x_0, y_0, dt):
        self.t.append(0)
        self.x.append(x_0)
        self.y.append(y_0)
        self.v_x.append(v_0*np.cos((theta/360)*2*np.pi))
        self.v_y.append(v_0*np.sin((theta/360)*2*np.pi))
        self.a_x.append(0)
        self.a_y.append(-9.81)
        self.dt = dt
        self.v_0 = v_0
        self.theta = theta


    def reset(self):
        self.__init__()


    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.v_x[-1]*self.dt)
        self.v_x.append(self.v_x[-1])
        self.a_x.append(0)
        self.y.append(self.y[-1] + self.v_y[-1]*self.dt)
        self.v_y.append(self.v_y[-1] + self.a_y[-1]*self.dt)
        self.a_y.append(-9.81)

    
    def range(self):
        while (self.y[-1]>=0):
            self.__move()
        return(self.x[-1])

    
    def range_analitical(self):
        self.d = (self.v_0**2)/9.81*np.sin((2*(self.theta/360)*2*np.pi))
        return self.d



    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.xlabel("x [m]", loc='right')
        plt.ylabel("y [m]", loc='top')
        plt.grid()

        plt.show()

         
