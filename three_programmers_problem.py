
#! The 3 Programmers Problem

# You hired three programmers
# Create a function that takes three numbers and returns the difference between highest and lowest paid programmers

def programmers(wage1, wage2, wage3):
    wage_list = [wage1, wage2, wage3]
    min_progammer = min(wage_list)
    max_programmer = max(wage_list)
    wage_diff = max_programmer - min_progammer
    return wage_diff

programmers(147, 33, 526)
programmers(33, 72, 74)
programmers(1, 5, 9)