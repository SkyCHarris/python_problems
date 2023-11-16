
#! Correct Inequality Signs

# Create a function that returns True if a given inequality expression is correct and False otherwise

def correct_signs(equation):
    return eval(equation)

correct_signs("3 < 7 < 11")
correct_signs("13 > 44 > 33 > 1")
correct_signs("1 < 2 < 6 < 9 > 3")