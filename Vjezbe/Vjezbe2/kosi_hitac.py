import numpy as np
import matplotlib.pyplot as plt

a = 9.81
dt = 0.005
# Range mi ide od (0 do v0/dt) umjesto npr. od (0 do 10000) u slucaju da korisnik upise visoki v0 da budem siguran da će cijeli graf biti nacrtan

def putanja(v0, theta):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    t = [0.]
    x = [0.]
    y = [0.]
    
    for i in range(0,int(v0/dt)):
        vy = a*t[i]
        if y[i] + v0y*dt - vy*dt >=0:
            t.append((i+1)*dt)
            x.append(x[i] + v0x*dt)
            y.append(y[i] + v0y*dt - vy*dt)
        else:
            break
        

    plt.plot(x,y)
    plt.xlabel("x [m]", loc='right')
    plt.ylabel("y [m]", loc='top')
    plt.grid()

    plt.show()


#################################################################################################################


def maks_visina(v0, theta):
    v0y = v0*np.sin((theta/360)*2*np.pi)

    for i in range(0,int(v0/dt)):
        t = i*dt
        vy = v0y - a*t
        if vy <= 0:
            break
    h = v0y*t - 0.5*a*t*t
    
    print("Maksimalna visina je {} m".format(h))


#################################################################################################################


def domet(v0, theta):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    t = [0.]
    x = [0.]
    y = [0.]
    
    for i in range(0,int(v0/dt)):
        vy = a*t[i]
        if y[i] + v0y*dt - vy*dt >=0:
            t.append((i+1)*dt)
            x.append(x[i] + v0x*dt)
            y.append(y[i] + v0y*dt - vy*dt)
        else:
            break
    
    d = v0x*t[-1]

    print("Domet je {} m".format(d))


#################################################################################################################


def maks_brzina(v0, theta):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    y = 0
    v_max = v0
    for i in range (0,int(v0/dt)):
        t = i*dt
        y = v0y*t - 0.5*a*t*t
        if y >=0:
            vy = v0y - a*t
            v = np.sqrt(v0x**2 + vy**2)
            if v > v_max:
                v_max = v
    
    # Maksimalna brzina u kosom hicu na horizontalnoj podlozi će uvijek bit jednaka brzini kad je y = 0 (početna brzina i udar)

    print("Maksimalna brzina je {} m/s".format(v_max))


#################################################################################################################


def meta(v0, theta, s1, s2, r):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    t = [0.]
    x = [0.]
    y = [0.]
    pogodak = False
    najmanja = np.sqrt(s1**2 + s2**2)
    
    for i in range(0,int(v0/dt)):
        vy = a*t[i]
        if y[i] + v0y*dt - vy*dt >=0:
            t.append((i+1)*dt)
            x.append(x[i] + v0x*dt)
            y.append(y[i] + v0y*dt - vy*dt)
            p1 = x[i] - s1
            p2 = y[i] - s2
            if p1**2 + p2**2 <= r**2:
                pogodak = True
            else:
                udaljenost = np.sqrt(p1**2 + p2**2) - r
                if udaljenost < najmanja:
                    najmanja = udaljenost
        else:
            break
    
    if pogodak == True:
        print("Meta je pogođena.")
    else:
        print("Meta nije pogođena. Najmanja udaljenost od mete je {} metara.".format(najmanja))

    alfa = np.linspace(0, 2*np.pi, 100)
    x1 = s1 + r*np.cos(alfa)
    y1 = s2 + r*np.sin(alfa)
    plt.plot(x1, y1)

    plt.plot(x,y)
    plt.xlabel("x [m]", loc='right')
    plt.ylabel("y [m]", loc='top')
    plt.grid()

    plt.show()




