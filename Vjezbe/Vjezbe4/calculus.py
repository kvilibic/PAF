import numpy as np

def der_u_tocki(f,x, dx):
    return((f(x+dx) - f(x))/dx)


def derivacija(f, a, b, dx, m=3):   #Dodaj varijablu "m" za 2 i 3
    x = [a]
    dfx = [(f(a+dx) - f(a))/dx]
    while x[-1] <= b:
        if m == 2:
            dfx.append((f(x[-1]+dx) - f(x[-1]))/dx)
            x.append(x[-1] + dx)
        elif m == 3:
            dfx.append((f(x[-1]+dx) - f(x[-1] - dx))/(2*dx))
            x.append(x[-1] + dx)
        else:
            print("Varijabla 'm' mora biti 2 ili 3" )
    return x, dfx


def integracija(f, a, b):
    donjaMeda = []
    gornjaMeda = []
    koraci = []
    for n in range (100, 1100, 100):
        x = np.linspace(a, b, n+1)
        dx = (b-a)/n
        donja = 0
        gornja = 0
        for i in range(n):
            donja += f(x[i])*dx
            gornja += f(x[i+1])*dx
        

        donjaMeda.append(donja)
        gornjaMeda.append(gornja)
        koraci.append(n)

    return donjaMeda, gornjaMeda, koraci


def trapez(f, a, b):
    integrali = []
    koraci = []
    for n in range (100, 1100, 100):
        x = np.linspace(a, b, n+1)
        dx = (b-a)/n
        vrijednost = 0
        for i in range(n):
            vrijednost += f(x[i])*dx + (f(x[i+1]) - f(x[i])) * dx/2
        
        integrali.append(vrijednost)
        koraci.append(n)    

    return integrali, koraci



