import numpy as np
import universe as grav
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import math

Mz = 5.9742*10**24
Ms = 1.989*10**30
Au = 1.486*10**11
godina = 365.242*24*60*60

Zemlja1 = grav.Planet(Mz, Au, 0, -29783, 6970000)
Sunce1 = grav.Planet(Ms, 0, 0, 0, 695700000)
Merkur1 = grav.Planet(0.055*Mz, 0.466*Au, 0, -47360, 2439000)
Venera1 = grav.Planet(0.815*Mz, 0.723*Au, 0, -35020, 6051000)
Mars1 = grav.Planet(0.107*Mz, 1.666*Au, 0, -24070, 3389500)
Komet1 = grav.Komet(10**14, Au, -6970000, 35000, -np.pi*1.5/2, 10000)

sv = grav.Svemir()

sv.addplanet(Sunce1)
sv.addplanet(Merkur1)
sv.addplanet(Venera1)
sv.addplanet(Zemlja1)
sv.addplanet(Mars1)
sv.addplanet(Komet1)

sv.evolve(godina, 3600*4)

Zemlja = grav.Planet(Mz, Zemlja1.x[-1], Zemlja1.y[-1], 29783, 6970000)
Sunce = grav.Planet(Ms, Sunce1.x[-1], Sunce1.y[-1], 0, 695700000)
Merkur = grav.Planet(0.055*Mz, Merkur1.x[-1], Merkur1.y[-1], 47360, 2439000)
Venera = grav.Planet(0.815*Mz, Venera1.x[-1], Venera1.y[-1], 35020, 6051000)
Mars = grav.Planet(0.107*Mz, Mars1.x[-1], Mars1.y[-1], 24070, 3389500)
Komet = grav.Komet(10**14, Komet1.x[-1], Komet1.y[-1], 35000, -np.pi*1.5/2, 10000)

Sunce.v = -Sunce1.v
Zemlja.v = -Zemlja1.v
Merkur.v = -Merkur1.v
Venera.v = -Venera1.v
Mars.v = -Mars1.v
Komet.v = -Komet1.v

del sv.planets[0:len(sv.planets)]

sv.addplanet(Sunce)
sv.addplanet(Merkur)
sv.addplanet(Venera)
sv.addplanet(Zemlja)
sv.addplanet(Mars)
sv.addplanet(Komet)

sv.t = 0
sv.evolve(godina, 3600*4)

'''
fig, ax = plt.subplots()

plt.plot(Merkur.x, Merkur.y, color="grey", label="Merkur")
plt.plot(Merkur.x[-1], Merkur.y[-1], 'o', color="grey")

plt.plot(Venera.x, Venera.y, color="orange", label="Venera")
plt.plot(Venera.x[-1], Venera.y[-1], 'o', color="orange")

plt.plot(Zemlja.x, Zemlja.y, color="blue", label="Zemlja")
plt.plot(Zemlja.x[-1], Zemlja.y[-1], 'o', color="blue")

plt.plot(Mars.x, Mars.y, color="red", label="Mars")
plt.plot(Mars.x[-1], Mars.y[-1], 'o', color="red")

plt.plot(Komet.x, Komet.y, color="black", label="Komet")
plt.plot(Komet.x[-1], Komet.y[-1], 'o', color="black")

plt.scatter(Sunce.x, Sunce.y, color='yellow', label="Sunce")

#circle = plt.Circle((Zemlja.x[-1], Zemlja.y[-1]), Zemlja.radius, color='blue')
#ax.add_artist(circle)

plt.legend(loc='upper right')
plt.xlim(-2.5*Au, 2.5*Au)
plt.ylim(-2.5*Au, 2.5*Au)
plt.grid()
plt.show()

'''
fig = plt.figure()
metadata = dict(title='Sudar.gif', artist='kvilibic')
writer = PillowWriter(fps=15, metadata=metadata)

with writer.saving(fig, "Sudar.gif", 100):
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

        plt.plot(Komet.x[0:i], Komet.y[0:i], color="black", label="Komet")
        plt.plot(Komet.x[i], Komet.y[i], 'D', markersize= 2.5, color="black")

        plt.legend(loc='upper right')
        plt.xlim(-2*Au, 2*Au)
        plt.ylim(-2*Au, 2*Au)
        plt.grid()
        plt.title('Sunčev sustav')

        writer.grab_frame()



