
#! Luke, I Am Your...

# Luke Skywalker has family and friends. Help him remind them who is who.
# Given a string with a name, return the relation of that person to Luke

def relation_to_luke(name):
    starwars_family = {'Darth Vader': 'father', 'Leia': 'sister', 'Han': 'brother in law', 'R2D2': 'droid'}
    if name == starwars_family.keys():
        return starwars_family.values()
    
relation_to_luke("Darth Vader")
relation_to_luke("Leia")

# Actual

def relation_to_luke(name):
    starwars_family = {'Darth Vader': 'father', 'Leia': 'sister', 'Han': 'brother in law', 'R2D2': 'droid'}

    for k,v in starwars_family.items():
        if k == name:
            msg = "Luke, I am your " + v + "."
            return msg

relation_to_luke("Darth Vader")
relation_to_luke("Leia")