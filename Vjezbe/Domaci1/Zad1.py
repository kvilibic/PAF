import particle as prt

p1 = prt.Particle()
p1.set_in_cond(10, 60, 0, 5, 0.01)

p1.total_time()
print("Ukupno vrijeme je {:.3f} s.".format(p1.t_uk))

p1.max_speed()
print("Maksimalna brzina je {:.3f} m/s.".format(p1.v_max))

p1.reset()
p1.velocity_to_hit_target(45, 0, 0, 10, 2, 2)
print("Najmanja potrebna početna brzina za pogodit kuglicu je {0:.2f} m/s, a najveća {1:.2f} m/s.".format(p1.v_0_pogodak[0], p1.v_0_pogodak[-1]))

p1.reset()
p1.angle_to_hit_target(100, 0, 0, 10, 2, 2)
print("Najmanji potrebni kut za pogodit kuglicu je {0:.2f}°, a najveći {1:.2f}°.".format(p1.theta_pogodak[0], p1.theta_pogodak[-1]))