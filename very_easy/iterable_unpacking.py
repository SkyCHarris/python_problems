
#! Iterable Unpacking

# There's an easy way to assign to array values to the nth index by using the Rest element

head, tail = [1, 2, 3, 4]
print(head) -> 1
print(tail) -> 2

# But how to make tail = [2, 3, 4] instead of tail = 2?

head, *tail = [1, 2, 3, 4]
print(head)
print(tail)