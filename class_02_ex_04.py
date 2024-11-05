import numpy as np
from sympy import symbols, Eq, solve
from equations import *

'''
Exercise 4: If a geocentric parabolic orbit has r_p = 6650km, determine:
(a) The semi-major axis a;
(b) The parameter p;
(c) The specific angular momentum h;
(d) The areal velocity dA;
(e) The perigee velocity v_p;
(f) The velocity v and trajectory angle phi for theta = pi/2.
'''

rp = 6650
e = 1 #parabolic orbit
theta = np.pi/2
G = 6.67259*10**-11 #gravitational constant
m1 = 5.9722*10**24 #Earth's mass in kg
mu = mu(G , m1)

p = parameter2(rp, e, 0)
a = semimajor(p, e)
print("a    =   ", a)
print("p    =   ", p)

r_p = radius(p, e, 0)
v_p = velocity(mu, r_p, a)
h = angular_momentum(r_p, v_p, 0)
print("h    =   ", h)

dA = areal_velocity(h)
print("dA   =   ", dA)
print("v_p  =   ", v_p)

r = radius(p, e, theta)
v = velocity(mu, r, a)
phi = phi(theta, e)
print("v    =   ", v)
print("phi  =   ", phi)
