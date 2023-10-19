
#! Number Split

# Given a number, return a list containing the two halves of the number
# If the number is odd, make the rightmost number higher

import math

def number_split(num):
    if num % 2 == 0:
        num_list = [math.floor(num/2), math.floor(num/2)]
        return num_list
    elif num % 2 != 0:
        num_list = [math.floor(num/2), math.floor(num/2) + 1]
        return num_list

number_split(4)
number_split(10)
number_split(11)
number_split(-9)