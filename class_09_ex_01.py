import numpy as np

# Exercício 1: Escreva um programa para integrar numericamente as equações do movimento 
# de dois corpos com perturbação, cuja órbita inicial é circular terrestre com 400 km de altitude.
# A aceleração perturbativa é uma desaceleração (de-boost) constante de 2 m/s2 aplicada por 500
# s. Ignore a variação de massa provocada pelo disparo dos motores foguete. Calcule os elementos
# orbitais da órbita obtida após o disparo dos retro foguetes.
# Assuma o raio médio da Terra: Re = 6378, 14 km.

h = 400e3 # [m] altitude
Re = 6378.14e3 # [m] earths radius

G = 6.6743e-11 # [m3 kg-1 s-2]
m1 = 5.9722e24 # [kg]
ri = h + Re # [m] apogee of the first orbit
ei = 0
ai = ri

ad = 2 # [m/s**2] perturbatie acceleration
td = 500 # [s]

mu = G*m1 # [m3 s-2]
vi = np.sqrt(mu*(2/ri - 1/ai)) # [m/s]
print("vi =", vi, "[m/s]")

deltav = ad * td # [m/s]
vf = vi - deltav
raf = ri
af = 1 / (2/raf - vf**2/mu)
print("af   =", af/1000, "[km]")
rpf = af*2 -raf
print("rpf  =", rpf/1000, "[km] Perigee final orbit")
print("raf  =", raf/1000, "[km] Apogee final orbit")
print("Re   =", Re/1000, "[km]  Earth's radius")

ef = (raf-rpf)/af
print("ef   =", ef, "Eccentricity final orbit")
pf = np.abs(af*(1 - ef**2)) 
print("pf =", pf, "[m]")
hf = np.sqrt(pf*mu)
print("hf =", hf)
phif = np.arccos(np.clip(hf/raf*vf, -1, 1))
print("phif =", phif, "[rad]")
thetaf = np.arccos((pf-raf)/(ef*raf))
n = np.sqrt(mu/af**3) # [rad/s]
Tf = 2*np.pi / n
print("Tf =", Tf/3600, "[h] Orbital period")
