
#! Make My Way Home

# You will be given a list showing how far James travels away from his home for each day
# He may choose to travel towards or away from his house, so negative values are to be expected

# Create a function that calculates what distance James must walk to get back home

def distance_home(lst):
    return abs(sum(lst))

distance_home([2, 4, 2, 5])
distance_home([-1, -4, -3, -2])
distance_home([3, 4, -5, -2])