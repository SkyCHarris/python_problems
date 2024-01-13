
#! Transform into a List with No Duplicates

# A set is a collection of unique items
# A set can be formed from a list by removing all duplicate items

def setify(lst):
    return sorted(set(lst))

setify([1, 3, 3, 5, 5])
setify([4, 4, 4, 4])
setify([5, 7, 8, 9, 10, 15])
setify([3, 3, 3, 2, 1])