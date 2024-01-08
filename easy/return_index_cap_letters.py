
#! Return the Index of All Capital Letters

# Create a function that takes a single string as argument and returns an ordered list
# containing the indices of all capital letters in the string

def index_of_caps(word):
    index_list = []
    cap_index = 0
    for i in word:
        if i.isupper() == True:
            cap_index += i.index()
            index_list.append(cap_index)
    return index_list

index_of_caps("eDaBiT")

# Attempt 2

def index_of_caps(word):
    caps_string = ''
    for i in word:
        if i.isupper() == True:
            caps_string += i

# Attempt 3
            
def index_of_caps(word):
    return [i for i, c in enumerate(word) if c.isupper()]

index_of_caps("eDaBiT")


    
