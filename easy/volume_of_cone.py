
#! Volume of a Cone

# Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth.

import math
from fractions import Fraction

def cone_volume(h, r):
    if h == 0 or r == 0:
        return 0
    else:
        volume = Fraction(1,3) * math.pi * r**2 * h
        return round(volume, 2)
    
cone_volume(3,2)
cone_volume(15,6)
cone_volume(18,0)