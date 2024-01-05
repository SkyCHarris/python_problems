
#! Repeating Letters

# Create a function that takes a string and returns a string in which each character is repeated once

def double_char(txt):
    doubled = [str(x) + str(x) for x in txt]
    joined = ''.join(doubled)
    return joined

double_char("String")
double_char("Hello World!")


# Beautiful condensed

def double_char(txt):
    return ''.join([c*2 for c in txt])

double_char("String")
double_char("Hello World!")