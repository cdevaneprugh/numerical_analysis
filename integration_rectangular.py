'''
Numerical integration using the rectanlular rule.
Takes bounds a and b, and number of slices N as arguments.
Calls function defined as f for integration.
'''

# rectangular rule
def rectangular(a, b, N):
    h = (b-a) / N  # calculate h from given bounds 
    
    s = 0 # initialize summation at zero
    
    # add left side of rectangle to summation
    # start at index 0
    for k in range(N):
        s += f(a + k*h)
        
    return s*h # return final calculated area
