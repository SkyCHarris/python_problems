# Create a function that takes a string: let's say that the front is the first three characters of the string
# If string length is less than three characters, the front is whatever is there
# Return a new string, which is three copies of the front

def front3(string):
    slice = string[0:3]
    if len(string) < 3:
        return string * 3
    else:
        return slice * 3
    
front3("Python")
front3("Cucumber")
front3("bioshock")