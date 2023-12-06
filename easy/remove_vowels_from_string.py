
#! Remove Every Vowel from a String

# Create a function that takes a string and returns a new string with all vowels removed

import re

def remove_vowels(txt):
    thing_list = re.sub(r'[aeiouAEIOU]', '', txt)
    return thing_list

remove_vowels("I have never seen a thin person drinking Diet Coke.")
remove_vowels("We're gonna build a wall!")
remove_vowels("Happy Thanksgiving to all--even the haters and losers!")

# Condensed

import re

def remove_vowels(txt):
    return re.sub(r'[aeiouAEIOU]', '', txt)