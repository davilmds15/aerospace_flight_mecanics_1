import numpy as np

def mu(G, m1):
    mu = G * m1
    return mu
    
def parameter(e, a):
    p = a * (1 - e**2)
    return p

def semimajor(p, e):
    if e ==1:
        a = float('inf')
        return a
    else:
        a = p / (1 - e**2)
        return a

def semimajor2(r, v, mu):
    term1 = 2/r
    term2 = (v**2)/mu
    result = term1 - term2
    a = 1/result
    return a

def parameter2(r, e, theta):
    p = r * (1 + e*np.cos(theta))
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

def angular_momentum2(r, omega):
    h = (r**2) * omega
    return h

def areal_velocity(h):
    dA = h / 2
    return dA

def phi(theta, e):
    denominator = 1 + e * np.cos(theta)
    phi = np.where(
        np.isclose(denominator, 0),
        np.where(np.sin(theta)>0, np.pi/2, -np.pi/2),
        np.arctan2(e*np.sin(theta), denominator)
    )
    return phi

def theta(p, r, e):
    value = ((p / r) - 1) / e
    value = np.clip(value, -1, 1)
    theta = np.arccos(value)
    return theta

def eccentricity(p, a):
    return np.sqrt(1 - (p/a))