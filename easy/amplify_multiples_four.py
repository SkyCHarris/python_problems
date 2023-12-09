
#! Amplify the Multiples of Four

# Create a functin that takes an int and returns a list from 1 to n, where:

# 1. If # can be divided evenly by 4, amplify it by 10 (return 10x the #)
# 2. If # cannot be divided evenly by 4, return the #

def amplify(num):
    amplist = []
    for i in range(1, num+1):
        if i % 4 == 0:
            i *= 10
        amplist.append(i)
    return amplist

amplify(4)
amplify(3)
amplify(25)

# Attempt 2

def amplify(num):
    return [i for i in range(1, num+1) if i % 4 == 0]

amplify(4)
amplify(3)
amplify(25)

# Actual (condensed)

def amplify(num):
    return [i if i % 4 != 0 else i * 10 for i in range(1, num+1)]

amplify(4)
amplify(3)
amplify(25)
