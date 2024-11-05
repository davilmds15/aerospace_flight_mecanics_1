import numpy as np
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve, sin

n = 0.002725257913632536
e =  2.770587807850761
tau = 0
t = 1000

print("______Using fsolve______")
def kepler(E):
    return n * (t - tau) - (E - e * np.sin(E))
E0 = n * (t - tau)
E_solution = fsolve(kepler, E0)[0]
print("t =", t, "s")
print("E =", E_solution)

print("______Using solve______")
n_s, t_s, tau_s, E_s, e_s = symbols('n_s t_s tau_s E_s e_s')
equation = Eq(n_s*(t_s - tau_s), E_s - e_s*sin(E_s))
E= solve(equation.subs({n_s: n, e_s: e, tau_s: tau, t_s: t}), E_s)
E = float(E[0])
print("t =", t, "s")
print("E =", E)

