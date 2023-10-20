
#! Flip the Boolean

# Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given

def reverse(boolean):
    if isinstance(boolean, bool) == True:
        return not boolean
    else:
        return "boolean expected"

reverse(True)
reverse(False)
reverse(0)
reverse(None)