import numpy as np
from equations import *
from scipy.optimize import fsolve

# [Portuguese]: Exercício 3 Uma trajetória hiperbólica de escape terrestre tem uma velocidade de perigeu 
# de 15 km/s em uma altitude de 300 km. Calcule:
# (a) O semi eixo maior a;
# (b) A excentricidade e;
#(c) O parâmetro p;
# (d) A velocidade de excesso hiperbólica (limite da velocidade para o tempo tendendo ao infnito);
# (e) O raio e a velocidade quando a anomalia verdadeira é 100°.
# (f) O tempo desde o periastro para a anomalia verdadeira de 100°

vp = 15000 # [m/s]
rp = 300000 # altitude [m] 
re =  6378137 # [m] earths radius
rp = rp + re
theta0 = 0
tau = 0

G = 6.67259*10**-11 #gravitational constant [m^3/kg*s^2]
m1 = 5.9722*10**24 #Earth's mass [kg]
mu = G*m1

a = semimajor2(rp, vp, mu)
print("a                =   ", a, " m")

def sistema(vars):
    e, p = vars
    eq1 = e**2 + (p / a) - 1
    eq2 = rp * e - p + rp
    return [eq1, eq2]

initial_guess = [1.5, a] # Trying e>1 because we have a hyperbolic trajectory
e, p = fsolve(sistema, initial_guess)
print("e                =   ",e)
print("p                =   ", p, " m")

v_lim = np.sqrt(mu/(-a)) # velocity at t = infinite
print("v_lim            =   ", v_lim, " m/s")

theta = 100*np.pi/180
r = radius(p, e, theta)
v = velocity(mu, r, a)
print("r(theta=100º)    =   ", r, "m")
print("v(theta=100º)    =   ", v, "m")

H = np.log( ( np.sqrt(e + 1) + np.sqrt(e - 1)*np.tan(theta/2) ) / (np.sqrt(e + 1) - np.sqrt(e - 1)*np.tan(theta/2) ))
Mh = e*np.sinh(H) - H
t = tau + Mh*np.sqrt( (p**3) / mu ) / ( (e**2 - 1)**(3 / 2) )
print("t                =   ", t, " s")

n = np.sqrt(mu/-a**3)
print("n = ", n)