
#! Return the Factorial

# Create a function that takes an integer and returns the factorial of that integer
# That is, the integer multiplied by all positive lower integers

def factorial(num):
    x = 0
    for x in range(num):
        x *= x
    return x

factorial(3)
factorial(5)
factorial(13)

# Attempt 2

def factorial(num):
    if num == 1:
        return num
    else:
        return num * (num-1)
    
factorial(3)
factorial(5)
factorial(13)

# Attempt 3

def factorial(num):
    for x in range(num):
        x  = x * (x -1)
    return x

factorial(3)
factorial(5)
factorial(13)

# Attempt 4

def factorial(num):
    facto = num
    while facto > 0 :
        facto = num - 1
        product = facto * facto
    return facto


factorial(3)
factorial(5)
factorial(13)

# Attempt 5

import math

def factorial(num):
    facto = 0
    while num > 0:
        facto *= num
        num -= 1
    return facto

factorial(3)
factorial(5)
factorial(13)

# Attempt 6

import math

def factorial(num):
    return math.factorial(num)

factorial(3)
factorial(5)
factorial(13)