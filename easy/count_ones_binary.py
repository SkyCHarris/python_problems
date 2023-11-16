
#! Count Ones in Binary Representation of Integer

# Count the amount of ones in the binary representation of an integer
# Ex. 12 is 1100 in binary, return value should be 2

def count_ones(int):
    binary = bin(int)
    print("Binary count equals:" + str(binary.count("1")))

count_ones(0)
count_ones(100)
count_ones(999)

# Condensed

def count_ones(int):
    binary = bin(int)
    return binary.count("1")

count_ones(0)
count_ones(100)
count_ones(999)