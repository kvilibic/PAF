class ProjectileDrop:
    def __init__(self, h, vx):
        self.h = h
        self.vx0 = vx
        self.t = [0]
        self.x = [self.t[-1]*self.vx0]
        self.y = [self.h]
        self.vx = [self.vx0]
        self.vy = [0]
        print("Objekt uspjesno stvoren. Visina je jednaka {} m, a brzina {} m/s.".format(h, vx))

    
    def reset(self):
        self.x = [self.t[-1]*self.vx[0]]
        self.y = [self.h]
        self.vx = [self.vx[0]]
        self.vy = [0]
        self.t = [0]


    def change_h(self,h):
        self.h = h


    def change_vx(self, dvx):
        self.vx0 += dvx

    
    def __move(self):
        a = -9.81
        self.t.append(self.t[-1] + self.dt)
        self.vx.append(self.vx[-1])
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.vy.append(self.vy[-1] + a*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)   
        

    def putanja(self, dt):
        self.dt = dt
        while (self.y[-1]>=0):
            self.__move()
        return self.x, self.y, self.vy, self.t

    
    def ovisnosti(self):
        dtlist = [0.001]
        tlist = []
        for i in range (100):
            self.putanja(dtlist[-1])
            tlist.append(self.t[-1])
            self.reset()
            dtlist.append(dtlist[-1]+0.001)
        del dtlist[-1]
        return tlist, dtlist
            
    
    def meta(self, x, r):
        x1 = x - r/2
        x2 = x + r/2
        pogodak = False
        t0 = 0
        while pogodak == False:
            self.putanja(0.1)
            if self.x[-1] >= x1 and self.x[-1] <= x2:
                pogodak = True
                print("Meta pogodena!")
                t_pogodak = t0
            else:
                self.reset()
                t0 += 0.1
                self.t = [t0]
        return t_pogodak, self.x, self.y


    def __move_vjetar(self):
        ay = -9.81
        self.t.append(self.t[-1] + self.dt)
        self.vx.append(self.vx[-1] + self.ax*self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.vy.append(self.vy[-1] + ay*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt) 


    def putanja_vjetar(self, dt):
        self.dt = dt
        while (self.y[-1]>=0):
            self.__move_vjetar()
        return self.x, self.y, self.vy, self.t


    def meta_vjetar(self, x, r, vjetar):
        self.ax = vjetar
        x1 = x - r/2
        x2 = x + r/2
        pogodak = False
        t0 = 0
        while pogodak == False:
            self.putanja_vjetar(0.1)
            if self.x[-1] >= x1 and self.x[-1] <= x2:
                pogodak = True
                t_pogodak = t0
            else:
                self.reset()
                t0 += 0.1
                self.t = [t0]
        return t_pogodak, self.x, self.y