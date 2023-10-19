
#! Solving Exponential Equations with Logarithms

# Create a function that takes a number a and finds the missing exponent x so that:
# a when raised to the power of x is equal to b

def solve_for_exp(a, b):
    square_root_b = b**(1/2)
    if a ** square_root_b == b:
        return a
    
# Attempt 2

def solve_for_exp(a, b):
    x = b**(1/2)
    return x

solve_for_exp(4, 1024)
solve_for_exp(2, 1024)
solve_for_exp(9, 3486784401)

# Attempt 3

import math

def solve_for_exp(a, b):
    return round(math.log(b, a))

solve_for_exp(4, 1024)
solve_for_exp(2, 1024)
solve_for_exp(9, 3486784401)