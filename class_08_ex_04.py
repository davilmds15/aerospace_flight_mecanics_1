# [Portuguese]: Exercício 4: Um satélite de comunicação terrestre está em uma órbita equatorial 
# de altitude de apogeu 41.756 km e excentricidade 0,0661. Qual é o mínimo impulso de velocidade
# total requerido para colocar o satélite em órbita geoestacionária?

import numpy as np

hi = 41756 #[km]
Re = 6378.137 # [km] earths radius
ri = hi + Re # [km] apogee of the first orbit
rp1 = ri
e1 = 0.0661
a1 = ri / (1 + e1)
G = 6.6743*10**(-11)*10**(-9) # [km3 kg-1 s-2]
m1 = 5.9722e24 # [kg]
mu = G * m1

T = 24*3600 # [s] Geostationary orbit period
ah = ((T/np.pi)**2 * mu)**(1/3) # [s] transfer orbit period
rah = 2*ah - rp1

e2 = 0
a2 = rah # [km] because it is GEOsync

# apogee and perigee speeds of the transfer orbit
vah = np.sqrt(mu * (2/rah - 1/ah))
print("vah =", vah, "[km/s]")
vph = np.sqrt(mu * (2/rp1 - 1/ah))
print("vph =", vph, "[km/s]")

# speeds of the initial and final orbits
# at the impulse aplication sites
vi = np.sqrt(mu * (2/ri - 1/a1))
vf = np.sqrt(mu * (2/rah - 1/a2))

deltaV1 = vph - vi
deltaV2 = vf - vah
print("deltaV1 =", deltaV1, "[km/s]")
print("deltaV2 =", deltaV2, "[km/s]")
