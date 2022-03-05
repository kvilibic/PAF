while True:
    try:    
        x1 = int(input("Upišite koordinatu x1: "))
        y1 = int(input("Upišite koordinatu y1: "))
        x2 = int(input("Upišite koordinatu x2: "))
        y2 = int(input("Upišite koordinatu y2: "))
    except ValueError:
        print("Greška, molimo ponovite upis: ")
        continue
    else:
        break

a = (y2-y1)/(x2-x1)
b = y1 - a*x1

if b>=0:
    predznak = "+"
else:
    predznak = "-"

print("Jednadžba pravca je y = ",round(a,2),"x",predznak, round(abs(b),2))