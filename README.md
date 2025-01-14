# Aerospace Flight Mechanics Exercises

## `equation.py`
This repository provides a collection of Python functions for solving exercises related to orbital mechanics. 
The core functionality resides in `equations.py` and defines functions for calculating various orbital parameters.

### Key equations
* Gravitational Parameter: `mu(G, m1)`
* Orbital Parameter: `parameter(e, a)`
* Semi-Major Axis: `semimajor(p, e)` & `semimajor2(r, v, mu)`
* Orbital Radius: `radius(p, e, theta)`
* Orbital Velocity: `velocity(mu, r, a)`
* Angular Momentum: `angular_momentum(r, v, phi)` & `angular_momentum2(r, omega)`
* Areal Velocity: `areal_velocity(h)`
* True Anomaly: `phi(theta, e)`
* Eccentric Anomaly: `theta(p, r, e)`
* Eccentricity: `eccentricity(p, a)`

## Note
This repository focuses on solving exercises using these equations. Refer to the individual Python files for specific implementations.
