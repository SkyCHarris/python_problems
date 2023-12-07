
#! Conver to Decimal Notation

# Create a function to convert a list of percentages to their decimal equivalents

def convert_to_decimal(perc):
    striplist = [float(x.strip('%')) * .01 for x in perc]
    return striplist

convert_to_decimal(["1%", "2%", "3%"])
convert_to_decimal(["33%", "98.1%", "56.44", "100%"])