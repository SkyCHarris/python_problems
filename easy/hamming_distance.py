
#! Hamming Distance

# Hamming distance is the # of characters that differ between two strings

# String1: "abcbba"
# String2 = "abcbda"

# Hamming Distance: 1 = "b" vs. "d" is the only difference

# Create a function for this

#TODO: THIS IS CORRECT
def hamming_distance(txt1, txt2):
    count = 0
    mapped = list(zip(txt1, txt2))
    for i, j in mapped:
        if i != j:
            count += 1
    return count
    

hamming_distance("abcde", "bcdef")
hamming_distance("abcde", "abcde")
hamming_distance("strong", "strung")


# Attempt 2

def hamming_distance(txt1, txt2):
    count = 0
    for i, j in txt1, txt2:
        if i == j:
            count += 1
    return count

hamming_distance("abcde", "bcdef")
hamming_distance("abcde", "abcde")
hamming_distance("strong", "strung")

# Test

def hamming_distance(txt1, txt2):
    count = 0
    for i in txt1:
        print(i)

hamming_distance("abcde", "bcdef")
hamming_distance("abcde", "abcde")
hamming_distance("strong", "strung")

# Attempt 3

def hamming_distance(txt1, txt2):
    count = 0
    mapped = list(zip(txt1, txt2))
    for i in mapped:
        print(i[0])

hamming_distance("abcde", "bcdef")
hamming_distance("abcde", "abcde")
hamming_distance("strong", "strung")

