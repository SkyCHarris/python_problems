
#! Century Crisis

# Scientists have discovered that in four decades the earth will explode!
# It will take three decades to make a spaceship to travel to a new planet that can hold the entire world population

# Calculate the number of people there will be in three decades from now
    # -The variable p is the world population now
    # -Assume that every month, someone gives birth to more people nP

# Return the number of people there will be when the spaceship is complete

def future_people(p, nP):
    return p + (nP * 30 * 12)

future_people(256, 2)
future_people(3248, 6)
future_people(5240, 3)