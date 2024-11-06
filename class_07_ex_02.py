import numpy as np
from scipy.optimize import fsolve

ei = 0.7
h = 500 #km
Re = 6378.137   # [km] earths radius
ri = (h + Re)*10**3 # [m]
vi = 7.4e3 # [m/s]
betha = 60*np.pi/180 # [rad]

deltav = 500 # [m/s]

m1 = 5.9722e24 # [kg]
G = 6.6743e-11 # [m3 kg-1 s-2]
mu = m1*G
a_inv = 2/ri - vi**2/mu
ai = 1/a_inv # [m]
pi = ai*(1-ei**2)
h = np.sqrt(pi*mu)

rpi = pi / (1 + ei * np.cos(0))
rai = pi / (1 + ei * np.cos(np.pi))

def equation(vars):
    vf, alpha = vars
    eq1 = deltav*np.sin(betha) - vf*np.sin(alpha)
    eq2 = deltav**2 - vf**2 - vi**2 + 2*vf*vi*np.cos(alpha)
    return eq1, eq2

guess = [vi+1000, 0]
vf, alpha = fsolve(equation, guess)
print("vf =", vf)
print("alpha =", alpha)

a_inv = 2/ri - vf**2/mu
af = 1/a_inv # [m]
print("af =", af)

phif = alpha
hf = ri*vf*np.cos(phif)
pf = hf**2 /mu

ef = np.sqrt(1 - pf/af)
print("ef =", ef)

raf = pf/(1-ef)
rpf = 2*af - raf
print("raf =",raf)
print("rpf =",rpf)
