import numpy as np
import matplotlib.pyplot as plt
#from sympy import symbols, Eq, solve
from equations import *

#Exercise 6: Determine an expression for the velocity of a hyperbolic orbit 
# as the radial distance tends to infinity. This is called hyperbolic excess velocity.

G = 6.67259*10**-11 #gravitational constant
m1 = 5.9722*10**24 #Earth's mass in kg
mu = mu(G, m1)

p = 13300
e = 1.5 
a = semimajor(p, e)

r_0 = 10
r_lim = 10**18
r = np.linspace(r_0, r_lim, 100000)
v = velocity(mu, r, a)
v_lim = np.sqrt(mu/(-a))
print("mu = ", mu)
print("a = ", a)
print("v_lim = ",v_lim)

plt.figure(figsize=(10, 6))
plt.plot(r, v, label='Velocity curve')
plt.scatter(r_lim, v_lim, color='red')
#plt.plot(r_lim, v_lim)
plt.title('Orbit Velocity vs. Orbit Radius')
plt.xlabel('Orbit Radius [km]')
plt.ylabel('Velocity [km/s]')
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()