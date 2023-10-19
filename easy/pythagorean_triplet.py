
#! Pythagorean Triplet

# Create a function that validates whether three given integers form a Pythagorean Triplet
# The sum of the squares of the two smallest integers must equal the square of the largest number to be validated

def is_triplet(n1, n2, n3):
    sorted_list = sorted([n1, n2, n3])
    add_square_smallest = sorted_list[0]**2 + sorted_list[1]**2
    square_largest = sorted_list[2]**2
    return add_square_smallest == square_largest

is_triplet(3, 4, 5)
is_triplet(13, 5, 12)
is_triplet(1, 2, 3)
