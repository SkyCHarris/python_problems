# Given two numbers, return True if the sum of both numbers is less than 100.
# Otherwise return False

def less_than_100(num1, num2):
    if num1 + num2 < 100:
        return True
    else:
        return False
    
# Option 2

def less_than_100(num1, num2):
    return num1 + num2 < 100