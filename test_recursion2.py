
# https://www.youtube.com/watch?v=ngCos392W4w

#? Write a recursive function that given an input n sums all nonnegative integers up to n

# 1. What's the simplest possible input for the function? (Base Case)
    # sum(0) = 0
    # Simplest case is base case.
    # Base Case is only input where we provide explicit answer
    # All other solutions to the problem will build on the base case
# 2. Play around with examples and visualize

def numsum(n):
    if n == 0:
        return 1
    else:
        return (n * numsum(n + 1))
    
numsum(5)