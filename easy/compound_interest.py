
#! Compound Interest

# Suppose that you invest $10k for 10 years at an interest rate of 6% compounded monthly
# What will be the value of the investment at the end of the 10 year period?

# Create a function that accepts the principal (p), term in years (t), interest rate (r), and number of compounding periods per year (n)
# The function returns the value at the end of the term rounded to the nearest cent

def compound_interest(p, t, r, n):
    return round(p * (1 + r/n) ** (n * t), 2)

compound_interest(10000, 10, 0.06, 12)
compound_interest(100, 1, 0.05, 1)
compound_interest(3500, 15, 0.1, 4)
compound_interest(100000, 20, 0.15, 365)