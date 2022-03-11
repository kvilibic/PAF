import numpy as np
import matplotlib.pyplot as plt


F = float(input("Upišite iznos sile: "))
M = float(input("Upišite masu tijela: "))


t = np.linspace(0, 10, 100)
a = F/M
v = a*t
x = 0.5*a*t*t

plt.plot(x, t)
plt.title("x-t graf")
plt.xlabel("Vrijeme [s]")
plt.ylabel("Pomak [m]")

plt.plot(v, t)
plt.title("v-t graf")
plt.xlabel("Vrijeme [s]")
plt.ylabel("Brzina [m]")

plt.plot(a, t)
plt.title("a-t graf")
plt.xlabel("Vrijeme [s]")
plt.ylabel("Akceleracija [m]")

plt.show()