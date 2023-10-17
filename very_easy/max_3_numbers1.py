def num_max(x, y, z) :
    if z <= x >= y :
        return x
    elif x <= z >= y :
        return z
    elif x <= y >= z :
        return y
    
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
num3 = float(input("Enter num3:"))

highest_num = num_max(num1, num2, num3)
print(highest_num)

# Not working
