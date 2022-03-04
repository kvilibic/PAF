def funkcija(x1,x2,y1,y2):

    a = (y2-y1)/(x2-x1)
    b = y1 - a*x1

    if b>=0:
        predznak = "+"
    else:
        predznak = ""

    print("y = ",round(a,2),"x ",predznak, round(b,2))

funkcija(4,3,12,17)