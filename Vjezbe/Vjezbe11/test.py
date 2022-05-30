import gravitacija as grav
import matplotlib.pyplot as plt

Mz = 5.9742*10**24
Ms = 1.989*10**30
Au = 1.486*10**11
godina = 365.242*24*60*60

Zemlja = grav.Planet(Mz, Au, 0, 29783)
Sunce = grav.Planet(Ms, 0, 0, 0)
Jupiter = grav.Planet(317*Mz, -5.2*Au, 0, 13070)
Neptun = grav.Planet(17*Mz, 30*Au, 0, 5430)

sv = grav.Svemir()
sv.addplanet(Zemlja)
sv.addplanet(Sunce)
sv.addplanet(Jupiter)
sv.addplanet(Neptun)

sv.orbita(164*godina, 3600*24)

plt.plot(Zemlja.x, Zemlja.y)
plt.scatter(Sunce.x, Sunce.y, color='orange')
plt.plot(Jupiter.x, Jupiter.y, color='brown')
plt.plot(Neptun.x, Neptun.y, color='darkblue')
plt.grid()
plt.axis('equal')
plt.show()