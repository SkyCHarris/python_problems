
#! CAPS LOCK DAY is over!

# Every sentence should be lowercase. Let's normalize a sentence

# Create a function tha ttake sa string. If all uppercase char, convert to lowercase and add exclamation mark

def normalize(txt):
    if txt.isupper():
        lowered = txt.lower()
        capitalized = lowered.capitalize()
        return capitalized + "!"
    else:
        return txt
    
normalize("CAPS LOCK DAY IS OVER")
normalize("Today is not caps lock day.")
normalize("Let us stay calm, no need to panic.")