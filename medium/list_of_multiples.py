
#! List of Multiples

# Create a function that takes 2 numbers as args. (num, length) 
# ...and returns a list of multiples of num until the list length reaches length

def list_of_multiples(num, length):
    new_list = []
    for i in range(length):
        return [x * x for x in num]

    
list_of_multiples(7, 5)
list_of_multiples(12, 10)
list_of_multiples(17, 6)

# Attempt 2 (GPT)

def list_of_multiples(num, length):
    multiples_list = []
    current_num = num

    while len(multiples_list) < length:
        multiples_list.append(current_num)
        current_num += num

    return multiples_list

list_of_multiples(7, 5)
list_of_multiples(12, 10)
list_of_multiples(17, 6)