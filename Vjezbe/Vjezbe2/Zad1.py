import numpy as np
import matplotlib.pyplot as plt

def gibanje(F, M):
    t = [0.]
    x = [0.]
    v = [0.]
    a = F/M
    dt = 0.01
    for i in range(0,1000):
        t.append(i*dt)
        v.append(v[i] + a*dt)
        x.append(x[i] + v[i]*dt)

    fig, graf = plt.subplots(3)
    
    graf[0].plot(t,x)
    graf[0].set_title("x-t graf")
    graf[0].grid()
    graf[0].xlabel("Vrijeme [s]")
    graf[0].ylabel("Pomak [m]")

    graf[1].plot(t,v)
    graf[1].set_title("v-t graf")
    graf[1].grid()
    graf[1].xlabel("Vrijeme [s]")
    graf[1].ylabel("Brzina [m/s]")

    ac = []
    for el in t:
        ac.append(a)
    graf[2].plot(t,ac)
    graf[2].set_title("a-t graf")
    graf[2].grid()

    plt.show()

gibanje(10, 25)


        