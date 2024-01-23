
#! Sum of Odd and Even Numbers

# Write funciton that takes list of numbers and returns a list with 2 elements:

# First element should be the sum of all even numbers in the list
# Second element should be sum of odds

def sum_odd_and_even(lst):
    evens_sum = 0
    odds_sum = 0
    for i in lst:
        if i % 2 == 0:
            evens_sum += i
        elif i % 2 != 0:
            odds_sum += i
    return [evens_sum, odds_sum]

sum_odd_and_even([1, 2, 3, 4, 5, 6])
sum_odd_and_even([-1, -2, -3, -4, -5, -6])
sum_odd_and_even([0, 0])
