
#! Find the Highest Integer in the List Using Recursion

# Create function that finds highest integer in the list using recursion

def find_highest(lst):
    if len(lst[0]) == 1:
        return lst[0]
    else:
        return max(lst[0], find_highest(lst[1:]))
    
find_highest([-1, 3, 5, 6, 99, 12, 2])