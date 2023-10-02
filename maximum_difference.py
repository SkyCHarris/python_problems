# Given a list of integers, return the difference between the largest and smallest integers in the list

def max_difference(list):
    min_sum = min(list)
    max_sum = max(list)
    return max_sum - min_sum