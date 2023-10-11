
#! Flip the Boolean

# Due to a programming concept known as truthiness, certain values can be evaluated to booleans
# Ex. 1 (or any number other than 0) is often equivalent to True, and 0 is often equivalent to False

def flip_bool(b):
    return int(not b)

flip_bool(True)
flip_bool(False)
flip_bool(1)
flip_bool(0)