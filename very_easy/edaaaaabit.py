
#! Edaaaaabit

# Write a function that takes an integer and returns a string with the given number of "a"s in Edabit

def how_many_times(num):
    num_as = num * 'a'
    return 'Ed' + num_as + 'bit'

how_many_times(5)
how_many_times(0)
how_many_times(12)

# Alternative 1

def how_many_times(num):
    text = "Edabit"
    return text.replace("a", "a"*num)

how_many_times(5)
how_many_times(0)
how_many_times(12)