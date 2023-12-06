
#! List Comprehensions

# An easier and more readable way to create a list
# Best way to learn is first showing what it looks like in for loop

nums = [1,2,3,4,5,6,7,8,9,10]

# For loop
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# I want 'n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = [n for n in nums]
print(my_list)

# First n -> what we're returning
# For n -> for loop

# I want 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = [n*n for n in nums]
print(my_list)

# Using a map + lambda
    # map runs everything in the list through a certain function
    # lambda is an anon. function
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = map(lambda n: n*n, nums)
print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

# for loop
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

# list comp.
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)


#? Dictionary Comprehensions

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman,', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(zip(names, heroes))

# I want a dict{'name': 'hero'} for each name, hero in zip(names, heros)

# for loop
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman,', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print(my_dict)

# dictionary comp.
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman,', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

# If name not equal to Peter
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman,', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)


#? Set Comprehensions

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)


# set comp.
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = {n for n in nums}
print(my_set)