
#! Vowel Sandwich

# Create a function which validates whether a 3 character string is a vowel sandwich
# In order to have a valid sandwhich, the string must:

# The first and last characters
# The character in the middle must be a vowel

import re

def is_vowel_sandwich(s):
    vowelsRegex = re.compile(r'[aeiou]')
    consonantsRegex = re.compile(r'[b-df-hj-np-tv-xz]')
    vowel = vowelsRegex.findall(s)
    consonant = consonantsRegex.findall(s)
    if s[0] and s[-1] == consonant and s[1] == vowel:
        return True
    else:
        return False

is_vowel_sandwich("cat")
is_vowel_sandwich("ear")
is_vowel_sandwich("bake")
is_vowel_sandwich("try")

# Attempt 2

import re

def is_vowel_sandwich(s):
    vowelsRegex = re.compile(r'[aeiou]')
    vowels = vowelsRegex.findall(s)
    consonantsRegex = re.compile(r'[b-df-hj-np-tv-xz]')
    consonants = consonantsRegex.findall(s)
    if str(vowels[0]) == s[1] and str(consonants[0]) == s[0] and str(consonants[-1] == s[-1]):
        return True
    else:
        return False


is_vowel_sandwich("cat")
is_vowel_sandwich("ear")
is_vowel_sandwich("bake")
is_vowel_sandwich("try")

# Attempt 3

import re

def is_vowel_sandwich(s):
    vowels = re.findall(r'[aeiouy]', s)
    consonants = re.findall(r'[b-df-hj-np-tv-xz]', s)
    if s[1] == vowels[0] and s[0] == consonants[0] and s[-1] == consonants[-1]:
        return True
    else:
        return False

is_vowel_sandwich("cat")
is_vowel_sandwich("ear")
is_vowel_sandwich("bake")
is_vowel_sandwich("try")