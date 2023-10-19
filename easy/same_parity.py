
#! Same Parity

# Create a function that takes a number as input and returns True if the sum of its digits has the same parity as the entire number
# Otherwise return False

def parity_analysis(num):
    if num % 2 == 0 and sum(range(num)) % 2 == 0:
        return True
    elif num % 2 != 0 and sum(range(num)) % 2 != 0:
        return False
    
# Attempt 2

def parity_analysis(num):
    return num % 2 == 0 and sum(range(num)) % 2 == 0

parity_analysis(243)
parity_analysis(12)
parity_analysis(3)

# Attempt 3

def parity_analysis(num):
    return sum(range(num))

parity_analysis(243)
parity_analysis(12)
parity_analysis(3)

# Attempt 4

def parity_analysis(num):
    result = num
    while result > 0:
        for i in range(num):
            i = i + i
            result = result * i
    return result

parity_analysis(243)
parity_analysis(12)
parity_analysis(3)

# Attempt 5

def parity_analysis(num):
    sum = 0
    for i in str(num):
        sum += int(i)
        if sum % 2 == 0 and num % 2 == 0:
            return True
        elif sum % 2 != 0 and num % 2 != 0:
            return True
        elif sum % 2 == 0 and num % 2 != 0:
            return False
        elif sum % 2 != 0 and num % 2 == 0:
            return False

parity_analysis(243)
parity_analysis(12)
parity_analysis(3)

# Attempt 6

def parity_analysis(num):
    sum = 0
    for i in str(num):
        sum += int(i)
        return sum % 2 == 0 and num % 2 == 0
    
parity_analysis(243)
parity_analysis(12)
parity_analysis(3)