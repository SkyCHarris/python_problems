
#! Shuffle the Name

# Create a function that takes a string (person's first and last name) and returns a string with the first and last name swapped

def name_shuffle(name):
    split_name = name.split()
    return split_name[-1] + ' ' + split_name[0]

name_shuffle("Donald Trump")
name_shuffle("Rosie O'Donnell")
name_shuffle("Seymour Butts")