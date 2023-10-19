
#! Hiding the Card Number

# Write a function that takes a credit card number and only displays the last four characters
# The rest of the card number must be replaced by ************

def card_hide(card):
    last_four = card[-1:-4]

# Attempt 2

def card_hide(card):
    remove()
    card.rjust(4, '*')

# Attempt 3

def card_hide(card):
    remove(card[-4:])

card_hide("1234123456785678")
card_hide("8754456321113213")