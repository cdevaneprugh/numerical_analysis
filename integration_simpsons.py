'''
Numerical integration using the simpsons rule.
Takes bounds a and b, and number of slices N as arguments.
Calls function defined as f for integration.
'''

# simpsons rule
def simpsons(a, b, N):
    h = (b-a) / N # calculate h from given bounds
     
    s = f(a) + f(b) # initialize summation
    
    # add odd terms
    for k in range(1, N, 2):
        s += 4 * f(a + k*h)
    
    # add even terms
    for k in range(2, N, 2):
        s += 2 * f(a + k*h)
    
    return (1/3)*h*s # return final calculated area
