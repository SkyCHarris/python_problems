
#! Even or Odd: Which is Greater?

# Create a function to determine if the sum of all the individual even digits are greater than the sum of all the individual odd digits in a string of numbers

def even_or_odd(s):
    even_list = []
    odd_list = []
    for element in s[0:-1]:
        if element % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(even_list)
    print(odd_list)

even_or_odd("22471")
even_or_odd("213613")
even_or_odd("23456")

# Attempt 2

def even_or_odd(s):
    even_list = []
    odd_list = []
    for i in s:
        if int(i) % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    if sum(even_list) > sum(odd_list):
        print("Even is greater than Odd")
    elif sum(odd_list) > sum(even_list):
        print("Odd is greater than Even")
    elif sum(odd_list) == sum(even_list):
        print("Even and Odd are the same")
            

even_or_odd("22471")
even_or_odd("213613")
even_or_odd("23456")