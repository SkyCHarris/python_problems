# Create a function that calculates the area of a rectangle
# If the argumnents are invalid, your funciton must return -1

def area(side1, side2):
    if side1 + side1 <= 0 or side2 + side2 < 0:
        return -1
    else:
        return side1 * side2
    
area(3, 4)
area(10, 11)
area(-1, 5)
area(0, 2)