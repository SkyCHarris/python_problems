
#! Probabilities (Part 1)

# Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list
# The probability should be expressed as a percentage, rounded to one decimal place

def probability(lst, n):
    total_outcomes = len(lst)
    count = 0
    fav_outcomes = 0
    for i in lst:
        if i >= n:
            count = count + 1
            fav_outcomes = count
    return round(100 * (fav_outcomes / total_outcomes), 1)

probability([5, 1, 8, 9], 6)
probability([7, 4, 17, 14, 12, 3], 16)
probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6)
