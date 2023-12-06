
#! List Operation

# Create a function that takes three parameters where:

# x is the start of the range (inclusive)
# y is the end of the range (inclusive)
# n is the divisor to be checked against

# Return an ordered list with numbers in the range that are divisible by the third paramater n
# Return an empty list if there are no numbers divisble by n

def list_operation(x, y, n):
    ordered_list = []
    for i in range(x, y+1):
        if n % i == 0:
            ordered_list.append(i)
            ordered_list.sort()
    return ordered_list

list_operation(1, 10, 3)
list_operation(7, 9, 2)
list_operation(15, 20, 7)

# Attempt 2

def list_operation(x, y, n):
    ordered_list = []
    for i in range(x, y+1):
        if i % n == 0:
            ordered_list.append(i)
            ordered_list.sort()
    return ordered_list

list_operation(1, 10, 3)
list_operation(7, 9, 2)
list_operation(15, 20, 7)