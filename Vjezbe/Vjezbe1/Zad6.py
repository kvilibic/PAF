import matplotlib.pyplot as plt
import numpy as np

def funkcija(x,y,s1,s2,r):

    a = x - s1
    b = y - s2
    
    if a**2 + b**2 < r**2:
        print("Točka se nalazi unutar kružnice")
    if a**2 + b**2 == r**2:
        print("Točka se nalazi na kružnici")
    if a**2 + b**2 > r**2:
        print("Točka se nalazi izvan kružnice")
    

    theta = np.linspace(0, 2*np.pi, 100)
    x1 = s1 + r*np.cos(theta)
    y1 = s2 + r*np.sin(theta)

    udaljenost = abs(np.sqrt(a**2 + b**2) - r)
    print("Točka se nalazi na koordinatama (",x,",",y,") te je njena udaljenost od kruznice jednaka ", round(udaljenost, 2))

    plt.plot(x1,y1)
    plt.plot(x, y, marker="o", color="blue")
    plt.axis('equal')
    plt.grid()
    
    while True:
        try:
            graf = int(input("Ako želite prikazati graf na ekranu upišite 1, ako ga želite spremiti kao PDF upišite 2: "))
        except ValueError:
            print("Pogrešan unos.")
            continue
        else:
            break

    if graf == 1:
        plt.show()
    if graf == 2:
        plt.savefig(input("Spremi kao: ")+".pdf")



funkcija(x=float(input("Upišite x koordinatu točke: ")), y=float(input("Upišite y koordinatu točke: ")), s1=float(input("Upišite x koordinatu središta kružnice: ")), s2=float(input("Upišite y koordinatu središta kružnice: ")), r=float(input("Upišite radijus kružnice: ")))