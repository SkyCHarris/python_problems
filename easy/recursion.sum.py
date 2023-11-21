
#! Recursion: Sum

# Write a function that finds the sum of the first n natural numbers
# Make your function recursive

def sum_numbers(num):
    if num <= 1:
        return 1
    else:
        return num + sum_numbers(num - 1)
    
sum_numbers(5)
sum_numbers(1)
sum_numbers(12)