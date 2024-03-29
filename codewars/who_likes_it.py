
#! Who Likes It?

# Implement function that takes an array containing names of people that like an item.
# Return the display text as shown in the examples:

# ex. "jacob and Alex like this"

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names) -2} others like this'
    
likes([])
likes(["Peter"])
likes(["Jacob", "Alex"])
likes(["Alex", "Jacob", "Mark", "Max"])