
#! Letters Only

# Write a function that removes any non-letters from a string, returning a well-nown film title

import re

def letters_only(str):
    new_str = ''
    for i in str:
        if i.isalpha():
            new_str += i
    return new_str

letters_only("R!=:~0o0./c&}9k`60=y")
letters_only("^,]%4B|@56a![0{2m>b1&4i4")
letters_only("^U)6$22>8p).")

# Attempt 2

import re

def letters_only(str):
    lettersRegex = re.compile(r'[A-Za-z]')
    mo = lettersRegex.findall(str)
    return ''.join(mo)

letters_only("R!=:~0o0./c&}9k`60=y")
letters_only("^,]%4B|@56a![0{2m>b1&4i4")
letters_only("^U)6$22>8p).")