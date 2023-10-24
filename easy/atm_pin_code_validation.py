
#! ATM PIN Code Validation

# ATM machines allow 4 or 6 digit PIN codes
# PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits
# Create a function that takes a string and returns True if the PIN is valid and False if it's not

def is_valid_PIN(pin):
    return pin.isdigit() and len(pin) == 4 or len(pin) == 6

is_valid_PIN("1234")
is_valid_PIN("12345")
is_valid_PIN("a234")
is_valid_PIN("")