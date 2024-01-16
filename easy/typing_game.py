
#! Typing Game

# Create a function that takes in two lists:
    # 1. User-typed words
    # 2. Correctly-typed words
# ..and outputs a list containing 1s (correctly-typed words) and -1s (incorrectly-typed words)

'''
User-typed: ["cat", "blue", "skt", "umbrells", "paddy"]
Correct: ["cat", "blue", "sky", "umbrella", "paddy"]

Output: [1, 1, -1, -1, 1]
'''

def correct_stream(user, correct):
    answer_list = []
    for i in user:
        if i == j:
            answer_list.append(1)
        elif i != j:
            answer_list.append(-1)
    return answer_list

correct_stream(
  ["it", "is", "find"],
  ["it", "is", "fine"]
)

# Attempt 2

def correct_stream(user, correct):
    answer_list = []
    answer_tuple = zip(user, correct)
    for i, j in answer_tuple:
        if i == j:
            answer_list.append(1)
        if i != j:
            answer_list.append(-1)
    return answer_list

correct_stream(
  ["it", "is", "find"],
  ["it", "is", "fine"]
)

correct_stream(
  ["april", "showrs", "bring", "may", "flowers"],
  ["april", "showers", "bring", "may", "flowers"]
)

# Condensed (incorrect)

def correct_stream(user, correct):
    answer_tuple = zip(user, correct)
    # answer_list = [1 for i == j in else -1 for i!= j answer_tuple]
    return answer_list

correct_stream(
  ["it", "is", "find"],
  ["it", "is", "fine"]
)

correct_stream(
  ["april", "showrs", "bring", "may", "flowers"],
  ["april", "showers", "bring", "may", "flowers"]
)