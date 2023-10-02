# Create a function that takes three arguments 'prob, prize, pay' and returns True if prob * prize > pay
# Otherwise return False

def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    else:
        return False
    

profitable_gamble(0.2, 50, 9)