
#! Destructuring Assignment

# You can assign variables from lists like this:

lst = [1, 2, 3, 4, 5, 6, 7, 8]
first = lst[0]
second = lst[1]
third = lst[2]
other = lst[3:]

print(first) # outputs 1
print(second) # outputs 2
print(third) # outputs 3
print(other) # outputs [4, 5, 6, 7, 8]

# Create variables first, second, third, and other from the given list using Destructuring Assignment

def writeyourcodehere = [1, 2, 3, 4, 5, 6, 7, 8]

#* Solution
first, second, third, *other = [1, 2, 3, 4, 5, 6, 7, 8]
print(first)
print(second)
print(third)
print(other)