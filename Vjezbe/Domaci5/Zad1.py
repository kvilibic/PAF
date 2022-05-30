import Particle as prt
import numpy as np
import matplotlib.pyplot as plt

def B_konst(t):
        return np.array([0., 0., 1.])

def B_promj(t):
    return np.array([0., 0., 0.1*t[-1]])

p1 = prt.Particle(-1, 1, np.array((1., 1., 1.)), np.array((0, 0, 0)), B_konst)
p1.RK4_gibanje(0.01)

p2 = prt.Particle(-1, 1, np.array((1., 1., 1.)), np.array((0, 0, 0)), B_promj)
p2.RK4_gibanje(0.01)

elektron = prt.Particle(-1, 1, np.array((1., 1., 1.)), np.array((0, 0, 0)), B_promj)
elektron.RK4_gibanje(0.01)

pozitron = prt.Particle(1, 1, np.array((1., 1., 1.)), np.array((0, 0, 0)), B_promj)
pozitron.RK4_gibanje(0.01)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(p1.x, p1.y, p1.z, label="Konstantno mag.polje")
ax.plot3D(p2.x, p2.y, p2.z, color="red", label="Promjenjivo mag.polje")
plt.legend(loc='upper right')
plt.grid()
plt.show()

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(elektron.x, elektron.y, elektron.z, label="Elektron")
ax.plot3D(pozitron.x, pozitron.y, pozitron.z, color="red", label="Pozitron")
plt.legend(loc='upper right')
plt.grid()
plt.show()