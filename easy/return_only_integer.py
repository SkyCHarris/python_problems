
#! Return Only the Integer

# Write a function that takes a list of elements and returns only the integers

def return_only_integers(lst):
    int_list = []
    for i in lst:
        if i.isdecimal():
            int_list.append()
    return int_list

return_only_integers([9, 2, "space", "car", "lion", 16])


# Attempt 2

def return_only_integers(lst):
    int_list = []
    for i in lst:
        if type(i) == int:
            int_list.append(i)
    return int_list

return_only_integers([9, 2, "space", "car", "lion", 16])