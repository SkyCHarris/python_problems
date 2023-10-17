# Create a recursive function that takes two parameters and repeats the string 'n' number of times
# The first parameter 'tx' is the string to be repeated
# The second parameter is the number of times the string is to be repeated

def repetition(txt, n):
    return n * str([txt])

# Attempt 2

def repetition(txt, n):
    return n * txt