# In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds these three species:

# Chickens = 2 legs
# Cows = 4 legs
# Pigs = 4 legs

# The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a funcion that returns the total number of legs of all the animals


def animals(chickens, cows, pigs):
    chickens = chickens * 2
    cows = cows * 4
    pigs = pigs * 4
    total_legs = chickens + cows + pigs
    print(total_legs)
    return total_legs

animals(2, 3, 5)
animals(1, 2, 3)
animals(5, 2, 8)
