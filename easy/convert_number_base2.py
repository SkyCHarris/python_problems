
#! Convert a Number to Base-2

# Create function that returns base-2 (binary) repr of a base-10 (decimal) string #


def binary(num):
    binary = bin(num)
    no_prefix_bin = [x for x in num[2, -1]]


# Attempt 2
    
def binary(num):
    binary = bin(num)
    no_prefix_bin = binary[2:]
    return no_prefix_bin

binary(1)
binary(5)
binary(10)