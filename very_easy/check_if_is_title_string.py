
#! Check If It's a Title String

# Check if a string txt is a title text or not. 
# A title text is one which ahs all the words in the text start with an upper case letter

def check_title(txt):
    return txt == txt.title()

check_title("A Mind Boggling Achievement")
check_title("A Simple Python Program!")
check_title("Water is transparent")