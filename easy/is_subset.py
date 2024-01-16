
#! Is One List a Subset of Another?

# Create a function that returns True if the first list is a subset of the second
# Return False otherwise

def is_subset(lst1, lst2):
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    return lst1_set.issubset(lst2_set)

is_subset([3, 2, 5], [5, 3, 7, 9, 2])
is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6])
is_subset([1, 2], [3, 5, 9, 1])