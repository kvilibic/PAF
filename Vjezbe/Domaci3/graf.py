import matplotlib.pyplot as plt

x = []
v = []
a = []
t = []

f1 = open("x.txt", "r")
x_string = f1.read()
f1.close()

f2 = open("v.txt", "r")
v_string = f2.read()
f2.close()

f3 = open("a.txt", "r")
a_string = f3.read()
f3.close()

f4 = open("t.txt", "r")
t_string = f4.read()
f4.close()

for el in x_string.split(","):
    x.append(float(el))
for el in v_string.split(","):
    v.append(float(el))
for el in a_string.split(","):
    a.append(float(el))
for el in t_string.split(","):
    t.append(float(el))    

plt.plot(t, x)
plt.grid()
plt.show()

plt.plot(t, v)
plt.grid()
plt.show()

plt.plot(t, a)
plt.grid()
plt.show()