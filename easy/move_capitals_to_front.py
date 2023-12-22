
#! Move Capital Letters to the Front

# Create a function that moves all capital letters to the front of a word

import re

def cap_to_front(str):
    capRegex = re.compile(r'[a-z]')
    capMatch = capRegex.findall(str)
    print(capMatch)

cap_to_front("hApPy")
cap_to_front("moveMENT")
cap_to_front("sh0rtCAKE")


# Attempt 2

def cap_to_front(str):
    final = ''
    lst_short = [x for x in sorted(str)]
    for i in lst_short:
        final += i
    return final

cap_to_front("hApPy")
cap_to_front("moveMENT")
cap_to_front("sh0rtCAKE")

# Attempt 3

def cap_to_front(str):
    newstr = ''
    for i in str:
        if i.isupper():
            newstr += i
        for i in str:
            if i.islower():
                newstr += i
    return newstr

cap_to_front("hApPy")
cap_to_front("moveMENT")
cap_to_front("sh0rtCAKE")


# Attempt 4

def cap_to_front(str):
    lowers = ''
    uppers = ''
    for i in str:
        if i.islower():
            lowers += i
        elif i.isupper():
            uppers += i
    return uppers + lowers

cap_to_front("hApPy")
cap_to_front("moveMENT")
cap_to_front("sh0rtCAKE")