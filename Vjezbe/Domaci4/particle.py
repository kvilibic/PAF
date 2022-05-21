import numpy as np

class Particle:
    def __init__(self, x0, y0, v0, theta, m, rho, Cd, tijelo, dimenzija):
        if tijelo == 1:
            self.A = np.pi*dimenzija**2
        elif tijelo == 2:
            self.A = dimenzija**2
        else:
            print("Greška, varijabla 'tijelo' mora imati vrijednost 1 ili 2")
        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        self.theta = theta
        self.m = m
        self.rho = rho
        self.Cd = Cd
        self.x = [x0]
        self.y = [y0]
        self.t = [0]
        self.vx = [v0*np.cos((theta/360)*2*np.pi)]
        self.vy = [v0*np.sin((theta/360)*2*np.pi)]
        self.ay = [-9.81 - (self.rho*self.Cd* self.A)/(2*self.m)*self.vy[-1]*abs(self.vy[-1])]
        self.ax = [(self.rho*self.Cd*self.A)/(2*self.m)*self.vx[-1]*abs(self.vx[-1])]

    def reset(self):
        self.x = [self.x0]
        self.y = [self.y0]
        self.t = [0]
        self.vx = [self.v0*np.cos((self.theta/360)*2*np.pi)]
        self.vy = [self.v0*np.sin((self.theta/360)*2*np.pi)]
        self.ay = [-9.81 - self.vy[-1]*abs(self.vy[-1])*(self.rho*self.Cd* self.A)/(2*self.m)]
        self.ax = [-self.vx[-1]*abs(self.vx[-1])*(self.rho*self.Cd*self.A)/(2*self.m)]
        
    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
        self.ax.append(-self.vx[-1]*abs(self.vx[-1])*(self.rho*self.Cd*self.A)/(2*self.m))
        self.ay.append(-9.81 - self.vy[-1]*abs(self.vy[-1])*(self.rho*self.Cd* self.A)/(2*self.m))
    
    def gibanje(self, dt):
        self.dt = dt
        while self.y[-1]>=0:
            self.__move()
        return self.x, self.y


    def RK4_ax(self, v, x=0, t=0):
        return - v*abs(v)*(self.rho*self.Cd*self.A)/(2*self.m)

    def RK4_ay(self, v, x=0, t=0):
        return -9.81 - v*abs(v)*(self.rho*self.Cd*self.A)/(2*self.m)

    def __RK4_move(self):
        k1x = self.vx[-1] * self.dt
        k1y = self.vy[-1] * self.dt
        k1vx = self.RK4_ax(self.vx[-1]) * self.dt
        k1vy = self.RK4_ay(self.vy[-1]) * self.dt
        
        k2x = (self.vx[-1] + (k1vx/2)) * self.dt
        k2y = (self.vy[-1] + (k1vy/2)) * self.dt
        k2vx = self.RK4_ax(self.vx[-1] + k1vx/2) * self.dt
        k2vy = self.RK4_ay(self.vy[-1] + k1vy/2) * self.dt
        
        k3x = (self.vx[-1] + (k2vx/2)) * self.dt
        k3y = (self.vy[-1] + (k2vy/2)) * self.dt
        k3vx = self.RK4_ax(self.vx[-1] + k2vx/2) * self.dt
        k3vy = self.RK4_ay(self.vy[-1] + k2vy/2) * self.dt

        k4x = (self.vx[-1] + k3vx) * self.dt
        k4y = (self.vy[-1] + k3vy) * self.dt
        k4vx = self.RK4_ax(self.vx[-1] + k3vx) * self.dt
        k4vy = self.RK4_ay(self.vy[-1] + k3vy) * self.dt

        self.x.append(self.x[-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)
        self.y.append(self.y[-1] + (k1y + 2*k2y + 2*k3y+k4y)/6)
        self.vx.append(self.vx[-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
        self.vy.append(self.vy[-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)

        
    def RK4_gibanje(self, dt):
        self.dt = dt
        while self.y[-1]>=0:
            self.__RK4_move()
        return self.x, self.y


    def domet_o_Cd(self, dt=0.005):
        self.dt = dt
        self.domet = []
        self.Cd_list = [0.01]
        for i in range (250):
            self.Cd = self.Cd_list[-1]
            while self.y[-1]>=0:
                self.__RK4_move()
            self.domet.append(self.x[-1])
            self.Cd_list.append(self.Cd + 0.01)
            self.reset()
        del self.Cd_list[-1]
        return self.domet, self.Cd_list

    def domet_o_m(self, dt=0.005):
        self.dt = dt
        self.domet = []
        self.m_list = [0.01]
        for i in range (500):
            self.m = self.m_list[-1]
            while self.y[-1]>=0:
                self.__RK4_move()
            self.domet.append(self.x[-1])
            self.m_list.append(self.m + 0.01)
            self.reset()
        del self.m_list[-1]
        return self.domet, self.m_list



    def angle_to_hit_target(self, s1, s2, r, dt=0.01):
        self.s1 = s1
        self.s2 = s2
        self.r = r
        self.dt = dt
        self.theta = 0
        pogodak = False
        for i in range (900):
            self.reset()
            while self.y[-1]>=0:
                self.__RK4_move()
                p1 = self.x[-1] - s1
                p2 = self.y[-1] - s2
                if p1**2 + p2**2 <= r**2:
                    pogodak = True
                    break
            if pogodak == True:
                break
            self.theta += 0.1
        if pogodak == False:
            print("Premalena brzina da se pogodi meta.")
            quit()
                


        
        