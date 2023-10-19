
#! End Corona

# Create a funciton that takes:
    # The number of daily average recovered cases 'recovers', daily average 'new cases', current 'active cases'
    # Return the number of days it will take to reach zero cases
import math

def end_corona(recovers, new_cases, active_cases):
    daily_case_diff = recovers - new_cases
    days = 0 
    while daily_case_diff * days < active_cases:
        days += 1
    return math.ceil(days)
        

    
end_corona(4000, 2000, 77000)
end_corona(3000, 2000, 50699)
end_corona(30000, 25000, 390205)

