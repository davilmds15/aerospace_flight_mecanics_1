import numpy as np
from equations import *

# Exercise 3 A satellite is in Earth orbit with e = 0.00132, i = 89.1° and ω = 261°.
# Its perigee altitude is 917 km. What is the maximum height of the satellite above the equatorial plane?

e = 0.00132
i = 89.1 * np.pi / 180
omega = 261 * np.pi / 180
alt_p = 917 #[km]
Re = 6378.137 # [km] earths radius
rp = alt_p + Re
a = rp / (1 - e)
height = a * np.sin(i)
print("height =", height, "km")
