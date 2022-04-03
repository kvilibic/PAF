import calculus as cal
import math
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x*x - 2*x

def int_f1(x):
    return 1/3*x*x*x - x*x

donjaMeda, gornjaMeda, koraci = cal.integracija(f1, 0, 10)
integrali, koraci = cal.trapez(f1, 0, 10)

plt.scatter(koraci, donjaMeda)
plt.scatter(koraci, gornjaMeda)
plt.scatter(koraci, integrali)

####### ANALITICKI #######
vrijednost = int_f1(10) - int_f1(0)
korak = np.linspace(0, 1000, 100)
integral = []
for i in range(len(korak)):
    integral.append(vrijednost)

plt.plot(korak, integral, color='red')
##########################

plt.grid()
plt.show()