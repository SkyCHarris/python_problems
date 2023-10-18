
#! Invert Colors

# Create a function that inverts the rgb values of a given tuple

def color_invert(rgb):
    list_rgb = list(rgb)
    rgb1 = 255 - list_rgb[0]
    rgb2 = 255 - list_rgb[1]
    rgb3 = 255 - list_rgb[2]
    tuple_rgb = (rgb1, rgb2, rgb3)
    return tuple_rgb

color_invert((255, 255, 255))
color_invert((0, 0, 0))
color_invert((165, 170, 221))