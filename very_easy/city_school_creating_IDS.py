
#! City School Creating IDs

# Many IDS (for emails or Google ID) are created using the person's name

# Create a function that will return a four-character ID using the person's first name and last name
# The first character will be the first letter of the first name but in lowercase
# The next three characters will be the first three characters of the last name, but the first letter will be capitalized and the other two will be in lower case

def create_Id(firstName, lastName):
    firstInitial = firstName.lower([0])
    lastThree = lastName.upper[0] + lastName.lower[1,2]
    return firstInitial + lastThree

create_Id("mary", "lamb")
create_Id("John", "SMITH")
create_Id("mary", "smith")

# Attempt 2

def create_id(firstName, lastName):
    firstInitial = firstName[0]
    lastOne = lastName[0]


# Attempt 3

def create_id(firstName, lastName):
    lowercase_id = firstName[0] + lastName[0,1,2]
    return lowercase_id
    
create_id("mary", "lamb")
create_id("John", "SMITH")
create_id("mary", "smith")