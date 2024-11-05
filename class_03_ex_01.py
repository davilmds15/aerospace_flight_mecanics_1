import numpy as np
from sympy import symbols, Eq, solve, cos, sin, diff, Matrix

p, r, theta, theta0, r0, mu, h, e = symbols('p r theta theta0 r0 mu h e')
f, g, fp, gp = symbols('f g fp gp')

A = Matrix([[ r*cos(theta), r*sin(theta)], [-mu*sin(theta)/h, mu*(e + cos(theta))/h]])
B = Matrix([ [(e + cos(theta0))/p , -r0*sin(theta0)/h], [ sin(theta0)/p , r0*cos(theta0)/h ] ])
PHI = A*B
f = PHI[0,0]
g = PHI[0,1]
fp = PHI[1,0]
gp = PHI[1,1]
print("PHI  =   ",PHI)
print("f    =   ",f)
print("g    =   ",g)
print("fp   =   ",fp)
print("gp   =   ",gp)
