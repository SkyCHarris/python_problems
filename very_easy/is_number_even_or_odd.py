
#! Is the Number Even or Odd?

# Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers

def isEvenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
isEvenOrOdd(3)
isEvenOrOdd(146)
isEvenOrOdd(19)