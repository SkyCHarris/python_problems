
#! Stuttering Function

# Write a function that stutters a word as if someone is struggling to read it
# The first two letters are repeated twice with an ellipsis ... and space after each, then the word is pronounced with a question mark ?

def stutter(word):
    stutter_word = 2 *(word[0] + word[1] + '...' + ' ') + word + '?'
    return stutter_word

stutter("incredible")
stutter("enthusiastic")
stutter("outstanding")