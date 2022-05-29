import Particle as prt
import numpy as np
import matplotlib.pyplot as plt

elektron = prt.Particle(-1, 1, np.array((1., 1., 1.)), np.array((0, 0, 0)), np.array((0, 0, 1)))
elektron.gibanje(0.01)

pozitron = prt.Particle(1, 1, np.array((1., 1., 1.)), np.array((0, 0, 0)), np.array((0, 0, 1)))
pozitron.gibanje(0.01)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(elektron.x, elektron.y, elektron.z)
ax.plot3D(pozitron.x, pozitron.y, pozitron.z, color="red")
plt.grid()
plt.show()

# Pozitron se giba u smjeru kazaljke na satu, a elektron suprotno od smjera kazaljke na satu.