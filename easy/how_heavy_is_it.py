
#! How Heavy Is It?

# Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder itself doesn't weigh anything
# Desired output should be give in kg and rounded to two decimal places

# 1. Calculate volume of cylinder
# 2. Convert cm into dm
# 3. 1dm = 1L, 1L is 1Kg

import math

def weight(r, h):
    cylinder_vol = math.pi * r**2 * h
    decimeters3 = cylinder_vol * .001
    return round(decimeters3, 2)

weight(4, 10)
weight(30, 60)
weight(15, 10)





# V = Bh
# V = pi * r^2 * h