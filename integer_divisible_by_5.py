# Create a function that returns True if an integer is evenly divisble by 5, and False otherwise

def divisible_by_five(num):
    if num % 5 == 0:
     return True
    else:
       return False
    
divisible_by_five(5)
divisible_by_five(-55)
divisible_by_five(37)