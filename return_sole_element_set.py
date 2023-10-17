
#! Return Sole Element in a Set

# Given a set containing one element, return the element

def element_from_set(s):
    set_form = set(s)
    return set_form.pop()

element_from_set({"edabit"})
element_from_set({True})
element_from_set({11037})