
#! Purge and Organize

# Given a list of nums, write function that returns a list that:

# 1. Has all duplicate elements removed
# 2. Is sorte4d from least to greatest value

def unique_sort(lst):
    return sorted(set(lst))

unique_sort([1, 2, 4, 3])
unique_sort([1, 4, 4, 4, 4, 3, 2, 1, 2])
unique_sort([6, 7, 3, 2, 1])