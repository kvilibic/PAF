import numpy as np
import matplotlib.pyplot as plt

a = -9.81
dt = 0.005

def putanja(v0, theta):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    t = [0.]
    x = [0.]
    y = [0.]
    vy = [v0y]
    
    for i in range(0,int(v0/dt)):
        while y[-1] >= 0:
            t.append(t[-1] + dt)
            x.append(x[-1] + v0x*dt)
            y.append(y[-1] + vy[-1]*dt)
            vy.append(vy[-1] + a*dt)
            break

    plt.plot(x,y)
    plt.xlabel("x [m]", loc='right')
    plt.ylabel("y [m]", loc='top')
    plt.grid()

    plt.show()

#################################################################################################################

def maks_visina(v0, theta):
    v0y = v0*np.sin((theta/360)*2*np.pi)
    vy = [v0y]
    y = [0.]

    for i in range(0,int(v0/dt)):
        while vy[-1] >=0:
            y.append(y[i] + vy[-1]*dt)
            vy.append(vy[-1] + a*dt)
            break
    
    print("Maksimalna visina je {:.2f} m".format(y[-1]))

#################################################################################################################

def domet(v0, theta):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    x = [0.]
    y = [0.]
    vy = [v0y]
    
    for i in range(0,int(v0/dt)):
        while y[-1] >= 0:
            x.append(x[-1] + v0x*dt)
            y.append(y[-1] + vy[-1]*dt)
            vy.append(vy[-1] + a*dt)
            break

    print("Domet je {:.2f} m".format(x[-1]))

#################################################################################################################

def maks_brzina(v0, theta):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    y = [0.]
    vy = [v0y]
    v_max = v0
    for i in range (0,int(v0/dt)):
        while y[-1] >= 0:
            y.append(y[-1] + vy[-1]*dt)
            vy.append(vy[-1] + a*dt)
            v = np.sqrt(v0x**2 + vy[-1]**2)
            if v > v_max:
                v_max = v
            break

    print("Maksimalna brzina je {:.2f} m/s".format(v_max))

#################################################################################################################

def meta(v0, theta, s1, s2, r):
    v0x = v0*np.cos((theta/360)*2*np.pi)
    v0y = v0*np.sin((theta/360)*2*np.pi)
    t = [0.]
    x = [0.]
    y = [0.]
    vy = [v0y]
    pogodak = False
    najmanja = np.sqrt(s1**2 + s2**2)
    
    for i in range(0,int(v0/dt)):
        while y[-1] >= 0:
            t.append(t[-1] + dt)
            x.append(x[-1] + v0x*dt)
            y.append(y[-1] + vy[-1]*dt)
            vy.append(vy[-1] + a*dt)
            p1 = x[-1] - s1
            p2 = y[-1] - s2
            if p1**2 + p2**2 <= r**2:
                pogodak = True
            else:
                udaljenost = np.sqrt(p1**2 + p2**2) - r
                if udaljenost < najmanja:
                    najmanja = udaljenost
            break
    
    if pogodak == True:
        print("Meta je pogođena.")
    else:
        print("Meta nije pogođena. Najmanja udaljenost od mete je {:.2f} metara.".format(najmanja))

    alfa = np.linspace(0, 2*np.pi, 100)
    x1 = s1 + r*np.cos(alfa)
    y1 = s2 + r*np.sin(alfa)
    plt.plot(x1, y1)

    plt.plot(x,y)
    plt.xlabel("x [m]", loc='right')
    plt.ylabel("y [m]", loc='top')
    plt.grid()

    plt.show()