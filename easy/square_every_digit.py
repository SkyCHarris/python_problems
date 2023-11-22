
#! Square Every Digit

# Create a function that squares every digit of a number

def square_digits(num):
    squared_str = ''
    num_str = str(num)
    for i in num_str:
        squared_num = i ** 2
    
square_digits(9119)
square_digits(2483)
square_digits(9414)

# Attempt 2

def square_digits(num):
    num_str = str(num)
    for i in num_str:
        squared_str = ''.join(i**2)
    return squared_str

square_digits(9119)
square_digits(2483)
square_digits(9414)

# Attempt 3

def square_digits(num):
    squared_str = ''
    num_str = str(num)
    for i in num_str:
        i = i**2
        squared_str += i
    return squared_str

square_digits(9119)
square_digits(2483)
square_digits(9414)

def square_digits(num):
    squared_str = ''
    num_str = str(num)
    for i in num_str:
        i = int(i)**2
        squared_str = squared_str + str(i)
    return int(squared_str)

square_digits(9119)
square_digits(2483)
square_digits(3212)