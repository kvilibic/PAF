import gibanje as gib
import matplotlib.pyplot as plt
import numpy as np


def sila_konst(x, v, t):
    return 5

def sila_elast(x, v, t):
    return -5*x

def sila_random(x, v, t):
    return 2*x - 3*v*t


g1 = gib.Particle()
g1.set_in_cond(5, 5, 1, sila_elast, 0.01, 10)
t, x, v, a = g1.gibanje()


plt.plot(t, x)
plt.xlabel("t [s]", loc='right')
plt.ylabel("x [m]", loc='top')
plt.grid()
plt.show()

plt.plot(t, v)
plt.xlabel("t [s]", loc='right')
plt.ylabel("v [m/s]", loc='top')
plt.grid()
plt.show()

plt.plot(t, a)
plt.xlabel("t [s]", loc='right')
plt.ylabel("a [m/s2]", loc='top')
plt.grid()
plt.show()