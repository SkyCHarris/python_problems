
#! Add the Index

# Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself
# So you add 0 to the number at index 0, 1 to the number at index 1, etc.

def add_indexes(lst):
    new_list = []
    for index, value in enumerate(lst):
        paired = index + value
        new_list.append(paired)
    return new_list

add_indexes([1, 2, 3, 4, 5])

# Condensed

def add_indexes(lst):
    return [index+value for index, value in enumerate(lst)]