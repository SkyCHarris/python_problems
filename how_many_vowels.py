
#! How Many Vowels?

# Create a function that takes a string and returns the number (count) of vowels contained within it

def count_vowels(txt):
    if 'a' 'e' 'i' 'o' or 'u' in txt:
        return txt.count()
    
# Attempt 2

def count_vowels(txt):
   return txt.count('a') + txt.count('e') + txt.count('i') + txt.count('o') + txt.count('u')