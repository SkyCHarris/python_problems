# You are counting points for a basketball game. 
# Given the amount of 3-pointers scored and 2-pointers scored, find the final points for the team and return that value

def total_points(twos, threes):
    twos = twos * 2
    threes = threes * 3
    print (threes + twos)
    return threes + twos

total_points(1, 1)
total_points(7, 5)
total_points(38, 8)