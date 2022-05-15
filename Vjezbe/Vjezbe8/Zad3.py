import particle as prt
import matplotlib.pyplot as plt

p1 = prt.Particle(0, 0, 25, 45, 1, 1, 1, 0.5)
domet, Cd = p1.domet_o_Cd()

plt.plot(Cd, domet)
plt.ylabel("Domet [m]", loc='top')
plt.xlabel("Koef.trenja", loc='right')
plt.grid()
plt.show()

p2 = prt.Particle(0, 0, 25, 45, 1, 1, 1, 0.5)
domet, m = p2.domet_o_m()

plt.plot(m, domet)
plt.ylabel("Domet [m]", loc='top')
plt.xlabel("Masa [kg]", loc='right')
plt.grid()
plt.show()
