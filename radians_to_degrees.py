
#! Radians to Degrees

# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place

import math

def radians_to_degrees(radians):
    return round(180 / math.pi * radians, 1)

radians_to_degrees(1)
radians_to_degrees(20)
radians_to_degrees(50)


# 1 radian = 180 degrees