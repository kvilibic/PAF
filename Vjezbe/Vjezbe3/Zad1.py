import particle as prt

p1 = prt.Particle()
p1.set_in_cond(10, 60, 0, 0, 0.01)
p1.range()
print("Domet je {:.2f} metara".format(p1.x[-1]))
p1.plot_trajectory()
p1.range_analitical()
print("Analitički domet je {:.2f} metara".format(p1.d))