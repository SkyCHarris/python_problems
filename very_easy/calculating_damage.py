
#! Calculating Damage

# Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time

def damage(dmg, spd, time):
    if time == "second":
        return dmg * spd
    elif time == "minute":
        return dmg * spd * 60
    elif time == "hour":
        return dmg * spd * 60 * 60
    elif dmg < 0 or spd < 0:
        return "invalid"
    
damage(40, 5, "second")
damage(100, 1, "minute")
damage(2, 100, "hour")
