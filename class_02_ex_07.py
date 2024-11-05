import numpy as np
from sympy import symbols, Eq, solve
from equations import *
import matplotlib.pyplot as plt

#Exercise 7: Determine the hyperbolic excess velocity from Exercise 3

r_p = 6650 #km
e = 1.15
theta = np.pi/2
G = 6.67259*10**-11 #gravitational constant
m1 = 5.9722*10**24 #Earth's mass in kg
mu = mu(G, m1)

rp_s, a_s, e_s = symbols('rps a_s es')
rp_equation = Eq(rp_s, -a_s * (e_s - 1))
a_sym = solve(rp_equation.subs({rp_s: r_p, e_s: e}), a_s)
a = float(a_sym[0])
print("a    =   ", a)

p = parameter(e, a)
print("p    =   ", p)

r_p = radius(p, e, 0)
v_p = velocity(mu, r_p, a)
h = angular_momentum(r_p, v_p, 0)
print("h    =   ", h)

dA = areal_velocity(h)
print("dA   =   ", dA)

print("v_p  =   ", v_p)

R = radius(p, e, theta)
v = velocity(mu, R, a)
print("v    =   ", v)
phi = phi(theta, e)
print("phi  =   ", phi)
print("no conversion of unit was executed")

r_0 = r_p
r_lim = 10**25
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
