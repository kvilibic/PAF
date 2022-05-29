import Particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle(-1, 1, np.array((1., 1., 1.)), np.array((0, 0, 0)), np.array((0, 0, 1)))
p1.gibanje(0.1)

p2 = prt.Particle(-1, 1, np.array((1., 1., 1.)), np.array((0, 0, 0)), np.array((0, 0, 1)))
p2.RK4_gibanje(0.1)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(p1.x, p1.y, p1.z)
ax.plot3D(p2.x, p2.y, p2.z, color="red", linestyle="dashed")
plt.grid()
plt.show()

# Na vecim koracima se vidi odstupanje putanja Eulerovom i RK metodom.