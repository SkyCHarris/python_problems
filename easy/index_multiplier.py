
#! Index Multiplier

# Return the sum of all items in a list, where each item is m ultiplied by its index (zero-based)
# For empty lists, return 0

def index_multiplier(lst):
    print(list(enumerate(lst)))

index_multiplier([1,2,3,4,5])
index_multiplier([-3,0,8,-6])

# Attempt 2

def index_multiplier(lst):
    sum = 0
    for i, j in enumerate(lst):
        sum += i*j
    return sum

index_multiplier([1,2,3,4,5])
index_multiplier([-3,0,8,-6])