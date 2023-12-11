
#! Excel in Python

# Open spreadsheet using load_workbook() method
# Use active to select the first sheet available
# use cell to select the cell by passing the row and column parameter

import openpyxl


# Open workbook
# Create workbook object
wb = openpyxl.load_workbook("mann_whitney/datafile.xlsx")

# Get the first sheet
first_sheet = wb.worksheets[0]

data_column = []

for row in first_sheet:
    name = row[0].value
    data_column.append(name)

print(data_column)
    