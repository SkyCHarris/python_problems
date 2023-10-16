
#! Triangle and Parallelogram Area Finder

# Write a function that accepts base(decimal), height(decimal), and shape('triangle', 'parallelogram') as input and calculates the area of that shape

def area_shape(base, height, shape):
    if shape == "triangle":
        return 0.5 * base * height
    elif shape == "parallelogram":
        return base * height
    
area_shape(2, 3, "triangle")
area_shape(8, 6, "parallelogram")