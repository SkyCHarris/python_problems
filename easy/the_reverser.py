
#! The Reverser!

# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case

def reverse(txt):
    reversed = txt[::-1]
    return reversed.swapcase()

reverse("Hello World")
reverse("ReVeRsE")
reverse("Radar")