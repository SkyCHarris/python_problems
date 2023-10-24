
#! Alphabet Soup

# Create a function that takes a string and returns a string with its letters in alphabetical order

def alphabet_soup(word):
    sorted_list = sorted(word)
    return ''.join(sorted_list)

alphabet_soup("hello")
alphabet_soup("edabit")
alphabet_soup("hacker")
alphabet_soup("geek")
alphabet_soup("javascript")