# Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them

def convert(hours, minutes):
    seconds = (hours * 3600) + (minutes * 60)
    print(seconds)
    return seconds

convert(1, 3)
convert(2, 0)
convert(0, 0)

