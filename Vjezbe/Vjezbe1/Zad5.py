import matplotlib.pyplot as plt

def funkcija(x1,y1,x2,y2):

    a = (y2-y1)/(x2-x1)
    b = y1 - a*x1

    if b>=0:
        predznak = "+"
    else:
        predznak = ""

    print("Jednadžba pravca je y = ",round(a,2),"x",predznak, round(b,2))

    plt.plot(x1, y1, marker="o", color="blue")
    plt.plot(x2, y2, marker="o", color="blue")
    plt.axline((x1,y1),(x2,y2))
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

    

funkcija(x1 = int(input("Upišite x1: ")), y1 = int(input("Upišite y1: ")), x2 = int(input("Upišite x2: ")), y2 = int(input("Upišite y2: ")))


