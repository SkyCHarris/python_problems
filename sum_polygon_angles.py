# Given an n-sided regular polygon 'n', return the total sum of internal angles (in degrees)

def sum_polygon(n):
    polygon_angle_sum = (n-2) * 180
    print(polygon_angle_sum)
    return polygon_angle_sum

sum_polygon(3)
sum_polygon(4)
sum_polygon(6)