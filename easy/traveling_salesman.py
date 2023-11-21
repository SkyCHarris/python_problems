
#! Traveling Salesman Problem

# A salesman has a number of cities to visit
# He wants to calculate the total number of possible paths he could take, visiting each city once before returning home
# Return the total number of possible paths a salesman can travel, given n cities

import math

def paths(n):
    return math.factorial(n)

paths(4)
paths(1)
paths(9)