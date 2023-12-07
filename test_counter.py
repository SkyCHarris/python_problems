
#! Python Counter

# Counting several repeated objects at once is a common programming problem
# Python has solutions. This one is "Pythonic"

# -Count several repeated objects at once
# -Create counters with Python's Counter
# -Retrieve most common objects in a counter
# -Update object counts
# -Use Counter to facilitate further computations

# To count several different objects at once you can use a Python dictionary
# Dictionary keys will store the objects you want to count
# Dictionary values will hold the number of repetitions, or the 'count'

# Count letters in the word 'Mississippi'

word = 'mississippi'
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

counter

# dict.get()

word = 'mississippi'
counter = {}

for letter in word:
    counter[letter] = counter.get(letter, 0) + 1

counter

# When calling .get() this way you get the current count of a given letter, or (0 by default) if the letter is missing
# Then i9ncrement the count by 1 and store it under the corresponding letter in the dictionary

# defaultdict

from collections import defaultdict

word = "mississippi"
counter = defaultdict(int)

for letter in word:
    counter[letter] += 1

counter

# More concise and readable
# Initilize the counter using a defaultdict with int() as a default factory function
# When you access a key taht doesn't exist in the underlying defaultdict, the dictionary automatically creates the key and initializes it with the value that the factory function returns