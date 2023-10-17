# Create a function that returns how many possible arrangements can come from a certain number of switches (on / off)
# For a given number of switches, how many different patterns of on and off can we have?

def pos_com(switches):
    if switches == 1:
        return switches + 1
    else:
        return 2 ** switches
    
pos_com(1)
pos_com(3)
pos_com(10)

# Attempt 2

def pos_com(switches):
    return 2**switches