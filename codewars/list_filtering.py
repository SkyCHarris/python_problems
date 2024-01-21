
#! List Filtering

# Create function that takes list of non-negative integers and strings and returns new list with strings filtered out

def filter_list(l):
    new_list = []
    for i in l:
        if isinstance(i, int) == True:
            new_list.append(i)
    return new_list

filter_list([1,2,'a','b'])
filter_list([1,'a','b',0,15])
filter_list([1,2,'aasf','1','123',123])