import numpy as np
import matplotlib.pyplot as plt

def kosi_hitac(v0, theta):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    t = [0.]
    x = [0.]
    y = [0.]
    vy = [v0y]
    a = -9.81
    dt = 0.01

    for i in range(0, 1000):
        while t[-1] <=10:
            t.append(t[-1] + dt)
            x.append(x[-1] + v0x*dt)
            y.append(y[-1] + vy[-1]*dt)
            vy.append(vy[-1] + a*dt)
            break
       
    fig, axs = plt.subplots(2,2)
    fig.delaxes(axs[1,1])
    fig.subplots_adjust(hspace=0.5)

    axs[0,0].plot(x,y)
    axs[0,0].set(xlabel='x [m]', ylabel='y [m]', title='x-y graf')
    axs[0,0].grid()
    

    axs[0,1].plot(t,x)
    axs[0,1].set(xlabel='t [s]', ylabel='x [m]', title='x-t graf')
    axs[0,1].grid()

    axs[1,0].plot(t,y)
    axs[1,0].set(xlabel='t [s]', ylabel='y [m]', title='y-t graf')
    axs[1,0].grid()

    plt.show()

kosi_hitac(25, 60)