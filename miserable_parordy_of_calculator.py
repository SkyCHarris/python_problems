
#! Miserable Parody of a Calculator

# Create a function that will handle simple math expressions.
# The input is an expression inthe form of a string

def calculator(txt):
    return eval(txt)

calculator("23+4")
calculator("45-15")
calculator("13+2-5*2")