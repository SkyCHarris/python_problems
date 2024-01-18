
#! Profit Margin

# Calculate the profit margin given cost_price and sales_price.
# Return the result as a % formatted string, and round to one decimal
# To calculate profit margin, subtract the cost from the sales price, then divide by sales price

def profit_margin(cost_price, sales_price):
    pre_profit = (sales_price - cost_price) / sales_price
    # return f'{pre_profit: .1%}'
    return "{:.1%}".format(pre_profit)

profit_margin(50, 50)
profit_margin(28, 39)
profit_margin(33, 84) 