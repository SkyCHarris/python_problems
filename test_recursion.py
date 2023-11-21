
#! Python Recursion

# Recursion is the process of defining something in terms of itself

# Ex. 2 parallel mirrors facing each other
    # Any object in between them would be reflected recursively

#? Python Recursive Function

# A function can call other functions in Python
# Functions can call themselves
# These types of constructs are called recursive functions

def recurse():

    recurse()

recurse()


#* Recursive function -> Find the Factorial of an Integer

def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    
num = 3
print("The facotrial of", num, "is", factorial(num))

# In this example, factorial() is a recursive function as it calls itself
# When we call this function with a positive integer, it will recursively call itself by decreasing the number
# Each function multiplies the number with the factorial of the number below it until it is equal to one
# Our recursion ends when the number reduces to 1.
    # This is called base condition

# Every recursive funciton must have a base condition that stops the recursion, or else the function calls itself infinitely
    # Python interpreter limits depths of recursion to avoid this and stack overflows
    # Max default depth of recursion is 1000
    # RecursionError

def recursor():
    recursor()
recursor()
# RecursionError limit


#* Advantages of Recursion

# 1. Recursive functions make the code look clean and elegant
# 2. A complex task can be broken down into simpler sub-problems w/ recursion
# 3. Sequence generation is easier with recursion than using some nested iteration

#* Disadvantages of Recursion

# 1. Sometimes the logic behind recursions is hard to follow through
# 2. Recursive calls are expensive (inefficent) and take up a lot of memory and time
# 3. Recursive functions are hard to debug