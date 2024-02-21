
#! Robot Path

# Robot is navigated by series of N, E, S, W commands
# Each command moves the robot one step in the given direction
# Robot is designed for only two destinations:

# 1. e, n, e, e, n
# 2. w, n, w, n, w, w, n

# Create function that takes list of commands and returns True if the robot reaches any of the destinations

# n = 1
# s = -1
# e = 2
# w = -2

def robot_path(lst):
    sum = 0
    dest1 = 8
    dest2 = -5
    for i in lst:
        if i == "n":
            sum += 1
        elif i == "s":
            sum += -1
        elif i == "e":
            sum += 2
        elif i == "w":
            sum += -2
    return sum == dest1 or sum == dest2

robot_path(["s", "e", "e", "n", "n", "e", "n"])
robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"])
robot_path(["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", "n"])