
#! Find the Odd Integer

# Create a function that takes a list and finds the integer which appears an odd number of times

def find_odd(lst):
    listcount = [lst.count(x) for x in lst for i in listcount if i % 2 != 0 return x]

find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])

# Attempt 2

def find_odd(lst):
    for i in lst:
        count = 0
        for j in lst:
            if lst[i] == lst[j]:
                count += 1
        if (count % 2 != 0):
            return lst[i]
        
    return -1

find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])

# Attempt 3

from collections import Counter

def find_odd(lst):
    counter_dict = Counter(lst)
    for i in counter_dict:
        if counter_dict[i] % 2 != 0:
            return counter_dict[i]

find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
find_odd([10])

# Attempt 4

from collections import Counter

def find_odd(lst):
    counter_dict = Counter(lst)
    for i in counter_dict:
        if counter_dict[i] % 2 != 0:
            return i

find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
find_odd([10])