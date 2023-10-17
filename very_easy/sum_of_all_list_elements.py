# Create a function that takes a list and returns the sum of all numbers in the list

# Attempt
def get_sum_of_elements(list):
    for i in range(len(list)):
        sum = i + i
        print(sum)
        return sum
    
get_sum_of_elements([2, 7, 4])

# Actual (1)
def get_sum_of_elements(lst):
    return sum(lst)

# Actual (2)
def get_sum_of_elements(lst):
    sum = 0
    for i in lst:
        sum = sum + 1
        return sum

get_sum_of_elements([2, 7, 4])