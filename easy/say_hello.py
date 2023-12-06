
#! Say Hello to Guests

# Take a list of names
# Add 'Hello' to every name
# Make one big string with all greetings

def greet_people(names):
    names_string = ''
    names_list = []
    for name in names:
        name = 'Hello ' + str(name) + ','
        names_list.append(name)
    return str(names_list)

greet_people(["Joe"])
greet_people(["Angela", "Joe"])

# Attempt 2

def greet_people(names):
    names_list = []
    for name in names:
        names_list.append(name)
        names_string = 'Hello'.join(names_list) + ', '
    return names_string

greet_people(["Joe"])
greet_people(["Angela", "Joe"])

# Attempt 3

def greet_people(names):
    names_list = []
    if names == []:
        return ""
    elif len(names) < 2:
        return "Hello " + names[0]
    else:
        for name in names:
            name = "Hello " + str(name) + ","
            names_list.append(name)
            names_string = ' '.join(names_list)
        return names_string

greet_people(["Joe"])
greet_people(["Angela", "Joe"])
greet_people(["Frank", "Angela", "Joe"])

# Attempt 4

def greet_people(names):
    names_list = []
    if names == []:
        return ""
    elif len(names) == 1:
        return "Hello " + names[0]
    else:
        for name in names:
            names_list.append(name)
            names_string = 'Hello' + ''.join(names_list) + ','
        return names_string

greet_people(["Joe"])
greet_people(["Angela", "Joe"])
greet_people(["Frank", "Angela", "Joe"])

# Attempt 5

def greet_people(names):
    names_list = []
    if names == []:
        return ""
    elif len(names) == 1:
        return 'Hello ' + names[0]
    else:
        for name in names:
            name = 'Hello ' + name
            names_list.append(name)
        return ', '.join(names_list)
    
greet_people(["Joe"])
greet_people(["Angela", "Joe"])
greet_people(["Frank", "Angela", "Joe"])

#* the .append() method can take additional parameters, such as a string format.
#* ex.:
    #