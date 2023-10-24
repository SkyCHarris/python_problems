
#! Xs and Os, Nobody Knows

# Create a function that takes a string:
    # Checks if it has the same number of "x's" and "o's"
    # Returns True or False

def XO(txt):
    lower_case = txt.lower()
    if lower_case.count("x") or lower_case.count("o") == 0:
        return True
    else:
        return lower_case.count("x") == lower_case.count("o")
    
XO("ooxx")
XO("xooxx")
XO("ooxXm")
XO("zpzpzpp")
XO("zzoo")

# Attempt 2

def XO(txt):
    txt.lower()
    if 'x' not in txt and 'o' not in txt:
        return True
    else:
        return txt.count('x') == txt.count('o')
    
XO("ooxx")
XO("xooxx")
XO("ooxXm")
XO("zpzpzpp")
XO("zzoo")

# Attempt 3

def XO(txt):
    lowered = txt.lower()
    if 'x' not in lowered and 'o' not in lowered:
        return True
    else:
        return lowered.count('x') == txt.count('o')
    
XO("ooxx")
XO("xooxx")
XO("ooxXm")
XO("zpzpzpp")
XO("zzoo")
