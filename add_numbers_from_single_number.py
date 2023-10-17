
#! Add up the Numbers from a Single Number

# Create a function that takes a number as an argument
# Add up all the numbers from 1 to the number you passed to the function

def addUp(num):
   result = 0
   for i in range(num):
      print(i + i)

addUp(10)
addUp(13)
addUp(600)

# Attempt 2

def addUp(num):
   numberRange = range(num)
   i = 0
   while i <  
