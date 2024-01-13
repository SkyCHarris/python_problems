
#! Chat Room Status

# Write a function that returns the # of users in a chatroom:

# 1. Nobody -> "no one online"
# 2. 1 Person -> "user1 online"
# 3. 2 People -> "user1 and user2 online"
# 4. n>2 People -> first 2 names and add "and n-2 more online"

def chatroom_status(users):
    excess_users = len(users) - 2
    if len(users) == 0:
        return "no one online"
    elif len(users) == 1:
        return "{} online".format(users[0])
    elif len(users) == 2:
        return "{} and {} online".format(users[0], users[1])
    elif len(users) > 2:
        return "{}, {} and {} more online".format(users[0], users[1], excess_users)
    
chatroom_status([])
chatroom_status(["paRIE_to"])
chatroom_status(["s234f", "mailbox2"])
chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])