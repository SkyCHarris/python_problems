
#! Multiples of 3 or 5

# ....

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        elif number <= 0:
            return 0
    return sum

solution(4)
solution(6)
solution(16)
solution(15)