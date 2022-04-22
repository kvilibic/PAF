import Projectile as pro
import matplotlib.pyplot as plt

p1 = pro.ProjectileDrop(2000, 200)

x, y, vy, t = p1.putanja(0.01)

plt.plot(x, y)
plt.grid()
plt.show()

plt.plot(t, vy)
plt.grid()
plt.show()