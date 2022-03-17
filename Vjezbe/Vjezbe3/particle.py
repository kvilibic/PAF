import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v_0, theta, x_0, y_0):
        self.v_0 = v_0
        self.theta = (theta/360)*2*np.pi
        self.x_0 = x_0
        self.y_0 = y_0
        self.x = x_0
        self.y = y_0
        

    def reset():
        del self.v_0
        del self.theta
        del self.x_0
        del self.y_0


    def move(dt):
        vx = v0*np.cos((theta/360)*2*np.pi)
        vy = v0*np.sin((theta/360)*2*np.pi)
        x = x + vx*dt
        y = y + vy*dt
        self.x = x
        self.y = y
        print("Nove koordinate su ",x,y)

    
    def range(self):
        v0x = v0*np.cos((theta/360)*2*np.pi)
        v0y = v0*np.sin((theta/360)*2*np.pi)
        t = [0.]
        x = [0.]
        y = [0.]
    
        for i in range(0,int(v0/dt)):
            vy = a*t[i]
            if y[i] + v0y*dt - vy*dt >=0:
                t.append((i+1)*dt)
                x.append(x[i] + v0x*dt)
                y.append(y[i] + v0y*dt - vy*dt)
            else:
                 break
    
        self.range = v0x*t[-1]


    def plot_trajectory(self):
        vx = v0*np.cos((theta/360)*2*np.pi)
        vy = v0*np.sin((theta/360)*2*np.pi)
        t = [0.]
        x = [0.]
        y = [0.]
        dt = 0.01
        for i in range(0, 1000):
            t.append(i*dt)
            x.append(x[i] + vx*dt)
            y.append(y[i] + vy*dt)
       
        plt.plot(x,y)
        plt.set(xlabel='x [m]', ylabel='y [m]', title='x-y graf')
        plt.grid()
        plt.set_aspect('equal')

        plt.show()

         
