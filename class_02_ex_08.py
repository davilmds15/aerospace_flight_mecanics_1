import numpy as np
from equations import *
from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt

# Exercise 8: Determine an expression for the asymptote angle of a hyperbolic trajectory. 
# What happens when the eccentricity approaches 1? 
# That is, in the limit where the hyperbolic trajectory approaches a parabolic one.

N = 3
e1 = 0
e2 = 0.5
e3 = 0.99999
e4 = 1.2
p = 1

theta = np.linspace(-np.pi, np.pi, 500)
theta2=np.linspace(-3*np.pi/4, 3*np.pi/4,500)

r1 = radius(p, e1, theta)
r2 = radius(p, e2, theta)
r3 = radius(p, e3, theta)
r4 = radius(p, e4, theta2)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.plot(theta, r1,label='e=0')
ax.plot(theta, r2,label='e=0.5')
ax.plot(theta, r3, label='e=0.99999')
ax.plot(theta2, r4,label='e=1.2')

ax.set_rmax(3)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-20)  # Move radial labels away from plotted line

ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')
ax.legend()
plt.show()
