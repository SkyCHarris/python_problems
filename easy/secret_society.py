
#! Secret Society

# Group of friends started a secret society.
# Name will be the first letter of each of their names, sorted in alphabetical order

# Create a function that takes in a list of names and returns the name of the secret society

def society_name(name_list):
    joined_names = ''
    sorted_names = name_list.sort()
    for i in sorted_names:
        first_letter = str(i[0])
        joined_names.join(first_letter)

        return first_letter
    
society_name(["Adam", "Sarah", "Malcom"])


# Attempt 2

def society_name(friends):
    sorted_names = friends.sort()
    return sorted_names

society_name(["Adam", "Sarah", "Malcom"])
society_name(["Harry", "Newt", "Luna", "Cho"])

# Attempt 3

def society_name(friends):
    friends.sort()
    team_name = ''
    for i in friends:
        team_name += i[0]
    return team_name

society_name(["Adam", "Sarah", "Malcom"])
society_name(["Harry", "Newt", "Luna", "Cho"])

# Condensed (taken from Edabit)

def society_name(friends):
    return ''.join(sorted(i[0] for i in friends))

society_name(["Adam", "Sarah", "Malcom"])
society_name(["Harry", "Newt", "Luna", "Cho"])