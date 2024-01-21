
#! Regex Validate PIN Code

# ATM mahcines allow 4 or 6 digit PIN codes. Must be digits.

# If the function is passed a valid PIN string, return True. Else, False.

import re

def validate_pin(pin):
    pattern = re.compile(r'^\d{4}$|^\d{6}$')
    return bool(pattern.match(pin))

validate_pin("1234")
validate_pin("12345")
validate_pin("a234")

# GPT No. 2

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False

validate_pin("1234")
validate_pin("12345")
validate_pin("a234")