
#! Many Operators!

# Via three parameters, use the operator parameter on num1 and num2

def operate(num1, num2, operator):
    new_string = str(num1) + operator + str(num2)
    return eval(new_string)

operate(1, 2, "+")
operate(7, 10, "-")