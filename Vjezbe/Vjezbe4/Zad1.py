import calculus as cal
import math
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x*x*x - 2*x

def der_f1(x):
    return 3*x*x - 2

def f2(x):
    return math.sin(x)

def der_f2(x):
    return math.cos(x)

print("Vrijednost derivacije u odabranoj točki je ", cal.der_u_tocki(f2, 2, 0.01))

x, dfx = cal.derivacija(f2, 0, 10, 0.5)
plt.scatter(x, dfx, s=2)

x, dfx = cal.derivacija(f2, 0, 10, 0.1)
plt.scatter(x, dfx, s=2, c='green')

####### ANALITICKI #######
korak = np.linspace(0, 10, 1000)
funkcija = []
for i in range(len(korak)):
    funkcija.append(der_f2(korak[i]))

plt.plot(korak, funkcija, color='red')
##########################

plt.grid()
plt.show()

