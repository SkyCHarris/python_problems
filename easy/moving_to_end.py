
#! Moving to the End

# Write a function that moves all elements of one type to the end of the list

def move_to_end(lst, num):
    end_list = []
    for i in lst:
        if i == num:
            end_list.append(i)
    return end_list

move_to_end([1, 3, 2, 4, 4, 1], 1)
move_to_end([7, 8, 9, 1, 2, 3, 4], 9)

# Attempt 2

def move_to_end(lst, num):
    i, j = 0, 0
    while j < len(lst):
        if lst[j] != num:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        j += 1
    return lst

move_to_end([1, 3, 2, 4, 4, 1], 1)
move_to_end([7, 8, 9, 1, 2, 3, 4], 9)