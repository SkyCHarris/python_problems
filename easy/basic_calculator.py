
#! Basic Calculator

# Create a function that takes two numbers and a mathematical operator
# Then performs a calculation with the given numbers

def calculator(num1, operator, num2):
    stringy = str(num1) + operator + str(num2)
    if num2 == 0:
        return "Can't divide by 0!"
    else:
        return eval(stringy)

calculator(2, "+", 2)
calculator(2, "*", 2)
calculator(4, "/", 2)