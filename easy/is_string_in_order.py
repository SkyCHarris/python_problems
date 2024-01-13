
#! Is the String in Order?

# Create a function that takes a string and returns True or False depending on whether the characters are in order or not

def is_in_order(txt):
    return txt == ''.join(sorted(txt))

is_in_order("abc")
is_in_order("edabit")
is_in_order("123")
is_in_order("xyzz")