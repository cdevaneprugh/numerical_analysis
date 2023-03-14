import numpy as np
import matplotlib.pyplot as plt

# dx/dt = x*y - x
# dy/dt = y - xy + sin^2 (omega*t)
# r = [x, y]

def f(r, t):
    x = r[0]
    y = r[1]

    fx = x*y - x
    fy = y - x*y + np.sin(t)**2 # omega = 1
    
    fr = np.array([fx, fy], float)
    return fr

a = 0
b = 10
N = 100
h = (b-a) / N

time = np.arange(a,b,h)
x_soln = []
y_soln = []

x0 = 1.
y0 = 1.

r = np.array([x0, y0])

for t in time:
    x_soln.append( r[0] )
    y_soln.append( r[1] )

    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)

    r += (k1 + 2.*k2 + 2.*k3 + k4) / 6.

#print(x_soln)
#print(y_soln)

plt.figure()
plt.plot(time, x_soln, label='x')
plt.plot(time, y_soln, label = 'y')
plt.legend()
plt.show()
