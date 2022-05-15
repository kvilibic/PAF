import particle as prt
import matplotlib.pyplot as plt

p1 = prt.Particle(0, 0, 25, 45, 1, 1, 1, 0.5)
x1, y1 = p1.gibanje(dt=0.01)

p2 = prt.Particle(0, 0, 25, 45, 1, 1, 1, 0.5)
x2, y2 = p2.RK4_gibanje(dt=0.01)

plt.plot(x1, y1, label="Eulerova metoda")
plt.plot(x2, y2, label="R-K metoda")
plt.legend(loc='upper right')
plt.grid()
plt.show()