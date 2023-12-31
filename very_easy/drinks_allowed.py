
#! Drinks Allowed?

# A bartender is writing a simple program to determine whether he should serve drinks to someone
# He only serves drinks to people 18 and older and when he's not on break

# Given the person's age, and whether break time is in session, create a function that returns whether he should serve drinks

def should_serve_drinks(age, on_break):
    return age >= 18 and not on_break

should_serve_drinks(17, True)
should_serve_drinks(19, False)
should_serve_drinks(30, True)