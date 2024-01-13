
#! Total Volume of All Boxes

# Given a list of boxes, create a function that returns the total volume of all boxes combined together
# A box is represented by a list with 3 elements: length, width, height


import numpy

def total_volume(*boxes):
    sum = 0
    for i in boxes:
        sum += numpy.prod(i)
    return sum

total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1])
total_volume([2, 2, 2], [2, 1, 1])
total_volume([1, 1, 1])