# Given a list of numbers, return True if the sum of the values in the list is less than 100
# Otherwise return False

def list_less_than_100(list):
    if (list[0] + list[-1]) < 100:
        return True
    else:
        return False

list_less_than_100([5, 57])
list_less_than_100([77, 30])
list_less_than_100([0])

# Attempt 2

def list_less_than_100(list):
    list_sum = sum(list)
    if list_sum < 100:
        return True
    else:
        return False
    
list_less_than_100([5, 57])
list_less_than_100([77, 30])
list_less_than_100([0])