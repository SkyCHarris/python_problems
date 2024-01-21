
#! Find the Odd Int

# Given array of integers, find the one that appears an odd number of times

def find_it(seq):
    result = 0
    for num in seq:
        result ^= num
    return result

# Example usage
find_it([1, 2, 3, 2, 1, 3, 5])

