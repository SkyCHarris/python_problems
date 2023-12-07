
#! Nested Loops

# A while loop in a while loop
# A for loop in a for loop
# A while loop in a for loop
# etc.

# Let's display the numbers 1-9 using a loop
# 2nd parameter 'end' allows you to put the print results on the same line (default is /n newline)

for x in range(1, 10):
    print(x, end="")

# What if we want to print this 3 times?
# Could create another loop

for x in range(1,4):    # Code in this loop will be executed 3x
    for y in range(1, 10):
        print(y, end="")
    print()     # Prints each outer loop iteration to a new line

#? Project: Print a rectangle made of a symbol that we set
    # User types in how many rows and columns

rows = int(input("Enter the # of rows:"))
columns = int(input("Enter the # of columns:"))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()