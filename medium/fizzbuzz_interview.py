
#! FizzBuzz Interview Question

# Create a functino that takes a number as an argument and returns "Fizz", "Buzz", or "FizzBuzz"

# - If number is mult of 3, output = "Fizz"
# - If number is mult of 5, output = "Buzz"
# - If number is mult of both 3 and 5, output = "FizzBuzz"
# - If not mult of 3 or 5, output itself
# - Output should always be a string even if it is not a multiple of 3 or 5

def fizz_buzz(num):
    if  num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
    
fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(4)