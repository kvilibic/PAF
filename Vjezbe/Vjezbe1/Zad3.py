x1 = int(input("Upišite koordinatu x1: "))
y1 = int(input("Upišite koordinatu y1: "))
x2 = int(input("Upišite koordinatu x2: "))
y2 = int(input("Upišite koordinatu y2: "))

a = (y2-y1)/(x2-x1)
b = y1 - a*x1

predznak = ""
if b>=0:
    predznak = "+"

print("y = ",round(a,2),"x ",predznak, round(b,2))