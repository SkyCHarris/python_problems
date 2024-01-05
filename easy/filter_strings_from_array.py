
#! Filter out Strings from an Array

# Create a function that takesx a list of non-negative integers and strings and return a new list without the strings

def filter_list(lst):
    new_list = []
    for i in lst:
        if type(i) is int:
            new_list.append(i)
    return new_list

filter_list([1, 2, "a", "b"])