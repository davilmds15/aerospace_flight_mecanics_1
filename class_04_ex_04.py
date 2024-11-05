import numpy as np
from equations import *
from scipy.optimize import fsolve

# [Portuguese]: Exercício 4 O último periélio do cometa Halley foi em 9 de fevereiro de 1986. Ele tem um
# semi eixo maior de 17,9564 a.u. (unidades astronômicas) e excentricidade e = 0, 967298. 
# Faça a predição do próximo periélio, e da posição atual do cometa.


e =  0.967298
a_u = 149597870.7 # [km] astronomical unit
a = 17.9564*a_u
mu =  132712440.018 # [km^3/s^2]
T_0 = 1986 # [year] in which Halley passed by

theta0 = 0
p = parameter(e, a)
rp = radius(p, e, theta0)

n = np.sqrt(mu/a**3)
T = 2*np.pi/n
T_h = T/3600 #[h]
T_day = T_h/24 #[days]
T_month = T_day/30 #[months]
T_year = T_month / 12 #[years]

T_year = T_year + T_0
print("next perihelion in", int(T_year), "years")
