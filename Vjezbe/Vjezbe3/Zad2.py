import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p2 = prt.Particle()
dt = [0.0001]
greska = []
for i in range(1000):
    p2.set_in_cond(10, 60, 0, 0, dt[i])
    p2.range()
    p2.range_analitical()
    greska.append(abs(p2.d - p2.x[-1])/p2.d*100)
    dt.append(dt[i] + 0.0001)
del dt[-1]

plt.plot(dt, greska)
plt.xlabel("dt [s]", loc='right')
plt.ylabel("Relativna pogreška [%]", loc='top')
plt.grid()
plt.show()

