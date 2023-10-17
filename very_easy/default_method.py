
#! Default Mood

# Create a function that takes in a current mood and return a sentence:
    # "Today, I am feeling {mood}"
# If no argumnet is passed, return "Today, I am feeling neutral"

def mood_today(mood = "neutral"):
    return "Today, I am feeling " + mood

mood_today("happy")
mood_today("sad")
mood_today()