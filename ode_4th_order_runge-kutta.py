import numpy as np
import matplotlib.pyplot as plt

# dx/dt = -x^3 + sin(t)
# solve for x from [0,10]

def f(x, t):
    return -1*x**3 + np.sin(t)

# parameters
a = 0
b = 10
N = 100
h = (b-a) / N

# general formula for euler is:
# x(t+h) = x(t) + h*f(x,t)

# initial condition
x = 0
x_of_t_soln = []
time = np.arange(a,b,h)

for t in time:
    x_of_t_soln.append(x)

    # fourth order
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1, t+0.5*h)
    k3 = h*f(x+0.5*k2, t+0.5*h)
    k4 = h*f(x+k3, t+h)

    x += 1/6 * (k1 + 2*k2 + 2*k3 + k4)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(time, x_of_t_soln)
plt.show()
