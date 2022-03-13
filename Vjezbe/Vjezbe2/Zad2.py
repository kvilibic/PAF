import numpy as np
import matplotlib.pyplot as plt


def kosi_hitac(v0, theta):
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
       
    fig, axs = plt.subplots(2,2)
    fig.delaxes(axs[1,1])
    fig.subplots_adjust(hspace=0.5)

    axs[0,0].plot(x,y)
    axs[0,0].set(xlabel='x [m]', ylabel='y [m]', title='x-y graf')
    axs[0,0].grid()
    axs[0,0].set_aspect('equal')

    axs[0,1].plot(t,x)
    axs[0,1].set(xlabel='t [s]', ylabel='x [m]', title='x-t graf')
    axs[0,1].grid()

    axs[1,0].plot(t,y)
    axs[1,0].set(xlabel='t [s]', ylabel='y [m]', title='y-t graf')
    axs[1,0].grid()

    plt.show()

kosi_hitac(10, 55)