
#! Word without First Character

# Create a function that takes a word and returns the new word without including the first character

def new_word(word):
    return word.replace([0], '')

new_word("apple")
new_word("cherry")
new_word("plum")

# Attempt 2

def new_word(word):
   return word.replace(word[0], '')

new_word("apple")
new_word("cherry")
new_word("plum")

# Actual

def new_word(word):
    return word[1: ]
