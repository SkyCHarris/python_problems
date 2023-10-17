# Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function

# Outputs the # of r's, as determined by parameter, in the word "burp"
def long_burp(letters):
    string = str(letters)
    string_mult = string * letters
    list_string = list(string_mult)
    list_string[0, -1] = 'r'
    burp = "Bu" + string_mult + "p"
    return burp

long_burp(3)
long_burp(5)
long_burp(9)

# Attempt 2

def long_burp(letters):
    letters_list = range(letters)
    letters_list[0,-1] = "r"
    return letters_list

    # burp = "Bu" + __ + "p"

long_burp(3)
long_burp(5)
long_burp(9)

