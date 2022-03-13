import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, M):
    t = [0.]
    x = [0.]
    v = [0.]
    a = F/M
    dt = 0.01
    for i in range(0,1000):
        t.append(i*dt)
        v.append(v[i] + a*dt)
        x.append(x[i] + v[i]*dt)

    
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

    ac = []
    for el in t:
        ac.append(a)
    axs[2].plot(t,ac)
    axs[2].set_title("a-t graf")
    axs[2].grid()
    axs[2].set_xlabel("t [s]", loc='right')
    axs[2].set_ylabel("a [m/s2]", loc='top')

    plt.show()

jednoliko_gibanje(100, 25)


        