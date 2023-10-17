# Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers

# Notes:
    # -(side1 + side2) - 1 = maximum range of the third edge
    # The side lengths of the triangle are positive integers

def max_edge(side1, side2):
    third_edge = (side1 + side2) - 1
    print(third_edge)
    return third_edge

max_edge(8, 10)
max_edge(5, 7)
max_edge(9, 2)
