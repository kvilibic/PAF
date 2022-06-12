import universe as grav
import matplotlib.pyplot as plt
import numpy as np

Mz = 5.9742*10**24
Ms = 1.989*10**30
Au = 1.486*10**11
godina = 365.242*24*60*60

Zemlja = grav.Planet(Mz, -Au, 0, 29783, 6970000)
Sunce = grav.Planet(Ms, 0, 0, 0, 695700000)
Merkur = grav.Planet(0.055*Mz, -0.466*Au, 0, 47360, 2439000)
Venera = grav.Planet(0.815*Mz, -0.723*Au, 0, 35020, 6051000)
Mars = grav.Planet(0.107*Mz, -1.666*Au, 0, 24070, 3389500)
Komet = grav.Komet(10**14, -3*Au, -3*Au, 15000, np.pi*1/3, 10000)

sv = grav.Svemir()

sv.addplanet(Sunce)
sv.addplanet(Merkur)
sv.addplanet(Venera)
sv.addplanet(Zemlja)
sv.addplanet(Mars)
sv.addplanet(Komet)

sv.evolve(1.4*godina, 3600*24)

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

plt.legend(loc='upper right')
plt.xlim(-2*Au, 2*Au)
plt.ylim(-2*Au, 2*Au)
plt.grid()
#plt.axis('equal')
plt.show()