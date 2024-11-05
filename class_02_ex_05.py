import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
from equations import *

#Exercise 5: What is the velocity of a parabolic orbit as the radial distance approaches infinity?

e = 1
a = float('inf')
G = 6.67259*10**-11 #gravitational constant
m1 = 5.9722*10**24 #Earth's mass in kg
mu = mu(G , m1)

r = np.linspace(10**3, 10**21, 500)
v = velocity(mu, r, a)

plt.figure(figsize=(10, 6))
plt.plot(r, v)
plt. title('velocity of Parabolic Orbit vs. Radial Distance')
plt.xlabel('Radial Distance [km]')
plt.ylabel('Velocity [km/s]')
plt.xscale('log')
plt.yscale('log')
plt.show()
