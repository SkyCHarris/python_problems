
#! Curzon Numbers

# In this challenge, establish if a given integer num is a Curzon number:
    # If 1 plus 2 elevated to num is exaclty divisible by 1 plus 2 multiplied by num, then num is a Curzon number

# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise

def is_curzon(num):
    test_1 = 2**num + 1
    test_2 = 2*num + 1
    return test_1 % test_2 == 0

is_curzon(5)
is_curzon(10)
is_curzon(14)