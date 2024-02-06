
#! Right Shift by Division

# Write a function that mimics the right shift operator and returns the result from two given integers

def shift_to_right(x, y):
    return x // 2**y

shift_to_right(80, 3)
shift_to_right(-24, 2)
shift_to_right(-5, 1)
shift_to_right(4666, 6)
shift_to_right(3777, 6)
shift_to_right(-512, 10)