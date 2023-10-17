
#! Is the Word Singular or Plural?

# Create a function that takes in a word and determines whether or not it is plural
# A plural word is one that ends in"s"

def is_plural(word):
    return word.endswith('s')

is_plural("changes")
is_plural("change")
is_plural("dudes")
is_plural("magic")