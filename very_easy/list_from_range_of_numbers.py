
#! List From a Range of Numbers

# Create a function that returns a list of all the integers between two given numbers start and end

def range_of_num(start, end):
    if start != end:
        return list(range(start + 1, end))
    elif start == end:
        return []

range_of_num(2, 4)
range_of_num(5, 9)
range_of_num(2, 11)