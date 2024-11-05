import numpy as np
from scipy.optimize import fsolve

h = 450 # [km] altitude
lat = 8 # [º] latitude
long = -48 # [º] longitude

vlin = 8.8 #km/s
Alin = 10*np.pi/180
philin = 5*np.pi/180

Re = 6378.137 # [km] earths radius
r0 = h + Re

t = 15+(5/60) # [h] UTC time 15h05

lambG = 5.27778e-5 # astronomical longitude of the Greenwich prime meridian
omegaE = 15 # [º/h] earth's rotation rate
long = lambG + omegaE*t + long
long = long*np.pi/180
lat = lat*np.pi/180

def equations(v, A, phi):
    eq1 = v*np.sin(phi) - vlin*np.sin(philin)
    eq2 = v* np.cos(phi)*np.sin(A) - r0*omegaE*np.cos(lat) - vlin* np.cos(philin)*np.sin(Alin)
    eq3 = v* np.cos(phi)*np.cos(A) - vlin* np.cos(philin)*np.cos(Alin)
    return eq1, eq2, eq3
