import numpy as np
from scipy.optimize import fsolve

h = 450     # [km] altitude
lat = 8     # [º] latitude
long = -48  # [º] longitude

vlin = 8.8              #km/s
Alin = 10*np.pi/180     # [rad]
philin = 5*np.pi/180    # [rad]

Re = 6378.137   # [km] earths radius
r0 = h + Re


t0 = 15+(5/60)  # [h] UTC time 15h05
t = t0 * 3600   # [s] UTC time 15h05

lambG = 219.30          # [º] astronomical longitude of the Greenwich prime meridian at 00:00:00 UTC
omegaE = 7.2921159e-5   # [rad/s] earth's rotation rate
long = lambG + (omegaE*180/np.pi)*t + long # [º]
long = long*np.pi/180   # [rad]
lat = lat*np.pi/180     # [rad]

#omegaE = omegaE*3600    # [rad/h] earth's rotation rate

def equations(vars):
    v, A, phi = vars
    eq1 = v*np.sin(phi) - vlin*np.sin(philin)
    eq2 = v* np.cos(phi)*np.sin(A) - r0*omegaE*np.cos(lat) - vlin* np.cos(philin)*np.sin(Alin)
    eq3 = v* np.cos(phi)*np.cos(A) - vlin* np.cos(philin)*np.cos(Alin)
    return [eq1, eq2, eq3]

guess = [vlin, Alin, philin]
v, A, phi = fsolve(equations, guess)
print("v =",v,"km/s")
print("A =", A*180/np.pi, "º")
print("phi =", phi*180/np.pi, "º")

vx = v*np.sin(phi)
vy = v*np.cos(phi)*np.sin(A)
vz = v*np.cos(phi)*np.cos(A)
Vhl = np.array([vx, vy, vz])

C_hl_c = np.array([[np.cos(lat)*np.cos(long), -np.sin(long), -np.cos(long)*np.sin(lat)], 
                  [np.cos(lat)*np.sin(long), np.cos(long), -np.sin(lat)*np.sin(long)],
                  [np.sin(lat), 0, np.cos(lat)]])

vX, vY, vZ = C_hl_c @ Vhl
Vc = np.array([vX, vY, vZ])
print("V_c =", Vc, "km/s")

Rhl = np.array([r0, 0, 0])
Rc = C_hl_c @ Rhl
print("R_c =", Rc, "km")

R = np.sqrt(Rc[0]**2 + Rc[1]**2 + Rc[2]**2)
m1 =5.972e24 # [kg]
G = 6.6743*10**(-11)*10**(-9) # [km3 kg-1 s-2]
mu = G*m1

h_vec = np.cross(Rc, Vc)
hx = h_vec[0]
hy = h_vec[1]
hz = h_vec[2]
e_vec = ((np.cross(Vc, h_vec)) / mu) - (Rc / r0)
e = np.linalg.norm(e_vec)
print("e = ",e)
h = np.linalg.norm(h_vec)

p = h**2 / mu
a = p / (1 - e**2)
print("a = ", a)

n = np.sqrt(mu/a**3)
theta0 = np.arccos(np.dot(Rc, e_vec)/(r0*e))


E0 = 2*np.arctan(np.sqrt((1-e)/(1+e))*np.tan(theta0/2))
tau = t - (E0-e*np.sin(E0))/n
print("tau =", tau)

#def KeplerEq(E, data):
#    e, M = data
#    return E - e*np.sin(E) - M
#def solveKepler(tau):
#    M = n*(t - tau)
#    data = [e, M]
#    guess = M
#    E = fsolve(KeplerEq, guess, args=data)[0]
#    return E
#Ep = solveKepler(tau)
#thetap = 2*np.arctan(np.sqrt((1+e)/(1-e))*np.tan(Ep/2))

K = np.array([0, 0, 1])
n_vec = np.cross(K, h_vec) / np.linalg.norm(np.cross(K, h_vec))
print("n_vec =", n_vec)
nx = n_vec[0]
ny = n_vec[1]
nz = n_vec[2]

Omega = np.arctan2(ny, nx)
print("Omega =", Omega, "[rad] longitude celeste do nodo ascendente")

i = np.arctan2(hx/np.sin(Omega), hz)
print("i = ", i, "[rad] inclination")


rp = a*(1-e)
print("h_p = ", rp-Re, "[km] perigee altitude")
