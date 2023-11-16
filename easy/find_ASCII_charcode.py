
#! Find ASCII Charcode of Inverse Case Character

# Create a function that takes a single character as an argument
    # ...and returns the char code of its lowercased / uppercased counterpart

# def counterpartCharCode(str):
#     charcode = chr(str)


# Attempt 2

def counterpartCharCode(letter):
    if letter.lower() == letter:
        return ord(letter.upper())
    elif letter.upper() == letter:
        return ord(letter.lower())
    elif letter.isalpha() == False:
        return ord(letter)
    
counterpartCharCode("A")
counterpartCharCode("a")