
#! Recreating the abs() Function

# The abs() function returns the absolute value of a number.
# This means it returns a number's positive value
    # It's the distance away from zero
# Create a function that recreates this functionality

def absolute(num):
    if num > 0:
        return num
    else:
        return num * -1
    
absolute(-5)
absolute(-3.14)
absolute(250)