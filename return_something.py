# Write a function that returns the string "something" joined with a space " " and the given argument 'a'"

def give_me_something(something):
    phrase = "something" + " " + something
    print(phrase)
    return phrase

give_me_something("is better than nothing")
give_me_something("Bob Jane")
give_me_something("something")