
#! Sum of Evenly Divisible Numbers from a Range

# Create a function that takes three arguments a, b, c...
    # ...and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive

def evenly_divisible(a, b, c):
    num_range = range(a, b+1)
    total = 0
    for i in num_range:
        if c % i == 0:
            total = total + i
        i += i
        return total
    

evenly_divisible(1, 10, 20)
evenly_divisible(1, 10, 2)
evenly_divisible(1, 10, 3)

# Actual

def evenly_divisible(a, b, c):
    total = 0
    for i in range(a, b+1):
        if i % c == 0:
            total = total + i
    return total

evenly_divisible(1, 10, 20)
evenly_divisible(1, 10, 2)
evenly_divisible(1, 10, 3)