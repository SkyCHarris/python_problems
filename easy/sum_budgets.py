
#! Get Sum of People's Budget

# Create the function that takes list of dictionaries and returns the sum of people's budgets

# def get_budgets(lst):
#     budget_sum = 0
#     for key, value in lst:
#         if key == "budget":
#             budget_sum += value
#     return budget_sum

# get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ])

# Attempt 2

# def get_budgets(lst):
#     budget_sum = 0
#     for i in lst:
#         lst.get("budget")
#         budget_sum += i
#     return budget_sum

# get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ])

# Attempt 3

def get_budgets(lst):
    sum = 0
    for i in lst:
        for value in i:
            print(value[2])

get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
])

# Attempt 4

def get_budgets(lst):
    sum = 0
    for i in lst:
        print(i["budget"])

get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
])

# Attempt 5

def get_budgets(lst):
    sum = 0
    for i in lst:
        sum += i["budget"]
    return sum

get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
])