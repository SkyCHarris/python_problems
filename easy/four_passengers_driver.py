
#! Four Passengers and a Driver

# Typical car holds four passengers, one driver, allowing five to travel
# Given n number of people, return how  many cars are needed to seat everyone comfortably

import math

def cars_needed(n):
    cars_float = (n / 5)
    return math.ceil(cars_float)

cars_needed(5)
cars_needed(11)
cars_needed(0)

# Condensed

import math

def cars_needed(n):
    return math.ceil(n/5)

cars_needed(5)
cars_needed(11)
cars_needed(0)