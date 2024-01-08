
#! Drunken Python

# Python got drunk and the built-in functions str() int() are acting odd

# Create two functions to substitute str() and int()
# 1. Function int_to_str() converts ints to strs
# 2. Function str_to_int() converts strings to integers

def int_to_str(num):
    return str(num)

def str_to_int(num):
    return int(num)

int_to_str(4)
str_to_int("4")
int_to_str(29348)