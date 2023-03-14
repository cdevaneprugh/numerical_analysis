'''
Numerical integration using the trapezoidal rule.
Takes bounds a and b, and number of slices N as arguments.
Calls function defined as f for integration.
'''

# trapezoidal rule
def trapezoidal(a, b, N):    
    h = (b-a) / N # calculate h from given bounds
    
    s = 0.5 * ( f(a) + f(b) ) # initialize summation at zero
    
    # add right side of trapezoid to summation 
    # start at index 1
    for k in range(1, N):
        s += f(a + k*h)
    
    return s*h # return final calculated area
