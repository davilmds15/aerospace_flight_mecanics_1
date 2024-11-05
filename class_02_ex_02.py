'''
Exercise 2: If a geocentric Keplerian orbit has a=7000km and 𝑒=0.05, determine: 
(a) The parameter p; 
(b) The specific angular momentum h; 
(c) The areal velocity; 
(d) The perigee and apogee radii; 
(e) The perigee and apogee velocities; 
(f) The velocity and trajectory angle for 𝜃=𝜋/2
'''
import numpy as np
#import matplotlib.pyplot as plt

a = 7000
e = 0.05
G = 6.67259*10**-11
m1 = 5.9722*10**24

def mu(G, m1):
    mu = G * m1
    return mu
    
def parameter(e, a):
    p = a * (1 - e**2)
    return p

def radius(p, e, theta):
    r = p / (1 + e * np.cos(theta))
    return r

def velocity(mu, r, a):
    v = np.sqrt( (mu / r) * (2 - r/a) )
    return v

def angular_momentum(r, v, phi):
    h = r * v * np.cos(phi)
    return h

def areal_velocity(h):
    dA = h / 2
    return dA

def phi(theta, e):
    phi = np.arctan((e * np.sin(theta)) / (1 + e * np.cos(theta)))
    return phi

p = parameter(e, a)
print("Parameter p =                        ", p, "km")

mu = mu(G, m1)
r_p = radius(p, e, 0)
v_p = velocity(mu, r_p, a)
h = angular_momentum(r_p, v_p, 0)
print("Specific angular momentum h =        ", h)

dA = areal_velocity(h)
print("Areal velocity =                     ", dA)

r_a = radius(p, e, np.pi)
print("Perigee radius r_p =                 ", r_p, " km")
print("Apogee radius r_a =                  ", r_a, " km")

v_a = velocity(mu, r_a, a)
print("Perigee velocity v_p =               ", v_p, "km/s")
print("Apogee velocity v_a =                ", v_a, "km/s")

r = radius(p, e, np.pi/2)
v = velocity(mu, r, a)
phi = phi(np.pi/2, e)
print("Velocity for 𝜃=𝜋/2 is v =            ", v/3.6, "km/s")
print("Trajectory angle for 𝜃=𝜋/2 is phi =  ", phi*180/np.pi, "º")
