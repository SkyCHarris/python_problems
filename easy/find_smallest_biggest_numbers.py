
#! Find the Smallest and Biggest Numbers

# Create a function that takes an array of numbers and return both the minimum and maximum numbers, in that order

def minMax(lst):
    sorted_list = lst.sort()
    mini = min(sorted_list)
    maxi = max(sorted_list)
    return [mini, maxi]

minMax([1, 2, 3, 4, 5])
minMax([2334454, 5])
minMax([1])

# Attempt 2

def minMax(lst):
    return [min(lst), max(lst)]

minMax([1, 2, 3, 4, 5])
minMax([2334454, 5])
minMax([1])