
#! Vowel Replacer

# Create a function that replaces all the vowels in a string with a specified character

def replace_vowels(str, char):
    if 'a' or 'e' or 'i' or 'o' or 'u' in str:
        str.replace("")

# Attempt 2

import re

def replace_vowels(str, char):
    return re.sub('a', char, str), re.sub('e', char, str), re.sub('i', char, str), re.sub('o', char, str), re.sub('u', char, str)

replace_vowels("the aardvark", "#")
replace_vowels("minnie mouse", "?")
replace_vowels("shakespeare", "*")

# Attempt 3

import re

def replace_vowels(str, char):
    str_list = list(str)
    for letter in str_list:
        if letter == 'a' or 'e' or 'i' or 'o' or 'u':
            return re.sub(letter, char, str)

replace_vowels("the aardvark", "#")
replace_vowels("minnie mouse", "?")
replace_vowels("shakespeare", "*")

# Actual

import re

def replace_vowels(str, char):
    return re.sub(r'[aeiouAEIOU]', char, str)

replace_vowels("the aardvark", "#")
replace_vowels("minnie mouse", "?")
replace_vowels("shakespeare", "*")