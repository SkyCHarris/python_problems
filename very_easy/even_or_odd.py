
#! Even or Odd?

# Givena list o integers, determine whether the sum of its elements is even or odd.
# The return value should be a string("odd" or "even")
# If the input list is empty, consider it as a list with a zero([0])

def even_or_odd(lst):
    if sum(lst) % 2 == 0:
        return "even"
    else:
        return "odd"

even_or_odd([0])
even_or_odd([1])
even_or_odd([])
even_or_odd([0, 1, 5])