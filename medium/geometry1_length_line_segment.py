
#! Geometry 1: Length of Line Segment

# Write a function that takes coordinates of two points on a 2d plane and returns the length of the line segment connecting those 2 points
import math

def line_length(dot1, dot2):
    line_distance = math.sqrt(((dot1[0] - dot2[0])**2) + ((dot1[1] - dot2[1])**2))
    return round(line_distance, 2)

line_length([15, 7], [22, 11])
line_length([0, 0], [0, 0])
line_length([0, 0], [1, 1])

# Condensed

def line_length(dot1, dot2):
    return round(math.dist(dot1, dot2), 2)

line_length([15, 7], [22, 11])
line_length([0, 0], [0, 0])
line_length([0, 0], [1, 1])
