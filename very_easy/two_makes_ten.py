# Create a function that takes two arguments.
# Both arguments are integers a and b. 
# Return True if one of them is 10 or if their sum is 10

def makes10(a, b):
    if (a == 10 or b == 10) or (a + b == 10):
        return True
    else:
        return False
    
# Attempt 2 (condense)

def makes10(a, b):
    return a == 10 or b == 10 or (a + b == 10)