import numpy as np
import matplotlib.pyplot as plt

# dx/dt = alpha*x - beta*x*y
# dy/dt = gamma*x*y - delta*y
# alpha=1, beta=0.5, gamma=0.5, delta=2
# r = [x, y]

def f(r, t):
    x, y = r[0], r[1]
    
    # Lotka-Volterra equations
    fx = x - (0.5*x*y) # rabbits
    fy = (0.5*x*y) - (2*y) # foxes

    fr = np.array([fx, fy], float)
    return fr

# time parameters
a = 0
b = 30
N = 1000
h = (b-a) / N
time = np.arange(a,b,h)

x_soln = []
y_soln = []

# initial conditions
x0 = 2.
y0 = 2.

r = np.array([x0, y0])

for t in time:
    # add values to lists
    x_soln.append( r[0] )
    y_soln.append( r[1] )
    
    # runge-kutta k values
    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)
    
    # update r
    r += (k1 + 2.*k2 + 2.*k3 + k4) / 6.

plt.figure()
plt.plot(time, x_soln, label='Prey')
plt.plot(time, y_soln, label = 'Predators')
plt.title("Predator and Prey Populations")
plt.ylabel("Population")
plt.xlabel("Time")
plt.legend()
plt.show()
