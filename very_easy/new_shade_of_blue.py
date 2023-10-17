
#! I'd Like a New Shade of Blue, Please

# I have a bucket containing an amount of navy blue paint, and would like to paint as many walls as possible
# Create a funciton that returns the number of complete walls that I can paint before needing to go to the shop to buy more

# n is the number of square meters i can paint
# w and h are the widths and heights of a single wall in meters

def how_many_walls(n, w, h):
    if w*h < n:
        return n // (w*h)
    elif w*h > n:
        return 0
    
how_many_walls(100, 4, 5)
how_many_walls(10, 15, 12)
how_many_walls(41, 3, 6)