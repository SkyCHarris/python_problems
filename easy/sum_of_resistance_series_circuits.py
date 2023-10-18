
#! Sum of Resistance in Series Circuits

# When resistors are connected together in a series...
# ...the same current passes through each resistor in the chain
# The total resistance, RT, of the circuit must be equal to the sum of all the individual resistors added together

# RT = R1 + R2 + R3

# Create a function that takes an array of values resistance that are connected in series, and calculates the total resistance of the circuit in ohms.
# The ohm is the standard unit of electrical resistance in the International System of Units (SI)

def series_resistance(resistance):
    return "The total resistance (RT) is " + str(sum(resistance)) + ' ohms'

series_resistance([1, 5, 6, 3])
series_resistance([16, 3.5, 6])
series_resistance([0.5, 0.5])

# Attempt 2 (syntax thing)

def series_resistance(resistance):
    rt = sum(resistance)
    if rt <= 1:
        return str(rt) + ' ohm'
    else:
        return str(rt) + ' ohms'

series_resistance([1, 5, 6, 3])
series_resistance([16, 3.5, 6])
series_resistance([0.5, 0.5])