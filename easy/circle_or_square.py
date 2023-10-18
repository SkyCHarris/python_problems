
#! Circle or Square

# Given the raidus of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter
# Return False if the square's perimeter is greater than the circumference of the circle

import math

def circle_or_square(radius, area):
    circumference = 2 * math.pi * radius
    perimeter = math.sqrt(area) * 4
    return circumference > perimeter

circle_or_square(16, 625)
circle_or_square(5, 100)
circle_or_square(8, 144)