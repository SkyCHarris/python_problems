
#! Automorphic Numbers

# A number n is automorphic if n^2 ends in n.

# ex. n = 5, n^2 = 25

# Create a function that takes a number and returns True if the number is automorphic, False if not

def is_automorphic(n):
    n_product = n**2
    n_str = str(n_product)
    return n_str.endswith(str(n))

is_automorphic(5)
is_automorphic(8)
is_automorphic(76)