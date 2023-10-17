# A vehicle needs 10 times the amount of fuel than the distance it travels.
# However, it must always carry a minimum of 100 fuel before setting off

# Create a function which calculates the amount of fuel it needs, given the distance

def fuel_needed(distance):
    gas_total = distance * 10
    if gas_total < 100:
        return gas_total + 100

    elif gas_total > 100:
        return gas_total
      
fuel_needed(15)
fuel_needed(23.5)
fuel_needed(3)


# Attempt 2

def calculate_fuel(distance):
    gas_total = distance * 10
    if gas_total < 100:
        return gas_total + 100
    else:
        return gas_total
    
fuel_needed(15)
fuel_needed(23.5)
fuel_needed(3)

# Attempt 3

def calculate_fuel(distance):
    if distance < 10:
        return 100
    else:
        return distance * 10
    
calculate_fuel(15)
calculate_fuel(23.5)
calculate_fuel(3)