
#! Get the Area of a Country

# Create a function that takes a country's name and area as arguments...
# ...and returns the area of the country's proportion of the total world's landmass
# Total world landmass = 148,940,000 km^2

def area_of_country(name, area):
    landmass_perc = area / 148_940_000 * 100
    return f"{name} is {landmass_perc:%.2} of the total world's landmass"

area_of_country("Russia", 17098242)
area_of_country("USA", 9372610)
area_of_country("Iran", 1648195)

# Attempt 2

def area_of_country(name, area):
    landmass_perc = (area / 148_940_000) * 100
    return "{} is {:.3}% the total world's landmass".format(name, landmass_perc)

area_of_country("Russia", 17098242)
area_of_country("USA", 9372610)
area_of_country("Iran", 1648195)

# Attempt 3 (Correct, edabit no f.strings)

def area_of_country(name, area):
    landmass_perc = area / 148940000
    return f"{name} is {landmass_perc:.2%} of the total world's landmass"

area_of_country("Russia", 17098242)
area_of_country("USA", 9372610)
area_of_country("Iran", 1648195)

# Attempt 4 (format version)

def area_of_country(name, area):
    landmass_perc = area / 148940000
    return "{} is {:.2%} of the total world's landmass".format(name, landmass_perc)

area_of_country("Russia", 17098242)
area_of_country("USA", 9372610)
area_of_country("Iran", 1648195)
