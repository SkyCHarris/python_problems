
#! Clone a List

# The Code tab has code which attempts to add a clone of a list to itself
# No error message, but results aren't as intended
# Fix code!

# Bugged
def clone(lst):
	lst.append(lst)
	return lst

clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])

# Fix
def clone(lst):
	for i in range(len(lst)):
		lst.append(lst[i])
		return lst
	
clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])

# Fix 2

def clone(lst):
	a = lst
	b = list(a)
	c = [a, b]
	return c

clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])

# Fix 3

def clone(lst):
	a = lst
	b = lst(a)
	c = a.append(b)

clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])

# Fix 4

def clone(lst):
	list_copy = []
	for item in lst: 
		lst.append(item)
		return list_copy

clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])

# Fix 5

def clone(lst):
	a = lst
	b = list(a)
	c = [a, b]
	return c

clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])

# Fix 6

def clone(lst):
	b = []
	for i in range(lst):
		lst.append(b)
	return lst

clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])

# Fix 7

def clone(lst):
	for x in lst:
		lst.append(lst)
		return lst
	
clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])

# Actual

def clone(lst):
	new_lst = [lst]
	return lst + new_lst

clone([1, 1])
clone([1, 2, 3])
clone(["x", "y"])