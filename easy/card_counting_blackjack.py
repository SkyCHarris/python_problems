
#! Card Counting (BlackJack)

# In BlackJack, cards are counted with -1, 0, 1 values:
    # - 2,3,4,5,6 are counted as +1
    # - 7,8,9 are counted as 0
    # - 10, J, Q, K, A are counted as -1

# Create a function that counts the number and returns it from the list of cards provided

def count(lst):
    num_sort = [n for n in range(lst) if n > 1 if n < 7]
    return num_sort

count([5, 9, 10, 3, "J", "A", 4, 8, 5])
count(["A", "A", "K", "Q", "Q", "J"])
count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7])

# Attempt 2

def count(lst):
    count = 0
    for n in range(lst):
        if 1 < n > 7:
            count = count + 1
        elif n > 6 and n < 10:
            count
        elif n == 10 or "J" or "Q" or "K" or "A":
            count = count - 1
    return count

count([5, 9, 10, 3, "J", "A", 4, 8, 5])
count(["A", "A", "K", "Q", "Q", "J"])
count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7])

# Actual 1

def count(deck):
    return sum([1 if str(i) in '23456' else -1 if str(i) in 'AKQJ10' else 0 for i in deck])

count([5, 9, 10, 3, "J", "A", 4, 8, 5])
count(["A", "A", "K", "Q", "Q", "J"])
count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7])
