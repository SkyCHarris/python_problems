
#! Convert Kilometers to Miles

# In this challenge, you have to implement a function that returns the given distance kilometers converted into miles
# Round up to the fifth decimal digit

def km_to_miles(km):
    return round(km * 0.621371, 5)

km_to_miles(2)
km_to_miles(6)
km_to_miles(8)