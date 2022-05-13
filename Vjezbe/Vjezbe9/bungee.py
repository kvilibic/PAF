class Bungee:
    def __init__(self, h, l, m, k, otpor):
        self.otpor = otpor
        self.h = h
        self.l = l
        self.k = k
        self.m = m
        self.Ep = [self.m*9.81*self.h]
        self.Ek = [0]
        self.Eel = [0]
        self.Euk = [self.m*9.81*self.h]
        self.t = [0]
        self.y = [self.h]
        self.v = [0]
        self.a = [-9.81]

    def reset(self):
        self.Ep = [self.m*9.81*self.h]
        self.Ek = [0]
        self.Eel = [0]
        self.Euk = [self.m*9.81*self.h]
        self.t = [0]
        self.y = [self.h]
        self.v = [0]
        self.a = [0]

    def __move(self):
        if self.y[-1] < (self.h-self.l):
            F_el = self.k*(self.h-self.l-self.y[-1])
            self.Eel.append(0.5*self.k*(self.h-self.l-self.y[-1])**2)
        else:
            F_el = 0
            self.Eel.append(0)
        F_g = self.m*(-9.81)
        self.t.append(self.t[-1] + self.dt)
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        if self.otpor == True:
            F_otp = (-self.v[-1]*abs(self.v[-1])*1*0.1*0.5*1.22)
        else:
            F_otp = 0
        self.a.append((F_el+F_g+F_otp)/self.m)
        self.y.append(self.y[-1] + self.v[-1]*self.dt)

        self.Ep.append(self.m*9.81*self.y[-1])
        self.Ek.append(0.5*self.m*self.v[-1]**2)
        self.Euk.append(self.Ep[-1]+self.Ek[-1]+self.Eel[-1])

        #Sila otpora = predznak*v^2*C*povrsina presjeka*0.5*gustoca zraka

    def gibanje(self, dt=0.001):
        self.dt = dt
        while (self.t[-1]<=50):
            self.__move()
            
            

