import bungee as bun
import matplotlib.pyplot as plt

p1 = bun.Bungee(200, 50, 80, 100, otpor=False)
p1.gibanje()

p2 = bun.Bungee(200, 50, 80, 100, otpor=True)
p2.gibanje()

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(p1.t, p1.y)
axs[0, 1].plot(p1.t, p1.Ep)
axs[0, 1].plot(p1.t, p1.Ek)
axs[0, 1].plot(p1.t, p1.Eel)
axs[0, 1].plot(p1.t, p1.Euk)
axs[1, 0].plot(p2.t, p2.y)
axs[1, 1].plot(p2.t, p2.Ep)
axs[1, 1].plot(p2.t, p2.Ek)
axs[1, 1].plot(p2.t, p2.Eel)
axs[1, 1].plot(p2.t, p2.Euk)
plt.show()
