# Write a function to check if a list contains a particular number

def check(list, el):
    return el in list

check([1, 2, 3, 4, 5], 3)
check([1, 1, 2, 1, 1], 3)
check([5, 5, 5, 6], 5)