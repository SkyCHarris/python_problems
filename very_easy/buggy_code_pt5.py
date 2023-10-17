
#! Buggy Code (Part 5)

# Mubashir created an infinite loop!
# Help him fix the code to pass the challenge


# New (debugged)

def print_list(n):
	for i in range(len(n)):
		return i
	
print_list(1)
print_list(3)
print_list(6)

# Attempt 2

def print_list(n):
	result=[]
	i=1
	while i<=n:
		result+=[i]
		i += 1
	return result

print_list(1)
print_list(3)
print_list(6)