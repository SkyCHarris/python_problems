
#! Quadratic Equation

# Create a function to find the root value of x in any quadratic equation
# 3 args:
# a is coefficient of x^2
# b is coefficient of x
# c is constant term

import math

def quadratic_equation(a, b, c):
    top = (b) + (b**2) - (4*a*c)
    sqrt_top = math.sqrt(top)
    bottom = sqrt_top / 2*a
    return bottom


quadratic_equation(1, 2, -3)
quadratic_equation(2, -7, 3)
quadratic_equation(1, -12, -28)

# Attempt 2

import math

def quadratic_equation(a,b,c):
    top = (b*-1) + (math.sqrt((b**2) - (4*a*c)))
    bottom = top / (2*a)
    return round(bottom)

quadratic_equation(1, 2, -3)
quadratic_equation(2, -7, 3)
quadratic_equation(1, -12, -28)

# Attempt 3

import math

def quadratic_equation(a,b,c):
