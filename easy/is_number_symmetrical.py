
#! Is the Number Symmetrical?

# Create a function that takes a number as an argument...
    # ...and returns True or False depending on whether the number is symmetrical or not

def is_symmetrical(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    return reversed_str == str(num)

is_symmetrical(7227)
is_symmetrical(12567)
is_symmetrical(44444444)

# Condensed (Edabit solutions)

def is_symmetrical(num):
    return str(num) == str(num)[::-1]