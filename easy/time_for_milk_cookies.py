
#! Is it Time for Milk and Cookies?

# Let's prep some milk and cookies for Santa
# Create a function that accepts a date object and returns True if it's Christmas Eve and False otherwise

import datetime

def time_for_milk_and_cookies(date):
    return date == datetime.date(date.year, 12, 24)

time_for_milk_and_cookies(datetime.date(2013, 12, 24))
time_for_milk_and_cookies(datetime.date(2013, 1, 23))
time_for_milk_and_cookies(datetime.date(3000, 12, 24))

# Attempt 2

import datetime

def time_for_milk_and_cookies(date):
    return date.month == 12 and date.day == 24

time_for_milk_and_cookies(datetime.date(2013, 12, 24))
time_for_milk_and_cookies(datetime.date(2013, 1, 23))
time_for_milk_and_cookies(datetime.date(3000, 12, 24))

