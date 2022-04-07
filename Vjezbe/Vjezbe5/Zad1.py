import harmonic_oscillator as har
import matplotlib.pyplot as plt

p1 = har.HarmonicOscillator()
p1.set_in_cond(5, 1, 5, 0.01, 10)

p2 = har.HarmonicOscillator()
p2.set_in_cond(5, 1, 5, 0.05, 10)

p3 = har.HarmonicOscillator()
p3.set_in_cond(5, 1, 5, 0.25, 10)

p_an = har.HarmonicOscillator()
p_an.set_in_cond(5, 1, 5, 0.005, 10)

t, x, v, a = p1.putanja()
t2, x2, v2, a2 = p2.putanja()
t3, x3, v3, a3 = p3.putanja()
t_an, x_an, v_an, a_an = p_an.analitical()

plt.scatter(t, x, s=2)
plt.scatter(t2, x2, s=2)
plt.scatter(t3, x3, s=2)
plt.plot(t_an, x_an)
plt.grid()
plt.show()

plt.scatter(t, v, s=2)
plt.scatter(t2, v2, s=2)
plt.scatter(t3, v3, s=2)
plt.plot(t_an, v_an)
plt.grid()
plt.show()

plt.scatter(t, a, s=2)
plt.scatter(t2, a2, s=2)
plt.scatter(t3, a3, s=2)
plt.plot(t_an, a_an)
plt.grid()
plt.show()