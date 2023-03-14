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
time_array = np.arange(a,b,h)

for time in time_array:
    x_of_t_soln.append(x)

    # define k1 and k2 then add eq
    # x(t+h) = x(t) + k2
    k1 = h * f(x,time)
    k2 = h * f(x+0.5*k1, time+0.5*h)
    x = x + k2
    #x = x+h * f(x, time)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(time_array, x_of_t_soln)
plt.show()
