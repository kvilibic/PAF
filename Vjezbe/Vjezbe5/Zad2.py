import harmonic_oscillator as har
import numpy as np

p1 = har.HarmonicOscillator()
p1.set_in_cond(5, 1, 5, 0.01, 10)

p2 = har.HarmonicOscillator()
p2.set_in_cond(5, 1, 5, 0.05, 10)

p3 = har.HarmonicOscillator()
p3.set_in_cond(5, 1, 5, 0.25, 10)

p1.period()
p2.period()
p3.period()
