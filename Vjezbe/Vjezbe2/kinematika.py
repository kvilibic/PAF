import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, M, vrijeme):
    t = [0.]
    x = [0.]
    v = [0.]
    a = [F/M]
    dt = vrijeme/1000
    for i in range(0,1000):
        t.append(t[-1] + dt)
        v.append(v[-1] + a[-1]*dt)
        x.append(x[-1] + v[-1]*dt)
        a.append(a[-1])

    
    fig, axs = plt.subplots(3)
    fig.subplots_adjust(hspace=1)
    
    axs[0].plot(t,x)
    axs[0].set_title("x-t graf")
    axs[0].grid()
    axs[0].set_xlabel("t [s]", loc='right')
    axs[0].set_ylabel("x [m]", loc='top')

    axs[1].plot(t,v)
    axs[1].set_title("v-t graf")
    axs[1].grid()
    axs[1].set_xlabel("t [s]", loc='right')
    axs[1].set_ylabel("v [m/s]", loc='top')

    axs[2].plot(t,a)
    axs[2].set_title("a-t graf")
    axs[2].grid()
    axs[2].set_xlabel("t [s]", loc='right')
    axs[2].set_ylabel("a [m/s2]", loc='top')

    plt.show()


def kosi_hitac(v0, theta):
    vx = v0*np.cos((theta/360)*2*np.pi)
    vy = v0*np.sin((theta/360)*2*np.pi)
    t = [0.]
    x = [0.]
    y = [0.]
    dt = 0.01
    for i in range(0, 1000):
        t.append(t[-1] + dt)
        x.append(x[-1] + vx*dt)
        y.append(y[-1] + vy*dt)
       
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