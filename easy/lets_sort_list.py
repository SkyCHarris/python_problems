
#! Let's Sort This List!

# Create a function that takes a list of numbers lst, and a string s
# Return a list of numbers as per:

# 1. "Asc" returns in ascending order
# 2. "Des" returns in descending order
# 3. "None" returns list without modifications

def asc_des_none(lst, s):
    if s == "Asc":
        return sorted(lst)
    elif s == "Des":
        return sorted(lst, reverse=True)
    elif s == "None":
        return lst
    
asc_des_none([4, 3, 2, 1], "Asc")
asc_des_none([7, 8, 11, 66], "Des")
asc_des_none([1, 2, 3, 4], "None")