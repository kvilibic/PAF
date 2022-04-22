import Projectile as pro
import matplotlib.pyplot as plt

p1 = pro.ProjectileDrop(2000, 200)

t, dt = p1.ovisnosti()

plt.plot(dt, t)
plt.grid()
plt.show()