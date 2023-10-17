
#! Calculate Using String Operation

# Create a function that takes two numbers and a mathematical operator and returns the result

def calculate(num1, num2, operator):
    new_string = str(num1), str(operator), str(num2)
    return eval(new_string)

calculate(4, 9, "+")

# Attempt 2

def calculate(num1, num2, operator):
    new_string = ''
    new_string += num1, operator, num2
    return eval(new_string)

calculate(4, 9, "+")

# Attempt 3

def calculate(num1, num2, operator):
    new_num1 = str(num1)
    new_num2 = str(num2)
    new_string = str(num1, operator, num2)
    return eval(new_string)

calculate(4, 9, "+")

# Actual

def calculate(num1, num2, op):
    return eval(str(num1 + op + str(num2)))

calculate(4, 9, "+")