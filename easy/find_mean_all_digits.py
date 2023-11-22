
#! Find the Mean of All Digits

# Create a function that returns the mean of all digits

def mean(num):
    num_sum = 0
    num_str = str(num)
    for i in num_str:
        num_sum += i
    temp_mean = num_sum / len(num)
    return temp_mean

mean(42)
mean(12345)
mean(666)

# Attempt 2

def mean(num):
    num_sum = 0
    num_str = str(num)
    for i in num_str:
        num_sum = int(num_str) + int(i)
        temp_mean = num_sum / len(str(num))
    return temp_mean
                
mean(42)
mean(12345)
mean(666)

# Attempt 3

def mean(num):
    num_sum = 0
    num_str = str(num)
    for i in num_str:
        num_sum = int(i) + num_sum
        temp_mean = num_sum / len(str(num))
    return temp_mean

mean(42)
mean(12345)
mean(666)