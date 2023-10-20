
#! Triangular Number Sequence

# This Triangular Number Sequence is generated from a pattern of dots that form a triangle
# The first 5 numbers of the sequence, or dots, are:

# 1, 3, 6, 10, 15

# This means the first triangle has one dot, second has three dots, third has 6 dots, etc.

# Write a function that returns the number of dots when given its corresponding triangle number of the sequence

def triangle(tri_num):
    return int(tri_num * (tri_num + 1) / 2)

triangle(1)
triangle(6)
triangle(215)