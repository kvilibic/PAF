import numpy as np
import universe as grav
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import math

Mz = 5.9742*10**24
Ms = 1.989*10**30
Au = 1.486*10**11
godina = 365.242*24*60*60

Zemlja = grav.Planet(Mz, Au, 0, 29783)
Sunce = grav.Planet(Ms, 0, 0, 0)
Merkur = grav.Planet(0.055*Mz, 0.466*Au, 0, 47360)
Venera = grav.Planet(0.815*Mz, 0.723*Au, 0, 35020)
Mars = grav.Planet(0.107*Mz, 1.666*Au, 0, 24070)

sv = grav.Svemir()

sv.addplanet(Sunce)
sv.addplanet(Merkur)
sv.addplanet(Venera)
sv.addplanet(Zemlja)
sv.addplanet(Mars)

sv.evolve(5*godina, 3600*24)

fig = plt.figure()
metadata = dict(title='SuncevSustav.gif', artist='kvilibic')
writer = PillowWriter(fps=10, metadata=metadata)

with writer.saving(fig, "SuncevSustav.gif", 100):
    for j in range(math.floor(len(Zemlja.x)/10)):
        i = j*10
        plt.clf()

        plt.scatter(Sunce.x[i], Sunce.y[i], color='yellow', label="Sunce")

        plt.plot(Merkur.x[0:i], Merkur.y[0:i], color="grey", label="Merkur")
        plt.plot(Merkur.x[i], Merkur.y[i], 'o', color="grey")

        plt.plot(Venera.x[0:i], Venera.y[0:i], color="orange", label="Venera")
        plt.plot(Venera.x[i], Venera.y[i], 'o', color="orange")

        plt.plot(Zemlja.x[0:i], Zemlja.y[0:i], color="blue", label="Zemlja")
        plt.plot(Zemlja.x[i], Zemlja.y[i], 'o', color="blue")

        plt.plot(Mars.x[0:i], Mars.y[0:i], color="red", label="Mars")
        plt.plot(Mars.x[i], Mars.y[i], 'o', color="red")

        plt.legend(loc='upper right')
        plt.xlim(-2*Au, 2*Au)
        plt.ylim(-2*Au, 2*Au)
        plt.grid()
        plt.title('Sunčev sustav')

        writer.grab_frame()

