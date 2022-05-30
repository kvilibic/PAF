import gravitacija as grav
import matplotlib.pyplot as plt

Mz = 5.9742*10**24
Ms = 1.989*10**30
Au = 1.486*10**11
godina = 365.242*24*60*60

Zemlja = grav.Planet(Mz, Au, 0, 29783)
Sunce = grav.Planet(Ms, 0, 0, 0)

sv = grav.Svemir()
sv.addplanet(Zemlja)
sv.addplanet(Sunce)

sv.orbita(godina, 3600)

plt.plot(Zemlja.x, Zemlja.y)
plt.scatter(Sunce.x, Sunce.y, color='orange')
plt.grid()
plt.axis('equal')
plt.show()