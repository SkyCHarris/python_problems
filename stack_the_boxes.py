
#! Stack the Boxes

# Here's an image of four models. Some of the cubes are hidden behind other cubes
# Model one consists of one cube. Model two consists of four cubes, and so on...

# Write a function that takes a number n and returns the number of stacked boxes in a model n levels high, visible and invisible

def stack_boxes(n):
    return n * n

stack_boxes(1)
stack_boxes(2)
stack_boxes(0)
stack_boxes(3)
stack_boxes(4)