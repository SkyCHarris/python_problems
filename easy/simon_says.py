
#! Simon Says

# Take in 2 lists, return True if 2nd list follows first list by 1 element, and False otherwise
# aka determine if the 2nd list is the first lift shifted to the right by 1

def simon_says(lst1, lst2):
    zipped = zip(lst1, lst2)
    lst1_slice = slice(0)
    lst2_slice = slice(1)

# Attempt 2
    
def simon_says(lst1, lst2):
    lst1.pop(-1)
    return lst1 == lst2[1:]

simon_says([1, 2], [5, 1])
simon_says([1, 2], [5, 5])
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])