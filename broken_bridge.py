
#! Broken Bridge

# Create a function which validates whether a bridge is safe to walk on (has no gaps)

def is_safe_bridge(s):
    return not '' in s

is_safe_bridge("####")
is_safe_bridge("## ####")
is_safe_bridge("#")

# Actual

def is_safe_bridge(s):
    return not ' ' in s

is_safe_bridge("####")
is_safe_bridge("## ####")
is_safe_bridge("#")