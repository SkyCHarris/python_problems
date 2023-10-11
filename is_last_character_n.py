
#! Is the Last Character an "N"?

# Create a function that takes a string (a random name). 
# If the last character of the name is an "n", return True, otherwise return False

def is_last_character_n(name):
    return name.endswith("n")

is_last_character_n("Aiden")
is_last_character_n("Piet")
is_last_character_n("Bert")
is_last_character_n("Dean")