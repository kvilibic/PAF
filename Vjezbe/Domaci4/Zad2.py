import particle as prt
import matplotlib.pyplot as plt
import numpy as np

#Kugla (tijelo==1), Kocka (tijelo==2)

p1 = prt.Particle(0, 0, 25, 45, 1, 1, 1, tijelo=1, dimenzija=0.2)
p1.angle_to_hit_target(20, 0, 0.3)
print("Projektil ce pogoditi metu ako ga izbacimo po kutem od {:.2f}°.".format(p1.theta))
plt.plot(p1.x, p1.y)

p2 = prt.Particle(0, 0, 25, 45, 1, 1, 1, tijelo=1, dimenzija=0.2)
p2.angle_to_hit_target(8, 12, 0.6)
print("Projektil ce pogoditi metu ako ga izbacimo po kutem od {:.2f}°.".format(p2.theta))
plt.plot(p2.x, p2.y)

kut = np.linspace(0, 2*np.pi, 100)
x1 = p1.s1 + p1.r*np.cos(kut)
y1 = p1.s2 + p1.r*np.sin(kut)
x2 = p2.s1 + p2.r*np.cos(kut)
y2 = p2.s2 + p2.r*np.sin(kut)
plt.plot(x1, y1, label="Meta 1 - potreban kut {:.2f}°".format(p1.theta))
plt.plot(x2, y2, label="Meta 2 - potreban kut {:.2f}°".format(p2.theta))

plt.legend(loc='upper right')
plt.axis('equal')
plt.grid()
plt.show()