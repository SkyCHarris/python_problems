
#! Stand in Line

# Write a function that takes a list and a number as arguments
# Add the number to the end of the list, then remove the first element of the list
# The function should return the updated list
# For an empty list input, return: "No list has been selected"

def next_in_line(lst, num):
    if len(lst) == 0:
        return "No list has been selected"
    elif len(lst) != 0:
        lst.append(num)
        del lst[0]
        return lst

next_in_line([5, 6, 7, 8, 9], 1)
next_in_line([7, 6, 3, 23, 17], 10)
next_in_line([1, 10, 20, 42], 6)
next_in_line([], 6)