
#! Half, Quarter, and Eigth

# Create a funciton that takes a number and returns a list of three numbers: 
    # Half of the number, quarter of the number, and eigth of the number

def half_quarter_eighth(num):
    half = num / 2
    quarter = num / 4
    eigth = num / 8
    return list[(half, quarter, eigth)]

half_quarter_eighth(6)
half_quarter_eighth(22)
half_quarter_eighth(25)

# Attempt 2

def half_quarter_eighth(num):
    return list[(num/2, num/4, num/8)]

half_quarter_eighth(6)
half_quarter_eighth(22)
half_quarter_eighth(25)

# Actual (don't need list function(method?) added to code)

def half_quarter_eighth(num):
    return [num/2, num/4, num/8]

half_quarter_eighth(6)
half_quarter_eighth(22)
half_quarter_eighth(25)