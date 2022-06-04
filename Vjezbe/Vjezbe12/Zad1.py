import universe as grav
import matplotlib.pyplot as plt

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

plt.plot(Merkur.x, Merkur.y, color="grey", label="Merkur")
plt.plot(Merkur.x[-1], Merkur.y[-1], 'o', color="grey")

plt.plot(Venera.x, Venera.y, color="orange", label="Venera")
plt.plot(Venera.x[-1], Venera.y[-1], 'o', color="orange")

plt.plot(Zemlja.x, Zemlja.y, color="blue", label="Zemlja")
plt.plot(Zemlja.x[-1], Zemlja.y[-1], 'o', color="blue")

plt.plot(Mars.x, Mars.y, color="red", label="Mars")
plt.plot(Mars.x[-1], Mars.y[-1], 'o', color="red")

plt.scatter(Sunce.x, Sunce.y, color='yellow', label="Sunce")

plt.legend(loc='upper right')
plt.grid()
plt.axis('equal')
plt.show()