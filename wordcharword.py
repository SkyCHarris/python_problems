
#! WordCharWord

# Create a function that will put the first argument, a character, between every word in the second argument, a string

def add(char, txt):
    if ' ' in txt:
       ' ' = char
       return ' ' = char


# Attempt 2

def add(char, txt):
    return txt.replace(" ", char)

add("R", "python is fun")
add("#", "hello world!")
add("#", " ")