import particle as prt
import matplotlib.pyplot as plt

#Kugla (tijelo==1), Kocka (tijelo==2)

p1 = prt.Particle(0, 0, 25, 45, 1, 1, 1, tijelo=1, dimenzija=0.2)
x1, y1 = p1.RK4_gibanje(dt=0.01)

p2 = prt.Particle(0, 0, 25, 45, 1, 1, 1, tijelo=2, dimenzija=0.2)
x2, y2 = p2.RK4_gibanje(dt=0.01)

plt.plot(x1, y1, label="Kugla")
plt.plot(x2, y2, label="Kocka")
plt.legend(loc='upper right')
plt.grid()
plt.show()