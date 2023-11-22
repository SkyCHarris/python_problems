
#! "EdaBit" Challenge

# Create a function that returns the list of numbers from a given range
# But for multiples of 3, return "Eda" instead of the number
# For multiples of 5, return "Bit"
# For numbers that are multiples of 3 and 5, return "EdaBit"

def eda_bit(start, end):
    edabit_list = []
    num_range = range(start, end + 1)
    for i in num_range:
        if i % 3 == 0 and i % 5 == 0:
            edabit_list.append("EdaBit")
        elif i % 3 == 0:
            edabit_list.append("Eda")
        elif i % 5 == 0:
            edabit_list.append("Bit")
        
        else:
            edabit_list.append(i)
    return edabit_list

eda_bit(0,10)
eda_bit(14,20)
eda_bit(99,106)
