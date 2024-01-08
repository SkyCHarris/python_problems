
#! Even Number Generator

# Using list comprehensions, create a function that finds all even numbers from 1 to the given number

def find_even_nums(num):
    return [x for x in range(1, num+1) if x % 2 == 0]

find_even_nums(8)
find_even_nums(4)
find_even_nums(2)