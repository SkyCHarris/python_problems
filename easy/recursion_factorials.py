
#! Recursion: Factorials

# Write a function that calculates the factorial of a number recursively

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
    
factorial(5)