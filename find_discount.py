
#! Find the Discount

# Create a function that takes two arguments:
    # The original price and the discount percentage as integers
# Then return the final price after the discount

def dis(price, discount):
    discount_decimal = discount * .01
    discount_cash = discount_decimal * price
    final_cost = price - discount_cash
    return round(final_cost, 2)

dis(1500, 50)
dis(89, 20)
dis(100, 75)

discount = 1500 * (100 - 50) * 0.01
print(discount)