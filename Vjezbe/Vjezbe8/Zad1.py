import particle as prt
import matplotlib.pyplot as plt

p1 = prt.Particle(0, 0, 25, 45, 1, 1, 1, 0.5)
x, y = p1.gibanje(dt=0.005)

plt.plot(x,y)
plt.ylabel("y [m]", loc='top')
plt.xlabel("x [m]", loc='right')
plt.grid()
plt.show()

print("Za dt manji od 0.01 Euleor-ova metoda daje dovoljno precizno numericko rjesenje.")
