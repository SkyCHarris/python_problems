
#! Instant Jazz

# Create a function which concatenates the number 7 to the end of every chord in a list
# Ignore all chords which already end with 7

def jazzify(list):

    newList = []

    for i in list:
        if i.endswith("7") == True:
            newList.append(i)
        elif i.endswith("7") == False:
            i = i + "7"
            newList.append(i)
        elif list == []:
            return []
            
    return newList
        
jazzify(["G", "F", "C"])
jazzify(["Dm", "G", "E", "A"])
jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])
jazzify([])