import numpy as np
from equations import *
from scipy.optimize import fsolve

# [Portuguese]: Exercício 1 Um veículo espacial foi observado numa órbita terrestre com altitude, 
# velocidade e ângulo de trajetória de 1.000 km, 10 km/s e −25°, respectivamente. 
# Determine a posição e a velocidade no referencial perifocal 20 horas depois que a 
# observação foi tomada.



r0 = 1000*10**3 # [m]
re =  6378137 # [m] earths radius
r0 = r0 + re
v0 = 10*10**3 # [m/s]
phi0 = -25*np.pi/180 #trajectory angle [rad]
t0 = 0 #seconds

# Goal: Position and Velocity at t=20h
t = 20*3600 #seconds

G = 6.67259*10**-11 #gravitational constant [m^3/kg*s^2]
m1 = 5.9722*10**24 #Earth's mass [kg]
mu = G*m1

v_lin = v0*np.cos(phi0)
omega_0 = v_lin/r0
h = angular_momentum2(r0, omega_0)
p = (h**2)/mu
a = semimajor2(r0, v0, mu) 
e = eccentricity(p, a)

theta0 = np.arccos( ( np.cos(phi0)*h*v0/mu - 1 ) / e )
tau = 0

n = np.sqrt(mu/a**3)

def KeplerEllipse(E, *dados):
    e, M = dados
    return E - e*np.sin(E) - M

def solveKeplerEllipse(t):
    M = n*(t - tau)
    E0 = M
    dados = (e, M)
    E = fsolve(KeplerEllipse, E0, args=dados)
    return E

E = solveKeplerEllipse(t)[0]
print("E = ", E)

tan_half_theta = np.sqrt((1+e)/(1-e))*np.tan(E/2)
theta = 2*np.tan(tan_half_theta)
print("theta = ", theta*180/np.pi)

r = radius(p, e, theta)
v = velocity(mu, r, a)
print("radius = ", r, " m")
print("velocity = ", v, " m/s")
