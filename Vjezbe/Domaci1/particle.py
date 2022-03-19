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


    ###################################
    ############ ZADATAK 1 ############
    ###################################
    
    def total_time(self):
        self.range()
        self.t_uk = self.t[-1]

    
    def max_speed(self):
        self.v_max = 0
        for i in range(len(self.t)):
            self.v = np.sqrt(self.v_x[i]**2 + self.v_y[i]**2)
            if self.v > self.v_max:
                self.v_max = self.v

    
    def velocity_to_hit_target(self, theta, x_0, y_0, s1, s2, r):
        v_0 = 0
        self.theta = theta
        self.v_0_pogodak = []
        for i in range(1000):
            pogodak = False
            self.t = [0]
            self.x = [x_0]
            self.y = [y_0]
            self.v_x = [v_0*np.cos((theta/360)*2*np.pi)]
            self.v_y = [v_0*np.sin((theta/360)*2*np.pi)]
            self.a_x = [0]
            self.a_y = [-9.81]
            while (self.y[-1]>=0):
                self.__move()
                p1 = self.x[-1] - s1
                p2 = self.y[-1] - s2
                if p1**2 + p2**2 <= r**2:
                    pogodak = True
            if pogodak == True:
                self.v_0_pogodak.append(v_0)
            v_0 += 0.1
        

    def angle_to_hit_target(self, v_0, x_0, y_0, s1, s2, r):
        theta = 0
        self.v_0 = v_0
        self.theta_pogodak = []
        for i in range(900):
            pogodak = False
            self.t = [0]
            self.x = [x_0]
            self.y = [y_0]
            self.v_x = [v_0*np.cos((theta/360)*2*np.pi)]
            self.v_y = [v_0*np.sin((theta/360)*2*np.pi)]
            self.a_x = [0]
            self.a_y = [-9.81]
            while (self.y[-1]>=0):
                self.__move()
                p1 = self.x[-1] - s1
                p2 = self.y[-1] - s2
                if p1**2 + p2**2 <= r**2:
                    pogodak = True
            if pogodak == True:
                self.theta_pogodak.append(theta)
            theta += 0.1
        

    ###################################
    ############ ZADATAK 2 ############
    ###################################
    
    def ovisnosti(self, v_0, x_0, y_0):
        self.v_0 = v_0
        dometi = []
        trajanja = []
        kutevi = [0]
        for i in range(900):
            pogodak = False
            self.t = [0]
            self.x = [x_0]
            self.y = [y_0]
            self.v_x = [v_0*np.cos((kutevi[i]/360)*2*np.pi)]
            self.v_y = [v_0*np.sin((kutevi[i]/360)*2*np.pi)]
            self.a_x = [0]
            self.a_y = [-9.81]
            while (self.y[-1]>=0):
                self.__move()
            dometi.append(self.x[-1])
            trajanja.append(self.t[-1])
            kutevi.append(kutevi[-1] + 0.1)
        del kutevi[-1]
        
        fig, axs = plt.subplots(2)
        fig.subplots_adjust(hspace=1)
    
        axs[0].plot(kutevi, trajanja)
        axs[0].set_title("Ovisnost trajanja hica o kutu")
        axs[0].grid()
        axs[0].set_xlabel("theta [°]", loc='right')
        axs[0].set_ylabel("t [s]", loc='top')

        axs[1].plot(kutevi, dometi)
        axs[1].set_title("Ovisnost dometa o kutu")
        axs[1].grid()
        axs[1].set_xlabel("theta [°]", loc='right')
        axs[1].set_ylabel("domet [m]", loc='top')

        plt.show()